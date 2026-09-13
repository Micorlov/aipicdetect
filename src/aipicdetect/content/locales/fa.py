"""Persian translation table. Falls back to English (see aipicdetect.content.locales) for
any key missing here, so this file only needs to define what has actually been translated.

Text is written as plain right-to-left prose; no directional markup is added here because the
page itself sets dir="rtl" for this locale.
"""

from __future__ import annotations

STRINGS: dict[str, str] = {
    # Page metadata
    "page.home.title": "AiPicDetect — تشخیص‌گر تصاویر هوش مصنوعی و پاک‌کننده متادیتای متن‌باز",
    "page.home.description": (
        "با AiPicDetect بررسی کنید که آیا یک تصویر توسط هوش مصنوعی تولید شده است یا نه؛ این یک "
        "تشخیص‌گر رایگان و متن‌باز است. آن را در مرورگر استفاده کنید یا با Docker یا Python روی "
        "دستگاه خودتان اجرا کنید."
    ),
    "page.home.h1": "آیا این عکس واقعی است؟ امتیاز و مدرک را دریافت کنید.",
    "page.faq.title": "سوالات متداول تشخیص‌گر تصاویر هوش مصنوعی: دقت، حریم خصوصی، فرمت‌ها، مدل‌ها",
    "page.faq.description": (
        "پاسخ به سوالات متداول درباره‌ی AiPicDetect: تشخیص تصاویر هوش مصنوعی چقدر دقیق است، تصویر شما "
        "کجا پردازش می‌شود، چه فرمت‌هایی پشتیبانی می‌شوند، تعویض مدل و محدودیت نرخ استفاده."
    ),
    "page.faq.h1": "سوالات متداول AiPicDetect",
    "page.faq.intro_suffix": (
        "این‌ها سوالاتی هستند که مردم بیشتر از همه درباره‌ی نحوه‌ی کارکرد، میزان دقت و سرنوشت "
        "تصاویری که آپلود می‌کنند می‌پرسند."
    ),
    "page.faq.still_unsure_html": (
        'هنوز مطمئن نیستید؟ در <a href="https://github.com/Micorlov/aipicdetect/issues" '
        'rel="noopener">GitHub</a> یک issue باز کنید.'
    ),
    # Home page copy
    "home.entity_sentence": (
        "AiPicDetect یک ابزار رایگان و متن‌باز است که تصاویر تولیدشده با هوش مصنوعی را امتیازدهی "
        "می‌کند و متادیتای پنهان را حذف می‌کند — چه به‌صورت میزبانی‌شده و چه با میزبانی شخصی، "
        "انتخاب با شماست."
    ),
    "home.lead": (
        "AiPicDetect یک مدل باز تشخیص هوش مصنوعی اجرا می‌کند و تمام فیلدهای EXIF، C2PA و IPTC موجود در "
        "یک عکس را می‌خواند — سپس یک نسخه‌ی پاک به شما می‌دهد که همه‌ی این‌ها از آن حذف شده است. "
        "بدون ثبت‌نام، بدون جعبه‌ی سیاه."
    ),
    "home.dropzone_note": (
        "JPEG، PNG، WebP، HEIC · تا 50 MB · در حافظه پردازش می‌شود و هرگز روی دیسک نوشته نمی‌شود"
    ),
    "home.summary": (
        "AiPicDetect یک ابزار رایگان و متن‌باز است که تصاویر تولیدشده با هوش مصنوعی را امتیازدهی "
        "می‌کند و متادیتای پنهان را حذف می‌کند — چه به‌صورت میزبانی‌شده و چه با میزبانی شخصی، "
        "انتخاب با شماست. این ابزار با استفاده از یک طبقه‌بند باز Hugging Face، احتمال تولید یک "
        "تصویر توسط مولد هوش مصنوعی را برآورد می‌کند و می‌تواند تصاویر را بازپردازی کند تا "
        "متادیتای EXIF، XMP، IPTC، ICC و C2PA حذف شود. از نمونه‌ی میزبانی‌شده استفاده کنید یا با "
        "Docker یا Python میزبانی شخصی انجام دهید."
    ),
    "home.stat.0": "مدل باز،<br>بدون API شخص ثالث",
    "home.stat.1": "بدون نیاز<br>به ثبت‌نام",
    "home.stat.2": "MB حداکثر<br>آپلود",
    # Detect steps
    "steps.detect.upload.name": "آپلود.",
    "steps.detect.detect.name": "تشخیص.",
    "steps.detect.decide.name": "تصمیم.",
    "steps.detect.upload.text": (
        "یک عکس را رها کنید، جای‌گذاری کنید یا انتخاب کنید. این عکس به سروری از AiPicDetect که استفاده "
        "می‌کنید فرستاده می‌شود (در حالت میزبانی شخصی، دستگاه خودتان)، در حافظه نگه‌داری می‌شود و "
        "هرگز روی دیسک نوشته نمی‌شود."
    ),
    "steps.detect.detect.text": (
        "یک طبقه‌بند تصویر متن‌باز احتمال تولید پیکسل‌ها توسط یک مولد را برآورد می‌کند."
    ),
    "steps.detect.decide.text": (
        "شما یک احتمال هوش مصنوعی بودن، یک بازه‌ی اطمینان و بلوک‌های متادیتایی که فایل حمل "
        "می‌کند دریافت می‌کنید — به‌عنوان یک احتمال، نه یک حکم قطعی."
    ),
    # Scrub steps — <code> blocks contain literal shell commands and must stay untranslated
    "steps.scrub.inspect.name": "بازرسی.",
    "steps.scrub.scrub.name": "پاک‌سازی.",
    "steps.scrub.verify.name": "تأیید.",
    "steps.scrub.inspect.text": (
        "برای فهرست کردن بلوک‌های EXIF، XMP، IPTC، C2PA و ICC که فایل حمل می‌کند، دستور "
        "<code>aipicdetect inspect photo.jpg</code> را اجرا کنید."
    ),
    "steps.scrub.scrub.text": (
        "دستور <code>aipicdetect scrub photo.jpg</code> (یا <code>POST /scrub</code>) را اجرا کنید. "
        "AiPicDetect پیکسل‌ها را رمزگشایی می‌کند، جهت EXIF را اعمال می‌کند و یک تصویر کاملاً جدید از "
        "بافر خام پیکسل می‌سازد."
    ),
    "steps.scrub.verify.text": (
        "دستور <code>aipicdetect inspect photo.clean.jpg</code> را اجرا کنید؛ باید عبارت "
        "“no metadata signatures found” را چاپ کند."
    ),
    # FAQ (home slugs)
    "faq.accuracy.question": "این تشخیص‌گر چقدر دقیق است؟",
    "faq.accuracy.answer_html": (
        "این ابزار یک احتمال گزارش می‌دهد، نه یک حکم قطعی. امتیازهای نزدیک به 50% با برچسب "
        "<em>نامشخص</em> مشخص می‌شوند؛ با هر نتیجه‌ی مجزا به‌عنوان یک نشانه رفتار کنید و آن را با "
        'شواهد دیگر ترکیب کنید. درباره‌ی <a href="/how-accurate">دقت تشخیص‌گرهای تصاویر هوش '
        "مصنوعی</a> بیشتر بخوانید."
    ),
    "faq.leaves_computer.question": "آیا تصویر من از کامپیوترم خارج می‌شود؟",
    "faq.leaves_computer.answer_html": (
        "در این نمونه‌ی عمومی، بله: عکس به سرور AiPicDetect (یک کانتینر Google Cloud Run که توسط "
        "نویسنده اجرا می‌شود) آپلود می‌شود، در حافظه امتیازدهی می‌شود و هرگز روی دیسک نوشته "
        "نمی‌شود. نسخه‌ی پاک‌شده فقط تا زمانی در حافظه نگه‌داری می‌شود که 100 نتیجه‌ی جدیدتر جای "
        "آن را بگیرد یا کانتینر مجدداً راه‌اندازی شود، و هیچ‌چیز به هیچ API شخص ثالثی ارسال "
        'نمی‌شود. اگر می‌خواهید چیزی از دستگاه شما خارج نشود، با یک دستور Docker '
        '<a href="/self-host">AiPicDetect را خودتان اجرا کنید</a>. جزئیات در <a href="/privacy">'
        "صفحه‌ی حریم خصوصی</a> موجود است."
    ),
    "faq.open_source.question": "آیا این متن‌باز است؟",
    "faq.open_source.answer_html": (
        "بله. کد، ایمیج Docker، ابزار خط فرمان (CLI) و GitHub Action همگی در "
        '<a href="https://github.com/Micorlov/aipicdetect" rel="noopener">مخزن AiPicDetect</a> تحت مجوز MIT '
        "موجودند. تشخیص‌گر یک مدل باز Hugging Face است که می‌توانید آن را بررسی یا جایگزین کنید."
    ),
    "faq.remove_metadata.question": "آیا می‌توانم C2PA و سایر متادیتاها را حذف کنم؟",
    "faq.remove_metadata.answer_html": (
        "بله. پس از بررسی یک عکس، از گزینه‌ی <em>دانلود نسخه‌ی پاک</em> استفاده کنید. AiPicDetect "
        "تصویر را از پیکسل‌های آن بازسازی می‌کند، بنابراین EXIF، XMP، IPTC، C2PA و پروفایل ICC "
        'همگی حذف می‌شوند. <a href="/remove-image-metadata">پاک‌کننده چگونه کار می‌کند</a>.'
    ),
    "faq.formats.question": "چه فرمت‌هایی پشتیبانی می‌شوند؟",
    "faq.formats.answer_html": (
        "JPEG، PNG، WebP، HEIC/HEIF و اکثر فرمت‌هایی که Pillow می‌تواند رمزگشایی کند، تا 50 MB."
    ),
    "faq.why_metadata.question": "چرا متادیتا نمایش داده می‌شود؟",
    "faq.why_metadata.answer_html": (
        "اعتبارنامه‌های محتوای C2PA و برچسب‌های نرم‌افزار ویرایش، نشانه‌هایی از منشأ تصویر "
        "هستند. این پنل نشان می‌دهد فایل کدام بلوک‌ها (EXIF، XMP، IPTC، C2PA، ICC) را حمل "
        'می‌کند تا بتوانید آن‌ها را در کنار امتیاز بسنجید. <a href="/c2pa">اعتبارنامه‌های محتوای '
        'C2PA</a> و <a href="/remove-image-metadata">نحوه‌ی حذف متادیتای تصویر</a> را ببینید.'
    ),
    "faq.different_model.question": "آیا می‌توانم از مدل دیگری استفاده کنم؟",
    "faq.different_model.answer_html": (
        "بله. متغیر <code>PICAI_DETECTOR_MODEL</code> را روی هر مدل طبقه‌بندی تصویر Hugging Face "
        "که برچسب‌های آن محتوای هوش مصنوعی/جعلی را در برابر انسانی/واقعی نام‌گذاری می‌کند، تنظیم "
        "کنید."
    ),
    # FAQ (more slugs)
    "faq.free.question": "آیا AiPicDetect رایگان است؟",
    "faq.free.answer_html": (
        "بله. AiPicDetect تحت مجوز MIT متن‌باز است. نمونه‌ی میزبانی‌شده رایگان است اما محدودیتی معادل "
        "10 تحلیل به ازای هر آدرس IP در هر 24 ساعت دارد؛ نسخه‌ی میزبانی‌شده‌ی شخصی هیچ محدودیتی "
        "ندارد."
    ),
    "faq.screenshots.question": "آیا روی اسکرین‌شات‌ها یا تصاویر بسیار فشرده‌شده کار می‌کند؟",
    "faq.screenshots.answer_html": (
        "این کار می‌کند، اما رمزگذاری مجدد، تغییر اندازه و گرفتن اسکرین‌شات برخی از ردپاهای سطح "
        "پیکسل را که طبقه‌بند به آن‌ها متکی است حذف می‌کند، پس انتظار اطمینان کمتر و نتایج "
        "<em>نامشخص</em> بیشتری داشته باشید."
    ),
    "faq.which_generator.question": (
        "آیا می‌تواند تشخیص دهد کدام مولد یک تصویر را ساخته است (Midjourney، DALL·E، Stable "
        "Diffusion)؟"
    ),
    "faq.which_generator.answer_html": (
        "خیر. AiPicDetect به‌طور کلی آمار پیکسل‌های تولیدشده در برابر واقعی را امتیازدهی می‌کند؛ این "
        "ابزار مولد را شناسایی نمی‌کند و هیچ اطلاعی از مولدهایی که پس از جمع‌آوری داده‌های "
        "آموزشی مدل آن منتشر شده‌اند، ندارد."
    ),
    "faq.false_positive.question": "چرا یک عکس واقعی امتیاز هوش مصنوعی گرفت؟",
    "faq.false_positive.answer_html": (
        "فیلترهای سنگین، پردازش HDR، بزرگ‌نمایی (آپ‌اسکیل)، تصویرسازی‌ها و رندرهای سه‌بعدی "
        "ویژگی‌های آماری مشترکی با تصاویر تولیدشده دارند. این امتیاز یک احتمال است، نه اثبات؛ "
        "نتایج مثبت کاذب رخ می‌دهند."
    ),
    "faq.offline.question": "آیا می‌توانم آن را آفلاین اجرا کنم؟",
    "faq.offline.answer_html": (
        "بله. پس از اینکه اجرای اول مدل را در کش Hugging Face دانلود کرد، یک AiPicDetect با میزبانی "
        "شخصی به هیچ دسترسی شبکه‌ای نیاز ندارد."
    ),
    "faq.rate_limit.question": "آیا در نمونه‌ی میزبانی‌شده محدودیت نرخ استفاده وجود دارد؟",
    "faq.rate_limit.answer_html": (
        "بله: 10 تحلیل به ازای هر IP کلاینت در هر بازه‌ی 24 ساعته‌ی متحرک. پاسخ‌ها هدر "
        "<code>X-RateLimit-Remaining</code> را حمل می‌کنند و درخواستی که از این محدودیت فراتر "
        "رود، وضعیت 429 را همراه با هدر <code>Retry-After</code> برمی‌گرداند."
    ),
    # Navigation
    "nav.detector": "تشخیص‌گر",
    "nav.how_it_works": "نحوه‌ی کارکرد",
    "nav.how-to-tell-if-an-image-is-ai-generated": "راهنما",
    "nav.api": "API",
    "nav.self-host": "میزبانی شخصی",
    # Footer
    "footer.remove-image-metadata": "حذف متادیتا",
    "footer.c2pa": "C2PA",
    "footer.faq": "سوالات متداول",
    "footer.privacy": "حریم خصوصی",
    "footer.self-host": "میزبانی شخصی",
    "footer.about": "درباره",
    # UI strings
    "ui.nav_aria_label": "ناوبری اصلی",
    "ui.loading_status": "در حال بارگذاری تشخیص‌گر…",
    "ui.hero_overline": "— فارنزیک متن‌باز تصاویر هوش مصنوعی",
    "ui.hero_heading_line1": "آیا این عکس واقعی است؟",
    "ui.hero_heading_line2": "امتیاز و مدرک را دریافت کنید.",
    "ui.tool_aria_label": "تشخیص‌گر تصاویر هوش مصنوعی",
    "ui.dropzone_aria_label": "برای تحلیل، یک تصویر آپلود کنید",
    "ui.dropzone_title_fine": "یک عکس را بکشید و رها کنید",
    "ui.dropzone_title_coarse": "یک عکس را بررسی کنید",
    "ui.dropzone_sub_fine": "یا از کلیپ‌بورد جای‌گذاری کنید، یا",
    "ui.dropzone_sub_coarse": "از گالری یا دوربین خود",
    "ui.btn_check_image_fine": "این تصویر را بررسی کنید",
    "ui.btn_choose_photo_coarse": "انتخاب عکس",
    "ui.btn_take_photo": "گرفتن عکس",
    "ui.dismiss_aria_label": "بستن",
    "ui.analyzing_prefix": "در حال تحلیل",
    "ui.analyzing_suffix": "· پیکسل‌ها · بلوک‌های متادیتا",
    "ui.verdict_overline": "— نتیجه",
    "ui.meter_real": "واقعی",
    "ui.meter_uncertain": "نامشخص",
    "ui.meter_ai": "هوش مصنوعی",
    "ui.model_label": "مدل",
    "ui.verdict_disclaimer_html": (
        "نتایج، احتمالاتی از یک طبقه‌بند هستند، نه احکام قطعی. "
        '<a href="/how-accurate">نحوه‌ی خواندن امتیاز.</a>'
    ),
    "ui.btn_check_another": "بررسی تصویر دیگر",
    "ui.preview_overline": "— پیش‌نمایش",
    "ui.preview_alt": "پیش‌نمایش تصویر آپلودشده",
    "ui.metadata_overline": "— متادیتا",
    "ui.metadata_heading": "در فایل یافت شد.",
    "ui.jpeg_segments_label": "بخش‌های JPEG",
    "ui.btn_download_clean": "دانلود نسخه‌ی پاک",
    "ui.metadata_scrub_note_html": (
        "از روی پیکسل‌ها بازسازی شده، بنابراین تمام بلوک‌های بالا حذف شده‌اند. "
        '<a href="/remove-image-metadata">نحوه‌ی کارکرد</a>'
    ),
    "ui.how_it_works_overline": "— نحوه‌ی کارکرد",
    "ui.how_it_works_heading": "سه مرحله. هیچ‌چیز ذخیره نمی‌شود.",
    "ui.how_it_works_links_html": (
        '<a href="/how-to-tell-if-an-image-is-ai-generated">راهنمای تشخیص تصاویر هوش مصنوعی را '
        'بخوانید</a> یا <a href="/self-host">آن را روی دستگاه خودتان اجرا کنید</a>.'
    ),
    "ui.faq_overline": "— سوالات متداول",
    "ui.faq_heading": "قبل از اینکه بپرسید.",
    "ui.faq_more_link": "سوالات و پاسخ‌های بیشتر →",
    "ui.footer_tagline": "AiPicDetect. · متن‌باز",
    "ui.footer_detector_label": "تشخیص‌گر:",
    "ui.breadcrumb_aria_label": "مسیر ناوبری",
    "ui.last_updated_prefix": "آخرین به‌روزرسانی",
    "ui.source_on_github": "کد منبع در GitHub",
    "ui.btn_try_detector": "تشخیص‌گر را امتحان کنید",
    "ui.status_ready": "تشخیص‌گر آماده است",
    "ui.status_unreachable": "دسترسی به سرور ممکن نیست",
    "ui.loading_model_note": "در حال بارگذاری مدل تشخیص‌گر (اجرای اول حدود 750 MB دانلود می‌کند)…",
    "ui.error_empty_file": "این فایل خالی است.",
    "ui.error_file_too_large": "{name} برابر با {size} است — محدودیت 50 MB است.",
    "ui.error_server_unreachable": "امکان اتصال به سرور نبود: {message}",
    "ui.verdict_ai": "احتمالاً تولیدشده با هوش مصنوعی",
    "ui.verdict_real": "احتمالاً یک عکس واقعی",
    "ui.verdict_uncertain": "نامشخص",
    "ui.confidence_suffix": "اطمینان",
    "ui.format_unknown": "ناشناخته",
    "ui.metadata_present": "موجود",
    "ui.metadata_not_present": "موجود نیست",
    "ui.no_jpeg_segments": "بدون بخش‌های APP در JPEG",
    "ui.quota_remaining": "امروز {remaining} تحلیل از {limit} باقی مانده است",
}
