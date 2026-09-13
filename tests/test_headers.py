from fastapi.testclient import TestClient

from aipicdetect import server
from aipicdetect.headers import policy_headers

client = TestClient(server.app)


def test_policy_headers_for_static_api_and_pages():
    assert policy_headers("/static/styles.css")["Cache-Control"] == "public, max-age=86400"
    api = policy_headers("/analyze")
    assert api["Cache-Control"] == "no-store" and api["X-Robots-Tag"] == "noindex"
    assert policy_headers("/download/abc")["X-Robots-Tag"] == "noindex"
    assert policy_headers("/docs")["X-Robots-Tag"] == "noindex"
    page = policy_headers("/", "text/html; charset=utf-8")
    assert page["Cache-Control"] == "public, max-age=300" and "X-Robots-Tag" not in page
    assert "Cache-Control" not in policy_headers("/nope", "text/html", 404)
    assert policy_headers("/")["X-Content-Type-Options"] == "nosniff"
    admin = policy_headers("/admin")
    assert admin["Cache-Control"] == "no-store" and admin["X-Robots-Tag"] == "noindex"
    assert "identity-credentials-get" in admin["Permissions-Policy"]


def test_docs_and_openapi_have_noindex_header():
    assert client.get("/docs").headers["x-robots-tag"] == "noindex"
    assert client.get("/openapi.json").headers["x-robots-tag"] == "noindex"
    assert "x-robots-tag" not in client.get("/").headers


def test_static_and_pages_get_cache_control():
    assert client.get("/static/styles.css").headers["cache-control"] == "public, max-age=86400"
    assert client.get("/").headers["cache-control"] == "public, max-age=300"


def test_gzip_applied_to_html_when_accepted():
    response = client.get("/", headers={"Accept-Encoding": "gzip"})
    assert response.headers.get("content-encoding") == "gzip"
    assert "<h1>" in response.text
