"""Bengali translation table. Falls back to English (see aipicdetect.content.locales) for
any key missing here, so this file only needs to define what has actually been translated.
"""

from __future__ import annotations

STRINGS: dict[str, str] = {
    # Page metadata
    "page.home.title": "AiPicDetect — ওপেন-সোর্স AI ইমেজ ডিটেক্টর ও মেটাডেটা স্ক্রাবার",
    "page.home.description": (
        "AiPicDetect দিয়ে যাচাই করুন কোনো ছবি AI দিয়ে তৈরি কিনা — এটি একটি বিনামূল্যের, ওপেন-সোর্স "
        "ডিটেক্টর। ব্রাউজারে ব্যবহার করুন অথবা Docker বা Python দিয়ে নিজের কম্পিউটারে চালান।"
    ),
    "page.home.h1": "এই ছবিটি কি আসল? স্কোর ও প্রমাণ দেখুন।",
    "page.faq.title": "AI ইমেজ ডিটেক্টর সংক্রান্ত সাধারণ প্রশ্ন: নির্ভুলতা, প্রাইভেসি, ফরম্যাট, মডেল",
    "page.faq.description": (
        "AiPicDetect সম্পর্কে সাধারণ প্রশ্নের উত্তর: AI ইমেজ শনাক্তকরণ কতটা নির্ভুল, আপনার ছবি কোথায় "
        "প্রসেস হয়, কোন ফরম্যাট সমর্থিত, মডেল পরিবর্তন এবং রেট লিমিট।"
    ),
    "page.faq.h1": "AiPicDetect সম্পর্কিত সাধারণ জিজ্ঞাসা",
    "page.faq.intro_suffix": (
        "এটি কীভাবে কাজ করে, কতটা নির্ভুল, এবং আপলোড করা ছবির সঙ্গে কী ঘটে — এই বিষয়ে মানুষ "
        "সবচেয়ে বেশি যে প্রশ্নগুলো করে থাকেন, সেগুলোই এখানে দেওয়া হলো।"
    ),
    "page.faq.still_unsure_html": (
        'এখনও নিশ্চিত নন? <a href="https://github.com/Micorlov/aipicdetect/issues" rel="noopener">'
        "GitHub</a>-এ একটি issue খুলুন।"
    ),
    # Home page copy
    "home.entity_sentence": (
        "AiPicDetect একটি বিনামূল্যের, ওপেন-সোর্স টুল যা কোনো ছবি AI দিয়ে তৈরি কিনা তার স্কোর দেয় এবং "
        "লুকানো মেটাডেটা মুছে ফেলে — হোস্টেড ব্যবহার করুন বা নিজে হোস্ট করুন, পছন্দ আপনার।"
    ),
    "home.lead": (
        "AiPicDetect একটি ওপেন AI-শনাক্তকরণ মডেল চালায় এবং একটি ছবিতে থাকা প্রতিটি EXIF, C2PA ও IPTC "
        "ফিল্ড পড়ে — তারপর সেগুলো মুছে দিয়ে আপনাকে একটি পরিষ্কার কপি দেয়। কোনো সাইন-আপ নেই, কোনো "
        "ব্ল্যাক বক্স নেই।"
    ),
    "home.dropzone_note": (
        "JPEG, PNG, WebP, HEIC · সর্বোচ্চ 50 MB পর্যন্ত · মেমোরিতে প্রসেস হয়, কখনো ডিস্কে লেখা "
        "হয় না"
    ),
    "home.summary": (
        "AiPicDetect একটি বিনামূল্যের, ওপেন-সোর্স টুল যা কোনো ছবি AI দিয়ে তৈরি কিনা তার স্কোর দেয় এবং "
        "লুকানো মেটাডেটা মুছে ফেলে — হোস্টেড ব্যবহার করুন বা নিজে হোস্ট করুন, পছন্দ আপনার। এটি একটি "
        "ওপেন Hugging Face ক্লাসিফায়ার ব্যবহার করে অনুমান করে যে কোনো ছবি AI জেনারেটর দিয়ে তৈরি "
        "হওয়ার সম্ভাবনা কতটা, এবং EXIF, XMP, IPTC, ICC ও C2PA মেটাডেটা মুছে ফেলতে ছবি পুনরায় "
        "রেন্ডার করতে পারে। হোস্টেড ইনস্ট্যান্স ব্যবহার করুন অথবা Docker বা Python দিয়ে নিজে হোস্ট "
        "করুন।"
    ),
    "home.stat.0": "ওপেন মডেল,<br>কোনো থার্ড-পার্টি API নেই",
    "home.stat.1": "সাইন-আপের<br>প্রয়োজন নেই",
    "home.stat.2": "MB সর্বোচ্চ<br>আপলোড",
    # Detect steps
    "steps.detect.upload.name": "আপলোড করুন।",
    "steps.detect.detect.name": "শনাক্ত করুন।",
    "steps.detect.decide.name": "সিদ্ধান্ত নিন।",
    "steps.detect.upload.text": (
        "একটি ছবি ড্রপ করুন, পেস্ট করুন অথবা বেছে নিন। এটি আপনার ব্যবহৃত AiPicDetect সার্ভারে পাঠানো হয় "
        "(সেল্ফ-হোস্ট করলে সেটি আপনার নিজের কম্পিউটার), মেমোরিতে রাখা হয় এবং কখনো ডিস্কে লেখা হয় না।"
    ),
    "steps.detect.detect.text": (
        "একটি ওপেন-সোর্স ইমেজ ক্লাসিফায়ার অনুমান করে যে পিক্সেলগুলো কোনো জেনারেটর দিয়ে তৈরি হওয়ার "
        "সম্ভাবনা কতটা।"
    ),
    "steps.detect.decide.text": (
        "আপনি পান একটি AI সম্ভাবনা, একটি কনফিডেন্স ব্যান্ড, এবং ফাইলে থাকা মেটাডেটা ব্লক — একটি "
        "সম্ভাবনা হিসেবে, চূড়ান্ত রায় হিসেবে নয়।"
    ),
    # Scrub steps — <code> blocks contain literal shell commands and must stay untranslated
    "steps.scrub.inspect.name": "পরীক্ষা করুন।",
    "steps.scrub.scrub.name": "স্ক্রাব করুন।",
    "steps.scrub.verify.name": "যাচাই করুন।",
    "steps.scrub.inspect.text": (
        "ফাইলে থাকা EXIF, XMP, IPTC, C2PA ও ICC ব্লকের তালিকা দেখতে "
        "<code>aipicdetect inspect photo.jpg</code> চালান।"
    ),
    "steps.scrub.scrub.text": (
        "<code>aipicdetect scrub photo.jpg</code> (অথবা <code>POST /scrub</code>) চালান। AiPicDetect পিক্সেল "
        "ডিকোড করে, EXIF ওরিয়েন্টেশন প্রয়োগ করে, এবং কাঁচা পিক্সেল বাফার থেকে একেবারে নতুন একটি "
        "ছবি তৈরি করে।"
    ),
    "steps.scrub.verify.text": (
        "<code>aipicdetect inspect photo.clean.jpg</code> চালান; এটি “no metadata signatures found” "
        "প্রিন্ট করা উচিত।"
    ),
    # FAQ (home slugs)
    "faq.accuracy.question": "ডিটেক্টরটি কতটা নির্ভুল?",
    "faq.accuracy.answer_html": (
        "এটি একটি সম্ভাবনা জানায়, চূড়ান্ত রায় নয়। 50%-এর কাছাকাছি স্কোরকে <em>অনিশ্চিত</em> "
        "লেবেল দেওয়া হয়; যেকোনো একক ফলাফলকে একটি ইঙ্গিত হিসেবে ধরুন এবং অন্যান্য প্রমাণের সঙ্গে "
        'মিলিয়ে দেখুন। <a href="/how-accurate">AI ইমেজ ডিটেক্টর কতটা নির্ভুল</a> সে বিষয়ে আরও পড়ুন।'
    ),
    "faq.leaves_computer.question": "আমার ছবি কি আমার কম্পিউটার থেকে বাইরে যায়?",
    "faq.leaves_computer.answer_html": (
        "এই পাবলিক ইনস্ট্যান্সে, হ্যাঁ: ছবিটি AiPicDetect সার্ভারে (লেখকের চালানো একটি Google Cloud Run "
        "কনটেইনার) আপলোড হয়, মেমোরিতে স্কোর করা হয় এবং কখনো ডিস্কে লেখা হয় না। স্ক্রাব করা কপিটি "
        "মেমোরিতে ততক্ষণই থাকে যতক্ষণ না 100টি নতুন ফলাফল সেটির জায়গা নেয় অথবা কনটেইনার রিস্টার্ট "
        "হয়, এবং কোনো কিছুই কোনো থার্ড-পার্টি API-তে পাঠানো হয় না। আপনি যদি চান যে আপনার কম্পিউটার "
        'থেকে কিছুই বাইরে না যাক, তাহলে একটিমাত্র Docker কমান্ড দিয়ে <a href="/self-host">AiPicDetect '
        'নিজে চালান</a>। বিস্তারিত আছে <a href="/privacy">প্রাইভেসি পেজে</a>।'
    ),
    "faq.open_source.question": "এটি কি ওপেন সোর্স?",
    "faq.open_source.answer_html": (
        "হ্যাঁ। কোড, Docker ইমেজ, CLI এবং GitHub Action সবই MIT লাইসেন্সের অধীনে "
        '<a href="https://github.com/Micorlov/aipicdetect" rel="noopener">AiPicDetect রিপোজিটরিতে</a> আছে। '
        "ডিটেক্টরটি একটি ওপেন Hugging Face মডেল, যা আপনি পরীক্ষা করতে বা প্রতিস্থাপন করতে পারেন।"
    ),
    "faq.remove_metadata.question": "আমি কি C2PA ও অন্যান্য মেটাডেটা মুছে ফেলতে পারি?",
    "faq.remove_metadata.answer_html": (
        "হ্যাঁ। একটি ছবি যাচাই করার পর, <em>পরিষ্কার কপি ডাউনলোড করুন</em> ব্যবহার করুন। AiPicDetect "
        "ছবিটিকে তার পিক্সেল থেকে পুনর্নির্মাণ করে, ফলে EXIF, XMP, IPTC, C2PA ও ICC প্রোফাইল "
        'সবকিছু ফেলে দেওয়া হয়। <a href="/remove-image-metadata">স্ক্রাবার কীভাবে কাজ করে</a>।'
    ),
    "faq.formats.question": "কোন ফরম্যাট সমর্থিত?",
    "faq.formats.answer_html": (
        "JPEG, PNG, WebP, HEIC/HEIF এবং Pillow যেসব ফরম্যাট ডিকোড করতে পারে তার বেশিরভাগই, "
        "সর্বোচ্চ 50 MB পর্যন্ত।"
    ),
    "faq.why_metadata.question": "মেটাডেটা কেন দেখানো হয়?",
    "faq.why_metadata.answer_html": (
        "C2PA কনটেন্ট ক্রেডেনশিয়াল ও এডিটিং-সফটওয়্যার ট্যাগ ছবির উৎস সম্পর্কে ইঙ্গিত দেয়। "
        "প্যানেলটি দেখায় ফাইলে কোন ব্লকগুলো (EXIF, XMP, IPTC, C2PA, ICC) আছে, যাতে আপনি সেগুলো "
        'স্কোরের সঙ্গে মিলিয়ে বিবেচনা করতে পারেন। দেখুন <a href="/c2pa">C2PA কনটেন্ট '
        'ক্রেডেনশিয়াল</a> এবং <a href="/remove-image-metadata">ছবির মেটাডেটা কীভাবে মুছবেন</a>।'
    ),
    "faq.different_model.question": "আমি কি ভিন্ন একটি মডেল ব্যবহার করতে পারি?",
    "faq.different_model.answer_html": (
        "হ্যাঁ। <code>PICAI_DETECTOR_MODEL</code>-কে এমন যেকোনো Hugging Face ইমেজ-ক্লাসিফিকেশন "
        "মডেলে সেট করুন, যার লেবেলগুলো AI/ভুয়া বনাম মানুষ/আসল কনটেন্টের নাম দেয়।"
    ),
    # FAQ (more slugs)
    "faq.free.question": "AiPicDetect কি বিনামূল্যে?",
    "faq.free.answer_html": (
        "হ্যাঁ। AiPicDetect MIT লাইসেন্সের অধীনে ওপেন সোর্স। হোস্টেড ইনস্ট্যান্স বিনামূল্যে ব্যবহারযোগ্য, "
        "তবে প্রতি IP ঠিকানায় প্রতি 24 ঘণ্টায় 10টি বিশ্লেষণের সীমা আছে; সেল্ফ-হোস্টেড কপির কোনো "
        "সীমা নেই।"
    ),
    "faq.screenshots.question": "এটি কি স্ক্রিনশট বা ভারী কম্প্রেস করা ছবিতে কাজ করে?",
    "faq.screenshots.answer_html": (
        "এটি কাজ করে, তবে রি-এনকোডিং, রিসাইজিং ও স্ক্রিনশট নেওয়ার ফলে পিক্সেল-স্তরের কিছু চিহ্ন "
        "হারিয়ে যায় যার ওপর ক্লাসিফায়ার নির্ভর করে, তাই কম কনফিডেন্স এবং বেশি <em>অনিশ্চিত</em> "
        "ফলাফল আশা করুন।"
    ),
    "faq.which_generator.question": (
        "এটি কি বলতে পারে কোন জেনারেটর ছবিটি তৈরি করেছে (Midjourney, DALL·E, Stable Diffusion)?"
    ),
    "faq.which_generator.answer_html": (
        "না। AiPicDetect সাধারণভাবে জেনারেটেড বনাম আসল পিক্সেলের পরিসংখ্যান স্কোর করে; এটি নির্দিষ্ট "
        "জেনারেটর শনাক্ত করে না, এবং যেসব জেনারেটর এর মডেলের ট্রেনিং ডেটা সংগ্রহের পরে প্রকাশ "
        "পেয়েছে সেগুলো সম্পর্কে এর কোনো ধারণা নেই।"
    ),
    "faq.false_positive.question": "একটি আসল ছবি কেন AI হিসেবে স্কোর পেল?",
    "faq.false_positive.answer_html": (
        "ভারী ফিল্টার, HDR প্রসেসিং, আপস্কেলিং, ইলাস্ট্রেশন ও 3D রেন্ডারে জেনারেটেড ছবির সঙ্গে মিল "
        "থাকা পরিসংখ্যানগত বৈশিষ্ট্য থাকে। এই স্কোর একটি সম্ভাবনা, প্রমাণ নয়; ফলস পজিটিভ ঘটতে পারে।"
    ),
    "faq.offline.question": "আমি কি এটি অফলাইনে চালাতে পারি?",
    "faq.offline.answer_html": (
        "হ্যাঁ। প্রথমবার চালানোর সময় মডেলটি Hugging Face ক্যাশে ডাউনলোড হয়ে যাওয়ার পর, "
        "সেল্ফ-হোস্টেড AiPicDetect-র কোনো নেটওয়ার্ক অ্যাক্সেসের প্রয়োজন হয় না।"
    ),
    "faq.rate_limit.question": "হোস্টেড ইনস্ট্যান্সে কি কোনো রেট লিমিট আছে?",
    "faq.rate_limit.answer_html": (
        "হ্যাঁ: যেকোনো রোলিং 24-ঘণ্টার উইন্ডোতে প্রতি ক্লায়েন্ট IP-তে 10টি বিশ্লেষণ। রেসপন্সে "
        "<code>X-RateLimit-Remaining</code> হেডার থাকে, এবং সীমার বেশি অনুরোধে "
        "<code>Retry-After</code> হেডারসহ 429 স্ট্যাটাস ফেরত আসে।"
    ),
    # Navigation
    "nav.detector": "ডিটেক্টর",
    "nav.how_it_works": "এটি কীভাবে কাজ করে",
    "nav.how-to-tell-if-an-image-is-ai-generated": "গাইড",
    "nav.api": "API",
    "nav.self-host": "সেল্ফ-হোস্ট",
    # Footer
    "footer.remove-image-metadata": "মেটাডেটা মুছুন",
    "footer.c2pa": "C2PA",
    "footer.faq": "সাধারণ প্রশ্ন",
    "footer.privacy": "প্রাইভেসি",
    "footer.self-host": "সেল্ফ-হোস্ট",
    "footer.about": "সম্পর্কে",
    # UI strings
    "ui.nav_aria_label": "প্রধান নেভিগেশন",
    "ui.loading_status": "ডিটেক্টর লোড হচ্ছে…",
    "ui.hero_overline": "— ওপেন-সোর্স AI ইমেজ ফরেনসিক্স",
    "ui.hero_heading_line1": "এই ছবিটি কি আসল?",
    "ui.hero_heading_line2": "স্কোর ও প্রমাণ দেখুন।",
    "ui.tool_aria_label": "AI ইমেজ ডিটেক্টর",
    "ui.dropzone_aria_label": "বিশ্লেষণের জন্য একটি ছবি আপলোড করুন",
    "ui.dropzone_title_fine": "একটি ছবি ড্র্যাগ ও ড্রপ করুন",
    "ui.dropzone_title_coarse": "একটি ছবি যাচাই করুন",
    "ui.dropzone_sub_fine": "অথবা ক্লিপবোর্ড থেকে পেস্ট করুন, বা",
    "ui.dropzone_sub_coarse": "আপনার লাইব্রেরি বা ক্যামেরা থেকে",
    "ui.btn_check_image_fine": "এই ছবিটি যাচাই করুন",
    "ui.btn_choose_photo_coarse": "ছবি বেছে নিন",
    "ui.btn_take_photo": "ছবি তুলুন",
    "ui.dismiss_aria_label": "বাতিল করুন",
    "ui.analyzing_prefix": "বিশ্লেষণ চলছে",
    "ui.analyzing_suffix": "· পিক্সেল · মেটাডেটা ব্লক",
    "ui.verdict_overline": "— রায়",
    "ui.meter_real": "আসল",
    "ui.meter_uncertain": "অনিশ্চিত",
    "ui.meter_ai": "AI",
    "ui.model_label": "মডেল",
    "ui.verdict_disclaimer_html": (
        "ফলাফলগুলো একটি ক্লাসিফায়ারের সম্ভাবনা, চূড়ান্ত রায় নয়। "
        '<a href="/how-accurate">স্কোর কীভাবে পড়বেন।</a>'
    ),
    "ui.btn_check_another": "আরেকটি ছবি যাচাই করুন",
    "ui.preview_overline": "— প্রিভিউ",
    "ui.preview_alt": "আপলোড করা ছবির প্রিভিউ",
    "ui.metadata_overline": "— মেটাডেটা",
    "ui.metadata_heading": "ফাইলে যা পাওয়া গেছে।",
    "ui.jpeg_segments_label": "JPEG সেগমেন্ট",
    "ui.btn_download_clean": "পরিষ্কার কপি ডাউনলোড করুন",
    "ui.metadata_scrub_note_html": (
        "পিক্সেল থেকে পুনরায় রেন্ডার করা হয়েছে, তাই ওপরের প্রতিটি ব্লক মুছে গেছে। "
        '<a href="/remove-image-metadata">এটি কীভাবে কাজ করে</a>'
    ),
    "ui.how_it_works_overline": "— এটি কীভাবে কাজ করে",
    "ui.how_it_works_heading": "তিনটি ধাপ। কিছুই সংরক্ষণ করা হয় না।",
    "ui.how_it_works_links_html": (
        '<a href="/how-to-tell-if-an-image-is-ai-generated">AI ছবি শনাক্ত করার গাইড পড়ুন</a> '
        'অথবা <a href="/self-host">নিজের কম্পিউটারে চালান</a>।'
    ),
    "ui.faq_overline": "— সাধারণ প্রশ্ন",
    "ui.faq_heading": "প্রশ্ন করার আগে।",
    "ui.faq_more_link": "আরও প্রশ্ন ও উত্তর →",
    "ui.footer_tagline": "AiPicDetect. · ওপেন সোর্স",
    "ui.footer_detector_label": "ডিটেক্টর:",
    "ui.breadcrumb_aria_label": "ব্রেডক্রাম্ব",
    "ui.last_updated_prefix": "সর্বশেষ আপডেট",
    "ui.source_on_github": "GitHub-এ সোর্স কোড",
    "ui.btn_try_detector": "ডিটেক্টর ব্যবহার করে দেখুন",
    "ui.status_ready": "ডিটেক্টর প্রস্তুত",
    "ui.status_unreachable": "সার্ভারে পৌঁছানো যাচ্ছে না",
    "ui.loading_model_note": "ডিটেক্টর মডেল লোড হচ্ছে (প্রথমবার চালালে প্রায় 750 MB ডাউনলোড হবে)…",
    "ui.error_empty_file": "ফাইলটি খালি।",
    "ui.error_file_too_large": "{name} এর আকার {size} — সীমা 50 MB।",
    "ui.error_server_unreachable": "সার্ভারে পৌঁছানো যায়নি: {message}",
    "ui.verdict_ai": "সম্ভবত AI-নির্মিত",
    "ui.verdict_real": "সম্ভবত একটি আসল ছবি",
    "ui.verdict_uncertain": "অনিশ্চিত",
    "ui.confidence_suffix": "কনফিডেন্স",
    "ui.format_unknown": "অজানা",
    "ui.metadata_present": "আছে",
    "ui.metadata_not_present": "নেই",
    "ui.no_jpeg_segments": "কোনো JPEG APP সেগমেন্ট নেই",
    "ui.quota_remaining": "আজ {limit}টির মধ্যে {remaining}টি বিশ্লেষণ বাকি আছে",
}
