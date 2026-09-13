# picai

picai is a free, open-source AI image detector and metadata scrubber. It scores how
likely a picture was produced by an AI generator using an open Hugging Face classifier
that runs inside the server process, lists the EXIF, XMP, IPTC, C2PA and ICC metadata
blocks the file carries, and can hand back a copy re-rendered from the raw pixels with
every one of those blocks removed.

Public instance: <https://picai-53480028562.europe-west1.run.app> (Cloud Run; the first
visit after idle takes about a minute while the model loads). Machine-readable summary
for AI assistants: [`/llms.txt`](https://picai-53480028562.europe-west1.run.app/llms.txt).

## Features

- **AI-likelihood score** (0–100 %) with a confidence band and an AI / Real / Uncertain
  classification, from `haywoodsloan/ai-image-detector-deploy` or any Hugging Face
  image-classification model you point it at.
- **Metadata inspection**: which of EXIF, XMP, IPTC, C2PA and ICC are present, plus JPEG
  APP segments.
- **Metadata removal by re-rendering** (`Image.frombytes`), so C2PA manifests and
  everything else are left behind rather than edited out.
- **Web page, CLI, HTTP API, Docker image and GitHub Action**; installable as a phone PWA.
- **Private by construction**: uploads are processed in memory and never written to disk;
  self-host it and nothing leaves your machine.

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

## Public pages, SEO and AI-assistant discoverability

Every public page is an entry in `PAGES` in `src/picai/pages.py` (path, title, meta
description, H1, section, schema types, last-modified date). The home page is
`static/index.html`; the other pages are body fragments in `static/pages/<slug>.html`
wrapped in `_layout.html`, and all of them share `_head.html` (canonical, Open Graph,
Twitter card, JSON-LD). Adding a page means dropping a fragment in that folder and adding
one `Page` to the registry; the sitemap, `llms.txt`, nav and footer follow automatically.

Served from the registry: `/robots.txt` (AI crawlers explicitly allowed, API routes
disallowed), `/sitemap.xml`, `/llms.txt` and `/llms-full.txt` (llmstxt.org format for
answer engines), `/.well-known/security.txt`, `/favicon.ico`, an HTML 404 page, and
JSON-LD (`SoftwareApplication`, `FAQPage`, `HowTo`, `BreadcrumbList`, `Article`) generated
from the same copy the pages render (`src/picai/content/`). `/docs`, `/redoc` and the
JSON endpoints carry `X-Robots-Tag: noindex`.

Environment variables read at request time:

- `PICAI_PUBLIC_URL` — public origin (e.g. `https://picai-53480028562.europe-west1.run.app`)
  used in canonical links, `og:url`, the sitemap and `llms.txt`; without it the request
  origin is used. Set it on every public deployment, and again after mapping a custom
  domain.
- `PICAI_GSC_VERIFICATION` / `PICAI_BING_VERIFICATION` — emit the Google Search Console
  and Bing Webmaster verification meta tags.
- `PICAI_GA_MEASUREMENT_ID` — emits the Google Analytics (GA4) gtag snippet when set (e.g.
  `G-X0LGV9CGFC`). Unset by default, so self-hosted instances send no analytics unless the
  operator opts in themselves; set it only on the hosted deployment.

After deploying: verify the site in Search Console and Bing Webmaster Tools, submit
`/sitemap.xml`, and check `/` and `/faq` with Google's Rich Results Test. AI-crawler
visits show up in the Cloud Run request logs:

```bash
gcloud logging read 'resource.type="cloud_run_revision" AND httpRequest.userAgent=~"GPTBot|ClaudeBot|PerplexityBot|Google-Extended|CCBot|OAI-SearchBot"' --project picai-260913 --limit 100
```

## Deploying to Cloud Run

The public instance runs on Google Cloud Run (project `picai-260913`, region
`europe-west1`), built from the Dockerfile by Cloud Build. `GET /ready` returns 503 until
the model is loaded; Cloud Run's startup probe waits on it so the model loads while the
container still has full CPU. To redeploy after a change:

```bash
gcloud run deploy picai --source . --project picai-260913 --region europe-west1 \
  --allow-unauthenticated --memory 4Gi --cpu 2 --min-instances 0 --max-instances 1 \
  --concurrency 4 --timeout 300 --cpu-boost --port 8000 \
  --set-env-vars PICAI_PUBLIC_URL=https://picai-53480028562.europe-west1.run.app,PICAI_GA_MEASUREMENT_ID=G-X0LGV9CGFC \
  --startup-probe httpGet.path=/ready,initialDelaySeconds=10,periodSeconds=10,timeoutSeconds=5,failureThreshold=24
```

The `/ready` probe means a crawler that hits an idle instance waits for the model before
it gets any HTML. If search-engine fetches start timing out, switch the probe to
`/health` so pages are served immediately while the model loads in the background (the
page already shows *Loading detector…*); the trade-off is a slower first analysis after a
cold start.

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

`--min-instances 0` keeps the bill near zero but means the first visitor after idle waits
about a minute for the model (the page shows *Loading detector…* meanwhile). Before a
launch post or any traffic push, redeploy with `--min-instances 1` and a higher
`--max-instances`; a warm 2-CPU/4 GiB instance costs roughly the whole monthly budget, so
turn it back to 0 afterwards.

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
- `src/picai/server.py` exposes `GET /status`, `POST /analyze`, `GET /download/{id}` and
  the older `POST /scrub`; `src/picai/pages.py` and `src/picai/seo.py` serve the HTML
  pages and the crawler files.

## Tests

```bash
uv run pytest -q
```

Tests inject a fake classifier, so they never download the model. Video is out of scope.
