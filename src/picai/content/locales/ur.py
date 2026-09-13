"""Urdu translation table. Falls back to English (see picai.content.locales) for
any key missing here, so this file only needs to define what has actually been translated.

Text is written as plain right-to-left prose; no directional markup is added here because the
page itself sets dir="rtl" for this locale.
"""

from __future__ import annotations

STRINGS: dict[str, str] = {
    # Page metadata
    "page.home.title": "picai — اوپن سورس AI امیج ڈیٹیکٹر اور میٹا ڈیٹا اسکربر",
    "page.home.description": (
        "picai کے ساتھ چیک کریں کہ آیا کوئی تصویر AI سے تیار کردہ ہے — یہ ایک مفت، اوپن سورس "
        "ڈیٹیکٹر ہے۔ اسے براؤزر میں استعمال کریں یا Docker یا Python کے ذریعے اپنی مشین پر چلائیں۔"
    ),
    "page.home.h1": "کیا یہ تصویر اصلی ہے؟ اسکور اور ثبوت حاصل کریں۔",
    "page.faq.title": "AI امیج ڈیٹیکٹر عمومی سوالات: درستگی، پرائیویسی، فارمیٹس، ماڈلز",
    "page.faq.description": (
        "picai کے بارے میں عام سوالات کے جوابات: AI امیج شناخت کتنی درست ہے، آپ کی تصویر کہاں "
        "پروسیس ہوتی ہے، کون سے فارمیٹس سپورٹڈ ہیں، ماڈل تبدیل کرنا اور ریٹ لمٹس۔"
    ),
    "page.faq.h1": "picai کے اکثر پوچھے جانے والے سوالات",
    "page.faq.intro_suffix": (
        "یہ وہ سوالات ہیں جو لوگ سب سے زیادہ پوچھتے ہیں — یہ کیسے کام کرتا ہے، کتنا درست ہے، اور "
        "اپ لوڈ کی گئی تصاویر کے ساتھ کیا ہوتا ہے۔"
    ),
    "page.faq.still_unsure_html": (
        'اب بھی غیر یقینی ہیں؟ <a href="https://github.com/Micorlov/picai/issues" '
        'rel="noopener">GitHub</a> پر ایک issue کھولیں۔'
    ),
    # Home page copy
    "home.entity_sentence": (
        "picai ایک مفت، اوپن سورس ٹول ہے جو اندازہ لگاتا ہے کہ کوئی تصویر AI سے بنائی گئی ہے یا "
        "نہیں اور پوشیدہ میٹا ڈیٹا ہٹا دیتا ہے — ہوسٹڈ استعمال کریں یا خود ہوسٹ کریں، انتخاب آپ کا "
        "ہے۔"
    ),
    "home.lead": (
        "picai ایک اوپن AI شناختی ماڈل چلاتا ہے اور تصویر میں موجود ہر EXIF، C2PA اور IPTC فیلڈ "
        "کو پڑھتا ہے — پھر آپ کو ایک صاف کاپی دیتا ہے جس سے یہ سب ہٹا دیا گیا ہو۔ نہ کوئی سائن اپ، "
        "نہ کوئی بلیک باکس۔"
    ),
    "home.dropzone_note": (
        "JPEG، PNG، WebP، HEIC · زیادہ سے زیادہ 50 MB تک · میموری میں پروسیس ہوتا ہے، کبھی ڈسک پر "
        "نہیں لکھا جاتا"
    ),
    "home.summary": (
        "picai ایک مفت، اوپن سورس ٹول ہے جو اندازہ لگاتا ہے کہ کوئی تصویر AI سے بنائی گئی ہے یا "
        "نہیں اور پوشیدہ میٹا ڈیٹا ہٹا دیتا ہے — ہوسٹڈ استعمال کریں یا خود ہوسٹ کریں، انتخاب آپ کا "
        "ہے۔ یہ ایک اوپن Hugging Face کلاسیفائر کے ذریعے اندازہ لگاتا ہے کہ تصویر کے AI جنریٹر سے "
        "بننے کا کتنا امکان ہے، اور EXIF، XMP، IPTC، ICC اور C2PA میٹا ڈیٹا ہٹانے کے لیے تصویر کو "
        "دوبارہ رینڈر کر سکتا ہے۔ ہوسٹڈ انسٹینس استعمال کریں یا Docker یا Python کے ساتھ خود ہوسٹ "
        "کریں۔"
    ),
    "home.stat.0": "اوپن ماڈل،<br>کوئی تھرڈ پارٹی API نہیں",
    "home.stat.1": "کسی سائن اپ کی<br>ضرورت نہیں",
    "home.stat.2": "MB زیادہ سے زیادہ<br>اپ لوڈ",
    # Detect steps
    "steps.detect.upload.name": "اپ لوڈ۔",
    "steps.detect.detect.name": "شناخت۔",
    "steps.detect.decide.name": "فیصلہ۔",
    "steps.detect.upload.text": (
        "کوئی تصویر ڈراپ کریں، پیسٹ کریں یا منتخب کریں۔ یہ اس picai سرور کو بھیجی جاتی ہے جو آپ "
        "استعمال کر رہے ہیں (خود ہوسٹ کرنے کی صورت میں آپ کی اپنی مشین)، میموری میں رکھی جاتی ہے "
        "اور کبھی ڈسک پر نہیں لکھی جاتی۔"
    ),
    "steps.detect.detect.text": (
        "ایک اوپن سورس امیج کلاسیفائر اندازہ لگاتا ہے کہ پکسلز کے کسی جنریٹر سے بننے کا کتنا امکان "
        "ہے۔"
    ),
    "steps.detect.decide.text": (
        "آپ کو AI کا امکان، ایک کانفیڈنس بینڈ، اور فائل میں موجود میٹا ڈیٹا بلاکس ملتے ہیں — بطور "
        "امکان، حتمی فیصلے کے طور پر نہیں۔"
    ),
    # Scrub steps — <code> blocks contain literal shell commands and must stay untranslated
    "steps.scrub.inspect.name": "معائنہ۔",
    "steps.scrub.scrub.name": "صفائی۔",
    "steps.scrub.verify.name": "تصدیق۔",
    "steps.scrub.inspect.text": (
        "فائل میں موجود EXIF، XMP، IPTC، C2PA اور ICC بلاکس کی فہرست دیکھنے کے لیے "
        "<code>picai inspect photo.jpg</code> چلائیں۔"
    ),
    "steps.scrub.scrub.text": (
        "<code>picai scrub photo.jpg</code> (یا <code>POST /scrub</code>) چلائیں۔ picai پکسلز کو "
        "ڈی کوڈ کرتا ہے، EXIF اورینٹیشن لاگو کرتا ہے، اور خام پکسل بفر سے بالکل نئی تصویر بناتا ہے۔"
    ),
    "steps.scrub.verify.text": (
        "<code>picai inspect photo.clean.jpg</code> چلائیں؛ اسے “no metadata signatures found” "
        "پرنٹ کرنا چاہیے۔"
    ),
    # FAQ (home slugs)
    "faq.accuracy.question": "ڈیٹیکٹر کتنا درست ہے؟",
    "faq.accuracy.answer_html": (
        "یہ ایک امکان بتاتا ہے، حتمی فیصلہ نہیں۔ 50% کے قریب اسکورز کو <em>غیر یقینی</em> کا لیبل "
        "دیا جاتا ہے؛ کسی بھی ایک نتیجے کو محض ایک اشارہ سمجھیں اور اسے دیگر شواہد کے ساتھ ملا کر "
        'دیکھیں۔ <a href="/how-accurate">AI امیج ڈیٹیکٹرز کتنے درست ہوتے ہیں</a> اس بارے میں مزید '
        "پڑھیں۔"
    ),
    "faq.leaves_computer.question": "کیا میری تصویر میرے کمپیوٹر سے باہر جاتی ہے؟",
    "faq.leaves_computer.answer_html": (
        "اس پبلک انسٹینس پر، جی ہاں: تصویر picai سرور (مصنف کے چلائے گئے Google Cloud Run "
        "کنٹینر) پر اپ لوڈ کی جاتی ہے، میموری میں اسکور کی جاتی ہے اور کبھی ڈسک پر نہیں لکھی جاتی۔ "
        "صاف کی گئی کاپی صرف اس وقت تک میموری میں رہتی ہے جب تک اس کی جگہ 100 نئے نتائج نہ لے لیں "
        "یا کنٹینر ری اسٹارٹ نہ ہو جائے، اور کچھ بھی کسی تھرڈ پارٹی API کو نہیں بھیجا جاتا۔ اگر آپ "
        'چاہتے ہیں کہ آپ کی مشین سے کچھ بھی باہر نہ جائے، تو ایک ہی Docker کمانڈ سے '
        '<a href="/self-host">picai خود چلائیں</a>۔ تفصیلات <a href="/privacy">پرائیویسی پیج</a> '
        "پر موجود ہیں۔"
    ),
    "faq.open_source.question": "کیا یہ اوپن سورس ہے؟",
    "faq.open_source.answer_html": (
        "جی ہاں۔ کوڈ، Docker امیج، CLI اور GitHub Action سب MIT لائسنس کے تحت "
        '<a href="https://github.com/Micorlov/picai" rel="noopener">picai ریپوزٹری</a> میں موجود '
        "ہیں۔ ڈیٹیکٹر ایک اوپن Hugging Face ماڈل ہے جسے آپ دیکھ یا تبدیل کر سکتے ہیں۔"
    ),
    "faq.remove_metadata.question": "کیا میں C2PA اور دیگر میٹا ڈیٹا ہٹا سکتا ہوں؟",
    "faq.remove_metadata.answer_html": (
        "جی ہاں۔ تصویر چیک کرنے کے بعد، <em>صاف کاپی ڈاؤن لوڈ کریں</em> استعمال کریں۔ picai تصویر "
        "کو اس کے پکسلز سے دوبارہ تعمیر کرتا ہے، اس لیے EXIF، XMP، IPTC، C2PA اور ICC پروفائل سب "
        'پیچھے رہ جاتے ہیں۔ <a href="/remove-image-metadata">اسکربر کیسے کام کرتا ہے</a>۔'
    ),
    "faq.formats.question": "کون سے فارمیٹس سپورٹڈ ہیں؟",
    "faq.formats.answer_html": (
        "JPEG، PNG، WebP، HEIC/HEIF اور زیادہ تر فارمیٹس جنہیں Pillow ڈی کوڈ کر سکتا ہے، زیادہ سے "
        "زیادہ 50 MB تک۔"
    ),
    "faq.why_metadata.question": "میٹا ڈیٹا کیوں دکھایا جاتا ہے؟",
    "faq.why_metadata.answer_html": (
        "C2PA کانٹینٹ کریڈینشلز اور ایڈیٹنگ سافٹ ویئر ٹیگز تصویر کے ماخذ کے اشارے ہیں۔ پینل دکھاتا "
        "ہے کہ فائل میں کون سے بلاکس (EXIF، XMP، IPTC، C2PA، ICC) موجود ہیں تاکہ آپ انہیں اسکور "
        'کے ساتھ ملا کر پرکھ سکیں۔ دیکھیں <a href="/c2pa">C2PA کانٹینٹ کریڈینشلز</a> اور '
        '<a href="/remove-image-metadata">تصویر کا میٹا ڈیٹا کیسے ہٹائیں</a>۔'
    ),
    "faq.different_model.question": "کیا میں کوئی مختلف ماڈل استعمال کر سکتا ہوں؟",
    "faq.different_model.answer_html": (
        "جی ہاں۔ <code>PICAI_DETECTOR_MODEL</code> کو کسی بھی Hugging Face امیج کلاسیفیکیشن ماڈل "
        "پر سیٹ کریں جس کے لیبلز AI/جعلی بمقابلہ انسانی/اصلی مواد کا نام دیتے ہوں۔"
    ),
    # FAQ (more slugs)
    "faq.free.question": "کیا picai مفت ہے؟",
    "faq.free.answer_html": (
        "جی ہاں۔ picai MIT لائسنس کے تحت اوپن سورس ہے۔ ہوسٹڈ انسٹینس مفت استعمال کے لیے ہے مگر ہر "
        "IP ایڈریس کے لیے ہر 24 گھنٹوں میں 10 تجزیوں کی حد ہے؛ خود ہوسٹ کی گئی کاپی کی کوئی حد "
        "نہیں۔"
    ),
    "faq.screenshots.question": "کیا یہ اسکرین شاٹس یا بہت زیادہ کمپریس کی گئی تصاویر پر کام کرتا ہے؟",
    "faq.screenshots.answer_html": (
        "یہ چلتا ہے، لیکن دوبارہ انکوڈنگ، سائز تبدیل کرنے اور اسکرین شاٹس لینے سے پکسل کی سطح کے "
        "کچھ نشانات مٹ جاتے ہیں جن پر کلاسیفائر انحصار کرتا ہے، اس لیے کم کانفیڈنس اور زیادہ "
        "<em>غیر یقینی</em> نتائج کی توقع رکھیں۔"
    ),
    "faq.which_generator.question": (
        "کیا یہ بتا سکتا ہے کہ تصویر کس جنریٹر (Midjourney، DALL·E، Stable Diffusion) نے بنائی؟"
    ),
    "faq.which_generator.answer_html": (
        "نہیں۔ picai عمومی طور پر جنریٹڈ بمقابلہ حقیقی پکسل کے اعداد و شمار کا اندازہ لگاتا ہے؛ "
        "یہ یہ شناخت نہیں کرتا کہ کون سے جنریٹر نے تصویر بنائی، اور اسے ان جنریٹرز کا کوئی علم "
        "نہیں ہوتا جو اس کے ماڈل کا تربیتی ڈیٹا جمع ہونے کے بعد جاری ہوئے۔"
    ),
    "faq.false_positive.question": "ایک اصلی تصویر کو AI کا اسکور کیوں ملا؟",
    "faq.false_positive.answer_html": (
        "بھاری فلٹرز، HDR پروسیسنگ، اپ اسکیلنگ، مصوری اور 3D رینڈرز میں جنریٹڈ تصاویر جیسی ہی کئی "
        "شماریاتی خصوصیات ہوتی ہیں۔ یہ اسکور ایک امکان ہے، ثبوت نہیں؛ غلط مثبت نتائج پیش آ سکتے ہیں۔"
    ),
    "faq.offline.question": "کیا میں اسے آف لائن چلا سکتا ہوں؟",
    "faq.offline.answer_html": (
        "جی ہاں۔ پہلی بار چلانے پر ماڈل کے Hugging Face کیش میں ڈاؤن لوڈ ہو جانے کے بعد، خود ہوسٹ "
        "کیے گئے picai کو کسی نیٹ ورک رسائی کی ضرورت نہیں رہتی۔"
    ),
    "faq.rate_limit.question": "کیا ہوسٹڈ انسٹینس پر کوئی ریٹ لمٹ ہے؟",
    "faq.rate_limit.answer_html": (
        "جی ہاں: کسی بھی رولنگ 24 گھنٹے کی ونڈو میں فی کلائنٹ IP 10 تجزیے۔ رسپانسز میں "
        "<code>X-RateLimit-Remaining</code> ہیڈر شامل ہوتا ہے، اور حد سے زیادہ درخواست پر "
        "<code>Retry-After</code> ہیڈر کے ساتھ 429 اسٹیٹس واپس آتا ہے۔"
    ),
    # Navigation
    "nav.detector": "ڈیٹیکٹر",
    "nav.how_it_works": "یہ کیسے کام کرتا ہے",
    "nav.how-to-tell-if-an-image-is-ai-generated": "گائیڈ",
    "nav.api": "API",
    "nav.self-host": "سیلف ہوسٹ",
    # Footer
    "footer.remove-image-metadata": "میٹا ڈیٹا ہٹائیں",
    "footer.c2pa": "C2PA",
    "footer.faq": "عمومی سوالات",
    "footer.privacy": "پرائیویسی",
    "footer.self-host": "سیلف ہوسٹ",
    "footer.about": "تعارف",
    # UI strings
    "ui.nav_aria_label": "مرکزی نیویگیشن",
    "ui.loading_status": "ڈیٹیکٹر لوڈ ہو رہا ہے…",
    "ui.hero_overline": "— اوپن سورس AI امیج فرانزکس",
    "ui.hero_heading_line1": "کیا یہ تصویر اصلی ہے؟",
    "ui.hero_heading_line2": "اسکور اور ثبوت حاصل کریں۔",
    "ui.tool_aria_label": "AI امیج ڈیٹیکٹر",
    "ui.dropzone_aria_label": "تجزیے کے لیے ایک تصویر اپ لوڈ کریں",
    "ui.dropzone_title_fine": "ایک تصویر ڈریگ اینڈ ڈراپ کریں",
    "ui.dropzone_title_coarse": "ایک تصویر چیک کریں",
    "ui.dropzone_sub_fine": "یا کلپ بورڈ سے پیسٹ کریں، یا",
    "ui.dropzone_sub_coarse": "اپنی لائبریری یا کیمرے سے",
    "ui.btn_check_image_fine": "یہ تصویر چیک کریں",
    "ui.btn_choose_photo_coarse": "تصویر منتخب کریں",
    "ui.btn_take_photo": "تصویر لیں",
    "ui.dismiss_aria_label": "بند کریں",
    "ui.analyzing_prefix": "تجزیہ ہو رہا ہے",
    "ui.analyzing_suffix": "· پکسلز · میٹا ڈیٹا بلاکس",
    "ui.verdict_overline": "— فیصلہ",
    "ui.meter_real": "اصلی",
    "ui.meter_uncertain": "غیر یقینی",
    "ui.meter_ai": "AI",
    "ui.model_label": "ماڈل",
    "ui.verdict_disclaimer_html": (
        "نتائج ایک کلاسیفائر کے امکانات ہیں، حتمی فیصلے نہیں۔ "
        '<a href="/how-accurate">اسکور کیسے پڑھیں۔</a>'
    ),
    "ui.btn_check_another": "کوئی اور تصویر چیک کریں",
    "ui.preview_overline": "— پیش منظر",
    "ui.preview_alt": "اپ لوڈ کی گئی تصویر کا پیش منظر",
    "ui.metadata_overline": "— میٹا ڈیٹا",
    "ui.metadata_heading": "فائل میں ملا۔",
    "ui.jpeg_segments_label": "JPEG سیگمنٹس",
    "ui.btn_download_clean": "صاف کاپی ڈاؤن لوڈ کریں",
    "ui.metadata_scrub_note_html": (
        "پکسلز سے دوبارہ رینڈر کیا گیا ہے، اس لیے اوپر دیا گیا ہر بلاک ختم ہو چکا ہے۔ "
        '<a href="/remove-image-metadata">یہ کیسے کام کرتا ہے</a>'
    ),
    "ui.how_it_works_overline": "— یہ کیسے کام کرتا ہے",
    "ui.how_it_works_heading": "تین مراحل۔ کچھ بھی محفوظ نہیں کیا جاتا۔",
    "ui.how_it_works_links_html": (
        '<a href="/how-to-tell-if-an-image-is-ai-generated">AI تصاویر پہچاننے کی گائیڈ پڑھیں</a> '
        'یا <a href="/self-host">اسے اپنی مشین پر چلائیں</a>۔'
    ),
    "ui.faq_overline": "— عمومی سوالات",
    "ui.faq_heading": "سوال پوچھنے سے پہلے۔",
    "ui.faq_more_link": "مزید سوالات اور جوابات →",
    "ui.footer_tagline": "picai. · اوپن سورس",
    "ui.footer_detector_label": "ڈیٹیکٹر:",
    "ui.breadcrumb_aria_label": "بریڈکرمب",
    "ui.last_updated_prefix": "آخری بار اپ ڈیٹ کیا گیا",
    "ui.source_on_github": "GitHub پر سورس کوڈ",
    "ui.btn_try_detector": "ڈیٹیکٹر آزمائیں",
    "ui.status_ready": "ڈیٹیکٹر تیار ہے",
    "ui.status_unreachable": "سرور تک رسائی ممکن نہیں",
    "ui.loading_model_note": "ڈیٹیکٹر ماڈل لوڈ ہو رہا ہے (پہلی بار چلانے پر تقریباً 750 MB ڈاؤن لوڈ ہوگا)…",
    "ui.error_empty_file": "یہ فائل خالی ہے۔",
    "ui.error_file_too_large": "{name} کا سائز {size} ہے — حد 50 MB ہے۔",
    "ui.error_server_unreachable": "سرور سے رابطہ نہیں ہو سکا: {message}",
    "ui.verdict_ai": "غالباً AI سے تیار کردہ",
    "ui.verdict_real": "غالباً ایک اصلی تصویر",
    "ui.verdict_uncertain": "غیر یقینی",
    "ui.confidence_suffix": "اعتماد",
    "ui.format_unknown": "نامعلوم",
    "ui.metadata_present": "موجود",
    "ui.metadata_not_present": "موجود نہیں",
    "ui.no_jpeg_segments": "کوئی JPEG APP سیگمنٹس نہیں",
    "ui.quota_remaining": "آج {limit} میں سے {remaining} تجزیے باقی ہیں",
}
