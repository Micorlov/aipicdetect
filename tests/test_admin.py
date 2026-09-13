import pytest
from fastapi.testclient import TestClient

from picai import admin, server
from picai.detect import Detector

client = TestClient(server.app)
CLIENT_ID = "test-client-id.apps.googleusercontent.com"
SECRET = "s" * 40
EMAIL = "micorlov@gmail.com"


@pytest.fixture(autouse=True)
def clear_cookies():
    client.cookies.clear()
    yield
    client.cookies.clear()


@pytest.fixture(autouse=True)
def fake_detector(monkeypatch):
    detector = Detector(model_name="fake/model", classifier=lambda image: [{"label": "ai", "score": 0.9}])
    monkeypatch.setattr(admin, "get_detector", lambda: detector)


@pytest.fixture
def configured(monkeypatch):
    monkeypatch.setenv("PICAI_GOOGLE_CLIENT_ID", CLIENT_ID)
    monkeypatch.setenv("PICAI_ADMIN_SESSION_SECRET", SECRET)
    monkeypatch.setenv("PICAI_ADMIN_EMAIL", EMAIL)
    return admin.admin_config()


def google_claims(email: str = EMAIL, *, email_verified: bool = True, iss: str = "https://accounts.google.com") -> dict:
    return {"iss": iss, "email": email, "email_verified": email_verified}


def stub_verify(monkeypatch, result=None, *, error: Exception | None = None):
    captured = {}

    def fake(token, request, audience=None, clock_skew_in_seconds=0):
        captured["token"] = token
        captured["audience"] = audience
        if error is not None:
            raise error
        return result

    monkeypatch.setattr(admin.id_token, "verify_oauth2_token", fake)
    return captured


def login(monkeypatch, email: str = EMAIL) -> object:
    stub_verify(monkeypatch, google_claims(email))
    return client.post("/admin/session", json={"credential": "fake.jwt.token"})


# --- not configured ----------------------------------------------------------


def test_admin_shows_unconfigured_message_by_default():
    response = client.get("/admin")
    assert response.status_code == 200
    assert "not configured" in response.text.lower()
    assert "set-cookie" not in {k.lower() for k in response.headers}
    assert "accounts.google.com" not in response.text


def test_session_endpoint_404_when_unconfigured():
    response = client.post("/admin/session", json={"credential": "whatever"})
    assert response.status_code == 404
    assert "set-cookie" not in {k.lower() for k in response.headers}


def test_weak_secret_is_treated_as_unconfigured(monkeypatch):
    monkeypatch.setenv("PICAI_GOOGLE_CLIENT_ID", CLIENT_ID)
    monkeypatch.setenv("PICAI_ADMIN_SESSION_SECRET", "short")
    assert "not configured" in client.get("/admin").text.lower()
    assert client.post("/admin/session", json={"credential": "x"}).status_code == 404


# --- login page ----------------------------------------------------------------


def test_admin_shows_login_button_when_configured(configured):
    response = client.get("/admin")
    assert response.status_code == 200
    assert f'data-client_id="{CLIENT_ID}"' in response.text
    assert "accounts.google.com/gsi/client" in response.text


# --- POST /admin/session -------------------------------------------------------


def test_valid_credential_sets_cookie_with_expected_attributes(configured, monkeypatch):
    response = login(monkeypatch)
    assert response.status_code == 200
    assert response.json() == {"ok": True}
    cookie_header = response.headers["set-cookie"]
    assert "HttpOnly" in cookie_header
    assert "Path=/admin" in cookie_header
    assert "samesite=lax" in cookie_header.lower()
    assert "Max-Age=604800" in cookie_header
    assert "Secure" not in cookie_header  # plain-http test client


def test_audience_is_passed_to_verify(configured, monkeypatch):
    captured = stub_verify(monkeypatch, google_claims())
    client.post("/admin/session", json={"credential": "fake.jwt.token"})
    assert captured["audience"] == CLIENT_ID


def test_wrong_email_is_rejected_without_cookie(configured, monkeypatch):
    response = login(monkeypatch, email="someone-else@gmail.com")
    assert response.status_code == 403
    assert "set-cookie" not in {k.lower() for k in response.headers}


def test_unverified_email_is_rejected(configured, monkeypatch):
    stub_verify(monkeypatch, google_claims(email_verified=False))
    response = client.post("/admin/session", json={"credential": "fake.jwt.token"})
    assert response.status_code == 400
    assert "set-cookie" not in {k.lower() for k in response.headers}


def test_wrong_issuer_is_rejected(configured, monkeypatch):
    stub_verify(monkeypatch, google_claims(iss="https://evil.example"))
    response = client.post("/admin/session", json={"credential": "fake.jwt.token"})
    assert response.status_code == 400


