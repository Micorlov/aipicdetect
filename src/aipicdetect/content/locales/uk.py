"""Ukrainian translation table.

Falls back to English (see :func:`aipicdetect.content.locales.t`) for any key not defined here, but
every key from :mod:`aipicdetect.content.locales.en` is translated below.
"""

from __future__ import annotations

STRINGS: dict[str, str] = {
    # Page metadata
    "page.home.title": (
        "AiPicDetect — детектор зображень зі штучним інтелектом і засіб очищення метаданих з відкритим "
        "кодом"
    ),
    "page.home.description": (
        "Перевірте, чи згенеровано зображення штучним інтелектом, за допомогою AiPicDetect — "
        "безкоштовного детектора з відкритим кодом. Використовуйте його в браузері або запустіть "
        "на власному комп’ютері через Docker чи Python."
    ),
    "page.home.h1": "Це фото справжнє? Отримайте оцінку і доказ.",
    "page.faq.title": "Часті запитання про детектор зображень ШІ: точність, приватність, формати, моделі",
    "page.faq.description": (
        "Відповіді на поширені запитання про AiPicDetect: наскільки точний детектор зображень зі "
        "штучним інтелектом, де обробляється ваше зображення, які формати підтримуються, заміна "
        "моделі та ліміти запитів."
    ),
    "page.faq.h1": "Часті запитання про AiPicDetect",
    "page.faq.intro_suffix": (
        "Це запитання, які люди найчастіше ставлять про те, як це працює, наскільки це точно і що "
        "відбувається із завантаженими зображеннями."
    ),
    "page.faq.still_unsure_html": (
        'Досі не впевнені? Відкрийте issue на <a href="https://github.com/Micorlov/aipicdetect/issues" '
        'rel="noopener">GitHub</a>.'
    ),
    # Home page copy
    "home.entity_sentence": (
        "AiPicDetect — безкоштовний інструмент з відкритим кодом, який оцінює ймовірність того, що "
        "зображення створене штучним інтелектом, і видаляє приховані метадані — хмарна версія або "
        "self-hosted, вибір за вами."
    ),
    "home.lead": (
        "AiPicDetect запускає відкриту модель для розпізнавання зображень ШІ і зчитує кожне поле EXIF, "
        "C2PA та IPTC, яке несе фото, — а потім віддає вам чисту копію з усім цим видаленим. Без "
        "реєстрації, без чорної скриньки."
    ),
    "home.dropzone_note": (
        "JPEG, PNG, WebP, HEIC · до 50 MB · обробка в пам’яті, файл ніколи не записується на диск"
    ),
    "home.summary": (
        "AiPicDetect — безкоштовний інструмент з відкритим кодом, який оцінює ймовірність того, що "
        "зображення створене штучним інтелектом, і видаляє приховані метадані — хмарна версія або "
        "self-hosted, вибір за вами. Він оцінює ймовірність того, що зображення створене "
        "генератором ШІ, за допомогою відкритого класифікатора Hugging Face, а також може "
        "перебудувати зображення, щоб видалити метадані EXIF, XMP, IPTC, ICC і C2PA. Використовуйте "
        "хмарний екземпляр або розгорніть AiPicDetect у себе через Docker чи Python."
    ),
    "home.stat.0": "відкрита модель,<br>без стороннього API",
    "home.stat.1": "реєстрація<br>не потрібна",
    "home.stat.2": "MB — максимум<br>для завантаження",
    # Detect steps
    "steps.detect.upload.name": "Завантажте.",
    "steps.detect.upload.text": (
        "Перетягніть, вставте або виберіть зображення. Воно надсилається на сервер AiPicDetect, яким ви "
        "користуєтесь (на вашу ж машину в разі self-hosted), зберігається в пам’яті і ніколи не "
        "записується на диск."
    ),
    "steps.detect.detect.name": "Детекція.",
    "steps.detect.detect.text": (
        "Класифікатор зображень з відкритим кодом оцінює ймовірність того, що пікселі створені "
        "генератором."
    ),
    "steps.detect.decide.name": "Рішення.",
    "steps.detect.decide.text": (
        "Ви отримуєте ймовірність того, що зображення створене ШІ, діапазон впевненості та блоки "
        "метаданих, які несе файл, — як ймовірність, а не як вирок."
    ),
    # Scrub steps — <code> blocks contain literal shell commands and must stay untranslated
    "steps.scrub.inspect.name": "Перевірте.",
    "steps.scrub.inspect.text": (
        "Виконайте <code>aipicdetect inspect photo.jpg</code>, щоб отримати список блоків EXIF, XMP, "
        "IPTC, C2PA і ICC, які несе файл."
    ),
    "steps.scrub.scrub.name": "Очистіть.",
    "steps.scrub.scrub.text": (
        "Виконайте <code>aipicdetect scrub photo.jpg</code> (або <code>POST /scrub</code>). AiPicDetect "
        "декодує пікселі, застосовує орієнтацію EXIF і будує цілком нове зображення з "
        "необробленого буфера пікселів."
    ),
    "steps.scrub.verify.name": "Перевірте результат.",
    "steps.scrub.verify.text": (
        "Виконайте <code>aipicdetect inspect photo.clean.jpg</code>; має вивестися «no metadata signatures found»."
    ),
    # FAQ (home slugs)
    "faq.accuracy.question": "Наскільки точний детектор?",
    "faq.accuracy.answer_html": (
        "Він видає ймовірність, а не вирок. Оцінки близько 50% позначаються як "
        "<em>Невизначено</em>; ставтеся до будь-якого окремого результату як до одного із сигналів "
        "і поєднуйте його з іншими доказами. Докладніше на сторінці "
        '<a href="/how-accurate">про точність детекторів зображень ШІ</a>.'
    ),
    "faq.leaves_computer.question": "Чи покидає моє зображення мій комп’ютер?",
    "faq.leaves_computer.answer_html": (
        "На цьому публічному екземплярі — так: зображення завантажується на сервер AiPicDetect "
        "(контейнер Google Cloud Run, яким керує автор), оцінюється в пам’яті і ніколи не "
        "записується на диск. Очищена копія зберігається в пам’яті лише доти, доки її не "
        "витіснять 100 новіших результатів або контейнер не перезапуститься, і нічого не "
        'надсилається до стороннього API. Якщо ви хочете, щоб нічого не покидало вашу машину, '
        '<a href="/self-host">розгорніть AiPicDetect самостійно</a> однією командою Docker. Подробиці — '
        'на <a href="/privacy">сторінці приватності</a>.'
    ),
    "faq.open_source.question": "Це проєкт з відкритим кодом?",
    "faq.open_source.answer_html": (
        "Так. Код, образ Docker, CLI і GitHub Action — усе в "
        '<a href="https://github.com/Micorlov/aipicdetect" rel="noopener">репозиторії AiPicDetect</a> за '
        "ліцензією MIT. Детектор — це відкрита модель Hugging Face, яку можна вивчити або "
        "замінити."
    ),
    "faq.remove_metadata.question": "Чи можу я видалити C2PA та інші метадані?",
    "faq.remove_metadata.answer_html": (
        "Так. Після перевірки зображення скористайтеся кнопкою <em>Завантажити чисту копію</em>. "
        "AiPicDetect перебудовує зображення з його пікселів, тож EXIF, XMP, IPTC, C2PA і профіль ICC "
        'повністю відкидаються. <a href="/remove-image-metadata">Як працює очищення</a>.'
    ),
    "faq.formats.question": "Які формати підтримуються?",
    "faq.formats.answer_html": (
        "JPEG, PNG, WebP, HEIC/HEIF і більшість форматів, які вміє декодувати Pillow, розміром до "
        "50 MB."
    ),
    "faq.why_metadata.question": "Чому показуються метадані?",
    "faq.why_metadata.answer_html": (
        "Облікові дані вмісту C2PA і теги програм для редагування — це підказки щодо походження "
        "файлу. Панель показує, які блоки (EXIF, XMP, IPTC, C2PA, ICC) несе файл, щоб ви могли "
        'враховувати їх разом з оцінкою. Див. <a href="/c2pa">облікові дані вмісту C2PA</a> і '
        '<a href="/remove-image-metadata">як видалити метадані зображення</a>.'
    ),
    "faq.different_model.question": "Чи можу я використати іншу модель?",
    "faq.different_model.answer_html": (
        "Так. Задайте <code>PICAI_DETECTOR_MODEL</code> — будь-яку модель класифікації зображень "
        "з Hugging Face, чиї мітки розрізняють ШІ/підробку та людину/реальність."
    ),
    # FAQ (more slugs)
    "faq.free.question": "AiPicDetect безкоштовний?",
    "faq.free.answer_html": (
        "Так. AiPicDetect — проєкт з відкритим кодом за ліцензією MIT. Хмарний екземпляр безкоштовний у "
        "використанні з лімітом 10 перевірок на IP-адресу кожні 24 години; у self-hosted копії "
        "ліміту немає."
    ),
    "faq.screenshots.question": "Чи працює це зі скриншотами або сильно стиснутими зображеннями?",
    "faq.screenshots.answer_html": (
        "Працює, але перекодування, зміна розміру і створення скриншотів стирають частину "
        "пікселевих слідів, на які спирається класифікатор, тож варто очікувати нижчої "
        "впевненості і більшої кількості результатів <em>Невизначено</em>."
    ),
    "faq.which_generator.question": (
        "Чи може він визначити, який генератор створив зображення (Midjourney, DALL·E, Stable "
        "Diffusion)?"
    ),
    "faq.which_generator.answer_html": (
        "Ні. AiPicDetect загалом оцінює статистику пікселів «згенеровано проти реального»; він не "
        "визначає конкретний генератор і нічого не знає про генератори, випущені після збору "
        "навчальних даних його моделі."
    ),
    "faq.false_positive.question": "Чому справжнє фото отримало оцінку ШІ?",
    "faq.false_positive.answer_html": (
        "Сильні фільтри, HDR-обробка, збільшення масштабу, ілюстрації і 3D-рендери мають "
        "статистичні риси, схожі на згенеровані зображення. Оцінка — це ймовірність, а не доказ; "
        "хибні спрацювання трапляються."
    ),
    "faq.offline.question": "Чи можу я використовувати це офлайн?",
    "faq.offline.answer_html": (
        "Так. Після того як перший запуск завантажить модель у кеш Hugging Face, self-hosted "
        "AiPicDetect не потребує доступу до мережі."
    ),
    "faq.rate_limit.question": "Чи є ліміт запитів на хмарному екземплярі?",
    "faq.rate_limit.answer_html": (
        "Так: 10 перевірок на клієнтську IP-адресу в будь-якому ковзному 24-годинному вікні. "
        "Відповіді несуть заголовок <code>X-RateLimit-Remaining</code>, а запит понад ліміт "
        "повертає 429 із заголовком <code>Retry-After</code>."
    ),
    # Navigation
    "nav.detector": "Детектор",
    "nav.how_it_works": "Як це працює",
    "nav.how-to-tell-if-an-image-is-ai-generated": "Гід",
    "nav.api": "API",
    "nav.self-host": "Self-host",
    # Footer
    "footer.remove-image-metadata": "Видалення метаданих",
    "footer.c2pa": "C2PA",
    "footer.faq": "Питання і відповіді",
    "footer.privacy": "Приватність",
    "footer.self-host": "Self-host",
    "footer.about": "Про проєкт",
    # UI strings
    "ui.nav_aria_label": "Головна навігація",
    "ui.loading_status": "Завантаження детектора…",
    "ui.hero_overline": "— ШІ-криміналістика зображень з відкритим кодом",
    "ui.hero_heading_line1": "Це фото справжнє?",
    "ui.hero_heading_line2": "Отримайте оцінку і доказ.",
    "ui.tool_aria_label": "Детектор зображень ШІ",
    "ui.dropzone_aria_label": "Завантажте зображення для аналізу",
    "ui.dropzone_title_fine": "Перетягніть фото сюди",
    "ui.dropzone_title_coarse": "Перевірити фото",
    "ui.dropzone_sub_fine": "або вставте з буфера обміну, або",
    "ui.dropzone_sub_coarse": "з галереї або з камери",
    "ui.btn_check_image_fine": "Перевірити це зображення",
    "ui.btn_choose_photo_coarse": "Вибрати фото",
    "ui.btn_take_photo": "Зробити фото",
    "ui.dismiss_aria_label": "Закрити",
    "ui.analyzing_prefix": "Аналіз",
    "ui.analyzing_suffix": "· пікселі · блоки метаданих",
    "ui.verdict_overline": "— Вердикт",
    "ui.meter_real": "Реальне",
    "ui.meter_uncertain": "Невизначено",
    "ui.meter_ai": "ШІ",
    "ui.model_label": "Модель",
    "ui.verdict_disclaimer_html": (
        "Результати — це ймовірності від класифікатора, а не вироки. "
        '<a href="/how-accurate">Як читати оцінку.</a>'
    ),
    "ui.btn_check_another": "Перевірити інше зображення",
    "ui.preview_overline": "— Перегляд",
    "ui.preview_alt": "Перегляд завантаженого зображення",
    "ui.metadata_overline": "— Метадані",
    "ui.metadata_heading": "Знайдено у файлі.",
    "ui.jpeg_segments_label": "Сегменти JPEG",
    "ui.btn_download_clean": "Завантажити чисту копію",
    "ui.metadata_scrub_note_html": (
        "Зображення перебудоване з пікселів, тому всі блоки вище видалено. "
        '<a href="/remove-image-metadata">Як це працює</a>'
    ),
    "ui.how_it_works_overline": "— Як це працює",
    "ui.how_it_works_heading": "Три кроки. Нічого не зберігається.",
    "ui.how_it_works_links_html": (
        '<a href="/how-to-tell-if-an-image-is-ai-generated">Прочитайте гід про те, як розпізнати '
        'зображення ШІ</a> або <a href="/self-host">розгорніть AiPicDetect на своїй машині</a>.'
    ),
    "ui.faq_overline": "— Питання і відповіді",
    "ui.faq_heading": "Перш ніж запитати.",
    "ui.faq_more_link": "Більше запитань і відповідей →",
    "ui.footer_tagline": "AiPicDetect. · відкритий код",
    "ui.footer_detector_label": "Детектор:",
    "ui.breadcrumb_aria_label": "Хлібні крихти",
    "ui.last_updated_prefix": "Востаннє оновлено",
    "ui.source_on_github": "вихідний код на GitHub",
    "ui.btn_try_detector": "Спробувати детектор",
    "ui.status_ready": "Детектор готовий",
    "ui.status_unreachable": "Сервер недоступний",
    "ui.loading_model_note": "Завантаження моделі детектора (перший запуск завантажує ~750 MB)…",
    "ui.error_empty_file": "Цей файл порожній.",
    "ui.error_file_too_large": "{name} — {size}, ліміт становить 50 MB.",
    "ui.error_server_unreachable": "Не вдалося з’єднатися із сервером: {message}",
    "ui.verdict_ai": "Ймовірно, створено ШІ",
    "ui.verdict_real": "Ймовірно, справжнє фото",
    "ui.verdict_uncertain": "Невизначено",
    "ui.confidence_suffix": "впевненість",
    "ui.format_unknown": "невідомо",
    "ui.metadata_present": "Присутні",
    "ui.metadata_not_present": "Відсутні",
    "ui.no_jpeg_segments": "Немає сегментів JPEG APP",
    "ui.quota_remaining": "Залишилося {remaining} із {limit} перевірок на сьогодні",
}
