"""Turkish translation table.

Falls back to English (see :func:`aipicdetect.content.locales.t`) for any key not defined here, but
every key from :mod:`aipicdetect.content.locales.en` is translated below.
"""

from __future__ import annotations

STRINGS: dict[str, str] = {
    # Page metadata
    "page.home.title": "AiPicDetect — Açık Kaynaklı Yapay Zeka Görsel Dedektörü ve Metadata Temizleyici",
    "page.home.description": (
        "AiPicDetect ile bir görselin yapay zeka tarafından üretilip üretilmediğini kontrol edin — "
        "ücretsiz, açık kaynaklı bir dedektör. Tarayıcıda kullanın veya Docker ya da Python ile "
        "kendi makinenizde çalıştırın."
    ),
    "page.home.h1": "Bu fotoğraf gerçek mi? Puanı ve kanıtı görün.",
    "page.faq.title": "Yapay Zeka Görsel Dedektörü SSS: Doğruluk, Gizlilik, Formatlar, Modeller",
    "page.faq.description": (
        "AiPicDetect hakkında sık sorulan sorular: yapay zeka görsel tespitinin doğruluğu, görselinizin "
        "nerede işlendiği, desteklenen formatlar, model değiştirme ve istek limitleri."
    ),
    "page.faq.h1": "AiPicDetect sıkça sorulan sorular",
    "page.faq.intro_suffix": (
        "Bunlar, aracın nasıl çalıştığı, ne kadar doğru olduğu ve yüklenen görsellere ne olduğu "
        "hakkında en çok sorulan sorular."
    ),
    "page.faq.still_unsure_html": (
        'Hâlâ emin değil misiniz? <a href="https://github.com/Micorlov/aipicdetect/issues" '
        'rel="noopener">GitHub</a> üzerinde bir issue açın.'
    ),
    # Home page copy
    "home.entity_sentence": (
        "AiPicDetect, yapay zeka tarafından üretilen görselleri puanlayan ve gizli metadata'yı temizleyen "
        "ücretsiz, açık kaynaklı bir araçtır — barındırılan ya da kendi sunucunuzda, tercih sizin."
    ),
    "home.lead": (
        "AiPicDetect, açık kaynaklı bir yapay zeka tespit modeli çalıştırır ve bir fotoğrafın taşıdığı her "
        "EXIF, C2PA ve IPTC alanını okur — ardından hepsi temizlenmiş hâlde size temiz bir kopya "
        "sunar. Kayıt yok, kara kutu yok."
    ),
    "home.dropzone_note": (
        "JPEG, PNG, WebP, HEIC · 50 MB'a kadar · bellekte işlenir, diske asla yazılmaz"
    ),
    "home.summary": (
        "AiPicDetect, yapay zeka tarafından üretilen görselleri puanlayan ve gizli metadata'yı temizleyen "
        "ücretsiz, açık kaynaklı bir araçtır — barındırılan ya da kendi sunucunuzda, tercih sizin. "
        "Açık bir Hugging Face sınıflandırıcısı kullanarak bir görselin yapay zeka üretici tarafından "
        "oluşturulma olasılığını puanlar ve EXIF, XMP, IPTC, ICC ve C2PA metadata'sını temizlemek "
        "için görselleri yeniden oluşturabilir. Barındırılan sürümü kullanın ya da Docker veya "
        "Python ile kendi sunucunuzda çalıştırın."
    ),
    "home.stat.0": "açık model,<br>üçüncü taraf API yok",
    "home.stat.1": "kayıt<br>gerekmiyor",
    "home.stat.2": "MB azami<br>yükleme boyutu",
    # Detect steps
    "steps.detect.upload.name": "Yükleyin.",
    "steps.detect.upload.text": (
        "Bir görseli sürükleyip bırakın, yapıştırın veya seçin. Kullandığınız AiPicDetect sunucusuna "
        "gönderilir (kendi sunucunuzda çalıştırıyorsanız kendi makinenize), bellekte tutulur ve "
        "diske asla yazılmaz."
    ),
    "steps.detect.detect.name": "Tespit edin.",
    "steps.detect.detect.text": (
        "Açık kaynaklı bir görsel sınıflandırıcı, piksellerin bir üretici tarafından oluşturulma "
        "olasılığını puanlar."
    ),
    "steps.detect.decide.name": "Karar verin.",
    "steps.detect.decide.text": (
        "Bir yapay zeka olasılığı, bir güven aralığı ve dosyanın taşıdığı metadata bloklarını "
        "alırsınız — bir kanıt değil, bir olasılık olarak."
    ),
    # Scrub steps — <code> blocks contain literal shell commands and must stay untranslated
    "steps.scrub.inspect.name": "İnceleyin.",
    "steps.scrub.inspect.text": (
        "Dosyanın taşıdığı EXIF, XMP, IPTC, C2PA ve ICC bloklarını listelemek için "
        "<code>aipicdetect inspect photo.jpg</code> komutunu çalıştırın."
    ),
    "steps.scrub.scrub.name": "Temizleyin.",
    "steps.scrub.scrub.text": (
        "<code>aipicdetect scrub photo.jpg</code> (veya <code>POST /scrub</code>) komutunu çalıştırın. "
        "AiPicDetect pikselleri çözer, EXIF yönünü uygular ve ham piksel arabelleğinden bambaşka yeni bir "
        "görsel oluşturur."
    ),
    "steps.scrub.verify.name": "Doğrulayın.",
    "steps.scrub.verify.text": (
        "<code>aipicdetect inspect photo.clean.jpg</code> komutunu çalıştırın; “no metadata signatures found” yazdırmalıdır."
    ),
    # FAQ (home slugs)
    "faq.accuracy.question": "Dedektör ne kadar doğru?",
    "faq.accuracy.answer_html": (
        "Bu bir hüküm değil, bir olasılık bildirir. %50'ye yakın puanlar <em>Belirsiz</em> olarak "
        "etiketlenir; tek bir sonucu bir sinyal olarak değerlendirin ve diğer kanıtlarla birlikte "
        'yorumlayın. Daha fazla bilgi için <a href="/how-accurate">yapay zeka görsel '
        "dedektörlerinin ne kadar doğru olduğu</a> sayfasına bakın."
    ),
    "faq.leaves_computer.question": "Görselim bilgisayarımdan çıkıyor mu?",
    "faq.leaves_computer.answer_html": (
        "Bu genel kullanıma açık örnekte evet: görsel AiPicDetect sunucusuna (yazar tarafından işletilen "
        "bir Google Cloud Run konteynerine) yüklenir, bellekte puanlanır ve diske asla yazılmaz. "
        "Temizlenmiş kopya, yerini 100 daha yeni sonuç alana ya da konteyner yeniden başlayana "
        "kadar yalnızca bellekte tutulur ve hiçbir şey üçüncü taraf bir API'ye gönderilmez. "
        'Makinenizden hiçbir şeyin çıkmasını istemiyorsanız, tek bir Docker komutuyla '
        '<a href="/self-host">AiPicDetect\'yi kendiniz çalıştırın</a>. Ayrıntılar '
        '<a href="/privacy">gizlilik sayfasında</a>.'
    ),
    "faq.open_source.question": "Bu açık kaynaklı bir proje mi?",
    "faq.open_source.answer_html": (
        "Evet. Kod, Docker imajı, CLI ve GitHub Action, MIT lisansı altında "
        '<a href="https://github.com/Micorlov/aipicdetect" rel="noopener">AiPicDetect deposunda</a> yer alır. '
        "Dedektör, inceleyebileceğiniz veya değiştirebileceğiniz açık bir Hugging Face modelidir."
    ),
    "faq.remove_metadata.question": "C2PA ve diğer metadata'ları kaldırabilir miyim?",
    "faq.remove_metadata.answer_html": (
        "Evet. Bir görseli kontrol ettikten sonra <em>Temiz kopyayı indir</em> seçeneğini kullanın. "
        "AiPicDetect, görseli piksellerinden yeniden oluşturur; böylece EXIF, XMP, IPTC, C2PA ve ICC "
        'profili tamamen geride bırakılır. <a href="/remove-image-metadata">Temizleyici nasıl '
        "çalışır</a>."
    ),
    "faq.formats.question": "Hangi formatlar destekleniyor?",
    "faq.formats.answer_html": (
        "JPEG, PNG, WebP, HEIC/HEIF ve Pillow'un çözebildiği çoğu format, 50 MB'a kadar."
    ),
    "faq.why_metadata.question": "Metadata neden listeleniyor?",
    "faq.why_metadata.answer_html": (
        "C2PA içerik kimlik bilgileri ve düzenleme yazılımı etiketleri, kaynağa dair ipuçlarıdır. "
        "Panel, dosyanın hangi blokları (EXIF, XMP, IPTC, C2PA, ICC) taşıdığını gösterir, böylece "
        'bunları puanla birlikte değerlendirebilirsiniz. <a href="/c2pa">C2PA içerik kimlik '
        'bilgilerine</a> ve <a href="/remove-image-metadata">görsel metadata\'sının nasıl '
        "kaldırılacağına</a> bakın."
    ),
    "faq.different_model.question": "Farklı bir model kullanabilir miyim?",
    "faq.different_model.answer_html": (
        "Evet. Etiketleri yapay zeka/sahte ile insan/gerçek içeriği ayıran herhangi bir Hugging "
        "Face görsel sınıflandırma modelini <code>PICAI_DETECTOR_MODEL</code> olarak ayarlayın."
    ),
    # FAQ (more slugs)
    "faq.free.question": "AiPicDetect ücretsiz mi?",
    "faq.free.answer_html": (
        "Evet. AiPicDetect, MIT lisansı altında açık kaynaklıdır. Barındırılan sürüm, IP adresi başına "
        "her 24 saatte 10 analiz sınırıyla ücretsiz kullanılabilir; kendi sunucunuzda çalıştırılan "
        "kopyada sınır yoktur."
    ),
    "faq.screenshots.question": "Ekran görüntülerinde veya yoğun sıkıştırılmış görsellerde çalışır mı?",
    "faq.screenshots.answer_html": (
        "Çalışır, ancak yeniden kodlama, yeniden boyutlandırma ve ekran görüntüsü alma, "
        "sınıflandırıcının dayandığı piksel düzeyindeki izlerin bir kısmını ortadan kaldırır; bu "
        "nedenle daha düşük güven ve daha fazla <em>Belirsiz</em> sonuç bekleyin."
    ),
    "faq.which_generator.question": (
        "Bir görseli hangi üreticinin oluşturduğunu (Midjourney, DALL·E, Stable Diffusion) "
        "söyleyebilir mi?"
    ),
    "faq.which_generator.answer_html": (
        "Hayır. AiPicDetect, genel olarak üretilmiş ile gerçek piksel istatistiklerini puanlar; belirli "
        "üreticiyi tanımlamaz ve modelinin eğitim verisi toplandıktan sonra piyasaya sürülen "
        "üreticiler hakkında hiçbir bilgisi yoktur."
    ),
    "faq.false_positive.question": "Gerçek bir fotoğraf neden yapay zeka olarak puanlandı?",
    "faq.false_positive.answer_html": (
        "Ağır filtreler, HDR işleme, büyütme, illüstrasyonlar ve 3D render'lar, üretilen görsellerle "
        "benzer istatistiksel özellikler taşır. Puan bir olasılıktır, kanıt değildir; yanlış "
        "pozitifler olabilir."
    ),
    "faq.offline.question": "Çevrimdışı kullanabilir miyim?",
    "faq.offline.answer_html": (
        "Evet. İlk çalıştırma modeli Hugging Face önbelleğine indirdikten sonra, kendi sunucunuzda "
        "çalıştırılan bir AiPicDetect ağ erişimine ihtiyaç duymaz."
    ),
    "faq.rate_limit.question": "Barındırılan sürümde bir istek sınırı var mı?",
    "faq.rate_limit.answer_html": (
        "Evet: herhangi bir kayan 24 saatlik pencerede istemci IP'si başına 10 analiz. Yanıtlar "
        "<code>X-RateLimit-Remaining</code> başlığını taşır ve sınırı aşan bir istek, "
        "<code>Retry-After</code> başlığıyla 429 döndürür."
    ),
    # Navigation
    "nav.detector": "Dedektör",
    "nav.how_it_works": "Nasıl çalışır",
    "nav.how-to-tell-if-an-image-is-ai-generated": "Rehber",
    "nav.api": "API",
    "nav.self-host": "Kendi sunucunuzda",
    # Footer
    "footer.remove-image-metadata": "Metadata kaldır",
    "footer.c2pa": "C2PA",
    "footer.faq": "SSS",
    "footer.privacy": "Gizlilik",
    "footer.self-host": "Kendi sunucunuzda",
    "footer.about": "Hakkında",
    # UI strings
    "ui.nav_aria_label": "Ana gezinme",
    "ui.loading_status": "Dedektör yükleniyor…",
    "ui.hero_overline": "— Açık kaynaklı yapay zeka görsel adli analizi",
    "ui.hero_heading_line1": "Bu fotoğraf gerçek mi?",
    "ui.hero_heading_line2": "Puanı ve kanıtı görün.",
    "ui.tool_aria_label": "Yapay zeka görsel dedektörü",
    "ui.dropzone_aria_label": "Analiz için bir görsel yükleyin",
    "ui.dropzone_title_fine": "Bir fotoğrafı sürükleyip bırakın",
    "ui.dropzone_title_coarse": "Bir fotoğrafı kontrol edin",
    "ui.dropzone_sub_fine": "veya panodan yapıştırın, ya da",
    "ui.dropzone_sub_coarse": "kitaplığınızdan veya kameradan",
    "ui.btn_check_image_fine": "Bu görseli kontrol et",
    "ui.btn_choose_photo_coarse": "Fotoğraf seç",
    "ui.btn_take_photo": "Fotoğraf çek",
    "ui.dismiss_aria_label": "Kapat",
    "ui.analyzing_prefix": "Analiz ediliyor",
    "ui.analyzing_suffix": "· pikseller · metadata blokları",
    "ui.verdict_overline": "— Sonuç",
    "ui.meter_real": "Gerçek",
    "ui.meter_uncertain": "Belirsiz",
    "ui.meter_ai": "YZ",
    "ui.model_label": "Model",
    "ui.verdict_disclaimer_html": (
        "Sonuçlar bir sınıflandırıcının olasılıklarıdır, hüküm değildir. "
        '<a href="/how-accurate">Puan nasıl okunur.</a>'
    ),
    "ui.btn_check_another": "Başka bir görsel kontrol et",
    "ui.preview_overline": "— Önizleme",
    "ui.preview_alt": "Yüklenen görsel önizlemesi",
    "ui.metadata_overline": "— Metadata",
    "ui.metadata_heading": "Dosyada bulunanlar.",
    "ui.jpeg_segments_label": "JPEG segmentleri",
    "ui.btn_download_clean": "Temiz kopyayı indir",
    "ui.metadata_scrub_note_html": (
        "Piksellerden yeniden oluşturuldu, bu yüzden yukarıdaki her blok kayboldu. "
        '<a href="/remove-image-metadata">Nasıl çalışır</a>'
    ),
    "ui.how_it_works_overline": "— Nasıl çalışır",
    "ui.how_it_works_heading": "Üç adım. Hiçbir şey saklanmaz.",
    "ui.how_it_works_links_html": (
        '<a href="/how-to-tell-if-an-image-is-ai-generated">Yapay zeka görsellerini fark etme '
        'rehberini okuyun</a> ya da <a href="/self-host">kendi makinenizde çalıştırın</a>.'
    ),
    "ui.faq_overline": "— SSS",
    "ui.faq_heading": "Sormadan önce.",
    "ui.faq_more_link": "Daha fazla soru ve cevap →",
    "ui.footer_tagline": "AiPicDetect. · açık kaynak",
    "ui.footer_detector_label": "Dedektör:",
    "ui.breadcrumb_aria_label": "İçerik yolu",
    "ui.last_updated_prefix": "Son güncelleme",
    "ui.source_on_github": "GitHub'daki kaynak kod",
    "ui.btn_try_detector": "Dedektörü deneyin",
    "ui.status_ready": "Dedektör hazır",
    "ui.status_unreachable": "Sunucuya ulaşılamıyor",
    "ui.loading_model_note": "Dedektör modeli yükleniyor (ilk çalıştırma ~750 MB indirir)…",
    "ui.error_empty_file": "Bu dosya boş.",
    "ui.error_file_too_large": "{name} {size} boyutunda — sınır 50 MB.",
    "ui.error_server_unreachable": "Sunucuya ulaşılamadı: {message}",
    "ui.verdict_ai": "Muhtemelen yapay zeka tarafından üretilmiş",
    "ui.verdict_real": "Muhtemelen gerçek bir fotoğraf",
    "ui.verdict_uncertain": "Belirsiz",
    "ui.confidence_suffix": "güven",
    "ui.format_unknown": "bilinmiyor",
    "ui.metadata_present": "Mevcut",
    "ui.metadata_not_present": "Mevcut değil",
    "ui.no_jpeg_segments": "JPEG APP segmenti yok",
    "ui.quota_remaining": "Bugün için {limit} analizden {remaining} kaldı",
}
