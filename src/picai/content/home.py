"""Home-page copy: the entity sentence, hero lead and the three detection steps."""

from __future__ import annotations

from dataclasses import dataclass

from picai.limits import DEFAULT_DAILY_LIMIT, MAX_UPLOAD_MB

BRAND = "picai"
AUTHOR = "Michael Orlov"
REPO_URL = "https://github.com/Micorlov/picai"
LICENSE_NAME = "MIT"
LICENSE_URL = "https://opensource.org/license/mit"

ENTITY_SENTENCE = "picai is a free, open-source AI image detector and metadata scrubber."
SUMMARY = (
    f"{ENTITY_SENTENCE} It scores how likely a picture was produced by an AI generator using an "
    "open Hugging Face classifier, and can re-render images to strip EXIF, XMP, IPTC, ICC and "
    "C2PA metadata. Use the hosted instance or self-host with Docker or Python."
)
LEAD = (
    "Score any picture with an open-source classifier. Use this hosted instance, or self-host "
    "and nothing ever leaves your machine."
)
DROPZONE_NOTE = f"JPEG, PNG, WebP, HEIC · up to {MAX_UPLOAD_MB} MB · processed in memory, never written to disk"


@dataclass(frozen=True)
class Step:
    name: str
    text: str


DETECT_STEPS: tuple[Step, ...] = (
    Step(
        "Upload.",
        "Drop, paste or pick a picture. It is sent to the picai server you are using (your own "
        "machine when self-hosted), held in memory and never written to disk.",
    ),
    Step("Detect.", "An open-source image classifier scores how likely the pixels were produced by a generator."),
    Step(
        "Read the verdict.",
        "You get an AI likelihood, a confidence band and the metadata blocks the file carries — "
        "as a probability, not a verdict.",
    ),
)

SCRUB_STEPS: tuple[Step, ...] = (
    Step("Inspect.", "Run <code>picai inspect photo.jpg</code> to list the EXIF, XMP, IPTC, C2PA and ICC blocks the file carries."),
    Step(
        "Scrub.",
        "Run <code>picai scrub photo.jpg</code> (or <code>POST /scrub</code>). picai decodes the pixels, "
        "applies the EXIF orientation, and builds a brand-new image from the raw pixel buffer.",
    ),
    Step("Verify.", "Run <code>picai inspect photo.clean.jpg</code>; it should print “no metadata signatures found”."),
)

STATS = (
    ("1", "open model,<br>no third-party API"),
    ("0", "sign-ups<br>required"),
    (str(MAX_UPLOAD_MB), "MB max<br>upload"),
)
HOSTED_LIMIT_SENTENCE = f"The hosted instance allows {DEFAULT_DAILY_LIMIT} analyses per IP address every 24 hours."
