"""Dutch translation table."""

from __future__ import annotations

STRINGS: dict[str, str] = {
    "page.home.title": "picai — Open-source AI-beelddetector en metadata-opschoner",
    "page.home.description": (
        "Controleer met picai, een gratis open-source detector, of een afbeelding door AI is "
        "gegenereerd. Gebruik hem in de browser of draai hem zelf met Docker of Python."
    ),
    "page.home.h1": "Is deze foto echt? Krijg de score en het bewijs.",
    "page.faq.title": "Veelgestelde vragen over de AI-beelddetector: nauwkeurigheid, privacy, formaten, modellen",
    "page.faq.description": (
        "Antwoorden op veelgestelde vragen over picai: hoe nauwkeurig AI-beelddetectie is, waar "
        "je afbeelding wordt verwerkt, ondersteunde formaten, modellen wisselen en snelheidslimieten."
    ),
    "page.faq.h1": "Veelgestelde vragen over picai",
    "page.faq.intro_suffix": (
        "Dit zijn de vragen die mensen het vaakst stellen over hoe het werkt, hoe nauwkeurig het "
        "is en wat er met geüploade afbeeldingen gebeurt."
    ),
    "page.faq.still_unsure_html": (
        'Nog steeds twijfels? Open een issue op <a href="https://github.com/Micorlov/picai/issues" '
        'rel="noopener">GitHub</a>.'
    ),
    "home.entity_sentence": (
        "picai is een gratis, open-source tool die AI-gegenereerde afbeeldingen beoordeelt en "
        "verborgen metadata verwijdert — gehost of zelf gehost, jij kiest."
    ),
    "home.lead": (
        "picai draait een open AI-detectiemodel en leest elk EXIF-, C2PA- en IPTC-veld dat een "
        "foto bevat — en levert je vervolgens een schone kopie waaruit dat alles is verwijderd. "
        "Geen registratie, geen zwarte doos."
    ),
    "home.dropzone_note": "JPEG, PNG, WebP, HEIC · tot 50 MB · verwerkt in het geheugen, nooit naar schijf geschreven",
    "home.summary": (
        "picai is een gratis, open-source tool die AI-gegenereerde afbeeldingen beoordeelt en "
        "verborgen metadata verwijdert — gehost of zelf gehost, jij kiest. Het schat met een open "
        "Hugging Face-classifier hoe waarschijnlijk het is dat een afbeelding door een "
        "AI-generator is gemaakt, en kan afbeeldingen opnieuw opbouwen om EXIF-, XMP-, IPTC-, "
        "ICC- en C2PA-metadata te verwijderen. Gebruik de gehoste instantie of host zelf met "
        "Docker of Python."
    ),
    "home.stat.0": "open model,<br>geen API van derden",
    "home.stat.1": "registraties<br>vereist",
    "home.stat.2": "MB max.<br>per upload",
    "steps.detect.upload.name": "Uploaden.",
    "steps.detect.detect.name": "Detecteren.",
    "steps.detect.decide.name": "Beslissen.",
    "steps.detect.upload.text": (
        "Sleep, plak of kies een afbeelding. Deze wordt verzonden naar de picai-server die je "
        "gebruikt (je eigen machine bij self-hosting), in het geheugen bewaard en nooit naar "
        "schijf geschreven."
    ),
    "steps.detect.detect.text": (
        "Een open-source beeldclassifier schat hoe waarschijnlijk het is dat de pixels door een "
        "generator zijn geproduceerd."
    ),
    "steps.detect.decide.text": (
        "Je krijgt een AI-waarschijnlijkheid, een betrouwbaarheidsmarge en de metadatablokken die "
        "het bestand bevat — als kans, geen oordeel."
    ),
    "steps.scrub.inspect.name": "Inspecteren.",
    "steps.scrub.scrub.name": "Opschonen.",
    "steps.scrub.verify.name": "Verifiëren.",
    "steps.scrub.inspect.text": (
        "Voer <code>picai inspect photo.jpg</code> uit om de EXIF-, XMP-, IPTC-, C2PA- en "
        "ICC-blokken van het bestand op te sommen."
    ),
    "steps.scrub.scrub.text": (
        "Voer <code>picai scrub photo.jpg</code> uit (of <code>POST /scrub</code>). picai "
        "decodeert de pixels, past de EXIF-oriëntatie toe en bouwt een gloednieuwe afbeelding op "
        "uit de ruwe pixelbuffer."
    ),
    "steps.scrub.verify.text": (
        "Voer <code>picai inspect photo.clean.jpg</code> uit; dit zou “no metadata signatures found” moeten tonen."
    ),
    "faq.accuracy.question": "Hoe nauwkeurig is de detector?",
    "faq.leaves_computer.question": "Verlaat mijn afbeelding mijn computer?",
    "faq.open_source.question": "Is het open source?",
    "faq.remove_metadata.question": "Kan ik C2PA en andere metadata verwijderen?",
    "faq.formats.question": "Welke formaten worden ondersteund?",
    "faq.why_metadata.question": "Waarom wordt metadata weergegeven?",
    "faq.different_model.question": "Kan ik een ander model gebruiken?",
    "faq.free.question": "Is picai gratis?",
    "faq.screenshots.question": "Werkt het op screenshots of zwaar gecomprimeerde afbeeldingen?",
    "faq.which_generator.question": (
        "Kan het zien welke generator een afbeelding heeft gemaakt (Midjourney, DALL·E, Stable "
        "Diffusion)?"
    ),
    "faq.false_positive.question": "Waarom kreeg een echte foto een AI-score?",
    "faq.offline.question": "Kan ik het offline gebruiken?",
    "faq.rate_limit.question": "Is er een snelheidslimiet op de gehoste instantie?",
    "faq.accuracy.answer_html": (
        "Het geeft een waarschijnlijkheid, geen oordeel. Scores rond de 50% krijgen het label "
        "<em>Onzeker</em>; behandel elk afzonderlijk resultaat als een aanwijzing en combineer het "
        'met ander bewijs. Lees meer over <a href="/how-accurate">hoe nauwkeurig '
        "AI-beelddetectoren zijn</a>."
    ),
    "faq.leaves_computer.answer_html": (
        "Op deze publieke instantie: ja — de afbeelding wordt geüpload naar de picai-server (een "
        "Google Cloud Run-container die door de auteur wordt beheerd), in het geheugen beoordeeld "
        "en nooit naar schijf geschreven. De opgeschoonde kopie blijft alleen in het geheugen "
        "totdat 100 nieuwere resultaten hem vervangen of de container opnieuw start, en er wordt "
        'niets naar een externe API gestuurd. Als je wilt dat niets je machine verlaat, <a '
        'href="/self-host">draai picai dan zelf</a> met één Docker-commando. Details staan op de '
        '<a href="/privacy">privacypagina</a>.'
    ),
    "faq.open_source.answer_html": (
        "Ja. De code, de Docker-image, de CLI en de GitHub Action staan allemaal in de "
        '<a href="https://github.com/Micorlov/picai" rel="noopener">picai-repository</a> onder de '
        "MIT-licentie. De detector is een open Hugging Face-model dat je kunt inspecteren of "
        "vervangen."
    ),
    "faq.remove_metadata.answer_html": (
        "Ja. Gebruik na het controleren van een afbeelding <em>Download schone kopie</em>. picai "
        "bouwt de afbeelding opnieuw op uit de pixels, zodat EXIF, XMP, IPTC, C2PA en het "
        'ICC-profiel allemaal achterblijven. <a href="/remove-image-metadata">Zo werkt de '
        "opschoner</a>."
    ),
    "faq.formats.answer_html": (
        "JPEG, PNG, WebP, HEIC/HEIF en de meeste formaten die Pillow kan decoderen, tot 50 MB."
    ),
    "faq.why_metadata.answer_html": (
        "C2PA-inhoudsreferenties en tags van bewerkingssoftware zijn aanwijzingen over herkomst. "
        "Het paneel toont welke blokken (EXIF, XMP, IPTC, C2PA, ICC) het bestand bevat, zodat je "
        'ze samen met de score kunt afwegen. Zie <a href="/c2pa">C2PA-inhoudsreferenties</a> en '
        '<a href="/remove-image-metadata">hoe je metadata van een afbeelding verwijdert</a>.'
    ),
    "faq.different_model.answer_html": (
        "Ja. Stel <code>PICAI_DETECTOR_MODEL</code> in op elk Hugging Face-beeldclassificatiemodel "
        "waarvan de labels AI/nep tegenover mens/echt benoemen."
    ),
    "faq.free.answer_html": (
        "Ja. picai is open source onder de MIT-licentie. De gehoste instantie is gratis te "
        "gebruiken met een limiet van 10 analyses per IP-adres per 24 uur; een zelf gehoste kopie "
        "heeft geen limiet."
    ),
    "faq.screenshots.answer_html": (
        "Het werkt, maar hercoderen, formaat wijzigen en screenshots verwijderen een deel van de "
        "sporen op pixelniveau waarop de classifier vertrouwt, dus verwacht een lagere "
        "betrouwbaarheid en meer <em>Onzeker</em>-resultaten."
    ),
    "faq.which_generator.answer_html": (
        "Nee. picai beoordeelt in het algemeen gegenereerde versus echte pixelstatistieken; het "
        "identificeert de generator niet en heeft geen kennis van generators die zijn uitgebracht "
        "nadat de trainingsdata van zijn model zijn verzameld."
    ),
    "faq.false_positive.answer_html": (
        "Zware filters, HDR-bewerking, opschalen, illustraties en 3D-renders delen statistische "
        "kenmerken met gegenereerde afbeeldingen. De score is een waarschijnlijkheid, geen bewijs; "
        "valse positieven komen voor."
    ),
    "faq.offline.answer_html": (
        "Ja. Nadat de eerste run het model naar de Hugging Face-cache heeft gedownload, heeft een "
        "zelf gehoste picai geen netwerktoegang meer nodig."
    ),
    "faq.rate_limit.answer_html": (
        "Ja: 10 analyses per client-IP binnen elk voortschrijdend venster van 24 uur. Antwoorden "
        "bevatten <code>X-RateLimit-Remaining</code>, en een verzoek boven de limiet geeft 429 "
        "terug met een <code>Retry-After</code>-header."
    ),
    "nav.detector": "Detector",
    "nav.how_it_works": "Hoe het werkt",
    "nav.how-to-tell-if-an-image-is-ai-generated": "Gids",
    "nav.api": "API",
    "nav.self-host": "Zelf hosten",
    "footer.remove-image-metadata": "Metadata verwijderen",
    "footer.c2pa": "C2PA",
    "footer.faq": "FAQ",
    "footer.privacy": "Privacy",
    "footer.self-host": "Zelf hosten",
    "footer.about": "Over",
    "ui.nav_aria_label": "Hoofdnavigatie",
    "ui.loading_status": "Detector wordt geladen…",
    "ui.hero_overline": "— Open-source AI-beeldforensisch onderzoek",
    "ui.hero_heading_line1": "Is deze foto echt?",
    "ui.hero_heading_line2": "Krijg de score en het bewijs.",
    "ui.tool_aria_label": "AI-beelddetector",
    "ui.dropzone_aria_label": "Upload een afbeelding om te analyseren",
    "ui.dropzone_title_fine": "Sleep een foto hierheen",
    "ui.dropzone_title_coarse": "Controleer een foto",
    "ui.dropzone_sub_fine": "of plak vanaf het klembord, of",
    "ui.dropzone_sub_coarse": "vanuit je bibliotheek of camera",
    "ui.btn_check_image_fine": "Controleer deze afbeelding",
    "ui.btn_choose_photo_coarse": "Kies foto",
    "ui.btn_take_photo": "Maak een foto",
    "ui.dismiss_aria_label": "Sluiten",
    "ui.analyzing_prefix": "Analyseren",
    "ui.analyzing_suffix": "· pixels · metadatablokken",
    "ui.verdict_overline": "— Oordeel",
    "ui.meter_real": "Echt",
    "ui.meter_uncertain": "Onzeker",
    "ui.meter_ai": "AI",
    "ui.model_label": "Model",
    "ui.verdict_disclaimer_html": (
        "Resultaten zijn waarschijnlijkheden van een classifier, geen oordelen. "
        '<a href="/how-accurate">Hoe je de score leest.</a>'
    ),
    "ui.btn_check_another": "Controleer nog een afbeelding",
    "ui.preview_overline": "— Voorbeeld",
    "ui.preview_alt": "Voorbeeld van de geüploade afbeelding",
    "ui.metadata_overline": "— Metadata",
    "ui.metadata_heading": "Gevonden in het bestand.",
    "ui.jpeg_segments_label": "JPEG-segmenten",
    "ui.btn_download_clean": "Download de schone kopie",
    "ui.metadata_scrub_note_html": (
        "Opnieuw opgebouwd uit de pixels, dus elk bovenstaand blok is verdwenen. "
        '<a href="/remove-image-metadata">Zo werkt het</a>'
    ),
    "ui.how_it_works_overline": "— Hoe het werkt",
    "ui.how_it_works_heading": "Drie stappen. Niets wordt bewaard.",
    "ui.how_it_works_links_html": (
        '<a href="/how-to-tell-if-an-image-is-ai-generated">Lees de gids om AI-afbeeldingen te '
        'herkennen</a> of <a href="/self-host">draai het op je eigen machine</a>.'
    ),
    "ui.faq_overline": "— FAQ",
    "ui.faq_heading": "Voordat je het vraagt.",
    "ui.faq_more_link": "Meer vragen en antwoorden →",
    "ui.footer_tagline": "picai. · open source",
    "ui.footer_detector_label": "Detector:",
    "ui.breadcrumb_aria_label": "Broodkruimelpad",
    "ui.last_updated_prefix": "Laatst bijgewerkt",
    "ui.source_on_github": "broncode op GitHub",
    "ui.btn_try_detector": "Probeer de detector",
    "ui.status_ready": "Detector gereed",
    "ui.status_unreachable": "Server onbereikbaar",
    "ui.loading_model_note": "Detectiemodel wordt geladen (eerste keer wordt ~750 MB gedownload)…",
    "ui.error_empty_file": "Dit bestand is leeg.",
    "ui.error_file_too_large": "{name} is {size} — de limiet is 50 MB.",
    "ui.error_server_unreachable": "Kon de server niet bereiken: {message}",
    "ui.verdict_ai": "Waarschijnlijk AI-gegenereerd",
    "ui.verdict_real": "Waarschijnlijk een echte foto",
    "ui.verdict_uncertain": "Onzeker",
    "ui.confidence_suffix": "betrouwbaarheid",
    "ui.format_unknown": "onbekend",
    "ui.metadata_present": "Aanwezig",
    "ui.metadata_not_present": "Niet aanwezig",
    "ui.no_jpeg_segments": "Geen JPEG APP-segmenten",
    "ui.quota_remaining": "{remaining} van {limit} analyses vandaag nog over",
}
