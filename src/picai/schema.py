"""JSON-LD (schema.org) builders. Each builder returns a dict built from the same copy the
page renders, so structured data can never describe content that is not on the page."""

from __future__ import annotations

import json
from importlib.metadata import PackageNotFoundError, version
from typing import TYPE_CHECKING, Any

from picai.content import home as copy
from picai.content.faq import FAQ_ALL, FAQ_HOME, FaqEntry
from picai.content.home import Step
from picai.detect import DEFAULT_MODEL

if TYPE_CHECKING:
    from picai.pages import Page

CONTEXT = "https://schema.org"
MODEL_URL = f"https://huggingface.co/{DEFAULT_MODEL}"


def software_version() -> str | None:
    try:
        return version("picai")
    except PackageNotFoundError:
        return None


def person() -> dict[str, Any]:
    return {"@type": "Person", "name": copy.AUTHOR, "url": copy.REPO_URL}


def website(origin: str) -> dict[str, Any]:
    return {"@type": "WebSite", "@id": f"{origin}/#website", "name": copy.BRAND, "url": f"{origin}/", "publisher": person()}


def software_application(origin: str) -> dict[str, Any]:
    app: dict[str, Any] = {
        "@type": "SoftwareApplication",
        "@id": f"{origin}/#app",
        "name": copy.BRAND,
        "description": copy.SUMMARY,
        "url": f"{origin}/",
        "applicationCategory": "MultimediaApplication",
        "operatingSystem": "Web, Linux, macOS, Windows",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "isAccessibleForFree": True,
        "license": copy.LICENSE_URL,
        "codeRepository": copy.REPO_URL,
        "author": person(),
        "isBasedOn": MODEL_URL,
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


def breadcrumb(origin: str, page: Page) -> dict[str, Any]:
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": copy.BRAND, "item": f"{origin}/"},
            {"@type": "ListItem", "position": 2, "name": page.h1, "item": f"{origin}{page.path}"},
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


def graph_for_page(page: Page, origin: str) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    if not page.is_home:
        items.append(breadcrumb(origin, page))
    for kind in page.schema_types:
        if kind == "WebSite":
            items.append(website(origin))
        elif kind == "SoftwareApplication":
            items.append(software_application(origin))
        elif kind == "FAQPage":
            items.append(faq_page(FAQ_HOME if page.is_home else FAQ_ALL))
        elif kind == "HowTo":
            steps = copy.DETECT_STEPS if page.is_home else copy.SCRUB_STEPS
            items.append(how_to(page.h1, steps))
        else:  # Article / TechArticle
            items.append(article(origin, page, kind))
    return items


def jsonld_for_page(page: Page, origin: str) -> str:
    items = graph_for_page(page, origin)
    if not items:
        return ""
    payload = json.dumps({"@context": CONTEXT, "@graph": items}, ensure_ascii=False)
    return f'<script type="application/ld+json">{payload.replace("</", "<\\/")}</script>'
