"""Hungarian translation table.

Falls back to English (see :func:`aipicdetect.content.locales.t`) for any key not defined here, but
every key from :mod:`aipicdetect.content.locales.en` is translated below.
"""

from __future__ import annotations

STRINGS: dict[str, str] = {
    # Page metadata
    "page.home.title": "AiPicDetect — nyílt forráskódú AI-képdetektor és metaadat-eltávolító",
    "page.home.description": (
        "A AiPicDetect, egy ingyenes, nyílt forráskódú detektor segítségével ellenőrizheted, hogy egy "
        "kép AI-generált-e. Használhatod böngészőben, vagy futtathatod a saját gépeden Dockerrel "
        "vagy Pythonnal."
    ),
    "page.home.h1": "Valódi ez a fotó? Nézd meg a pontszámot és a bizonyítékot.",
    "page.faq.title": "GYIK az AI-képdetektorról: pontosság, adatvédelem, formátumok, modellek",
    "page.faq.description": (
        "Válaszok a AiPicDetect szolgáltatással kapcsolatos leggyakoribb kérdésekre: mennyire pontos az "
        "AI-alapú képfelismerés, hol dolgozzák fel a képedet, milyen formátumokat támogat, hogyan "
        "cserélhető le a modell, és milyenek a kérési korlátok."
    ),
    "page.faq.h1": "A AiPicDetect gyakran ismételt kérdései",
    "page.faq.intro_suffix": (
        "Ezeket a kérdéseket teszik fel a leggyakrabban: hogyan működik, mennyire pontos, és mi "
        "történik a feltöltött képekkel."
    ),
    "page.faq.still_unsure_html": (
        'Még mindig bizonytalan vagy? Nyiss egy issue-t a '
        '<a href="https://github.com/Micorlov/aipicdetect/issues" rel="noopener">GitHubon</a>.'
    ),
    # Home page copy
    "home.entity_sentence": (
        "A AiPicDetect egy ingyenes, nyílt forráskódú eszköz, amely pontszámot ad az AI-generált "
        "képeknek, és eltávolítja a rejtett metaadatokat — hosztolt vagy self-hosted verzióban, a "
        "választás rajtad múlik."
    ),
    "home.lead": (
        "A AiPicDetect egy nyílt AI-detektáló modellt futtat, és beolvassa a fotó minden EXIF, C2PA és "
        "IPTC mezőjét — majd egy tiszta másolatot ad, amelyből mindezt eltávolította. Regisztráció "
        "és fekete doboz nélkül."
    ),
    "home.dropzone_note": (
        "JPEG, PNG, WebP, HEIC · legfeljebb 50 MB · memóriában dolgozzuk fel, sosem kerül lemezre"
    ),
    "home.summary": (
        "A AiPicDetect egy ingyenes, nyílt forráskódú eszköz, amely pontszámot ad az AI-generált "
        "képeknek, és eltávolítja a rejtett metaadatokat — hosztolt vagy self-hosted verzióban, a "
        "választás rajtad múlik. Egy nyílt Hugging Face osztályozó segítségével megbecsüli, mekkora "
        "eséllyel készült a kép AI-generátorral, és képes újrarenderelni a képeket az EXIF, XMP, "
        "IPTC, ICC és C2PA metaadatok eltávolításához. Használd a hosztolt példányt, vagy telepítsd "
        "a AiPicDetect szoftvert saját magad Dockerrel vagy Pythonnal."
    ),
    "home.stat.0": "nyílt modell,<br>nincs külső API",
    "home.stat.1": "regisztráció<br>szükséges",
    "home.stat.2": "MB<br>feltöltési limit",
    # Detect steps
    "steps.detect.upload.name": "Feltöltés.",
    "steps.detect.upload.text": (
        "Húzd be, illeszd be vagy válaszd ki a képet. A kép elküldésre kerül a használt AiPicDetect "
        "szerverre (self-hosted esetén a saját gépedre), a memóriában marad, és sosem kerül "
        "lemezre."
    ),
    "steps.detect.detect.name": "Észlelés.",
    "steps.detect.detect.text": (
        "Egy nyílt forráskódú képosztályozó megbecsüli, mekkora eséllyel készültek a pixelek egy "
        "generátorral."
    ),
    "steps.detect.decide.name": "Döntés.",
    "steps.detect.decide.text": (
        "Megkapod az AI valószínűségét, egy megbízhatósági sávot és a fájlban található "
        "metaadat-blokkokat — valószínűségként, nem ítéletként."
    ),
    # Scrub steps — <code> blocks contain literal shell commands and must stay untranslated
    "steps.scrub.inspect.name": "Vizsgálat.",
    "steps.scrub.inspect.text": (
        "Futtasd le a <code>aipicdetect inspect photo.jpg</code> parancsot, hogy listázd a fájlban lévő "
        "EXIF, XMP, IPTC, C2PA és ICC blokkokat."
    ),
    "steps.scrub.scrub.name": "Tisztítás.",
    "steps.scrub.scrub.text": (
        "Futtasd le a <code>aipicdetect scrub photo.jpg</code> parancsot (vagy a <code>POST /scrub</code> "
        "kérést). A AiPicDetect dekódolja a pixeleket, alkalmazza az EXIF tájolást, és a nyers "
        "pixelpufferből felépít egy vadonatúj képet."
    ),
    "steps.scrub.verify.name": "Ellenőrzés.",
    "steps.scrub.verify.text": (
        "Futtasd le a <code>aipicdetect inspect photo.clean.jpg</code> parancsot; ekkor a „no metadata "
        "signatures found” üzenetnek kell megjelennie."
    ),
    # FAQ (home slugs)
    "faq.accuracy.question": "Mennyire pontos a detektor?",
    "faq.accuracy.answer_html": (
        "Ez egy valószínűséget közöl, nem ítéletet. Az 50% körüli pontszámok "
        "<em>Bizonytalan</em> jelölést kapnak; kezelj minden egyes eredményt egyetlen jelzésként, "
        'és kombináld más bizonyítékokkal. További részletek: <a href="/how-accurate">mennyire '
        "pontosak az AI-képdetektorok</a>."
    ),
    "faq.leaves_computer.question": "Elhagyja a képem a számítógépemet?",
    "faq.leaves_computer.answer_html": (
        "Ezen a nyilvános példányon igen: a kép feltöltődik a AiPicDetect szerverre (egy, a szerző által "
        "futtatott Google Cloud Run konténerbe), a memóriában történik a kiértékelés, és sosem "
        "kerül lemezre. A megtisztított másolat csak addig marad a memóriában, amíg 100 újabb "
        "eredmény le nem váltja, vagy amíg a konténer újra nem indul, és semmi nem kerül elküldésre "
        "külső API-nak. Ha azt szeretnéd, hogy semmi ne hagyja el a gépedet, "
        '<a href="/self-host">telepítsd a AiPicDetect rendszert saját magad</a> egyetlen Docker '
        'paranccsal. A részletek az <a href="/privacy">adatvédelmi oldalon</a> találhatók.'
    ),
    "faq.open_source.question": "Nyílt forráskódú?",
    "faq.open_source.answer_html": (
        "Igen. A kód, a Docker image, a CLI és a GitHub Action mind megtalálható a "
        '<a href="https://github.com/Micorlov/aipicdetect" rel="noopener">AiPicDetect tárolóban</a>, MIT '
        "licenc alatt. A detektor egy nyílt Hugging Face modell, amelyet megvizsgálhatsz vagy "
        "lecserélhetsz."
    ),
    "faq.remove_metadata.question": "Eltávolíthatom a C2PA-t és más metaadatokat?",
    "faq.remove_metadata.answer_html": (
        "Igen. A kép ellenőrzése után használd a <em>Tiszta másolat letöltése</em> gombot. A AiPicDetect "
        "a pixelekből építi újra a képet, így az EXIF, XMP, IPTC, C2PA és az ICC profil is teljesen "
        'eltűnik. <a href="/remove-image-metadata">Hogyan működik a tisztítás</a>.'
    ),
    "faq.formats.question": "Milyen formátumokat támogat?",
    "faq.formats.answer_html": (
        "JPEG, PNG, WebP, HEIC/HEIF és a legtöbb formátum, amelyet a Pillow dekódolni tud, "
        "legfeljebb 50 MB méretig."
    ),
    "faq.why_metadata.question": "Miért vannak felsorolva a metaadatok?",
    "faq.why_metadata.answer_html": (
        "A C2PA tartalomhitelesítési adatok és a szerkesztőszoftver-címkék a fájl eredetére utaló "
        "jelek. A panel megmutatja, mely blokkokat (EXIF, XMP, IPTC, C2PA, ICC) hordozza a fájl, "
        'hogy ezeket a pontszám mellett is mérlegelhesd. Lásd: <a href="/c2pa">C2PA '
        'tartalomhitelesítési adatok</a> és <a href="/remove-image-metadata">hogyan távolíthatók el '
        "a kép metaadatai</a>."
    ),
    "faq.different_model.question": "Használhatok másik modellt?",
    "faq.different_model.answer_html": (
        "Igen. Állítsd be a <code>PICAI_DETECTOR_MODEL</code> változót bármely Hugging Face "
        "képosztályozó modellre, amelynek címkéi AI/hamis és emberi/valódi tartalmat "
        "különböztetnek meg."
    ),
    # FAQ (more slugs)
    "faq.free.question": "Ingyenes a AiPicDetect?",
    "faq.free.answer_html": (
        "Igen. A AiPicDetect nyílt forráskódú, MIT licenc alatt. A hosztolt példány ingyenesen "
        "használható, IP-címenként napi 10 elemzés korlátjával; egy self-hosted példánynak nincs "
        "korlátja."
    ),
    "faq.screenshots.question": "Működik képernyőképeken vagy erősen tömörített képeken?",
    "faq.screenshots.answer_html": (
        "Fut rajtuk, de az újrakódolás, az átméretezés és a képernyőképek eltüntetik a pixelszintű "
        "nyomok egy részét, amelyekre az osztályozó támaszkodik, ezért számíts alacsonyabb "
        "megbízhatóságra és több <em>Bizonytalan</em> eredményre."
    ),
    "faq.which_generator.question": (
        "Meg tudja mondani, melyik generátor készítette a képet (Midjourney, DALL·E, Stable "
        "Diffusion)?"
    ),
    "faq.which_generator.answer_html": (
        "Nem. A AiPicDetect általánosságban a generált és a valódi pixelek statisztikáit értékeli; nem "
        "azonosítja a konkrét generátort, és nincs tudomása azokról a generátorokról, amelyek a "
        "modell tanítóadatainak gyűjtése után jelentek meg."
    ),
    "faq.false_positive.question": "Miért kapott AI besorolást egy valódi fotó?",
    "faq.false_positive.answer_html": (
        "Az erős szűrők, a HDR-feldolgozás, a felskálázás, az illusztrációk és a 3D renderek "
        "statisztikai jellemzőkben osztoznak a generált képekkel. A pontszám valószínűség, nem "
        "bizonyíték; előfordulnak téves pozitív eredmények."
    ),
    "faq.offline.question": "Futtathatom offline is?",
    "faq.offline.answer_html": (
        "Igen. Miután az első futtatás letölti a modellt a Hugging Face gyorsítótárba, egy "
        "self-hosted AiPicDetect rendszernek nincs szüksége hálózati hozzáférésre."
    ),
    "faq.rate_limit.question": "Van kérési korlát a hosztolt példányon?",
    "faq.rate_limit.answer_html": (
        "Igen: kliens IP-nként 10 elemzés bármely gördülő 24 órás időszakban. A válaszok "
        "tartalmazzák a <code>X-RateLimit-Remaining</code> fejlécet, a limitet túllépő kérés pedig "
        "429-es választ ad <code>Retry-After</code> fejléccel."
    ),
    # Navigation
    "nav.detector": "Detektor",
    "nav.how_it_works": "Hogyan működik",
    "nav.how-to-tell-if-an-image-is-ai-generated": "Útmutató",
    "nav.api": "API",
    "nav.self-host": "Self-hosting",
    # Footer
    "footer.remove-image-metadata": "Metaadatok eltávolítása",
    "footer.c2pa": "C2PA",
    "footer.faq": "GYIK",
    "footer.privacy": "Adatvédelem",
    "footer.self-host": "Self-hosting",
    "footer.about": "A projektről",
    # UI strings
    "ui.nav_aria_label": "Fő navigáció",
    "ui.loading_status": "Detektor betöltése…",
    "ui.hero_overline": "— Nyílt forráskódú AI-képforenzika",
    "ui.hero_heading_line1": "Valódi ez a fotó?",
    "ui.hero_heading_line2": "Nézd meg a pontszámot és a bizonyítékot.",
    "ui.tool_aria_label": "AI-képdetektor",
    "ui.dropzone_aria_label": "Tölts fel egy képet elemzésre",
    "ui.dropzone_title_fine": "Húzd ide a fotót",
    "ui.dropzone_title_coarse": "Ellenőrizz egy fotót",
    "ui.dropzone_sub_fine": "vagy illeszd be a vágólapról, vagy",
    "ui.dropzone_sub_coarse": "a galériádból vagy a kamerával",
    "ui.btn_check_image_fine": "Kép ellenőrzése",
    "ui.btn_choose_photo_coarse": "Fotó kiválasztása",
    "ui.btn_take_photo": "Fotó készítése",
    "ui.dismiss_aria_label": "Bezárás",
    "ui.analyzing_prefix": "Elemzés",
    "ui.analyzing_suffix": "· pixelek · metaadat-blokkok",
    "ui.verdict_overline": "— Ítélet",
    "ui.meter_real": "Valódi",
    "ui.meter_uncertain": "Bizonytalan",
    "ui.meter_ai": "AI",
    "ui.model_label": "Modell",
    "ui.verdict_disclaimer_html": (
        "Az eredmények egy osztályozótól származó valószínűségek, nem ítéletek. "
        '<a href="/how-accurate">Hogyan olvasd a pontszámot.</a>'
    ),
    "ui.btn_check_another": "Másik kép ellenőrzése",
    "ui.preview_overline": "— Előnézet",
    "ui.preview_alt": "A feltöltött kép előnézete",
    "ui.metadata_overline": "— Metaadatok",
    "ui.metadata_heading": "A fájlban található.",
    "ui.jpeg_segments_label": "JPEG szegmensek",
    "ui.btn_download_clean": "Tiszta másolat letöltése",
    "ui.metadata_scrub_note_html": (
        "A pixelekből lett újrarenderelve, ezért a fenti blokkok mindegyike eltűnt. "
        '<a href="/remove-image-metadata">Hogyan működik</a>'
    ),
    "ui.how_it_works_overline": "— Hogyan működik",
    "ui.how_it_works_heading": "Három lépés. Semmi sem kerül mentésre.",
    "ui.how_it_works_links_html": (
        '<a href="/how-to-tell-if-an-image-is-ai-generated">Olvasd el az útmutatót az AI-képek '
        'felismeréséhez</a>, vagy <a href="/self-host">futtasd a saját gépeden</a>.'
    ),
    "ui.faq_overline": "— GYIK",
    "ui.faq_heading": "Mielőtt kérdeznél.",
    "ui.faq_more_link": "További kérdések és válaszok →",
    "ui.footer_tagline": "AiPicDetect. · open source",
    "ui.footer_detector_label": "Detektor:",
    "ui.breadcrumb_aria_label": "Morzsamenü",
    "ui.last_updated_prefix": "Utolsó frissítés",
    "ui.source_on_github": "forráskód a GitHubon",
    "ui.btn_try_detector": "Próbáld ki a detektort",
    "ui.status_ready": "A detektor kész",
    "ui.status_unreachable": "A szerver nem elérhető",
    "ui.loading_model_note": "A detektor modelljének betöltése (az első futtatás ~750 MB-ot tölt le)…",
    "ui.error_empty_file": "Ez a fájl üres.",
    "ui.error_file_too_large": "{name} mérete {size} — a korlát 50 MB.",
    "ui.error_server_unreachable": "Nem sikerült elérni a szervert: {message}",
    "ui.verdict_ai": "Valószínűleg AI-generált",
    "ui.verdict_real": "Valószínűleg valódi fotó",
    "ui.verdict_uncertain": "Bizonytalan",
    "ui.confidence_suffix": "megbízhatóság",
    "ui.format_unknown": "ismeretlen",
    "ui.metadata_present": "Jelen van",
    "ui.metadata_not_present": "Nincs jelen",
    "ui.no_jpeg_segments": "Nincsenek JPEG APP szegmensek",
    "ui.quota_remaining": "Ma még {remaining} elemzésed maradt a napi {limit}-ből",
}
