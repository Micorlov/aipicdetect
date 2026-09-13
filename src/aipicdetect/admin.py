"""Admin panel: Google sign-in restricted to a single email.

Optional feature. Self-hosted instances that leave ``AIPICDETECT_GOOGLE_CLIENT_ID`` /
``AIPICDETECT_ADMIN_SESSION_SECRET`` unset get a "not configured" page at ``/admin``
instead of an error — nothing else in the app depends on this module.
"""

from __future__ import annotations

import os
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from html import escape
from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse, Response
from google.auth.exceptions import GoogleAuthError, TransportError
from google.auth.transport import requests as google_requests
from google.oauth2 import id_token
from itsdangerous import BadSignature, URLSafeTimedSerializer
from pydantic import BaseModel, Field

from aipicdetect.detect import get_detector
from aipicdetect.limits import DEFAULT_DAILY_LIMIT, MAX_UPLOAD_MB, RESULT_CACHE_LIMIT
from aipicdetect.pages import ASSET_VERSION, render
from aipicdetect.ratelimit import DailyQuota, client_address
from aipicdetect.usage import UsageReport, usage_report

STATIC_DIR = Path(__file__).parent / "static"
ADMIN_DIR = STATIC_DIR / "admin"
HEAD_FILE = ADMIN_DIR / "_head.html"
LOGIN_FILE = ADMIN_DIR / "login.html"
UNCONFIGURED_FILE = ADMIN_DIR / "unconfigured.html"
DASHBOARD_FILE = ADMIN_DIR / "dashboard.html"

CLIENT_ID_ENV = "AIPICDETECT_GOOGLE_CLIENT_ID"
SECRET_ENV = "AIPICDETECT_ADMIN_SESSION_SECRET"
EMAIL_ENV = "AIPICDETECT_ADMIN_EMAIL"
DEFAULT_ADMIN_EMAIL = "micorlov@gmail.com"
MIN_SECRET_LENGTH = 32  # a shorter secret makes the session cookie forgeable; treat as unset

COOKIE_NAME = "aipicdetect_admin"
COOKIE_PATH = "/admin"
SESSION_MAX_AGE = 7 * 24 * 60 * 60
SIGNER_SALT = "aipicdetect-admin-session"
CLOCK_SKEW_SECONDS = 10
LOGIN_ATTEMPTS_PER_DAY = 20
GOOGLE_ISSUERS = frozenset({"accounts.google.com", "https://accounts.google.com"})
CREDENTIAL_MAX_LENGTH = 4096  # real Google ID tokens run ~1-2 KB

STARTED_AT = time.time()
_login_quota = DailyQuota(LOGIN_ATTEMPTS_PER_DAY)

router = APIRouter(include_in_schema=False)


@dataclass(frozen=True)
class AdminConfig:
    client_id: str
    secret: str
    email: str

    @property
    def is_configured(self) -> bool:
        return bool(self.client_id) and bool(self.email) and len(self.secret) >= MIN_SECRET_LENGTH


def admin_config() -> AdminConfig:
    """Admin env vars, read per request (mirrors ``aipicdetect.pages.public_url``)."""
    return AdminConfig(
        client_id=os.environ.get(CLIENT_ID_ENV, "").strip(),
        secret=os.environ.get(SECRET_ENV, "").strip(),
        email=os.environ.get(EMAIL_ENV, DEFAULT_ADMIN_EMAIL).strip().lower(),
    )


def _signer(config: AdminConfig) -> URLSafeTimedSerializer:
    return URLSafeTimedSerializer(config.secret, salt=SIGNER_SALT)


def issue_session(config: AdminConfig, email: str) -> str:
    return _signer(config).dumps(email)


def session_email(config: AdminConfig, token: str) -> str | None:
    """Admin email carried by a cookie value, or ``None`` if unconfigured, absent, tampered,
    expired, or no longer the configured admin (checked live, not just at login)."""
    if not config.is_configured or not token:
        return None
    try:
        decoded = _signer(config).loads(token, max_age=SESSION_MAX_AGE)
    except BadSignature:
        return None
    if not isinstance(decoded, str) or decoded.strip().lower() != config.email:
        return None
    return config.email


def optional_admin(request: Request) -> str | None:
    """Signed-in admin email, or ``None`` — for pages that show a login form instead of erroring."""
    return session_email(admin_config(), request.cookies.get(COOKIE_NAME, ""))


def require_admin(admin: str | None = Depends(optional_admin)) -> str:
    """Guard for any future admin sub-route; 401s instead of falling back to a login page."""
    if admin is None:
        raise HTTPException(status_code=401, detail="admin session required")
    return admin


