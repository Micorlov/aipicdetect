"""Danish translation table."""

from __future__ import annotations

STRINGS: dict[str, str] = {
    "page.home.title": "picai — AI-billeddetektor og metadata-renser med åben kildekode",
    "page.home.description": (
        "Tjek om et billede er AI-genereret med picai, en gratis open source-detektor. Brug den "
        "i browseren, eller kør den selv med Docker eller Python."
    ),
    "page.home.h1": "Er dette foto ægte? Få scoren og beviset.",
    "page.faq.title": "Ofte stillede spørgsmål om AI-billeddetektoren: nøjagtighed, privatliv, formater, modeller",
    "page.faq.description": (
        "Svar på almindelige spørgsmål om picai: hvor nøjagtig AI-billeddetektion er, hvor dit "
        "billede behandles, understøttede formater, modelskift og hastighedsgrænser."
    ),
    "page.faq.h1": "Ofte stillede spørgsmål om picai",
    "page.faq.intro_suffix": (
        "Det er de spørgsmål, folk oftest stiller om, hvordan det virker, hvor nøjagtigt det er, "
        "og hvad der sker med billeder, der uploades."
    ),
    "page.faq.still_unsure_html": (
        'Stadig i tvivl? Opret et issue på <a href="https://github.com/Micorlov/picai/issues" '
        'rel="noopener">GitHub</a>.'
    ),
    "home.entity_sentence": (
        "picai er et gratis værktøj med åben kildekode, der vurderer AI-genererede billeder og "
        "fjerner skjult metadata — hostet eller selv-hostet, du vælger."
    ),
    "home.lead": (
        "picai kører en åben AI-detektionsmodel og læser hvert EXIF-, C2PA- og IPTC-felt et foto "
        "indeholder — og giver dig derefter en ren kopi, hvor det hele er fjernet. Ingen "
        "tilmelding, ingen sort boks."
    ),
    "home.dropzone_note": "JPEG, PNG, WebP, HEIC · op til 50 MB · behandlet i hukommelsen, aldrig skrevet til disk",
    "home.summary": (
        "picai er et gratis værktøj med åben kildekode, der vurderer AI-genererede billeder og "
        "fjerner skjult metadata — hostet eller selv-hostet, du vælger. Det vurderer "
        "sandsynligheden for, at et billede er skabt af en AI-generator, ved hjælp af en åben "
        "Hugging Face-klassifikator, og kan gen-rendere billeder for at fjerne EXIF-, XMP-, "
        "IPTC-, ICC- og C2PA-metadata. Brug den hostede instans, eller vær selv-hostet med Docker "
        "eller Python."
    ),
    "home.stat.0": "åben model,<br>ingen tredjeparts-API",
    "home.stat.1": "tilmeldinger<br>krævet",
    "home.stat.2": "MB maks.<br>pr. upload",
    "steps.detect.upload.name": "Upload.",
    "steps.detect.detect.name": "Detektér.",
    "steps.detect.decide.name": "Afgør.",
    "steps.detect.upload.text": (
        "Træk, indsæt eller vælg et billede. Det sendes til den picai-server, du bruger (din egen "
        "maskine ved selv-hosting), holdes i hukommelsen og skrives aldrig til disk."
    ),
    "steps.detect.detect.text": (
        "En billedklassifikator med åben kildekode vurderer sandsynligheden for, at pixlerne er "
        "produceret af en generator."
    ),
    "steps.detect.decide.text": (
        "Du får en AI-sandsynlighed, et konfidensinterval og de metadatablokke, filen indeholder "
        "— som en sandsynlighed, ikke en dom."
    ),
    "steps.scrub.inspect.name": "Undersøg.",
    "steps.scrub.scrub.name": "Rens.",
    "steps.scrub.verify.name": "Verificér.",
    "steps.scrub.inspect.text": (
        "Kør <code>picai inspect photo.jpg</code> for at liste de EXIF-, XMP-, IPTC-, C2PA- og "
        "ICC-blokke, filen indeholder."
    ),
    "steps.scrub.scrub.text": (
        "Kør <code>picai scrub photo.jpg</code> (eller <code>POST /scrub</code>). picai afkoder "
        "pixlerne, anvender EXIF-orienteringen og bygger et helt nyt billede ud fra den rå "
        "pixelbuffer."
    ),
    "steps.scrub.verify.text": (
        "Kør <code>picai inspect photo.clean.jpg</code>; det bør vise »no metadata signatures found«."
    ),
    "faq.accuracy.question": "Hvor nøjagtig er detektoren?",
    "faq.leaves_computer.question": "Forlader mit billede min computer?",
    "faq.open_source.question": "Er det open source?",
    "faq.remove_metadata.question": "Kan jeg fjerne C2PA og anden metadata?",
    "faq.formats.question": "Hvilke formater understøttes?",
    "faq.why_metadata.question": "Hvorfor vises metadata?",
    "faq.different_model.question": "Kan jeg bruge en anden model?",
    "faq.free.question": "Er picai gratis?",
    "faq.screenshots.question": "Virker det på skærmbilleder eller stærkt komprimerede billeder?",
    "faq.which_generator.question": (
        "Kan den se, hvilken generator der har lavet et billede (Midjourney, DALL·E, Stable "
        "Diffusion)?"
    ),
    "faq.false_positive.question": "Hvorfor fik et rigtigt foto en AI-score?",
    "faq.offline.question": "Kan jeg køre den offline?",
    "faq.rate_limit.question": "Er der en hastighedsgrænse på den hostede instans?",
    "faq.accuracy.answer_html": (
        "Den angiver en sandsynlighed, ikke en dom. Scorer tæt på 50 % mærkes <em>Usikker</em>; "
        "betragt ethvert enkeltresultat som et signal, og kombinér det med andre beviser. Læs "
        'mere om <a href="/how-accurate">hvor nøjagtige AI-billeddetektorer er</a>.'
    ),
    "faq.leaves_computer.answer_html": (
        "På denne offentlige instans: ja — billedet uploades til picai-serveren (en Google Cloud "
        "Run-container drevet af forfatteren), vurderes i hukommelsen og skrives aldrig til disk. "
        "Den rensede kopi ligger kun i hukommelsen, indtil 100 nyere resultater erstatter den, "
        "eller containeren genstarter, og intet sendes til en tredjeparts-API. Hvis du ikke vil "
        'have, at noget forlader din maskine, så <a href="/self-host">kør picai selv</a> med én '
        'Docker-kommando. Detaljerne findes på <a href="/privacy">privatlivssiden</a>.'
    ),
    "faq.open_source.answer_html": (
        "Ja. Koden, Docker-imaget, CLI-værktøjet og GitHub Action findes alle i "
        '<a href="https://github.com/Micorlov/picai" rel="noopener">picai-repositoriet</a> under '
        "MIT-licensen. Detektoren er en åben Hugging Face-model, som du kan inspicere eller "
        "udskifte."
    ),
    "faq.remove_metadata.answer_html": (
        "Ja. Efter at have tjekket et billede skal du bruge <em>Download ren kopi</em>. picai "
        "genopbygger billedet ud fra dets pixels, så EXIF, XMP, IPTC, C2PA og ICC-profilen alle "
        'efterlades. <a href="/remove-image-metadata">Sådan fungerer renseren</a>.'
    ),
    "faq.formats.answer_html": (
        "JPEG, PNG, WebP, HEIC/HEIF og de fleste formater, Pillow kan afkode, op til 50 MB."
    ),
    "faq.why_metadata.answer_html": (
        "C2PA-indholdslegitimationer og tags fra redigeringssoftware er spor om oprindelse. "
        "Panelet viser, hvilke blokke (EXIF, XMP, IPTC, C2PA, ICC) filen indeholder, så du kan "
        'afveje dem mod scoren. Se <a href="/c2pa">C2PA-indholdslegitimationer</a> og '
        '<a href="/remove-image-metadata">hvordan man fjerner billedmetadata</a>.'
    ),
    "faq.different_model.answer_html": (
        "Ja. Sæt <code>PICAI_DETECTOR_MODEL</code> til en hvilken som helst "
        "Hugging Face-billedklassifikationsmodel, hvis labels navngiver AI/falsk over for "
        "menneske/ægte."
    ),
    "faq.free.answer_html": (
        "Ja. picai er open source under MIT-licensen. Den hostede instans er gratis at bruge med "
        "en grænse på 10 analyser pr. IP-adresse hver 24. time; en selv-hostet kopi har ingen "
        "grænse."
    ),
    "faq.screenshots.answer_html": (
        "Det virker, men genkodning, ændring af størrelse og skærmbilleder fjerner nogle af de "
        "spor på pixelniveau, som klassifikatoren er afhængig af, så forvent lavere konfidens og "
        "flere <em>Usikker</em>-resultater."
    ),
    "faq.which_generator.answer_html": (
        "Nej. picai vurderer generelt genereret kontra ægte pixelstatistik; den identificerer "
        "ikke generatoren og har ingen viden om generatorer, der er udgivet, efter modellens "
        "træningsdata blev indsamlet."
    ),
    "faq.false_positive.answer_html": (
        "Kraftige filtre, HDR-behandling, opskalering, illustrationer og 3D-renderinger deler "
        "statistiske træk med genererede billeder. Scoren er en sandsynlighed, ikke et bevis; "
        "falske positiver forekommer."
    ),
    "faq.offline.answer_html": (
        "Ja. Når den første kørsel har downloadet modellen til Hugging Face-cachen, har en "
        "selv-hostet picai ikke brug for netværksadgang."
    ),
    "faq.rate_limit.answer_html": (
        "Ja: 10 analyser pr. klient-IP inden for et hvilket som helst glidende 24-timers vindue. "
        "Svarene bærer <code>X-RateLimit-Remaining</code>, og en forespørgsel over grænsen "
        "returnerer 429 med en <code>Retry-After</code>-header."
    ),
    "nav.detector": "Detektor",
    "nav.how_it_works": "Sådan virker det",
    "nav.how-to-tell-if-an-image-is-ai-generated": "Guide",
    "nav.api": "API",
    "nav.self-host": "Selv-hosting",
    "footer.remove-image-metadata": "Fjern metadata",
    "footer.c2pa": "C2PA",
    "footer.faq": "FAQ",
    "footer.privacy": "Privatliv",
    "footer.self-host": "Selv-hosting",
    "footer.about": "Om",
    "ui.nav_aria_label": "Hovednavigation",
    "ui.loading_status": "Indlæser detektor…",
    "ui.hero_overline": "— AI-billedforensik med åben kildekode",
    "ui.hero_heading_line1": "Er dette foto ægte?",
    "ui.hero_heading_line2": "Få scoren og beviset.",
    "ui.tool_aria_label": "AI-billeddetektor",
    "ui.dropzone_aria_label": "Upload et billede til analyse",
    "ui.dropzone_title_fine": "Træk og slip et foto",
    "ui.dropzone_title_coarse": "Tjek et foto",
    "ui.dropzone_sub_fine": "eller indsæt fra udklipsholderen, eller",
    "ui.dropzone_sub_coarse": "fra dit bibliotek eller kamera",
    "ui.btn_check_image_fine": "Tjek dette billede",
    "ui.btn_choose_photo_coarse": "Vælg foto",
    "ui.btn_take_photo": "Tag et foto",
    "ui.dismiss_aria_label": "Luk",
    "ui.analyzing_prefix": "Analyserer",
    "ui.analyzing_suffix": "· pixels · metadatablokke",
    "ui.verdict_overline": "— Dom",
    "ui.meter_real": "Ægte",
    "ui.meter_uncertain": "Usikker",
    "ui.meter_ai": "AI",
    "ui.model_label": "Model",
    "ui.verdict_disclaimer_html": (
        "Resultaterne er sandsynligheder fra en klassifikator, ikke domme. "
        '<a href="/how-accurate">Sådan læser du scoren.</a>'
    ),
    "ui.btn_check_another": "Tjek et andet billede",
    "ui.preview_overline": "— Forhåndsvisning",
    "ui.preview_alt": "Forhåndsvisning af det uploadede billede",
    "ui.metadata_overline": "— Metadata",
    "ui.metadata_heading": "Fundet i filen.",
    "ui.jpeg_segments_label": "JPEG-segmenter",
    "ui.btn_download_clean": "Download den rene kopi",
    "ui.metadata_scrub_note_html": (
        "Gen-renderet ud fra pixels, så hver blok ovenfor er væk. "
        '<a href="/remove-image-metadata">Sådan virker det</a>'
    ),
    "ui.how_it_works_overline": "— Sådan virker det",
    "ui.how_it_works_heading": "Tre trin. Intet gemmes.",
    "ui.how_it_works_links_html": (
        '<a href="/how-to-tell-if-an-image-is-ai-generated">Læs guiden til at spotte '
        'AI-billeder</a> eller <a href="/self-host">kør det på din egen maskine</a>.'
    ),
    "ui.faq_overline": "— FAQ",
    "ui.faq_heading": "Før du spørger.",
    "ui.faq_more_link": "Flere spørgsmål og svar →",
    "ui.footer_tagline": "picai. · open source",
    "ui.footer_detector_label": "Detektor:",
    "ui.breadcrumb_aria_label": "Brødkrumme-navigation",
    "ui.last_updated_prefix": "Sidst opdateret",
    "ui.source_on_github": "kildekode på GitHub",
    "ui.btn_try_detector": "Prøv detektoren",
    "ui.status_ready": "Detektor klar",
    "ui.status_unreachable": "Server ikke tilgængelig",
    "ui.loading_model_note": "Indlæser detektionsmodel (første kørsel downloader ~750 MB)…",
    "ui.error_empty_file": "Denne fil er tom.",
    "ui.error_file_too_large": "{name} er {size} — grænsen er 50 MB.",
    "ui.error_server_unreachable": "Kunne ikke få forbindelse til serveren: {message}",
    "ui.verdict_ai": "Sandsynligvis AI-genereret",
    "ui.verdict_real": "Sandsynligvis et ægte foto",
    "ui.verdict_uncertain": "Usikker",
    "ui.confidence_suffix": "sikkerhed",
    "ui.format_unknown": "ukendt",
    "ui.metadata_present": "Til stede",
    "ui.metadata_not_present": "Ikke til stede",
    "ui.no_jpeg_segments": "Ingen JPEG APP-segmenter",
    "ui.quota_remaining": "{remaining} af {limit} analyser tilbage i dag",
}
