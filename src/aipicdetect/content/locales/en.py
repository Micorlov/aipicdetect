"""English translation table: the canonical locale. Every other locale falls back to this one
for any key it does not define (see :func:`aipicdetect.content.locales.t`).

Text is sourced directly from ``content/home.py`` and ``content/faq.py`` rather than retyped, so
English visitors see byte-for-byte the same copy as before locale support existed.
"""

from __future__ import annotations

from aipicdetect.content.faq import FAQ_ALL
from aipicdetect.content.home import DETECT_STEPS, DROPZONE_NOTE, ENTITY_SENTENCE, LEAD, SCRUB_STEPS, STATS, SUMMARY

_FAQ_HOME_SLUGS = (
    "accuracy",
    "leaves_computer",
    "open_source",
    "remove_metadata",
    "formats",
    "why_metadata",
    "different_model",
)
_FAQ_MORE_SLUGS = ("free", "screenshots", "which_generator", "false_positive", "offline", "rate_limit")
_FAQ_SLUGS = _FAQ_HOME_SLUGS + _FAQ_MORE_SLUGS
_DETECT_SLUGS = ("upload", "detect", "decide")
_SCRUB_SLUGS = ("inspect", "scrub", "verify")

STRINGS: dict[str, str] = {
    "page.home.title": "AiPicDetect — Free AI Image Detector & Metadata Scrubber",
    "page.home.description": (
        "Check whether a picture is AI-generated with AiPicDetect, a free AI image detector. Get a "
        "score, a confidence band, and a metadata report in your browser."
    ),
    "page.home.h1": "Is this photo real? Get the score and the proof.",
    "page.faq.title": "AI Image Detector FAQ: Accuracy, Privacy, Formats, Models",
    "page.faq.description": (
        "Answers to common questions about AiPicDetect: how accurate AI detection is, where your "
        "image is processed, supported formats, model swapping and rate limits."
    ),
    "page.faq.h1": "AiPicDetect frequently asked questions",
    "page.faq.intro_suffix": (
        "These are the questions people ask most about how it works, how accurate it is, and what "
        "happens to the images they upload."
    ),
    "page.faq.still_unsure_html": (
        "Still unsure? Run the same image through more than one detector before drawing a conclusion."
    ),
    # ── Guide & product page meta (English baseline; non-English locales override these) ────────
    "page.how-to-tell-if-an-image-is-ai-generated.title": "How to Tell If an Image Is AI-Generated (2026 Guide)",
    "page.how-to-tell-if-an-image-is-ai-generated.description": (
        "A practical checklist for spotting AI-generated images: visual tells, C2PA and EXIF "
        "metadata, reverse image search, and how to read a detector score."
    ),
    "page.how-to-tell-if-an-image-is-ai-generated.h1": "How to tell if an image is AI-generated",
    "page.how-accurate.title": "How Accurate Are AI Detectors? Reading an AiPicDetect Score",
    "page.how-accurate.description": (
        "AI image detectors give probabilities, not proof. How AiPicDetect turns classifier scores into "
        "a percentage and confidence band, and where detectors fail."
    ),
    "page.how-accurate.h1": "How accurate is an AI image detector?",
    "page.remove-image-metadata.title": "Remove EXIF, XMP, IPTC and C2PA Metadata from Images",
    "page.remove-image-metadata.description": (
        "Strip EXIF, XMP, IPTC, ICC and C2PA content credentials from JPEG, PNG, WebP and HEIC "
        "files by re-rendering the pixels with AiPicDetect's free CLI or HTTP API."
    ),
    "page.remove-image-metadata.h1": "Remove all metadata from an image",
    "page.c2pa.title": "C2PA Content Credentials: How to Check and Remove Them",
    "page.c2pa.description": (
        "What C2PA content credentials are, how AiPicDetect finds them next to EXIF, XMP, IPTC and ICC "
        "blocks, and how re-rendering leaves every one of them behind."
    ),
    "page.c2pa.h1": "C2PA content credentials: what they are and how AiPicDetect handles them",
    "page.privacy.title": "Privacy: What Happens to Images You Upload to AiPicDetect",
    "page.privacy.description": (
        "AiPicDetect processes uploads in memory, never writes them to disk, keeps scrubbed copies only "
        "briefly and sends no image to any third-party service."
    ),
    "page.privacy.h1": "What happens to an image you upload",
    "page.about.title": "About AiPicDetect: Author and Model Credits",
    "page.about.description": (
        "Who builds AiPicDetect and which open-source Hugging Face model powers the AI image "
        "detector behind it."
    ),
    "page.about.h1": "About AiPicDetect",
    "page.self-host.title": "Self-Host AiPicDetect: AI Image Detector with Docker or uv",
    "page.self-host.description": (
        "Run AiPicDetect on your own machine or server with one Docker command or with uv. Model "
        "download size, environment variables, phone access and Cloud Run notes."
    ),
    "page.self-host.h1": "Run AiPicDetect on your own machine",
    "page.detect-midjourney-images.title": "Detect Midjourney Images: Visual Tells and Metadata",
    "page.detect-midjourney-images.description": (
        "Identify Midjourney AI images by XMP prompt metadata, painterly skin texture, unusual bokeh, "
        "and AiPicDetect pixel-level detector score."
    ),
    "page.detect-midjourney-images.h1": "How to detect Midjourney images",
    "page.detect-dall-e-images.title": "Detect DALL-E Images: C2PA Credentials and Pixel Score",
    "page.detect-dall-e-images.description": (
        "DALL-E 3 images carry C2PA credentials signed by OpenAI — the strongest AI proof. "
        "How to verify them and read the pixel-level detector score."
    ),
    "page.detect-dall-e-images.h1": "How to detect DALL-E images",
    "page.detect-stable-diffusion-images.title": "Detect Stable Diffusion Images: Metadata and Pixel Score",
    "page.detect-stable-diffusion-images.description": (
        "Stable Diffusion PNGs often embed sampler metadata in PNG chunks. How to check ComfyUI "
        "and A1111 outputs, use the AI detector, and spot each checkpoint."
    ),
    "page.detect-stable-diffusion-images.h1": "How to detect Stable Diffusion images",
    "page.ai-detector-false-positives.title": "AI Detector False Positives: When Scores Can Be Wrong",
    "page.ai-detector-false-positives.description": (
        "AI image detectors return probabilities, not verdicts. When real photos score as AI and "
        "AI images score as real — and how to interpret uncertain scores."
    ),
    "page.ai-detector-false-positives.h1": "When can an AI image detector be wrong?",
    "page.view-exif-data.title": "View EXIF Data Online: Free Image Metadata Inspector",
    "page.view-exif-data.description": (
        "View EXIF, XMP, IPTC, ICC and C2PA metadata in any JPEG, PNG, WebP or HEIC file. "
        "Free, no account, processed in the browser — nothing stored server-side."
    ),
    "page.view-exif-data.h1": "View the EXIF and metadata in an image",
    "page.does-screenshot-remove-metadata.title": "Does a Screenshot Remove Metadata? EXIF, GPS, AI Proof",
    "page.does-screenshot-remove-metadata.description": (
        "Screenshots strip EXIF and C2PA from the original image but add new device metadata "
        "from the capturing phone or PC. What this means for AI detection."
    ),
    "page.does-screenshot-remove-metadata.h1": "Does taking a screenshot remove image metadata?",
    # ── Home-page copy ───────────────────────────────────────────────────────────────────────────
    "home.entity_sentence": ENTITY_SENTENCE,
    "home.lead": LEAD,
    "home.dropzone_note": DROPZONE_NOTE,
    "home.summary": SUMMARY,
    **{f"home.stat.{i}": label for i, (_numeral, label) in enumerate(STATS)},
    **{f"steps.detect.{slug}.name": step.name for slug, step in zip(_DETECT_SLUGS, DETECT_STEPS)},
    **{f"steps.detect.{slug}.text": step.text for slug, step in zip(_DETECT_SLUGS, DETECT_STEPS)},
    # steps.scrub.*.text carries inline <code>...</code> shell commands — a translator must
    # preserve that markup verbatim and translate only the surrounding prose.
    **{f"steps.scrub.{slug}.name": step.name for slug, step in zip(_SCRUB_SLUGS, SCRUB_STEPS)},
    **{f"steps.scrub.{slug}.text": step.text for slug, step in zip(_SCRUB_SLUGS, SCRUB_STEPS)},
    **{f"faq.{slug}.question": entry.question for slug, entry in zip(_FAQ_SLUGS, FAQ_ALL)},
    **{f"faq.{slug}.answer_html": entry.answer_html for slug, entry in zip(_FAQ_SLUGS, FAQ_ALL)},
    "nav.detector": "Detector",
    "nav.how_it_works": "How it works",
    "nav.how-to-tell-if-an-image-is-ai-generated": "Guide",
    "nav.api": "API",
    "nav.self-host": "Self-host",
    "footer.remove-image-metadata": "Remove metadata",
    "footer.c2pa": "C2PA",
    "footer.faq": "FAQ",
    "footer.privacy": "Privacy",
    "footer.self-host": "Self-host",
    "footer.about": "About",
    "ui.source_on_github": "source on GitHub",
    "ui.nav_aria_label": "Main navigation",
    "ui.loading_status": "Loading detector…",
    "ui.hero_overline": "— AI image forensics",
    "ui.hero_heading_line1": "Is this photo real?",
    "ui.hero_heading_line2": "Get the score and the proof.",
    "ui.tool_aria_label": "AI image detector",
    "ui.dropzone_aria_label": "Upload an image to analyze",
    "ui.dropzone_title_fine": "Drag & drop a photo",
    "ui.dropzone_title_coarse": "Check a photo",
    "ui.dropzone_sub_fine": "or paste from the clipboard, or",
    "ui.dropzone_sub_coarse": "from your library or camera",
    "ui.btn_check_image_fine": "Check this image",
    "ui.btn_choose_photo_coarse": "Choose photo",
    "ui.btn_take_photo": "Take a photo",
    "ui.dismiss_aria_label": "Dismiss",
    "ui.analyzing_prefix": "Analyzing",
    "ui.analyzing_suffix": "· pixels · metadata blocks",
    "ui.verdict_overline": "— Verdict",
    "ui.meter_real": "Real",
    "ui.meter_uncertain": "Uncertain",
    "ui.meter_ai": "AI",
    "ui.model_label": "Model",
    "ui.verdict_disclaimer_html": (
        "Results are probabilities from a classifier, not verdicts. "
        '<a href="/how-accurate">How to read the score.</a>'
    ),
    "ui.btn_check_another": "Check another image",
    "ui.preview_overline": "— Preview",
    "ui.preview_alt": "Uploaded image preview",
    "ui.metadata_overline": "— Metadata",
    "ui.metadata_heading": "Found in the file.",
    "ui.jpeg_segments_label": "JPEG segments",
    "ui.btn_download_clean": "Download the clean copy",
    "ui.metadata_scrub_note_html": (
        "Re-rendered from the pixels, so every block above is gone. "
        '<a href="/remove-image-metadata">How it works</a>'
    ),
    "ui.how_it_works_overline": "— How it works",
    "ui.how_it_works_heading": "Three steps. Nothing saved.",
    "ui.how_it_works_links_html": (
        '<a href="/how-to-tell-if-an-image-is-ai-generated">Read the guide to spotting AI images</a>.'
    ),
    "ui.faq_overline": "— FAQ",
    "ui.faq_heading": "Before you ask.",
    "ui.faq_more_link": "More questions and answers →",
    "ui.footer_tagline": "AiPicDetect.",
    "ui.footer_detector_label": "Detector:",
    "ui.breadcrumb_aria_label": "Breadcrumb",
    "ui.last_updated_prefix": "Last updated",
    "ui.btn_try_detector": "Try the detector",
    "ui.status_ready": "Detector ready",
    "ui.status_unreachable": "Server unreachable",
    "ui.loading_model_note": "Loading detector model (first run downloads ~750 MB)…",
    "ui.error_empty_file": "That file is empty.",
    "ui.error_file_too_large": "{name} is {size} — the limit is 50 MB.",
    "ui.error_server_unreachable": "Could not reach the server: {message}",
    "ui.verdict_ai": "Likely AI-generated",
    "ui.verdict_real": "Likely a real photo",
    "ui.verdict_uncertain": "Uncertain",
    "ui.confidence_suffix": "confidence",
    "ui.format_unknown": "unknown",
    "ui.metadata_present": "Present",
    "ui.metadata_not_present": "Not present",
    "ui.no_jpeg_segments": "No JPEG APP segments",
    "ui.quota_remaining": "{remaining} of {limit} analyses left today",
}
