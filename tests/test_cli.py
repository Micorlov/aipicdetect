from io import BytesIO

from PIL import Image

from aipicdetect.cli import main


def test_cli_scrub_writes_clean_file_and_inspect_reports_nothing(tmp_path, capsys):
    exif = Image.Exif()
    exif[0x0110] = "AI Camera"
    src = tmp_path / "in.jpg"
    buffer = BytesIO()
    Image.new("RGB", (8, 8), "red").save(buffer, format="JPEG", exif=exif.tobytes())
    src.write_bytes(buffer.getvalue())

    assert main(["scrub", str(src)]) == 0
    out = tmp_path / "in.clean.jpg"
    assert out.exists()

    assert main(["inspect", str(out)]) == 0
    assert "no metadata signatures found" in capsys.readouterr().out


def test_cli_scrub_missing_file_returns_error(tmp_path, capsys):
    assert main(["scrub", str(tmp_path / "nope.jpg")]) == 1
    assert "does not exist" in capsys.readouterr().err


def test_serve_subcommand_parses_flags():
    from aipicdetect.cli import build_parser

    args = build_parser().parse_args(["serve", "--port", "9000", "--reload"])
    assert (args.host, args.port, args.reload) == ("127.0.0.1", 9000, True)