def test_rejected_token_returns_400(configured, monkeypatch):
    stub_verify(monkeypatch, error=ValueError("bad token"))
    response = client.post("/admin/session", json={"credential": "fake.jwt.token"})
    assert response.status_code == 400
    assert "set-cookie" not in {k.lower() for k in response.headers}


def test_unreachable_google_returns_503(configured, monkeypatch):
    from google.auth.exceptions import TransportError

    stub_verify(monkeypatch, error=TransportError("network down"))
    response = client.post("/admin/session", json={"credential": "fake.jwt.token"})
    assert response.status_code == 503


def test_form_encoded_body_is_rejected(configured):
    response = client.post("/admin/session", data={"credential": "x"})
    assert response.status_code == 422


def test_oversized_credential_is_rejected(configured):
    response = client.post("/admin/session", json={"credential": "x" * 5000})
    assert response.status_code == 422


def test_login_rate_limit(configured, monkeypatch):
    stub_verify(monkeypatch, error=ValueError("bad token"))
    for _ in range(admin.LOGIN_ATTEMPTS_PER_DAY):
        assert client.post("/admin/session", json={"credential": "fake.jwt.token"}).status_code == 400
    response = client.post("/admin/session", json={"credential": "fake.jwt.token"})
    assert response.status_code == 429


# --- session validation ---------------------------------------------------------


def test_dashboard_shown_with_valid_session(configured, monkeypatch):
    login(monkeypatch)
    response = client.get("/admin")
    assert response.status_code == 200
    assert EMAIL in response.text
    assert "fake/model" in response.text
    assert "{{" not in response.text


def test_tampered_cookie_falls_back_to_login(configured, monkeypatch):
    login(monkeypatch)
    client.cookies.set(admin.COOKIE_NAME, client.cookies.get(admin.COOKIE_NAME) + "x")
    response = client.get("/admin")
    assert "g_id_signin" in response.text


def test_cookie_signed_with_different_secret_falls_back_to_login(configured, monkeypatch):
    login(monkeypatch)
    other = admin.AdminConfig(client_id=CLIENT_ID, secret="t" * 40, email=EMAIL)
    forged = admin.issue_session(other, EMAIL)
    client.cookies.set(admin.COOKIE_NAME, forged)
    response = client.get("/admin")
    assert "g_id_signin" in response.text


def test_expired_session_falls_back_to_login(configured, monkeypatch):
    import time as time_module

    login(monkeypatch)
    later = time_module.time() + admin.SESSION_MAX_AGE + 10
    monkeypatch.setattr(time_module, "time", lambda: later)
    response = client.get("/admin")
    assert "g_id_signin" in response.text


def test_changing_admin_email_invalidates_existing_session(configured, monkeypatch):
    login(monkeypatch)
    monkeypatch.setenv("PICAI_ADMIN_EMAIL", "someone-else@gmail.com")
    response = client.get("/admin")
    assert "g_id_signin" in response.text


def test_logout_clears_cookie(configured, monkeypatch):
    login(monkeypatch)
    response = client.post("/admin/logout", follow_redirects=False)
    assert response.status_code == 303
    assert response.headers["location"] == "/admin"


def test_logout_without_a_cookie_sets_no_cookie(configured):
    # A cross-site forged logout POST never carries the SameSite=Lax cookie; if we still
    # answered with a Set-Cookie deletion, the forged request could clear a real session
    # anyway (SameSite protects the request, not the response). Confirm we no-op instead.
    response = client.post("/admin/logout", follow_redirects=False)
    assert response.status_code == 303
    assert "set-cookie" not in {k.lower() for k in response.headers}
    response = client.get("/admin", follow_redirects=False)
    assert "g_id_signin" in response.text


# --- headers / SEO surface -------------------------------------------------------


def test_admin_responses_are_not_cached_or_indexed(configured):
    response = client.get("/admin")
    assert response.headers["cache-control"] == "no-store"
    assert response.headers["x-robots-tag"] == "noindex"
    assert "identity-credentials-get" in response.headers["permissions-policy"]


def test_admin_absent_from_seo_surfaces():
    assert "/admin" not in client.get("/robots.txt").text
    assert "/admin" not in client.get("/sitemap.xml").text
    assert "/admin" not in client.get("/llms.txt").text


# --- is_secure ---------------------------------------------------------------


def _cookie_secure(response) -> bool:
    return "Secure" in response.headers["set-cookie"]


