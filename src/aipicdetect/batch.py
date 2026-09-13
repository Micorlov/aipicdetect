"""Batch processing: scrub every image in a folder and write a report."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Callable

from aipicdetect.detect import DetectResult
from aipicdetect.inspect import find_metadata
from aipicdetect.scrub import UnsupportedImageError, scrub_bytes

IMAGE_SUFFIXES = frozenset({".jpg", ".jpeg", ".png", ".webp", ".heic", ".heif", ".bmp", ".tif", ".tiff", ".gif"})
Detect = Callable[[bytes], DetectResult]


@dataclass(frozen=True)
class BatchItem:
    source: str
    output: str | None
    removed: list[str]
    input_bytes: int
    output_bytes: int
    detection: dict[str, Any] | None
    error: str | None = None


def image_files(folder: Path) -> list[Path]:
    return sorted(p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_SUFFIXES)


def process_folder(
    input_dir: Path,
    output_dir: Path,
    output_format: str | None = None,
    quality: int = 95,
    detect: Detect | None = None,
) -> list[BatchItem]:
    output_dir.mkdir(parents=True, exist_ok=True)
    return [_process_one(path, output_dir, output_format, quality, detect) for path in image_files(input_dir)]


def _process_one(path: Path, output_dir: Path, output_format: str | None, quality: int, detect: Detect | None) -> BatchItem:
    payload = path.read_bytes()
    try:
        result = scrub_bytes(payload, output_format, quality)
    except UnsupportedImageError as exc:
        return BatchItem(str(path), None, [], len(payload), 0, None, error=str(exc))
    target = output_dir / f"{path.stem}.clean{result.extension}"
    target.write_bytes(result.data)
    detection = _detection_dict(detect, payload) if detect else None
    return BatchItem(str(path), str(target), sorted(find_metadata(payload)), len(payload), len(result.data), detection)


def _detection_dict(detect: Detect, payload: bytes) -> dict[str, Any]:
    d = detect(payload)
    return {"percent": d.percent, "confidence": d.confidence, "classification": d.classification, "model": d.model}


def write_report(items: list[BatchItem], json_path: Path, markdown_path: Path | None = None) -> str:
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps([asdict(i) for i in items], indent=2))
    markdown = render_markdown(items)
    if markdown_path is not None:
        markdown_path.parent.mkdir(parents=True, exist_ok=True)
        markdown_path.write_text(markdown)
    return markdown


def render_markdown(items: list[BatchItem]) -> str:
    if not items:
        return "## AiPicDetect\n\nNo images found in the inbox.\n"
    has_detection = any(i.detection for i in items)
    header = "| File | Metadata removed | Size | AI likelihood | Verdict | Output |" if has_detection else "| File | Metadata removed | Size | Output |"
    divider = "|---|---|---|---|---|---|" if has_detection else "|---|---|---|---|"
    rows = [header, divider]
    for i in items:
        name = Path(i.source).name
        if i.error:
            rows.append(f"| {name} | – | – | " + ("– | – | " if has_detection else "") + f"error: {i.error} |")
            continue
        removed = ", ".join(i.removed) if i.removed else "none"
        size = f"{_kb(i.input_bytes)} → {_kb(i.output_bytes)}"
        out = Path(i.output).name if i.output else "–"
        if has_detection and i.detection:
            d = i.detection
            rows.append(f"| {name} | {removed} | {size} | {d['percent']}% ({d['confidence']}) | {d['classification']} | {out} |")
        elif has_detection:
            rows.append(f"| {name} | {removed} | {size} | – | – | {out} |")
        else:
            rows.append(f"| {name} | {removed} | {size} | {out} |")
    return "## AiPicDetect\n\n" + "\n".join(rows) + "\n"


def _kb(n: int) -> str:
    return f"{n / 1024:.0f} KB" if n < 1024 * 1024 else f"{n / 1024 / 1024:.1f} MB"
