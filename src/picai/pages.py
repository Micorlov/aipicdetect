"""Page registry and HTML rendering for the home page and the content pages.

Every public page is a ``Page`` in ``PAGES``. Body fragments live in
``static/pages/<slug>.html`` and are wrapped in ``_layout.html``; the home page is
``static/index.html``. Both use ``{{KEY}}`` placeholders filled by :func:`render`.
The public origin comes from ``PICAI_PUBLIC_URL`` when set, otherwise the request.
"""

from __future__ import annotations

import hashlib
import os
import re
from dataclasses import dataclass
from datetime import date
from html import escape
from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from picai.content import home as copy
from picai.content.faq import FAQ_ALL, FAQ_HOME, FaqEntry
from picai.content.home import Step
from picai.detect import DEFAULT_MODEL
from picai.limits import DEFAULT_DAILY_LIMIT, MAX_UPLOAD_MB, RESULT_CACHE_LIMIT
from picai.schema import jsonld_for_page

STATIC_DIR = Path(__file__).parent / "static"
PAGES_DIR = STATIC_DIR / "pages"
INDEX_FILE = STATIC_DIR / "index.html"
LAYOUT_FILE = PAGES_DIR / "_layout.html"
HEAD_FILE = PAGES_DIR / "_head.html"
NOT_FOUND_FILE = PAGES_DIR / "404.html"
PUBLIC_URL_ENV = "PICAI_PUBLIC_URL"
GSC_ENV = "PICAI_GSC_VERIFICATION"
BING_ENV = "PICAI_BING_VERIFICATION"
GA_ENV = "PICAI_GA_MEASUREMENT_ID"
GA_ID_PATTERN = re.compile(r"^G-[A-Z0-9]{4,20}$")
OG_IMAGE_PATH = "/static/og/picai-og.png"
PLACEHOLDER = re.compile(r"\{\{([A-Z0-9_]+)\}\}")
LAST_REVIEWED = date(2026, 9, 13)
VERSIONED_ASSETS = ("styles.css", "pages.css", "app.js")


def asset_version() -> str:
    """Short content hash of the CSS/JS bundle, appended as ``?v=`` so long cache lifetimes are safe."""
    digest = hashlib.sha1()
    for name in VERSIONED_ASSETS:
        digest.update((STATIC_DIR / name).read_bytes())
    return digest.hexdigest()[:10]


ASSET_VERSION = asset_version()


@dataclass(frozen=True)
class Page:
    slug: str  # "" for the home page
    title: str  # 50-60 chars
    description: str  # 120-160 chars
    h1: str
    section: str  # Product | Guides | Developers (llms.txt grouping)
    schema_types: tuple[str, ...] = ()
    lastmod: date = LAST_REVIEWED
    nav_label: str | None = None
    footer_label: str | None = None
    priority: float = 0.5

    @property
    def path(self) -> str:
        return f"/{self.slug}"

    @property
    def file(self) -> Path:
        return INDEX_FILE if self.is_home else PAGES_DIR / f"{self.slug}.html"

    @property
    def is_home(self) -> bool:
        return self.slug == ""


