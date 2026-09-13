"""Render static/og/picai-og.png (1200x630) for Open Graph / Twitter cards.

Run once with ``uv run python scripts/make_og_image.py``; the PNG is committed.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
STATIC = ROOT / "src" / "picai" / "static"
OUT = STATIC / "og" / "picai-og.png"
SIZE = (1200, 630)
BG = "#1D2130"
ACCENT = "#F3A93B"
MUTED = "#C9CEDC"
FONT_CANDIDATES = (
    "/Library/Fonts/Poppins-Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
)


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for path in FONT_CANDIDATES:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default(size)


def main() -> None:
    image = Image.new("RGB", SIZE, BG)
    draw = ImageDraw.Draw(image)
    icon = Image.open(STATIC / "icons" / "icon-512.png").convert("RGBA").resize((220, 220))
    image.paste(icon, (90, 205), icon)
    draw.text((360, 190), "picai", fill="white", font=font(110))
    draw.text((360, 320), "AI image detector", fill=ACCENT, font=font(58))
    draw.text((360, 405), "Free · open source · self-hostable", fill=MUTED, font=font(36))
    draw.rectangle((360, 470, 420, 476), fill=ACCENT)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    image.save(OUT, format="PNG", optimize=True)
    print(OUT, image.size)


if __name__ == "__main__":
    main()
