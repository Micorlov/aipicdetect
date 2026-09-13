"""Indonesian translation table. Falls back to English (see picai.content.locales) for
any key missing here, so this file only needs to define what has actually been translated.
"""

from __future__ import annotations

STRINGS: dict[str, str] = {
    # Page metadata
    "page.home.title": "picai — Detektor Gambar AI dan Pembersih Metadata Sumber Terbuka",
    "page.home.description": (
        "Periksa apakah sebuah gambar dihasilkan oleh AI dengan picai, detektor gratis dan sumber "
        "terbuka. Gunakan langsung di browser atau jalankan di komputer Anda sendiri dengan Docker "
        "atau Python."
    ),
    "page.home.h1": "Apakah foto ini asli? Dapatkan skor dan buktinya.",
    "page.faq.title": "FAQ Detektor Gambar AI: Akurasi, Privasi, Format, Model",
    "page.faq.description": (
        "Jawaban atas pertanyaan umum tentang picai: seberapa akurat deteksi gambar AI, di mana "
        "gambar Anda diproses, format yang didukung, penggantian model, dan batas penggunaan."
    ),
    "page.faq.h1": "Pertanyaan yang sering diajukan tentang picai",
    "page.faq.intro_suffix": (
        "Ini adalah pertanyaan yang paling sering ditanyakan orang tentang cara kerjanya, seberapa "
        "akurat, dan apa yang terjadi pada gambar yang mereka unggah."
    ),
    "page.faq.still_unsure_html": (
        'Masih belum yakin? Buka issue di <a href="https://github.com/Micorlov/picai/issues" '
        'rel="noopener">GitHub</a>.'
    ),
    # Home page copy
    "home.entity_sentence": (
        "picai adalah alat gratis dan sumber terbuka yang menilai gambar buatan AI dan menghapus "
        "metadata tersembunyi — versi hosting atau self-host, pilihan ada di tangan Anda."
    ),
    "home.lead": (
        "picai menjalankan model deteksi AI sumber terbuka dan membaca setiap kolom EXIF, C2PA, dan "
        "IPTC yang dibawa sebuah foto — lalu memberi Anda salinan bersih dengan semuanya dihapus. "
        "Tanpa pendaftaran, tanpa kotak hitam."
    ),
    "home.dropzone_note": (
        "JPEG, PNG, WebP, HEIC · hingga 50 MB · diproses dalam memori, tidak pernah ditulis ke disk"
    ),
    "home.summary": (
        "picai adalah alat gratis dan sumber terbuka yang menilai gambar buatan AI dan menghapus "
        "metadata tersembunyi — versi hosting atau self-host, pilihan ada di tangan Anda. Alat ini "
        "menilai seberapa besar kemungkinan sebuah gambar dihasilkan oleh generator AI menggunakan "
        "pengklasifikasi terbuka dari Hugging Face, dan dapat me-render ulang gambar untuk menghapus "
        "metadata EXIF, XMP, IPTC, ICC, dan C2PA. Gunakan instans hosting atau self-host dengan "
        "Docker atau Python."
    ),
    "home.stat.0": "model terbuka,<br>tanpa API pihak ketiga",
    "home.stat.1": "tanpa perlu<br>pendaftaran",
    "home.stat.2": "MB maksimum<br>unggahan",
    # Detect steps
    "steps.detect.upload.name": "Unggah.",
    "steps.detect.detect.name": "Deteksi.",
    "steps.detect.decide.name": "Putuskan.",
    "steps.detect.upload.text": (
        "Seret, tempel, atau pilih sebuah gambar. Gambar dikirim ke server picai yang Anda gunakan "
        "(komputer Anda sendiri jika self-host), disimpan dalam memori, dan tidak pernah ditulis ke "
        "disk."
    ),
    "steps.detect.detect.text": (
        "Pengklasifikasi gambar sumber terbuka menilai seberapa besar kemungkinan piksel tersebut "
        "dihasilkan oleh generator."
    ),
    "steps.detect.decide.text": (
        "Anda mendapatkan kemungkinan AI, rentang keyakinan, dan blok metadata yang dibawa file — "
        "sebagai probabilitas, bukan vonis."
    ),
    # Scrub steps — <code> blocks contain literal shell commands and must stay untranslated
    "steps.scrub.inspect.name": "Periksa.",
    "steps.scrub.scrub.name": "Bersihkan.",
    "steps.scrub.verify.name": "Verifikasi.",
    "steps.scrub.inspect.text": (
        "Jalankan <code>picai inspect photo.jpg</code> untuk menampilkan daftar blok EXIF, XMP, "
        "IPTC, C2PA, dan ICC yang dibawa file."
    ),
    "steps.scrub.scrub.text": (
        "Jalankan <code>picai scrub photo.jpg</code> (atau <code>POST /scrub</code>). picai "
        "mendekode piksel, menerapkan orientasi EXIF, dan membangun gambar yang sama sekali baru "
        "dari buffer piksel mentah."
    ),
    "steps.scrub.verify.text": (
        "Jalankan <code>picai inspect photo.clean.jpg</code>; hasilnya harus menampilkan "
        "“no metadata signatures found”."
    ),
    # FAQ (home slugs)
    "faq.accuracy.question": "Seberapa akurat detektor ini?",
    "faq.accuracy.answer_html": (
        "Detektor ini melaporkan probabilitas, bukan vonis. Skor mendekati 50% diberi label "
        "<em>Tidak pasti</em>; anggap setiap hasil sebagai satu sinyal dan gabungkan dengan bukti "
        'lain. Baca lebih lanjut tentang <a href="/how-accurate">seberapa akurat detektor gambar '
        "AI</a>."
    ),
    "faq.leaves_computer.question": "Apakah gambar saya keluar dari komputer saya?",
    "faq.leaves_computer.answer_html": (
        "Pada instans publik ini, ya: gambar diunggah ke server picai (kontainer Google Cloud Run "
        "yang dijalankan oleh penulis), dinilai dalam memori dan tidak pernah ditulis ke disk. "
        "Salinan yang telah dibersihkan hanya disimpan dalam memori sampai digantikan oleh 100 "
        "hasil yang lebih baru atau kontainer dimulai ulang, dan tidak ada yang dikirim ke API "
        'pihak ketiga mana pun. Jika Anda ingin tidak ada apa pun yang keluar dari komputer Anda, '
        '<a href="/self-host">jalankan picai sendiri</a> dengan satu perintah Docker. Detailnya '
        'ada di <a href="/privacy">halaman privasi</a>.'
    ),
    "faq.open_source.question": "Apakah ini sumber terbuka?",
    "faq.open_source.answer_html": (
        "Ya. Kode, image Docker, CLI, dan GitHub Action semuanya ada di "
        '<a href="https://github.com/Micorlov/picai" rel="noopener">repositori picai</a> di bawah '
        "lisensi MIT. Detektornya adalah model terbuka dari Hugging Face yang dapat Anda periksa "
        "atau ganti."
    ),
    "faq.remove_metadata.question": "Bisakah saya menghapus C2PA dan metadata lainnya?",
    "faq.remove_metadata.answer_html": (
        "Ya. Setelah memeriksa sebuah gambar, gunakan <em>Unduh salinan bersih</em>. picai "
        "membangun ulang gambar dari pikselnya, sehingga EXIF, XMP, IPTC, C2PA, dan profil ICC "
        'semuanya tertinggal. <a href="/remove-image-metadata">Cara kerja pembersih</a>.'
    ),
    "faq.formats.question": "Format apa saja yang didukung?",
    "faq.formats.answer_html": (
        "JPEG, PNG, WebP, HEIC/HEIF, dan sebagian besar format yang dapat didekode oleh Pillow, "
        "hingga 50 MB."
    ),
    "faq.why_metadata.question": "Mengapa metadata ditampilkan?",
    "faq.why_metadata.answer_html": (
        "Kredensial konten C2PA dan tag perangkat lunak penyuntingan adalah petunjuk asal gambar. "
        "Panel ini menampilkan blok mana (EXIF, XMP, IPTC, C2PA, ICC) yang dibawa oleh file "
        'tersebut sehingga Anda dapat mempertimbangkannya bersama skor. Lihat <a href="/c2pa">'
        'kredensial konten C2PA</a> dan <a href="/remove-image-metadata">cara menghapus metadata '
        "gambar</a>."
    ),
    "faq.different_model.question": "Bisakah saya menggunakan model yang berbeda?",
    "faq.different_model.answer_html": (
        "Ya. Atur <code>PICAI_DETECTOR_MODEL</code> ke model klasifikasi gambar Hugging Face mana "
        "pun yang labelnya menamai konten AI/palsu vs. manusia/asli."
    ),
    # FAQ (more slugs)
    "faq.free.question": "Apakah picai gratis?",
    "faq.free.answer_html": (
        "Ya. picai bersifat sumber terbuka di bawah lisensi MIT. Instans hosting gratis digunakan "
        "dengan batas 10 analisis per alamat IP setiap 24 jam; salinan self-host tidak memiliki "
        "batas."
    ),
    "faq.screenshots.question": "Apakah ini bekerja pada tangkapan layar atau gambar yang sangat terkompresi?",
    "faq.screenshots.answer_html": (
        "Ini tetap berjalan, tetapi pengodean ulang, pengubahan ukuran, dan tangkapan layar "
        "menghilangkan sebagian jejak tingkat piksel yang diandalkan oleh pengklasifikasi, jadi "
        "perkirakan keyakinan yang lebih rendah dan lebih banyak hasil <em>Tidak pasti</em>."
    ),
    "faq.which_generator.question": (
        "Bisakah ini mengetahui generator mana yang membuat sebuah gambar (Midjourney, DALL·E, "
        "Stable Diffusion)?"
    ),
    "faq.which_generator.answer_html": (
        "Tidak. picai secara umum menilai statistik piksel yang dihasilkan versus asli; ini tidak "
        "mengidentifikasi generatornya, dan tidak memiliki pengetahuan tentang generator yang "
        "dirilis setelah data pelatihan modelnya dikumpulkan."
    ),
    "faq.false_positive.question": "Mengapa foto asli mendapat skor sebagai AI?",
    "faq.false_positive.answer_html": (
        "Filter berat, pemrosesan HDR, upscaling, ilustrasi, dan render 3D memiliki fitur statistik "
        "yang mirip dengan gambar yang dihasilkan AI. Skor ini adalah probabilitas, bukan bukti; "
        "positif palsu bisa terjadi."
    ),
    "faq.offline.question": "Bisakah saya menjalankannya secara offline?",
    "faq.offline.answer_html": (
        "Ya. Setelah menjalankan pertama kali dan mengunduh model ke cache Hugging Face, picai yang "
        "di-self-host tidak memerlukan akses jaringan."
    ),
    "faq.rate_limit.question": "Apakah ada batas laju penggunaan pada instans hosting?",
    "faq.rate_limit.answer_html": (
        "Ya: 10 analisis per IP klien dalam jendela bergulir 24 jam mana pun. Respons membawa "
        "header <code>X-RateLimit-Remaining</code>, dan permintaan yang melebihi batas akan "
        "mengembalikan status 429 dengan header <code>Retry-After</code>."
    ),
    # Navigation
    "nav.detector": "Detektor",
    "nav.how_it_works": "Cara kerja",
    "nav.how-to-tell-if-an-image-is-ai-generated": "Panduan",
    "nav.api": "API",
    "nav.self-host": "Self-host",
    # Footer
    "footer.remove-image-metadata": "Hapus metadata",
    "footer.c2pa": "C2PA",
    "footer.faq": "FAQ",
    "footer.privacy": "Privasi",
    "footer.self-host": "Self-host",
    "footer.about": "Tentang",
    # UI strings
    "ui.nav_aria_label": "Navigasi utama",
    "ui.loading_status": "Memuat detektor…",
    "ui.hero_overline": "— Forensik gambar AI sumber terbuka",
    "ui.hero_heading_line1": "Apakah foto ini asli?",
    "ui.hero_heading_line2": "Dapatkan skor dan buktinya.",
    "ui.tool_aria_label": "Detektor gambar AI",
    "ui.dropzone_aria_label": "Unggah gambar untuk dianalisis",
    "ui.dropzone_title_fine": "Seret & lepas sebuah foto",
    "ui.dropzone_title_coarse": "Periksa sebuah foto",
    "ui.dropzone_sub_fine": "atau tempel dari clipboard, atau",
    "ui.dropzone_sub_coarse": "dari galeri atau kamera Anda",
    "ui.btn_check_image_fine": "Periksa gambar ini",
    "ui.btn_choose_photo_coarse": "Pilih foto",
    "ui.btn_take_photo": "Ambil foto",
    "ui.dismiss_aria_label": "Tutup",
    "ui.analyzing_prefix": "Menganalisis",
    "ui.analyzing_suffix": "· piksel · blok metadata",
    "ui.verdict_overline": "— Vonis",
    "ui.meter_real": "Asli",
    "ui.meter_uncertain": "Tidak pasti",
    "ui.meter_ai": "AI",
    "ui.model_label": "Model",
    "ui.verdict_disclaimer_html": (
        "Hasil adalah probabilitas dari sebuah pengklasifikasi, bukan vonis. "
        '<a href="/how-accurate">Cara membaca skor.</a>'
    ),
    "ui.btn_check_another": "Periksa gambar lain",
    "ui.preview_overline": "— Pratinjau",
    "ui.preview_alt": "Pratinjau gambar yang diunggah",
    "ui.metadata_overline": "— Metadata",
    "ui.metadata_heading": "Ditemukan dalam file.",
    "ui.jpeg_segments_label": "Segmen JPEG",
    "ui.btn_download_clean": "Unduh salinan bersih",
    "ui.metadata_scrub_note_html": (
        "Di-render ulang dari piksel, sehingga setiap blok di atas telah hilang. "
        '<a href="/remove-image-metadata">Cara kerjanya</a>'
    ),
    "ui.how_it_works_overline": "— Cara kerja",
    "ui.how_it_works_heading": "Tiga langkah. Tidak ada yang disimpan.",
    "ui.how_it_works_links_html": (
        '<a href="/how-to-tell-if-an-image-is-ai-generated">Baca panduan mengenali gambar AI</a> '
        'atau <a href="/self-host">jalankan di komputer Anda sendiri</a>.'
    ),
    "ui.faq_overline": "— FAQ",
    "ui.faq_heading": "Sebelum Anda bertanya.",
    "ui.faq_more_link": "Lebih banyak pertanyaan dan jawaban →",
    "ui.footer_tagline": "picai. · sumber terbuka",
    "ui.footer_detector_label": "Detektor:",
    "ui.breadcrumb_aria_label": "Remah roti",
    "ui.last_updated_prefix": "Terakhir diperbarui",
    "ui.source_on_github": "kode sumber di GitHub",
    "ui.btn_try_detector": "Coba detektornya",
    "ui.status_ready": "Detektor siap",
    "ui.status_unreachable": "Server tidak dapat dijangkau",
    "ui.loading_model_note": "Memuat model detektor (jalan pertama mengunduh ~750 MB)…",
    "ui.error_empty_file": "File tersebut kosong.",
    "ui.error_file_too_large": "{name} berukuran {size} — batasnya adalah 50 MB.",
    "ui.error_server_unreachable": "Tidak dapat menjangkau server: {message}",
    "ui.verdict_ai": "Kemungkinan besar dihasilkan AI",
    "ui.verdict_real": "Kemungkinan besar foto asli",
    "ui.verdict_uncertain": "Tidak pasti",
    "ui.confidence_suffix": "keyakinan",
    "ui.format_unknown": "tidak diketahui",
    "ui.metadata_present": "Ada",
    "ui.metadata_not_present": "Tidak ada",
    "ui.no_jpeg_segments": "Tidak ada segmen APP JPEG",
    "ui.quota_remaining": "{remaining} dari {limit} analisis tersisa hari ini",
}
