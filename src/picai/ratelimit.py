"""Per-client daily quota for the analyze endpoint (in-memory, sliding 24 h window)."""

from __future__ import annotations

import math
import threading
import time
from collections import deque
from dataclasses import dataclass
from typing import Callable

from starlette.requests import Request

WINDOW_SECONDS = 24 * 60 * 60


@dataclass(frozen=True)
class QuotaStatus:
    limit: int
    remaining: int
    retry_after: int  # seconds until the oldest counted request leaves the window; 0 when allowed

    @property
    def allowed(self) -> bool:
        return self.limit <= 0 or self.remaining > 0

    def headers(self) -> dict[str, str]:
        headers = {"X-RateLimit-Limit": str(self.limit), "X-RateLimit-Remaining": str(self.remaining)}
        if not self.allowed:
            headers["Retry-After"] = str(self.retry_after)
        return headers


class DailyQuota:
    """Allow at most ``limit`` hits per key in any rolling 24 h window. ``limit <= 0`` disables."""

    def __init__(self, limit: int, clock: Callable[[], float] = time.monotonic) -> None:
        self.limit = limit
        self._clock = clock
        self._hits: dict[str, deque[float]] = {}
        self._lock = threading.Lock()

    @property
    def enabled(self) -> bool:
        return self.limit > 0

    def check(self, key: str) -> QuotaStatus:
        with self._lock:
            return self._status(key, self._clock())

    def record(self, key: str) -> QuotaStatus:
        with self._lock:
            now = self._clock()
            if self.enabled:
                self._hits.setdefault(key, deque()).append(now)
            return self._status(key, now)

    def reset(self) -> None:
        with self._lock:
            self._hits.clear()

    def _status(self, key: str, now: float) -> QuotaStatus:
        if not self.enabled:
            return QuotaStatus(limit=0, remaining=0, retry_after=0)
        hits = self._hits.get(key)
        if hits is None:
            return QuotaStatus(self.limit, self.limit, 0)
        cutoff = now - WINDOW_SECONDS
        while hits and hits[0] <= cutoff:
            hits.popleft()
        if not hits:
            del self._hits[key]
            return QuotaStatus(self.limit, self.limit, 0)
        remaining = max(self.limit - len(hits), 0)
        if remaining:
            return QuotaStatus(self.limit, remaining, 0)
        retry_after = max(1, math.ceil(hits[0] + WINDOW_SECONDS - now))
        return QuotaStatus(self.limit, 0, retry_after)


def client_address(request: Request) -> str:
    """Client IP as seen through the Cloud Run proxy (first X-Forwarded-For hop)."""
    forwarded = request.headers.get("x-forwarded-for", "")
    first_hop = forwarded.split(",")[0].strip()
    if first_hop:
        return first_hop
    return request.client.host if request.client else "unknown"
