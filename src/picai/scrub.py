"""Rebuild an image from its raw pixels so no embedded metadata survives.

The approach mirrors taking a screenshot: the source file is decoded to a
pixel buffer, a brand-new image object is created from that buffer alone,
and the new image is encoded to a fresh file. Because the new image never
sees the source container, C2PA manifests (JUMBF/APP11), IPTC (APP13),
XMP (APP1), EXIF (APP1), ICC profiles and PNG/WebP text chunks are all
left behind.
"""

from __future__ import annotations

from dataclasses import dataclass
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageOps

# Format name -> (file extension, MIME type)
SUPPORTED_FORMATS: dict[str, tuple[str, str]] = {
    "JPEG": (".jpg", "image/jpeg"),
    "PNG": (".png", "image/png"),
    "WEBP": (".webp", "image/webp"),
}
DEFAULT_JPEG_QUALITY = 95
DEFAULT_WEBP_QUALITY = 95
MAX_PIXELS = 120_000_000  # decompression-bomb guard (~11k x 11k)
ALPHA_MODES = frozenset({"RGBA", "LA", "PA"})

Image.MAX_IMAGE_PIXELS = MAX_PIXELS


class UnsupportedImageError(ValueError):
    """Raised when the input cannot be decoded or the target format is unknown."""


@dataclass(frozen=True)
class ScrubResult:
    data: bytes
    format: str
    extension: str
    media_type: str


def scrub_bytes(
    source: bytes,
    output_format: str | None = None,
    quality: int = DEFAULT_JPEG_QUALITY,
) -> ScrubResult:
    """Decode ``source``, snapshot its pixels, and encode a metadata-free copy."""
    try:
        decoded = Image.open(BytesIO(source))
        decoded.load()
    except (Image.UnidentifiedImageError, OSError, ValueError) as exc:
        raise UnsupportedImageError(f"could not decode image: {exc}") from exc

    fmt = _resolve_format(decoded, output_format)
    snapshot = _snapshot_pixels(decoded, fmt)
    data = _encode(snapshot, fmt, quality)
    extension, media_type = SUPPORTED_FORMATS[fmt]
    return ScrubResult(data=data, format=fmt, extension=extension, media_type=media_type)


def scrub_file(
    input_path: Path,
    output_path: Path | None = None,
    output_format: str | None = None,
    quality: int = DEFAULT_JPEG_QUALITY,
) -> Path:
    """Scrub ``input_path`` and write the result, returning the output path."""
    result = scrub_bytes(input_path.read_bytes(), output_format, quality)
    target = output_path or input_path.with_name(f"{input_path.stem}.clean{result.extension}")
    target.write_bytes(result.data)
    return target


def _resolve_format(decoded: Image.Image, requested: str | None) -> str:
    if requested is not None:
        fmt = requested.upper().replace("JPG", "JPEG")
        if fmt not in SUPPORTED_FORMATS:
            raise UnsupportedImageError(f"unsupported output format: {requested}")
        return fmt
    if decoded.format in SUPPORTED_FORMATS:
        return decoded.format
    return "PNG" if _has_alpha(decoded) else "JPEG"


def _has_alpha(image: Image.Image) -> bool:
    if image.mode in ALPHA_MODES:
        return True
    return image.mode == "P" and "transparency" in image.info


def _snapshot_pixels(decoded: Image.Image, fmt: str) -> Image.Image:
    """Return a new image built only from pixel data (the 'screenshot')."""
    # Apply the EXIF orientation first so the visual result matches the
    # original even though the orientation tag itself is being dropped.
    upright = ImageOps.exif_transpose(decoded) or decoded
    keep_alpha = fmt != "JPEG" and _has_alpha(upright)
    mode = "RGBA" if keep_alpha else "RGB"
    converted = upright.convert(mode)
    return Image.frombytes(mode, converted.size, converted.tobytes())


def _encode(image: Image.Image, fmt: str, quality: int) -> bytes:
    buffer = BytesIO()
    if fmt == "JPEG":
        image.save(buffer, format="JPEG", quality=quality, optimize=True, subsampling="4:2:0")
    elif fmt == "WEBP":
        image.save(buffer, format="WEBP", quality=quality or DEFAULT_WEBP_QUALITY, method=4)
    else:
        image.save(buffer, format="PNG", optimize=True)
    return buffer.getvalue()
