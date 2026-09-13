import pytest
from fastapi.testclient import TestClient

from picai import server
from picai.pages import CONTENT_PAGES, render_page

client = TestClient(server.app, base_url="http://testserver")


def test_robots_allows_crawling_and_points_at_sitemap():
    response = client.get("/robots.txt")
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/plain")
    assert "User-agent: *" in response.text
    assert "Disallow: /download/" in response.text
    assert "Sitemap: http://testserver/sitemap.xml" in response.text


def test_sitemap_lists_home_and_every_content_page():
    response = client.get("/sitemap.xml")
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/xml")
    assert "<loc>http://testserver/</loc>" in response.text
    for page in CONTENT_PAGES:
        assert f"<loc>http://testserver{page.path}</loc>" in response.text


def test_public_url_env_overrides_request_origin(monkeypatch):
    monkeypatch.setenv("PICAI_PUBLIC_URL", "https://picai.example/")
    assert "Sitemap: https://picai.example/sitemap.xml" in client.get("/robots.txt").text
    assert "<loc>https://picai.example/c2pa</loc>" in client.get("/sitemap.xml").text
    page = client.get("/c2pa").text
    assert '<link rel="canonical" href="https://picai.example/c2pa">' in page
    assert 'content="https://picai.example/static/icons/icon-512.png"' in page


@pytest.mark.parametrize("page", CONTENT_PAGES, ids=lambda page: page.slug)
def test_content_pages_render_with_head_and_navigation(page):
    response = client.get(page.path)
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert f"<title>{page.title} · picai</title>" in response.text
    assert f'<meta name="description" content="{page.description}">' in response.text
    assert '<link rel="stylesheet" href="/static/pages.css">' in response.text
    assert "<h1>" in response.text
    assert 'href="/self-host"' in response.text and 'href="/how-accurate"' in response.text


def test_layout_placeholders_are_all_filled():
    for page in CONTENT_PAGES:
        assert "{{" not in render_page(page, "http://x")


def test_unknown_page_is_404_and_api_routes_still_win():
    assert client.get("/nope").status_code == 404
    assert client.get("/health").json() == {"status": "ok"}
    assert client.get("/docs").status_code == 200


def test_home_page_is_honest_about_the_public_instance_and_links_the_pages():
    home = client.get("/").text
    assert "Nothing leaves your computer" not in home
    assert 'href="/self-host"' in home and 'href="/c2pa"' in home
    assert 'application/ld+json' in home and 'property="og:title"' in home
    assert 'id="download"' in home
