"""HTTP service: dashboard page, ``POST /analyze`` (detect + scrub) and downloads."""

from __future__ import annotations

import os
import threading
import uuid
from collections import OrderedDict
from contextlib import asynccontextmanager
from io import BytesIO
from pathlib import Path
from typing import Any, AsyncIterator

from fastapi import FastAPI, File, HTTPException, Query, UploadFile
from fastapi.concurrency import run_in_threadpool
from fastapi.responses import FileResponse, Response
from PIL import Image

from picai.detect import DetectResult, get_detector
from picai.inspect import find_metadata, jpeg_app_markers
from picai.scrub import DEFAULT_JPEG_QUALITY, ScrubResult, UnsupportedImageError, scrub_bytes

MAX_UPLOAD_BYTES = 50 * 1024 * 1024
RESULT_CACHE_LIMIT = 100
STATIC_DIR = Path(__file__).parent / "static"
INDEX_PAGE = STATIC_DIR / "index.html"
FORMAT_PATTERN = "^(?i)(jpe?g|png|webp)$"

# id -> (bytes, media type, download filename); newest last
_results: OrderedDict[str, tuple[bytes, str, str]] = OrderedDict()
_results_lock = threading.Lock()


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    if os.environ.get("PICAI_SKIP_WARMUP") != "1":
        threading.Thread(target=get_detector().load, name="picai-warmup", daemon=True).start()
    yield


app = FastAPI(title="picai", description="AI-image likelihood + metadata scrubbing", lifespan=lifespan)


@app.get("/", include_in_schema=False)
def index() -> FileResponse:
    return FileResponse(INDEX_PAGE, media_type="text/html")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/status")
def status() -> dict[str, Any]:
    detector = get_detector()
    return {"model": detector.model_name, "model_loaded": detector.is_loaded}


@app.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    format: str | None = Query(default=None, pattern=FORMAT_PATTERN),
    quality: int = Query(default=DEFAULT_JPEG_QUALITY, ge=1, le=100),
) -> dict[str, Any]:
    payload = await _read_upload(file)
    try:
        scrubbed = scrub_bytes(payload, format, quality)
    except UnsupportedImageError as exc:
        raise HTTPException(status_code=415, detail=str(exc)) from exc
    detection = await run_in_threadpool(get_detector().detect, payload)

    stem = (file.filename or "image").rsplit(".", 1)[0]
    download_name = f"{stem}.clean{scrubbed.extension}"
    result_id = _store_result(scrubbed, download_name)
    return {
        "id": result_id,
        "download_url": f"/download/{result_id}",
        "download_name": download_name,
        "detection": _detection_payload(detection),
        "metadata": {
            "removed": find_metadata(payload),
            "jpeg_app_segments": [f"APP{n}" for n in jpeg_app_markers(payload)],
        },
        "input": _describe_input(payload),
        "output": {"bytes": len(scrubbed.data), "format": scrubbed.format, "media_type": scrubbed.media_type},
    }


@app.post("/scrub")
async def scrub(
    file: UploadFile = File(...),
    format: str | None = Query(default=None, pattern=FORMAT_PATTERN),
    quality: int = Query(default=DEFAULT_JPEG_QUALITY, ge=1, le=100),
) -> Response:
    payload = await _read_upload(file)
    try:
        result = scrub_bytes(payload, format, quality)
    except UnsupportedImageError as exc:
        raise HTTPException(status_code=415, detail=str(exc)) from exc
    stem = (file.filename or "image").rsplit(".", 1)[0]
    return Response(
        content=result.data,
        media_type=result.media_type,
        headers={
            "Content-Disposition": f'attachment; filename="{stem}.clean{result.extension}"',
            "X-Picai-Removed": ",".join(sorted(find_metadata(payload))),
        },
    )


@app.get("/download/{result_id}")
def download(result_id: str) -> Response:
    with _results_lock:
        entry = _results.get(result_id)
    if entry is None:
        raise HTTPException(status_code=404, detail="result expired or unknown")
    data, media_type, filename = entry
    return Response(
        content=data,
        media_type=media_type,
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )


async def _read_upload(file: UploadFile) -> bytes:
    payload = await file.read(MAX_UPLOAD_BYTES + 1)
    if not payload:
        raise HTTPException(status_code=400, detail="empty upload")
    if len(payload) > MAX_UPLOAD_BYTES:
        raise HTTPException(status_code=413, detail="upload exceeds 50 MB")
    return payload


def _store_result(scrubbed: ScrubResult, filename: str) -> str:
    result_id = uuid.uuid4().hex
    with _results_lock:
        _results[result_id] = (scrubbed.data, scrubbed.media_type, filename)
        while len(_results) > RESULT_CACHE_LIMIT:
            _results.popitem(last=False)
    return result_id


def _detection_payload(detection: DetectResult) -> dict[str, Any]:
    return {
        "ai_likelihood": round(detection.ai_likelihood, 4),
        "percent": detection.percent,
        "confidence": detection.confidence,
        "classification": detection.classification,
        "model": detection.model,
    }


def _describe_input(payload: bytes) -> dict[str, Any]:
    try:
        with Image.open(BytesIO(payload)) as image:
            width, height, fmt = image.width, image.height, image.format
    except OSError:
        width = height = 0
        fmt = None
    return {"bytes": len(payload), "width": width, "height": height, "format": fmt}
