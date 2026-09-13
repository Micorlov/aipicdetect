"""German translation table."""

from __future__ import annotations

STRINGS: dict[str, str] = {
    "page.home.title": "AiPicDetect — Open-Source-KI-Bilderkennung & Metadaten-Bereiniger",
    "page.home.description": (
        "Prüfen Sie mit AiPicDetect, einem kostenlosen Open-Source-Detektor, ob ein Bild KI-generiert ist. "
        "Nutzen Sie ihn im Browser oder betreiben Sie ihn selbst mit Docker oder Python."
    ),
    "page.home.h1": "Ist dieses Foto echt? Sie erhalten den Score und den Beleg.",
    "page.faq.title": "FAQ zur KI-Bilderkennung: Genauigkeit, Datenschutz, Formate, Modelle",
    "page.faq.description": (
        "Antworten auf häufige Fragen zu AiPicDetect: wie genau die KI-Bilderkennung ist, wo Ihr Bild "
        "verarbeitet wird, welche Formate unterstützt werden, Modellwechsel und Ratenbegrenzungen."
    ),
    "page.faq.h1": "Häufig gestellte Fragen zu AiPicDetect",
    "page.faq.intro_suffix": (
        "Das sind die Fragen, die am häufigsten gestellt werden: wie es funktioniert, wie genau es "
        "ist und was mit hochgeladenen Bildern passiert."
    ),
    "page.faq.still_unsure_html": (
        'Noch unsicher? Erstelle ein Issue auf <a href="https://github.com/Micorlov/aipicdetect/issues" '
        'rel="noopener">GitHub</a>.'
    ),
    # ── Guide page meta ─────────────────────────────────────────────────────────────────────
    "page.how-to-tell-if-an-image-is-ai-generated.title": 'Wie erkenne ich, ob ein Bild KI-generiert ist? (Leitfaden 2026)',
    "page.how-to-tell-if-an-image-is-ai-generated.description": (
        'Praxischeckliste zur Erkennung KI-generierter Bilder: visuelle Hinweise, C2PA- und EXIF-Metadaten, umgekehrte Bildersuche und Auswertung des Detektorwerts.'
    ),
    "page.how-to-tell-if-an-image-is-ai-generated.h1": 'Wie erkenne ich, ob ein Bild KI-generiert ist?',
    "page.how-accurate.title": 'Wie genau sind KI-Bilddetektoren? Den AiPicDetect-Score verstehen',
    "page.how-accurate.description": (
        'KI-Bilddetektoren liefern Wahrscheinlichkeiten, keine Beweise. Wie AiPicDetect Klassifikatorwerte in Prozent und Konfidenzband umrechnet und wo Detektoren versagen.'
    ),
    "page.how-accurate.h1": 'Wie genau ist ein KI-Bilddetektor?',
    "page.remove-image-metadata.title": 'EXIF-, XMP-, IPTC- und C2PA-Metadaten aus Bildern entfernen',
    "page.remove-image-metadata.description": (
        'Entfernen Sie EXIF, XMP, IPTC, ICC und C2PA Content Credentials aus JPEG-, PNG-, WebP- und HEIC-Dateien durch Neurendern der Pixel mit der kostenlosen AiPicDetect-CLI.'
    ),
    "page.remove-image-metadata.h1": 'Alle Metadaten aus einem Bild entfernen',
    "home.entity_sentence": (
        "AiPicDetect ist ein kostenloses Open-Source-Tool, das KI-generierte Bilder bewertet und versteckte "
        "Metadaten entfernt — gehostet oder selbst gehostet, Sie haben die Wahl."
    ),
    "home.lead": (
        "AiPicDetect führt ein offenes KI-Erkennungsmodell aus und liest jedes EXIF-, C2PA- und "
        "IPTC-Feld, das ein Foto enthält — und liefert Ihnen anschließend eine saubere Kopie, aus "
        "der alles entfernt wurde. Keine Registrierung, keine Blackbox."
    ),
    "home.dropzone_note": "JPEG, PNG, WebP, HEIC · bis zu 50 MB · im Speicher verarbeitet, nie auf die Festplatte geschrieben",
    "home.summary": (
        "AiPicDetect ist ein kostenloses Open-Source-Tool, das KI-generierte Bilder bewertet und versteckte "
        "Metadaten entfernt — gehostet oder selbst gehostet, Sie haben die Wahl. Es bewertet mit "
        "einem offenen Hugging-Face-Klassifikator die Wahrscheinlichkeit, dass ein Bild von einem "
        "KI-Generator erzeugt wurde, und kann Bilder neu rendern, um EXIF-, XMP-, IPTC-, ICC- und "
        "C2PA-Metadaten zu entfernen. Nutzen Sie die gehostete Instanz oder hosten Sie selbst mit "
        "Docker oder Python."
    ),
    "home.stat.0": "offenes Modell,<br>keine Drittanbieter-API",
    "home.stat.1": "Anmeldungen<br>erforderlich",
    "home.stat.2": "MB max.<br>Upload",
    "steps.detect.upload.name": "Hochladen.",
    "steps.detect.detect.name": "Erkennen.",
    "steps.detect.decide.name": "Entscheiden.",
    "steps.detect.upload.text": (
        "Ziehen, einfügen oder ein Bild auswählen. Es wird an den AiPicDetect-Server gesendet, den Sie "
        "verwenden (bei Selbsthosting Ihre eigene Maschine), im Speicher gehalten und nie auf die "
        "Festplatte geschrieben."
    ),
    "steps.detect.detect.text": (
        "Ein Open-Source-Bildklassifikator bewertet die Wahrscheinlichkeit, dass die Pixel von einem "
        "Generator erzeugt wurden."
    ),
    "steps.detect.decide.text": (
        "Sie erhalten eine KI-Wahrscheinlichkeit, eine Konfidenzspanne und die Metadatenblöcke, die "
        "die Datei enthält — als Wahrscheinlichkeit, nicht als Urteil."
    ),
    "steps.scrub.inspect.name": "Prüfen.",
    "steps.scrub.scrub.name": "Bereinigen.",
    "steps.scrub.verify.name": "Verifizieren.",
    "steps.scrub.inspect.text": (
        "Führen Sie <code>aipicdetect inspect photo.jpg</code> aus, um die EXIF-, XMP-, IPTC-, C2PA- und "
        "ICC-Blöcke der Datei aufzulisten."
    ),
    "steps.scrub.scrub.text": (
        "Führen Sie <code>aipicdetect scrub photo.jpg</code> aus (oder <code>POST /scrub</code>). AiPicDetect "
        "dekodiert die Pixel, wendet die EXIF-Ausrichtung an und baut aus dem rohen Pixelpuffer ein "
        "brandneues Bild."
    ),
    "steps.scrub.verify.text": (
        "Führen Sie <code>aipicdetect inspect photo.clean.jpg</code> aus; es sollte „no metadata signatures found“ ausgeben."
    ),
    "faq.accuracy.question": "Wie genau ist der Detektor?",
    "faq.leaves_computer.question": "Verlässt mein Bild meinen Computer?",
    "faq.open_source.question": "Ist es Open Source?",
    "faq.remove_metadata.question": "Kann ich C2PA und andere Metadaten entfernen?",
    "faq.formats.question": "Welche Formate werden unterstützt?",
    "faq.why_metadata.question": "Warum werden Metadaten aufgelistet?",
    "faq.different_model.question": "Kann ich ein anderes Modell verwenden?",
    "faq.free.question": "Ist AiPicDetect kostenlos?",
    "faq.screenshots.question": "Funktioniert es bei Screenshots oder stark komprimierten Bildern?",
    "faq.which_generator.question": (
        "Kann es erkennen, welcher Generator ein Bild erzeugt hat (Midjourney, DALL·E, Stable "
        "Diffusion)?"
    ),
    "faq.false_positive.question": "Warum wurde ein echtes Foto als KI bewertet?",
    "faq.offline.question": "Kann ich es offline nutzen?",
    "faq.rate_limit.question": "Gibt es eine Ratenbegrenzung auf der gehosteten Instanz?",
    "faq.accuracy.answer_html": (
        "Er gibt eine Wahrscheinlichkeit an, kein Urteil. Werte nahe 50 % werden als "
        "<em>Unsicher</em> gekennzeichnet; behandeln Sie ein einzelnes Ergebnis als Hinweis und "
        'kombinieren Sie es mit anderen Belegen. Mehr dazu unter <a href="/how-accurate">wie genau '
        "KI-Bilderkennung ist</a>."
    ),
    "faq.leaves_computer.answer_html": (
        "Auf dieser öffentlichen Instanz: ja — das Bild wird an den AiPicDetect-Server (einen vom Autor "
        "betriebenen Google-Cloud-Run-Container) hochgeladen, im Speicher bewertet und nie auf die "
        "Festplatte geschrieben. Die bereinigte Kopie bleibt nur so lange im Speicher, bis 100 "
        "neuere Ergebnisse sie ersetzen oder der Container neu startet, und nichts wird an eine "
        "Drittanbieter-API gesendet. Wenn nichts Ihre Maschine verlassen soll, "
        '<a href="/self-host">betreiben Sie AiPicDetect selbst</a> mit einem einzigen Docker-Befehl. '
        'Details finden Sie auf der <a href="/privacy">Datenschutzseite</a>.'
    ),
    "faq.open_source.answer_html": (
        "Ja. Der Code, das Docker-Image, die CLI und die GitHub Action befinden sich alle im "
        '<a href="https://github.com/Micorlov/aipicdetect" rel="noopener">AiPicDetect-Repository</a> unter der '
        "MIT-Lizenz. Der Detektor ist ein offenes Hugging-Face-Modell, das Sie prüfen oder ersetzen "
        "können."
    ),
    "faq.remove_metadata.answer_html": (
        "Ja. Verwenden Sie nach dem Prüfen eines Bildes <em>Saubere Kopie herunterladen</em>. AiPicDetect "
        "baut das Bild aus seinen Pixeln neu auf, sodass EXIF, XMP, IPTC, C2PA und das ICC-Profil "
        'alle zurückbleiben. <a href="/remove-image-metadata">So funktioniert der Bereiniger</a>.'
    ),
    "faq.formats.answer_html": (
        "JPEG, PNG, WebP, HEIC/HEIF und die meisten Formate, die Pillow dekodieren kann, bis zu "
        "50 MB."
    ),
    "faq.why_metadata.answer_html": (
        "C2PA-Content-Credentials und Tags von Bearbeitungssoftware sind Herkunftshinweise. Das "
        "Panel zeigt, welche Blöcke (EXIF, XMP, IPTC, C2PA, ICC) die Datei enthält, damit Sie sie "
        'gegen den Score abwägen können. Siehe <a href="/c2pa">C2PA-Content-Credentials</a> und '
        '<a href="/remove-image-metadata">wie man Bildmetadaten entfernt</a>.'
    ),
    "faq.different_model.answer_html": (
        "Ja. Setzen Sie <code>PICAI_DETECTOR_MODEL</code> auf ein beliebiges "
        "Hugging-Face-Bildklassifikationsmodell, dessen Labels KI/gefälscht gegenüber "
        "menschlich/echt benennen."
    ),
    "faq.free.answer_html": (
        "Ja. AiPicDetect ist Open Source unter der MIT-Lizenz. Die gehostete Instanz ist kostenlos nutzbar "
        "mit einem Limit von 10 Analysen pro IP-Adresse alle 24 Stunden; eine selbst gehostete Kopie "
        "hat kein Limit."
    ),
    "faq.screenshots.answer_html": (
        "Es funktioniert, aber Neukodierung, Größenänderung und Screenshots entfernen einen Teil der "
        "Spuren auf Pixelebene, auf die sich der Klassifikator stützt — erwarten Sie daher geringere "
        "Konfidenz und mehr <em>Unsicher</em>-Ergebnisse."
    ),
    "faq.which_generator.answer_html": (
        "Nein. AiPicDetect bewertet generell generierte gegenüber echten Pixelstatistiken; es identifiziert "
        "den Generator nicht und hat keine Kenntnis von Generatoren, die nach der Erhebung der "
        "Trainingsdaten seines Modells veröffentlicht wurden."
    ),
    "faq.false_positive.answer_html": (
        "Starke Filter, HDR-Verarbeitung, Hochskalierung, Illustrationen und 3D-Renderings teilen "
        "statistische Merkmale mit generierten Bildern. Der Score ist eine Wahrscheinlichkeit, kein "
        "Beweis; falsch positive Ergebnisse kommen vor."
    ),
    "faq.offline.answer_html": (
        "Ja. Nachdem der erste Lauf das Modell in den Hugging-Face-Cache heruntergeladen hat, "
        "benötigt ein selbst gehostetes AiPicDetect keinen Netzwerkzugriff mehr."
    ),
    "faq.rate_limit.answer_html": (
        "Ja: 10 Analysen pro Client-IP in jedem gleitenden 24-Stunden-Fenster. Antworten enthalten "
        "<code>X-RateLimit-Remaining</code>, und eine Anfrage über dem Limit liefert 429 mit einem "
        "<code>Retry-After</code>-Header."
    ),
    "nav.detector": "Detektor",
    "nav.how_it_works": "So funktioniert's",
    "nav.how-to-tell-if-an-image-is-ai-generated": "Leitfaden",
    "nav.api": "API",
    "nav.self-host": "Selbst hosten",
    "footer.remove-image-metadata": "Metadaten entfernen",
    "footer.c2pa": "C2PA",
    "footer.faq": "FAQ",
    "footer.privacy": "Datenschutz",
    "footer.self-host": "Selbst hosten",
    "footer.about": "Über",
    "ui.nav_aria_label": "Hauptnavigation",
    "ui.loading_status": "Detektor wird geladen…",
    "ui.hero_overline": "— Open-Source-KI-Bildforensik",
    "ui.hero_heading_line1": "Ist dieses Foto echt?",
    "ui.hero_heading_line2": "Sie erhalten den Score und den Beleg.",
    "ui.tool_aria_label": "KI-Bilderkennung",
    "ui.dropzone_aria_label": "Ein Bild zur Analyse hochladen",
    "ui.dropzone_title_fine": "Foto per Drag & Drop ablegen",
    "ui.dropzone_title_coarse": "Foto prüfen",
    "ui.dropzone_sub_fine": "oder aus der Zwischenablage einfügen, oder",
    "ui.dropzone_sub_coarse": "aus Ihrer Mediathek oder der Kamera",
    "ui.btn_check_image_fine": "Dieses Bild prüfen",
    "ui.btn_choose_photo_coarse": "Foto auswählen",
    "ui.btn_take_photo": "Foto aufnehmen",
    "ui.dismiss_aria_label": "Schließen",
    "ui.analyzing_prefix": "Analysiere",
    "ui.analyzing_suffix": "· Pixel · Metadatenblöcke",
    "ui.verdict_overline": "— Ergebnis",
    "ui.meter_real": "Echt",
    "ui.meter_uncertain": "Unsicher",
    "ui.meter_ai": "KI",
    "ui.model_label": "Modell",
    "ui.verdict_disclaimer_html": (
        "Die Ergebnisse sind Wahrscheinlichkeiten eines Klassifikators, keine Urteile. "
        '<a href="/how-accurate">So lesen Sie den Score.</a>'
    ),
    "ui.btn_check_another": "Weiteres Bild prüfen",
    "ui.preview_overline": "— Vorschau",
    "ui.preview_alt": "Vorschau des hochgeladenen Bildes",
    "ui.metadata_overline": "— Metadaten",
    "ui.metadata_heading": "In der Datei gefunden.",
    "ui.jpeg_segments_label": "JPEG-Segmente",
    "ui.btn_download_clean": "Saubere Kopie herunterladen",
    "ui.metadata_scrub_note_html": (
        "Aus den Pixeln neu gerendert, sodass jeder Block oben entfernt wurde. "
        '<a href="/remove-image-metadata">So funktioniert es</a>'
    ),
    "ui.how_it_works_overline": "— So funktioniert's",
    "ui.how_it_works_heading": "Drei Schritte. Nichts wird gespeichert.",
    "ui.how_it_works_links_html": (
        '<a href="/how-to-tell-if-an-image-is-ai-generated">Lesen Sie den Leitfaden zum Erkennen von '
        'KI-Bildern</a> oder <a href="/self-host">betreiben Sie es auf Ihrer eigenen Maschine</a>.'
    ),
    "ui.faq_overline": "— FAQ",
    "ui.faq_heading": "Bevor Sie fragen.",
    "ui.faq_more_link": "Weitere Fragen und Antworten →",
    "ui.footer_tagline": "AiPicDetect. · open source",
    "ui.footer_detector_label": "Detektor:",
    "ui.breadcrumb_aria_label": "Brotkrümelnavigation",
    "ui.last_updated_prefix": "Zuletzt aktualisiert",
    "ui.source_on_github": "Quellcode auf GitHub",
    "ui.btn_try_detector": "Detektor ausprobieren",
    "ui.status_ready": "Detektor bereit",
    "ui.status_unreachable": "Server nicht erreichbar",
    "ui.loading_model_note": "Detektormodell wird geladen (erster Start lädt ~750 MB herunter)…",
    "ui.error_empty_file": "Diese Datei ist leer.",
    "ui.error_file_too_large": "{name} ist {size} groß — das Limit liegt bei 50 MB.",
    "ui.error_server_unreachable": "Server konnte nicht erreicht werden: {message}",
    "ui.verdict_ai": "Wahrscheinlich KI-generiert",
    "ui.verdict_real": "Wahrscheinlich ein echtes Foto",
    "ui.verdict_uncertain": "Unsicher",
    "ui.confidence_suffix": "Konfidenz",
    "ui.format_unknown": "unbekannt",
    "ui.metadata_present": "Vorhanden",
    "ui.metadata_not_present": "Nicht vorhanden",
    "ui.no_jpeg_segments": "Keine JPEG-APP-Segmente",
    "ui.quota_remaining": "{remaining} von {limit} Analysen heute übrig",
}
