"""FAQ entries: rendered as <details> blocks and as FAQPage JSON-LD from the same tuples."""

from __future__ import annotations

from dataclasses import dataclass

from picai.limits import DEFAULT_DAILY_LIMIT, MAX_UPLOAD_MB, RESULT_CACHE_LIMIT


@dataclass(frozen=True)
class FaqEntry:
    question: str
    answer_html: str  # inline HTML only (<a>, <code>, <em>); used verbatim in HTML and JSON-LD


FAQ_HOME: tuple[FaqEntry, ...] = (
    FaqEntry(
        "How accurate is the detector?",
        "It reports a probability, not a verdict. Scores near 50% are labelled <em>Uncertain</em>; "
        "treat any single result as a signal and combine it with other evidence. "
        'Read more on <a href="/how-accurate">how accurate AI image detectors are</a>.',
    ),
    FaqEntry(
        "Does my image leave my computer?",
        "On this public instance, yes: the picture is uploaded to the picai server (a Google Cloud Run "
        "container run by the author), scored in memory and never written to disk. The scrubbed copy is "
        f"held in memory only until {RESULT_CACHE_LIMIT} newer results replace it or the container restarts, "
        'and nothing is sent to a third-party API. If you want nothing to leave your machine, '
        '<a href="/self-host">run picai yourself</a> with one Docker command. Details are on the '
        '<a href="/privacy">privacy page</a>.',
    ),
    FaqEntry(
        "Is it open source?",
        "Yes. The code, the Docker image, the CLI and the GitHub Action are all in the "
        '<a href="https://github.com/Micorlov/picai" rel="noopener">picai repository</a> under the MIT '
        "licence. The detector is an open Hugging Face model you can inspect or replace.",
    ),
    FaqEntry(
        "Can I remove C2PA and other metadata?",
        "Yes. After checking a picture, use <em>Download clean copy</em>. picai rebuilds the image from its "
        "pixels, so EXIF, XMP, IPTC, C2PA and the ICC profile are all left behind. "
        '<a href="/remove-image-metadata">How the scrubber works</a>.',
    ),
    FaqEntry(
        "Which formats are supported?",
        f"JPEG, PNG, WebP, HEIC/HEIF and most formats Pillow can decode, up to {MAX_UPLOAD_MB} MB.",
    ),
    FaqEntry(
        "Why is metadata listed?",
        "C2PA content credentials and editing-software tags are provenance hints. The panel shows "
        "which blocks (EXIF, XMP, IPTC, C2PA, ICC) the file carries so you can weigh them alongside "
        'the score. See <a href="/c2pa">C2PA content credentials</a> and '
        '<a href="/remove-image-metadata">how to remove image metadata</a>.',
    ),
    FaqEntry(
        "Can I use a different model?",
        "Yes. Set <code>PICAI_DETECTOR_MODEL</code> to any Hugging Face image-classification model "
        "whose labels name AI/fake vs. human/real content.",
    ),
)

FAQ_MORE: tuple[FaqEntry, ...] = (
    FaqEntry(
        "Is picai free?",
        "Yes. picai is open source under the MIT licence. The hosted instance is free to use with a "
        f"limit of {DEFAULT_DAILY_LIMIT} analyses per IP address every 24 hours; a self-hosted copy has no limit.",
    ),
    FaqEntry(
        "Does it work on screenshots or heavily compressed images?",
        "It runs, but re-encoding, resizing and screenshots remove some of the pixel-level traces the "
        "classifier relies on, so expect lower confidence and more <em>Uncertain</em> results.",
    ),
    FaqEntry(
        "Can it tell which generator made an image (Midjourney, DALL·E, Stable Diffusion)?",
        "No. picai scores generated-versus-real pixel statistics in general; it does not identify the "
        "generator, and it has no knowledge of generators released after its model's training data was collected.",
    ),
    FaqEntry(
        "Why did a real photo score as AI?",
        "Heavy filters, HDR processing, upscaling, illustrations and 3D renders share statistical "
        "features with generated images. The score is a probability, not proof; false positives happen.",
    ),
    FaqEntry(
        "Can I run it offline?",
        "Yes. After the first run downloads the model into the Hugging Face cache, a self-hosted picai "
        "needs no network access.",
    ),
    FaqEntry(
        "Is there a rate limit on the hosted instance?",
        f"Yes: {DEFAULT_DAILY_LIMIT} analyses per client IP in any rolling 24-hour window. Responses carry "
        "<code>X-RateLimit-Remaining</code>, and a request over the limit returns 429 with a "
        "<code>Retry-After</code> header.",
    ),
)

FAQ_ALL: tuple[FaqEntry, ...] = FAQ_HOME + FAQ_MORE
