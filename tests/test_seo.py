import xml.etree.ElementTree as ET

import pytest
from fastapi.testclient import TestClient

from picai import pages, server
from picai.seo import AI_CRAWLERS, build_llms_txt

client = TestClient(server.app)
PUBLIC = "https://picai.example"
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}


@pytest.fixture
def public_url(monkeypatch):
    monkeypatch.setenv("PICAI_PUBLIC_URL", PUBLIC)
    return PUBLIC


def test_robots_allows_ai_crawlers_and_blocks_api(public_url):
    response = client.get("/robots.txt")
    assert response.status_code == 200 and "text/plain" in response.headers["content-type"]
    body = response.text
    for bot in AI_CRAWLERS:
        assert f"User-agent: {bot}" in body
    assert "Allow: /\n" in body
    for path in ("/analyze", "/scrub", "/download/", "/openapi.json"):
        assert f"Disallow: {path}" in body
    assert "Disallow: /docs" not in body
    assert f"Sitemap: {public_url}/sitemap.xml" in body


def test_sitemap_contains_every_registered_page(public_url):
    response = client.get("/sitemap.xml")
    assert response.status_code == 200 and "xml" in response.headers["content-type"]
    root = ET.fromstring(response.text)
    urls = root.findall("sm:url", NS)
    assert {u.find("sm:loc", NS).text for u in urls} == {public_url + p.path for p in pages.PAGES}
    for url in urls:
        assert url.find("sm:lastmod", NS).text.count("-") == 2
        assert url.find("sm:priority", NS) is not None


def test_sitemap_uses_request_origin_without_public_url(monkeypatch):
    monkeypatch.delenv("PICAI_PUBLIC_URL", raising=False)
    assert "<loc>http://testserver/</loc>" in client.get("/sitemap.xml").text


def test_favicon_ico_is_served():
    response = client.get("/favicon.ico")
    assert response.status_code == 200 and response.headers["content-type"] == "image/png"


def test_security_txt_has_contact_and_expiry(public_url):
    body = client.get("/.well-known/security.txt").text
    assert "Contact: https://github.com/Micorlov/picai/issues" in body
    assert "Expires: 20" in body and f"Canonical: {public_url}/.well-known/security.txt" in body


def test_llms_txt_has_h1_blockquote_and_every_page(public_url):
    response = client.get("/llms.txt")
    assert response.status_code == 200 and "text/plain" in response.headers["content-type"]
    body = response.text
    assert body.startswith("# picai\n\n> picai is a free, open-source AI image detector and metadata scrubber.")
    for page in pages.PAGES:
        assert f"]({public_url}{page.path}): " in body
    for section in ("## Product", "## Guides", "## Developers", "## Optional"):
        assert section in body
    assert f"{public_url}/llms-full.txt" in body


def test_llms_full_contains_every_page_heading_and_text(public_url):
    body = client.get("/llms-full.txt").text
    for page in pages.PAGES:
        assert f"# {page.h1}\nSource: {public_url}{page.path}\n" in body
    assert "Does my image leave my computer?" in body
    assert "<p>" not in body and "<details>" not in body


def test_llms_builder_is_pure():
    assert build_llms_txt("https://a.example") != build_llms_txt("https://b.example")
