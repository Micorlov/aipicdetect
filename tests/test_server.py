from io import BytesIO

import pytest
from fastapi.testclient import TestClient
from PIL import Image

from picai import server
from picai.detect import Detector
from picai.inspect import find_metadata

client = TestClient(server.app)


def _jpeg_with_exif() -> bytes:
    exif = Image.Exif()
    exif[0x0110] = "AI Camera"
    buffer = BytesIO()
    Image.new("RGB", (16, 16), "blue").save(buffer, format="JPEG", exif=exif.tobytes())
    return buffer.getvalue()


@pytest.fixture(autouse=True)
def fake_detector(monkeypatch):
    detector = Detector(
        model_name="fake/model",
        classifier=lambda image: [{"label": "ai", "score": 0.97}, {"label": "hum", "score": 0.03}],
    )
    monkeypatch.setattr(server, "get_detector", lambda: detector)
    return detector


def test_health_and_status():
    assert client.get("/health").json() == {"status": "ok"}
    assert client.get("/status").json() == {"model": "fake/model", "model_loaded": True}


def test_index_serves_dashboard_page():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert 'type="file"' in response.text and "/analyze" in response.text


def test_analyze_returns_detection_metadata_and_download_link():
    response = client.post("/analyze", files={"file": ("photo.jpg", _jpeg_with_exif(), "image/jpeg")})

    assert response.status_code == 200
    body = response.json()
    assert body["detection"] == {
        "ai_likelihood": 0.97, "percent": 97, "confidence": "High", "classification": "AI", "model": "fake/model",
    }
    assert "EXIF" in body["metadata"]["removed"]
    assert body["input"]["width"] == 16 and body["output"]["format"] == "JPEG"
    assert body["download_name"] == "photo.clean.jpg"

    download = client.get(body["download_url"])
    assert download.status_code == 200
    assert download.headers["content-type"] == "image/jpeg"
    assert 'filename="photo.clean.jpg"' in download.headers["content-disposition"]
    assert find_metadata(download.content) == {}


def test_download_unknown_id_is_404():
    assert client.get("/download/nope").status_code == 404


def test_scrub_endpoint_still_returns_clean_image():
    response = client.post("/scrub", files={"file": ("photo.jpg", _jpeg_with_exif(), "image/jpeg")})
    assert response.status_code == 200
    assert "EXIF" in response.headers["x-picai-removed"].split(",")
    assert find_metadata(response.content) == {}


def test_analyze_rejects_non_image():
    response = client.post("/analyze", files={"file": ("x.txt", b"hello", "text/plain")})
    assert response.status_code == 415
