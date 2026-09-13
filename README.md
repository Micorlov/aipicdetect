---
title: picai
emoji: 🔍
colorFrom: yellow
colorTo: gray
sdk: docker
app_port: 8000
pinned: false
---

# picai

Local web dashboard that scores a picture with an open-source AI-image detector and
hands back a re-rendered copy with no C2PA, IPTC, XMP, EXIF or ICC metadata.
(The YAML block above is Hugging Face Space metadata; GitHub shows it as a table.)

## Run

```bash
uv sync
uv run picai serve
```

Open <http://127.0.0.1:8000>. The first run downloads the detector model
(`haywoodsloan/ai-image-detector-deploy`, about 750 MB) into the Hugging Face cache; the
status pill in the top bar shows "Detector ready" once it is loaded. Everything runs on
this machine and the server binds to localhost only.

Drop, paste or pick an image on the page to get:

- a verdict (**Likely AI-generated** / **Likely a real photo** / **Uncertain**), the AI
  likelihood percentage, a confidence label and a probability meter
- every metadata block found in the upload (EXIF, XMP, IPTC, C2PA, ICC) with the matched
  signatures, plus the JPEG APP segments

The web page is detection-only. Metadata scrubbing is still available through the CLI
and the `POST /scrub` / `POST /analyze` API endpoints below.

## On your phone

The page is a small PWA: on a phone it shows **Choose photo** / **Take a photo** buttons
instead of the drag-and-drop hints, and it can be added to the home screen (Safari:
Share → *Add to Home Screen*; Chrome: menu → *Install app*).

The phone needs to reach the server over your Wi-Fi, so start it on all interfaces:

```bash
uv run picai serve --host 0.0.0.0
```

then open `http://<your-computer's-LAN-IP>:8000` on the phone (on macOS the IP is under
System Settings → Wi-Fi → Details). The Docker image already listens on all interfaces.

Set `PICAI_DETECTOR_MODEL` to any Hugging Face image-classification model whose labels
name AI/fake vs. human/real content to swap the detector.

## Public demo on Hugging Face Spaces

The **Deploy to Hugging Face Space** workflow
([deploy-space.yml](.github/workflows/deploy-space.yml)) pushes `main` to a Docker Space
named `picai` under your Hugging Face account on every push, creating the Space on first
run. One-time setup:

1. Create a Hugging Face account and a **write** access token
   (Settings → Access Tokens → New token).
2. Add it to this repo as the `HF_TOKEN` secret:

   ```bash
   gh secret set HF_TOKEN --repo Micorlov/picai
   ```

3. Push to `main` (or run the workflow from the Actions tab). The run summary links to
   `https://huggingface.co/spaces/<your-hf-username>/picai`; the first build takes a few
   minutes while the Space installs torch and downloads the model.

The free CPU tier is enough for the detector. Spaces go to sleep after 48 h without
visitors and wake on the next request.

## GitHub Actions

Three workflows run in the repo (plus the Space deploy above):

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
