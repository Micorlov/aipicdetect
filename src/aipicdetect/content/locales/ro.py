"""Romanian translation table.

Falls back to English (see :func:`aipicdetect.content.locales.t`) for any key not defined here, but
every key from :mod:`aipicdetect.content.locales.en` is translated below.
"""

from __future__ import annotations

STRINGS: dict[str, str] = {
    # Page metadata
    "page.home.title": (
        "AiPicDetect — detector open-source de imagini generate de AI și instrument de curățare a "
        "metadatelor"
    ),
    "page.home.description": (
        "Verifică dacă o imagine este generată de AI cu AiPicDetect, un detector gratuit și open-source. "
        "Folosește-l în browser sau rulează-l pe propriul calculator cu Docker sau Python."
    ),
    "page.home.h1": "Această fotografie este reală? Află scorul și dovada.",
    "page.faq.title": (
        "Întrebări frecvente despre detectorul de imagini AI: acuratețe, confidențialitate, "
        "formate, modele"
    ),
    "page.faq.description": (
        "Răspunsuri la întrebările frecvente despre AiPicDetect: cât de precisă este detectarea "
        "imaginilor AI, unde este procesată imaginea ta, ce formate sunt acceptate, schimbarea "
        "modelului și limitele de cereri."
    ),
    "page.faq.h1": "Întrebări frecvente despre AiPicDetect",
    "page.faq.intro_suffix": (
        "Acestea sunt întrebările pe care oamenii le pun cel mai des: cum funcționează, cât de "
        "precis este și ce se întâmplă cu imaginile încărcate."
    ),
    "page.faq.still_unsure_html": (
        'Încă nu ești sigur? Deschide un issue pe <a href="https://github.com/Micorlov/aipicdetect/issues" '
        'rel="noopener">GitHub</a>.'
    ),
    # Home page copy
    "home.entity_sentence": (
        "AiPicDetect este un instrument gratuit, open-source, care evaluează probabilitatea ca o imagine "
        "să fie generată de AI și elimină metadatele ascunse — găzduit sau self-hosted, alegerea "
        "îți aparține."
    ),
    "home.lead": (
        "AiPicDetect rulează un model deschis de detectare AI și citește fiecare câmp EXIF, C2PA și IPTC "
        "purtat de o fotografie — apoi îți oferă o copie curată din care toate acestea au fost "
        "eliminate. Fără înregistrare, fără cutie neagră."
    ),
    "home.dropzone_note": (
        "JPEG, PNG, WebP, HEIC · până la 50 MB · procesată în memorie, niciodată scrisă pe disc"
    ),
    "home.summary": (
        "AiPicDetect este un instrument gratuit, open-source, care evaluează probabilitatea ca o imagine "
        "să fie generată de AI și elimină metadatele ascunse — găzduit sau self-hosted, alegerea "
        "îți aparține. Evaluează probabilitatea ca o imagine să fi fost produsă de un generator AI "
        "folosind un clasificator Hugging Face deschis și poate re-reda imaginile pentru a elimina "
        "metadatele EXIF, XMP, IPTC, ICC și C2PA. Folosește instanța găzduită sau auto-găzduiește-l "
        "cu Docker sau Python."
    ),
    "home.stat.0": "model deschis,<br>fără API terț",
    "home.stat.1": "înregistrări<br>necesare",
    "home.stat.2": "MB<br>limită de încărcare",
    # Detect steps
    "steps.detect.upload.name": "Încarcă.",
    "steps.detect.upload.text": (
        "Trage, lipește sau alege o imagine. Aceasta este trimisă către serverul AiPicDetect pe care îl "
        "folosești (propriul calculator, în cazul instanței self-hosted), este păstrată în memorie "
        "și nu este niciodată scrisă pe disc."
    ),
    "steps.detect.detect.name": "Detectează.",
    "steps.detect.detect.text": (
        "Un clasificator de imagini open-source evaluează probabilitatea ca pixelii să fi fost "
        "produși de un generator."
    ),
    "steps.detect.decide.name": "Decide.",
    "steps.detect.decide.text": (
        "Primești o probabilitate de generare AI, un interval de încredere și blocurile de "
        "metadate purtate de fișier — ca probabilitate, nu ca verdict."
    ),
    # Scrub steps — <code> blocks contain literal shell commands and must stay untranslated
    "steps.scrub.inspect.name": "Inspectează.",
    "steps.scrub.inspect.text": (
        "Rulează <code>aipicdetect inspect photo.jpg</code> pentru a lista blocurile EXIF, XMP, IPTC, "
        "C2PA și ICC purtate de fișier."
    ),
    "steps.scrub.scrub.name": "Curăță.",
    "steps.scrub.scrub.text": (
        "Rulează <code>aipicdetect scrub photo.jpg</code> (sau <code>POST /scrub</code>). AiPicDetect decodează "
        "pixelii, aplică orientarea EXIF și construiește o imagine complet nouă din bufferul brut "
        "de pixeli."
    ),
    "steps.scrub.verify.name": "Verifică.",
    "steps.scrub.verify.text": (
        "Rulează <code>aipicdetect inspect photo.clean.jpg</code>; ar trebui să afișeze „no metadata "
        "signatures found”."
    ),
    # FAQ (home slugs)
    "faq.accuracy.question": "Cât de precis este detectorul?",
    "faq.accuracy.answer_html": (
        "Acesta oferă o probabilitate, nu un verdict. Scorurile apropiate de 50% sunt etichetate "
        "<em>Incert</em>; tratează orice rezultat izolat ca pe un simplu semnal și combină-l cu "
        'alte dovezi. Află mai multe despre <a href="/how-accurate">cât de precise sunt '
        "detectoarele de imagini AI</a>."
    ),
    "faq.leaves_computer.question": "Îmi părăsește imaginea computerul?",
    "faq.leaves_computer.answer_html": (
        "Pe această instanță publică, da: imaginea este încărcată pe serverul AiPicDetect (un container "
        "Google Cloud Run rulat de autor), evaluată în memorie și niciodată scrisă pe disc. Copia "
        "curățată este păstrată în memorie doar până când este înlocuită de 100 de rezultate mai "
        "noi sau containerul repornește, iar nimic nu este trimis către un API terț. Dacă vrei ca "
        'nimic să nu părăsească dispozitivul tău, <a href="/self-host">rulează AiPicDetect chiar tu</a> '
        'cu o singură comandă Docker. Detaliile sunt pe <a href="/privacy">pagina de '
        "confidențialitate</a>."
    ),
    "faq.open_source.question": "Este open source?",
    "faq.open_source.answer_html": (
        "Da. Codul, imaginea Docker, CLI-ul și GitHub Action se află toate în "
        '<a href="https://github.com/Micorlov/aipicdetect" rel="noopener">repository-ul AiPicDetect</a>, sub '
        "licența MIT. Detectorul este un model deschis Hugging Face pe care îl poți inspecta sau "
        "înlocui."
    ),
    "faq.remove_metadata.question": "Pot elimina C2PA și alte metadate?",
    "faq.remove_metadata.answer_html": (
        "Da. După ce verifici o imagine, folosește <em>Descarcă o copie curată</em>. AiPicDetect "
        "reconstruiește imaginea din pixelii ei, astfel încât EXIF, XMP, IPTC, C2PA și profilul ICC "
        'sunt toate eliminate. <a href="/remove-image-metadata">Cum funcționează curățarea</a>.'
    ),
    "faq.formats.question": "Ce formate sunt acceptate?",
    "faq.formats.answer_html": (
        "JPEG, PNG, WebP, HEIC/HEIF și majoritatea formatelor pe care Pillow le poate decoda, până "
        "la 50 MB."
    ),
    "faq.why_metadata.question": "De ce sunt listate metadatele?",
    "faq.why_metadata.answer_html": (
        "Acreditările de conținut C2PA și etichetele software-ului de editare sunt indicii de "
        "proveniență. Panoul arată ce blocuri (EXIF, XMP, IPTC, C2PA, ICC) poartă fișierul, ca să "
        'le poți lua în calcul alături de scor. Vezi <a href="/c2pa">acreditările de conținut '
        'C2PA</a> și <a href="/remove-image-metadata">cum se elimină metadatele unei imagini</a>.'
    ),
    "faq.different_model.question": "Pot folosi un alt model?",
    "faq.different_model.answer_html": (
        "Da. Setează <code>PICAI_DETECTOR_MODEL</code> la orice model de clasificare a imaginilor "
        "de pe Hugging Face ale cărui etichete disting conținut AI/fals față de uman/real."
    ),
    # FAQ (more slugs)
    "faq.free.question": "AiPicDetect este gratuit?",
    "faq.free.answer_html": (
        "Da. AiPicDetect este open source, sub licența MIT. Instanța găzduită este gratuită, cu o limită "
        "de 10 analize per adresă IP la fiecare 24 de ore; o copie self-hosted nu are nicio limită."
    ),
    "faq.screenshots.question": "Funcționează pe capturi de ecran sau imagini puternic comprimate?",
    "faq.screenshots.answer_html": (
        "Funcționează, dar recodarea, redimensionarea și capturile de ecran elimină o parte din "
        "urmele la nivel de pixel pe care se bazează clasificatorul, așa că poți avea încredere mai "
        "scăzută și mai multe rezultate <em>Incert</em>."
    ),
    "faq.which_generator.question": (
        "Poate spune care generator a creat o imagine (Midjourney, DALL·E, Stable Diffusion)?"
    ),
    "faq.which_generator.answer_html": (
        "Nu. AiPicDetect evaluează, în general, statistici de pixeli generat-versus-real; nu identifică "
        "generatorul și nu are nicio cunoștință despre generatoarele apărute după colectarea "
        "datelor de antrenare ale modelului său."
    ),
    "faq.false_positive.question": "De ce o fotografie reală a fost evaluată ca fiind AI?",
    "faq.false_positive.answer_html": (
        "Filtrele puternice, procesarea HDR, mărirea rezoluției (upscaling), ilustrațiile și "
        "randările 3D au caracteristici statistice comune cu imaginile generate. Scorul este o "
        "probabilitate, nu o dovadă; apar și rezultate fals pozitive."
    ),
    "faq.offline.question": "Pot să îl rulez offline?",
    "faq.offline.answer_html": (
        "Da. După ce prima rulare descarcă modelul în cache-ul Hugging Face, o instanță AiPicDetect "
        "self-hosted nu mai are nevoie de acces la rețea."
    ),
    "faq.rate_limit.question": "Există o limită de cereri pe instanța găzduită?",
    "faq.rate_limit.answer_html": (
        "Da: 10 analize per IP de client în orice fereastră glisantă de 24 de ore. Răspunsurile "
        "poartă antetul <code>X-RateLimit-Remaining</code>, iar o cerere peste limită returnează "
        "429 cu antetul <code>Retry-After</code>."
    ),
    # Navigation
    "nav.detector": "Detector",
    "nav.how_it_works": "Cum funcționează",
    "nav.how-to-tell-if-an-image-is-ai-generated": "Ghid",
    "nav.api": "API",
    "nav.self-host": "Self-hosting",
    # Footer
    "footer.remove-image-metadata": "Eliminarea metadatelor",
    "footer.c2pa": "C2PA",
    "footer.faq": "Întrebări frecvente",
    "footer.privacy": "Confidențialitate",
    "footer.self-host": "Self-hosting",
    "footer.about": "Despre proiect",
    # UI strings
    "ui.nav_aria_label": "Navigare principală",
    "ui.loading_status": "Se încarcă detectorul…",
    "ui.hero_overline": "— Analiză criminalistică open-source a imaginilor AI",
    "ui.hero_heading_line1": "Această fotografie este reală?",
    "ui.hero_heading_line2": "Află scorul și dovada.",
    "ui.tool_aria_label": "Detector de imagini AI",
    "ui.dropzone_aria_label": "Încarcă o imagine pentru analiză",
    "ui.dropzone_title_fine": "Trage și plasează o fotografie",
    "ui.dropzone_title_coarse": "Verifică o fotografie",
    "ui.dropzone_sub_fine": "sau lipește din clipboard, sau",
    "ui.dropzone_sub_coarse": "din galerie sau de la cameră",
    "ui.btn_check_image_fine": "Verifică această imagine",
    "ui.btn_choose_photo_coarse": "Alege o fotografie",
    "ui.btn_take_photo": "Fă o fotografie",
    "ui.dismiss_aria_label": "Închide",
    "ui.analyzing_prefix": "Se analizează",
    "ui.analyzing_suffix": "· pixeli · blocuri de metadate",
    "ui.verdict_overline": "— Verdict",
    "ui.meter_real": "Real",
    "ui.meter_uncertain": "Incert",
    "ui.meter_ai": "AI",
    "ui.model_label": "Model",
    "ui.verdict_disclaimer_html": (
        "Rezultatele sunt probabilități oferite de un clasificator, nu verdicte. "
        '<a href="/how-accurate">Cum se citește scorul.</a>'
    ),
    "ui.btn_check_another": "Verifică o altă imagine",
    "ui.preview_overline": "— Previzualizare",
    "ui.preview_alt": "Previzualizarea imaginii încărcate",
    "ui.metadata_overline": "— Metadate",
    "ui.metadata_heading": "Găsite în fișier.",
    "ui.jpeg_segments_label": "Segmente JPEG",
    "ui.btn_download_clean": "Descarcă o copie curată",
    "ui.metadata_scrub_note_html": (
        "Re-randată din pixeli, așa că fiecare bloc de mai sus a dispărut. "
        '<a href="/remove-image-metadata">Cum funcționează</a>'
    ),
    "ui.how_it_works_overline": "— Cum funcționează",
    "ui.how_it_works_heading": "Trei pași. Nimic nu este salvat.",
    "ui.how_it_works_links_html": (
        '<a href="/how-to-tell-if-an-image-is-ai-generated">Citește ghidul pentru recunoașterea '
        'imaginilor AI</a> sau <a href="/self-host">rulează-l pe propriul calculator</a>.'
    ),
    "ui.faq_overline": "— Întrebări frecvente",
    "ui.faq_heading": "Înainte să întrebi.",
    "ui.faq_more_link": "Mai multe întrebări și răspunsuri →",
    "ui.footer_tagline": "AiPicDetect. · open source",
    "ui.footer_detector_label": "Detector:",
    "ui.breadcrumb_aria_label": "Fir de Ariadnă",
    "ui.last_updated_prefix": "Ultima actualizare",
    "ui.source_on_github": "codul sursă pe GitHub",
    "ui.btn_try_detector": "Încearcă detectorul",
    "ui.status_ready": "Detector pregătit",
    "ui.status_unreachable": "Serverul nu poate fi contactat",
    "ui.loading_model_note": "Se încarcă modelul detectorului (prima rulare descarcă ~750 MB)…",
    "ui.error_empty_file": "Acest fișier este gol.",
    "ui.error_file_too_large": "{name} are {size} — limita este de 50 MB.",
    "ui.error_server_unreachable": "Nu s-a putut contacta serverul: {message}",
    "ui.verdict_ai": "Probabil generată de AI",
    "ui.verdict_real": "Probabil o fotografie reală",
    "ui.verdict_uncertain": "Incert",
    "ui.confidence_suffix": "încredere",
    "ui.format_unknown": "necunoscut",
    "ui.metadata_present": "Prezente",
    "ui.metadata_not_present": "Absente",
    "ui.no_jpeg_segments": "Niciun segment JPEG APP",
    "ui.quota_remaining": "Mai ai {remaining} din {limit} analize disponibile azi",
}
