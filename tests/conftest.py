import os

os.environ["PICAI_SKIP_WARMUP"] = "1"

import pytest


@pytest.fixture(autouse=True)
def reset_daily_quota():
    from picai import server

    server._quota.reset()
    yield
    server._quota.reset()
