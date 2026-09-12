import json
from io import BytesIO
from pathlib import Path

from PIL import Image

from picai.batch import BatchItem, process_folder, render_markdown, write_report
from picai.cli import main
from picai.detect import DetectResult
from picai.inspect import find_metadata


def _write_jpeg(path: Path, with_exif: bool = True) -> None:
    kwargs = {}
    if with_exif:
        exif = Image.Exif()
        exif[0x0110] = "AI Camera"
        kwargs["exif"] = exif.tobytes()
    buffer = BytesIO()
    Image.new("RGB", (8, 8), "red").save(buffer, format="JPEG", **kwargs)
    path.write_bytes(buffer.getvalue())


def test_process_folder_scrubs_images_and_skips_others(tmp_path):
    inbox, out = tmp_path / "inbox", tmp_path / "clean"
    inbox.mkdir()
    _write_jpeg(inbox / "a.jpg")
    (inbox / "notes.txt").write_text("skip me")
    (inbox / "broken.png").write_bytes(b"nope")

    items = process_folder(inbox, out)

    assert [Path(i.source).name for i in items] == ["a.jpg", "broken.png"]
    ok, bad = items
    assert ok.removed == ["EXIF"] and Path(ok.output).name == "a.clean.jpg"
    assert find_metadata(Path(ok.output).read_bytes()) == {}
    assert bad.error and bad.output is None


def test_process_folder_runs_detector_when_given(tmp_path):
    inbox, out = tmp_path / "inbox", tmp_path / "clean"
    inbox.mkdir()
    _write_jpeg(inbox / "a.jpg")
    fake = lambda payload: DetectResult(0.91, "High", "AI", "fake/model")

    items = process_folder(inbox, out, detect=fake)

    assert items[0].detection == {"percent": 91, "confidence": "High", "classification": "AI", "model": "fake/model"}


def test_write_report_emits_json_and_markdown(tmp_path):
    items = [
        BatchItem("inbox/a.jpg", "clean/a.clean.jpg", ["EXIF", "XMP"], 2048, 1024, {"percent": 91, "confidence": "High", "classification": "AI", "model": "m"}),
        BatchItem("inbox/b.png", None, [], 10, 0, None, error="could not decode"),
    ]
    md = write_report(items, tmp_path / "r" / "report.json", tmp_path / "summary.md")

    data = json.loads((tmp_path / "r" / "report.json").read_text())
    assert data[0]["removed"] == ["EXIF", "XMP"] and data[1]["error"] == "could not decode"
    assert "| a.jpg | EXIF, XMP | 2 KB → 1 KB | 91% (High) | AI | a.clean.jpg |" in md
    assert "error: could not decode" in md
    assert (tmp_path / "summary.md").read_text() == md


def test_render_markdown_without_detection_and_empty():
    assert "No images found" in render_markdown([])
    md = render_markdown([BatchItem("x/a.jpg", "y/a.clean.jpg", [], 1024, 1024, None)])
    assert "| a.jpg | none | 1 KB → 1 KB | a.clean.jpg |" in md
    assert "AI likelihood" not in md


def test_cli_batch_writes_outputs_and_summary(tmp_path, capsys):
    inbox, out, summary = tmp_path / "inbox", tmp_path / "clean", tmp_path / "summary.md"
    inbox.mkdir()
    _write_jpeg(inbox / "a.jpg")

    assert main(["batch", str(inbox), str(out), "--summary", str(summary), "--format", "png"]) == 0

    assert (out / "a.clean.png").exists() and (out / "report.json").exists()
    assert "a.clean.png" in summary.read_text()
    assert "1 processed, 0 failed" in capsys.readouterr().out


def test_cli_batch_returns_error_for_missing_dir(tmp_path, capsys):
    assert main(["batch", str(tmp_path / "nope"), str(tmp_path / "out")]) == 1
    assert "not a directory" in capsys.readouterr().err
