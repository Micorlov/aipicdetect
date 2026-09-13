"""Lightweight checks for embedded metadata, used by the CLI and tests."""

from __future__ import annotations

# Byte signatures that identify metadata containers inside image files.
METADATA_SIGNATURES: dict[str, tuple[bytes, ...]] = {
    "EXIF": (b"Exif\x00\x00",),
    "XMP": (b"http://ns.adobe.com/xap/1.0/", b"<x:xmpmeta", b"XML:com.adobe.xmp"),
    "IPTC": (b"Photoshop 3.0", b"8BIM"),
    "C2PA": (b"jumb", b"c2pa", b"caBX", b"jumd"),
    "ICC": (b"ICC_PROFILE", b"iCCP"),
}

JPEG_SOI = b"\xff\xd8"
JPEG_MARKER_PREFIX = 0xFF
JPEG_APP0 = 0xE0
JPEG_APP15 = 0xEF
JPEG_SOS = 0xDA
STANDALONE_MARKERS = frozenset({0xD8, 0x01, *range(0xD0, 0xD8)})


def find_metadata(data: bytes) -> dict[str, list[str]]:
    """Return {category: [matched signatures]} for every signature present."""
    found: dict[str, list[str]] = {}
    for category, signatures in METADATA_SIGNATURES.items():
        hits = [sig.decode("latin-1") for sig in signatures if sig in data]
        if hits:
            found[category] = hits
    return found


def jpeg_app_markers(data: bytes) -> list[int]:
    """List the APPn marker numbers (0..15) present before the scan segment."""
    if not data.startswith(JPEG_SOI):
        return []
    markers: list[int] = []
    pos = len(JPEG_SOI)
    while pos + 4 <= len(data) and data[pos] == JPEG_MARKER_PREFIX:
        marker = data[pos + 1]
        if marker == JPEG_SOS:
            break
        if marker in STANDALONE_MARKERS:
            pos += 2
            continue
        length = int.from_bytes(data[pos + 2 : pos + 4], "big")
        if JPEG_APP0 <= marker <= JPEG_APP15:
            markers.append(marker - JPEG_APP0)
        pos += 2 + length
    return markers