def is_secure(request: Request) -> bool:
    """True when the browser hop is HTTPS.

    Cloud Run terminates TLS at its front end and ``cli.py`` starts uvicorn without
    ``forwarded_allow_ips``, so ``request.url.scheme`` reads ``http`` in production. Trust
    the last ``X-Forwarded-Proto`` hop (the one Cloud Run's edge itself set — earlier hops
    are client-controlled), mirroring ``ratelimit.client_address``.
    """
    last_hop = request.headers.get("x-forwarded-proto", "").rsplit(",", 1)[-1].strip().lower()
    if last_hop:
        return last_hop == "https"
    return request.url.scheme == "https"


def set_session_cookie(response: Response, request: Request, token: str) -> None:
    response.set_cookie(
        COOKIE_NAME,
        token,
        max_age=SESSION_MAX_AGE,
        path=COOKIE_PATH,
        httponly=True,
        secure=is_secure(request),
        samesite="lax",
    )


def clear_session_cookie(response: Response, request: Request) -> None:
    response.delete_cookie(
        COOKIE_NAME,
        path=COOKIE_PATH,
        httponly=True,
        secure=is_secure(request),
        samesite="lax",
    )


def verify_google_email(credential: str, client_id: str) -> str:
    """Email from a verified Google ID token.

    Raises ``ValueError`` for a token we reject (bad signature/expiry/issuer/audience, or an
    unverified email); ``TransportError`` when Google's certs can't be fetched.
    """
    claims = id_token.verify_oauth2_token(
        credential,
        google_requests.Request(),
        audience=client_id,
        clock_skew_in_seconds=CLOCK_SKEW_SECONDS,
    )
    if claims.get("iss") not in GOOGLE_ISSUERS:
        raise ValueError("unexpected token issuer")
    if not claims.get("email_verified"):
        raise ValueError("Google has not verified this address")
    email = str(claims.get("email", "")).strip().lower()
    if not email:
        raise ValueError("token carries no email claim")
    return email


class Credential(BaseModel):
    credential: str = Field(min_length=1, max_length=CREDENTIAL_MAX_LENGTH)


@dataclass(frozen=True)
class Stat:
    label: str
    value: str


def render_stats(stats: tuple[Stat, ...]) -> str:
    return "".join(f'<div class="stat"><dt>{escape(s.label)}</dt><dd>{escape(s.value)}</dd></div>' for s in stats)


def _result_cache_size() -> int:
    from aipicdetect import server  # deferred: server.py imports this module at startup

    return server.result_cache_size()


