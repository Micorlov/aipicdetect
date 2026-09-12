# picai

Local web dashboard that scores a picture with an open-source AI-image detector and
hands back a re-rendered copy with no C2PA, IPTC, XMP, EXIF or ICC metadata.

## Run

```bash
uv sync
uv run picai serve
```

Open <http://127.0.0.1:8000>. The first run downloads the detector model
(`Ateeqq/ai-vs-human-image-detector`, about 370 MB) into the Hugging Face cache; the
page shows "detector ready" once it is loaded. Everything runs on this machine and the
server binds to localhost only.

Drop an image on the page to get:

- **AI Likelihood**, **Confidence** and **Classification** from the detector
- the metadata blocks found in the upload (C2PA, IPTC, XMP, EXIF, ICC)
- side-by-side original and clean re-render, plus a **Download clean copy** button

Set `PICAI_DETECTOR_MODEL` to any Hugging Face image-classification model whose labels
name AI/fake vs. human/real content to swap the detector.

## GitHub Actions

Two workflows run in the repo:

- **Process inbox** ([process-inbox.yml](.github/workflows/process-inbox.yml)).
  Drop images into `inbox/` and push to `main`. The workflow scrubs and scores each
  one, writes the clean copies plus `report.json` into `clean/`, commits them back,
  clears the inbox, and shows a results table in the run summary. The clean files
  are also attached as a downloadable artifact. It can be started by hand from the
  Actions tab with a chosen output format and quality.
- **Publish Docker image** ([docker-publish.yml](.github/workflows/docker-publish.yml)).
  Every change to the app pushes `ghcr.io/micorlov/picai:latest`. Run it anywhere:

  ```bash
  docker run -p 8000:8000 -v picai-models:/data ghcr.io/micorlov/picai:latest
  ```

## CLI

```bash
uv run picai scrub photo.jpg            # writes photo.clean.jpg
uv run picai scrub photo.png --format webp --quality 90
uv run picai inspect photo.clean.jpg    # prints "no metadata signatures found"
uv run picai batch inbox clean --detect # scrub a folder, score it, write clean/report.json
```

## How it works

- `src/picai/detect.py` lazily loads a transformers image-classification pipeline and
  folds its label scores into an AI probability with confidence bands.
- `src/picai/scrub.py` decodes the upload, applies EXIF orientation, builds a brand-new
  image from the raw pixel buffer (`Image.frombytes`) and encodes it fresh. The new
  image never sees the original container, so every metadata block is left behind.
- `src/picai/inspect.py` scans bytes for metadata signatures and JPEG APP segments; the
  dashboard uses it to report what was removed.
- `src/picai/server.py` exposes `GET /`, `GET /status`, `POST /analyze`,
  `GET /download/{id}` and the older `POST /scrub`.

## Tests

```bash
uv run pytest -q
```

Tests inject a fake classifier, so they never download the model. Video is out of scope.
