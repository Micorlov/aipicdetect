"""Russian translation table.

Falls back to English (see :func:`aipicdetect.content.locales.t`) for any key not defined here, but
every key from :mod:`aipicdetect.content.locales.en` is translated below.
"""

from __future__ import annotations

STRINGS: dict[str, str] = {
    # Page metadata
    "page.home.title": "AiPicDetect — детектор изображений ИИ и очиститель метаданных с открытым кодом",
    "page.home.description": (
        "Проверьте, сгенерировано ли изображение ИИ, с помощью AiPicDetect — бесплатного детектора с "
        "открытым исходным кодом. Используйте его в браузере или запустите на своей машине через "
        "Docker или Python."
    ),
    "page.home.h1": "Это фото настоящее? Получите оценку и доказательство.",
    "page.faq.title": "Вопросы о детекторе изображений ИИ: точность, приватность, форматы, модели",
    "page.faq.description": (
        "Ответы на частые вопросы о AiPicDetect: насколько точен детектор ИИ-изображений, где "
        "обрабатывается ваше изображение, какие форматы поддерживаются, как заменить модель и "
        "какие действуют лимиты запросов."
    ),
    "page.faq.h1": "Часто задаваемые вопросы о AiPicDetect",
    "page.faq.intro_suffix": (
        "Это самые частые вопросы о том, как это работает, насколько это точно и что происходит с "
        "загруженными изображениями."
    ),
    "page.faq.still_unsure_html": (
        'Остались вопросы? Откройте issue на <a href="https://github.com/Micorlov/aipicdetect/issues" '
        'rel="noopener">GitHub</a>.'
    ),
    # Home page copy
    "home.entity_sentence": (
        "AiPicDetect — бесплатный инструмент с открытым исходным кодом, который оценивает вероятность "
        "того, что изображение создано ИИ, и удаляет скрытые метаданные — облачная версия или "
        "self-hosted, выбор за вами."
    ),
    "home.lead": (
        "AiPicDetect запускает открытую модель для распознавания ИИ-изображений и считывает каждое поле "
        "EXIF, C2PA и IPTC, которое несёт фото, — а затем отдаёт вам чистую копию со всем этим "
        "удалённым. Без регистрации, без чёрного ящика."
    ),
    "home.dropzone_note": (
        "JPEG, PNG, WebP, HEIC · до 50 MB · обработка в памяти, файл никогда не записывается на диск"
    ),
    "home.summary": (
        "AiPicDetect — бесплатный инструмент с открытым исходным кодом, который оценивает вероятность "
        "того, что изображение создано ИИ, и удаляет скрытые метаданные — облачная версия или "
        "self-hosted, выбор за вами. Он оценивает вероятность того, что изображение создано "
        "ИИ-генератором, с помощью открытого классификатора Hugging Face, а также может "
        "перестроить изображение, чтобы удалить метаданные EXIF, XMP, IPTC, ICC и C2PA. "
        "Используйте облачный экземпляр или разверните AiPicDetect у себя через Docker или Python."
    ),
    "home.stat.0": "открытая модель,<br>без стороннего API",
    "home.stat.1": "регистрация<br>не нужна",
    "home.stat.2": "MB — максимум<br>для загрузки",
    # Detect steps
    "steps.detect.upload.name": "Загрузите.",
    "steps.detect.upload.text": (
        "Перетащите, вставьте или выберите изображение. Оно отправляется на сервер AiPicDetect, который "
        "вы используете (на вашу же машину при self-hosted-варианте), хранится в памяти и никогда "
        "не записывается на диск."
    ),
    "steps.detect.detect.name": "Детекция.",
    "steps.detect.detect.text": (
        "Классификатор изображений с открытым кодом оценивает вероятность того, что пиксели были "
        "созданы генератором."
    ),
    "steps.detect.decide.name": "Решение.",
    "steps.detect.decide.text": (
        "Вы получаете вероятность того, что изображение создано ИИ, диапазон уверенности и блоки "
        "метаданных, которые несёт файл, — как вероятность, а не как вердикт."
    ),
    # Scrub steps — <code> blocks contain literal shell commands and must stay untranslated
    "steps.scrub.inspect.name": "Проверьте.",
    "steps.scrub.inspect.text": (
        "Выполните <code>aipicdetect inspect photo.jpg</code>, чтобы получить список блоков EXIF, XMP, "
        "IPTC, C2PA и ICC, которые несёт файл."
    ),
    "steps.scrub.scrub.name": "Очистите.",
    "steps.scrub.scrub.text": (
        "Выполните <code>aipicdetect scrub photo.jpg</code> (или <code>POST /scrub</code>). AiPicDetect "
        "декодирует пиксели, применяет ориентацию EXIF и строит совершенно новое изображение из "
        "необработанного буфера пикселей."
    ),
    "steps.scrub.verify.name": "Проверьте результат.",
    "steps.scrub.verify.text": (
        "Выполните <code>aipicdetect inspect photo.clean.jpg</code>; должно вывестись «no metadata "
        "signatures found»."
    ),
    # FAQ (home slugs)
    "faq.accuracy.question": "Насколько точен детектор?",
    "faq.accuracy.answer_html": (
        "Он выдаёт вероятность, а не вердикт. Оценки около 50% помечаются как <em>Неопределённо</em>; "
        "относитесь к любому отдельному результату как к одному из сигналов и сочетайте его с "
        "другими доказательствами. Подробнее — на странице "
        '<a href="/how-accurate">о точности детекторов ИИ-изображений</a>.'
    ),
    "faq.leaves_computer.question": "Покидает ли моё изображение мой компьютер?",
    "faq.leaves_computer.answer_html": (
        "На этом публичном экземпляре — да: изображение загружается на сервер AiPicDetect (контейнер "
        "Google Cloud Run, которым управляет автор), оценивается в памяти и никогда не "
        "записывается на диск. Очищенная копия хранится в памяти только до тех пор, пока её не "
        "вытеснят 100 более новых результатов или контейнер не перезапустится, и ничего не "
        'отправляется стороннему API. Если вы хотите, чтобы ничего не покидало вашу машину, '
        '<a href="/self-host">разверните AiPicDetect самостоятельно</a> одной командой Docker. '
        'Подробности — на <a href="/privacy">странице приватности</a>.'
    ),
    "faq.open_source.question": "Это проект с открытым исходным кодом?",
    "faq.open_source.answer_html": (
        "Да. Код, образ Docker, CLI и GitHub Action — всё в "
        '<a href="https://github.com/Micorlov/aipicdetect" rel="noopener">репозитории AiPicDetect</a> под '
        "лицензией MIT. Детектор — это открытая модель Hugging Face, которую можно изучить или "
        "заменить."
    ),
    "faq.remove_metadata.question": "Могу ли я удалить C2PA и другие метаданные?",
    "faq.remove_metadata.answer_html": (
        "Да. После проверки изображения используйте <em>Скачать чистую копию</em>. AiPicDetect "
        "перестраивает изображение из его пикселей, поэтому EXIF, XMP, IPTC, C2PA и профиль ICC "
        'полностью отбрасываются. <a href="/remove-image-metadata">Как работает очистка</a>.'
    ),
    "faq.formats.question": "Какие форматы поддерживаются?",
    "faq.formats.answer_html": (
        "JPEG, PNG, WebP, HEIC/HEIF и большинство форматов, которые умеет декодировать Pillow, "
        "размером до 50 MB."
    ),
    "faq.why_metadata.question": "Почему показываются метаданные?",
    "faq.why_metadata.answer_html": (
        "Учётные данные содержимого C2PA и теги редактирующего ПО — это подсказки о происхождении "
        "файла. Панель показывает, какие блоки (EXIF, XMP, IPTC, C2PA, ICC) несёт файл, чтобы вы "
        'могли учитывать их вместе с оценкой. См. <a href="/c2pa">учётные данные содержимого '
        'C2PA</a> и <a href="/remove-image-metadata">как удалить метаданные изображения</a>.'
    ),
    "faq.different_model.question": "Могу ли я использовать другую модель?",
    "faq.different_model.answer_html": (
        "Да. Задайте <code>PICAI_DETECTOR_MODEL</code> — любую модель классификации изображений с "
        "Hugging Face, чьи метки различают ИИ/подделку и человека/реальность."
    ),
    # FAQ (more slugs)
    "faq.free.question": "AiPicDetect бесплатен?",
    "faq.free.answer_html": (
        "Да. AiPicDetect — проект с открытым исходным кодом под лицензией MIT. Облачный экземпляр "
        "бесплатен в использовании с лимитом 10 проверок на IP-адрес каждые 24 часа; у "
        "self-hosted-копии лимита нет."
    ),
    "faq.screenshots.question": "Работает ли он со скриншотами или сильно сжатыми изображениями?",
    "faq.screenshots.answer_html": (
        "Работает, но перекодирование, изменение размера и создание скриншотов стирают часть "
        "пиксельных следов, на которые опирается классификатор, поэтому стоит ожидать более "
        "низкой уверенности и большего числа результатов <em>Неопределённо</em>."
    ),
    "faq.which_generator.question": (
        "Может ли он определить, какой генератор создал изображение (Midjourney, DALL·E, Stable "
        "Diffusion)?"
    ),
    "faq.which_generator.answer_html": (
        "Нет. AiPicDetect в целом оценивает статистику пикселей «сгенерировано против реального»; он не "
        "определяет конкретный генератор и ничего не знает о генераторах, выпущенных после сбора "
        "обучающих данных его модели."
    ),
    "faq.false_positive.question": "Почему реальное фото получило оценку ИИ?",
    "faq.false_positive.answer_html": (
        "Сильные фильтры, HDR-обработка, увеличение масштаба, иллюстрации и 3D-рендеры имеют "
        "статистические черты, схожие со сгенерированными изображениями. Оценка — это "
        "вероятность, а не доказательство; ложные срабатывания случаются."
    ),
    "faq.offline.question": "Могу ли я использовать его офлайн?",
    "faq.offline.answer_html": (
        "Да. После того как первый запуск загрузит модель в кэш Hugging Face, self-hosted AiPicDetect не "
        "нуждается в доступе к сети."
    ),
    "faq.rate_limit.question": "Есть ли лимит запросов на облачном экземпляре?",
    "faq.rate_limit.answer_html": (
        "Да: 10 проверок на клиентский IP-адрес в любом скользящем 24-часовом окне. Ответы несут "
        "заголовок <code>X-RateLimit-Remaining</code>, а запрос сверх лимита возвращает 429 с "
        "заголовком <code>Retry-After</code>."
    ),
    # Navigation
    "nav.detector": "Детектор",
    "nav.how_it_works": "Как это работает",
    "nav.how-to-tell-if-an-image-is-ai-generated": "Гайд",
    "nav.api": "API",
    "nav.self-host": "Self-host",
    # Footer
    "footer.remove-image-metadata": "Удаление метаданных",
    "footer.c2pa": "C2PA",
    "footer.faq": "Вопросы и ответы",
    "footer.privacy": "Приватность",
    "footer.self-host": "Self-host",
    "footer.about": "О проекте",
    # UI strings
    "ui.nav_aria_label": "Главная навигация",
    "ui.loading_status": "Загрузка детектора…",
    "ui.hero_overline": "— ИИ-криминалистика изображений с открытым кодом",
    "ui.hero_heading_line1": "Это фото настоящее?",
    "ui.hero_heading_line2": "Получите оценку и доказательство.",
    "ui.tool_aria_label": "Детектор ИИ-изображений",
    "ui.dropzone_aria_label": "Загрузите изображение для анализа",
    "ui.dropzone_title_fine": "Перетащите фото сюда",
    "ui.dropzone_title_coarse": "Проверить фото",
    "ui.dropzone_sub_fine": "или вставьте из буфера обмена, или",
    "ui.dropzone_sub_coarse": "из галереи или с камеры",
    "ui.btn_check_image_fine": "Проверить это изображение",
    "ui.btn_choose_photo_coarse": "Выбрать фото",
    "ui.btn_take_photo": "Сделать фото",
    "ui.dismiss_aria_label": "Закрыть",
    "ui.analyzing_prefix": "Анализ",
    "ui.analyzing_suffix": "· пиксели · блоки метаданных",
    "ui.verdict_overline": "— Вердикт",
    "ui.meter_real": "Реальное",
    "ui.meter_uncertain": "Неопределённо",
    "ui.meter_ai": "ИИ",
    "ui.model_label": "Модель",
    "ui.verdict_disclaimer_html": (
        "Результаты — это вероятности от классификатора, а не вердикты. "
        '<a href="/how-accurate">Как читать оценку.</a>'
    ),
    "ui.btn_check_another": "Проверить другое изображение",
    "ui.preview_overline": "— Превью",
    "ui.preview_alt": "Превью загруженного изображения",
    "ui.metadata_overline": "— Метаданные",
    "ui.metadata_heading": "Найдено в файле.",
    "ui.jpeg_segments_label": "Сегменты JPEG",
    "ui.btn_download_clean": "Скачать чистую копию",
    "ui.metadata_scrub_note_html": (
        "Изображение перестроено из пикселей, поэтому все блоки выше удалены. "
        '<a href="/remove-image-metadata">Как это работает</a>'
    ),
    "ui.how_it_works_overline": "— Как это работает",
    "ui.how_it_works_heading": "Три шага. Ничего не сохраняется.",
    "ui.how_it_works_links_html": (
        '<a href="/how-to-tell-if-an-image-is-ai-generated">Прочитайте гайд о том, как распознать '
        'ИИ-изображения</a> или <a href="/self-host">разверните AiPicDetect на своей машине</a>.'
    ),
    "ui.faq_overline": "— Вопросы и ответы",
    "ui.faq_heading": "Прежде чем спросить.",
    "ui.faq_more_link": "Больше вопросов и ответов →",
    "ui.footer_tagline": "AiPicDetect. · открытый код",
    "ui.footer_detector_label": "Детектор:",
    "ui.breadcrumb_aria_label": "Хлебные крошки",
    "ui.last_updated_prefix": "Обновлено",
    "ui.source_on_github": "исходный код на GitHub",
    "ui.btn_try_detector": "Попробовать детектор",
    "ui.status_ready": "Детектор готов",
    "ui.status_unreachable": "Сервер недоступен",
    "ui.loading_model_note": "Загрузка модели детектора (первый запуск скачивает ~750 MB)…",
    "ui.error_empty_file": "Этот файл пуст.",
    "ui.error_file_too_large": "{name} — {size}, лимит составляет 50 MB.",
    "ui.error_server_unreachable": "Не удалось связаться с сервером: {message}",
    "ui.verdict_ai": "Вероятно, создано ИИ",
    "ui.verdict_real": "Вероятно, настоящее фото",
    "ui.verdict_uncertain": "Неопределённо",
    "ui.confidence_suffix": "уверенность",
    "ui.format_unknown": "неизвестно",
    "ui.metadata_present": "Присутствует",
    "ui.metadata_not_present": "Отсутствует",
    "ui.no_jpeg_segments": "Нет сегментов JPEG APP",
    "ui.quota_remaining": "Осталось {remaining} из {limit} проверок на сегодня",
}
