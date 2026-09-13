"""Hindi translation table.

Falls back to English (see :func:`picai.content.locales.t`) for any key not defined here, but
every key from :mod:`picai.content.locales.en` is translated below.
"""

from __future__ import annotations

STRINGS: dict[str, str] = {
    # Page metadata
    "page.home.title": "picai — ओपन-सोर्स AI इमेज डिटेक्टर और मेटाडेटा स्क्रबर",
    "page.home.description": (
        "picai से जाँचें कि कोई तस्वीर AI-जनरेटेड है या नहीं — यह एक मुफ़्त, ओपन-सोर्स डिटेक्टर है। "
        "इसे ब्राउज़र में इस्तेमाल करें या Docker या Python के ज़रिए अपनी मशीन पर चलाएँ।"
    ),
    "page.home.h1": "क्या यह तस्वीर असली है? स्कोर और सबूत पाएँ।",
    "page.faq.title": "AI इमेज डिटेक्टर पर सामान्य प्रश्न: सटीकता, प्राइवेसी, फ़ॉर्मैट, मॉडल",
    "page.faq.description": (
        "picai से जुड़े सामान्य सवालों के जवाब: AI इमेज डिटेक्शन कितना सटीक है, आपकी इमेज कहाँ "
        "प्रोसेस होती है, कौन-से फ़ॉर्मैट सपोर्ट किए जाते हैं, मॉडल कैसे बदलें और रेट लिमिट क्या है।"
    ),
    "page.faq.h1": "picai से जुड़े सामान्य प्रश्न",
    "page.faq.intro_suffix": (
        "ये वे सवाल हैं जो लोग सबसे ज़्यादा पूछते हैं—यह कैसे काम करता है, कितना सटीक है, और अपलोड की गई "
        "तस्वीरों का क्या होता है।"
    ),
    "page.faq.still_unsure_html": (
        'अब भी संशय है? <a href="https://github.com/Micorlov/picai/issues" rel="noopener">GitHub</a> पर '
        'एक issue खोलें।'
    ),
    # Home page copy
    "home.entity_sentence": (
        "picai एक मुफ़्त, ओपन-सोर्स टूल है जो यह आँकता है कि कोई इमेज AI से बनी है या नहीं, और "
        "छिपे हुए मेटाडेटा को हटा देता है — होस्टेड इस्तेमाल करें या सेल्फ़-होस्ट, चुनाव आपका है।"
    ),
    "home.lead": (
        "picai एक ओपन AI-डिटेक्शन मॉडल चलाता है और तस्वीर में मौजूद हर EXIF, C2PA और IPTC फ़ील्ड "
        "को पढ़ता है — फिर आपको एक साफ़ कॉपी देता है जिसमें यह सब हटा दिया गया हो। न कोई साइन-अप, "
        "न कोई ब्लैक बॉक्स।"
    ),
    "home.dropzone_note": (
        "JPEG, PNG, WebP, HEIC · अधिकतम 50 MB तक · मेमोरी में प्रोसेस, कभी डिस्क पर सेव नहीं होता"
    ),
    "home.summary": (
        "picai एक मुफ़्त, ओपन-सोर्स टूल है जो यह आँकता है कि कोई इमेज AI से बनी है या नहीं, और "
        "छिपे हुए मेटाडेटा को हटा देता है — होस्टेड इस्तेमाल करें या सेल्फ़-होस्ट, चुनाव आपका है। "
        "यह एक ओपन Hugging Face क्लासिफ़ायर का उपयोग करके यह आँकता है कि तस्वीर किसी AI जनरेटर "
        "से बनने की कितनी संभावना है, और इमेज को फिर से रेंडर करके EXIF, XMP, IPTC, ICC और C2PA "
        "मेटाडेटा हटा सकता है। होस्टेड इंस्टेंस इस्तेमाल करें या Docker या Python के साथ "
        "सेल्फ़-होस्ट करें।"
    ),
    "home.stat.0": "ओपन मॉडल,<br>कोई थर्ड-पार्टी API नहीं",
    "home.stat.1": "साइन-अप की<br>ज़रूरत नहीं",
    "home.stat.2": "MB अधिकतम<br>अपलोड",
    # Detect steps
    "steps.detect.upload.name": "अपलोड करें।",
    "steps.detect.upload.text": (
        "कोई तस्वीर ड्रॉप करें, पेस्ट करें या चुनें। यह उस picai सर्वर पर भेजी जाती है जिसे आप "
        "इस्तेमाल कर रहे हैं (सेल्फ़-होस्ट में यह आपकी अपनी मशीन होती है), मेमोरी में रखी जाती है "
        "और कभी डिस्क पर सेव नहीं होती।"
    ),
    "steps.detect.detect.name": "डिटेक्ट करें।",
    "steps.detect.detect.text": (
        "एक ओपन-सोर्स इमेज क्लासिफ़ायर यह आँकता है कि पिक्सल किसी जनरेटर से बनने की कितनी "
        "संभावना है।"
    ),
    "steps.detect.decide.name": "फ़ैसला लें।",
    "steps.detect.decide.text": (
        "आपको AI होने की संभावना, एक कॉन्फ़िडेंस बैंड, और फ़ाइल में मौजूद मेटाडेटा ब्लॉक्स मिलते "
        "हैं — यह एक संभावना है, कोई अंतिम फ़ैसला नहीं।"
    ),
    # Scrub steps — <code> blocks contain literal shell commands and must stay untranslated
    "steps.scrub.inspect.name": "जाँचें।",
    "steps.scrub.inspect.text": (
        "फ़ाइल में मौजूद EXIF, XMP, IPTC, C2PA और ICC ब्लॉक्स की सूची पाने के लिए "
        "<code>picai inspect photo.jpg</code> चलाएँ।"
    ),
    "steps.scrub.scrub.name": "स्क्रब करें।",
    "steps.scrub.scrub.text": (
        "<code>picai scrub photo.jpg</code> (या <code>POST /scrub</code>) चलाएँ। picai पिक्सल "
        "डिकोड करता है, EXIF ओरिएंटेशन लागू करता है, और कच्चे पिक्सल बफ़र से एक बिल्कुल नई इमेज "
        "बनाता है।"
    ),
    "steps.scrub.verify.name": "सत्यापित करें।",
    "steps.scrub.verify.text": (
        "<code>picai inspect photo.clean.jpg</code> चलाएँ; इसे "
        "“no metadata signatures found” प्रिंट करना चाहिए।"
    ),
    # FAQ (home slugs)
    "faq.accuracy.question": "यह डिटेक्टर कितना सटीक है?",
    "faq.accuracy.answer_html": (
        "यह एक संभावना बताता है, कोई अंतिम फ़ैसला नहीं। 50% के आसपास के स्कोर को "
        "<em>अनिश्चित</em> बताया जाता है; किसी भी एक नतीजे को सिर्फ़ एक संकेत मानें और उसे "
        "बाक़ी सबूतों के साथ जोड़कर देखें। "
        '<a href="/how-accurate">AI इमेज डिटेक्टर कितने सटीक होते हैं</a>, इस बारे में और पढ़ें।'
    ),
    "faq.leaves_computer.question": "क्या मेरी इमेज मेरे कंप्यूटर से बाहर जाती है?",
    "faq.leaves_computer.answer_html": (
        "इस पब्लिक इंस्टेंस पर, हाँ: तस्वीर picai सर्वर (लेखक द्वारा चलाया जा रहा एक Google "
        "Cloud Run कंटेनर) पर अपलोड होती है, मेमोरी में स्कोर होती है और कभी डिस्क पर सेव नहीं "
        "होती। स्क्रब की गई कॉपी तब तक ही मेमोरी में रहती है जब तक उसकी जगह 100 नए नतीजे न आ "
        "जाएँ या कंटेनर रीस्टार्ट न हो जाए, और कुछ भी किसी थर्ड-पार्टी API को नहीं भेजा जाता। "
        'अगर आप चाहते हैं कि कुछ भी आपकी मशीन से बाहर न जाए, तो एक ही Docker कमांड से '
        '<a href="/self-host">picai को खुद चलाएँ</a>। जानकारी '
        '<a href="/privacy">प्राइवेसी पेज</a> पर है।'
    ),
    "faq.open_source.question": "क्या यह ओपन सोर्स है?",
    "faq.open_source.answer_html": (
        "हाँ। कोड, Docker इमेज, CLI और GitHub Action सब "
        '<a href="https://github.com/Micorlov/picai" rel="noopener">picai रिपॉज़िटरी</a> में '
        "MIT लाइसेंस के तहत मौजूद हैं। डिटेक्टर एक ओपन Hugging Face मॉडल है जिसे आप देख या बदल "
        "सकते हैं।"
    ),
    "faq.remove_metadata.question": "क्या मैं C2PA और बाक़ी मेटाडेटा हटा सकता/सकती हूँ?",
    "faq.remove_metadata.answer_html": (
        "हाँ। तस्वीर जाँचने के बाद <em>साफ़ कॉपी डाउनलोड करें</em> इस्तेमाल करें। picai इमेज को "
        "उसके पिक्सल से फिर से बनाता है, इसलिए EXIF, XMP, IPTC, C2PA और ICC प्रोफ़ाइल सब पीछे "
        'छूट जाते हैं। <a href="/remove-image-metadata">स्क्रबर कैसे काम करता है</a>।'
    ),
    "faq.formats.question": "कौन-से फ़ॉर्मैट सपोर्ट किए जाते हैं?",
    "faq.formats.answer_html": (
        "JPEG, PNG, WebP, HEIC/HEIF और वे ज़्यादातर फ़ॉर्मैट जिन्हें Pillow डिकोड कर सकता है, "
        "अधिकतम 50 MB तक।"
    ),
    "faq.why_metadata.question": "मेटाडेटा क्यों दिखाया जाता है?",
    "faq.why_metadata.answer_html": (
        "C2PA कंटेंट क्रेडेंशियल्स और एडिटिंग-सॉफ़्टवेयर टैग्स इस बात के संकेत होते हैं कि इमेज "
        "कहाँ से आई। पैनल यह दिखाता है कि फ़ाइल में कौन-से ब्लॉक्स (EXIF, XMP, IPTC, C2PA, ICC) "
        'मौजूद हैं, ताकि आप उन्हें स्कोर के साथ मिलाकर तौल सकें। देखें '
        '<a href="/c2pa">C2PA कंटेंट क्रेडेंशियल्स</a> और '
        '<a href="/remove-image-metadata">इमेज मेटाडेटा कैसे हटाएँ</a>।'
    ),
    "faq.different_model.question": "क्या मैं कोई अलग मॉडल इस्तेमाल कर सकता/सकती हूँ?",
    "faq.different_model.answer_html": (
        "हाँ। <code>PICAI_DETECTOR_MODEL</code> को किसी भी Hugging Face इमेज-क्लासिफ़िकेशन "
        "मॉडल पर सेट करें, जिसके लेबल AI/नक़ली बनाम इंसान/असली कंटेंट को नाम देते हों।"
    ),
    # FAQ (more slugs)
    "faq.free.question": "क्या picai मुफ़्त है?",
    "faq.free.answer_html": (
        "हाँ। picai MIT लाइसेंस के तहत ओपन सोर्स है। होस्टेड इंस्टेंस मुफ़्त है, इसकी सीमा हर "
        "IP एड्रेस के लिए हर 24 घंटे में 10 विश्लेषण है; सेल्फ़-होस्टेड कॉपी की कोई सीमा नहीं है।"
    ),
    "faq.screenshots.question": "क्या यह स्क्रीनशॉट या बहुत ज़्यादा कंप्रेस की गई इमेज पर काम करता है?",
    "faq.screenshots.answer_html": (
        "यह चलता तो है, लेकिन री-एन्कोडिंग, रीसाइज़िंग और स्क्रीनशॉट लेने से पिक्सल-स्तर के कुछ "
        "वे निशान मिट जाते हैं जिन पर क्लासिफ़ायर निर्भर करता है, इसलिए कम कॉन्फ़िडेंस और ज़्यादा "
        "<em>अनिश्चित</em> नतीजों की उम्मीद रखें।"
    ),
    "faq.which_generator.question": (
        "क्या यह बता सकता है कि इमेज किस जनरेटर (Midjourney, DALL·E, Stable Diffusion) से बनी है?"
    ),
    "faq.which_generator.answer_html": (
        "नहीं। picai सामान्य तौर पर जनरेटेड बनाम असली पिक्सल आँकड़ों का आकलन करता है; यह यह "
        "पहचान नहीं करता कि किस जनरेटर ने इमेज बनाई, और उसे उन जनरेटरों की कोई जानकारी नहीं होती "
        "जो उसके मॉडल का ट्रेनिंग डेटा इकट्ठा होने के बाद जारी हुए।"
    ),
    "faq.false_positive.question": "एक असली फ़ोटो को AI का स्कोर क्यों मिला?",
    "faq.false_positive.answer_html": (
        "भारी फ़िल्टर, HDR प्रोसेसिंग, अपस्केलिंग, इलस्ट्रेशन और 3D रेंडर्स में जनरेटेड इमेज जैसी "
        "ही कई सांख्यिकीय विशेषताएँ होती हैं। यह स्कोर एक संभावना है, कोई सबूत नहीं; फ़ॉल्स "
        "पॉज़िटिव होना संभव है।"
    ),
    "faq.offline.question": "क्या मैं इसे ऑफ़लाइन चला सकता/सकती हूँ?",
    "faq.offline.answer_html": (
        "हाँ। पहली बार चलाने पर मॉडल Hugging Face कैश में डाउनलोड हो जाने के बाद, सेल्फ़-होस्टेड "
        "picai को नेटवर्क एक्सेस की ज़रूरत नहीं रहती।"
    ),
    "faq.rate_limit.question": "क्या होस्टेड इंस्टेंस पर कोई रेट लिमिट है?",
    "faq.rate_limit.answer_html": (
        "हाँ: किसी भी रोलिंग 24-घंटे की विंडो में प्रति क्लाइंट IP 10 विश्लेषण। रिस्पॉन्स में "
        "<code>X-RateLimit-Remaining</code> हेडर होता है, और सीमा से ऊपर के रिक्वेस्ट पर 429 "
        "स्टेटस के साथ <code>Retry-After</code> हेडर मिलता है।"
    ),
    # Navigation
    "nav.detector": "डिटेक्टर",
    "nav.how_it_works": "यह कैसे काम करता है",
    "nav.how-to-tell-if-an-image-is-ai-generated": "गाइड",
    "nav.api": "API",
    "nav.self-host": "सेल्फ़-होस्ट",
    # Footer
    "footer.remove-image-metadata": "मेटाडेटा हटाएँ",
    "footer.c2pa": "C2PA",
    "footer.faq": "सामान्य प्रश्न",
    "footer.privacy": "प्राइवेसी",
    "footer.self-host": "सेल्फ़-होस्ट",
    "footer.about": "परिचय",
    # UI strings
    "ui.nav_aria_label": "मुख्य नेविगेशन",
    "ui.loading_status": "डिटेक्टर लोड हो रहा है…",
    "ui.hero_overline": "— ओपन-सोर्स AI इमेज फ़ॉरेंसिक्स",
    "ui.hero_heading_line1": "क्या यह तस्वीर असली है?",
    "ui.hero_heading_line2": "स्कोर और सबूत पाएँ।",
    "ui.tool_aria_label": "AI इमेज डिटेक्टर",
    "ui.dropzone_aria_label": "विश्लेषण के लिए एक इमेज अपलोड करें",
    "ui.dropzone_title_fine": "फ़ोटो को ड्रैग करके यहाँ छोड़ें",
    "ui.dropzone_title_coarse": "एक फ़ोटो जाँचें",
    "ui.dropzone_sub_fine": "या क्लिपबोर्ड से पेस्ट करें, या",
    "ui.dropzone_sub_coarse": "अपनी लाइब्रेरी या कैमरे से",
    "ui.btn_check_image_fine": "यह इमेज जाँचें",
    "ui.btn_choose_photo_coarse": "फ़ोटो चुनें",
    "ui.btn_take_photo": "फ़ोटो लें",
    "ui.dismiss_aria_label": "बंद करें",
    "ui.analyzing_prefix": "विश्लेषण हो रहा है",
    "ui.analyzing_suffix": "· पिक्सल · मेटाडेटा ब्लॉक्स",
    "ui.verdict_overline": "— नतीजा",
    "ui.meter_real": "असली",
    "ui.meter_uncertain": "अनिश्चित",
    "ui.meter_ai": "AI",
    "ui.model_label": "मॉडल",
    "ui.verdict_disclaimer_html": (
        "नतीजे एक क्लासिफ़ायर की संभावनाएँ हैं, अंतिम फ़ैसला नहीं। "
        '<a href="/how-accurate">स्कोर को कैसे पढ़ें।</a>'
    ),
    "ui.btn_check_another": "दूसरी इमेज जाँचें",
    "ui.preview_overline": "— पूर्वावलोकन",
    "ui.preview_alt": "अपलोड की गई इमेज का पूर्वावलोकन",
    "ui.metadata_overline": "— मेटाडेटा",
    "ui.metadata_heading": "फ़ाइल में यह मिला।",
    "ui.jpeg_segments_label": "JPEG सेगमेंट",
    "ui.btn_download_clean": "साफ़ कॉपी डाउनलोड करें",
    "ui.metadata_scrub_note_html": (
        "इमेज को पिक्सल से फिर से रेंडर किया गया है, इसलिए ऊपर के सभी ब्लॉक्स हट चुके हैं। "
        '<a href="/remove-image-metadata">यह कैसे काम करता है</a>'
    ),
    "ui.how_it_works_overline": "— यह कैसे काम करता है",
    "ui.how_it_works_heading": "तीन चरण। कुछ भी सेव नहीं होता।",
    "ui.how_it_works_links_html": (
        '<a href="/how-to-tell-if-an-image-is-ai-generated">AI इमेज पहचानने की गाइड पढ़ें</a> '
        'या <a href="/self-host">इसे अपनी मशीन पर चलाएँ</a>।'
    ),
    "ui.faq_overline": "— सामान्य प्रश्न",
    "ui.faq_heading": "पूछने से पहले।",
    "ui.faq_more_link": "और सवाल-जवाब देखें →",
    "ui.footer_tagline": "picai. · ओपन सोर्स",
    "ui.footer_detector_label": "डिटेक्टर:",
    "ui.breadcrumb_aria_label": "ब्रेडक्रंब",
    "ui.last_updated_prefix": "आख़िरी बार अपडेट हुआ",
    "ui.source_on_github": "GitHub पर सोर्स कोड",
    "ui.btn_try_detector": "डिटेक्टर आज़माएँ",
    "ui.status_ready": "डिटेक्टर तैयार है",
    "ui.status_unreachable": "सर्वर तक नहीं पहुँचा जा सका",
    "ui.loading_model_note": "डिटेक्टर मॉडल लोड हो रहा है (पहली बार चलाने पर ~750 MB डाउनलोड होगा)…",
    "ui.error_empty_file": "यह फ़ाइल खाली है।",
    "ui.error_file_too_large": "{name} का आकार {size} है — सीमा 50 MB है।",
    "ui.error_server_unreachable": "सर्वर से संपर्क नहीं हो सका: {message}",
    "ui.verdict_ai": "संभवतः AI-जनरेटेड",
    "ui.verdict_real": "संभवतः एक असली फ़ोटो",
    "ui.verdict_uncertain": "अनिश्चित",
    "ui.confidence_suffix": "कॉन्फ़िडेंस",
    "ui.format_unknown": "अज्ञात",
    "ui.metadata_present": "मौजूद",
    "ui.metadata_not_present": "मौजूद नहीं",
    "ui.no_jpeg_segments": "कोई JPEG APP सेगमेंट नहीं",
    "ui.quota_remaining": "आज के लिए {limit} में से {remaining} विश्लेषण बाक़ी हैं",
}
