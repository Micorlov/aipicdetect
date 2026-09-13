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

from fastapi import FastAPI, File, HTTPException, Query, Request, UploadFile
from fastapi.concurrency import run_in_threadpool
from fastapi.exception_handlers import http_exception_handler
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import HTMLResponse, Response
from fastapi.staticfiles import StaticFiles
from PIL import Image
from starlette.exceptions import HTTPException as StarletteHTTPException

from picai.admin import router as admin_router
from picai.detect import DetectResult, get_detector
from picai.headers import apply_policy
from picai.i18n import resolve_locale
from picai.inspect import find_metadata, jpeg_app_markers
from picai.limits import DEFAULT_DAILY_LIMIT, MAX_UPLOAD_BYTES, MAX_UPLOAD_MB, RESULT_CACHE_LIMIT
from picai.pages import public_url, render_not_found
from picai.pages import router as pages_router
from picai.ratelimit import DailyQuota, QuotaStatus, client_address
from picai.scrub import DEFAULT_JPEG_QUALITY, ScrubResult, UnsupportedImageError, scrub_bytes
from picai.seo import router as seo_router

STATIC_DIR = Path(__file__).parent / "static"
FORMAT_PATTERN = "^(?i)(jpe?g|png|webp)$"
GZIP_MIN_BYTES = 500
# Analyses allowed per client IP in any rolling 24 h window; 0 disables the limit.
DAILY_LIMIT = int(os.environ.get("PICAI_DAILY_LIMIT", DEFAULT_DAILY_LIMIT))

_quota = DailyQuota(DAILY_LIMIT)

# id -> (bytes, media type, download filename); newest last
_results: OrderedDict[str, tuple[bytes, str, str]] = OrderedDict()
_results_lock = threading.Lock()


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    if os.environ.get("PICAI_SKIP_WARMUP") != "1":
        threading.Thread(target=get_detector().load, name="picai-warmup", daemon=True).start()
    yield


app = FastAPI(title="picai", description="AI-image likelihood + metadata scrubbing", lifespan=lifespan)
app.add_middleware(GZipMiddleware, minimum_size=GZIP_MIN_BYTES)
app.middleware("http")(apply_policy)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
app.include_router(pages_router)
app.include_router(seo_router)
app.include_router(admin_router)


@app.exception_handler(StarletteHTTPException)
async def not_found_page(request: Request, exc: StarletteHTTPException) -> Response:
    """Browsers get an HTML 404 page; API clients keep FastAPI's JSON error body."""
    if exc.status_code == 404 and "text/html" in request.headers.get("accept", ""):
        return HTMLResponse(render_not_found(public_url(request), resolve_locale(request)), status_code=404)
    return await http_exception_handler(request, exc)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/status")
def status() -> dict[str, Any]:
    detector = get_detector()
    return {"model": detector.model_name, "model_loaded": detector.is_loaded}


@app.get("/ready")
def ready() -> dict[str, bool]:
    if not get_detector().is_loaded:
        raise HTTPException(status_code=503, detail="detector is still loading")
    return {"ready": True}


@app.post("/analyze")
async def analyze(
    request: Request,
    file: UploadFile = File(...),
    format: str | None = Query(default=None, pattern=FORMAT_PATTERN),
    quality: int = Query(default=DEFAULT_JPEG_QUALITY, ge=1, le=100),
) -> dict[str, Any]:
    client = client_address(request)
    _enforce_quota(client)
    payload = await _read_upload(file)
    try:
        scrubbed = scrub_bytes(payload, format, quality)
    except UnsupportedImageError as exc:
        raise HTTPException(status_code=415, detail=str(exc)) from exc
    detection = await run_in_threadpool(get_detector().detect, payload)

    stem = (file.filename or "image").rsplit(".", 1)[0]
    download_name = f"{stem}.clean{scrubbed.extension}"
    result_id = _store_result(scrubbed, download_name)
    quota = _quota.record(client)
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
        "quota": _quota_payload(quota),
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


def _enforce_quota(client: str) -> None:
    status = _quota.check(client)
    if status.allowed:
        return
    hours = max(1, -(-status.retry_after // 3600))
    raise HTTPException(
        status_code=429,
        detail=f"Daily limit reached: {status.limit} images per 24 hours. Try again in about {hours} h.",
        headers=status.headers(),
    )


def _quota_payload(status: QuotaStatus) -> dict[str, Any] | None:
    if not _quota.enabled:
        return None
    return {"limit": status.limit, "remaining": status.remaining, "window_hours": 24}


async def _read_upload(file: UploadFile) -> bytes:
    payload = await file.read(MAX_UPLOAD_BYTES + 1)
    if not payload:
        raise HTTPException(status_code=400, detail="empty upload")
    if len(payload) > MAX_UPLOAD_BYTES:
        raise HTTPException(status_code=413, detail=f"upload exceeds {MAX_UPLOAD_MB} MB")
    return payload


def result_cache_size() -> int:
    """Scrubbed results currently held in memory (read by the admin dashboard)."""
    with _results_lock:
        return len(_results)


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

