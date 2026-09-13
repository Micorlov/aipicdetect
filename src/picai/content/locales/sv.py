"""Swedish translation table."""

from __future__ import annotations

STRINGS: dict[str, str] = {
    "page.home.title": "picai — Öppen källkods-AI-bilddetektor och metadatarensare",
    "page.home.description": (
        "Kontrollera om en bild är AI-genererad med picai, en gratis detektor med öppen källkod. "
        "Använd den i webbläsaren eller kör den själv med Docker eller Python."
    ),
    "page.home.h1": "Är det här fotot äkta? Få poängen och beviset.",
    "page.faq.title": "Vanliga frågor om AI-bilddetektorn: noggrannhet, integritet, format, modeller",
    "page.faq.description": (
        "Svar på vanliga frågor om picai: hur noggrann AI-bilddetektering är, var din bild "
        "bearbetas, format som stöds, byte av modell och hastighetsgränser."
    ),
    "page.faq.h1": "Vanliga frågor om picai",
    "page.faq.intro_suffix": (
        "Det här är de vanligaste frågorna om hur det fungerar, hur noggrant det är och vad som "
        "händer med bilder som laddas upp."
    ),
    "page.faq.still_unsure_html": (
        'Fortfarande osäker? Öppna ett ärende på <a href="https://github.com/Micorlov/picai/issues" '
        'rel="noopener">GitHub</a>.'
    ),
    "home.entity_sentence": (
        "picai är ett gratis verktyg med öppen källkod som bedömer AI-genererade bilder och tar "
        "bort dold metadata — värdbaserat eller självhostat, du väljer."
    ),
    "home.lead": (
        "picai kör en öppen AI-detekteringsmodell och läser varje EXIF-, C2PA- och IPTC-fält ett "
        "foto bär på — och ger dig sedan en ren kopia där allt detta är borttaget. Ingen "
        "registrering, ingen svart låda."
    ),
    "home.dropzone_note": "JPEG, PNG, WebP, HEIC · upp till 50 MB · bearbetas i minnet, skrivs aldrig till disk",
    "home.summary": (
        "picai är ett gratis verktyg med öppen källkod som bedömer AI-genererade bilder och tar "
        "bort dold metadata — värdbaserat eller självhostat, du väljer. Det bedömer hur sannolikt "
        "det är att en bild skapats av en AI-generator med hjälp av en öppen "
        "Hugging Face-klassificerare, och kan rendera om bilder för att ta bort EXIF-, XMP-, "
        "IPTC-, ICC- och C2PA-metadata. Använd den värdbaserade instansen eller självhosta med "
        "Docker eller Python."
    ),
    "home.stat.0": "öppen modell,<br>ingen tredjeparts-API",
    "home.stat.1": "registreringar<br>krävs",
    "home.stat.2": "MB max<br>per uppladdning",
    "steps.detect.upload.name": "Ladda upp.",
    "steps.detect.detect.name": "Upptäck.",
    "steps.detect.decide.name": "Bedöm.",
    "steps.detect.upload.text": (
        "Släpp, klistra in eller välj en bild. Den skickas till picai-servern du använder (din "
        "egen maskin vid självhostning), hålls i minnet och skrivs aldrig till disk."
    ),
    "steps.detect.detect.text": (
        "En bildklassificerare med öppen källkod bedömer sannolikheten för att pixlarna "
        "producerats av en generator."
    ),
    "steps.detect.decide.text": (
        "Du får en AI-sannolikhet, ett konfidensintervall och de metadatablock som filen bär på "
        "— som sannolikhet, inte som dom."
    ),
    "steps.scrub.inspect.name": "Inspektera.",
    "steps.scrub.scrub.name": "Rensa.",
    "steps.scrub.verify.name": "Verifiera.",
    "steps.scrub.inspect.text": (
        "Kör <code>picai inspect photo.jpg</code> för att lista de EXIF-, XMP-, IPTC-, C2PA- och "
        "ICC-block filen bär på."
    ),
    "steps.scrub.scrub.text": (
        "Kör <code>picai scrub photo.jpg</code> (eller <code>POST /scrub</code>). picai avkodar "
        "pixlarna, tillämpar EXIF-orienteringen och bygger en helt ny bild från den råa "
        "pixelbufferten."
    ),
    "steps.scrub.verify.text": (
        "Kör <code>picai inspect photo.clean.jpg</code>; det bör visa ”no metadata signatures found”."
    ),
    "faq.accuracy.question": "Hur noggrann är detektorn?",
    "faq.leaves_computer.question": "Lämnar min bild min dator?",
    "faq.open_source.question": "Är det öppen källkod?",
    "faq.remove_metadata.question": "Kan jag ta bort C2PA och annan metadata?",
    "faq.formats.question": "Vilka format stöds?",
    "faq.why_metadata.question": "Varför listas metadata?",
    "faq.different_model.question": "Kan jag använda en annan modell?",
    "faq.free.question": "Är picai gratis?",
    "faq.screenshots.question": "Fungerar det på skärmdumpar eller kraftigt komprimerade bilder?",
    "faq.which_generator.question": (
        "Kan den avgöra vilken generator som skapat en bild (Midjourney, DALL·E, Stable "
        "Diffusion)?"
    ),
    "faq.false_positive.question": "Varför fick ett riktigt foto en AI-poäng?",
    "faq.offline.question": "Kan jag köra den offline?",
    "faq.rate_limit.question": "Finns det en hastighetsgräns på den värdbaserade instansen?",
    "faq.accuracy.answer_html": (
        "Den anger en sannolikhet, inte en dom. Poäng nära 50 % märks <em>Osäker</em>; behandla "
        "varje enskilt resultat som en signal och kombinera det med andra bevis. Läs mer om "
        '<a href="/how-accurate">hur noggranna AI-bilddetektorer är</a>.'
    ),
    "faq.leaves_computer.answer_html": (
        "På den här offentliga instansen: ja — bilden laddas upp till picai-servern (en Google "
        "Cloud Run-container som drivs av författaren), bedöms i minnet och skrivs aldrig till "
        "disk. Den rensade kopian finns kvar i minnet bara tills 100 nyare resultat ersätter den "
        "eller containern startar om, och inget skickas till något tredjeparts-API. Om du vill "
        'att inget ska lämna din maskin, <a href="/self-host">kör picai själv</a> med ett enda '
        'Docker-kommando. Detaljer finns på <a href="/privacy">sidan om integritet</a>.'
    ),
    "faq.open_source.answer_html": (
        "Ja. Koden, Docker-avbildningen, CLI:t och GitHub Action finns alla i "
        '<a href="https://github.com/Micorlov/picai" rel="noopener">picai-repot</a> under '
        "MIT-licensen. Detektorn är en öppen Hugging Face-modell som du kan granska eller byta ut."
    ),
    "faq.remove_metadata.answer_html": (
        "Ja. Efter att du kontrollerat en bild, använd <em>Ladda ner ren kopia</em>. picai bygger "
        "om bilden från dess pixlar, så EXIF, XMP, IPTC, C2PA och ICC-profilen lämnas alla kvar. "
        '<a href="/remove-image-metadata">Så fungerar rensaren</a>.'
    ),
    "faq.formats.answer_html": (
        "JPEG, PNG, WebP, HEIC/HEIF och de flesta format Pillow kan avkoda, upp till 50 MB."
    ),
    "faq.why_metadata.answer_html": (
        "C2PA-innehållsuppgifter och taggar från redigeringsprogram är ledtrådar om ursprung. "
        "Panelen visar vilka block (EXIF, XMP, IPTC, C2PA, ICC) filen bär på så att du kan väga "
        'dem mot poängen. Se <a href="/c2pa">C2PA-innehållsuppgifter</a> och '
        '<a href="/remove-image-metadata">hur du tar bort bildmetadata</a>.'
    ),
    "faq.different_model.answer_html": (
        "Ja. Ställ in <code>PICAI_DETECTOR_MODEL</code> till valfri "
        "Hugging Face-bildklassificeringsmodell vars etiketter namnger AI/falskt kontra "
        "mänskligt/äkta."
    ),
    "faq.free.answer_html": (
        "Ja. picai är öppen källkod under MIT-licensen. Den värdbaserade instansen är gratis att "
        "använda med en gräns på 10 analyser per IP-adress var 24:e timme; en självhostad kopia "
        "har ingen gräns."
    ),
    "faq.screenshots.answer_html": (
        "Den fungerar, men omkodning, storleksändring och skärmdumpar tar bort en del av de spår "
        "på pixelnivå som klassificeraren förlitar sig på, så förvänta dig lägre konfidens och "
        "fler <em>Osäker</em>-resultat."
    ),
    "faq.which_generator.answer_html": (
        "Nej. picai bedömer generellt genererad kontra äkta pixelstatistik; den identifierar inte "
        "generatorn och har ingen kännedom om generatorer som släpptes efter att dess modells "
        "träningsdata samlades in."
    ),
    "faq.false_positive.answer_html": (
        "Kraftiga filter, HDR-bearbetning, uppskalning, illustrationer och 3D-renderingar delar "
        "statistiska egenskaper med genererade bilder. Poängen är en sannolikhet, inte ett bevis; "
        "falska positiva förekommer."
    ),
    "faq.offline.answer_html": (
        "Ja. Efter att den första körningen har laddat ner modellen till Hugging Face-cachen "
        "behöver en självhostad picai ingen nätverksåtkomst."
    ),
    "faq.rate_limit.answer_html": (
        "Ja: 10 analyser per klient-IP under vilket rullande 24-timmarsfönster som helst. Svaren "
        "bär <code>X-RateLimit-Remaining</code>, och en begäran över gränsen returnerar 429 med "
        "en <code>Retry-After</code>-header."
    ),
    "nav.detector": "Detektor",
    "nav.how_it_works": "Så funkar det",
    "nav.how-to-tell-if-an-image-is-ai-generated": "Guide",
    "nav.api": "API",
    "nav.self-host": "Självhostning",
    "footer.remove-image-metadata": "Ta bort metadata",
    "footer.c2pa": "C2PA",
    "footer.faq": "Vanliga frågor",
    "footer.privacy": "Integritet",
    "footer.self-host": "Självhostning",
    "footer.about": "Om",
    "ui.nav_aria_label": "Huvudnavigering",
    "ui.loading_status": "Laddar detektor…",
    "ui.hero_overline": "— AI-bildforensik med öppen källkod",
    "ui.hero_heading_line1": "Är det här fotot äkta?",
    "ui.hero_heading_line2": "Få poängen och beviset.",
    "ui.tool_aria_label": "AI-bilddetektor",
    "ui.dropzone_aria_label": "Ladda upp en bild att analysera",
    "ui.dropzone_title_fine": "Dra och släpp ett foto",
    "ui.dropzone_title_coarse": "Kontrollera ett foto",
    "ui.dropzone_sub_fine": "eller klistra in från urklipp, eller",
    "ui.dropzone_sub_coarse": "från ditt bibliotek eller kameran",
    "ui.btn_check_image_fine": "Kontrollera den här bilden",
    "ui.btn_choose_photo_coarse": "Välj foto",
    "ui.btn_take_photo": "Ta ett foto",
    "ui.dismiss_aria_label": "Stäng",
    "ui.analyzing_prefix": "Analyserar",
    "ui.analyzing_suffix": "· pixlar · metadatablock",
    "ui.verdict_overline": "— Dom",
    "ui.meter_real": "Äkta",
    "ui.meter_uncertain": "Osäker",
    "ui.meter_ai": "AI",
    "ui.model_label": "Modell",
    "ui.verdict_disclaimer_html": (
        "Resultaten är sannolikheter från en klassificerare, inte domar. "
        '<a href="/how-accurate">Så läser du poängen.</a>'
    ),
    "ui.btn_check_another": "Kontrollera en annan bild",
    "ui.preview_overline": "— Förhandsvisning",
    "ui.preview_alt": "Förhandsvisning av den uppladdade bilden",
    "ui.metadata_overline": "— Metadata",
    "ui.metadata_heading": "Hittades i filen.",
    "ui.jpeg_segments_label": "JPEG-segment",
    "ui.btn_download_clean": "Ladda ner den rena kopian",
    "ui.metadata_scrub_note_html": (
        "Omrenderad från pixlarna, så varje block ovan är borta. "
        '<a href="/remove-image-metadata">Så fungerar det</a>'
    ),
    "ui.how_it_works_overline": "— Så funkar det",
    "ui.how_it_works_heading": "Tre steg. Inget sparas.",
    "ui.how_it_works_links_html": (
        '<a href="/how-to-tell-if-an-image-is-ai-generated">Läs guiden för att upptäcka '
        'AI-bilder</a> eller <a href="/self-host">kör det på din egen maskin</a>.'
    ),
    "ui.faq_overline": "— Vanliga frågor",
    "ui.faq_heading": "Innan du frågar.",
    "ui.faq_more_link": "Fler frågor och svar →",
    "ui.footer_tagline": "picai. · öppen källkod",
    "ui.footer_detector_label": "Detektor:",
    "ui.breadcrumb_aria_label": "Brödsmulespår",
    "ui.last_updated_prefix": "Senast uppdaterad",
    "ui.source_on_github": "källkod på GitHub",
    "ui.btn_try_detector": "Prova detektorn",
    "ui.status_ready": "Detektorn redo",
    "ui.status_unreachable": "Servern är inte nåbar",
    "ui.loading_model_note": "Laddar detekteringsmodellen (första körningen laddar ner ~750 MB)…",
    "ui.error_empty_file": "Filen är tom.",
    "ui.error_file_too_large": "{name} är {size} — gränsen är 50 MB.",
    "ui.error_server_unreachable": "Kunde inte nå servern: {message}",
    "ui.verdict_ai": "Troligen AI-genererad",
    "ui.verdict_real": "Troligen ett äkta foto",
    "ui.verdict_uncertain": "Osäker",
    "ui.confidence_suffix": "konfidens",
    "ui.format_unknown": "okänt",
    "ui.metadata_present": "Finns",
    "ui.metadata_not_present": "Finns inte",
    "ui.no_jpeg_segments": "Inga JPEG APP-segment",
    "ui.quota_remaining": "{remaining} av {limit} analyser kvar idag",
}
