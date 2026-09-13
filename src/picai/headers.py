"""Per-path response header policy: caching, crawler directives and baseline security."""

from __future__ import annotations

from typing import Awaitable, Callable

from starlette.requests import Request
from starlette.responses import Response

STATIC_PREFIX = "/static/"
STATIC_MAX_AGE = 86400
PAGE_MAX_AGE = 300
NO_STORE_PREFIXES = ("/analyze", "/scrub", "/download/")
NOINDEX_PATHS = frozenset({"/docs", "/docs/oauth2-redirect", "/redoc", "/openapi.json", "/health", "/status", "/ready"})
SECURITY_HEADERS = {
    "X-Content-Type-Options": "nosniff",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "Permissions-Policy": "camera=(self), microphone=(), geolocation=()",
    "X-Frame-Options": "DENY",
}


def policy_headers(path: str, content_type: str = "", status_code: int = 200) -> dict[str, str]:
    """Headers to add for a response at ``path`` (pure function, easy to test)."""
    headers = dict(SECURITY_HEADERS)
    if path.startswith(STATIC_PREFIX):
        headers["Cache-Control"] = f"public, max-age={STATIC_MAX_AGE}"
    elif path.startswith(NO_STORE_PREFIXES):
        headers["Cache-Control"] = "no-store"
        headers["X-Robots-Tag"] = "noindex"
    elif path in NOINDEX_PATHS:
        headers["X-Robots-Tag"] = "noindex"
    elif status_code == 200 and content_type.startswith("text/html"):
        headers["Cache-Control"] = f"public, max-age={PAGE_MAX_AGE}"
    return headers


async def apply_policy(request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
    response = await call_next(request)
    for name, value in policy_headers(request.url.path, response.headers.get("content-type", ""), response.status_code).items():
        response.headers.setdefault(name, value)
    return response
