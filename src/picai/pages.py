"""Crawlable surface: ``robots.txt``, ``sitemap.xml`` and the static content pages.

Content pages live in ``static/pages/<slug>.html`` as body fragments and are wrapped in
``static/pages/_layout.html`` at request time so the head (title, description, canonical
URL) is filled in per page. The public origin comes from ``PICAI_PUBLIC_URL`` when set,
otherwise from the request, so sitemap and canonical links follow whatever domain serves
the app.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from html import escape
from pathlib import Path

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse, PlainTextResponse, Response

PAGES_DIR = Path(__file__).parent / "static" / "pages"
LAYOUT_FILE = PAGES_DIR / "_layout.html"
REPO_URL = "https://github.com/Micorlov/picai"


@dataclass(frozen=True)
class Page:
    slug: str
    title: str
    description: str

    @property
    def path(self) -> str:
        return f"/{self.slug}"

    @property
    def file(self) -> Path:
        return PAGES_DIR / f"{self.slug}.html"


CONTENT_PAGES: tuple[Page, ...] = (
    Page(
        "self-host",
        "Self-host picai: open-source AI image detector in Docker",
        "Run the picai AI image detector on your own machine with one Docker command or the CLI. "
        "Nothing leaves your computer.",
    ),
    Page(
        "api",
        "picai API: AI image detection and metadata scrubbing over HTTP",
        "POST an image to /analyze for an AI likelihood score plus its EXIF, XMP, IPTC, C2PA and ICC "
        "blocks, or to /scrub for a metadata-free copy.",
    ),
    Page(
        "c2pa",
        "C2PA content credentials: how to check and remove them",
        "What C2PA content credentials are, how picai finds them next to EXIF, XMP, IPTC and ICC "
        "blocks, and how to download a copy with every block removed.",
    ),
    Page(
        "how-accurate",
        "How accurate is an AI image detector? What picai can and cannot tell you",
        "AI image detectors give probabilities, not proof. What published benchmarks say about "
        "detector accuracy on newer generators and how to read a picai score.",
    ),
)
_PAGES_BY_SLUG = {page.slug: page for page in CONTENT_PAGES}

router = APIRouter(include_in_schema=False)


def public_url(request: Request) -> str:
    """Origin used for absolute URLs: ``PICAI_PUBLIC_URL`` if set, else the request's base."""
    configured = os.environ.get("PICAI_PUBLIC_URL", "").strip()
    return (configured or str(request.base_url)).rstrip("/")


@router.get("/robots.txt")
def robots(request: Request) -> PlainTextResponse:
    body = "\n".join(
        [
            "User-agent: *",
            "Allow: /",
            "Disallow: /analyze",
            "Disallow: /scrub",
            "Disallow: /download/",
            "",
            f"Sitemap: {public_url(request)}/sitemap.xml",
            "",
        ]
    )
    return PlainTextResponse(body)


@router.get("/sitemap.xml")
def sitemap(request: Request) -> Response:
    base = public_url(request)
    urls = [f"{base}/"] + [f"{base}{page.path}" for page in CONTENT_PAGES]
    entries = "".join(f"  <url><loc>{escape(url)}</loc></url>\n" for url in urls)
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{entries}</urlset>\n"
    )
    return Response(content=xml, media_type="application/xml")


@router.get("/{slug}")
def content_page(slug: str, request: Request) -> HTMLResponse:
    page = _PAGES_BY_SLUG.get(slug)
    if page is None:
        raise HTTPException(status_code=404, detail="page not found")
    return HTMLResponse(render_page(page, public_url(request)))


def render_page(page: Page, base_url: str) -> str:
    """Wrap the page's body fragment in the shared layout with its head filled in."""
    layout = LAYOUT_FILE.read_text(encoding="utf-8")
    body = page.file.read_text(encoding="utf-8")
    values = {
        "TITLE": escape(page.title),
        "DESCRIPTION": escape(page.description),
        "CANONICAL": escape(f"{base_url}{page.path}"),
        "BASE_URL": escape(base_url),
        "SLUG": page.slug,
        "REPO_URL": REPO_URL,
        "BODY": body,
    }
    for key, value in values.items():
        layout = layout.replace("{{" + key + "}}", value)
    return layout
