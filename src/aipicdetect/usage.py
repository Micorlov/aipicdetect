"""Usage numbers for the admin dashboard.

Visitors come from the GA4 Data API (the public pages already load gtag); image uploads
come from Cloud Run's request logs, where ``remoteIp`` is set by Google's front end rather
than by the client. Both sources are optional: without credentials or config the
dashboard shows "unavailable" instead of failing.
"""

from __future__ import annotations

import ipaddress
import os
import re
import threading
import time
from concurrent.futures import Future, ThreadPoolExecutor
from concurrent.futures import TimeoutError as FutureTimeout
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Any, Callable, Iterable

GA_PROPERTY_ENV = "AIPICDETECT_GA_PROPERTY_ID"
SERVICE_ENV = "K_SERVICE"
DEFAULT_SERVICE = "aipicdetect"
SERVICE_PATTERN = re.compile(r"^[a-z0-9-]{1,63}$")
WINDOWS_DAYS = (7, 30)
CACHE_TTL_SECONDS = 300
FETCH_TIMEOUT_SECONDS = 15
LOG_PAGE_SIZE = 1000
LOG_MAX_ENTRIES = 20_000  # rate-limited endpoint; far above any realistic month
TOP_CLIENTS = 20


@dataclass(frozen=True)
class Visitors:
    days: int
    users: int
    page_views: int


@dataclass(frozen=True)
class UploadWindow:
    days: int
    total: int


@dataclass(frozen=True)
class ClientUploads:
    address: str
    uploads: int
    last_seen: datetime


@dataclass(frozen=True)
class Uploads:
    windows: tuple[UploadWindow, ...]
    clients: tuple[ClientUploads, ...]  # busiest first, over the longest window


@dataclass(frozen=True)
class UsageReport:
    visitors: tuple[Visitors, ...] | None
    visitors_error: str | None
    uploads: Uploads | None
    uploads_error: str | None


# --- Google Analytics -----------------------------------------------------------


def ga_property_id() -> str:
    return os.environ.get(GA_PROPERTY_ENV, "").strip()


def fetch_visitors(property_id: str) -> tuple[Visitors, ...]:
    from google.analytics.data_v1beta import BetaAnalyticsDataClient
    from google.analytics.data_v1beta.types import DateRange, Metric, RunReportRequest

    request = RunReportRequest(
        property=f"properties/{property_id}",
        date_ranges=[DateRange(start_date=f"{d}daysAgo", end_date="today", name=f"{d}d") for d in WINDOWS_DAYS],
        metrics=[Metric(name="activeUsers"), Metric(name="screenPageViews")],
    )
    response = BetaAnalyticsDataClient().run_report(request, timeout=FETCH_TIMEOUT_SECONDS)
    return parse_visitors(response.rows)


def parse_visitors(rows: Iterable[Any]) -> tuple[Visitors, ...]:
    """Rows of a multi-range report: one row per range, named ``<days>d``."""
    by_name = {row.dimension_values[0].value: row for row in rows}
    visitors = []
    for days in WINDOWS_DAYS:
        row = by_name.get(f"{days}d")
        users = int(row.metric_values[0].value) if row else 0
        views = int(row.metric_values[1].value) if row else 0
        visitors.append(Visitors(days, users, views))
    return tuple(visitors)


# --- Cloud Run request logs -----------------------------------------------------


def service_name() -> str:
    name = os.environ.get(SERVICE_ENV, DEFAULT_SERVICE).strip()
    return name if SERVICE_PATTERN.match(name) else DEFAULT_SERVICE


def uploads_filter(service: str, since: datetime) -> str:
    return " AND ".join(
        (
            'resource.type="cloud_run_revision"',
            f'resource.labels.service_name="{service}"',
            'logName:"requests"',
            'httpRequest.requestMethod="POST"',
            'httpRequest.requestUrl:"/analyze"',
            "httpRequest.status=200",
            f'timestamp>="{since.isoformat()}"',
        )
    )


def fetch_uploads(now: datetime) -> Uploads:
    from google.cloud import logging as cloud_logging

    since = now - timedelta(days=max(WINDOWS_DAYS))
    entries = cloud_logging.Client().list_entries(
        filter_=uploads_filter(service_name(), since), page_size=LOG_PAGE_SIZE, max_results=LOG_MAX_ENTRIES
    )
    return aggregate_uploads(entries, now)


def valid_address(value: Any) -> str | None:
    """The address if it parses as an IP; ``None`` for anything else (never rendered)."""
    try:
        return str(ipaddress.ip_address(str(value).strip()))
    except ValueError:
        return None


def aggregate_uploads(entries: Iterable[Any], now: datetime) -> Uploads:
    """Entries need ``timestamp`` (aware datetime) and ``http_request`` (dict with ``remoteIp``)."""
    totals = {days: 0 for days in WINDOWS_DAYS}
    counts: dict[str, int] = {}
    last_seen: dict[str, datetime] = {}
    for entry in entries:
        seen = entry.timestamp
        for days in WINDOWS_DAYS:
            if seen >= now - timedelta(days=days):
                totals[days] += 1
        address = valid_address((entry.http_request or {}).get("remoteIp", ""))
        if address is None:
            continue
        counts[address] = counts.get(address, 0) + 1
        last_seen[address] = max(last_seen.get(address, seen), seen)
    clients = sorted(
        (ClientUploads(address, uploads, last_seen[address]) for address, uploads in counts.items()),
        key=lambda c: (-c.uploads, c.address),
    )
    return Uploads(
        windows=tuple(UploadWindow(days, totals[days]) for days in WINDOWS_DAYS),
        clients=tuple(clients[:TOP_CLIENTS]),
    )


# --- report with caching and timeouts --------------------------------------------

_lock = threading.Lock()
_cached: tuple[float, UsageReport] | None = None


def _describe(exc: BaseException) -> str:
    return f"{type(exc).__name__}: {str(exc)[:160]}".rstrip(": ")


def _settle(future: Future) -> tuple[Any, str | None]:
    try:
        return future.result(timeout=FETCH_TIMEOUT_SECONDS), None
    except FutureTimeout:
        return None, f"timed out after {FETCH_TIMEOUT_SECONDS}s"
    except Exception as exc:  # any client/network failure is reported, never raised
        return None, _describe(exc)


def build_report(now: datetime) -> UsageReport:
    property_id = ga_property_id()
    pool = ThreadPoolExecutor(max_workers=2, thread_name_prefix="aipicdetect-usage")
    try:
        uploads_future = pool.submit(fetch_uploads, now)
        visitors_future = pool.submit(fetch_visitors, property_id) if property_id else None
        uploads, uploads_error = _settle(uploads_future)
        if visitors_future is None:
            visitors, visitors_error = None, f"{GA_PROPERTY_ENV} is not set"
        else:
            visitors, visitors_error = _settle(visitors_future)
    finally:
        pool.shutdown(wait=False)  # a hung fetch must not hold the admin page hostage
    return UsageReport(visitors, visitors_error, uploads, uploads_error)


def usage_report(clock: Callable[[], float] = time.time) -> UsageReport:
    """Cached for ``CACHE_TTL_SECONDS`` so reloading the dashboard doesn't re-query Google."""
    global _cached
    with _lock:
        started = clock()
        if _cached is not None and started - _cached[0] < CACHE_TTL_SECONDS:
            return _cached[1]
        report = build_report(datetime.fromtimestamp(started, tz=timezone.utc))
        _cached = (started, report)
        return report


def reset_cache() -> None:
    global _cached
    with _lock:
        _cached = None
