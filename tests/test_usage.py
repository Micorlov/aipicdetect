import time
from datetime import datetime, timedelta, timezone
from types import SimpleNamespace

import pytest

from aipicdetect import usage

NOW = datetime(2026, 9, 13, 12, 0, tzinfo=timezone.utc)


def entry(ip: str, days_ago: float) -> SimpleNamespace:
    return SimpleNamespace(timestamp=NOW - timedelta(days=days_ago), http_request={"remoteIp": ip})


# --- pure helpers ----------------------------------------------------------------


def test_valid_address_accepts_ipv4_and_ipv6_and_rejects_junk():
    assert usage.valid_address(" 203.0.113.7 ") == "203.0.113.7"
    assert usage.valid_address("2001:db8::1") == "2001:db8::1"
    assert usage.valid_address("<script>alert(1)</script>") is None
    assert usage.valid_address("") is None
    assert usage.valid_address(None) is None


def test_aggregate_uploads_counts_windows_and_clients():
    entries = [
        entry("203.0.113.7", 0.5),
        entry("203.0.113.7", 3),
        entry("203.0.113.7", 20),  # outside 7 days, inside 30
        entry("198.51.100.2", 1),
        entry("not-an-ip", 1),  # counted in totals, never listed as a client
    ]
    uploads = usage.aggregate_uploads(entries, NOW)
    assert uploads.windows == (usage.UploadWindow(7, 4), usage.UploadWindow(30, 5))
    assert [(c.address, c.uploads) for c in uploads.clients] == [("203.0.113.7", 3), ("198.51.100.2", 1)]
    assert uploads.clients[0].last_seen == NOW - timedelta(days=0.5)


def test_aggregate_uploads_caps_the_client_list(monkeypatch):
    monkeypatch.setattr(usage, "TOP_CLIENTS", 2)
    entries = [entry(f"10.0.0.{n}", 1) for n in range(5)]
    assert len(usage.aggregate_uploads(entries, NOW).clients) == 2


def test_parse_visitors_maps_named_ranges_and_defaults_missing_to_zero():
    row = lambda name, users, views: SimpleNamespace(  # noqa: E731
        dimension_values=[SimpleNamespace(value=name)],
        metric_values=[SimpleNamespace(value=users), SimpleNamespace(value=views)],
    )
    visitors = usage.parse_visitors([row("30d", "42", "99"), row("7d", "5", "12")])
    assert visitors == (usage.Visitors(7, 5, 12), usage.Visitors(30, 42, 99))
    assert usage.parse_visitors([]) == (usage.Visitors(7, 0, 0), usage.Visitors(30, 0, 0))


def test_uploads_filter_pins_service_method_path_status_and_window():
    text = usage.uploads_filter("aipicdetect", NOW - timedelta(days=30))
    for fragment in ('service_name="aipicdetect"', 'requestMethod="POST"', 'requestUrl:"/analyze"', "status=200", "2026-08-14"):
        assert fragment in text


def test_service_name_falls_back_when_env_is_unsafe(monkeypatch):
    monkeypatch.setenv("K_SERVICE", 'bad" OR 1=1')
    assert usage.service_name() == usage.DEFAULT_SERVICE
    monkeypatch.setenv("K_SERVICE", "aipicdetect-staging")
    assert usage.service_name() == "aipicdetect-staging"


# --- report assembly ------------------------------------------------------------


@pytest.fixture
def fetchers(monkeypatch):
    calls = {"uploads": 0, "visitors": 0}

    def fake_uploads(now):
        calls["uploads"] += 1
        return usage.aggregate_uploads([entry("203.0.113.7", 1)], now)

    def fake_visitors(property_id):
        calls["visitors"] += 1
        return (usage.Visitors(7, 3, 9), usage.Visitors(30, 8, 20))

    monkeypatch.setattr(usage, "fetch_uploads", fake_uploads)
    monkeypatch.setattr(usage, "fetch_visitors", fake_visitors)
    return calls


def test_build_report_succeeds_with_property_set(fetchers, monkeypatch):
    monkeypatch.setenv("AIPICDETECT_GA_PROPERTY_ID", "123")
    report = usage.build_report(NOW)
    assert report.visitors_error is None and report.uploads_error is None
    assert report.visitors[0].users == 3
    assert report.uploads.windows[1].total == 1


def test_build_report_reports_missing_property_without_calling_ga(fetchers, monkeypatch):
    monkeypatch.delenv("AIPICDETECT_GA_PROPERTY_ID", raising=False)
    report = usage.build_report(NOW)
    assert report.visitors is None and "AIPICDETECT_GA_PROPERTY_ID" in report.visitors_error
    assert fetchers["visitors"] == 0
    assert report.uploads is not None


def test_build_report_turns_exceptions_into_messages(monkeypatch):
    monkeypatch.setenv("AIPICDETECT_GA_PROPERTY_ID", "123")

    def boom(*_):
        raise PermissionError("caller lacks logging.entries.list")

    monkeypatch.setattr(usage, "fetch_uploads", boom)
    monkeypatch.setattr(usage, "fetch_visitors", boom)
    report = usage.build_report(NOW)
    assert report.uploads is None and "PermissionError" in report.uploads_error
    assert report.visitors is None and "logging.entries.list" in report.visitors_error


def test_build_report_times_out_a_hung_fetch(monkeypatch):
    monkeypatch.delenv("AIPICDETECT_GA_PROPERTY_ID", raising=False)
    monkeypatch.setattr(usage, "FETCH_TIMEOUT_SECONDS", 0.05)
    monkeypatch.setattr(usage, "fetch_uploads", lambda now: time.sleep(1))
    started = time.monotonic()
    report = usage.build_report(NOW)
    assert time.monotonic() - started < 0.9
    assert report.uploads is None and "timed out" in report.uploads_error


def test_usage_report_is_cached_until_the_ttl_expires(fetchers, monkeypatch):
    monkeypatch.setenv("AIPICDETECT_GA_PROPERTY_ID", "123")
    clock = [1_000_000.0]
    usage.usage_report(clock=lambda: clock[0])
    usage.usage_report(clock=lambda: clock[0] + 10)
    assert fetchers["uploads"] == 1
    clock[0] += usage.CACHE_TTL_SECONDS + 1
    usage.usage_report(clock=lambda: clock[0])
    assert fetchers["uploads"] == 2
