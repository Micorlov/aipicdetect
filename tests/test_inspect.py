import struct
import zlib
from io import BytesIO

from PIL import Image, PngImagePlugin

from picai.inspect import find_metadata, jpeg_app_markers


def _segment(marker: int, payload: bytes) -> bytes:
    return bytes([0xFF, marker]) + struct.pack(">H", len(payload) + 2) + payload


def _plain_jpeg() -> bytes:
    buffer = BytesIO()
    Image.new("RGB", (4, 4), "red").save(buffer, format="JPEG")
    return buffer.getvalue()


def test_find_metadata_returns_empty_for_plain_bytes():
    assert find_metadata(b"\xff\xd8\xff\xd9") == {}


def test_find_metadata_reports_each_category_with_matching_signatures():
    data = b"Exif\x00\x00" + b"<x:xmpmeta" + b"8BIM" + b"c2pa" + b"ICC_PROFILE"
    found = find_metadata(data)
    assert set(found) == {"EXIF", "XMP", "IPTC", "C2PA", "ICC"}
    assert found["XMP"] == ["<x:xmpmeta"]


def test_find_metadata_detects_png_text_and_icc_chunks():
    image = Image.new("RGB", (4, 4), "green")
    info = PngImagePlugin.PngInfo()
    info.add_itxt("XML:com.adobe.xmp", "<x:xmpmeta/>")
    buffer = BytesIO()
    image.save(buffer, format="PNG", pnginfo=info, icc_profile=b"\x00" * 16)
    found = find_metadata(buffer.getvalue())
    assert "XMP" in found and "ICC" in found


def test_jpeg_app_markers_returns_empty_for_non_jpeg():
    assert jpeg_app_markers(b"\x89PNG\r\n\x1a\n") == []
    assert jpeg_app_markers(b"") == []


def test_jpeg_app_markers_lists_segments_in_file_order():
    plain = _plain_jpeg()
    tagged = plain[:2] + _segment(0xE1, b"Exif\x00\x00") + _segment(0xED, b"Photoshop 3.0") + plain[2:]
    assert jpeg_app_markers(tagged)[:2] == [1, 13]
    assert jpeg_app_markers(plain) == [0]


def test_jpeg_app_markers_stops_at_start_of_scan():
    plain = _plain_jpeg()
    sos = plain.index(b"\xff\xda")
    # Anything injected after SOS is image data, not a marker segment.
    tampered = plain[: sos + 2] + b"\xff\xe5" + plain[sos + 2 :]
    assert 5 not in jpeg_app_markers(tampered)


def test_jpeg_app_markers_skips_standalone_restart_markers():
    plain = _plain_jpeg()
    with_rst = plain[:2] + b"\xff\xd0" + _segment(0xE2, b"ICC_PROFILE") + plain[2:]
    assert 2 in jpeg_app_markers(with_rst)
