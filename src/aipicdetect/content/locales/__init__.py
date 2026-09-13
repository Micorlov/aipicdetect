"""Loads each locale's ``STRINGS`` table and exposes a single lookup, :func:`t`.

Falls back to :data:`aipicdetect.i18n.DEFAULT_LOCALE` for an unknown locale or a key missing from a
partially-translated one, so a locale never renders a raw key or crashes.
"""

from __future__ import annotations

from importlib import import_module

from aipicdetect.i18n import DEFAULT_LOCALE, SUPPORTED_LOCALES

_TABLES: dict[str, dict[str, str]] = {
    locale: import_module(f"aipicdetect.content.locales.{locale}").STRINGS for locale in SUPPORTED_LOCALES
}


def t(locale: str, key: str) -> str:
    table = _TABLES.get(locale, _TABLES[DEFAULT_LOCALE])
    value = table.get(key)
    return value if value is not None else _TABLES[DEFAULT_LOCALE][key]
