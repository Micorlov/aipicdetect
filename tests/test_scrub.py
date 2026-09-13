import struct
import zlib
from io import BytesIO

import pytest
from PIL import Image

from aipicdetect.inspect import find_metadata, jpeg_app_markers
from aipicdetect.scrub import UnsupportedImageError, scrub_bytes

XMP_PACKET = (
    b"http://ns.adobe.com/xap/1.0/\x00"
    b'<x:xmpmeta xmlns:x="adobe:ns:meta/"><rdf:RDF/></x:xmpmeta>'
)
FAKE_C2PA_JUMBF = b"JP\x00\x01" + b"\x00\x00\x00\x20jumb" + b"\x00\x00\x00\x18jumdc2pa" + b"\x00" * 8
FAKE_IPTC = b"Photoshop 3.0\x008BIM\x04\x04\x00\x00\x00\x00\x00\x10\x1c\x02\x78\x00\x0bAI caption"


def _jpeg_segment(marker: int, payload: bytes) -> bytes:
    return bytes([0xFF, marker]) + struct.pack(">H", len(payload) + 2) + payload


def _png_chunk(kind: bytes, payload: bytes) -> bytes:
    crc = zlib.crc32(kind + payload) & 0xFFFFFFFF
    return struct.pack(">I", len(payload)) + kind + payload + struct.pack(">I", crc)


def _tagged_jpeg(size=(64, 48)) -> bytes:
    """A JPEG carrying EXIF, XMP, IPTC (APP13) and a fake C2PA (APP11) segment."""
    image = Image.new("RGB", size, (200, 30, 90))
    exif = Image.Exif()
    exif[0x0110] = "AI Camera"  # Model
    buffer = BytesIO()
    image.save(buffer, format="JPEG", exif=exif.tobytes())
    data = buffer.getvalue()
    injected = _jpeg_segment(0xE1, XMP_PACKET) + _jpeg_segment(0xEB, FAKE_C2PA_JUMBF) + _jpeg_segment(0xED, FAKE_IPTC)
    return data[:2] + injected + data[2:]


def _tagged_png() -> bytes:
    """A PNG with alpha, an XMP iTXt chunk and a fake C2PA caBX chunk."""
    from PIL import PngImagePlugin

    image = Image.new("RGBA", (32, 32), (10, 20, 30, 128))
    info = PngImagePlugin.PngInfo()
    info.add_itxt("XML:com.adobe.xmp", "<x:xmpmeta/>")
    buffer = BytesIO()
    image.save(buffer, format="PNG", pnginfo=info)
    data = buffer.getvalue()
    iend = data.rindex(b"IEND") - 4
    return data[:iend] + _png_chunk(b"caBX", FAKE_C2PA_JUMBF) + data[iend:]


def test_tagged_fixture_actually_contains_metadata():
    found = find_metadata(_tagged_jpeg())
    assert set(found) >= {"EXIF", "XMP", "IPTC", "C2PA"}
    assert {1, 11, 13} <= set(jpeg_app_markers(_tagged_jpeg()))


def test_jpeg_output_has_no_metadata_signatures_or_app_segments():
    result = scrub_bytes(_tagged_jpeg())

    assert result.format == "JPEG"
    assert find_metadata(result.data) == {}
    assert jpeg_app_markers(result.data) == [0]  # only the plain JFIF APP0 header


def test_png_output_drops_xmp_and_c2pa_chunks_and_keeps_alpha():
    result = scrub_bytes(_tagged_png())

    assert result.format == "PNG"
    assert find_metadata(result.data) == {}
    assert b"caBX" not in result.data and b"iTXt" not in result.data
    assert Image.open(BytesIO(result.data)).mode == "RGBA"


def test_pixels_survive_the_round_trip():
    result = scrub_bytes(_tagged_png())
    assert Image.open(BytesIO(result.data)).getpixel((5, 5)) == (10, 20, 30, 128)


def test_exif_orientation_is_baked_into_pixels():
    image = Image.new("RGB", (40, 20), "white")
    exif = Image.Exif()
    exif[0x0112] = 6  # rotate 90 degrees clockwise
    buffer = BytesIO()
    image.save(buffer, format="JPEG", exif=exif.tobytes())

    result = scrub_bytes(buffer.getvalue())

    assert Image.open(BytesIO(result.data)).size == (20, 40)


def test_explicit_output_format_and_webp():
    result = scrub_bytes(_tagged_jpeg(), output_format="webp")
    assert result.format == "WEBP" and result.media_type == "image/webp"
    assert find_metadata(result.data) == {}


def test_rejects_non_image_and_unknown_format():
    with pytest.raises(UnsupportedImageError):
        scrub_bytes(b"definitely not an image")
    with pytest.raises(UnsupportedImageError):
        scrub_bytes(_tagged_jpeg(), output_format="bmp")


def test_scrub_bytes_decodes_heic():
    # Arrange: a HEIC written by pillow-heif (registered on package import)
    import aipicdetect  # noqa: F401  (registers the HEIF opener)

    buffer = BytesIO()
    Image.new("RGB", (64, 48), (10, 120, 200)).save(buffer, format="HEIF")

    # Act
    result = scrub_bytes(buffer.getvalue())

    # Assert: it decoded and re-rendered (as JPEG, since HEIC is input-only) instead of raising
    assert result.format == "JPEG"
    assert Image.open(BytesIO(result.data)).size == (64, 48)