PAGES: tuple[Page, ...] = (
    Page(
        "",
        "picai: Free Open-Source AI Image Detector (Online & Local)",
        "Check whether a picture is AI-generated with picai, a free open-source detector. Use it in "
        "the browser or run it on your own machine with Docker or Python.",
        "Detect AI-generated images. Free and open source.",
        "Product",
        ("WebSite", "SoftwareApplication", "FAQPage", "HowTo"),
        priority=1.0,
    ),
    Page(
        "how-to-tell-if-an-image-is-ai-generated",
        "How to Tell If an Image Is AI-Generated (2026 Guide)",
        "A practical checklist for spotting AI-generated images: visual tells, C2PA and EXIF "
        "metadata, reverse image search, and how to read a detector score.",
        "How to tell if an image is AI-generated",
        "Guides",
        ("Article",),
        nav_label="Guide",
        priority=0.8,
    ),
    Page(
        "how-accurate",
        "How Accurate Are AI Image Detectors? Reading a picai Score",
        "AI image detectors give probabilities, not proof. How picai turns classifier scores into "
        "a percentage and confidence band, and where detectors fail.",
        "How accurate is an AI image detector?",
        "Guides",
        ("Article",),
        priority=0.7,
    ),
    Page(
        "remove-image-metadata",
        "Remove EXIF, XMP, IPTC and C2PA Metadata from Images",
        "Strip EXIF, XMP, IPTC, ICC and C2PA content credentials from JPEG, PNG, WebP and HEIC "
        "files by re-rendering the pixels with picai's free CLI or HTTP API.",
        "Remove all metadata from an image",
        "Guides",
        ("HowTo",),
        footer_label="Remove metadata",
        priority=0.8,
    ),
    Page(
        "c2pa",
        "C2PA Content Credentials: How to Check and Remove Them",
        "What C2PA content credentials are, how picai finds them next to EXIF, XMP, IPTC and ICC "
        "blocks, and how re-rendering an image leaves every one of them behind.",
        "C2PA content credentials: what they are and how picai handles them",
        "Guides",
        ("Article",),
        footer_label="C2PA",
        priority=0.6,
    ),
    Page(
        "faq",
        "AI Image Detector FAQ: Accuracy, Privacy, Formats, Models",
        "Answers to common questions about picai: how accurate AI image detection is, where your "
        "image is processed, supported formats, model swapping and rate limits.",
        "picai frequently asked questions",
        "Product",
        ("FAQPage",),
        footer_label="FAQ",
        priority=0.6,
    ),
    Page(
        "privacy",
        "Privacy: What Happens to Images You Upload to picai",
        "picai processes uploads in memory, never writes them to disk, keeps scrubbed copies only "
        "briefly and sends no image to any third-party service.",
        "What happens to an image you upload",
        "Product",
        ("Article",),
        footer_label="Privacy",
        priority=0.5,
    ),
    Page(
        "api",
        "picai API: Detect AI Images and Scrub Metadata with curl",
        "Reference for picai's HTTP API: POST /analyze for an AI likelihood plus metadata report, "
        "POST /scrub for a clean re-rendered image, plus curl examples.",
        "picai HTTP API",
        "Developers",
        ("TechArticle",),
        nav_label="API",
        priority=0.7,
    ),
    Page(
        "self-host",
        "Self-Host picai: AI Image Detector with Docker or uv",
        "Run picai on your own machine or server with one Docker command or with uv. Model "
        "download size, environment variables, phone access and Cloud Run notes.",
        "Run picai on your own machine",
        "Developers",
        ("TechArticle",),
        nav_label="Self-host",
        footer_label="Self-host",
        priority=0.7,
    ),
    Page(
        "about",
        "About picai: Author, Model Credits and How to Cite",
        "Who builds picai, which open-source model powers the AI image detector, the licence it "
        "ships under, and how to cite the project in an article or paper.",
        "About picai",
        "Developers",
        ("Article",),
        footer_label="About",
        priority=0.4,
    ),
)
HOME = PAGES[0]
_PAGES_BY_PATH = {page.path: page for page in PAGES}

router = APIRouter(include_in_schema=False)


def page_for(path: str) -> Page | None:
    return _PAGES_BY_PATH.get(path)


def normalise_public_url(value: str) -> str:
    """Strip whitespace and trailing slashes; reject anything that is not an http(s) origin."""
    origin = value.strip().rstrip("/")
    if not re.match(r"^https?://[^/\s]+$", origin):
        raise ValueError(f"{PUBLIC_URL_ENV} must be an http(s) origin without a path, got {value!r}")
    return origin


def public_url(request: Request) -> str:
    """Origin used for absolute URLs: ``PICAI_PUBLIC_URL`` if set, else the request's base."""
    configured = os.environ.get(PUBLIC_URL_ENV, "")
    if configured.strip():
        return normalise_public_url(configured)
    return str(request.base_url).rstrip("/")


def render(template: str, values: dict[str, str]) -> str:
    """Single-pass ``{{KEY}}`` substitution; unknown keys are an error, not silent output."""

    def replace(match: re.Match[str]) -> str:
        key = match.group(1)
        if key not in values:
            raise KeyError(f"template placeholder {key} has no value")
        return values[key]

    return PLACEHOLDER.sub(replace, template)


def render_head(page: Page, origin: str) -> str:
    return render(
        HEAD_FILE.read_text(encoding="utf-8"),
        {
            "TITLE": escape(page.title),
            "DESCRIPTION": escape(page.description),
            "CANONICAL": escape(f"{origin}{page.path}"),
            "OG_IMAGE": escape(f"{origin}{OG_IMAGE_PATH}"),
            "OG_TYPE": "website" if page.is_home else "article",
            "VERIFICATION": verification_tags(),
            "ANALYTICS": analytics_tag(),
            "EXTRA_CSS": "" if page.is_home else f'<link rel="stylesheet" href="/static/pages.css?v={ASSET_VERSION}">',
            "ASSET_V": ASSET_VERSION,
            "JSONLD": jsonld_for_page(page, origin),
        },
    )


def verification_tags() -> str:
    tags = []
    google = os.environ.get(GSC_ENV, "").strip()
    bing = os.environ.get(BING_ENV, "").strip()
    if google:
        tags.append(f'<meta name="google-site-verification" content="{escape(google)}">')
    if bing:
        tags.append(f'<meta name="msvalidate.01" content="{escape(bing)}">')
    return "\n".join(tags)