def runtime_stats() -> tuple[Stat, ...]:
    detector = get_detector()
    uptime_minutes = int((time.time() - STARTED_AT) // 60)
    return (
        Stat("Detector model", detector.model_name),
        Stat("Detector loaded", "yes" if detector.is_loaded else "still loading"),
        Stat("Uptime", f"{uptime_minutes} min"),
        Stat("Cloud Run revision", os.environ.get("K_REVISION", "local")),
        Stat("Cached results", f"{_result_cache_size()} / {RESULT_CACHE_LIMIT}"),
    )


def quota_stats() -> tuple[Stat, ...]:
    from aipicdetect import server  # deferred: server.py imports this module at startup

    snapshot = server._quota.snapshot()
    return (
        Stat("Daily limit per client", str(server.DAILY_LIMIT) if server._quota.enabled else "disabled"),
        Stat("Clients tracked (24h)", str(snapshot.clients)),
        Stat("Analyses recorded (24h)", str(snapshot.hits)),
        Stat("Admin sign-in attempts today", str(_login_quota.snapshot().hits)),
    )


def config_stats(config: AdminConfig) -> tuple[Stat, ...]:
    return (
        Stat("Max upload size", f"{MAX_UPLOAD_MB} MB"),
        Stat("Result cache limit", str(RESULT_CACHE_LIMIT)),
        Stat("Default daily limit", str(DEFAULT_DAILY_LIMIT)),
        Stat("Admin session secret", "set" if config.secret else "not set"),
    )


def usage_stats(report: UsageReport) -> tuple[Stat, ...]:
    stats: list[Stat] = []
    if report.visitors is None:
        stats.append(Stat("Visitors", f"unavailable: {report.visitors_error}"))
    else:
        stats.extend(Stat(f"Visitors ({v.days} days)", str(v.users)) for v in report.visitors)
        stats.append(Stat(f"Page views ({report.visitors[-1].days} days)", str(report.visitors[-1].page_views)))
    if report.uploads is None:
        stats.append(Stat("Images analyzed", f"unavailable: {report.uploads_error}"))
    else:
        stats.extend(Stat(f"Images analyzed ({w.days} days)", str(w.total)) for w in report.uploads.windows)
    return tuple(stats)


def render_clients(report: UsageReport) -> str:
    """Uploads per client IP over the longest window, busiest first."""
    if report.uploads is None:
        return f'<p class="admin-note">Unavailable: {escape(report.uploads_error or "")}</p>'
    if not report.uploads.clients:
        return '<p class="admin-note">No uploads in this window.</p>'
    rows = "".join(
        f"<tr><td><code>{escape(c.address)}</code></td><td>{c.uploads}</td>"
        f"<td>{escape(c.last_seen.strftime('%Y-%m-%d %H:%M'))} UTC</td></tr>"
        for c in report.uploads.clients
    )
    return f'<table class="clients"><thead><tr><th>Client IP</th><th>Images</th><th>Last upload</th></tr></thead><tbody>{rows}</tbody></table>'


def console_links() -> str:
    """Links to the GCP console, shown only when running on Cloud Run (``K_SERVICE`` set)."""
    service = os.environ.get("K_SERVICE", "").strip()
    if not service:
        return ""
    links = [f'<a href="https://console.cloud.google.com/run/detail/europe-west1/{escape(service)}" rel="noopener">Cloud Run service</a>']
    project = os.environ.get("GOOGLE_CLOUD_PROJECT", "").strip()
    if project:
        links.append(
            f'<a href="https://console.cloud.google.com/billing/budgets?project={escape(project)}" '
            'rel="noopener">Billing budgets</a>'
        )
    return "\n".join(f"<li>{link}</li>" for link in links)


def render_head(title: str) -> str:
    return render(HEAD_FILE.read_text(encoding="utf-8"), {"TITLE": escape(title), "ASSET_V": ASSET_VERSION})


def render_login(config: AdminConfig) -> str:
    values = {
        "HEAD": render_head("Sign in | AiPicDetect admin"),
        "CLIENT_ID": escape(config.client_id),
        "ASSET_V": ASSET_VERSION,
    }
    return render(LOGIN_FILE.read_text(encoding="utf-8"), values)


def render_unconfigured() -> str:
    values = {
        "HEAD": render_head("Admin not configured | AiPicDetect"),
        "CLIENT_ID_ENV": escape(CLIENT_ID_ENV),
        "SECRET_ENV": escape(SECRET_ENV),
        "ASSET_V": ASSET_VERSION,
    }
    return render(UNCONFIGURED_FILE.read_text(encoding="utf-8"), values)


def render_dashboard(config: AdminConfig, email: str) -> str:
    report = usage_report()
    values = {
        "HEAD": render_head("Admin | AiPicDetect"),
        "EMAIL": escape(email),
        "USAGE": render_stats(usage_stats(report)),
        "CLIENTS": render_clients(report),
        "RUNTIME": render_stats(runtime_stats()),
        "QUOTA": render_stats(quota_stats()),
        "CONFIG": render_stats(config_stats(config)),
        "LINKS": console_links(),
        "GENERATED": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "ASSET_V": ASSET_VERSION,
    }
    return render(DASHBOARD_FILE.read_text(encoding="utf-8"), values)


@router.get("/admin", response_class=HTMLResponse)
def admin_home(admin: str | None = Depends(optional_admin)) -> HTMLResponse:
    config = admin_config()
    if not config.is_configured:
        return HTMLResponse(render_unconfigured())
    if admin is None:
        return HTMLResponse(render_login(config))
    return HTMLResponse(render_dashboard(config, admin))


@router.post("/admin/session")
def create_session(request: Request, body: Credential) -> Response:
    config = admin_config()
    if not config.is_configured:
        raise HTTPException(status_code=404)
    client = client_address(request)
    status = _login_quota.check(client)
    if not status.allowed:
        raise HTTPException(status_code=429, detail="too many sign-in attempts", headers=status.headers())
    _login_quota.record(client)
    try:
        email = verify_google_email(body.credential, config.client_id)
    except TransportError as exc:
        raise HTTPException(status_code=503, detail="could not reach Google to verify the sign-in") from exc
    except (ValueError, GoogleAuthError) as exc:
        raise HTTPException(status_code=400, detail="sign-in token was rejected") from exc
    if email != config.email:
        raise HTTPException(status_code=403, detail="this Google account is not the admin for this instance")
    response = JSONResponse({"ok": True})
    set_session_cookie(response, request, issue_session(config, email))
    return response


@router.post("/admin/logout")
def destroy_session(request: Request) -> RedirectResponse:
    """303 back to ``/admin``, clearing the cookie only if the request actually carried one.

    A cross-site forged POST here never carries the cookie (``SameSite=Lax`` withholds it
    from cross-site requests), so skipping the clear in that case avoids letting a forged
    request still force a same-origin ``Set-Cookie`` deletion in the response.
    """
    response = RedirectResponse("/admin", status_code=303)
    if request.cookies.get(COOKIE_NAME):
        clear_session_cookie(response, request)
    return response
