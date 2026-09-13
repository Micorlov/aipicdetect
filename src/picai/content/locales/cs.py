"""Czech translation table.

Falls back to English (see :func:`picai.content.locales.t`) for any key not defined here, but
every key from :mod:`picai.content.locales.en` is translated below.
"""

from __future__ import annotations

STRINGS: dict[str, str] = {
    # Page metadata
    "page.home.title": "picai — open-source detektor AI obrázků a nástroj na čištění metadat",
    "page.home.description": (
        "Zjistěte, zda je obrázek vygenerovaný AI, pomocí picai — bezplatného open-source "
        "detektoru. Použijte ho v prohlížeči, nebo si ho spusťte na vlastním počítači přes Docker "
        "či Python."
    ),
    "page.home.h1": "Je tahle fotka opravdová? Zjistěte skóre a důkaz.",
    "page.faq.title": "Časté dotazy o detektoru AI obrázků: přesnost, soukromí, formáty, modely",
    "page.faq.description": (
        "Odpovědi na časté otázky o picai: jak přesná je detekce AI obrázků, kde se vaše fotka "
        "zpracovává, jaké formáty jsou podporované, jak vyměnit model a jaké platí limity "
        "požadavků."
    ),
    "page.faq.h1": "Nejčastější dotazy o picai",
    "page.faq.intro_suffix": (
        "To jsou otázky, které lidé kladou nejčastěji: jak to funguje, jak přesné to je a co se "
        "stane s nahranými obrázky."
    ),
    "page.faq.still_unsure_html": (
        'Pořád si nejste jistí? Založte issue na <a href="https://github.com/Micorlov/picai/issues" '
        'rel="noopener">GitHubu</a>.'
    ),
    # Home page copy
    "home.entity_sentence": (
        "picai je bezplatný open-source nástroj, který hodnotí, zda je obrázek vygenerovaný AI, a "
        "odstraňuje skrytá metadata — hostovaně, nebo self-hosted, výběr je na vás."
    ),
    "home.lead": (
        "picai spouští otevřený model pro detekci AI a čte každé pole EXIF, C2PA a IPTC, které "
        "fotka nese — a pak vám vrátí čistou kopii se vším odstraněným. Bez registrace, bez černé "
        "skříňky."
    ),
    "home.dropzone_note": (
        "JPEG, PNG, WebP, HEIC · do 50 MB · zpracováno v paměti, nikdy neuloženo na disk"
    ),
    "home.summary": (
        "picai je bezplatný open-source nástroj, který hodnotí, zda je obrázek vygenerovaný AI, a "
        "odstraňuje skrytá metadata — hostovaně, nebo self-hosted, výběr je na vás. Hodnotí "
        "pravděpodobnost, že obrázek vytvořil generátor AI, pomocí otevřeného klasifikátoru "
        "Hugging Face, a dokáže obrázek znovu vykreslit, aby odstranil metadata EXIF, XMP, IPTC, "
        "ICC a C2PA. Použijte hostovanou instanci, nebo si picai nainstalujte sami přes Docker či "
        "Python."
    ),
    "home.stat.0": "otevřený model,<br>žádné API třetích stran",
    "home.stat.1": "registrací<br>vyžadováno",
    "home.stat.2": "MB<br>limit nahrávání",
    # Detect steps
    "steps.detect.upload.name": "Nahrajte.",
    "steps.detect.upload.text": (
        "Přetáhněte, vložte nebo vyberte obrázek. Odešle se na server picai, který používáte (na "
        "váš vlastní počítač v případě self-hosted verze), uchová se v paměti a nikdy se neuloží "
        "na disk."
    ),
    "steps.detect.detect.name": "Detekujte.",
    "steps.detect.detect.text": (
        "Open-source klasifikátor obrázků odhaduje pravděpodobnost, že pixely vytvořil generátor."
    ),
    "steps.detect.decide.name": "Rozhodněte.",
    "steps.detect.decide.text": (
        "Získáte pravděpodobnost AI, pásmo jistoty a bloky metadat, které soubor obsahuje — jako "
        "pravděpodobnost, ne jako verdikt."
    ),
    # Scrub steps — <code> blocks contain literal shell commands and must stay untranslated
    "steps.scrub.inspect.name": "Zkontrolujte.",
    "steps.scrub.inspect.text": (
        "Spusťte <code>picai inspect photo.jpg</code> a zobrazte si seznam bloků EXIF, XMP, IPTC, "
        "C2PA a ICC, které soubor obsahuje."
    ),
    "steps.scrub.scrub.name": "Vyčistěte.",
    "steps.scrub.scrub.text": (
        "Spusťte <code>picai scrub photo.jpg</code> (nebo <code>POST /scrub</code>). picai dekóduje "
        "pixely, použije orientaci EXIF a sestaví úplně nový obrázek ze surového bufferu pixelů."
    ),
    "steps.scrub.verify.name": "Ověřte.",
    "steps.scrub.verify.text": (
        "Spusťte <code>picai inspect photo.clean.jpg</code>; mělo by se vypsat „no metadata "
        "signatures found“."
    ),
    # FAQ (home slugs)
    "faq.accuracy.question": "Jak přesný je detektor?",
    "faq.accuracy.answer_html": (
        "Uvádí pravděpodobnost, ne verdikt. Skóre blízké 50 % je označeno jako <em>Nejisté</em>; "
        "každý jednotlivý výsledek berte jako signál a kombinujte ho s dalšími důkazy. Více se "
        'dozvíte na stránce <a href="/how-accurate">o přesnosti detektorů AI obrázků</a>.'
    ),
    "faq.leaves_computer.question": "Opouští moje fotka můj počítač?",
    "faq.leaves_computer.answer_html": (
        "Na této veřejné instanci ano: obrázek se nahraje na server picai (kontejner Google Cloud "
        "Run provozovaný autorem), vyhodnotí se v paměti a nikdy se neuloží na disk. Vyčištěná "
        "kopie zůstává v paměti jen do doby, než ji nahradí 100 novějších výsledků nebo se "
        "kontejner restartuje, a nic se neposílá žádnému externímu API. Pokud chcete, aby nic "
        'neopustilo váš počítač, <a href="/self-host">spusťte si picai sami</a> jedním příkazem '
        'Dockeru. Podrobnosti najdete na <a href="/privacy">stránce o soukromí</a>.'
    ),
    "faq.open_source.question": "Je to open source?",
    "faq.open_source.answer_html": (
        "Ano. Kód, Docker image, CLI i GitHub Action jsou k dispozici v "
        '<a href="https://github.com/Micorlov/picai" rel="noopener">repozitáři picai</a> pod '
        "licencí MIT. Detektor je otevřený model Hugging Face, který si můžete prohlédnout nebo "
        "nahradit."
    ),
    "faq.remove_metadata.question": "Můžu odstranit C2PA a další metadata?",
    "faq.remove_metadata.answer_html": (
        "Ano. Po kontrole obrázku použijte <em>Stáhnout čistou kopii</em>. picai obrázek znovu "
        "sestaví z jeho pixelů, takže EXIF, XMP, IPTC, C2PA i profil ICC zůstanou úplně stranou. "
        '<a href="/remove-image-metadata">Jak čištění funguje</a>.'
    ),
    "faq.formats.question": "Jaké formáty jsou podporované?",
    "faq.formats.answer_html": (
        "JPEG, PNG, WebP, HEIC/HEIF a většina formátů, které umí dekódovat Pillow, do velikosti "
        "50 MB."
    ),
    "faq.why_metadata.question": "Proč se zobrazují metadata?",
    "faq.why_metadata.answer_html": (
        "Obsahové certifikáty C2PA a značky editačního softwaru jsou náznaky původu souboru. Panel "
        "ukazuje, které bloky (EXIF, XMP, IPTC, C2PA, ICC) soubor obsahuje, abyste je mohli zvážit "
        'spolu se skóre. Viz <a href="/c2pa">obsahové certifikáty C2PA</a> a '
        '<a href="/remove-image-metadata">jak odstranit metadata obrázku</a>.'
    ),
    "faq.different_model.question": "Můžu použít jiný model?",
    "faq.different_model.answer_html": (
        "Ano. Nastavte <code>PICAI_DETECTOR_MODEL</code> na libovolný model klasifikace obrázků z "
        "Hugging Face, jehož štítky rozlišují obsah AI/falešný oproti lidský/skutečný."
    ),
    # FAQ (more slugs)
    "faq.free.question": "Je picai zdarma?",
    "faq.free.answer_html": (
        "Ano. picai je open source pod licencí MIT. Hostovaná instance je zdarma, s limitem 10 "
        "analýz na IP adresu za 24 hodin; self-hosted kopie žádný limit nemá."
    ),
    "faq.screenshots.question": "Funguje na screenshotech nebo silně komprimovaných obrázcích?",
    "faq.screenshots.answer_html": (
        "Funguje to, ale opětovné kódování, změna velikosti a snímky obrazovky odstraňují část "
        "stop na úrovni pixelů, na kterých klasifikátor staví, takže očekávejte nižší jistotu a "
        "více výsledků <em>Nejisté</em>."
    ),
    "faq.which_generator.question": (
        "Pozná, který generátor obrázek vytvořil (Midjourney, DALL·E, Stable Diffusion)?"
    ),
    "faq.which_generator.answer_html": (
        "Ne. picai obecně vyhodnocuje statistiky pixelů typu vygenerováno versus skutečné; "
        "neidentifikuje konkrétní generátor a nemá žádné znalosti o generátorech vydaných po sběru "
        "trénovacích dat jeho modelu."
    ),
    "faq.false_positive.question": "Proč bylo skutečné foto vyhodnoceno jako AI?",
    "faq.false_positive.answer_html": (
        "Silné filtry, zpracování HDR, zvětšování rozlišení (upscaling), ilustrace a 3D rendery "
        "sdílejí statistické rysy s vygenerovanými obrázky. Skóre je pravděpodobnost, ne důkaz; "
        "falešně pozitivní výsledky se stávají."
    ),
    "faq.offline.question": "Můžu to spustit offline?",
    "faq.offline.answer_html": (
        "Ano. Poté, co první spuštění stáhne model do mezipaměti Hugging Face, self-hosted picai "
        "už nepotřebuje přístup k síti."
    ),
    "faq.rate_limit.question": "Má hostovaná instance limit požadavků?",
    "faq.rate_limit.answer_html": (
        "Ano: 10 analýz na klientskou IP adresu v jakémkoli klouzavém 24hodinovém okně. Odpovědi "
        "obsahují hlavičku <code>X-RateLimit-Remaining</code> a požadavek nad limit vrátí 429 s "
        "hlavičkou <code>Retry-After</code>."
    ),
    # Navigation
    "nav.detector": "Detektor",
    "nav.how_it_works": "Jak to funguje",
    "nav.how-to-tell-if-an-image-is-ai-generated": "Návod",
    "nav.api": "API",
    "nav.self-host": "Self-hosting",
    # Footer
    "footer.remove-image-metadata": "Odstranění metadat",
    "footer.c2pa": "C2PA",
    "footer.faq": "FAQ",
    "footer.privacy": "Soukromí",
    "footer.self-host": "Self-hosting",
    "footer.about": "O projektu",
    # UI strings
    "ui.nav_aria_label": "Hlavní navigace",
    "ui.loading_status": "Načítání detektoru…",
    "ui.hero_overline": "— Open-source forenzní analýza AI obrázků",
    "ui.hero_heading_line1": "Je tahle fotka opravdová?",
    "ui.hero_heading_line2": "Zjistěte skóre a důkaz.",
    "ui.tool_aria_label": "Detektor AI obrázků",
    "ui.dropzone_aria_label": "Nahrajte obrázek k analýze",
    "ui.dropzone_title_fine": "Přetáhněte sem fotku",
    "ui.dropzone_title_coarse": "Zkontrolujte fotku",
    "ui.dropzone_sub_fine": "nebo vložte ze schránky, nebo",
    "ui.dropzone_sub_coarse": "z galerie nebo fotoaparátu",
    "ui.btn_check_image_fine": "Zkontrolovat tento obrázek",
    "ui.btn_choose_photo_coarse": "Vybrat fotku",
    "ui.btn_take_photo": "Vyfotit",
    "ui.dismiss_aria_label": "Zavřít",
    "ui.analyzing_prefix": "Analyzuji",
    "ui.analyzing_suffix": "· pixely · bloky metadat",
    "ui.verdict_overline": "— Verdikt",
    "ui.meter_real": "Reálné",
    "ui.meter_uncertain": "Nejisté",
    "ui.meter_ai": "AI",
    "ui.model_label": "Model",
    "ui.verdict_disclaimer_html": (
        "Výsledky jsou pravděpodobnosti od klasifikátoru, ne verdikty. "
        '<a href="/how-accurate">Jak číst skóre.</a>'
    ),
    "ui.btn_check_another": "Zkontrolovat jiný obrázek",
    "ui.preview_overline": "— Náhled",
    "ui.preview_alt": "Náhled nahraného obrázku",
    "ui.metadata_overline": "— Metadata",
    "ui.metadata_heading": "Nalezeno v souboru.",
    "ui.jpeg_segments_label": "Segmenty JPEG",
    "ui.btn_download_clean": "Stáhnout čistou kopii",
    "ui.metadata_scrub_note_html": (
        "Znovu vykresleno z pixelů, takže každý z výše uvedených bloků zmizel. "
        '<a href="/remove-image-metadata">Jak to funguje</a>'
    ),
    "ui.how_it_works_overline": "— Jak to funguje",
    "ui.how_it_works_heading": "Tři kroky. Nic se neukládá.",
    "ui.how_it_works_links_html": (
        '<a href="/how-to-tell-if-an-image-is-ai-generated">Přečtěte si návod, jak poznat AI '
        'obrázky</a>, nebo <a href="/self-host">si ho spusťte na vlastním počítači</a>.'
    ),
    "ui.faq_overline": "— FAQ",
    "ui.faq_heading": "Než se zeptáte.",
    "ui.faq_more_link": "Další otázky a odpovědi →",
    "ui.footer_tagline": "picai. · open source",
    "ui.footer_detector_label": "Detektor:",
    "ui.breadcrumb_aria_label": "Drobečková navigace",
    "ui.last_updated_prefix": "Naposledy aktualizováno",
    "ui.source_on_github": "zdrojový kód na GitHubu",
    "ui.btn_try_detector": "Vyzkoušet detektor",
    "ui.status_ready": "Detektor připraven",
    "ui.status_unreachable": "Server nedostupný",
    "ui.loading_model_note": "Načítání modelu detektoru (první spuštění stáhne ~750 MB)…",
    "ui.error_empty_file": "Tento soubor je prázdný.",
    "ui.error_file_too_large": "{name} má velikost {size} — limit je 50 MB.",
    "ui.error_server_unreachable": "Nepodařilo se spojit se serverem: {message}",
    "ui.verdict_ai": "Pravděpodobně vygenerováno AI",
    "ui.verdict_real": "Pravděpodobně skutečná fotka",
    "ui.verdict_uncertain": "Nejisté",
    "ui.confidence_suffix": "jistoty",
    "ui.format_unknown": "neznámý",
    "ui.metadata_present": "Přítomno",
    "ui.metadata_not_present": "Nepřítomno",
    "ui.no_jpeg_segments": "Žádné segmenty JPEG APP",
    "ui.quota_remaining": "Zbývá {remaining} z {limit} analýz na dnešek",
}
