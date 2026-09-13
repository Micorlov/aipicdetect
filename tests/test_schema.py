import json
import re
from html.parser import HTMLParser

import pytest
from fastapi.testclient import TestClient
from PIL import Image

from aipicdetect import pages, schema, server
from aipicdetect.content.faq import FAQ_HOME
from aipicdetect.content.home import DETECT_STEPS, SCRUB_STEPS

client = TestClient(server.app)


@pytest.fixture(autouse=True)
def public_url(monkeypatch):
    monkeypatch.setenv("AIPICDETECT_PUBLIC_URL", "https://aipicdetect.example")


def graph(path: str) -> list[dict]:
    html = client.get(path).text
    match = re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
    payload = json.loads(match.group(1))
    assert payload["@context"] == "https://schema.org"
    return payload["@graph"]


class _Headings(HTMLParser):
    def __init__(self, tag):
        super().__init__()
        self.tag, self.texts, self._in = tag, [], False

    def handle_starttag(self, tag, attrs):
        self._in = tag == self.tag

    def handle_endtag(self, tag):
        self._in = False

    def handle_data(self, data):
        if self._in:
            self.texts.append(data)


def headings(html: str, tag: str) -> list[str]:
    parser = _Headings(tag)
    parser.feed(html)
    return parser.texts


def test_home_jsonld_has_expected_types_and_free_offer():
    items = {item["@type"]: item for item in graph("/")}
    assert {"WebSite", "SoftwareApplication", "FAQPage", "HowTo"} <= items.keys()
    app = items["SoftwareApplication"]
    assert app["offers"]["price"] == "0" and app["url"] == "https://aipicdetect.example/"
    assert app["codeRepository"] == "https://github.com/Micorlov/aipicdetect"
    assert app["description"].startswith("AiPicDetect is a free, open-source tool that scores AI-generated images")


def test_faq_jsonld_questions_equal_visible_faq():
    html = client.get("/").text
    faq = next(i for i in graph("/") if i["@type"] == "FAQPage")
    assert [q["name"] for q in faq["mainEntity"]] == headings(html, "summary") == [e.question for e in FAQ_HOME]
    assert faq["mainEntity"][0]["acceptedAnswer"]["text"] == FAQ_HOME[0].answer_html


def test_howto_steps_equal_visible_steps():
    home = next(i for i in graph("/") if i["@type"] == "HowTo")
    assert [s["name"] for s in home["step"]] == headings(client.get("/").text, "h3") == [s.name for s in DETECT_STEPS]
    scrub = next(i for i in graph("/remove-image-metadata") if i["@type"] == "HowTo")
    assert [s["name"] for s in scrub["step"]] == [s.name for s in SCRUB_STEPS]
    assert all(name in client.get("/remove-image-metadata").text for name in scrub["step"][0].values() if isinstance(name, str))


def test_article_pages_carry_date_and_author():
    item = next(i for i in graph("/how-accurate") if i["@type"] == "Article")
    assert item["dateModified"] == pages.page_for("/how-accurate").lastmod.isoformat()
    assert item["author"]["name"] == "Michael Orlov"


def test_jsonld_escapes_closing_script_tags():
    out = schema.jsonld_for_page(pages.HOME, "https://x.example", "en")
    assert "</script>" in out and out.count("</script>") == 1


def test_og_image_exists_and_is_1200x630():
    with Image.open(pages.STATIC_DIR / "og" / "aipicdetect-og.png") as image:
        assert image.size == (1200, 630)
    assert client.get("/static/og/aipicdetect-og.png").status_code == 200
