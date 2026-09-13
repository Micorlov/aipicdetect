from io import BytesIO

import pytest
from fastapi.testclient import TestClient
from PIL import Image

from picai import server
from picai.detect import Detector

client = TestClient(server.app)


def _png() -> bytes:
    buffer = BytesIO()
    Image.new("RGBA", (12, 12), (0, 0, 255, 120)).save(buffer, format="PNG")
    return buffer.getvalue()


@pytest.fixture(autouse=True)
def fake_detector(monkeypatch):
    detector = Detector(
        model_name="fake/model",
        classifier=lambda image: [{"label": "ai", "score": 0.2}, {"label": "hum", "score": 0.8}],
    )
    monkeypatch.setattr(server, "get_detector", lambda: detector)
    return detector


def test_analyze_reports_real_classification():
    body = client.post("/analyze", files={"file": ("pic.png", _png(), "image/png")}).json()
    assert body["detection"]["classification"] == "Real"
    assert body["detection"]["confidence"] == "Medium"
    assert body["detection"]["percent"] == 20


def test_analyze_honours_format_and_quality():
    response = client.post("/analyze?format=webp&quality=80", files={"file": ("pic.png", _png(), "image/png")})
    body = response.json()
    assert body["output"]["format"] == "WEBP"
    assert body["download_name"] == "pic.clean.webp"
    assert client.get(body["download_url"]).headers["content-type"] == "image/webp"


def test_analyze_rejects_bad_format_and_quality():
    assert client.post("/analyze?format=gif", files={"file": ("p.png", _png(), "image/png")}).status_code == 422
    assert client.post("/analyze?quality=0", files={"file": ("p.png", _png(), "image/png")}).status_code == 422
    assert client.post("/analyze?quality=101", files={"file": ("p.png", _png(), "image/png")}).status_code == 422


def test_empty_upload_is_400():
    assert client.post("/analyze", files={"file": ("empty.png", b"", "image/png")}).status_code == 400
    assert client.post("/scrub", files={"file": ("empty.png", b"", "image/png")}).status_code == 400


def test_oversized_upload_is_413(monkeypatch):
    monkeypatch.setattr(server, "MAX_UPLOAD_BYTES", 64)
    assert client.post("/analyze", files={"file": ("big.png", _png(), "image/png")}).status_code == 413


def test_filename_without_extension_still_gets_download_name():
    body = client.post("/analyze", files={"file": ("noext", _png(), "image/png")}).json()
    assert body["download_name"] == "noext.clean.png"


def test_result_cache_evicts_oldest(monkeypatch):
    monkeypatch.setattr(server, "RESULT_CACHE_LIMIT", 2)
    with server._results_lock:
        server._results.clear()

    ids = [client.post("/analyze", files={"file": ("p.png", _png(), "image/png")}).json()["id"] for _ in range(3)]

    assert client.get(f"/download/{ids[0]}").status_code == 404
    assert client.get(f"/download/{ids[1]}").status_code == 200
    assert client.get(f"/download/{ids[2]}").status_code == 200


def test_status_reports_unloaded_model(monkeypatch):
    monkeypatch.setattr(server, "get_detector", lambda: Detector(model_name="lazy/model"))
    assert client.get("/status").json() == {"model": "lazy/model", "model_loaded": False}


def test_index_page_references_analyze_and_download_flow():
    html = client.get("/").text
    assert "/static/app.js" in html and 'id="dropzone"' in html
    js = client.get("/static/app.js").text
    assert "/analyze" in js and "/status" in js


def test_static_assets_are_served():
    css = client.get("/static/styles.css")
    js = client.get("/static/app.js")
    assert css.status_code == 200 and "text/css" in css.headers["content-type"]
    assert js.status_code == 200 and "javascript" in js.headers["content-type"]


def test_pwa_manifest_and_icons_are_served():
    manifest = client.get("/static/manifest.json")
    assert manifest.status_code == 200
    icons = [icon["src"] for icon in manifest.json()["icons"]]
    assert icons and all(client.get(src).status_code == 200 for src in icons)
    assert client.get("/static/icons/apple-touch-icon.png").status_code == 200


def test_static_unknown_file_is_404():
    assert client.get("/static/missing.js").status_code == 404
