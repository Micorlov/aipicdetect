# picai

Local web dashboard that scores a picture with an open-source AI-image detector and
hands back a re-rendered copy with no C2PA, IPTC, XMP, EXIF or ICC metadata.

Public instance: <https://picai-53480028562.europe-west1.run.app> (Cloud Run; the first
visit after idle takes about a minute while the model loads).

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

`POST /analyze` is limited to 10 images per client IP in any rolling 24-hour window
(the 11th request gets `429` with a `Retry-After` header). Set `PICAI_DAILY_LIMIT` to
change the number, or to `0` to turn the limit off. The counter is in memory, so it
resets when the process restarts, and behind Cloud Run the client IP is
read from the first `X-Forwarded-For` hop.

## Deploying to Cloud Run

The public instance runs on Google Cloud Run (project `picai-260913`, region
`europe-west1`), built from the Dockerfile by Cloud Build. `GET /ready` returns 503 until
the model is loaded; Cloud Run's startup probe waits on it so the model loads while the
container still has full CPU. To redeploy after a change:

```bash
gcloud run deploy picai --source . --project picai-260913 --region europe-west1 \
  --allow-unauthenticated --memory 4Gi --cpu 2 --min-instances 0 --max-instances 1 \
  --concurrency 4 --timeout 300 --cpu-boost --port 8000 \
  --startup-probe httpGet.path=/ready,initialDelaySeconds=10,periodSeconds=10,timeoutSeconds=5,failureThreshold=24
```

### Budget and automatic shut-off

A ₪20/month budget with 50/90/100 % email alerts is attached to the project, and it
publishes spend updates to the Pub/Sub topic `picai-budget`. The Cloud Function in
[deploy/budget-guard](deploy/budget-guard/main.py) listens on that topic and, once the
month's cost reaches the budget, removes `allUsers` from the service's invoker role, so
the public URL answers 403 and nothing more is billed (billing data lags by a few hours,
so the stop lands slightly after the line is crossed). To switch the site back on:

```bash
gcloud run services add-iam-policy-binding picai --project picai-260913 --region europe-west1 \
  --member=allUsers --role=roles/run.invoker
```

To redeploy the guard after editing it:

```bash
gcloud functions deploy picai-budget-guard --gen2 --project picai-260913 --region europe-west1 \
  --runtime python312 --source deploy/budget-guard --entry-point guard --trigger-topic picai-budget \
  --service-account picai-budget-guard@picai-260913.iam.gserviceaccount.com \
  --set-env-vars SERVICE_NAME=projects/picai-260913/locations/europe-west1/services/picai
```

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
