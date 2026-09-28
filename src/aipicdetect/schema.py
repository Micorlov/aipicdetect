"""JSON-LD (schema.org) builders. Each builder returns a dict built from the same copy the
page renders, so structured data can never describe content that is not on the page."""

from __future__ import annotations

import json
from importlib.metadata import PackageNotFoundError, version
from typing import TYPE_CHECKING, Any

from aipicdetect.content import home as copy
from aipicdetect.content.faq import FaqEntry
from aipicdetect.content.home import Step
from aipicdetect.content.locales import t
from aipicdetect.detect import DEFAULT_MODEL

if TYPE_CHECKING:
    from aipicdetect.pages import Page

CONTEXT = "https://schema.org"
MODEL_URL = f"https://huggingface.co/{DEFAULT_MODEL}"
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


def _localized_faq(locale: str, slugs: tuple[str, ...]) -> tuple[FaqEntry, ...]:
    return tuple(FaqEntry(t(locale, f"faq.{slug}.question"), t(locale, f"faq.{slug}.answer_html")) for slug in slugs)


def _localized_steps(locale: str, prefix: str, slugs: tuple[str, ...]) -> tuple[Step, ...]:
    return tuple(
        Step(t(locale, f"steps.{prefix}.{slug}.name"), t(locale, f"steps.{prefix}.{slug}.text")) for slug in slugs
    )


def _localized_h1(page: Page, locale: str) -> str:
    """The page's ``<h1>`` as it actually renders: localized for home/faq, unchanged otherwise."""
    if page.slug in ("", "faq"):
        return t(locale, f"page.{page.slug or 'home'}.h1")
    return page.h1


def software_version() -> str | None:
    try:
        return version("aipicdetect")
    except PackageNotFoundError:
        return None


def person() -> dict[str, Any]:
    return {"@type": "Person", "name": copy.AUTHOR}


def website(origin: str, locale: str) -> dict[str, Any]:
    return {
        "@type": "WebSite",
        "@id": f"{origin}/#website",
        "name": copy.BRAND,
        "url": f"{origin}/",
        "publisher": person(),
        "inLanguage": locale,
    }


def software_application(origin: str, locale: str) -> dict[str, Any]:
    app: dict[str, Any] = {
        "@type": "SoftwareApplication",
        "@id": f"{origin}/#app",
        "name": copy.BRAND,
        "description": t(locale, "home.summary"),
        "url": f"{origin}/",
        "applicationCategory": "MultimediaApplication",
        "operatingSystem": "Web, Linux, macOS, Windows",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "isAccessibleForFree": True,
        "author": person(),
        "isBasedOn": MODEL_URL,
        "codeRepository": copy.REPO_URL,
        "inLanguage": locale,
    }
    if ver := software_version():
        app["softwareVersion"] = ver
    return app


def faq_page(entries: tuple[FaqEntry, ...]) -> dict[str, Any]:
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": e.question, "acceptedAnswer": {"@type": "Answer", "text": e.answer_html}}
            for e in entries
        ],
    }


def how_to(name: str, steps: tuple[Step, ...]) -> dict[str, Any]:
    return {
        "@type": "HowTo",
        "name": name,
        "step": [{"@type": "HowToStep", "position": i, "name": s.name, "text": s.text} for i, s in enumerate(steps, 1)],
    }


def breadcrumb(origin: str, page: Page, locale: str) -> dict[str, Any]:
    return {
        "@type": "BreadcrumbList",
        "inLanguage": locale,
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": copy.BRAND, "item": f"{origin}/"},
            {"@type": "ListItem", "position": 2, "name": _localized_h1(page, locale), "item": f"{origin}{page.path}"},
        ],
    }


def article(origin: str, page: Page, kind: str) -> dict[str, Any]:
    return {
        "@type": kind,
        "headline": page.h1,
        "description": page.description,
        "url": f"{origin}{page.path}",
        "dateModified": page.lastmod.isoformat(),
        "author": person(),
        "publisher": person(),
        "isPartOf": {"@id": f"{origin}/#website"},
    }


def graph_for_page(page: Page, origin: str, locale: str) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    if not page.is_home:
        items.append(breadcrumb(origin, page, locale))
    for kind in page.schema_types:
        if kind == "WebSite":
            items.append(website(origin, locale))
        elif kind == "SoftwareApplication":
            items.append(software_application(origin, locale))
        elif kind == "FAQPage":
            slugs = _FAQ_HOME_SLUGS if page.is_home else _FAQ_ALL_SLUGS
            faq = faq_page(_localized_faq(locale, slugs))
            faq["inLanguage"] = locale
            items.append(faq)
        elif kind == "HowTo":
            prefix = "detect" if page.is_home else "scrub"
            slugs = _DETECT_STEP_SLUGS if page.is_home else _SCRUB_STEP_SLUGS
            howto = how_to(_localized_h1(page, locale), _localized_steps(locale, prefix, slugs))
            howto["inLanguage"] = locale
            items.append(howto)
        else:  # Article / TechArticle
            article_item = article(origin, page, kind)
            article_item["inLanguage"] = locale
            items.append(article_item)
    return items


def jsonld_for_page(page: Page, origin: str, locale: str) -> str:
    items = graph_for_page(page, origin, locale)
    if not items:
        return ""
    payload = json.dumps({"@context": CONTEXT, "@graph": items}, ensure_ascii=False)
    return f'<script type="application/ld+json">{payload.replace("</", "<\\/")}</script>'
