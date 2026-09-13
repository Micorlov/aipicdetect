from io import BytesIO
from pathlib import Path

import pytest
from PIL import Image

from aipicdetect.inspect import find_metadata
from aipicdetect.scrub import UnsupportedImageError, scrub_bytes, scrub_file


def _encode(image: Image.Image, fmt: str, **kwargs) -> bytes:
    buffer = BytesIO()
    image.save(buffer, format=fmt, **kwargs)
    return buffer.getvalue()


def test_palette_png_with_transparency_stays_rgba_png():
    palette = Image.new("RGBA", (10, 10), (255, 0, 0, 0)).convert("P")
    data = _encode(palette, "PNG", transparency=0)

    result = scrub_bytes(data)

    assert result.format == "PNG"
    assert Image.open(BytesIO(result.data)).mode == "RGBA"


def test_alpha_image_forced_to_jpeg_is_flattened_to_rgb():
    data = _encode(Image.new("RGBA", (10, 10), (0, 255, 0, 128)), "PNG")

    result = scrub_bytes(data, output_format="jpg")

    assert result.format == "JPEG"
    assert Image.open(BytesIO(result.data)).mode == "RGB"


def test_grayscale_jpeg_is_converted_to_rgb():
    data = _encode(Image.new("L", (10, 10), 128), "JPEG")
    assert Image.open(BytesIO(scrub_bytes(data).data)).mode == "RGB"


def test_unknown_input_format_without_alpha_defaults_to_jpeg():
    data = _encode(Image.new("RGB", (10, 10), "blue"), "BMP")
    result = scrub_bytes(data)
    assert result.format == "JPEG" and result.extension == ".jpg"


def test_unknown_input_format_with_alpha_defaults_to_png():
    data = _encode(Image.new("RGBA", (10, 10), (0, 0, 255, 200)), "TIFF")
    result = scrub_bytes(data)
    assert result.format == "PNG"


def test_lower_quality_produces_smaller_jpeg():
    noisy = Image.effect_noise((128, 128), 64).convert("RGB")
    data = _encode(noisy, "PNG")

    high = scrub_bytes(data, output_format="jpeg", quality=95)
    low = scrub_bytes(data, output_format="jpeg", quality=60)

    assert len(low.data) < len(high.data)


def test_webp_input_round_trips_without_metadata():
    exif = Image.Exif()
    exif[0x0110] = "AI Camera"
    data = _encode(Image.new("RGB", (16, 16), "purple"), "WEBP", exif=exif.tobytes())
    assert Image.open(BytesIO(data)).info.get("exif")  # libwebp may omit the Exif\0\0 prefix

    result = scrub_bytes(data)

    assert result.format == "WEBP"
    assert find_metadata(result.data) == {}
    assert not Image.open(BytesIO(result.data)).info.get("exif")


def test_format_names_are_case_insensitive():
    data = _encode(Image.new("RGB", (4, 4), "red"), "PNG")
    assert scrub_bytes(data, output_format="Png").format == "PNG"
    assert scrub_bytes(data, output_format="JPG").format == "JPEG"


def test_truncated_image_raises_unsupported():
    data = _encode(Image.new("RGB", (64, 64), "red"), "JPEG")
    with pytest.raises(UnsupportedImageError):
        scrub_bytes(data[: len(data) // 2])


def test_scrub_file_defaults_to_clean_suffix_next_to_input(tmp_path: Path):
    src = tmp_path / "photo.png"
    src.write_bytes(_encode(Image.new("RGB", (4, 4), "red"), "PNG"))

    out = scrub_file(src)

    assert out == tmp_path / "photo.clean.png"
    assert out.exists()


def test_scrub_file_honours_explicit_output_and_format(tmp_path: Path):
    src = tmp_path / "photo.png"
    src.write_bytes(_encode(Image.new("RGB", (4, 4), "red"), "PNG"))
    target = tmp_path / "custom.webp"

    out = scrub_file(src, target, output_format="webp")

    assert out == target
    assert Image.open(target).format == "WEBP"
