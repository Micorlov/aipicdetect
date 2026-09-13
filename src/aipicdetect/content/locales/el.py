"""Greek translation table.

Falls back to English (see :func:`aipicdetect.content.locales.t`) for any key not defined here, but
every key from :mod:`aipicdetect.content.locales.en` is translated below.
"""

from __future__ import annotations

STRINGS: dict[str, str] = {
    # Page metadata
    "page.home.title": (
        "AiPicDetect — Ανιχνευτής Εικόνων Τεχνητής Νοημοσύνης και Καθαριστής Μεταδεδομένων Ανοιχτού "
        "Κώδικα"
    ),
    "page.home.description": (
        "Ελέγξτε αν μια εικόνα έχει δημιουργηθεί από τεχνητή νοημοσύνη με το AiPicDetect, έναν δωρεάν "
        "ανιχνευτή ανοιχτού κώδικα. Χρησιμοποιήστε το στον περιηγητή ή εκτελέστε το στον δικό σας "
        "υπολογιστή με Docker ή Python."
    ),
    "page.home.h1": "Είναι αληθινή αυτή η φωτογραφία; Δείτε τη βαθμολογία και την απόδειξη.",
    "page.faq.title": "Συχνές Ερωτήσεις για τον Ανιχνευτή Εικόνων ΤΝ: Ακρίβεια, Απόρρητο, Μορφές, Μοντέλα",
    "page.faq.description": (
        "Απαντήσεις σε συχνές ερωτήσεις σχετικά με το AiPicDetect: πόσο ακριβής είναι η ανίχνευση εικόνων "
        "τεχνητής νοημοσύνης, πού επεξεργάζεται η εικόνα σας, ποιες μορφές υποστηρίζονται, αλλαγή "
        "μοντέλου και όρια αιτημάτων."
    ),
    "page.faq.h1": "Συχνές ερωτήσεις για το AiPicDetect",
    "page.faq.intro_suffix": (
        "Αυτές είναι οι ερωτήσεις που κάνουν συχνότερα οι χρήστες σχετικά με το πώς λειτουργεί, "
        "πόσο ακριβές είναι και τι συμβαίνει με τις εικόνες που ανεβάζουν."
    ),
    "page.faq.still_unsure_html": (
        'Έχετε ακόμη αμφιβολίες; Ανοίξτε ένα issue στο <a '
        'href="https://github.com/Micorlov/aipicdetect/issues" rel="noopener">GitHub</a>.'
    ),
    # Home page copy
    "home.entity_sentence": (
        "Το AiPicDetect είναι ένα δωρεάν εργαλείο ανοιχτού κώδικα που βαθμολογεί εικόνες που "
        "δημιουργήθηκαν από τεχνητή νοημοσύνη και αφαιρεί κρυφά μεταδεδομένα — φιλοξενούμενο ή "
        "αυτοφιλοξενούμενο, η επιλογή είναι δική σας."
    ),
    "home.lead": (
        "Το AiPicDetect εκτελεί ένα ανοιχτό μοντέλο ανίχνευσης ΤΝ και διαβάζει κάθε πεδίο EXIF, C2PA και "
        "IPTC που φέρει μια φωτογραφία — και στη συνέχεια σας δίνει ένα καθαρό αντίγραφο "
        "απαλλαγμένο από όλα αυτά. Χωρίς εγγραφή, χωρίς μαύρο κουτί."
    ),
    "home.dropzone_note": (
        "JPEG, PNG, WebP, HEIC · έως 50 MB · επεξεργασία στη μνήμη, ποτέ δεν γράφεται στον δίσκο"
    ),
    "home.summary": (
        "Το AiPicDetect είναι ένα δωρεάν εργαλείο ανοιχτού κώδικα που βαθμολογεί εικόνες που "
        "δημιουργήθηκαν από τεχνητή νοημοσύνη και αφαιρεί κρυφά μεταδεδομένα — φιλοξενούμενο ή "
        "αυτοφιλοξενούμενο, η επιλογή είναι δική σας. Βαθμολογεί την πιθανότητα μια εικόνα να έχει "
        "παραχθεί από γεννήτρια ΤΝ χρησιμοποιώντας έναν ανοιχτό ταξινομητή Hugging Face και μπορεί "
        "να αποδώσει εκ νέου εικόνες για να αφαιρέσει μεταδεδομένα EXIF, XMP, IPTC, ICC και C2PA. "
        "Χρησιμοποιήστε τη φιλοξενούμενη έκδοση ή αυτοφιλοξενήστε το AiPicDetect με Docker ή Python."
    ),
    "home.stat.0": "ανοιχτό μοντέλο,<br>χωρίς API τρίτων",
    "home.stat.1": "εγγραφές<br>δεν απαιτούνται",
    "home.stat.2": "MB μέγιστο<br>μέγεθος μεταφόρτωσης",
    # Detect steps
    "steps.detect.upload.name": "Ανεβάστε.",
    "steps.detect.upload.text": (
        "Σύρετε, επικολλήστε ή επιλέξτε μια εικόνα. Αποστέλλεται στον διακομιστή AiPicDetect που "
        "χρησιμοποιείτε (στο δικό σας μηχάνημα αν είναι αυτοφιλοξενούμενο), διατηρείται στη μνήμη "
        "και δεν γράφεται ποτέ στον δίσκο."
    ),
    "steps.detect.detect.name": "Ανίχνευση.",
    "steps.detect.detect.text": (
        "Ένας ταξινομητής εικόνων ανοιχτού κώδικα βαθμολογεί την πιθανότητα τα pixel να έχουν "
        "παραχθεί από μια γεννήτρια."
    ),
    "steps.detect.decide.name": "Απόφαση.",
    "steps.detect.decide.text": (
        "Λαμβάνετε μια πιθανότητα ΤΝ, ένα εύρος εμπιστοσύνης και τα μπλοκ μεταδεδομένων που φέρει "
        "το αρχείο — ως πιθανότητα, όχι ως ετυμηγορία."
    ),
    # Scrub steps — <code> blocks contain literal shell commands and must stay untranslated
    "steps.scrub.inspect.name": "Επιθεωρήστε.",
    "steps.scrub.inspect.text": (
        "Εκτελέστε <code>aipicdetect inspect photo.jpg</code> για να παραθέσετε τα μπλοκ EXIF, XMP, "
        "IPTC, C2PA και ICC που φέρει το αρχείο."
    ),
    "steps.scrub.scrub.name": "Καθαρίστε.",
    "steps.scrub.scrub.text": (
        "Εκτελέστε <code>aipicdetect scrub photo.jpg</code> (ή <code>POST /scrub</code>). Το AiPicDetect "
        "αποκωδικοποιεί τα pixel, εφαρμόζει τον προσανατολισμό EXIF και δημιουργεί μια "
        "ολοκαίνουργια εικόνα από το ακατέργαστο buffer pixel."
    ),
    "steps.scrub.verify.name": "Επαληθεύστε.",
    "steps.scrub.verify.text": (
        "Εκτελέστε <code>aipicdetect inspect photo.clean.jpg</code>· θα πρέπει να εκτυπώσει «no metadata signatures found»."
    ),
    # FAQ (home slugs)
    "faq.accuracy.question": "Πόσο ακριβής είναι ο ανιχνευτής;",
    "faq.accuracy.answer_html": (
        "Αναφέρει μια πιθανότητα, όχι ετυμηγορία. Βαθμολογίες κοντά στο 50% χαρακτηρίζονται ως "
        "<em>Αβέβαιο</em>· αντιμετωπίστε κάθε μεμονωμένο αποτέλεσμα ως ένδειξη και συνδυάστε το με "
        'άλλα στοιχεία. Διαβάστε περισσότερα στο <a href="/how-accurate">πόσο ακριβείς είναι οι '
        "ανιχνευτές εικόνων ΤΝ</a>."
    ),
    "faq.leaves_computer.question": "Η εικόνα μου φεύγει από τον υπολογιστή μου;",
    "faq.leaves_computer.answer_html": (
        "Σε αυτή τη δημόσια έκδοση, ναι: η εικόνα ανεβαίνει στον διακομιστή AiPicDetect (ένα container "
        "Google Cloud Run που διαχειρίζεται ο δημιουργός), βαθμολογείται στη μνήμη και δεν "
        "γράφεται ποτέ στον δίσκο. Το καθαρισμένο αντίγραφο παραμένει στη μνήμη μόνο έως ότου το "
        "αντικαταστήσουν 100 νεότερα αποτελέσματα ή επανεκκινήσει το container, και τίποτα δεν "
        'αποστέλλεται σε API τρίτων. Αν θέλετε τίποτα να μην φεύγει από το μηχάνημά σας, '
        '<a href="/self-host">εκτελέστε το AiPicDetect μόνοι σας</a> με μία εντολή Docker. Λεπτομέρειες '
        'στη <a href="/privacy">σελίδα απορρήτου</a>.'
    ),
    "faq.open_source.question": "Είναι ανοιχτού κώδικα;",
    "faq.open_source.answer_html": (
        "Ναι. Ο κώδικας, η εικόνα Docker, το CLI και το GitHub Action βρίσκονται όλα στο "
        '<a href="https://github.com/Micorlov/aipicdetect" rel="noopener">αποθετήριο AiPicDetect</a> υπό την '
        "άδεια MIT. Ο ανιχνευτής είναι ένα ανοιχτό μοντέλο Hugging Face που μπορείτε να "
        "επιθεωρήσετε ή να αντικαταστήσετε."
    ),
    "faq.remove_metadata.question": "Μπορώ να αφαιρέσω το C2PA και άλλα μεταδεδομένα;",
    "faq.remove_metadata.answer_html": (
        "Ναι. Αφού ελέγξετε μια εικόνα, χρησιμοποιήστε την επιλογή <em>Λήψη καθαρού "
        "αντιγράφου</em>. Το AiPicDetect ανακατασκευάζει την εικόνα από τα pixel της, οπότε τα EXIF, "
        'XMP, IPTC, C2PA και το προφίλ ICC αφαιρούνται εντελώς. <a href="/remove-image-metadata">'
        "Πώς λειτουργεί ο καθαρισμός</a>."
    ),
    "faq.formats.question": "Ποιες μορφές υποστηρίζονται;",
    "faq.formats.answer_html": (
        "JPEG, PNG, WebP, HEIC/HEIF και οι περισσότερες μορφές που μπορεί να αποκωδικοποιήσει το "
        "Pillow, έως 50 MB."
    ),
    "faq.why_metadata.question": "Γιατί εμφανίζονται τα μεταδεδομένα;",
    "faq.why_metadata.answer_html": (
        "Τα διαπιστευτήρια περιεχομένου C2PA και οι ετικέτες λογισμικού επεξεργασίας είναι "
        "ενδείξεις προέλευσης. Ο πίνακας δείχνει ποια μπλοκ (EXIF, XMP, IPTC, C2PA, ICC) φέρει το "
        'αρχείο, ώστε να μπορείτε να τα συνεκτιμήσετε μαζί με τη βαθμολογία. Δείτε τα '
        '<a href="/c2pa">διαπιστευτήρια περιεχομένου C2PA</a> και '
        '<a href="/remove-image-metadata">πώς να αφαιρέσετε τα μεταδεδομένα εικόνας</a>.'
    ),
    "faq.different_model.question": "Μπορώ να χρησιμοποιήσω διαφορετικό μοντέλο;",
    "faq.different_model.answer_html": (
        "Ναι. Ορίστε το <code>PICAI_DETECTOR_MODEL</code> σε οποιοδήποτε μοντέλο ταξινόμησης "
        "εικόνων του Hugging Face του οποίου οι ετικέτες ονομάζουν περιεχόμενο ΤΝ/ψεύτικο έναντι "
        "ανθρώπινου/πραγματικού."
    ),
    # FAQ (more slugs)
    "faq.free.question": "Είναι δωρεάν το AiPicDetect;",
    "faq.free.answer_html": (
        "Ναι. Το AiPicDetect είναι ανοιχτού κώδικα υπό την άδεια MIT. Η φιλοξενούμενη έκδοση είναι "
        "δωρεάν με όριο 10 αναλύσεων ανά διεύθυνση IP κάθε 24 ώρες· ένα αυτοφιλοξενούμενο "
        "αντίγραφο δεν έχει όριο."
    ),
    "faq.screenshots.question": "Λειτουργεί σε στιγμιότυπα οθόνης ή σε ιδιαίτερα συμπιεσμένες εικόνες;",
    "faq.screenshots.answer_html": (
        "Λειτουργεί, αλλά η επανακωδικοποίηση, η αλλαγή μεγέθους και τα στιγμιότυπα οθόνης "
        "αφαιρούν μέρος των ιχνών σε επίπεδο pixel στα οποία βασίζεται ο ταξινομητής, οπότε "
        "αναμένετε χαμηλότερη εμπιστοσύνη και περισσότερα αποτελέσματα <em>Αβέβαιο</em>."
    ),
    "faq.which_generator.question": (
        "Μπορεί να διακρίνει ποια γεννήτρια δημιούργησε μια εικόνα (Midjourney, DALL·E, Stable "
        "Diffusion);"
    ),
    "faq.which_generator.answer_html": (
        "Όχι. Το AiPicDetect βαθμολογεί γενικά τα στατιστικά στοιχεία pixel «παραγμένο έναντι "
        "πραγματικού»· δεν αναγνωρίζει τη συγκεκριμένη γεννήτρια και δεν γνωρίζει τίποτα για "
        "γεννήτριες που κυκλοφόρησαν μετά τη συλλογή των δεδομένων εκπαίδευσης του μοντέλου του."
    ),
    "faq.false_positive.question": "Γιατί μια πραγματική φωτογραφία βαθμολογήθηκε ως ΤΝ;",
    "faq.false_positive.answer_html": (
        "Έντονα φίλτρα, επεξεργασία HDR, μεγέθυνση, εικονογραφήσεις και τρισδιάστατα renders "
        "μοιράζονται στατιστικά χαρακτηριστικά με τις παραγόμενες εικόνες. Η βαθμολογία είναι "
        "πιθανότητα, όχι απόδειξη· συμβαίνουν ψευδώς θετικά αποτελέσματα."
    ),
    "faq.offline.question": "Μπορώ να το χρησιμοποιήσω εκτός σύνδεσης;",
    "faq.offline.answer_html": (
        "Ναι. Αφού η πρώτη εκτέλεση κατεβάσει το μοντέλο στην cache του Hugging Face, ένα "
        "αυτοφιλοξενούμενο AiPicDetect δεν χρειάζεται πρόσβαση στο δίκτυο."
    ),
    "faq.rate_limit.question": "Υπάρχει όριο αιτημάτων στη φιλοξενούμενη έκδοση;",
    "faq.rate_limit.answer_html": (
        "Ναι: 10 αναλύσεις ανά IP πελάτη σε οποιοδήποτε κυλιόμενο παράθυρο 24 ωρών. Οι απαντήσεις "
        "φέρουν την κεφαλίδα <code>X-RateLimit-Remaining</code>, και ένα αίτημα πέρα από το όριο "
        "επιστρέφει 429 με κεφαλίδα <code>Retry-After</code>."
    ),
    # Navigation
    "nav.detector": "Ανιχνευτής",
    "nav.how_it_works": "Πώς λειτουργεί",
    "nav.how-to-tell-if-an-image-is-ai-generated": "Οδηγός",
    "nav.api": "API",
    "nav.self-host": "Αυτοφιλοξενία",
    # Footer
    "footer.remove-image-metadata": "Αφαίρεση μεταδεδομένων",
    "footer.c2pa": "C2PA",
    "footer.faq": "Συχνές ερωτήσεις",
    "footer.privacy": "Απόρρητο",
    "footer.self-host": "Αυτοφιλοξενία",
    "footer.about": "Σχετικά",
    # UI strings
    "ui.nav_aria_label": "Κύρια πλοήγηση",
    "ui.loading_status": "Φόρτωση ανιχνευτή…",
    "ui.hero_overline": "— Ανοιχτού κώδικα εγκληματολογία εικόνων ΤΝ",
    "ui.hero_heading_line1": "Είναι αληθινή αυτή η φωτογραφία;",
    "ui.hero_heading_line2": "Δείτε τη βαθμολογία και την απόδειξη.",
    "ui.tool_aria_label": "Ανιχνευτής εικόνων ΤΝ",
    "ui.dropzone_aria_label": "Ανεβάστε μια εικόνα για ανάλυση",
    "ui.dropzone_title_fine": "Σύρετε και αφήστε μια φωτογραφία",
    "ui.dropzone_title_coarse": "Ελέγξτε μια φωτογραφία",
    "ui.dropzone_sub_fine": "ή επικολλήστε από το πρόχειρο, ή",
    "ui.dropzone_sub_coarse": "από τη βιβλιοθήκη σας ή την κάμερα",
    "ui.btn_check_image_fine": "Έλεγχος αυτής της εικόνας",
    "ui.btn_choose_photo_coarse": "Επιλογή φωτογραφίας",
    "ui.btn_take_photo": "Λήψη φωτογραφίας",
    "ui.dismiss_aria_label": "Απόρριψη",
    "ui.analyzing_prefix": "Ανάλυση",
    "ui.analyzing_suffix": "· pixel · μπλοκ μεταδεδομένων",
    "ui.verdict_overline": "— Ετυμηγορία",
    "ui.meter_real": "Πραγματικό",
    "ui.meter_uncertain": "Αβέβαιο",
    "ui.meter_ai": "ΤΝ",
    "ui.model_label": "Μοντέλο",
    "ui.verdict_disclaimer_html": (
        "Τα αποτελέσματα είναι πιθανότητες από έναν ταξινομητή, όχι ετυμηγορίες. "
        '<a href="/how-accurate">Πώς να διαβάσετε τη βαθμολογία.</a>'
    ),
    "ui.btn_check_another": "Έλεγχος άλλης εικόνας",
    "ui.preview_overline": "— Προεπισκόπηση",
    "ui.preview_alt": "Προεπισκόπηση εικόνας που ανέβηκε",
    "ui.metadata_overline": "— Μεταδεδομένα",
    "ui.metadata_heading": "Βρέθηκαν στο αρχείο.",
    "ui.jpeg_segments_label": "Τμήματα JPEG",
    "ui.btn_download_clean": "Λήψη του καθαρού αντιγράφου",
    "ui.metadata_scrub_note_html": (
        "Αποδόθηκε εκ νέου από τα pixel, οπότε κάθε μπλοκ παραπάνω έχει εξαφανιστεί. "
        '<a href="/remove-image-metadata">Πώς λειτουργεί</a>'
    ),
    "ui.how_it_works_overline": "— Πώς λειτουργεί",
    "ui.how_it_works_heading": "Τρία βήματα. Τίποτα δεν αποθηκεύεται.",
    "ui.how_it_works_links_html": (
        '<a href="/how-to-tell-if-an-image-is-ai-generated">Διαβάστε τον οδηγό για να εντοπίζετε '
        'εικόνες ΤΝ</a> ή <a href="/self-host">εκτελέστε το στο δικό σας μηχάνημα</a>.'
    ),
    "ui.faq_overline": "— Συχνές ερωτήσεις",
    "ui.faq_heading": "Πριν ρωτήσετε.",
    "ui.faq_more_link": "Περισσότερες ερωτήσεις και απαντήσεις →",
    "ui.footer_tagline": "AiPicDetect. · ανοιχτός κώδικας",
    "ui.footer_detector_label": "Ανιχνευτής:",
    "ui.breadcrumb_aria_label": "Διαδρομή πλοήγησης",
    "ui.last_updated_prefix": "Τελευταία ενημέρωση",
    "ui.source_on_github": "πηγαίος κώδικας στο GitHub",
    "ui.btn_try_detector": "Δοκιμάστε τον ανιχνευτή",
    "ui.status_ready": "Ο ανιχνευτής είναι έτοιμος",
    "ui.status_unreachable": "Ο διακομιστής δεν είναι προσβάσιμος",
    "ui.loading_model_note": "Φόρτωση μοντέλου ανιχνευτή (η πρώτη εκτέλεση κατεβάζει ~750 MB)…",
    "ui.error_empty_file": "Αυτό το αρχείο είναι κενό.",
    "ui.error_file_too_large": "Το {name} είναι {size} — το όριο είναι 50 MB.",
    "ui.error_server_unreachable": "Δεν ήταν δυνατή η σύνδεση με τον διακομιστή: {message}",
    "ui.verdict_ai": "Πιθανώς δημιουργήθηκε από ΤΝ",
    "ui.verdict_real": "Πιθανώς πραγματική φωτογραφία",
    "ui.verdict_uncertain": "Αβέβαιο",
    "ui.confidence_suffix": "εμπιστοσύνη",
    "ui.format_unknown": "άγνωστο",
    "ui.metadata_present": "Υπάρχει",
    "ui.metadata_not_present": "Δεν υπάρχει",
    "ui.no_jpeg_segments": "Δεν υπάρχουν τμήματα JPEG APP",
    "ui.quota_remaining": "Απομένουν {remaining} από {limit} αναλύσεις σήμερα",
}
