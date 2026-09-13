# Launch posts

Drafts to paste when the public instance is warm (`--min-instances 1`) and, ideally,
behind a custom domain. Replace `PUBLIC_URL` before posting. Each one is written for
its venue's norms; do not cross-post the same text verbatim.

## Hacker News — Show HN

**Title:** Show HN: AiPicDetect – open-source AI image detector that also shows C2PA/EXIF provenance

**Text:**

I built a small tool that scores whether a picture is AI-generated and, next to the
score, lists every metadata block the file carries: EXIF, XMP, IPTC, C2PA content
credentials and the ICC profile, with the matched signatures. You can then download a
copy rebuilt from the raw pixels with all of it gone.

Why both: pixel classifiers are unreliable on newer generators (the public benchmarks
are grim: under 40% on 2024-era models), while a C2PA manifest naming a generator is
strong evidence when it survives. Showing them side by side felt more honest than a
single percentage.

It is a FastAPI app around an open Hugging Face classifier that runs on CPU. Docker
image, CLI, HTTP API and a GitHub Action that scrubs and scores anything you push into
an `inbox/` folder. Swap the model with one env var. MIT.

Demo: PUBLIC_URL (public instance, 10 checks per IP per day; self-host to remove that)
Code: https://github.com/Micorlov/aipicdetect

Things I would like feedback on: better open detector models that still run on CPU,
and whether the C2PA reading is useful to anyone doing verification work.

## r/selfhosted

**Title:** AiPicDetect: self-hosted AI image detector + metadata (C2PA/EXIF/XMP) inspector and scrubber, one Docker command

**Text:**

    docker run -p 8000:8000 -v aipicdetect-models:/data ghcr.io/micorlov/aipicdetect:latest

Drop an image on the page and you get an AI-likelihood score from an open-source
classifier plus a list of every metadata block in the file (EXIF, XMP, IPTC, C2PA,
ICC). One click gives you a copy re-rendered from the pixels with none of it. Nothing
leaves your box; the server binds to localhost unless you tell it otherwise.

Also has a CLI (`aipicdetect scrub`, `aipicdetect inspect`, `aipicdetect batch`) and a JSON API. First
start downloads a ~750 MB model; after that it is CPU-only and a second or two per image.

Source (MIT): https://github.com/Micorlov/aipicdetect
Docs on self-hosting and the API: PUBLIC_URL/self-host

## r/StableDiffusion

**Title:** Open-source tool to check how "detectable" your generations are, and what metadata they leak

**Text:**

Made this mostly out of curiosity about what detectors actually see. AiPicDetect runs an open
Hugging Face AI-image classifier locally and shows the score, but the part I find more
interesting is the metadata panel: it lists every EXIF/XMP/IPTC/C2PA/ICC block in the
file, so you can see exactly what a PNG from ComfyUI or an export from Photoshop carries
before you share it. There is a "download clean copy" button that rebuilds the image
from pixels with everything stripped.

Runs on CPU, Docker or `uv run`, MIT licensed. Curious which current models people
find it flags well or badly.

https://github.com/Micorlov/aipicdetect · demo: PUBLIC_URL

## Product Hunt

**Name:** AiPicDetect
**Tagline:** Open-source AI image detector that reads the provenance too
**Description:**

AiPicDetect scores whether a picture is AI-generated and shows every metadata block it
carries: EXIF, XMP, IPTC, C2PA content credentials and ICC. Then it hands you a clean
copy rebuilt from the pixels. No sign-up. Self-host it with one Docker command and
nothing leaves your machine. CLI, HTTP API and a GitHub Action included. MIT.

**Topics:** Open Source, Privacy, Developer Tools, Artificial Intelligence

## Directory submissions

Same short blurb for all of them:

> Open-source AI image detector with metadata inspection. Scores a picture with an open
> classifier, lists its EXIF, XMP, IPTC, C2PA and ICC blocks, and returns a clean copy
> rebuilt from the pixels. Self-hostable with one Docker command; CLI and HTTP API.

- There's An AI For That: https://theresanaiforthat.com/submit/
- Futurepedia: https://www.futurepedia.io/submit-tool
- AlternativeTo: https://alternativeto.net/ (add as alternative to "AI or Not", "Illuminarty", "Hive AI Detector")
- awesome-selfhosted: open a PR adding AiPicDetect under "Photo and Video Galleries" or
  "Miscellaneous"; the list requires a license and a working demo or screenshot.
- Hugging Face: the Space that deploys from `main` counts as a listing; add tags
  `ai-detection`, `c2pa`, `metadata` in its README front matter.