def analytics_tag() -> str:
    """Google tag (gtag.js) for the hosted instance; empty unless ``PICAI_GA_MEASUREMENT_ID`` is set.

    Self-hosted deployments get no analytics unless the operator sets this themselves.
    """
    measurement_id = os.environ.get(GA_ENV, "").strip()
    if not measurement_id:
        return ""
    if not GA_ID_PATTERN.match(measurement_id):
        raise ValueError(f"{GA_ENV} must look like G-XXXXXXXXXX, got {measurement_id!r}")
    safe_id = measurement_id
    return (
        f'<script async src="https://www.googletagmanager.com/gtag/js?id={safe_id}"></script>\n'
        "<script>\n"
        "  window.dataLayer = window.dataLayer || [];\n"
        "  function gtag(){dataLayer.push(arguments);}\n"
        "  gtag('js', new Date());\n"
        f"  gtag('config', '{safe_id}');\n"
        "</script>"
    )


def nav_links(current: Page) -> str:
    links = ['<a href="/#tool"{}>Detector</a>'.format(' class="active"' if current.is_home else "")]
    links.append('<a href="/#how">How it works</a>')
    for page in PAGES:
        if page.nav_label:
            active = ' class="active"' if page == current else ""
            links.append(f'<a href="{page.path}"{active}>{escape(page.nav_label)}</a>')
    return "\n    ".join(links)


def footer_links() -> str:
    links = [f'<a href="{p.path}">{escape(p.footer_label)}</a>' for p in PAGES if p.footer_label]
    links.append(f'<a href="{copy.REPO_URL}" rel="noopener">GitHub</a>')
    return "\n  ".join(links)


def render_faq(entries: tuple[FaqEntry, ...]) -> str:
    return "\n".join(
        f"<details><summary>{escape(e.question)}</summary><p>{e.answer_html}</p></details>" for e in entries
    )


def render_steps(steps: tuple[Step, ...]) -> str:
    items = []
    for index, step in enumerate(steps, start=1):
        featured = ' class="featured"' if index == 1 else ""
        items.append(
            f'<li{featured}><span class="step-num">{index:02d}</span><h3>{escape(step.name)}</h3><p>{step.text}</p></li>'
        )
    return "\n".join(items)


def body_values(page: Page, origin: str) -> dict[str, str]:
    """Placeholders available inside body fragments and index.html."""
    return {
        "ORIGIN": escape(origin),
        "LEAD": escape(copy.LEAD),
        "ENTITY": escape(copy.ENTITY_SENTENCE),
        "DROPZONE_NOTE": escape(copy.DROPZONE_NOTE),
        "STATS": "".join(f"<li><strong>{n}</strong><span>{label}.</span></li>" for n, label in copy.STATS),
        "STEPS": render_steps(copy.DETECT_STEPS),
        "SCRUB_STEPS": render_steps(copy.SCRUB_STEPS),
        "FAQ": render_faq(FAQ_HOME),
        "FAQ_ALL": render_faq(FAQ_ALL),
        "NAV": nav_links(page),
        "FOOTER_LINKS": footer_links(),
        "MODEL": escape(DEFAULT_MODEL),
        "MAX_UPLOAD_MB": str(MAX_UPLOAD_MB),
        "RESULT_CACHE_LIMIT": str(RESULT_CACHE_LIMIT),
        "DAILY_LIMIT": str(DEFAULT_DAILY_LIMIT),
        "REPO_URL": copy.REPO_URL,
        "AUTHOR": escape(copy.AUTHOR),
        "LASTMOD": page.lastmod.isoformat(),
        "H1": escape(page.h1),
        "ASSET_V": ASSET_VERSION,
    }


def render_page(page: Page, origin: str) -> str:
    values = body_values(page, origin)
    values["HEAD"] = render_head(page, origin)
    if page.is_home:
        return render(INDEX_FILE.read_text(encoding="utf-8"), values)
    values["BODY"] = render(page.file.read_text(encoding="utf-8"), values)
    return render(LAYOUT_FILE.read_text(encoding="utf-8"), values)


def render_not_found(origin: str) -> str:
    page = Page("404", "Page not found | picai", "This page does not exist.", "Page not found", "Product")
    values = body_values(page, origin)
    values["HEAD"] = render_head(page, origin).replace('content="index, follow', 'content="noindex')
    values["BODY"] = render(NOT_FOUND_FILE.read_text(encoding="utf-8"), values)
    return render(LAYOUT_FILE.read_text(encoding="utf-8"), values)


def _endpoint(page: Page):
    def serve(request: Request) -> HTMLResponse:
        return HTMLResponse(render_page(page, public_url(request)))

    serve.__name__ = f"page_{page.slug or 'home'}"
    return serve


for _page in PAGES:
    router.add_api_route(_page.path, _endpoint(_page), methods=["GET"], response_class=HTMLResponse)
