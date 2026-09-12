"""Command-line entry point: ``picai scrub`` and ``picai inspect``."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from picai.inspect import find_metadata, jpeg_app_markers
from picai.scrub import DEFAULT_JPEG_QUALITY, SUPPORTED_FORMATS, UnsupportedImageError, scrub_file

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8000


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="picai", description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    scrub = sub.add_parser("scrub", help="re-render an image and drop all metadata")
    scrub.add_argument("input", type=Path)
    scrub.add_argument("output", type=Path, nargs="?")
    scrub.add_argument("--format", choices=[f.lower() for f in SUPPORTED_FORMATS])
    scrub.add_argument("--quality", type=int, default=DEFAULT_JPEG_QUALITY)

    inspect = sub.add_parser("inspect", help="report metadata signatures found in a file")
    inspect.add_argument("input", type=Path)

    batch = sub.add_parser("batch", help="scrub every image in a folder and write a report")
    batch.add_argument("input_dir", type=Path)
    batch.add_argument("output_dir", type=Path)
    batch.add_argument("--format", choices=[f.lower() for f in SUPPORTED_FORMATS])
    batch.add_argument("--quality", type=int, default=DEFAULT_JPEG_QUALITY)
    batch.add_argument("--detect", action="store_true", help="also score each image with the AI detector")
    batch.add_argument("--report", type=Path, help="write report.json here (default: <output_dir>/report.json)")
    batch.add_argument("--summary", type=Path, help="append a markdown summary to this file (e.g. $GITHUB_STEP_SUMMARY)")

    serve = sub.add_parser("serve", help="run the local web app (upload in the browser, download the clean copy)")
    serve.add_argument("--host", default=DEFAULT_HOST)
    serve.add_argument("--port", type=int, default=DEFAULT_PORT)
    serve.add_argument("--reload", action="store_true")
    return parser


def run_scrub(args: argparse.Namespace) -> int:
    try:
        output = scrub_file(args.input, args.output, args.format, args.quality)
    except FileNotFoundError:
        print(f"error: {args.input} does not exist", file=sys.stderr)
        return 1
    except UnsupportedImageError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    leftovers = find_metadata(output.read_bytes())
    if leftovers:
        print(f"warning: metadata signatures still present: {leftovers}", file=sys.stderr)
        return 2
    print(output)
    return 0


def run_inspect(args: argparse.Namespace) -> int:
    try:
        data = args.input.read_bytes()
    except FileNotFoundError:
        print(f"error: {args.input} does not exist", file=sys.stderr)
        return 1
    found = find_metadata(data)
    markers = jpeg_app_markers(data)
    if markers:
        print("JPEG APP segments:", ", ".join(f"APP{m}" for m in markers))
    if not found:
        print("no metadata signatures found")
        return 0
    for category, hits in found.items():
        print(f"{category}: {', '.join(hits)}")
    return 0


def run_batch(args: argparse.Namespace) -> int:
    from picai.batch import process_folder, write_report

    if not args.input_dir.is_dir():
        print(f"error: {args.input_dir} is not a directory", file=sys.stderr)
        return 1
    detect = None
    if args.detect:
        from picai.detect import get_detector

        detect = get_detector().detect
    items = process_folder(args.input_dir, args.output_dir, args.format, args.quality, detect)
    report = args.report or args.output_dir / "report.json"
    markdown = write_report(items, report)
    if args.summary:
        with args.summary.open("a") as fh:
            fh.write(markdown)
    print(markdown)
    failures = [i for i in items if i.error]
    print(f"{len(items) - len(failures)} processed, {len(failures)} failed, report: {report}")
    return 1 if failures else 0


def run_serve(args: argparse.Namespace) -> int:
    import uvicorn

    print(f"picai web app: http://{args.host}:{args.port}")
    uvicorn.run("picai.server:app", host=args.host, port=args.port, reload=args.reload)
    return 0


COMMANDS = {"scrub": run_scrub, "inspect": run_inspect, "batch": run_batch, "serve": run_serve}


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return COMMANDS[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
