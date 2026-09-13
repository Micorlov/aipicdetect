"""Spanish translation table. Falls back to English (see aipicdetect.content.locales) for any key
missing here, so this file only needs to define what has actually been translated.
"""

from __future__ import annotations

STRINGS: dict[str, str] = {
    "page.home.title": "AiPicDetect — Detector de imágenes de IA y eliminador de metadatos de código abierto",
    "page.home.description": (
        "Comprueba si una imagen fue generada por IA con AiPicDetect, un detector gratuito y de código "
        "abierto. Úsalo en el navegador o ejecútalo en tu propio equipo con Docker o Python."
    ),
    "page.home.h1": "¿Es real esta foto? Obtén la puntuación y la prueba.",
    "page.faq.title": "Preguntas frecuentes sobre el detector de imágenes de IA: precisión, privacidad, formatos, modelos",
    "page.faq.description": (
        "Respuestas a preguntas habituales sobre AiPicDetect: qué tan precisa es la detección de imágenes "
        "de IA, dónde se procesa tu imagen, formatos admitidos, cambio de modelo y límites de uso."
    ),
    "page.faq.h1": "Preguntas frecuentes de AiPicDetect",
    "page.faq.intro_suffix": (
        "Estas son las preguntas que la gente hace con más frecuencia sobre cómo funciona, qué tan "
        "preciso es y qué ocurre con las imágenes que suben."
    ),
    "page.faq.still_unsure_html": (
        '¿Aún tienes dudas? Abre un issue en <a href="https://github.com/Micorlov/aipicdetect/issues" '
        'rel="noopener">GitHub</a>.'
    ),
    # ── Guide page meta ─────────────────────────────────────────────────────────────────────
    "page.how-to-tell-if-an-image-is-ai-generated.title": 'Cómo saber si una imagen fue generada por IA (Guía 2026)',
    "page.how-to-tell-if-an-image-is-ai-generated.description": (
        'Lista de verificación para detectar imágenes generadas por IA: señales visuales, metadatos C2PA y EXIF, búsqueda inversa de imágenes y cómo leer la puntuación del detector.'
    ),
    "page.how-to-tell-if-an-image-is-ai-generated.h1": 'Cómo saber si una imagen fue generada por IA',
    "page.how-accurate.title": '¿Cuán precisos son los detectores de IA? Cómo leer una puntuación de AiPicDetect',
    "page.how-accurate.description": (
        'Los detectores de imágenes de IA dan probabilidades, no veredictos. Cómo AiPicDetect convierte las puntuaciones del clasificador en un porcentaje y banda de confianza.'
    ),
    "page.how-accurate.h1": '¿Qué tan preciso es un detector de imágenes de IA?',
    "page.remove-image-metadata.title": 'Eliminar metadatos EXIF, XMP, IPTC y C2PA de imágenes',
    "page.remove-image-metadata.description": (
        'Elimina EXIF, XMP, IPTC, ICC y credenciales de contenido C2PA de archivos JPEG, PNG, WebP y HEIC volviendo a renderizar los píxeles con la CLI gratuita de AiPicDetect.'
    ),
    "page.remove-image-metadata.h1": 'Eliminar todos los metadatos de una imagen',
    "page.privacy.title": 'Privacidad: qué ocurre con las imágenes que subes a AiPicDetect',
    "page.privacy.description": (
        'AiPicDetect procesa las subidas en memoria, nunca las escribe en disco, conserva las copias limpias solo brevemente y no envía ninguna imagen a servicios de terceros.'
    ),
    "page.privacy.h1": 'Qué ocurre con una imagen que subes',
    "home.entity_sentence": (
        "AiPicDetect es una herramienta gratuita y de código abierto que puntúa imágenes generadas por IA "
        "y elimina los metadatos ocultos — alojada o autoalojada, tú eliges."
    ),
    "home.lead": (
        "AiPicDetect ejecuta un modelo abierto de detección de IA y lee todos los campos EXIF, C2PA e IPTC "
        "que lleva una foto — y luego te entrega una copia limpia con todo eso eliminado. Sin "
        "registro, sin caja negra."
    ),
    "home.dropzone_note": "JPEG, PNG, WebP, HEIC · hasta 50 MB · procesado en memoria, nunca se escribe en disco",
    "home.summary": (
        "AiPicDetect es una herramienta gratuita y de código abierto que puntúa imágenes generadas por IA "
        "y elimina los metadatos ocultos — alojada o autoalojada, tú eliges. Calcula la probabilidad "
        "de que una imagen haya sido producida por un generador de IA usando un clasificador abierto "
        "de Hugging Face, y puede volver a renderizar imágenes para eliminar los metadatos EXIF, XMP, "
        "IPTC, ICC y C2PA. Usa la instancia alojada o autoalójalo con Docker o Python."
    ),
    "home.stat.0": "modelo abierto,<br>sin API de terceros",
    "home.stat.1": "registros<br>necesarios",
    "home.stat.2": "MB máx.<br>de subida",
    "steps.detect.upload.name": "Subir.",
    "steps.detect.detect.name": "Detectar.",
    "steps.detect.decide.name": "Decidir.",
    "steps.detect.upload.text": (
        "Arrastra, pega o elige una imagen. Se envía al servidor de AiPicDetect que estés usando (tu "
        "propio equipo si lo autoalojas), se mantiene en memoria y nunca se escribe en disco."
    ),
    "steps.detect.detect.text": (
        "Un clasificador de imágenes de código abierto calcula la probabilidad de que los píxeles "
        "hayan sido producidos por un generador."
    ),
    "steps.detect.decide.text": (
        "Obtienes una probabilidad de IA, una banda de confianza y los bloques de metadatos que "
        "lleva el archivo — como una probabilidad, no un veredicto."
    ),
    # steps.scrub.*.text carries inline <code>...</code> shell commands — preserved verbatim below,
    # only the surrounding prose is translated.
    "steps.scrub.inspect.name": "Inspeccionar.",
    "steps.scrub.scrub.name": "Limpiar.",
    "steps.scrub.verify.name": "Verificar.",
    "steps.scrub.inspect.text": (
        "Ejecuta <code>aipicdetect inspect photo.jpg</code> para listar los bloques EXIF, XMP, IPTC, C2PA "
        "e ICC que lleva el archivo."
    ),
    "steps.scrub.scrub.text": (
        "Ejecuta <code>aipicdetect scrub photo.jpg</code> (o <code>POST /scrub</code>). AiPicDetect decodifica "
        "los píxeles, aplica la orientación EXIF y construye una imagen completamente nueva a partir "
        "del búfer de píxeles en bruto."
    ),
    "steps.scrub.verify.text": (
        "Ejecuta <code>aipicdetect inspect photo.clean.jpg</code>; debería mostrar «no metadata signatures found»."
    ),
    "faq.accuracy.question": "¿Qué tan preciso es el detector?",
    "faq.leaves_computer.question": "¿Mi imagen sale de mi ordenador?",
    "faq.open_source.question": "¿Es de código abierto?",
    "faq.remove_metadata.question": "¿Puedo eliminar C2PA y otros metadatos?",
    "faq.formats.question": "¿Qué formatos son compatibles?",
    "faq.why_metadata.question": "¿Por qué se muestran los metadatos?",
    "faq.different_model.question": "¿Puedo usar un modelo distinto?",
    "faq.free.question": "¿AiPicDetect es gratis?",
    "faq.screenshots.question": "¿Funciona con capturas de pantalla o imágenes muy comprimidas?",
    "faq.which_generator.question": (
        "¿Puede indicar qué generador creó una imagen (Midjourney, DALL·E, Stable Diffusion)?"
    ),
    "faq.false_positive.question": "¿Por qué una foto real obtuvo una puntuación de IA?",
    "faq.offline.question": "¿Puedo usarlo sin conexión?",
    "faq.rate_limit.question": "¿Hay un límite de uso en la instancia alojada?",
    "faq.accuracy.answer_html": (
        "Ofrece una probabilidad, no un veredicto. Las puntuaciones cercanas al 50 % se etiquetan "
        "como <em>Incierto</em>; trata cualquier resultado individual como una señal y combínalo con "
        'otras pruebas. Más información sobre <a href="/how-accurate">qué tan precisos son los '
        "detectores de imágenes de IA</a>."
    ),
    "faq.leaves_computer.answer_html": (
        "En esta instancia pública, sí: la imagen se sube al servidor de AiPicDetect (un contenedor de "
        "Google Cloud Run gestionado por el autor), se puntúa en memoria y nunca se escribe en "
        "disco. La copia limpia se mantiene en memoria solo hasta que 100 resultados más recientes "
        "la reemplazan o el contenedor se reinicia, y nada se envía a una API de terceros. Si no "
        'quieres que nada salga de tu equipo, <a href="/self-host">ejecuta AiPicDetect tú mismo</a> con un '
        'solo comando de Docker. Los detalles están en la <a href="/privacy">página de privacidad</a>.'
    ),
    "faq.open_source.answer_html": (
        "Sí. El código, la imagen de Docker, la CLI y la GitHub Action están todos en el "
        '<a href="https://github.com/Micorlov/aipicdetect" rel="noopener">repositorio de AiPicDetect</a> bajo la '
        "licencia MIT. El detector es un modelo abierto de Hugging Face que puedes inspeccionar o "
        "sustituir."
    ),
    "faq.remove_metadata.answer_html": (
        "Sí. Después de comprobar una imagen, usa <em>Descargar copia limpia</em>. AiPicDetect reconstruye "
        "la imagen a partir de sus píxeles, de modo que EXIF, XMP, IPTC, C2PA y el perfil ICC quedan "
        'todos eliminados. <a href="/remove-image-metadata">Cómo funciona el limpiador</a>.'
    ),
    "faq.formats.answer_html": (
        "JPEG, PNG, WebP, HEIC/HEIF y la mayoría de los formatos que Pillow puede decodificar, hasta 50 MB."
    ),
    "faq.why_metadata.answer_html": (
        "Las credenciales de contenido C2PA y las etiquetas del software de edición son indicios de "
        "procedencia. El panel muestra qué bloques (EXIF, XMP, IPTC, C2PA, ICC) lleva el archivo "
        'para que puedas valorarlos junto con la puntuación. Consulta <a href="/c2pa">las '
        'credenciales de contenido C2PA</a> y <a href="/remove-image-metadata">cómo eliminar los '
        "metadatos de una imagen</a>."
    ),
    "faq.different_model.answer_html": (
        "Sí. Configura <code>PICAI_DETECTOR_MODEL</code> con cualquier modelo de clasificación de "
        "imágenes de Hugging Face cuyas etiquetas distingan contenido IA/falso frente a humano/real."
    ),
    "faq.free.answer_html": (
        "Sí. AiPicDetect es de código abierto bajo la licencia MIT. La instancia alojada es gratuita, con "
        "un límite de 10 análisis por dirección IP cada 24 horas; una copia autoalojada no tiene límite."
    ),
    "faq.screenshots.answer_html": (
        "Funciona, pero volver a codificar, redimensionar y las capturas de pantalla eliminan parte "
        "de los indicios a nivel de píxel en los que se basa el clasificador, así que espera menor "
        "confianza y más resultados <em>Incierto</em>."
    ),
    "faq.which_generator.answer_html": (
        "No. AiPicDetect puntúa, en general, las estadísticas de píxeles generados frente a reales; no "
        "identifica el generador y no tiene conocimiento de los generadores publicados después de "
        "que se recopilaran los datos de entrenamiento de su modelo."
    ),
    "faq.false_positive.answer_html": (
        "Los filtros intensos, el procesado HDR, el escalado, las ilustraciones y los renders 3D "
        "comparten características estadísticas con las imágenes generadas. La puntuación es una "
        "probabilidad, no una prueba; los falsos positivos ocurren."
    ),
    "faq.offline.answer_html": (
        "Sí. Después de que la primera ejecución descargue el modelo en la caché de Hugging Face, un "
        "AiPicDetect autoalojado no necesita acceso a la red."
    ),
    "faq.rate_limit.answer_html": (
        "Sí: 10 análisis por IP de cliente en cualquier ventana móvil de 24 horas. Las respuestas "
        "incluyen <code>X-RateLimit-Remaining</code>, y una solicitud que supere el límite devuelve "
        "429 con una cabecera <code>Retry-After</code>."
    ),
    "nav.detector": "Detector",
    "nav.how_it_works": "Cómo funciona",
    "nav.how-to-tell-if-an-image-is-ai-generated": "Guía",
    "nav.api": "API",
    "nav.self-host": "Autoalojar",
    "footer.remove-image-metadata": "Eliminar metadatos",
    "footer.c2pa": "C2PA",
    "footer.faq": "Preguntas frecuentes",
    "footer.privacy": "Privacidad",
    "footer.self-host": "Autoalojar",
    "footer.about": "Acerca de",
    "ui.nav_aria_label": "Navegación principal",
    "ui.loading_status": "Cargando detector…",
    "ui.hero_overline": "— Análisis forense de imágenes de IA de código abierto",
    "ui.hero_heading_line1": "¿Es real esta foto?",
    "ui.hero_heading_line2": "Obtén la puntuación y la prueba.",
    "ui.tool_aria_label": "Detector de imágenes de IA",
    "ui.dropzone_aria_label": "Sube una imagen para analizarla",
    "ui.dropzone_title_fine": "Arrastra y suelta una foto",
    "ui.dropzone_title_coarse": "Comprueba una foto",
    "ui.dropzone_sub_fine": "o pégala desde el portapapeles, o",
    "ui.dropzone_sub_coarse": "desde tu galería o la cámara",
    "ui.btn_check_image_fine": "Comprobar esta imagen",
    "ui.btn_choose_photo_coarse": "Elegir foto",
    "ui.btn_take_photo": "Hacer una foto",
    "ui.dismiss_aria_label": "Cerrar",
    "ui.analyzing_prefix": "Analizando",
    "ui.analyzing_suffix": "· píxeles · bloques de metadatos",
    "ui.verdict_overline": "— Veredicto",
    "ui.meter_real": "Real",
    "ui.meter_uncertain": "Incierto",
    "ui.meter_ai": "IA",
    "ui.model_label": "Modelo",
    "ui.verdict_disclaimer_html": (
        "Los resultados son probabilidades de un clasificador, no veredictos. "
        '<a href="/how-accurate">Cómo interpretar la puntuación.</a>'
    ),
    "ui.btn_check_another": "Comprobar otra imagen",
    "ui.preview_overline": "— Vista previa",
    "ui.preview_alt": "Vista previa de la imagen subida",
    "ui.metadata_overline": "— Metadatos",
    "ui.metadata_heading": "Encontrado en el archivo.",
    "ui.jpeg_segments_label": "Segmentos JPEG",
    "ui.btn_download_clean": "Descargar la copia limpia",
    "ui.metadata_scrub_note_html": (
        "Vuelto a renderizar desde los píxeles, así que todo bloque anterior ha desaparecido. "
        '<a href="/remove-image-metadata">Cómo funciona</a>'
    ),
    "ui.how_it_works_overline": "— Cómo funciona",
    "ui.how_it_works_heading": "Tres pasos. Nada se guarda.",
    "ui.how_it_works_links_html": (
        '<a href="/how-to-tell-if-an-image-is-ai-generated">Lee la guía para detectar imágenes de '
        'IA</a> o <a href="/self-host">ejecútalo en tu propio equipo</a>.'
    ),
    "ui.faq_overline": "— Preguntas frecuentes",
    "ui.faq_heading": "Antes de preguntar.",
    "ui.faq_more_link": "Más preguntas y respuestas →",
    "ui.footer_tagline": "AiPicDetect. · código abierto",
    "ui.footer_detector_label": "Detector:",
    "ui.breadcrumb_aria_label": "Ruta de navegación",
    "ui.last_updated_prefix": "Última actualización",
    "ui.source_on_github": "código fuente en GitHub",
    "ui.btn_try_detector": "Probar el detector",
    "ui.status_ready": "Detector listo",
    "ui.status_unreachable": "Servidor inaccesible",
    "ui.loading_model_note": "Cargando el modelo del detector (la primera vez descarga ~750 MB)…",
    "ui.error_empty_file": "Ese archivo está vacío.",
    "ui.error_file_too_large": "{name} pesa {size} — el límite es 50 MB.",
    "ui.error_server_unreachable": "No se pudo conectar con el servidor: {message}",
    "ui.verdict_ai": "Probablemente generada por IA",
    "ui.verdict_real": "Probablemente una foto real",
    "ui.verdict_uncertain": "Incierto",
    "ui.confidence_suffix": "de confianza",
    "ui.format_unknown": "desconocido",
    "ui.metadata_present": "Presente",
    "ui.metadata_not_present": "No presente",
    "ui.no_jpeg_segments": "Sin segmentos APP de JPEG",
    "ui.quota_remaining": "{remaining} de {limit} análisis restantes hoy",
}
