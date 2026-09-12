import struct
from io import BytesIO
from pathlib import Path

from PIL import Image

from picai import cli
from picai.cli import main


def _jpeg(path: Path, with_exif: bool = False) -> Path:
    buffer = BytesIO()
    kwargs = {}
    if with_exif:
        exif = Image.Exif()
        exif[0x0110] = "AI Camera"
        kwargs["exif"] = exif.tobytes()
    Image.new("RGB", (8, 8), "red").save(buffer, format="JPEG", **kwargs)
    path.write_bytes(buffer.getvalue())
    return path


def test_scrub_with_explicit_output_and_format(tmp_path, capsys):
    src = _jpeg(tmp_path / "in.jpg")
    out = tmp_path / "out.webp"

    assert main(["scrub", str(src), str(out), "--format", "webp"]) == 0

    assert capsys.readouterr().out.strip() == str(out)
    assert Image.open(out).format == "WEBP"


def test_scrub_non_image_reports_error(tmp_path, capsys):
    bad = tmp_path / "bad.jpg"
    bad.write_bytes(b"not an image at all")

    assert main(["scrub", str(bad)]) == 1
    assert "could not decode" in capsys.readouterr().err


def test_scrub_warns_when_metadata_survives(tmp_path, capsys, monkeypatch):
    src = _jpeg(tmp_path / "in.jpg")
    monkeypatch.setattr(cli, "find_metadata", lambda data: {"EXIF": ["Exif"]})

    assert main(["scrub", str(src)]) == 2
    assert "still present" in capsys.readouterr().err


def test_inspect_reports_categories_and_segments(tmp_path, capsys):
    src = _jpeg(tmp_path / "tagged.jpg", with_exif=True)
    data = src.read_bytes()
    xmp = b"http://ns.adobe.com/xap/1.0/\x00<x:xmpmeta/>"
    segment = b"\xff\xe1" + struct.pack(">H", len(xmp) + 2) + xmp
    src.write_bytes(data[:2] + segment + data[2:])

    assert main(["inspect", str(src)]) == 0

    out = capsys.readouterr().out
    assert "JPEG APP segments: APP1" in out
    assert "EXIF:" in out and "XMP:" in out


def test_inspect_missing_file(tmp_path, capsys):
    assert main(["inspect", str(tmp_path / "missing.jpg")]) == 1
    assert "does not exist" in capsys.readouterr().err


def test_serve_invokes_uvicorn_with_parsed_options(monkeypatch, capsys):
    calls = []
    import uvicorn

    monkeypatch.setattr(uvicorn, "run", lambda app, **kw: calls.append((app, kw)))

    assert main(["serve", "--host", "0.0.0.0", "--port", "9001", "--reload"]) == 0

    assert calls == [("picai.server:app", {"host": "0.0.0.0", "port": 9001, "reload": True})]
    assert "http://0.0.0.0:9001" in capsys.readouterr().out


def test_unknown_command_exits_with_usage_error():
    import pytest

    with pytest.raises(SystemExit) as exc:
        main(["frobnicate"])
    assert exc.value.code == 2
