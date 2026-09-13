"""Finnish translation table.

Falls back to English (see :func:`picai.content.locales.t`) for any key not defined here, but
every key from :mod:`picai.content.locales.en` is translated below.
"""

from __future__ import annotations

STRINGS: dict[str, str] = {
    # Page metadata
    "page.home.title": "picai — avoimen lähdekoodin tekoälykuvantunnistin ja metatietojen puhdistaja",
    "page.home.description": (
        "Tarkista, onko kuva tekoälyn luoma picai-palvelulla, ilmaisella avoimen lähdekoodin "
        "tunnistimella. Käytä sitä selaimessa tai aja se omalla koneellasi Dockerilla tai "
        "Pythonilla."
    ),
    "page.home.h1": "Onko tämä valokuva aito? Katso pisteet ja todisteet.",
    "page.faq.title": "Tekoälykuvantunnistimen UKK: tarkkuus, yksityisyys, tiedostomuodot, mallit",
    "page.faq.description": (
        "Vastauksia picaita koskeviin yleisiin kysymyksiin: kuinka tarkka tekoälykuvien tunnistus "
        "on, missä kuvasi käsitellään, mitkä tiedostomuodot ovat tuettuja, mallin vaihtaminen ja "
        "pyyntörajat."
    ),
    "page.faq.h1": "picain usein kysytyt kysymykset",
    "page.faq.intro_suffix": (
        "Nämä ovat kysymyksiä, joita kysytään useimmin siitä, miten se toimii, kuinka tarkka se on "
        "ja mitä ladatuille kuville tapahtuu."
    ),
    "page.faq.still_unsure_html": (
        'Vieläkö epäilyttää? Avaa issue osoitteessa <a '
        'href="https://github.com/Micorlov/picai/issues" rel="noopener">GitHub</a>.'
    ),
    # Home page copy
    "home.entity_sentence": (
        "picai on ilmainen, avoimen lähdekoodin työkalu, joka arvioi tekoälyn tuottamia kuvia ja "
        "poistaa piilotetut metatiedot — pilvipalveluna tai omalla palvelimella, valinta on sinun."
    ),
    "home.lead": (
        "picai käyttää avointa tekoälyntunnistusmallia ja lukee jokaisen EXIF-, C2PA- ja "
        "IPTC-kentän, jonka valokuva sisältää — ja antaa sinulle sitten puhtaan kopion, josta "
        "kaikki tämä on poistettu. Ei rekisteröitymistä, ei mustaa laatikkoa."
    ),
    "home.dropzone_note": (
        "JPEG, PNG, WebP, HEIC · enintään 50 MB · käsitellään muistissa, ei koskaan kirjoiteta "
        "levylle"
    ),
    "home.summary": (
        "picai on ilmainen, avoimen lähdekoodin työkalu, joka arvioi tekoälyn tuottamia kuvia ja "
        "poistaa piilotetut metatiedot — pilvipalveluna tai omalla palvelimella, valinta on sinun. "
        "Se arvioi avoimen Hugging Face -luokittimen avulla, kuinka todennäköisesti kuvan on "
        "tuottanut tekoälygeneraattori, ja voi renderöidä kuvat uudelleen poistaakseen EXIF-, "
        "XMP-, IPTC-, ICC- ja C2PA-metatiedot. Käytä pilvipalvelua tai aja picai itse Dockerilla "
        "tai Pythonilla."
    ),
    "home.stat.0": "avoin malli,<br>ei kolmannen osapuolen API:a",
    "home.stat.1": "rekisteröitymistä<br>ei vaadita",
    "home.stat.2": "MB maks.<br>lataus",
    # Detect steps
    "steps.detect.upload.name": "Lataa.",
    "steps.detect.upload.text": (
        "Vedä, liitä tai valitse kuva. Se lähetetään käyttämällesi picai-palvelimelle (omalle "
        "koneellesi, jos ajat sitä itse), pidetään muistissa eikä sitä koskaan kirjoiteta levylle."
    ),
    "steps.detect.detect.name": "Tunnista.",
    "steps.detect.detect.text": (
        "Avoimen lähdekoodin kuvaluokitin arvioi, kuinka todennäköisesti pikselit on tuottanut "
        "generaattori."
    ),
    "steps.detect.decide.name": "Päätä.",
    "steps.detect.decide.text": (
        "Saat tekoälytodennäköisyyden, luottamusvälin ja tiedoston sisältämät metatietolohkot — "
        "todennäköisyytenä, ei tuomiona."
    ),
    # Scrub steps — <code> blocks contain literal shell commands and must stay untranslated
    "steps.scrub.inspect.name": "Tarkasta.",
    "steps.scrub.inspect.text": (
        "Aja <code>picai inspect photo.jpg</code> listataksesi tiedoston sisältämät EXIF-, XMP-, "
        "IPTC-, C2PA- ja ICC-lohkot."
    ),
    "steps.scrub.scrub.name": "Puhdista.",
    "steps.scrub.scrub.text": (
        "Aja <code>picai scrub photo.jpg</code> (tai <code>POST /scrub</code>). picai purkaa "
        "pikselit, soveltaa EXIF-suunnan ja rakentaa raa'asta pikselipuskurista täysin uuden kuvan."
    ),
    "steps.scrub.verify.name": "Varmista.",
    "steps.scrub.verify.text": (
        "Aja <code>picai inspect photo.clean.jpg</code>; sen pitäisi tulostaa ”no metadata signatures found”."
    ),
    # FAQ (home slugs)
    "faq.accuracy.question": "Kuinka tarkka tunnistin on?",
    "faq.accuracy.answer_html": (
        "Se ilmoittaa todennäköisyyden, ei tuomiota. Noin 50 %:n pisteet merkitään "
        "<em>Epävarma</em>-tulokseksi; kohtele mitä tahansa yksittäistä tulosta yhtenä signaalina "
        'ja yhdistä se muihin todisteisiin. Lue lisää siitä, <a href="/how-accurate">kuinka '
        "tarkkoja tekoälykuvantunnistimet ovat</a>."
    ),
    "faq.leaves_computer.question": "Poistuuko kuvani tietokoneeltani?",
    "faq.leaves_computer.answer_html": (
        "Tässä julkisessa palvelussa kyllä: kuva ladataan picai-palvelimelle (tekijän ylläpitämä "
        "Google Cloud Run -kontti), pisteytetään muistissa eikä sitä koskaan kirjoiteta levylle. "
        "Puhdistettu kopio säilyy muistissa vain, kunnes 100 uudempaa tulosta korvaa sen tai "
        "kontti käynnistyy uudelleen, eikä mitään lähetetä kolmannen osapuolen API:lle. Jos et "
        'halua minkään poistuvan koneeltasi, <a href="/self-host">aja picai itse</a> yhdellä '
        'Docker-komennolla. Lisätietoja <a href="/privacy">tietosuojasivulla</a>.'
    ),
    "faq.open_source.question": "Onko se avointa lähdekoodia?",
    "faq.open_source.answer_html": (
        "Kyllä. Koodi, Docker-image, komentorivityökalu ja GitHub Action ovat kaikki "
        '<a href="https://github.com/Micorlov/picai" rel="noopener">picai-repositoriossa</a> '
        "MIT-lisenssin alla. Tunnistin on avoin Hugging Face -malli, jota voit tarkastella tai "
        "korvata."
    ),
    "faq.remove_metadata.question": "Voinko poistaa C2PA:n ja muut metatiedot?",
    "faq.remove_metadata.answer_html": (
        "Kyllä. Kun olet tarkistanut kuvan, käytä <em>Lataa puhdas kopio</em> -toimintoa. picai "
        "rakentaa kuvan uudelleen sen pikseleistä, joten EXIF, XMP, IPTC, C2PA ja ICC-profiili "
        'jäävät kaikki pois. <a href="/remove-image-metadata">Näin puhdistus toimii</a>.'
    ),
    "faq.formats.question": "Mitkä tiedostomuodot ovat tuettuja?",
    "faq.formats.answer_html": (
        "JPEG, PNG, WebP, HEIC/HEIF ja useimmat muodot, jotka Pillow osaa purkaa, aina 50 MB:aan "
        "asti."
    ),
    "faq.why_metadata.question": "Miksi metatiedot näytetään?",
    "faq.why_metadata.answer_html": (
        "C2PA-sisältötunnisteet ja muokkausohjelmistojen tunnisteet ovat vihjeitä alkuperästä. "
        "Paneeli näyttää, mitä lohkoja (EXIF, XMP, IPTC, C2PA, ICC) tiedosto sisältää, jotta voit "
        'punnita niitä yhdessä pisteiden kanssa. Katso <a href="/c2pa">C2PA-sisältötunnisteet</a> '
        'ja <a href="/remove-image-metadata">kuvan metatietojen poistaminen</a>.'
    ),
    "faq.different_model.question": "Voinko käyttää toista mallia?",
    "faq.different_model.answer_html": (
        "Kyllä. Aseta <code>PICAI_DETECTOR_MODEL</code> mihin tahansa Hugging Facen "
        "kuvaluokittelumalliin, jonka tunnisteet nimeävät tekoäly/väärennös- ja ihminen/aito-"
        "sisällön."
    ),
    # FAQ (more slugs)
    "faq.free.question": "Onko picai ilmainen?",
    "faq.free.answer_html": (
        "Kyllä. picai on avointa lähdekoodia MIT-lisenssin alla. Pilvipalvelu on ilmainen käyttää, "
        "ja siinä on 10 analyysin raja IP-osoitetta kohti 24 tunnin välein; itse ylläpidetyssä "
        "kopiossa ei ole rajaa."
    ),
    "faq.screenshots.question": "Toimiiko se kuvakaappauksilla tai voimakkaasti pakatuilla kuvilla?",
    "faq.screenshots.answer_html": (
        "Se toimii, mutta uudelleenkoodaus, koon muuttaminen ja kuvakaappaukset poistavat osan "
        "pikselitason jäljistä, joihin luokitin nojaa, joten odota alhaisempaa luottamusta ja "
        "enemmän <em>Epävarma</em>-tuloksia."
    ),
    "faq.which_generator.question": (
        "Osaako se kertoa, mikä generaattori loi kuvan (Midjourney, DALL·E, Stable Diffusion)?"
    ),
    "faq.which_generator.answer_html": (
        "Ei. picai arvioi yleisesti generoitujen ja aitojen pikselien tilastoja; se ei tunnista "
        "tiettyä generaattoria, eikä sillä ole tietoa generaattoreista, jotka on julkaistu sen "
        "mallin koulutusdatan keräämisen jälkeen."
    ),
    "faq.false_positive.question": "Miksi aito valokuva sai tekoälypisteet?",
    "faq.false_positive.answer_html": (
        "Voimakkaat suodattimet, HDR-käsittely, suurentaminen, kuvitukset ja 3D-renderöinnit "
        "jakavat tilastollisia piirteitä generoitujen kuvien kanssa. Pisteet ovat todennäköisyys, "
        "ei todiste; virheellisiä positiivisia tuloksia esiintyy."
    ),
    "faq.offline.question": "Voinko käyttää sitä ilman verkkoyhteyttä?",
    "faq.offline.answer_html": (
        "Kyllä. Kun ensimmäinen ajokerta on ladannut mallin Hugging Facen välimuistiin, itse "
        "ylläpidetty picai ei tarvitse verkkoyhteyttä."
    ),
    "faq.rate_limit.question": "Onko pilvipalvelussa pyyntörajaa?",
    "faq.rate_limit.answer_html": (
        "Kyllä: 10 analyysiä asiakas-IP:tä kohti missä tahansa liukuvassa 24 tunnin ikkunassa. "
        "Vastaukset sisältävät <code>X-RateLimit-Remaining</code>-otsikon, ja rajan ylittävä "
        "pyyntö palauttaa 429-vastauksen <code>Retry-After</code>-otsikolla."
    ),
    # Navigation
    "nav.detector": "Tunnistin",
    "nav.how_it_works": "Näin se toimii",
    "nav.how-to-tell-if-an-image-is-ai-generated": "Opas",
    "nav.api": "API",
    "nav.self-host": "Oma palvelin",
    # Footer
    "footer.remove-image-metadata": "Poista metatiedot",
    "footer.c2pa": "C2PA",
    "footer.faq": "UKK",
    "footer.privacy": "Tietosuoja",
    "footer.self-host": "Oma palvelin",
    "footer.about": "Tietoa",
    # UI strings
    "ui.nav_aria_label": "Päänavigaatio",
    "ui.loading_status": "Ladataan tunnistinta…",
    "ui.hero_overline": "— Avoimen lähdekoodin tekoälykuvien forensiikka",
    "ui.hero_heading_line1": "Onko tämä valokuva aito?",
    "ui.hero_heading_line2": "Katso pisteet ja todisteet.",
    "ui.tool_aria_label": "Tekoälykuvantunnistin",
    "ui.dropzone_aria_label": "Lataa kuva analysoitavaksi",
    "ui.dropzone_title_fine": "Vedä ja pudota valokuva",
    "ui.dropzone_title_coarse": "Tarkista valokuva",
    "ui.dropzone_sub_fine": "tai liitä leikepöydältä, tai",
    "ui.dropzone_sub_coarse": "kirjastostasi tai kamerasta",
    "ui.btn_check_image_fine": "Tarkista tämä kuva",
    "ui.btn_choose_photo_coarse": "Valitse valokuva",
    "ui.btn_take_photo": "Ota valokuva",
    "ui.dismiss_aria_label": "Sulje",
    "ui.analyzing_prefix": "Analysoidaan",
    "ui.analyzing_suffix": "· pikselit · metatietolohkot",
    "ui.verdict_overline": "— Tulos",
    "ui.meter_real": "Aito",
    "ui.meter_uncertain": "Epävarma",
    "ui.meter_ai": "Tekoäly",
    "ui.model_label": "Malli",
    "ui.verdict_disclaimer_html": (
        "Tulokset ovat luokittimen todennäköisyyksiä, ei tuomioita. "
        '<a href="/how-accurate">Näin luet pisteet.</a>'
    ),
    "ui.btn_check_another": "Tarkista toinen kuva",
    "ui.preview_overline": "— Esikatselu",
    "ui.preview_alt": "Ladatun kuvan esikatselu",
    "ui.metadata_overline": "— Metatiedot",
    "ui.metadata_heading": "Löytyi tiedostosta.",
    "ui.jpeg_segments_label": "JPEG-segmentit",
    "ui.btn_download_clean": "Lataa puhdas kopio",
    "ui.metadata_scrub_note_html": (
        "Renderöity uudelleen pikseleistä, joten jokainen yllä oleva lohko on poistunut. "
        '<a href="/remove-image-metadata">Näin se toimii</a>'
    ),
    "ui.how_it_works_overline": "— Näin se toimii",
    "ui.how_it_works_heading": "Kolme vaihetta. Mitään ei tallenneta.",
    "ui.how_it_works_links_html": (
        '<a href="/how-to-tell-if-an-image-is-ai-generated">Lue opas tekoälykuvien '
        'tunnistamiseen</a> tai <a href="/self-host">aja se omalla koneellasi</a>.'
    ),
    "ui.faq_overline": "— UKK",
    "ui.faq_heading": "Ennen kuin kysyt.",
    "ui.faq_more_link": "Lisää kysymyksiä ja vastauksia →",
    "ui.footer_tagline": "picai. · avoin lähdekoodi",
    "ui.footer_detector_label": "Tunnistin:",
    "ui.breadcrumb_aria_label": "Murupolku",
    "ui.last_updated_prefix": "Viimeksi päivitetty",
    "ui.source_on_github": "lähdekoodi GitHubissa",
    "ui.btn_try_detector": "Kokeile tunnistinta",
    "ui.status_ready": "Tunnistin valmis",
    "ui.status_unreachable": "Palvelinta ei tavoiteta",
    "ui.loading_model_note": "Ladataan tunnistinmallia (ensimmäinen ajokerta lataa ~750 MB)…",
    "ui.error_empty_file": "Tiedosto on tyhjä.",
    "ui.error_file_too_large": "{name} on {size} — raja on 50 MB.",
    "ui.error_server_unreachable": "Palvelinta ei tavoitettu: {message}",
    "ui.verdict_ai": "Todennäköisesti tekoälyn luoma",
    "ui.verdict_real": "Todennäköisesti aito valokuva",
    "ui.verdict_uncertain": "Epävarma",
    "ui.confidence_suffix": "luottamus",
    "ui.format_unknown": "tuntematon",
    "ui.metadata_present": "Läsnä",
    "ui.metadata_not_present": "Ei läsnä",
    "ui.no_jpeg_segments": "Ei JPEG APP -segmenttejä",
    "ui.quota_remaining": "{remaining}/{limit} analyysiä jäljellä tänään",
}
