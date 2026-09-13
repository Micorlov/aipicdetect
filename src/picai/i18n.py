"""Locale negotiation: which language to render a page in, and its writing direction."""

from __future__ import annotations

from starlette.requests import Request

SUPPORTED_LOCALES: tuple[str, ...] = (
    "en", "he", "es", "fr", "de", "pt", "ar", "ru", "zh", "hi",
    "ja", "ko", "it", "nl", "pl", "tr", "vi", "th", "id", "uk",
    "el", "cs", "sv", "ro", "hu", "fi", "da", "bn", "ur", "fa",
)
DEFAULT_LOCALE = "en"
RTL_LOCALES: frozenset[str] = frozenset({"he", "ar", "ur", "fa"})
LOCALE_NAMES: dict[str, str] = {
    "en": "English",
    "he": "עברית",
    "es": "Español",
    "fr": "Français",
    "de": "Deutsch",
    "pt": "Português",
    "ar": "العربية",
    "ru": "Русский",
    "zh": "中文",
    "hi": "हिन्दी",
    "ja": "日本語",
    "ko": "한국어",
    "it": "Italiano",
    "nl": "Nederlands",
    "pl": "Polski",
    "tr": "Türkçe",
    "vi": "Tiếng Việt",
    "th": "ไทย",
    "id": "Bahasa Indonesia",
    "uk": "Українська",
    "el": "Ελληνικά",
    "cs": "Čeština",
    "sv": "Svenska",
    "ro": "Română",
    "hu": "Magyar",
    "fi": "Suomi",
    "da": "Dansk",
    "bn": "বাংলা",
    "ur": "اردو",
    "fa": "فارسی",
}
LANG_COOKIE = "picai_lang"


def parse_accept_language(header: str) -> list[str]:
    """Base language codes from an ``Accept-Language`` header, ordered by descending q-value.

    Tolerant of malformed segments: a segment that cannot be parsed is skipped rather than
    raising. Codes are lowercase, region subtags are stripped, and duplicates are dropped
    (keeping the first, highest-ranked, occurrence).
    """
    parsed: list[tuple[float, int, str]] = []
    for index, part in enumerate(header.split(",")):
        part = part.strip()
        if not part:
            continue
        tag, _, param = part.partition(";")
        tag = tag.strip()
        if not tag:
            continue
        quality = 1.0
        param = param.strip()
        if param:
            if not param.startswith("q="):
                continue
            try:
                quality = float(param[2:])
            except ValueError:
                continue
        code = tag.split("-", 1)[0].strip().lower()
        if not code:
            continue
        parsed.append((quality, index, code))
    parsed.sort(key=lambda item: (-item[0], item[1]))
    seen: set[str] = set()
    ordered: list[str] = []
    for _, _, code in parsed:
        if code not in seen:
            seen.add(code)
            ordered.append(code)
    return ordered


def resolve_locale(request: Request) -> str:
    """Locale for this request: ``?lang=`` query param, then the ``picai_lang`` cookie, then
    ``Accept-Language``, then :data:`DEFAULT_LOCALE`."""
    query_lang = request.query_params.get("lang")
    if query_lang in SUPPORTED_LOCALES:
        return query_lang
    cookie_lang = request.cookies.get(LANG_COOKIE)
    if cookie_lang in SUPPORTED_LOCALES:
        return cookie_lang
    for code in parse_accept_language(request.headers.get("accept-language", "")):
        if code in SUPPORTED_LOCALES:
            return code
    return DEFAULT_LOCALE


def direction(locale: str) -> str:
    return "rtl" if locale in RTL_LOCALES else "ltr"
