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
    "page.home.title": "AiPicDetect — Open-Source AI Detector & Metadata Scrubber",
    "page.home.description": (
        "Check whether a picture is AI-generated with AiPicDetect, a free open-source detector. Use it in "
        "the browser or on your own machine with Docker or Python."
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
        'Still unsure? Open an issue on <a href="https://github.com/Micorlov/aipicdetect/issues" '
        'rel="noopener">GitHub</a>.'
    ),
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
    "ui.nav_aria_label": "Main navigation",
    "ui.loading_status": "Loading detector…",
    "ui.hero_overline": "— Open-source AI image forensics",
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
        '<a href="/how-to-tell-if-an-image-is-ai-generated">Read the guide to spotting AI images</a> '
        'or <a href="/self-host">run it on your own machine</a>.'
    ),
    "ui.faq_overline": "— FAQ",
    "ui.faq_heading": "Before you ask.",
    "ui.faq_more_link": "More questions and answers →",
    "ui.footer_tagline": "AiPicDetect. · open source",
    "ui.footer_detector_label": "Detector:",
    "ui.breadcrumb_aria_label": "Breadcrumb",
    "ui.last_updated_prefix": "Last updated",
    "ui.source_on_github": "source on GitHub",
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
