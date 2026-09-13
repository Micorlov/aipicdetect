"""Arabic translation table. Falls back to English (see picai.content.locales) for any key
missing here, so this file only needs to define what has actually been translated.

Text is written as plain right-to-left prose; no directional markup is added here because the
page itself sets dir="rtl" for this locale.
"""

from __future__ import annotations

STRINGS: dict[str, str] = {
    "page.home.title": "picai — كاشف صور الذكاء الاصطناعي مفتوح المصدر ومنظّف البيانات الوصفية",
    "page.home.description": (
        "تحقّق مما إذا كانت الصورة مولّدة بالذكاء الاصطناعي باستخدام picai، وهو كاشف مجاني ومفتوح "
        "المصدر. استخدمه في المتصفح أو شغّله على جهازك الخاص باستخدام Docker أو Python."
    ),
    "page.home.h1": "هل هذه الصورة حقيقية؟ احصل على النتيجة والدليل.",
    "page.faq.title": "الأسئلة الشائعة حول كاشف صور الذكاء الاصطناعي: الدقة، الخصوصية، الصيغ، النماذج",
    "page.faq.description": (
        "إجابات عن الأسئلة الشائعة حول picai: مدى دقة كشف صور الذكاء الاصطناعي، وأين تتم معالجة "
        "صورتك، والصيغ المدعومة، وتبديل النموذج، وحدود الاستخدام."
    ),
    "page.faq.h1": "الأسئلة الشائعة حول picai",
    "page.faq.intro_suffix": "هذه هي الأسئلة الأكثر شيوعًا حول طريقة عمله، ومدى دقته، وما يحدث للصور التي يتم رفعها.",
    "page.faq.still_unsure_html": (
        'ما زلت غير متأكد؟ افتح issue على <a href="https://github.com/Micorlov/picai/issues" '
        'rel="noopener">GitHub</a>.'
    ),
    "home.entity_sentence": (
        "picai أداة مجانية ومفتوحة المصدر تُقيّم احتمال كون الصورة مولّدة بالذكاء الاصطناعي وتزيل "
        "البيانات الوصفية المخفية — سواء عبر النسخة المستضافة أو عبر الاستضافة الذاتية، الخيار لك."
    ),
    "home.lead": (
        "يشغّل picai نموذج كشف مفتوح المصدر ويقرأ كل حقول EXIF وC2PA وIPTC التي تحملها الصورة — ثم "
        "يمنحك نسخة نظيفة تمت إزالة كل ذلك منها. بلا تسجيل، بلا صندوق أسود."
    ),
    "home.dropzone_note": "JPEG وPNG وWebP وHEIC · حتى 50 MB · تتم المعالجة في الذاكرة ولا تُكتب أبدًا على القرص",
    "home.summary": (
        "picai أداة مجانية ومفتوحة المصدر تُقيّم احتمال كون الصورة مولّدة بالذكاء الاصطناعي وتزيل "
        "البيانات الوصفية المخفية — سواء عبر النسخة المستضافة أو عبر الاستضافة الذاتية، الخيار لك. "
        "يُقدّر مدى احتمال إنتاج الصورة بواسطة مولّد ذكاء اصطناعي باستخدام مصنّف مفتوح من Hugging "
        "Face، ويمكنه إعادة تصيير الصور لإزالة بيانات EXIF وXMP وIPTC وICC وC2PA الوصفية. استخدم "
        "النسخة المستضافة أو استضفه بنفسك باستخدام Docker أو Python."
    ),
    "home.stat.0": "نموذج مفتوح،<br>بلا API من جهة خارجية",
    "home.stat.1": "تسجيلات<br>مطلوبة",
    "home.stat.2": "MB كحد أقصى<br>للرفع",
    "steps.detect.upload.name": "الرفع.",
    "steps.detect.detect.name": "الكشف.",
    "steps.detect.decide.name": "القرار.",
    "steps.detect.upload.text": (
        "اسحب الصورة أو الصقها أو اخترها. تُرسَل إلى خادم picai الذي تستخدمه (جهازك الخاص عند "
        "الاستضافة الذاتية)، وتُحفظ في الذاكرة ولا تُكتب أبدًا على القرص."
    ),
    "steps.detect.detect.text": (
        "يقوم مصنّف صور مفتوح المصدر بتقدير مدى احتمال أن تكون البكسلات ناتجة عن مولّد."
    ),
    "steps.detect.decide.text": (
        "تحصل على احتمال كون الصورة من إنتاج الذكاء الاصطناعي، ونطاق ثقة، وكتل البيانات الوصفية "
        "التي يحملها الملف — كاحتمال، وليس كحكم قاطع."
    ),
    # steps.scrub.*.text carries inline <code>...</code> shell commands — preserved verbatim below,
    # only the surrounding prose is translated.
    "steps.scrub.inspect.name": "الفحص.",
    "steps.scrub.scrub.name": "التنظيف.",
    "steps.scrub.verify.name": "التحقق.",
    "steps.scrub.inspect.text": (
        "شغّل <code>picai inspect photo.jpg</code> لعرض كتل EXIF وXMP وIPTC وC2PA وICC التي يحملها الملف."
    ),
    "steps.scrub.scrub.text": (
        "شغّل <code>picai scrub photo.jpg</code> (أو <code>POST /scrub</code>). يقوم picai بفك "
        "ترميز البكسلات، وتطبيق اتجاه EXIF، وبناء صورة جديدة تمامًا من مخزن البكسلات الخام."
    ),
    "steps.scrub.verify.text": (
        'شغّل <code>picai inspect photo.clean.jpg</code>؛ يجب أن يعرض "no metadata signatures found".'
    ),
    "faq.accuracy.question": "ما مدى دقة الكاشف؟",
    "faq.leaves_computer.question": "هل تغادر صورتي جهاز الكمبيوتر الخاص بي؟",
    "faq.open_source.question": "هل هو مفتوح المصدر؟",
    "faq.remove_metadata.question": "هل يمكنني إزالة C2PA وبيانات وصفية أخرى؟",
    "faq.formats.question": "ما الصيغ المدعومة؟",
    "faq.why_metadata.question": "لماذا تُعرض البيانات الوصفية؟",
    "faq.different_model.question": "هل يمكنني استخدام نموذج مختلف؟",
    "faq.free.question": "هل picai مجاني؟",
    "faq.screenshots.question": "هل يعمل مع لقطات الشاشة أو الصور المضغوطة بشدة؟",
    "faq.which_generator.question": (
        "هل يمكنه تحديد أي مولّد أنشأ الصورة (Midjourney أو DALL·E أو Stable Diffusion)؟"
    ),
    "faq.false_positive.question": "لماذا حصلت صورة حقيقية على نتيجة تشير إلى الذكاء الاصطناعي؟",
    "faq.offline.question": "هل يمكنني تشغيله دون اتصال بالإنترنت؟",
    "faq.rate_limit.question": "هل يوجد حد لمعدل الاستخدام في النسخة المستضافة؟",
    "faq.accuracy.answer_html": (
        "يعرض الكاشف احتمالًا، وليس حكمًا قاطعًا. النتائج القريبة من 50% تُصنَّف كـ<em>غير "
        "مؤكدة</em>؛ تعامل مع أي نتيجة منفردة كمؤشر واجمعها مع أدلة أخرى. اقرأ المزيد حول "
        '<a href="/how-accurate">مدى دقة كاشفات صور الذكاء الاصطناعي</a>.'
    ),
    "faq.leaves_computer.answer_html": (
        "في هذه النسخة العامة، نعم: تُرفع الصورة إلى خادم picai (حاوية Google Cloud Run يديرها "
        "المؤلف)، وتُقيَّم في الذاكرة ولا تُكتب أبدًا على القرص. تُحفظ النسخة المنظّفة في الذاكرة "
        "فقط إلى أن تحل محلها 100 نتيجة أحدث أو تتم إعادة تشغيل الحاوية، ولا يُرسَل شيء إلى أي "
        'واجهة برمجة تابعة لجهة خارجية. إذا كنت تريد ألا يغادر أي شيء جهازك، <a href="/self-host">'
        'شغّل picai بنفسك</a> بأمر Docker واحد. التفاصيل موجودة في <a href="/privacy">صفحة '
        "الخصوصية</a>."
    ),
    "faq.open_source.answer_html": (
        "نعم. الكود، وصورة Docker، وأداة سطر الأوامر، وGitHub Action كلها موجودة في "
        '<a href="https://github.com/Micorlov/picai" rel="noopener">مستودع picai</a> بموجب ترخيص '
        "MIT. الكاشف هو نموذج مفتوح من Hugging Face يمكنك فحصه أو استبداله."
    ),
    "faq.remove_metadata.answer_html": (
        "نعم. بعد فحص صورة، استخدم <em>تنزيل النسخة النظيفة</em>. يعيد picai بناء الصورة من "
        "بكسلاتها، بحيث تُترك خلفها جميع بيانات EXIF وXMP وIPTC وC2PA وملف ICC الشخصي. "
        '<a href="/remove-image-metadata">كيف يعمل المنظّف</a>.'
    ),
    "faq.formats.answer_html": (
        "JPEG وPNG وWebP وHEIC/HEIF ومعظم الصيغ التي يمكن لمكتبة Pillow فك ترميزها، حتى 50 MB."
    ),
    "faq.why_metadata.answer_html": (
        "اعتمادات محتوى C2PA وعلامات برامج التحرير هي مؤشرات على مصدر الصورة. تعرض اللوحة الكتل "
        "التي يحملها الملف (EXIF وXMP وIPTC وC2PA وICC) حتى تتمكن من موازنتها مع النتيجة. راجع "
        '<a href="/c2pa">اعتمادات محتوى C2PA</a> و<a href="/remove-image-metadata">كيفية إزالة '
        "البيانات الوصفية من الصورة</a>."
    ),
    "faq.different_model.answer_html": (
        "نعم. اضبط <code>PICAI_DETECTOR_MODEL</code> على أي نموذج تصنيف صور من Hugging Face تميّز "
        "تسمياته بين محتوى ذكاء اصطناعي/مزيّف ومحتوى بشري/حقيقي."
    ),
    "faq.free.answer_html": (
        "نعم. picai مفتوح المصدر بموجب ترخيص MIT. النسخة المستضافة مجانية الاستخدام بحد أقصى 10 "
        "عمليات تحليل لكل عنوان IP كل 24 ساعة؛ أما النسخة ذاتية الاستضافة فلا حد لها."
    ),
    "faq.screenshots.answer_html": (
        "يعمل، لكن إعادة الترميز وتغيير الحجم ولقطات الشاشة تزيل بعض الآثار على مستوى البكسل التي "
        "يعتمد عليها المصنّف، لذا توقع ثقة أقل ونتائج <em>غير مؤكدة</em> أكثر."
    ),
    "faq.which_generator.answer_html": (
        "لا. يقيّم picai بشكل عام إحصاءات البكسلات المولَّدة مقابل الحقيقية؛ ولا يحدد المولّد نفسه، "
        "وليس لديه أي معرفة بالمولّدات التي صدرت بعد جمع بيانات تدريب نموذجه."
    ),
    "faq.false_positive.answer_html": (
        "الفلاتر القوية، ومعالجة HDR، وتكبير الدقة، والرسوم التوضيحية، والتصيير ثلاثي الأبعاد "
        "تشترك جميعها في خصائص إحصائية مع الصور المولَّدة. النتيجة احتمال وليست دليلًا؛ وتحدث "
        "النتائج الإيجابية الكاذبة."
    ),
    "faq.offline.answer_html": (
        "نعم. بعد أن يقوم أول تشغيل بتنزيل النموذج إلى ذاكرة Hugging Face المؤقتة، لا يحتاج picai "
        "المستضاف ذاتيًا إلى أي اتصال بالشبكة."
    ),
    "faq.rate_limit.answer_html": (
        "نعم: 10 عمليات تحليل لكل عنوان IP للعميل خلال أي نافذة متحركة مدتها 24 ساعة. تتضمن "
        "الاستجابات ترويسة <code>X-RateLimit-Remaining</code>، وأي طلب يتجاوز الحد يُعيد الرمز 429 "
        "مع ترويسة <code>Retry-After</code>."
    ),
    "nav.detector": "الكاشف",
    "nav.how_it_works": "كيف يعمل",
    "nav.how-to-tell-if-an-image-is-ai-generated": "الدليل",
    "nav.api": "API",
    "nav.self-host": "الاستضافة الذاتية",
    "footer.remove-image-metadata": "إزالة البيانات الوصفية",
    "footer.c2pa": "C2PA",
    "footer.faq": "الأسئلة الشائعة",
    "footer.privacy": "الخصوصية",
    "footer.self-host": "الاستضافة الذاتية",
    "footer.about": "حول",
    "ui.nav_aria_label": "التنقل الرئيسي",
    "ui.loading_status": "جارٍ تحميل الكاشف…",
    "ui.hero_overline": "— تحليل جنائي مفتوح المصدر لصور الذكاء الاصطناعي",
    "ui.hero_heading_line1": "هل هذه الصورة حقيقية؟",
    "ui.hero_heading_line2": "احصل على النتيجة والدليل.",
    "ui.tool_aria_label": "كاشف صور الذكاء الاصطناعي",
    "ui.dropzone_aria_label": "ارفع صورة لتحليلها",
    "ui.dropzone_title_fine": "اسحب صورة وأفلتها هنا",
    "ui.dropzone_title_coarse": "تحقّق من صورة",
    "ui.dropzone_sub_fine": "أو الصقها من الحافظة، أو",
    "ui.dropzone_sub_coarse": "من مكتبتك أو الكاميرا",
    "ui.btn_check_image_fine": "تحقّق من هذه الصورة",
    "ui.btn_choose_photo_coarse": "اختر صورة",
    "ui.btn_take_photo": "التقط صورة",
    "ui.dismiss_aria_label": "إغلاق",
    "ui.analyzing_prefix": "جارٍ التحليل",
    "ui.analyzing_suffix": "· بكسلات · كتل بيانات وصفية",
    "ui.verdict_overline": "— الحكم",
    "ui.meter_real": "حقيقية",
    "ui.meter_uncertain": "غير مؤكد",
    "ui.meter_ai": "ذكاء اصطناعي",
    "ui.model_label": "النموذج",
    "ui.verdict_disclaimer_html": (
        "النتائج احتمالات صادرة عن مصنّف، وليست أحكامًا قاطعة. "
        '<a href="/how-accurate">كيفية قراءة النتيجة.</a>'
    ),
    "ui.btn_check_another": "تحقّق من صورة أخرى",
    "ui.preview_overline": "— معاينة",
    "ui.preview_alt": "معاينة الصورة التي تم رفعها",
    "ui.metadata_overline": "— البيانات الوصفية",
    "ui.metadata_heading": "تم العثور عليه في الملف.",
    "ui.jpeg_segments_label": "مقاطع JPEG",
    "ui.btn_download_clean": "تنزيل النسخة النظيفة",
    "ui.metadata_scrub_note_html": (
        "أُعيد تصييرها من البكسلات، لذا اختفت كل الكتل المذكورة أعلاه. "
        '<a href="/remove-image-metadata">كيف يعمل ذلك</a>'
    ),
    "ui.how_it_works_overline": "— كيف يعمل",
    "ui.how_it_works_heading": "ثلاث خطوات. لا شيء يُحفظ.",
    "ui.how_it_works_links_html": (
        '<a href="/how-to-tell-if-an-image-is-ai-generated">اقرأ الدليل لاكتشاف صور الذكاء '
        'الاصطناعي</a> أو <a href="/self-host">شغّله على جهازك الخاص</a>.'
    ),
    "ui.faq_overline": "— الأسئلة الشائعة",
    "ui.faq_heading": "قبل أن تسأل.",
    "ui.faq_more_link": "المزيد من الأسئلة والأجوبة →",
    "ui.footer_tagline": "picai. · مفتوح المصدر",
    "ui.footer_detector_label": "الكاشف:",
    "ui.breadcrumb_aria_label": "مسار التنقل",
    "ui.last_updated_prefix": "آخر تحديث",
    "ui.source_on_github": "الكود المصدري على GitHub",
    "ui.btn_try_detector": "جرّب الكاشف",
    "ui.status_ready": "الكاشف جاهز",
    "ui.status_unreachable": "تعذّر الوصول إلى الخادم",
    "ui.loading_model_note": "جارٍ تحميل نموذج الكاشف (يقوم أول تشغيل بتنزيل نحو 750 MB)…",
    "ui.error_empty_file": "هذا الملف فارغ.",
    "ui.error_file_too_large": "{name} حجمه {size} — الحد الأقصى هو 50 MB.",
    "ui.error_server_unreachable": "تعذّر الاتصال بالخادم: {message}",
    "ui.verdict_ai": "على الأرجح مولّدة بالذكاء الاصطناعي",
    "ui.verdict_real": "على الأرجح صورة حقيقية",
    "ui.verdict_uncertain": "غير مؤكد",
    "ui.confidence_suffix": "ثقة",
    "ui.format_unknown": "غير معروف",
    "ui.metadata_present": "موجودة",
    "ui.metadata_not_present": "غير موجودة",
    "ui.no_jpeg_segments": "لا توجد مقاطع APP من JPEG",
    "ui.quota_remaining": "{remaining} من {limit} تحليلات متبقية اليوم",
}
