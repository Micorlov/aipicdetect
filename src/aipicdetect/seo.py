"""Crawler-facing plain files: robots.txt, sitemap.xml, llms.txt, llms-full.txt,
favicon.ico and security.txt. All URLs derive from :func:`aipicdetect.pages.public_url`."""

from __future__ import annotations

from datetime import date
from html import escape
from html.parser import HTMLParser

from fastapi import APIRouter, Request
from fastapi.responses import FileResponse, PlainTextResponse, Response

from aipicdetect.content import home as copy
from aipicdetect.content.faq import FAQ_HOME
from aipicdetect.detect import DEFAULT_MODEL
from aipicdetect.i18n import SUPPORTED_LOCALES
from aipicdetect.pages import PAGES, STATIC_DIR, Page, body_values, locale_path, public_url, render

AI_CRAWLERS = ("GPTBot", "OAI-SearchBot", "ClaudeBot", "anthropic-ai", "PerplexityBot", "Google-Extended", "CCBot", "Applebot-Extended")
DISALLOWED = ("/analyze", "/scrub", "/download/", "/openapi.json", "/health", "/status", "/ready")
SECTIONS = ("Product", "Guides", "Developers")
SECURITY_CONTACT = f"{copy.REPO_URL}/issues"
SECURITY_EXPIRES = date(2027, 9, 13)
FAVICON = STATIC_DIR / "icons" / "favicon-32.png"

router = APIRouter(include_in_schema=False)


@router.get("/robots.txt")
def robots(request: Request) -> PlainTextResponse:
    lines = ["User-agent: *", *[f"User-agent: {bot}" for bot in AI_CRAWLERS], "Allow: /"]
    lines += [f"Disallow: {path}" for path in DISALLOWED]
    lines += ["", f"Sitemap: {public_url(request)}/sitemap.xml", ""]
    return PlainTextResponse("\n".join(lines))


@router.get("/sitemap.xml")
def sitemap(request: Request) -> Response:
    origin = public_url(request)

    def _url_entry(p: Page) -> str:
        # xhtml:link alternate for every supported locale + x-default
        alternates = "".join(
            f'    <xhtml:link rel="alternate" hreflang="{lc}"'
            f' href="{escape(origin + locale_path(p, lc))}"/>\n'
            for lc in SUPPORTED_LOCALES
        )
        alternates += f'    <xhtml:link rel="alternate" hreflang="x-default" href="{escape(origin + p.path)}"/>\n'
        return (
            "  <url>\n"
            f"    <loc>{escape(origin + p.path)}</loc>\n"
            f"    <lastmod>{p.lastmod.isoformat()}</lastmod>\n"
            f"    <priority>{p.priority:.1f}</priority>\n"
            f"{alternates}"
            "  </url>\n"
        )

    entries = "".join(_url_entry(p) for p in PAGES)
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"'
        ' xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        f"{entries}</urlset>\n"
    )
    return Response(content=xml, media_type="application/xml")


@router.get("/favicon.ico")
def favicon() -> FileResponse:
    return FileResponse(FAVICON, media_type="image/png")


@router.get("/.well-known/security.txt")
def security_txt(request: Request) -> PlainTextResponse:
    body = "\n".join(
        [
            f"Contact: {SECURITY_CONTACT}",
            f"Expires: {SECURITY_EXPIRES.isoformat()}T00:00:00.000Z",
            f"Canonical: {public_url(request)}/.well-known/security.txt",
            "Preferred-Languages: en",
            "",
        ]
    )
    return PlainTextResponse(body)


@router.get("/llms.txt")
def llms_txt(request: Request) -> PlainTextResponse:
    return PlainTextResponse(build_llms_txt(public_url(request)), media_type="text/plain; charset=utf-8")


@router.get("/llms-full.txt")
def llms_full_txt(request: Request) -> PlainTextResponse:
    return PlainTextResponse(build_llms_full(public_url(request)), media_type="text/plain; charset=utf-8")


def _header(origin: str) -> list[str]:
    summary = copy.SUMMARY.replace("Use the hosted instance", f"Use the hosted instance at {origin}/")
    return [
        f"# {copy.BRAND}",
        "",
        f"> {summary}",
        "",
        f"Author: {copy.AUTHOR}. Source: {copy.REPO_URL} ({copy.LICENSE_NAME}). "
        f"Default model: {DEFAULT_MODEL}. Last updated: {max(p.lastmod for p in PAGES).isoformat()}.",
        "",
    ]


def build_llms_txt(origin: str) -> str:
    lines = _header(origin)
    for section in SECTIONS:
        lines.append(f"## {section}")
        lines += [f"- [{p.h1}]({origin}{p.path}): {p.description}" for p in PAGES if p.section == section]
        lines.append("")
    lines += ["## Optional", f"- [OpenAPI schema]({origin}/openapi.json)", f"- [Full text of all pages]({origin}/llms-full.txt)", ""]
    return "\n".join(lines)


def build_llms_full(origin: str) -> str:
    lines = _header(origin)
    for page in PAGES:
        lines += [f"# {page.h1}", f"Source: {origin}{page.path}", f"Last updated: {page.lastmod.isoformat()}", "", page_text(page, origin), ""]
    return "\n".join(lines)


def page_text(page: Page, origin: str) -> str:
    """Plain text of a page body: the rendered fragment with tags stripped."""
    if page.is_home:
        fragment = "\n".join(
            [f"<p>{copy.ENTITY_SENTENCE} {copy.LEAD}</p>", "<h2>How it works</h2>", "{{STEPS}}", "<h2>FAQ</h2>", "{{FAQ}}"]
        )
    else:
        fragment = page.file.read_text(encoding="utf-8")
    return _strip_tags(render(fragment, body_values(page, origin)))


class _TextExtractor(HTMLParser):
    BLOCK_TAGS = {"p", "h1", "h2", "h3", "li", "details", "summary", "pre", "tr", "dt", "dd"}

    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in self.BLOCK_TAGS:
            self.parts.append("\n")
        if tag.startswith("h") and tag[1:].isdigit():
            self.parts.append("#" * int(tag[1:]) + " ")

    def handle_data(self, data: str) -> None:
        self.parts.append(data)


def _strip_tags(html: str) -> str:
    extractor = _TextExtractor()
    extractor.feed(html)
    text = "".join(extractor.parts)
    return "\n".join(line.strip() for line in text.splitlines() if line.strip())


__all__ = ["router", "build_llms_txt", "build_llms_full", "page_text", "FAQ_HOME"]
