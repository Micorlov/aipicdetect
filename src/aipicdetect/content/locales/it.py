"""Italian translation table."""

from __future__ import annotations

STRINGS: dict[str, str] = {
    "page.home.title": "AiPicDetect — Rilevatore di immagini IA open source e pulitore di metadati",
    "page.home.description": (
        "Verifica se un'immagine è generata dall'IA con AiPicDetect, un rilevatore gratuito e open "
        "source. Usalo nel browser oppure eseguilo sulla tua macchina con Docker o Python."
    ),
    "page.home.h1": "Questa foto è reale? Ottieni il punteggio e la prova.",
    "page.faq.title": "FAQ sul rilevatore di immagini IA: precisione, privacy, formati, modelli",
    "page.faq.description": (
        "Risposte alle domande più comuni su AiPicDetect: quanto è accurato il rilevamento di immagini "
        "IA, dove viene elaborata la tua immagine, i formati supportati, la sostituzione del "
        "modello e i limiti di frequenza."
    ),
    "page.faq.h1": "Domande frequenti su AiPicDetect",
    "page.faq.intro_suffix": (
        "Ecco le domande più frequenti su come funziona, quanto è accurato e cosa succede alle "
        "immagini caricate."
    ),
    "page.faq.still_unsure_html": (
        'Hai ancora dubbi? Apri una issue su <a href="https://github.com/Micorlov/aipicdetect/issues" '
        'rel="noopener">GitHub</a>.'
    ),
    "home.entity_sentence": (
        "AiPicDetect è uno strumento gratuito e open source che valuta le immagini generate dall'IA e "
        "rimuove i metadati nascosti — ospitato o self-hosted, a tua scelta."
    ),
    "home.lead": (
        "AiPicDetect esegue un modello di rilevamento IA aperto e legge ogni campo EXIF, C2PA e IPTC "
        "presente in una foto — poi ti restituisce una copia pulita, privata di tutto questo. "
        "Nessuna registrazione, nessuna scatola nera."
    ),
    "home.dropzone_note": "JPEG, PNG, WebP, HEIC · fino a 50 MB · elaborato in memoria, mai scritto su disco",
    "home.summary": (
        "AiPicDetect è uno strumento gratuito e open source che valuta le immagini generate dall'IA e "
        "rimuove i metadati nascosti — ospitato o self-hosted, a tua scelta. Valuta la probabilità "
        "che un'immagine sia stata prodotta da un generatore IA usando un classificatore Hugging "
        "Face aperto, e può ricostruire le immagini per rimuovere i metadati EXIF, XMP, IPTC, ICC "
        "e C2PA. Usa l'istanza ospitata oppure fai il self-hosting con Docker o Python."
    ),
    "home.stat.0": "modello aperto,<br>nessuna API di terze parti",
    "home.stat.1": "registrazioni<br>richieste",
    "home.stat.2": "MB max<br>per caricamento",
    "steps.detect.upload.name": "Carica.",
    "steps.detect.detect.name": "Rileva.",
    "steps.detect.decide.name": "Decidi.",
    "steps.detect.upload.text": (
        "Trascina, incolla o scegli un'immagine. Viene inviata al server AiPicDetect che stai usando "
        "(la tua macchina, in caso di self-hosting), mantenuta in memoria e mai scritta su disco."
    ),
    "steps.detect.detect.text": (
        "Un classificatore di immagini open source valuta la probabilità che i pixel siano stati "
        "prodotti da un generatore."
    ),
    "steps.detect.decide.text": (
        "Ottieni una probabilità IA, un margine di confidenza e i blocchi di metadati presenti "
        "nel file — come probabilità, non come verdetto."
    ),
    "steps.scrub.inspect.name": "Ispeziona.",
    "steps.scrub.scrub.name": "Pulisci.",
    "steps.scrub.verify.name": "Verifica.",
    "steps.scrub.inspect.text": (
        "Esegui <code>aipicdetect inspect photo.jpg</code> per elencare i blocchi EXIF, XMP, IPTC, C2PA "
        "e ICC presenti nel file."
    ),
    "steps.scrub.scrub.text": (
        "Esegui <code>aipicdetect scrub photo.jpg</code> (oppure <code>POST /scrub</code>). AiPicDetect "
        "decodifica i pixel, applica l'orientamento EXIF e costruisce un'immagine completamente "
        "nuova a partire dal buffer di pixel grezzi."
    ),
    "steps.scrub.verify.text": (
        "Esegui <code>aipicdetect inspect photo.clean.jpg</code>; dovrebbe restituire «no metadata signatures found»."
    ),
    "faq.accuracy.question": "Quanto è accurato il rilevatore?",
    "faq.leaves_computer.question": "La mia immagine lascia il mio computer?",
    "faq.open_source.question": "È open source?",
    "faq.remove_metadata.question": "Posso rimuovere il C2PA e altri metadati?",
    "faq.formats.question": "Quali formati sono supportati?",
    "faq.why_metadata.question": "Perché i metadati vengono elencati?",
    "faq.different_model.question": "Posso usare un modello diverso?",
    "faq.free.question": "AiPicDetect è gratuito?",
    "faq.screenshots.question": "Funziona con screenshot o immagini molto compresse?",
    "faq.which_generator.question": (
        "Può capire quale generatore ha creato un'immagine (Midjourney, DALL·E, Stable Diffusion)?"
    ),
    "faq.false_positive.question": "Perché una foto reale è stata valutata come IA?",
    "faq.offline.question": "Posso usarlo offline?",
    "faq.rate_limit.question": "C'è un limite di frequenza sull'istanza ospitata?",
    "faq.accuracy.answer_html": (
        "Riporta una probabilità, non un verdetto. I punteggi vicini al 50% sono etichettati come "
        "<em>Incerto</em>; considera ogni singolo risultato come un indizio da combinare con altre "
        'prove. Scopri di più su <a href="/how-accurate">quanto sono accurati i rilevatori di '
        "immagini IA</a>."
    ),
    "faq.leaves_computer.answer_html": (
        "Su questa istanza pubblica, sì: l'immagine viene caricata sul server AiPicDetect (un container "
        "Google Cloud Run gestito dall'autore), valutata in memoria e mai scritta su disco. La "
        "copia pulita resta in memoria solo finché 100 risultati più recenti non la sostituiscono "
        "o il container non si riavvia, e nulla viene inviato a un'API di terze parti. Se vuoi che "
        'nulla lasci la tua macchina, <a href="/self-host">esegui AiPicDetect da solo</a> con un solo '
        'comando Docker. I dettagli sono nella <a href="/privacy">pagina sulla privacy</a>.'
    ),
    "faq.open_source.answer_html": (
        "Sì. Il codice, l'immagine Docker, la CLI e la GitHub Action si trovano tutti nel "
        '<a href="https://github.com/Micorlov/aipicdetect" rel="noopener">repository AiPicDetect</a> sotto '
        "licenza MIT. Il rilevatore è un modello Hugging Face aperto che puoi ispezionare o "
        "sostituire."
    ),
    "faq.remove_metadata.answer_html": (
        "Sì. Dopo aver verificato un'immagine, usa <em>Scarica la copia pulita</em>. AiPicDetect "
        "ricostruisce l'immagine a partire dai suoi pixel, quindi EXIF, XMP, IPTC, C2PA e il "
        'profilo ICC vengono tutti eliminati. <a href="/remove-image-metadata">Come funziona il '
        "pulitore</a>."
    ),
    "faq.formats.answer_html": (
        "JPEG, PNG, WebP, HEIC/HEIF e la maggior parte dei formati che Pillow può decodificare, "
        "fino a 50 MB."
    ),
    "faq.why_metadata.answer_html": (
        "Le credenziali di contenuto C2PA e i tag del software di editing sono indizi di "
        "provenienza. Il pannello mostra quali blocchi (EXIF, XMP, IPTC, C2PA, ICC) porta il file, "
        'così puoi valutarli insieme al punteggio. Vedi <a href="/c2pa">le credenziali di '
        'contenuto C2PA</a> e <a href="/remove-image-metadata">come rimuovere i metadati di '
        "un'immagine</a>."
    ),
    "faq.different_model.answer_html": (
        "Sì. Imposta <code>PICAI_DETECTOR_MODEL</code> su qualsiasi modello di classificazione di "
        "immagini Hugging Face le cui etichette distinguano IA/falso da umano/reale."
    ),
    "faq.free.answer_html": (
        "Sì. AiPicDetect è open source sotto licenza MIT. L'istanza ospitata è gratuita con un limite "
        "di 10 analisi per indirizzo IP ogni 24 ore; una copia self-hosted non ha limiti."
    ),
    "faq.screenshots.answer_html": (
        "Funziona, ma la ricodifica, il ridimensionamento e gli screenshot rimuovono parte delle "
        "tracce a livello di pixel su cui si basa il classificatore, quindi aspettati una "
        "confidenza più bassa e più risultati <em>Incerto</em>."
    ),
    "faq.which_generator.answer_html": (
        "No. AiPicDetect valuta in generale le statistiche dei pixel generati rispetto a quelli reali; "
        "non identifica il generatore e non ha alcuna conoscenza dei generatori usciti dopo la "
        "raccolta dei dati di addestramento del suo modello."
    ),
    "faq.false_positive.answer_html": (
        "Filtri intensi, elaborazione HDR, upscaling, illustrazioni e render 3D condividono "
        "caratteristiche statistiche con le immagini generate. Il punteggio è una probabilità, "
        "non una prova; i falsi positivi capitano."
    ),
    "faq.offline.answer_html": (
        "Sì. Dopo che la prima esecuzione ha scaricato il modello nella cache di Hugging Face, un "
        "AiPicDetect self-hosted non necessita di alcun accesso alla rete."
    ),
    "faq.rate_limit.answer_html": (
        "Sì: 10 analisi per IP client in qualsiasi finestra mobile di 24 ore. Le risposte "
        "includono <code>X-RateLimit-Remaining</code>, e una richiesta oltre il limite restituisce "
        "429 con un'intestazione <code>Retry-After</code>."
    ),
    "nav.detector": "Rilevatore",
    "nav.how_it_works": "Come funziona",
    "nav.how-to-tell-if-an-image-is-ai-generated": "Guida",
    "nav.api": "API",
    "nav.self-host": "Self-hosting",
    "footer.remove-image-metadata": "Rimuovi metadati",
    "footer.c2pa": "C2PA",
    "footer.faq": "FAQ",
    "footer.privacy": "Privacy",
    "footer.self-host": "Self-hosting",
    "footer.about": "Informazioni",
    "ui.nav_aria_label": "Navigazione principale",
    "ui.loading_status": "Caricamento del rilevatore…",
    "ui.hero_overline": "— Analisi forense di immagini IA open source",
    "ui.hero_heading_line1": "Questa foto è reale?",
    "ui.hero_heading_line2": "Ottieni il punteggio e la prova.",
    "ui.tool_aria_label": "Rilevatore di immagini IA",
    "ui.dropzone_aria_label": "Carica un'immagine da analizzare",
    "ui.dropzone_title_fine": "Trascina qui una foto",
    "ui.dropzone_title_coarse": "Verifica una foto",
    "ui.dropzone_sub_fine": "oppure incolla dagli appunti, o",
    "ui.dropzone_sub_coarse": "dalla libreria o dalla fotocamera",
    "ui.btn_check_image_fine": "Verifica questa immagine",
    "ui.btn_choose_photo_coarse": "Scegli una foto",
    "ui.btn_take_photo": "Scatta una foto",
    "ui.dismiss_aria_label": "Chiudi",
    "ui.analyzing_prefix": "Analisi in corso",
    "ui.analyzing_suffix": "· pixel · blocchi di metadati",
    "ui.verdict_overline": "— Verdetto",
    "ui.meter_real": "Reale",
    "ui.meter_uncertain": "Incerto",
    "ui.meter_ai": "IA",
    "ui.model_label": "Modello",
    "ui.verdict_disclaimer_html": (
        "I risultati sono probabilità generate da un classificatore, non verdetti. "
        '<a href="/how-accurate">Come leggere il punteggio.</a>'
    ),
    "ui.btn_check_another": "Verifica un'altra immagine",
    "ui.preview_overline": "— Anteprima",
    "ui.preview_alt": "Anteprima dell'immagine caricata",
    "ui.metadata_overline": "— Metadati",
    "ui.metadata_heading": "Trovato nel file.",
    "ui.jpeg_segments_label": "Segmenti JPEG",
    "ui.btn_download_clean": "Scarica la copia pulita",
    "ui.metadata_scrub_note_html": (
        "Ricreata dai pixel, quindi ogni blocco sopra elencato è stato rimosso. "
        '<a href="/remove-image-metadata">Come funziona</a>'
    ),
    "ui.how_it_works_overline": "— Come funziona",
    "ui.how_it_works_heading": "Tre passaggi. Niente viene salvato.",
    "ui.how_it_works_links_html": (
        '<a href="/how-to-tell-if-an-image-is-ai-generated">Leggi la guida per riconoscere le '
        'immagini IA</a> oppure <a href="/self-host">eseguilo sulla tua macchina</a>.'
    ),
    "ui.faq_overline": "— FAQ",
    "ui.faq_heading": "Prima di chiedere.",
    "ui.faq_more_link": "Altre domande e risposte →",
    "ui.footer_tagline": "AiPicDetect. · open source",
    "ui.footer_detector_label": "Rilevatore:",
    "ui.breadcrumb_aria_label": "Percorso di navigazione",
    "ui.last_updated_prefix": "Ultimo aggiornamento",
    "ui.source_on_github": "codice sorgente su GitHub",
    "ui.btn_try_detector": "Prova il rilevatore",
    "ui.status_ready": "Rilevatore pronto",
    "ui.status_unreachable": "Server non raggiungibile",
    "ui.loading_model_note": "Caricamento del modello di rilevamento (il primo avvio scarica ~750 MB)…",
    "ui.error_empty_file": "Questo file è vuoto.",
    "ui.error_file_too_large": "{name} è {size} — il limite è 50 MB.",
    "ui.error_server_unreachable": "Impossibile raggiungere il server: {message}",
    "ui.verdict_ai": "Probabilmente generata dall'IA",
    "ui.verdict_real": "Probabilmente una foto reale",
    "ui.verdict_uncertain": "Incerto",
    "ui.confidence_suffix": "confidenza",
    "ui.format_unknown": "sconosciuto",
    "ui.metadata_present": "Presente",
    "ui.metadata_not_present": "Assente",
    "ui.no_jpeg_segments": "Nessun segmento JPEG APP",
    "ui.quota_remaining": "{remaining} di {limit} analisi rimaste oggi",
}
