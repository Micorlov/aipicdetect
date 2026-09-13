import json
import re
from html import escape
from html.parser import HTMLParser

import pytest
from fastapi.testclient import TestClient

from aipicdetect import pages, server
from aipicdetect.content.faq import FAQ_ALL, FAQ_HOME
from aipicdetect.detect import Detector

client = TestClient(server.app)
PUBLIC = "https://aipicdetect.example"


@pytest.fixture(autouse=True)
def fake_detector(monkeypatch):
    detector = Detector(model_name="fake/model", classifier=lambda image: [{"label": "ai", "score": 0.9}])
    monkeypatch.setattr(server, "get_detector", lambda: detector)


@pytest.fixture
def public_url(monkeypatch):
    monkeypatch.setenv("AIPICDETECT_PUBLIC_URL", PUBLIC + "/")
    return PUBLIC


class _Summaries(HTMLParser):
    def __init__(self):
        super().__init__()
        self.texts, self._in = [], False

    def handle_starttag(self, tag, attrs):
        self._in = tag == "summary"

    def handle_endtag(self, tag):
        self._in = False

    def handle_data(self, data):
        if self._in:
            self.texts.append(data)


def summaries(html: str) -> list[str]:
    parser = _Summaries()
    parser.feed(html)
    return parser.texts


def jsonld(html: str) -> dict:
    match = re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
    assert match, "no JSON-LD on page"
    return json.loads(match.group(1))


# --- config -----------------------------------------------------------------


def test_public_url_normalises_trailing_slash():
    assert pages.normalise_public_url(" https://x.example/ ") == "https://x.example"


@pytest.mark.parametrize("bad", ["x.example", "ftp://x.example", "https://x.example/app"])
def test_public_url_rejects_non_origin(bad):
    with pytest.raises(ValueError):
        pages.normalise_public_url(bad)


def test_render_rejects_unknown_placeholder():
    with pytest.raises(KeyError):
        pages.render("hello {{NOPE}}", {})


# --- home page head + copy --------------------------------------------------


def test_index_has_canonical_and_og_from_public_url(public_url):
    html = client.get("/").text
    assert f'<link rel="canonical" href="{public_url}/">' in html
    assert f'<meta property="og:url" content="{public_url}/">' in html
    assert f'<meta property="og:image" content="{public_url}/static/og/aipicdetect-og.png">' in html
    assert '<meta name="twitter:card" content="summary_large_image">' in html
    assert 'name="robots" content="index, follow' in html


def test_index_falls_back_to_request_origin_when_unset(monkeypatch):
    monkeypatch.delenv("AIPICDETECT_PUBLIC_URL", raising=False)
    assert '<link rel="canonical" href="http://testserver/">' in client.get("/").text


def test_verification_tags_only_when_configured(monkeypatch):
    assert "google-site-verification" not in client.get("/").text
    monkeypatch.setenv("AIPICDETECT_GSC_VERIFICATION", "abc123")
    monkeypatch.setenv("AIPICDETECT_BING_VERIFICATION", "bing456")
    html = client.get("/").text
    assert '<meta name="google-site-verification" content="abc123">' in html
    assert '<meta name="msvalidate.01" content="bing456">' in html


def test_analytics_tag_only_when_configured(monkeypatch):
    assert "googletagmanager.com" not in client.get("/").text
    monkeypatch.setenv("AIPICDETECT_GA_MEASUREMENT_ID", "G-ABC123")
    html = client.get("/").text
    assert '<script async src="https://www.googletagmanager.com/gtag/js?id=G-ABC123"></script>' in html
    assert "gtag('config', 'G-ABC123');" in html


def test_index_copy_does_not_claim_localhost():
    html = client.get("/").text
    assert "localhost" not in html
    assert "Nothing leaves your computer" not in html
    assert escape(pages.HOME.title) in html and "<h1>" in html


def test_home_faq_renders_every_entry():
    assert summaries(client.get("/").text) == [e.question for e in FAQ_HOME]


# --- registry ----------------------------------------------------------------