def test_is_secure_trusts_forwarded_proto_over_the_raw_scheme(configured, monkeypatch):
    https_client = TestClient(server.app, base_url="https://testserver")

    stub_verify(monkeypatch, google_claims())
    plain_http = client.post("/admin/session", json={"credential": "t"})
    assert not _cookie_secure(plain_http)  # http request, no forwarded header

    stub_verify(monkeypatch, google_claims())
    forwarded_https = client.post(
        "/admin/session", json={"credential": "t"}, headers={"X-Forwarded-Proto": "https"}
    )
    assert _cookie_secure(forwarded_https)  # http request, but trusted proxy says https

    stub_verify(monkeypatch, google_claims())
    real_https = https_client.post("/admin/session", json={"credential": "t"})
    assert _cookie_secure(real_https)  # https request, no forwarded header

    stub_verify(monkeypatch, google_claims())
    forwarded_http = https_client.post(
        "/admin/session", json={"credential": "t"}, headers={"X-Forwarded-Proto": "http"}
    )
    assert not _cookie_secure(forwarded_http)  # forwarded header overrides the raw https scheme

    # A spoofed leading hop must not defeat the real (last, Cloud-Run-set) hop.
    stub_verify(monkeypatch, google_claims())
    spoofed_leading_hop = client.post(
        "/admin/session", json={"credential": "t"}, headers={"X-Forwarded-Proto": "https, http"}
    )
    assert not _cookie_secure(spoofed_leading_hop)


# --- require_admin guard (unused by any route yet, but verified directly) -------


def test_require_admin_rejects_missing_session():
    with pytest.raises(Exception) as exc_info:
        admin.require_admin(None)
    assert exc_info.value.status_code == 401


def test_require_admin_passes_through_a_session():
    assert admin.require_admin(EMAIL) == EMAIL


# --- token edge cases and Cloud Run links ----------------------------------------


def test_verify_google_email_rejects_missing_email_claim(configured, monkeypatch):
    stub_verify(monkeypatch, {"iss": "https://accounts.google.com", "email_verified": True})
    response = client.post("/admin/session", json={"credential": "t"})
    assert response.status_code == 400


def test_console_links_shown_only_on_cloud_run(configured, monkeypatch):
    login(monkeypatch)
    response = client.get("/admin")
    assert "console.cloud.google.com" not in response.text

    monkeypatch.setenv("K_SERVICE", "picai")
    monkeypatch.setenv("GOOGLE_CLOUD_PROJECT", "picai-260913")
    response = client.get("/admin")
    assert "console.cloud.google.com/run/detail" in response.text
    assert "console.cloud.google.com/billing/budgets?project=picai-260913" in response.text


# --- usage section -----------------------------------------------------------------


def test_dashboard_renders_visitor_and_upload_numbers(configured, monkeypatch):
    from datetime import datetime, timezone

    from picai import usage

    report = usage.UsageReport(
        visitors=(usage.Visitors(7, 12, 40), usage.Visitors(30, 57, 190)),
        visitors_error=None,
        uploads=usage.Uploads(
            windows=(usage.UploadWindow(7, 9), usage.UploadWindow(30, 31)),
            clients=(usage.ClientUploads("203.0.113.7", 6, datetime(2026, 9, 12, 8, 30, tzinfo=timezone.utc)),),
        ),
        uploads_error=None,
    )
    monkeypatch.setattr(admin, "usage_report", lambda: report)
    login(monkeypatch)
    html = client.get("/admin").text
    for fragment in ("Visitors (7 days)", ">12<", ">57<", "Page views (30 days)", ">190<"):
        assert fragment in html
    for fragment in ("Images analyzed (7 days)", ">9<", ">31<"):
        assert fragment in html
    assert "<code>203.0.113.7</code>" in html and "<td>6</td>" in html and "2026-09-12 08:30 UTC" in html


def test_dashboard_shows_unavailable_when_usage_sources_fail(configured, monkeypatch):
    from picai import usage

    monkeypatch.setattr(
        admin, "usage_report", lambda: usage.UsageReport(None, "PermissionError: no", None, "timed out after 15s")
    )
    login(monkeypatch)
    html = client.get("/admin").text
    assert "unavailable: PermissionError: no" in html
    assert "unavailable: timed out after 15s" in html
    assert "Unavailable: timed out after 15s" in html  # the clients table placeholder


def test_dashboard_says_so_when_there_are_no_uploads(configured, monkeypatch):
    from picai import usage

    empty = usage.Uploads(windows=(usage.UploadWindow(7, 0), usage.UploadWindow(30, 0)), clients=())
    monkeypatch.setattr(admin, "usage_report", lambda: usage.UsageReport(None, "off", empty, None))
    login(monkeypatch)
    assert "No uploads in this window." in client.get("/admin").text


# --- no IP/XSS leakage into the dashboard ----------------------------------------


def test_dashboard_never_renders_raw_client_keys(configured, monkeypatch):
    login(monkeypatch)
    hostile = "<script>alert(1)</script>"
    server._quota.record(hostile)  # simulates an attacker-controlled X-Forwarded-For value
    response = client.get("/admin")
    assert hostile not in response.text
    assert "<script>" not in response.text
