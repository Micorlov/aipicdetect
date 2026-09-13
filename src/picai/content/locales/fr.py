"""French translation table."""

from __future__ import annotations

STRINGS: dict[str, str] = {
    "page.home.title": "picai — Détecteur d'images IA et nettoyeur de métadonnées open source",
    "page.home.description": (
        "Vérifiez si une image est générée par IA avec picai, un détecteur gratuit et open source. "
        "Utilisez-le dans le navigateur ou sur votre propre machine avec Docker ou Python."
    ),
    "page.home.h1": "Cette photo est-elle réelle ? Obtenez le score et la preuve.",
    "page.faq.title": "FAQ du détecteur d'images IA : précision, confidentialité, formats, modèles",
    "page.faq.description": (
        "Réponses aux questions courantes sur picai : la précision de la détection d'images IA, où "
        "votre image est traitée, les formats pris en charge, le changement de modèle et les limites "
        "de débit."
    ),
    "page.faq.h1": "Questions fréquentes sur picai",
    "page.faq.intro_suffix": (
        "Voici les questions les plus fréquentes sur son fonctionnement, sa précision et ce qu'il "
        "advient des images envoyées."
    ),
    "page.faq.still_unsure_html": (
        'Toujours des doutes ? Ouvrez une issue sur <a href="https://github.com/Micorlov/picai/issues" '
        'rel="noopener">GitHub</a>.'
    ),
    "home.entity_sentence": (
        "picai est un outil gratuit et open source qui évalue les images générées par IA et supprime "
        "les métadonnées cachées — hébergé ou auto-hébergé, à vous de choisir."
    ),
    "home.lead": (
        "picai exécute un modèle de détection IA ouvert et lit tous les champs EXIF, C2PA et IPTC "
        "que porte une photo — puis vous remet une copie propre, débarrassée de tout cela. Pas "
        "d'inscription, pas de boîte noire."
    ),
    "home.dropzone_note": "JPEG, PNG, WebP, HEIC · jusqu'à 50 MB · traité en mémoire, jamais écrit sur disque",
    "home.summary": (
        "picai est un outil gratuit et open source qui évalue les images générées par IA et supprime "
        "les métadonnées cachées — hébergé ou auto-hébergé, à vous de choisir. Il évalue la "
        "probabilité qu'une image ait été produite par un générateur IA à l'aide d'un classificateur "
        "Hugging Face ouvert, et peut reconstruire les images pour en supprimer les métadonnées "
        "EXIF, XMP, IPTC, ICC et C2PA. Utilisez l'instance hébergée ou auto-hébergez avec Docker ou "
        "Python."
    ),
    "home.stat.0": "modèle ouvert,<br>aucune API tierce",
    "home.stat.1": "inscriptions<br>requises",
    "home.stat.2": "MB max<br>par envoi",
    "steps.detect.upload.name": "Envoyer.",
    "steps.detect.detect.name": "Détecter.",
    "steps.detect.decide.name": "Décider.",
    "steps.detect.upload.text": (
        "Déposez, collez ou choisissez une image. Elle est envoyée au serveur picai que vous "
        "utilisez (votre propre machine en auto-hébergement), conservée en mémoire et jamais "
        "écrite sur disque."
    ),
    "steps.detect.detect.text": (
        "Un classificateur d'images open source évalue la probabilité que les pixels aient été "
        "produits par un générateur."
    ),
    "steps.detect.decide.text": (
        "Vous obtenez une probabilité IA, une marge de confiance et les blocs de métadonnées que "
        "porte le fichier — comme une probabilité, pas un verdict."
    ),
    "steps.scrub.inspect.name": "Inspecter.",
    "steps.scrub.scrub.name": "Nettoyer.",
    "steps.scrub.verify.name": "Vérifier.",
    "steps.scrub.inspect.text": (
        "Lancez <code>picai inspect photo.jpg</code> pour lister les blocs EXIF, XMP, IPTC, C2PA et "
        "ICC que porte le fichier."
    ),
    "steps.scrub.scrub.text": (
        "Lancez <code>picai scrub photo.jpg</code> (ou <code>POST /scrub</code>). picai décode les "
        "pixels, applique l'orientation EXIF, et construit une toute nouvelle image à partir du "
        "tampon de pixels brut."
    ),
    "steps.scrub.verify.text": (
        "Lancez <code>picai inspect photo.clean.jpg</code> ; il devrait afficher « no metadata signatures found »."
    ),
    "faq.accuracy.question": "Quelle est la précision du détecteur ?",
    "faq.leaves_computer.question": "Mon image quitte-t-elle mon ordinateur ?",
    "faq.open_source.question": "Est-ce open source ?",
    "faq.remove_metadata.question": "Puis-je supprimer le C2PA et les autres métadonnées ?",
    "faq.formats.question": "Quels formats sont pris en charge ?",
    "faq.why_metadata.question": "Pourquoi les métadonnées sont-elles listées ?",
    "faq.different_model.question": "Puis-je utiliser un modèle différent ?",
    "faq.free.question": "picai est-il gratuit ?",
    "faq.screenshots.question": "Fonctionne-t-il sur des captures d'écran ou des images très compressées ?",
    "faq.which_generator.question": (
        "Peut-il identifier le générateur d'une image (Midjourney, DALL·E, Stable Diffusion) ?"
    ),
    "faq.false_positive.question": "Pourquoi une vraie photo a-t-elle été notée comme IA ?",
    "faq.offline.question": "Puis-je l'utiliser hors ligne ?",
    "faq.rate_limit.question": "Y a-t-il une limite de débit sur l'instance hébergée ?",
    "faq.accuracy.answer_html": (
        "Il indique une probabilité, pas un verdict. Les scores proches de 50 % sont étiquetés "
        "<em>Incertain</em> ; considérez tout résultat isolé comme un simple indice à combiner avec "
        'd\'autres preuves. En savoir plus sur <a href="/how-accurate">la précision des détecteurs '
        "d'images IA</a>."
    ),
    "faq.leaves_computer.answer_html": (
        "Sur cette instance publique, oui : l'image est envoyée au serveur picai (un conteneur "
        "Google Cloud Run géré par l'auteur), évaluée en mémoire et jamais écrite sur disque. La "
        "copie nettoyée reste en mémoire seulement jusqu'à ce que 100 résultats plus récents la "
        "remplacent ou que le conteneur redémarre, et rien n'est envoyé à une API tierce. Si vous "
        'voulez que rien ne quitte votre machine, <a href="/self-host">exécutez picai vous-même</a> '
        "avec une seule commande Docker. Les détails sont sur la "
        '<a href="/privacy">page de confidentialité</a>.'
    ),
    "faq.open_source.answer_html": (
        "Oui. Le code, l'image Docker, le CLI et la GitHub Action sont tous dans le "
        '<a href="https://github.com/Micorlov/picai" rel="noopener">dépôt picai</a> sous licence '
        "MIT. Le détecteur est un modèle Hugging Face ouvert que vous pouvez inspecter ou remplacer."
    ),
    "faq.remove_metadata.answer_html": (
        "Oui. Après avoir vérifié une image, utilisez <em>Télécharger la copie propre</em>. picai "
        "reconstruit l'image à partir de ses pixels, si bien que l'EXIF, le XMP, l'IPTC, le C2PA et "
        'le profil ICC sont tous laissés de côté. <a href="/remove-image-metadata">Comment '
        "fonctionne le nettoyeur</a>."
    ),
    "faq.formats.answer_html": (
        "JPEG, PNG, WebP, HEIC/HEIF et la plupart des formats que Pillow peut décoder, jusqu'à 50 MB."
    ),
    "faq.why_metadata.answer_html": (
        "Les identifiants de contenu C2PA et les balises de logiciel d'édition sont des indices de "
        "provenance. Le panneau indique quels blocs (EXIF, XMP, IPTC, C2PA, ICC) porte le fichier "
        'afin que vous puissiez les mettre en balance avec le score. Voir <a href="/c2pa">les '
        'identifiants de contenu C2PA</a> et <a href="/remove-image-metadata">comment supprimer les '
        "métadonnées d'une image</a>."
    ),
    "faq.different_model.answer_html": (
        "Oui. Définissez <code>PICAI_DETECTOR_MODEL</code> avec n'importe quel modèle de "
        "classification d'images Hugging Face dont les étiquettes nomment IA/faux contre "
        "humain/réel."
    ),
    "faq.free.answer_html": (
        "Oui. picai est open source sous licence MIT. L'instance hébergée est gratuite avec une "
        "limite de 10 analyses par adresse IP toutes les 24 heures ; une copie auto-hébergée n'a "
        "aucune limite."
    ),
    "faq.screenshots.answer_html": (
        "Il fonctionne, mais le ré-encodage, le redimensionnement et les captures d'écran effacent "
        "une partie des traces au niveau des pixels sur lesquelles s'appuie le classificateur, donc "
        "attendez-vous à une confiance plus faible et à davantage de résultats <em>Incertain</em>."
    ),
    "faq.which_generator.answer_html": (
        "Non. picai évalue globalement des statistiques de pixels générés contre réels ; il "
        "n'identifie pas le générateur, et n'a aucune connaissance des générateurs sortis après la "
        "collecte des données d'entraînement de son modèle."
    ),
    "faq.false_positive.answer_html": (
        "Les filtres intenses, le traitement HDR, l'agrandissement, les illustrations et les rendus "
        "3D partagent des caractéristiques statistiques avec les images générées. Le score est une "
        "probabilité, pas une preuve ; des faux positifs surviennent."
    ),
    "faq.offline.answer_html": (
        "Oui. Une fois que le premier lancement a téléchargé le modèle dans le cache Hugging Face, "
        "un picai auto-hébergé n'a besoin d'aucun accès réseau."
    ),
    "faq.rate_limit.answer_html": (
        "Oui : 10 analyses par IP cliente sur toute fenêtre glissante de 24 heures. Les réponses "
        "portent <code>X-RateLimit-Remaining</code>, et une requête dépassant la limite renvoie 429 "
        "avec un en-tête <code>Retry-After</code>."
    ),
    "nav.detector": "Détecteur",
    "nav.how_it_works": "Fonctionnement",
    "nav.how-to-tell-if-an-image-is-ai-generated": "Guide",
    "nav.api": "API",
    "nav.self-host": "Auto-hébergement",
    "footer.remove-image-metadata": "Supprimer les métadonnées",
    "footer.c2pa": "C2PA",
    "footer.faq": "FAQ",
    "footer.privacy": "Confidentialité",
    "footer.self-host": "Auto-hébergement",
    "footer.about": "À propos",
    "ui.nav_aria_label": "Navigation principale",
    "ui.loading_status": "Chargement du détecteur…",
    "ui.hero_overline": "— Analyse forensique d'images par IA, open source",
    "ui.hero_heading_line1": "Cette photo est-elle réelle ?",
    "ui.hero_heading_line2": "Obtenez le score et la preuve.",
    "ui.tool_aria_label": "Détecteur d'images IA",
    "ui.dropzone_aria_label": "Envoyer une image à analyser",
    "ui.dropzone_title_fine": "Glissez-déposez une photo",
    "ui.dropzone_title_coarse": "Vérifier une photo",
    "ui.dropzone_sub_fine": "ou collez depuis le presse-papiers, ou",
    "ui.dropzone_sub_coarse": "depuis votre photothèque ou l'appareil photo",
    "ui.btn_check_image_fine": "Vérifier cette image",
    "ui.btn_choose_photo_coarse": "Choisir une photo",
    "ui.btn_take_photo": "Prendre une photo",
    "ui.dismiss_aria_label": "Fermer",
    "ui.analyzing_prefix": "Analyse en cours",
    "ui.analyzing_suffix": "· pixels · blocs de métadonnées",
    "ui.verdict_overline": "— Verdict",
    "ui.meter_real": "Réel",
    "ui.meter_uncertain": "Incertain",
    "ui.meter_ai": "IA",
    "ui.model_label": "Modèle",
    "ui.verdict_disclaimer_html": (
        "Les résultats sont des probabilités issues d'un classificateur, pas des verdicts. "
        '<a href="/how-accurate">Comment lire le score.</a>'
    ),
    "ui.btn_check_another": "Vérifier une autre image",
    "ui.preview_overline": "— Aperçu",
    "ui.preview_alt": "Aperçu de l'image envoyée",
    "ui.metadata_overline": "— Métadonnées",
    "ui.metadata_heading": "Trouvé dans le fichier.",
    "ui.jpeg_segments_label": "Segments JPEG",
    "ui.btn_download_clean": "Télécharger la copie propre",
    "ui.metadata_scrub_note_html": (
        "Reconstruite à partir des pixels, donc chaque bloc ci-dessus a disparu. "
        '<a href="/remove-image-metadata">Comment ça marche</a>'
    ),
    "ui.how_it_works_overline": "— Fonctionnement",
    "ui.how_it_works_heading": "Trois étapes. Rien n'est conservé.",
    "ui.how_it_works_links_html": (
        '<a href="/how-to-tell-if-an-image-is-ai-generated">Lisez le guide pour repérer les images '
        'IA</a> ou <a href="/self-host">exécutez-le sur votre propre machine</a>.'
    ),
    "ui.faq_overline": "— FAQ",
    "ui.faq_heading": "Avant de demander.",
    "ui.faq_more_link": "Plus de questions et réponses →",
    "ui.footer_tagline": "picai. · open source",
    "ui.footer_detector_label": "Détecteur :",
    "ui.breadcrumb_aria_label": "Fil d'Ariane",
    "ui.last_updated_prefix": "Dernière mise à jour",
    "ui.source_on_github": "code source sur GitHub",
    "ui.btn_try_detector": "Essayer le détecteur",
    "ui.status_ready": "Détecteur prêt",
    "ui.status_unreachable": "Serveur injoignable",
    "ui.loading_model_note": "Chargement du modèle de détection (le premier lancement télécharge ~750 MB)…",
    "ui.error_empty_file": "Ce fichier est vide.",
    "ui.error_file_too_large": "{name} fait {size} — la limite est de 50 MB.",
    "ui.error_server_unreachable": "Impossible de joindre le serveur : {message}",
    "ui.verdict_ai": "Probablement généré par IA",
    "ui.verdict_real": "Probablement une vraie photo",
    "ui.verdict_uncertain": "Incertain",
    "ui.confidence_suffix": "confiance",
    "ui.format_unknown": "inconnu",
    "ui.metadata_present": "Présent",
    "ui.metadata_not_present": "Absent",
    "ui.no_jpeg_segments": "Aucun segment JPEG APP",
    "ui.quota_remaining": "{remaining} analyses restantes sur {limit} aujourd'hui",
}
