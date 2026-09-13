import xml.etree.ElementTree as ET

import pytest
from fastapi.testclient import TestClient

from aipicdetect import pages, server
from aipicdetect.seo import AI_CRAWLERS, build_llms_txt

client = TestClient(server.app)
PUBLIC = "https://aipicdetect.example"
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}


@pytest.fixture
def public_url(monkeypatch):
    monkeypatch.setenv("AIPICDETECT_PUBLIC_URL", PUBLIC)
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
    monkeypatch.delenv("AIPICDETECT_PUBLIC_URL", raising=False)
    assert "<loc>http://testserver/</loc>" in client.get("/sitemap.xml").text


def test_favicon_ico_is_served():
    response = client.get("/favicon.ico")
    assert response.status_code == 200 and response.headers["content-type"] == "image/png"


def test_security_txt_has_contact_and_expiry(public_url):
    body = client.get("/.well-known/security.txt").text
    assert "Contact: https://github.com/Micorlov/aipicdetect/issues" in body
    assert "Expires: 20" in body and f"Canonical: {public_url}/.well-known/security.txt" in body


def test_llms_txt_has_h1_blockquote_and_every_page(public_url):
    response = client.get("/llms.txt")
    assert response.status_code == 200 and "text/plain" in response.headers["content-type"]
    body = response.text
    assert body.startswith(
        "# AiPicDetect\n\n> AiPicDetect is a free, open-source tool that scores AI-generated images and "
        "strips hidden metadata"
    )
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


# ─── Locale URL, hreflang and sitemap alternate tests ──────────────────────

XHTML_NS = "http://www.w3.org/1999/xhtml"
NS_FULL = {**NS, "xhtml": XHTML_NS}
from aipicdetect.i18n import SUPPORTED_LOCALES
from aipicdetect.pages import locale_path


def test_sitemap_has_hreflang_alternates_for_every_locale(public_url):
    """Every <url> in the sitemap must carry 30 xhtml:link alternate entries + x-default."""
    root = ET.fromstring(client.get("/sitemap.xml").text)
    urls = root.findall("sm:url", NS)
    assert urls, "sitemap has no <url> entries"
    for url_el in urls:
        links = url_el.findall(f"{{{XHTML_NS}}}link")
        hreflangs = {lnk.get("hreflang") for lnk in links}
        assert hreflangs == set(SUPPORTED_LOCALES) | {"x-default"}, (
            f"Missing hreflang values: {(set(SUPPORTED_LOCALES) | {'x-default'}) - hreflangs}"
        )


def test_sitemap_alternate_hrefs_use_locale_prefix(public_url):
    """Spanish alternates should start with /es/; English with /."""
    root = ET.fromstring(client.get("/sitemap.xml").text)
    # Check the home page entry
    home_url = next(
        u for u in root.findall("sm:url", NS)
        if u.find("sm:loc", NS).text == f"{PUBLIC}/"
    )
    links = {lnk.get("hreflang"): lnk.get("href") for lnk in home_url.findall(f"{{{XHTML_NS}}}link")}
    assert links["en"] == f"{PUBLIC}/", "English alternate should be root"
    assert links["es"] == f"{PUBLIC}/es/", "Spanish alternate should be /es/"
    assert links["he"] == f"{PUBLIC}/he/", "Hebrew alternate should be /he/"
    assert links["x-default"] == f"{PUBLIC}/", "x-default should be English root"


def test_locale_home_route_returns_200(public_url):
    """Every non-English locale home URL should respond 200."""
    for locale in SUPPORTED_LOCALES:
        if locale == "en":
            continue
        path = locale_path(pages.HOME, locale)
        resp = client.get(path)
        assert resp.status_code == 200, f"GET {path} returned {resp.status_code}"


def test_locale_content_page_returns_200():
    """A sample non-English locale prefix on a content page should respond 200."""
    for locale in ("es", "he", "de", "ja"):
        path = locale_path(pages.PAGES[1], locale)  # how-to-tell page
        resp = client.get(path)
        assert resp.status_code == 200, f"GET {path} returned {resp.status_code}"


def test_locale_page_has_correct_lang_attribute():
    """The <html lang=> on a locale-prefix page should match the URL locale."""
    for locale in ("es", "he", "ar"):
        path = locale_path(pages.HOME, locale)
        resp = client.get(path)
        assert f'lang="{locale}"' in resp.text, f"/html> lang attribute missing for {locale}"


def test_locale_page_has_correct_canonical(public_url):
    """The canonical on /es/ should point to {origin}/es/ not /."""
    resp = client.get("/es/")
    assert f'href="{PUBLIC}/es/"' in resp.text, "canonical should be the Spanish locale URL"


def test_lang_query_param_redirects_to_locale_prefix():
    """?lang=es on / should redirect 302 to /es/."""
    resp = client.get("/?lang=es", follow_redirects=False)
    assert resp.status_code == 302
    assert resp.headers["location"] == "/es/"


def test_lang_en_query_param_redirects_to_root():
    """?lang=en should redirect to the English root /."""
    resp = client.get("/faq?lang=en", follow_redirects=False)
    assert resp.status_code == 302
    assert resp.headers["location"] == "/faq"


def test_hreflang_tags_present_on_home_page(public_url):
    """The home page HTML must contain hreflang link tags for every locale."""
    html = client.get("/").text
    assert 'hreflang="es"' in html
    assert 'hreflang="he"' in html
    assert 'hreflang="x-default"' in html
    # Every locale should appear
    for lc in SUPPORTED_LOCALES:
        assert f'hreflang="{lc}"' in html, f"Missing hreflang for {lc} on home page"


def test_lang_switcher_has_crawler_links():
    """The rendered home page should contain <a> links to locale URLs in the lang switcher."""
    html = client.get("/").text
    assert 'href="/es/"' in html, "Spanish locale link missing from lang switcher"
    assert 'href="/he/"' in html, "Hebrew locale link missing from lang switcher"
    assert 'class="lang-links' in html
