"""Hebrew translation table. Falls back to English (see picai.content.locales) for any key
missing here, so this file only needs to define what has actually been translated.

Text is written as plain right-to-left prose; no directional markup is added here because the
page itself sets dir="rtl" for this locale.
"""

from __future__ import annotations

STRINGS: dict[str, str] = {
    "page.home.title": "picai — גלאי תמונות בינה מלאכותית וכלי לניקוי מטא-דאטה בקוד פתוח",
    "page.home.description": (
        "בדקו אם תמונה נוצרה על ידי בינה מלאכותית באמצעות picai, גלאי חינמי ובקוד פתוח. השתמשו בו "
        "בדפדפן או הריצו אותו במחשב שלכם עם Docker או Python."
    ),
    "page.home.h1": "האם התמונה הזו אמיתית? קבלו את הציון וההוכחה.",
    "page.faq.title": "שאלות נפוצות על גלאי תמונות בינה מלאכותית: דיוק, פרטיות, פורמטים, מודלים",
    "page.faq.description": (
        "תשובות לשאלות נפוצות על picai: עד כמה גילוי תמונות בינה מלאכותית מדויק, היכן מעובדת "
        "התמונה שלכם, פורמטים נתמכים, החלפת מודל ומגבלות שימוש."
    ),
    "page.faq.h1": "שאלות נפוצות על picai",
    "page.faq.intro_suffix": "אלה השאלות שהכי שואלים על איך זה עובד, כמה זה מדויק, ומה קורה לתמונות שמעלים.",
    "page.faq.still_unsure_html": (
        'עדיין לא בטוחים? פתחו issue ב-<a href="https://github.com/Micorlov/picai/issues" '
        'rel="noopener">GitHub</a>.'
    ),
    "home.entity_sentence": (
        "picai הוא כלי חינמי בקוד פתוח שמדרג תמונות שנוצרו בבינה מלאכותית ומסיר מטא-דאטה נסתרת — "
        "מתארח או באירוח עצמי, הבחירה בידיכם."
    ),
    "home.lead": (
        "picai מריץ מודל גילוי בינה מלאכותית בקוד פתוח וקורא כל שדה EXIF, C2PA ו-IPTC שהתמונה "
        "נושאת — ואז מעביר לכם עותק נקי שממנו הוסר הכול. בלי הרשמה, בלי קופסה שחורה."
    ),
    "home.dropzone_note": "JPEG, PNG, WebP, HEIC · עד 50 MB · מעובד בזיכרון, לעולם לא נכתב לדיסק",
    "home.summary": (
        "picai הוא כלי חינמי בקוד פתוח שמדרג תמונות שנוצרו בבינה מלאכותית ומסיר מטא-דאטה נסתרת — "
        "מתארח או באירוח עצמי, הבחירה בידיכם. הוא מעריך את הסבירות שתמונה הופקה על ידי מחולל בינה "
        "מלאכותית באמצעות מסווג פתוח של Hugging Face, ויכול לעבד מחדש תמונות כדי להסיר מטא-דאטה "
        "מסוג EXIF, XMP, IPTC, ICC ו-C2PA. השתמשו במופע המתארח או הריצו אותו בעצמכם עם Docker או Python."
    ),
    "home.stat.0": "מודל פתוח,<br>ללא API של צד שלישי",
    "home.stat.1": "הרשמות<br>נדרשות",
    "home.stat.2": "MB מקסימום<br>להעלאה",
    "steps.detect.upload.name": "העלאה.",
    "steps.detect.detect.name": "גילוי.",
    "steps.detect.decide.name": "החלטה.",
    "steps.detect.upload.text": (
        "גררו, הדביקו או בחרו תמונה. היא נשלחת לשרת picai שבו אתם משתמשים (המחשב שלכם, במקרה של "
        "אירוח עצמי), נשמרת בזיכרון ולעולם לא נכתבת לדיסק."
    ),
    "steps.detect.detect.text": (
        "מסווג תמונות בקוד פתוח מעריך את הסבירות שהפיקסלים הופקו על ידי מחולל."
    ),
    "steps.detect.decide.text": (
        "תקבלו סבירות לבינה מלאכותית, טווח ביטחון ואת בלוקי המטא-דאטה שהקובץ נושא — כהסתברות, לא כפסיקה."
    ),
    # steps.scrub.*.text carries inline <code>...</code> shell commands — preserved verbatim below,
    # only the surrounding prose is translated.
    "steps.scrub.inspect.name": "בדיקה.",
    "steps.scrub.scrub.name": "ניקוי.",
    "steps.scrub.verify.name": "אימות.",
    "steps.scrub.inspect.text": (
        "הריצו <code>picai inspect photo.jpg</code> כדי לרשום את בלוקי EXIF, XMP, IPTC, C2PA ו-ICC "
        "שהקובץ נושא."
    ),
    "steps.scrub.scrub.text": (
        "הריצו <code>picai scrub photo.jpg</code> (או <code>POST /scrub</code>). picai מפענח את "
        "הפיקסלים, מיישם את כיוון ה-EXIF, ובונה תמונה חדשה לגמרי ממאגר הפיקסלים הגולמי."
    ),
    "steps.scrub.verify.text": (
        'הריצו <code>picai inspect photo.clean.jpg</code>; הפלט אמור להציג "no metadata signatures found".'
    ),
    "faq.accuracy.question": "עד כמה הגלאי מדויק?",
    "faq.leaves_computer.question": "האם התמונה שלי יוצאת מהמחשב שלי?",
    "faq.open_source.question": "האם זה בקוד פתוח?",
    "faq.remove_metadata.question": "האם אפשר להסיר C2PA ומטא-דאטה אחרת?",
    "faq.formats.question": "אילו פורמטים נתמכים?",
    "faq.why_metadata.question": "למה מוצגת מטא-דאטה?",
    "faq.different_model.question": "האם אפשר להשתמש במודל אחר?",
    "faq.free.question": "האם picai חינמי?",
    "faq.screenshots.question": "האם זה עובד על צילומי מסך או תמונות דחוסות מאוד?",
    "faq.which_generator.question": (
        "האם אפשר לזהות איזה מחולל יצר תמונה (Midjourney, DALL·E, Stable Diffusion)?"
    ),
    "faq.false_positive.question": "למה תמונה אמיתית קיבלה ציון של בינה מלאכותית?",
    "faq.offline.question": "האם אפשר להריץ את זה במצב לא מקוון?",
    "faq.rate_limit.question": "האם יש מגבלת קצב במופע המתארח?",
    "faq.accuracy.answer_html": (
        "הוא מציג הסתברות, לא פסיקה. ציונים סביב 50% מסומנים כ-<em>לא ודאי</em>; יש להתייחס לכל "
        "תוצאה בודדת כאל אינדיקציה ולשלב אותה עם ראיות נוספות. מידע נוסף על "
        '<a href="/how-accurate">עד כמה גלאי תמונות בינה מלאכותית מדויקים</a>.'
    ),
    "faq.leaves_computer.answer_html": (
        "במופע הציבורי הזה, כן: התמונה מועלית לשרת picai (קונטיינר של Google Cloud Run שמופעל על "
        "ידי היוצר), מדורגת בזיכרון ולעולם לא נכתבת לדיסק. העותק הנקי נשמר בזיכרון רק עד ש-100 "
        "תוצאות חדשות יותר מחליפות אותו או שהקונטיינר מופעל מחדש, ושום דבר לא נשלח ל-API של צד "
        'שלישי. אם אתם רוצים שדבר לא יצא מהמחשב שלכם, <a href="/self-host">הריצו את picai '
        'בעצמכם</a> בפקודת Docker אחת. פרטים נוספים נמצאים ב<a href="/privacy">עמוד הפרטיות</a>.'
    ),
    "faq.open_source.answer_html": (
        "כן. הקוד, תמונת ה-Docker, כלי שורת הפקודה וה-GitHub Action כולם נמצאים במאגר "
        '<a href="https://github.com/Micorlov/picai" rel="noopener">picai</a> תחת רישיון MIT. '
        "הגלאי הוא מודל פתוח של Hugging Face שאפשר לבדוק או להחליף."
    ),
    "faq.remove_metadata.answer_html": (
        "כן. אחרי בדיקת תמונה, השתמשו ב<em>הורדת עותק נקי</em>. picai בונה מחדש את התמונה "
        "מהפיקסלים שלה, כך ש-EXIF, XMP, IPTC, C2PA ופרופיל ה-ICC כולם מוסרים. "
        '<a href="/remove-image-metadata">איך הכלי לניקוי עובד</a>.'
    ),
    "faq.formats.answer_html": (
        "JPEG, PNG, WebP, HEIC/HEIF ורוב הפורמטים שספריית Pillow יודעת לפענח, עד 50 MB."
    ),
    "faq.why_metadata.answer_html": (
        "אישורי תוכן C2PA ותגיות של תוכנות עריכה הם רמזי מקור. הפאנל מציג אילו בלוקים (EXIF, XMP, "
        "IPTC, C2PA, ICC) הקובץ נושא כדי שתוכלו לשקול אותם יחד עם הציון. ראו "
        '<a href="/c2pa">אישורי תוכן C2PA</a> וגם <a href="/remove-image-metadata">איך להסיר '
        "מטא-דאטה מתמונה</a>."
    ),
    "faq.different_model.answer_html": (
        "כן. הגדירו את <code>PICAI_DETECTOR_MODEL</code> לכל מודל סיווג תמונות של Hugging Face "
        "שהתוויות שלו מבחינות בין תוכן בינה-מלאכותית/מזויף לבין תוכן אנושי/אמיתי."
    ),
    "faq.free.answer_html": (
        "כן. picai הוא קוד פתוח תחת רישיון MIT. המופע המתארח חינמי לשימוש עם מגבלה של 10 ניתוחים "
        "לכתובת IP בכל 24 שעות; עותק באירוח עצמי ללא מגבלה."
    ),
    "faq.screenshots.answer_html": (
        "זה עובד, אבל קידוד מחדש, שינוי גודל וצילומי מסך מסירים חלק מהעקבות ברמת הפיקסל שעליהן "
        "המסווג מסתמך, ולכן צפו לביטחון נמוך יותר וליותר תוצאות <em>לא ודאי</em>."
    ),
    "faq.which_generator.answer_html": (
        "לא. picai מדרג באופן כללי סטטיסטיקות פיקסלים של תוכן מיוצר מול אמיתי; הוא לא מזהה את "
        "המחולל הספציפי, ואין לו ידע על מחוללים שיצאו לאחר שנאספו נתוני האימון של המודל שלו."
    ),
    "faq.false_positive.answer_html": (
        "פילטרים חזקים, עיבוד HDR, הגדלת רזולוציה, איורים ורינדורים תלת-ממדיים חולקים מאפיינים "
        "סטטיסטיים עם תמונות מיוצרות. הציון הוא הסתברות, לא הוכחה; תוצאות שגויות-חיוביות קורות."
    ),
    "faq.offline.answer_html": (
        "כן. אחרי שההרצה הראשונה מורידה את המודל למטמון של Hugging Face, picai באירוח עצמי לא "
        "זקוק לגישה לרשת."
    ),
    "faq.rate_limit.answer_html": (
        "כן: 10 ניתוחים לכתובת IP של לקוח בכל חלון נע של 24 שעות. התגובות כוללות "
        "<code>X-RateLimit-Remaining</code>, ובקשה שחורגת מהמגבלה מחזירה קוד 429 עם כותרת "
        "<code>Retry-After</code>."
    ),
    "nav.detector": "גלאי",
    "nav.how_it_works": "איך זה עובד",
    "nav.how-to-tell-if-an-image-is-ai-generated": "מדריך",
    "nav.api": "API",
    "nav.self-host": "אירוח עצמי",
    "footer.remove-image-metadata": "הסרת מטא-דאטה",
    "footer.c2pa": "C2PA",
    "footer.faq": "שאלות נפוצות",
    "footer.privacy": "פרטיות",
    "footer.self-host": "אירוח עצמי",
    "footer.about": "אודות",
    "ui.nav_aria_label": "ניווט ראשי",
    "ui.loading_status": "טוען גלאי…",
    "ui.hero_overline": "— זיהוי פורנזי בקוד פתוח לתמונות בינה מלאכותית",
    "ui.hero_heading_line1": "האם התמונה הזו אמיתית?",
    "ui.hero_heading_line2": "קבלו את הציון וההוכחה.",
    "ui.tool_aria_label": "גלאי תמונות בינה מלאכותית",
    "ui.dropzone_aria_label": "העלו תמונה לניתוח",
    "ui.dropzone_title_fine": "גררו ושחררו תמונה",
    "ui.dropzone_title_coarse": "בדקו תמונה",
    "ui.dropzone_sub_fine": "או הדביקו מהלוח, או",
    "ui.dropzone_sub_coarse": "מהספרייה או מהמצלמה",
    "ui.btn_check_image_fine": "בדקו את התמונה הזו",
    "ui.btn_choose_photo_coarse": "בחרו תמונה",
    "ui.btn_take_photo": "צלמו תמונה",
    "ui.dismiss_aria_label": "סגירה",
    "ui.analyzing_prefix": "מנתח",
    "ui.analyzing_suffix": "· פיקסלים · בלוקי מטא-דאטה",
    "ui.verdict_overline": "— פסיקה",
    "ui.meter_real": "אמיתי",
    "ui.meter_uncertain": "לא ודאי",
    "ui.meter_ai": "בינה מלאכותית",
    "ui.model_label": "מודל",
    "ui.verdict_disclaimer_html": (
        "התוצאות הן הסתברויות ממסווג, לא פסיקות. "
        '<a href="/how-accurate">איך לקרוא את הציון.</a>'
    ),
    "ui.btn_check_another": "בדקו תמונה נוספת",
    "ui.preview_overline": "— תצוגה מקדימה",
    "ui.preview_alt": "תצוגה מקדימה של התמונה שהועלתה",
    "ui.metadata_overline": "— מטא-דאטה",
    "ui.metadata_heading": "נמצא בקובץ.",
    "ui.jpeg_segments_label": "מקטעי JPEG",
    "ui.btn_download_clean": "הורידו את העותק הנקי",
    "ui.metadata_scrub_note_html": (
        "עובד מחדש מהפיקסלים, כך שכל בלוק שלמעלה נעלם. "
        '<a href="/remove-image-metadata">איך זה עובד</a>'
    ),
    "ui.how_it_works_overline": "— איך זה עובד",
    "ui.how_it_works_heading": "שלושה שלבים. שום דבר לא נשמר.",
    "ui.how_it_works_links_html": (
        '<a href="/how-to-tell-if-an-image-is-ai-generated">קראו את המדריך לזיהוי תמונות בינה '
        'מלאכותית</a> או <a href="/self-host">הריצו את זה במחשב שלכם</a>.'
    ),
    "ui.faq_overline": "— שאלות נפוצות",
    "ui.faq_heading": "לפני שתשאלו.",
    "ui.faq_more_link": "עוד שאלות ותשובות →",
    "ui.footer_tagline": "picai. · קוד פתוח",
    "ui.footer_detector_label": "גלאי:",
    "ui.breadcrumb_aria_label": "פירורי לחם",
    "ui.last_updated_prefix": "עודכן לאחרונה",
    "ui.source_on_github": "קוד המקור ב-GitHub",
    "ui.btn_try_detector": "נסו את הגלאי",
    "ui.status_ready": "הגלאי מוכן",
    "ui.status_unreachable": "השרת לא זמין",
    "ui.loading_model_note": "טוען את מודל הגלאי (בהרצה הראשונה מורידים כ-750 MB)…",
    "ui.error_empty_file": "הקובץ הזה ריק.",
    "ui.error_file_too_large": "{name} הוא בגודל {size} — המגבלה היא 50 MB.",
    "ui.error_server_unreachable": "לא ניתן להתחבר לשרת: {message}",
    "ui.verdict_ai": "ככל הנראה נוצר בבינה מלאכותית",
    "ui.verdict_real": "ככל הנראה תמונה אמיתית",
    "ui.verdict_uncertain": "לא ודאי",
    "ui.confidence_suffix": "ביטחון",
    "ui.format_unknown": "לא ידוע",
    "ui.metadata_present": "קיים",
    "ui.metadata_not_present": "לא קיים",
    "ui.no_jpeg_segments": "אין מקטעי APP של JPEG",
    "ui.quota_remaining": "{remaining} מתוך {limit} ניתוחים נותרו היום",
}
