from importlib import import_module

from starlette.requests import Request

from aipicdetect.i18n import (
    DEFAULT_LOCALE,
    LANG_COOKIE,
    LOCALE_NAMES,
    RTL_LOCALES,
    SUPPORTED_LOCALES,
    direction,
    parse_accept_language,
    resolve_locale,
)


def _request(query_string: str = "", headers: dict[str, str] | None = None) -> Request:
    raw_headers = [(k.lower().encode(), v.encode()) for k, v in (headers or {}).items()]
    scope = {
        "type": "http",
        "headers": raw_headers,
        "query_string": query_string.encode(),
        "client": ("127.0.0.1", 12345),
    }
    return Request(scope)


# --- constants ---------------------------------------------------------------


def test_supported_locales_default_and_rtl_membership():
    assert SUPPORTED_LOCALES[0] == DEFAULT_LOCALE == "en"
    assert RTL_LOCALES == {"he", "ar", "ur", "fa"}
    assert set(LOCALE_NAMES) == set(SUPPORTED_LOCALES)
    assert LANG_COOKIE == "aipicdetect_lang"


# --- parse_accept_language ----------------------------------------------------


def test_parse_accept_language_orders_by_descending_quality():
    # Arrange
    header = "en-US,en;q=0.9,he;q=0.8"

    # Act
    result = parse_accept_language(header)

    # Assert
    assert result == ["en", "he"]


def test_parse_accept_language_handles_q_values_out_of_order():
    # Arrange
    header = "he;q=0.5,fr;q=0.9,en;q=0.7"

    # Act
    result = parse_accept_language(header)

    # Assert
    assert result == ["fr", "en", "he"]


def test_parse_accept_language_skips_malformed_segments():
    # Arrange: a bad q-value and an empty tag are both dropped, not raised
    header = "en;q=notanumber,he;q=0.8,;garbage,fr"

    # Act
    result = parse_accept_language(header)

    # Assert
    assert result == ["fr", "he"]


def test_parse_accept_language_returns_empty_list_for_empty_header():
    assert parse_accept_language("") == []


def test_parse_accept_language_strips_region_subtags_and_deduplicates():
    # Arrange
    header = "en-US,en-GB;q=0.9,en;q=0.8"

    # Act
    result = parse_accept_language(header)

    # Assert
    assert result == ["en"]


# --- resolve_locale ------------------------------------------------------------


def test_resolve_locale_prefers_query_param_over_cookie_and_header():
    # Arrange
    request = _request(query_string="lang=he", headers={"cookie": "aipicdetect_lang=es", "accept-language": "fr"})

    # Act / Assert
    assert resolve_locale(request) == "he"


def test_resolve_locale_ignores_unsupported_query_param_and_falls_back_to_cookie():
    # Arrange
    request = _request(query_string="lang=xx", headers={"cookie": "aipicdetect_lang=es"})

    # Act / Assert
    assert resolve_locale(request) == "es"


def test_resolve_locale_prefers_cookie_over_accept_language_header():
    # Arrange
    request = _request(headers={"cookie": "aipicdetect_lang=de", "accept-language": "fr"})

    # Act / Assert
    assert resolve_locale(request) == "de"


def test_resolve_locale_falls_back_to_accept_language_header():
    # Arrange
    request = _request(headers={"accept-language": "fr-FR,fr;q=0.9,en;q=0.8"})

    # Act / Assert
    assert resolve_locale(request) == "fr"


def test_resolve_locale_skips_unsupported_codes_in_accept_language():
    # Arrange
    request = _request(headers={"accept-language": "xx,zz;q=0.9,ru;q=0.5"})

    # Act / Assert
    assert resolve_locale(request) == "ru"


def test_resolve_locale_defaults_to_english_when_nothing_matches():
    # Arrange
    request = _request()

    # Act / Assert
    assert resolve_locale(request) == DEFAULT_LOCALE


# --- direction -----------------------------------------------------------------


def test_direction_is_rtl_for_hebrew_and_arabic():
    assert direction("he") == "rtl"
    assert direction("ar") == "rtl"


def test_direction_is_ltr_for_default_locale():
    assert direction(DEFAULT_LOCALE) == "ltr"


# --- translation tables ---------------------------------------------------------


def test_all_locales_have_the_same_keys_as_english():
    """All locales must define every core key that English defines.

    Page-meta keys for non-home/faq pages (page.<slug>.title/description/h1) are
    intentionally optional: missing keys fall back to the English value via t().
    """
    import re as _re
    _optional_pattern = _re.compile(r"^page\.(?!home\.|faq\.).")
    english_strings = import_module("aipicdetect.content.locales.en").STRINGS
    required_keys = {k for k in english_strings if not _optional_pattern.match(k)}

    for locale in SUPPORTED_LOCALES:
        keys = set(import_module(f"aipicdetect.content.locales.{locale}").STRINGS)
        all_en_keys = set(english_strings)
        # Must have all required (non-optional) English keys
        missing_required = required_keys - keys
        assert not missing_required, f"{locale} missing required keys: {missing_required}"
        # Must not define keys that English does not have
        extra = keys - all_en_keys
        assert not extra, f"{locale} has extra keys not in English: {extra}"