def test_title_and_description_lengths():
    for page in pages.PAGES:
        assert 50 <= len(page.title) <= 60, (page.slug, len(page.title))
        assert 120 <= len(page.description) <= 160, (page.slug, len(page.description))


def test_paths_are_unique_and_fragments_exist():
    paths = [p.path for p in pages.PAGES]
    assert len(set(paths)) == len(paths)
    for page in pages.PAGES:
        assert page.file.is_file(), page.file


def test_every_registered_page_returns_html_200(public_url):
    for page in pages.PAGES:
        response = client.get(page.path)
        assert response.status_code == 200, page.path
        assert "text/html" in response.headers["content-type"]
        html = response.text
        assert f"<title>{escape(page.title)}</title>" in html
        assert f'<link rel="canonical" href="{public_url}{page.path}">' in html
        assert "localhost" not in html or page.slug in {"self-host", "privacy", "api", "faq"}


def test_interior_pages_have_breadcrumb_and_declared_schema(public_url):
    for page in pages.PAGES[1:]:
        graph = jsonld(client.get(page.path).text)["@graph"]
        types = [item["@type"] for item in graph]
        assert types[0] == "BreadcrumbList", page.path
        assert graph[0]["itemListElement"][1]["item"] == f"{public_url}{page.path}"
        for kind in page.schema_types:
            assert kind in types, (page.path, kind)


def test_nav_and_footer_links_resolve():
    html = client.get("/").text
    hrefs = set(re.findall(r'href="(/[^"#]*)"', html))
    assert hrefs >= {p.path for p in pages.PAGES if p.nav_label or p.footer_label}
    for href in hrefs:
        if href.startswith("/static/"):
            continue
        assert client.get(href).status_code == 200, href


def test_faq_page_includes_home_and_extra_entries():
    html = client.get("/faq").text
    assert summaries(html) == [e.question for e in FAQ_ALL]
    questions = [q["name"] for q in jsonld(html)["@graph"][1]["mainEntity"]]
    assert questions == [e.question for e in FAQ_ALL]


def test_unknown_page_is_html_404_for_browsers_and_json_for_api():
    browser = client.get("/nope", headers={"Accept": "text/html,application/xhtml+xml"})
    assert browser.status_code == 404
    assert "text/html" in browser.headers["content-type"] and "Page not found" in browser.text
    assert "noindex" in browser.text
    api = client.get("/download/nope")
    assert api.status_code == 404 and api.headers["content-type"].startswith("application/json")


def test_layout_placeholders_are_all_filled():
    for page in pages.PAGES:
        assert "{{" not in pages.render_page(page, "http://x", "en")
    assert "{{" not in pages.render_not_found("http://x", "en")


def test_api_routes_are_not_shadowed_by_pages():
    assert client.get("/health").json() == {"status": "ok"}
    assert client.get("/docs").status_code == 200


def test_home_page_links_download_and_content_pages():
    home = client.get("/").text
    assert 'id="download"' in home
    assert 'href="/self-host"' in home and 'href="/c2pa"' in home and 'href="/faq"' in home
    assert 'application/ld+json' in home and 'property="og:title"' in home
    assert "fonts.googleapis.com" not in home


def test_assets_are_versioned_by_content_hash():
    html = client.get("/").text
    assert f'/static/styles.css?v={pages.ASSET_VERSION}' in html and f'/static/app.js?v={pages.ASSET_VERSION}' in html
    assert len(pages.ASSET_VERSION) == 10
    assert f'/static/pages.css?v={pages.ASSET_VERSION}' in client.get("/faq").text


def test_analytics_id_must_be_a_ga4_measurement_id(monkeypatch):
    monkeypatch.setenv("AIPICDETECT_GA_MEASUREMENT_ID", "G-ABC123'); alert(1); //")
    with pytest.raises(ValueError):
        pages.analytics_tag()
    monkeypatch.setenv("AIPICDETECT_GA_MEASUREMENT_ID", "G-ABC12345")
    assert "gtag('config', 'G-ABC12345')" in pages.analytics_tag()
