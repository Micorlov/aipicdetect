from io import BytesIO

from PIL import Image

from aipicdetect.detect import Detector, ai_probability, score_to_result


def _png() -> bytes:
    buffer = BytesIO()
    Image.new("RGB", (8, 8), "green").save(buffer, format="PNG")
    return buffer.getvalue()


def test_ai_probability_sums_ai_like_labels():
    scores = [{"label": "ai", "score": 0.7}, {"label": "hum", "score": 0.3}]
    assert ai_probability(scores) == 0.7
    scores = [{"label": "REAL", "score": 0.9}, {"label": "FAKE", "score": 0.1}]
    assert ai_probability(scores) == 0.1


def test_score_to_result_bands():
    high_ai = score_to_result([{"label": "ai", "score": 0.97}, {"label": "hum", "score": 0.03}], "m")
    assert (high_ai.classification, high_ai.confidence, high_ai.percent) == ("AI", "High", 97)

    real = score_to_result([{"label": "ai", "score": 0.2}, {"label": "hum", "score": 0.8}], "m")
    assert (real.classification, real.confidence) == ("Real", "Medium")

    coin_flip = score_to_result([{"label": "ai", "score": 0.52}, {"label": "hum", "score": 0.48}], "m")
    assert (coin_flip.classification, coin_flip.confidence) == ("Uncertain", "Low")


def test_detector_uses_injected_classifier_without_loading_a_model():
    seen = []

    def fake(image):
        seen.append(image.size)
        return [{"label": "artificial", "score": 0.9}, {"label": "human", "score": 0.1}]

    detector = Detector(model_name="fake/model", classifier=fake)
    result = detector.detect(_png())

    assert seen == [(8, 8)]
    assert result.classification == "AI" and result.model == "fake/model"


def test_model_name_comes_from_environment(monkeypatch):
    monkeypatch.setenv("AIPICDETECT_DETECTOR_MODEL", "org/custom-detector")
    assert Detector().model_name == "org/custom-detector"
    assert Detector(model_name="explicit/model").model_name == "explicit/model"


def test_get_detector_returns_singleton(monkeypatch):
    from aipicdetect import detect

    monkeypatch.setattr(detect, "_default_detector", None)
    first = detect.get_detector()
    assert detect.get_detector() is first


def test_load_is_idempotent_once_classifier_present():
    detector = Detector(model_name="fake/model", classifier=lambda image: [])
    detector.load()  # must not try to import/download anything
    assert detector.is_loaded


def test_ai_probability_handles_all_zero_scores():
    assert ai_probability([{"label": "ai", "score": 0.0}, {"label": "hum", "score": 0.0}]) == 0.0


def test_ai_label_hints_cover_common_names():
    from aipicdetect.detect import _is_ai_label

    assert all(_is_ai_label(n) for n in ("AI", "fake", "Artificial", "ai-generated", "synthetic"))
    assert not any(_is_ai_label(n) for n in ("hum", "real", "human", "photo"))
