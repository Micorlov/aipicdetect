from io import BytesIO

from fastapi.testclient import TestClient
from PIL import Image

from aipicdetect import server
from aipicdetect.detect import Detector
from aipicdetect.ratelimit import WINDOW_SECONDS, DailyQuota, QuotaSnapshot, client_address

import pytest

client = TestClient(server.app)


def _png() -> bytes:
    buffer = BytesIO()
    Image.new("RGB", (8, 8), "red").save(buffer, format="PNG")
    return buffer.getvalue()


@pytest.fixture(autouse=True)
def fake_detector(monkeypatch):
    detector = Detector(model_name="fake/model", classifier=lambda image: [{"label": "ai", "score": 0.5}])
    monkeypatch.setattr(server, "get_detector", lambda: detector)


def _analyze(ip: str | None = None):
    headers = {"X-Forwarded-For": ip} if ip else {}
    return client.post("/analyze", files={"file": ("p.png", _png(), "image/png")}, headers=headers)


# --- DailyQuota unit tests -------------------------------------------------


def test_quota_counts_down_and_blocks_at_limit():
    now = [1000.0]
    quota = DailyQuota(limit=3, clock=lambda: now[0])

    assert quota.check("a").remaining == 3
    for expected in (2, 1, 0):
        assert quota.check("a").allowed
        assert quota.record("a").remaining == expected

    blocked = quota.check("a")
    assert not blocked.allowed
    assert blocked.retry_after == WINDOW_SECONDS
    assert blocked.headers() == {"X-RateLimit-Limit": "3", "X-RateLimit-Remaining": "0", "Retry-After": str(WINDOW_SECONDS)}


def test_quota_window_slides_after_24_hours():
    now = [0.0]
    quota = DailyQuota(limit=2, clock=lambda: now[0])
    quota.record("a")
    now[0] = 3600
    quota.record("a")
    assert not quota.check("a").allowed

    now[0] = WINDOW_SECONDS + 1  # first hit expired, second still counted
    status = quota.check("a")
    assert status.allowed and status.remaining == 1

    now[0] = WINDOW_SECONDS + 3601
    assert quota.check("a").remaining == 2


def test_quota_keys_are_independent_and_reset_clears_all():
    quota = DailyQuota(limit=1)
    quota.record("a")
    assert not quota.check("a").allowed
    assert quota.check("b").allowed
    quota.reset()
    assert quota.check("a").allowed


def test_quota_disabled_when_limit_is_zero():
    quota = DailyQuota(limit=0)
    for _ in range(50):
        assert quota.record("a").allowed
    assert not quota.enabled


def test_snapshot_is_empty_for_a_fresh_quota():
    quota = DailyQuota(limit=5)
    assert quota.snapshot() == QuotaSnapshot(clients=0, hits=0)


def test_snapshot_aggregates_clients_and_hits_without_exposing_keys():
    quota = DailyQuota(limit=5)
    quota.record("a")
    quota.record("a")
    quota.record("b")
    assert quota.snapshot() == QuotaSnapshot(clients=2, hits=3)


def test_snapshot_prunes_expired_hits():
    now = [0.0]
    quota = DailyQuota(limit=5, clock=lambda: now[0])
    quota.record("a")
    now[0] = WINDOW_SECONDS + 1
    assert quota.snapshot() == QuotaSnapshot(clients=0, hits=0)


def _request(headers: dict[str, str], client_host: str | None = "192.0.2.1"):
    from starlette.requests import Request

    raw_headers = [(k.lower().encode(), v.encode()) for k, v in headers.items()]
    scope = {"type": "http", "headers": raw_headers, "client": (client_host, 12345) if client_host else None}
    return Request(scope)


def test_client_address_trusts_only_the_last_forwarded_hop():
    # Cloud Run appends the IP it observed to X-Forwarded-For rather than replacing it, so
    # every hop except the last is a value the client itself could have sent.
    assert client_address(_request({"x-forwarded-for": "203.0.113.7"})) == "203.0.113.7"
    assert client_address(_request({"x-forwarded-for": "attacker-claim, 203.0.113.7"})) == "203.0.113.7"
    assert client_address(_request({"x-forwarded-for": "a, b, 203.0.113.7"})) == "203.0.113.7"
    assert client_address(_request({})) == "192.0.2.1"  # no header: falls back to the raw TCP peer
    assert client_address(_request({}, client_host=None)) == "unknown"


# --- Endpoint integration --------------------------------------------------


def test_analyze_allows_ten_then_returns_429_for_same_ip():
    for i in range(10):
        response = _analyze("203.0.113.7")
        assert response.status_code == 200, response.text
        assert response.json()["quota"] == {"limit": 10, "remaining": 9 - i, "window_hours": 24}

    blocked = _analyze("203.0.113.7")
    assert blocked.status_code == 429
    assert blocked.headers["X-RateLimit-Remaining"] == "0"
    assert int(blocked.headers["Retry-After"]) > 0
    assert "10 images per 24 hours" in blocked.json()["detail"]


def test_other_ips_keep_their_own_quota():
    for _ in range(10):
        assert _analyze("203.0.113.7").status_code == 200
    assert _analyze("203.0.113.7").status_code == 429
    for _ in range(10):
        assert _analyze("198.51.100.2").status_code == 200
    assert _analyze("198.51.100.2").status_code == 429
    # Cloud Run appends the IP it observed; only the last (rightmost) hop is trustworthy —
    # a client-supplied leading hop must not let someone dodge another IP's exhausted quota.
    assert _analyze("spoofed-client-claim, 198.51.100.2").status_code == 429


def test_rejected_uploads_do_not_consume_quota():
    for _ in range(10):
        response = client.post("/analyze", files={"file": ("x.txt", b"not an image", "text/plain")},
                               headers={"X-Forwarded-For": "203.0.113.9"})
        assert response.status_code == 415
    assert _analyze("203.0.113.9").status_code == 200


def _scrub(ip: str | None = None):
    headers = {"X-Forwarded-For": ip} if ip else {}
    return client.post("/scrub", files={"file": ("p.png", _png(), "image/png")}, headers=headers)


def test_scrub_allows_ten_then_returns_429_for_same_ip():
    for i in range(10):
        response = _scrub("203.0.113.7")
        assert response.status_code == 200, response.text
        assert response.headers["X-RateLimit-Remaining"] == str(9 - i)

    blocked = _scrub("203.0.113.7")
    assert blocked.status_code == 429
    assert blocked.headers["X-RateLimit-Remaining"] == "0"
    assert int(blocked.headers["Retry-After"]) > 0


def test_scrub_and_analyze_share_the_same_daily_quota():
    for _ in range(6):
        assert _analyze("203.0.113.7").status_code == 200
    for _ in range(4):
        assert _scrub("203.0.113.7").status_code == 200
    assert _scrub("203.0.113.7").status_code == 429
    assert _analyze("203.0.113.7").status_code == 429


def test_rejected_scrub_uploads_do_not_consume_quota():
    for _ in range(10):
        response = client.post("/scrub", files={"file": ("x.txt", b"not an image", "text/plain")},
                               headers={"X-Forwarded-For": "203.0.113.9"})
        assert response.status_code == 415
    assert _scrub("203.0.113.9").status_code == 200


def test_quota_can_be_disabled(monkeypatch):
    monkeypatch.setattr(server, "_quota", DailyQuota(limit=0))
    for _ in range(12):
        response = _analyze("203.0.113.7")
        assert response.status_code == 200
        assert response.json()["quota"] is None
