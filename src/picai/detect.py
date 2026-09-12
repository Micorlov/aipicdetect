"""AI-image likelihood scoring with a local open-source classifier.

The model is loaded lazily on first use and cached for the process. Set
``PICAI_DETECTOR_MODEL`` to any Hugging Face image-classification model whose
labels distinguish AI-generated from human-made pictures.
"""

from __future__ import annotations

import os
import threading
from dataclasses import dataclass
from io import BytesIO
from typing import Any, Callable

from PIL import Image

DEFAULT_MODEL = "Ateeqq/ai-vs-human-image-detector"
AI_LABEL_HINTS = ("ai", "fake", "artificial", "generated", "synthetic")
HIGH_CONFIDENCE_MARGIN = 0.35  # |p - 0.5| above this -> High
MEDIUM_CONFIDENCE_MARGIN = 0.15
UNCERTAIN_BAND = 0.10  # within this of 0.5 -> "Uncertain"

Classifier = Callable[[Image.Image], list[dict[str, Any]]]


@dataclass(frozen=True)
class DetectResult:
    ai_likelihood: float  # 0..1
    confidence: str  # High / Medium / Low
    classification: str  # AI / Real / Uncertain
    model: str

    @property
    def percent(self) -> int:
        return round(self.ai_likelihood * 100)


class Detector:
    """Thread-safe lazy wrapper around a transformers image-classification pipeline."""

    def __init__(self, model_name: str | None = None, classifier: Classifier | None = None) -> None:
        self.model_name = model_name or os.environ.get("PICAI_DETECTOR_MODEL", DEFAULT_MODEL)
        self._classifier = classifier
        self._lock = threading.Lock()

    @property
    def is_loaded(self) -> bool:
        return self._classifier is not None

    def load(self) -> None:
        with self._lock:
            if self._classifier is not None:
                return
            from transformers import pipeline

            self._classifier = pipeline("image-classification", model=self.model_name, top_k=None)

    def detect(self, image_bytes: bytes) -> DetectResult:
        if self._classifier is None:
            self.load()
        assert self._classifier is not None
        image = Image.open(BytesIO(image_bytes)).convert("RGB")
        scores = self._classifier(image)
        return score_to_result(scores, self.model_name)


def ai_probability(scores: list[dict[str, Any]]) -> float:
    """Sum the probability mass of every label that names AI/fake content."""
    total = sum(float(s["score"]) for s in scores) or 1.0
    ai_mass = sum(float(s["score"]) for s in scores if _is_ai_label(str(s["label"])))
    return max(0.0, min(1.0, ai_mass / total))


def score_to_result(scores: list[dict[str, Any]], model_name: str) -> DetectResult:
    p = ai_probability(scores)
    margin = abs(p - 0.5)
    if margin >= HIGH_CONFIDENCE_MARGIN:
        confidence = "High"
    elif margin >= MEDIUM_CONFIDENCE_MARGIN:
        confidence = "Medium"
    else:
        confidence = "Low"
    if margin < UNCERTAIN_BAND:
        classification = "Uncertain"
    else:
        classification = "AI" if p > 0.5 else "Real"
    return DetectResult(ai_likelihood=p, confidence=confidence, classification=classification, model=model_name)


def _is_ai_label(label: str) -> bool:
    text = label.lower()
    return any(hint in text for hint in AI_LABEL_HINTS)


_default_detector: Detector | None = None


def get_detector() -> Detector:
    global _default_detector
    if _default_detector is None:
        _default_detector = Detector()
    return _default_detector
