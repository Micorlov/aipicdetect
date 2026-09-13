"""Page registry and HTML rendering for the home page and the content pages.

Every public page is a ``Page`` in ``PAGES``. Body fragments live in
``static/pages/<slug>.html`` and are wrapped in ``_layout.html``; the home page is
``static/index.html``. Both use ``{{KEY}}`` placeholders filled by :func:`render`.
The public origin comes from ``PICAI_PUBLIC_URL`` when set, otherwise the request.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
from dataclasses import dataclass
from datetime import date
from html import escape
from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from picai.content import home as copy
from picai.content.faq import FaqEntry
from picai.content.home import Step
from picai.content.locales import t
from picai.detect import DEFAULT_MODEL
from picai.i18n import DEFAULT_LOCALE, LANG_COOKIE, LOCALE_NAMES, SUPPORTED_LOCALES, direction, resolve_locale
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
VERSIONED_ASSETS = ("styles.css", "pages.css", "app.js", "admin/admin.css", "admin/admin.js")
LANG_COOKIE_MAX_AGE = 60 * 60 * 24 * 365
_FAQ_HOME_SLUGS: tuple[str, ...] = (
    "accuracy",
    "leaves_computer",
    "open_source",
    "remove_metadata",
    "formats",
    "why_metadata",
    "different_model",
)
_FAQ_MORE_SLUGS: tuple[str, ...] = ("free", "screenshots", "which_generator", "false_positive", "offline", "rate_limit")
_FAQ_ALL_SLUGS: tuple[str, ...] = _FAQ_HOME_SLUGS + _FAQ_MORE_SLUGS
_DETECT_STEP_SLUGS: tuple[str, ...] = ("upload", "detect", "decide")
_SCRUB_STEP_SLUGS: tuple[str, ...] = ("inspect", "scrub", "verify")
_UI_TEXT_KEYS: dict[str, str] = {
    "NAV_ARIA_LABEL": "ui.nav_aria_label",
    "LOADING_STATUS": "ui.loading_status",
    "HERO_OVERLINE": "ui.hero_overline",
    "HERO_HEADING_LINE1": "ui.hero_heading_line1",
    "HERO_HEADING_LINE2": "ui.hero_heading_line2",
    "TOOL_ARIA_LABEL": "ui.tool_aria_label",
    "DROPZONE_ARIA_LABEL": "ui.dropzone_aria_label",
    "DZ_TITLE_FINE": "ui.dropzone_title_fine",
    "DZ_TITLE_COARSE": "ui.dropzone_title_coarse",
    "DZ_SUB_FINE": "ui.dropzone_sub_fine",
    "DZ_SUB_COARSE": "ui.dropzone_sub_coarse",
    "BTN_CHECK_FINE": "ui.btn_check_image_fine",
    "BTN_CHOOSE_COARSE": "ui.btn_choose_photo_coarse",
    "BTN_TAKE_PHOTO": "ui.btn_take_photo",
    "DISMISS_ARIA_LABEL": "ui.dismiss_aria_label",
    "ANALYZING_PREFIX": "ui.analyzing_prefix",
    "ANALYZING_SUFFIX": "ui.analyzing_suffix",
    "VERDICT_OVERLINE": "ui.verdict_overline",
    "METER_REAL": "ui.meter_real",
    "METER_UNCERTAIN": "ui.meter_uncertain",
    "METER_AI": "ui.meter_ai",
    "MODEL_LABEL": "ui.model_label",
    "BTN_CHECK_ANOTHER": "ui.btn_check_another",
    "PREVIEW_OVERLINE": "ui.preview_overline",
    "PREVIEW_ALT": "ui.preview_alt",
    "METADATA_OVERLINE": "ui.metadata_overline",
    "METADATA_HEADING": "ui.metadata_heading",
    "JPEG_SEGMENTS_LABEL": "ui.jpeg_segments_label",
    "BTN_DOWNLOAD_CLEAN": "ui.btn_download_clean",
    "HOW_OVERLINE": "ui.how_it_works_overline",
    "HOW_HEADING": "ui.how_it_works_heading",
    "FAQ_OVERLINE": "ui.faq_overline",
    "FAQ_HEADING": "ui.faq_heading",
    "FAQ_MORE_LINK": "ui.faq_more_link",
    "FOOTER_TAGLINE": "ui.footer_tagline",
    "FOOTER_DETECTOR_LABEL": "ui.footer_detector_label",
    "BREADCRUMB_ARIA_LABEL": "ui.breadcrumb_aria_label",
    "LAST_UPDATED_PREFIX": "ui.last_updated_prefix",
    "SOURCE_ON_GITHUB": "ui.source_on_github",
    "BTN_TRY_DETECTOR": "ui.btn_try_detector",
}
_UI_HTML_KEYS: dict[str, str] = {
    "VERDICT_DISCLAIMER_HTML": "ui.verdict_disclaimer_html",
    "METADATA_SCRUB_NOTE_HTML": "ui.metadata_scrub_note_html",
    "HOW_LINKS_HTML": "ui.how_it_works_links_html",
}
_JS_UI_KEYS: tuple[str, ...] = (
    "loading_status",
    "status_ready",
    "status_unreachable",
    "loading_model_note",
    "error_empty_file",
    "error_file_too_large",
    "error_server_unreachable",
    "verdict_ai",
    "verdict_real",
    "verdict_uncertain",
    "confidence_suffix",
    "format_unknown",
    "metadata_present",
    "metadata_not_present",
    "no_jpeg_segments",
    "quota_remaining",
)


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
        "picai — Open-Source AI Image Detector & Metadata Scrubber",
        "Check whether a picture is AI-generated with picai, a free open-source detector. Use it in "
        "the browser or run it on your own machine with Docker or Python.",
        "Is this photo real? Get the score and the proof.",
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


def localized_page_meta(page: Page, locale: str) -> tuple[str, str, str]:
    """(title, description, h1) as they actually render: localized for home/faq, unchanged otherwise."""
    if page.slug in ("", "faq"):
        prefix = page.slug or "home"
        return (
            t(locale, f"page.{prefix}.title"),
            t(locale, f"page.{prefix}.description"),
            t(locale, f"page.{prefix}.h1"),
        )
    return page.title, page.description, page.h1


def render_head(page: Page, origin: str, locale: str) -> str:
    title, description, _ = localized_page_meta(page, locale)
    return render(
        HEAD_FILE.read_text(encoding="utf-8"),
        {
            "TITLE": escape(title),
            "DESCRIPTION": escape(description),
            "CANONICAL": escape(f"{origin}{page.path}"),
            "OG_IMAGE": escape(f"{origin}{OG_IMAGE_PATH}"),
            "OG_TYPE": "website" if page.is_home else "article",
            "VERIFICATION": verification_tags(),
            "ANALYTICS": analytics_tag(),
            "EXTRA_CSS": "" if page.is_home else f'<link rel="stylesheet" href="/static/pages.css?v={ASSET_VERSION}">',
            "ASSET_V": ASSET_VERSION,
            "JSONLD": jsonld_for_page(page, origin, locale),
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


def nav_links(current: Page, locale: str) -> str:
    links = [
        '<a href="/#tool"{}>{}</a>'.format(
            ' class="active"' if current.is_home else "", escape(t(locale, "nav.detector"))
        )
    ]
    links.append(f'<a href="/#how">{escape(t(locale, "nav.how_it_works"))}</a>')
    for page in PAGES:
        if page.nav_label:
            active = ' class="active"' if page == current else ""
            links.append(f'<a href="{page.path}"{active}>{escape(t(locale, f"nav.{page.slug}"))}</a>')
    return "\n    ".join(links)


def footer_links(locale: str) -> str:
    links = [f'<a href="{p.path}">{escape(t(locale, f"footer.{p.slug}"))}</a>' for p in PAGES if p.footer_label]
    links.append(f'<a href="{copy.REPO_URL}" rel="noopener">GitHub</a>')
    return "\n  ".join(links)


def render_lang_switcher(current_locale: str) -> str:
    options = []
    for code in SUPPORTED_LOCALES:
        selected = " selected" if code == current_locale else ""
        options.append(f'<option value="{code}"{selected}>{escape(LOCALE_NAMES[code])}</option>')
    return (
        '<label class="lang-switcher"><span class="sr-only">Language</span>'
        f'<select onchange="location.search=\'?lang=\'+this.value">{"".join(options)}</select></label>'
    )


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


def localized_faq(locale: str, slugs: tuple[str, ...]) -> tuple[FaqEntry, ...]:
    return tuple(FaqEntry(t(locale, f"faq.{slug}.question"), t(locale, f"faq.{slug}.answer_html")) for slug in slugs)


def localized_steps(locale: str, prefix: str, slugs: tuple[str, ...]) -> tuple[Step, ...]:
    return tuple(
        Step(t(locale, f"steps.{prefix}.{slug}.name"), t(locale, f"steps.{prefix}.{slug}.text")) for slug in slugs
    )


def _ui_values(locale: str) -> dict[str, str]:
    values = {placeholder: escape(t(locale, key)) for placeholder, key in _UI_TEXT_KEYS.items()}
    values.update({placeholder: t(locale, key) for placeholder, key in _UI_HTML_KEYS.items()})
    return values


def body_values(page: Page, origin: str, locale: str = DEFAULT_LOCALE) -> dict[str, str]:
    """Placeholders available inside body fragments and index.html."""
    _, _, h1 = localized_page_meta(page, locale)
    stats = tuple((numeral, t(locale, f"home.stat.{i}")) for i, (numeral, _label) in enumerate(copy.STATS))
    values: dict[str, str] = {
        "ORIGIN": escape(origin),
        "LEAD": escape(t(locale, "home.lead")),
        "ENTITY": escape(t(locale, "home.entity_sentence")),
        "DROPZONE_NOTE": escape(t(locale, "home.dropzone_note")),
        "STATS": "".join(f"<li><strong>{n}</strong><span>{label}.</span></li>" for n, label in stats),
        "STEPS": render_steps(localized_steps(locale, "detect", _DETECT_STEP_SLUGS)),
        "SCRUB_STEPS": render_steps(localized_steps(locale, "scrub", _SCRUB_STEP_SLUGS)),
        "FAQ": render_faq(localized_faq(locale, _FAQ_HOME_SLUGS)),
        "FAQ_ALL": render_faq(localized_faq(locale, _FAQ_ALL_SLUGS)),
        "NAV": nav_links(page, locale),
        "FOOTER_LINKS": footer_links(locale),
        "MODEL": escape(DEFAULT_MODEL),
        "MAX_UPLOAD_MB": str(MAX_UPLOAD_MB),
        "RESULT_CACHE_LIMIT": str(RESULT_CACHE_LIMIT),
        "DAILY_LIMIT": str(DEFAULT_DAILY_LIMIT),
        "REPO_URL": copy.REPO_URL,
        "AUTHOR": escape(copy.AUTHOR),
        "LASTMOD": page.lastmod.isoformat(),
        "H1": escape(h1),
        "ASSET_V": ASSET_VERSION,
        "LANG": locale,
        "DIR": direction(locale),
        "LANG_SWITCHER": render_lang_switcher(locale),
        "FAQ_INTRO_SUFFIX": escape(t(locale, "page.faq.intro_suffix")),
        "FAQ_STILL_UNSURE_HTML": t(locale, "page.faq.still_unsure_html"),
        **_ui_values(locale),
    }
    if page.is_home:
        payload = json.dumps({key: t(locale, f"ui.{key}") for key in _JS_UI_KEYS}, ensure_ascii=False)
        values["PICAI_I18N_JSON"] = payload.replace("</", "<\\/")
    return values


def render_page(page: Page, origin: str, locale: str) -> str:
    values = body_values(page, origin, locale)
    values["HEAD"] = render_head(page, origin, locale)
    if page.is_home:
        return render(INDEX_FILE.read_text(encoding="utf-8"), values)
    values["BODY"] = render(page.file.read_text(encoding="utf-8"), values)
    return render(LAYOUT_FILE.read_text(encoding="utf-8"), values)


def render_not_found(origin: str, locale: str) -> str:
    page = Page("404", "Page not found | picai", "This page does not exist.", "Page not found", "Product")
    values = body_values(page, origin, locale)
    values["HEAD"] = render_head(page, origin, locale).replace('content="index, follow', 'content="noindex')
    values["BODY"] = render(NOT_FOUND_FILE.read_text(encoding="utf-8"), values)
    return render(LAYOUT_FILE.read_text(encoding="utf-8"), values)


def _endpoint(page: Page):
    def serve(request: Request) -> HTMLResponse:
        locale = resolve_locale(request)
        response = HTMLResponse(render_page(page, public_url(request), locale))
        query_lang = request.query_params.get("lang")
        if query_lang in SUPPORTED_LOCALES:
            response.set_cookie(LANG_COOKIE, query_lang, max_age=LANG_COOKIE_MAX_AGE, samesite="lax")
        return response

    serve.__name__ = f"page_{page.slug or 'home'}"
    return serve


for _page in PAGES:
    router.add_api_route(_page.path, _endpoint(_page), methods=["GET"], response_class=HTMLResponse)
