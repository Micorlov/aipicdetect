import os

os.environ["AIPICDETECT_SKIP_WARMUP"] = "1"

import pytest


@pytest.fixture(autouse=True)
def reset_daily_quota():
    from aipicdetect import admin, server

    server._quota.reset()
    admin._login_quota.reset()
    yield
    server._quota.reset()
    admin._login_quota.reset()


@pytest.fixture(autouse=True)
def no_usage_fetch(monkeypatch):
    """Never query Google Analytics / Cloud Logging from tests; individual tests override."""
    from aipicdetect import admin, usage

    unavailable = usage.UsageReport(None, "stubbed", None, "stubbed")
    monkeypatch.setattr(admin, "usage_report", lambda: unavailable)
    usage.reset_cache()
    yield
    usage.reset_cache()
