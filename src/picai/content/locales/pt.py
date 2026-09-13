"""Portuguese translation table."""

from __future__ import annotations

STRINGS: dict[str, str] = {
    "page.home.title": "picai — Detetor de Imagens IA e Limpador de Metadados Open Source",
    "page.home.description": (
        "Verifique se uma imagem foi gerada por IA com o picai, um detetor gratuito e open source. "
        "Use-o no navegador ou execute-o na sua própria máquina com Docker ou Python."
    ),
    "page.home.h1": "Esta fotografia é real? Obtenha a pontuação e a prova.",
    "page.faq.title": "FAQ do Detetor de Imagens IA: Precisão, Privacidade, Formatos, Modelos",
    "page.faq.description": (
        "Respostas a perguntas comuns sobre o picai: quão precisa é a deteção de imagens IA, onde a "
        "sua imagem é processada, formatos suportados, troca de modelo e limites de taxa."
    ),
    "page.faq.h1": "Perguntas frequentes sobre o picai",
    "page.faq.intro_suffix": (
        "Estas são as perguntas mais frequentes sobre como funciona, quão preciso é e o que acontece "
        "com as imagens enviadas."
    ),
    "page.faq.still_unsure_html": (
        'Ainda com dúvidas? Abra uma issue no <a href="https://github.com/Micorlov/picai/issues" '
        'rel="noopener">GitHub</a>.'
    ),
    "home.entity_sentence": (
        "O picai é uma ferramenta gratuita e open source que avalia imagens geradas por IA e remove "
        "metadados ocultos — alojado ou autoalojado, a escolha é sua."
    ),
    "home.lead": (
        "O picai executa um modelo aberto de deteção de IA e lê todos os campos EXIF, C2PA e IPTC "
        "que uma fotografia contém — depois entrega-lhe uma cópia limpa, com tudo isso removido. Sem "
        "registo, sem caixa preta."
    ),
    "home.dropzone_note": "JPEG, PNG, WebP, HEIC · até 50 MB · processado em memória, nunca escrito em disco",
    "home.summary": (
        "O picai é uma ferramenta gratuita e open source que avalia imagens geradas por IA e remove "
        "metadados ocultos — alojado ou autoalojado, a escolha é sua. Avalia a probabilidade de uma "
        "imagem ter sido produzida por um gerador de IA usando um classificador aberto do Hugging "
        "Face, e pode reconstruir imagens para remover metadados EXIF, XMP, IPTC, ICC e C2PA. Use a "
        "instância alojada ou autoaloje-se com Docker ou Python."
    ),
    "home.stat.0": "modelo aberto,<br>sem API de terceiros",
    "home.stat.1": "registos<br>necessários",
    "home.stat.2": "MB máx.<br>por envio",
    "steps.detect.upload.name": "Enviar.",
    "steps.detect.detect.name": "Detetar.",
    "steps.detect.decide.name": "Decidir.",
    "steps.detect.upload.text": (
        "Arraste, cole ou escolha uma imagem. É enviada para o servidor picai que está a usar (a "
        "sua própria máquina, em caso de autoalojamento), mantida em memória e nunca escrita em "
        "disco."
    ),
    "steps.detect.detect.text": (
        "Um classificador de imagens open source avalia a probabilidade de os pixels terem sido "
        "produzidos por um gerador."
    ),
    "steps.detect.decide.text": (
        "Obtém uma probabilidade de IA, uma faixa de confiança e os blocos de metadados que o "
        "ficheiro contém — como uma probabilidade, não um veredito."
    ),
    "steps.scrub.inspect.name": "Inspecionar.",
    "steps.scrub.scrub.name": "Limpar.",
    "steps.scrub.verify.name": "Verificar.",
    "steps.scrub.inspect.text": (
        "Execute <code>picai inspect photo.jpg</code> para listar os blocos EXIF, XMP, IPTC, C2PA e "
        "ICC que o ficheiro contém."
    ),
    "steps.scrub.scrub.text": (
        "Execute <code>picai scrub photo.jpg</code> (ou <code>POST /scrub</code>). O picai "
        "descodifica os pixels, aplica a orientação EXIF e constrói uma imagem totalmente nova a "
        "partir do buffer de pixels em bruto."
    ),
    "steps.scrub.verify.text": (
        "Execute <code>picai inspect photo.clean.jpg</code>; deverá imprimir «no metadata signatures found»."
    ),
    "faq.accuracy.question": "Qual é a precisão do detetor?",
    "faq.leaves_computer.question": "A minha imagem sai do meu computador?",
    "faq.open_source.question": "É open source?",
    "faq.remove_metadata.question": "Posso remover o C2PA e outros metadados?",
    "faq.formats.question": "Que formatos são suportados?",
    "faq.why_metadata.question": "Porque são listados os metadados?",
    "faq.different_model.question": "Posso usar um modelo diferente?",
    "faq.free.question": "O picai é gratuito?",
    "faq.screenshots.question": "Funciona com capturas de ecrã ou imagens muito comprimidas?",
    "faq.which_generator.question": (
        "Consegue identificar qual o gerador que criou uma imagem (Midjourney, DALL·E, Stable "
        "Diffusion)?"
    ),
    "faq.false_positive.question": "Porque é que uma fotografia real teve pontuação de IA?",
    "faq.offline.question": "Posso usá-lo offline?",
    "faq.rate_limit.question": "Existe um limite de taxa na instância alojada?",
    "faq.accuracy.answer_html": (
        "Reporta uma probabilidade, não um veredito. Pontuações próximas de 50% são identificadas "
        "como <em>Incerto</em>; trate qualquer resultado isolado como um indício e combine-o com "
        'outras evidências. Saiba mais sobre <a href="/how-accurate">a precisão dos detetores de '
        "imagens IA</a>."
    ),
    "faq.leaves_computer.answer_html": (
        "Nesta instância pública, sim: a imagem é enviada para o servidor picai (um contentor Google "
        "Cloud Run gerido pelo autor), avaliada em memória e nunca escrita em disco. A cópia limpa "
        "é mantida em memória apenas até 100 resultados mais recentes a substituírem ou o contentor "
        "reiniciar, e nada é enviado para uma API de terceiros. Se quiser que nada saia da sua "
        'máquina, <a href="/self-host">execute o picai você mesmo</a> com um único comando Docker. '
        'Os detalhes estão na <a href="/privacy">página de privacidade</a>.'
    ),
    "faq.open_source.answer_html": (
        "Sim. O código, a imagem Docker, o CLI e a GitHub Action estão todos no "
        '<a href="https://github.com/Micorlov/picai" rel="noopener">repositório picai</a> sob a '
        "licença MIT. O detetor é um modelo aberto do Hugging Face que pode inspecionar ou "
        "substituir."
    ),
    "faq.remove_metadata.answer_html": (
        "Sim. Depois de verificar uma imagem, use <em>Transferir cópia limpa</em>. O picai "
        "reconstrói a imagem a partir dos seus pixels, pelo que o EXIF, o XMP, o IPTC, o C2PA e o "
        'perfil ICC ficam todos para trás. <a href="/remove-image-metadata">Como funciona o '
        "limpador</a>."
    ),
    "faq.formats.answer_html": (
        "JPEG, PNG, WebP, HEIC/HEIF e a maioria dos formatos que o Pillow consegue descodificar, até "
        "50 MB."
    ),
    "faq.why_metadata.answer_html": (
        "As credenciais de conteúdo C2PA e as etiquetas de software de edição são indícios de "
        "proveniência. O painel mostra que blocos (EXIF, XMP, IPTC, C2PA, ICC) o ficheiro contém "
        'para que os possa ponderar juntamente com a pontuação. Veja <a href="/c2pa">as credenciais '
        'de conteúdo C2PA</a> e <a href="/remove-image-metadata">como remover metadados de '
        "imagens</a>."
    ),
    "faq.different_model.answer_html": (
        "Sim. Defina <code>PICAI_DETECTOR_MODEL</code> para qualquer modelo de classificação de "
        "imagens do Hugging Face cujas etiquetas nomeiem IA/falso versus humano/real."
    ),
    "faq.free.answer_html": (
        "Sim. O picai é open source sob a licença MIT. A instância alojada é gratuita, com um limite "
        "de 10 análises por endereço IP a cada 24 horas; uma cópia autoalojada não tem limite."
    ),
    "faq.screenshots.answer_html": (
        "Funciona, mas a recodificação, o redimensionamento e as capturas de ecrã removem parte dos "
        "vestígios ao nível dos pixels em que o classificador se baseia, pelo que deve esperar menor "
        "confiança e mais resultados <em>Incerto</em>."
    ),
    "faq.which_generator.answer_html": (
        "Não. O picai avalia, em geral, estatísticas de pixels gerados versus reais; não identifica "
        "o gerador e não tem conhecimento de geradores lançados depois de os dados de treino do seu "
        "modelo terem sido recolhidos."
    ),
    "faq.false_positive.answer_html": (
        "Filtros intensos, processamento HDR, ampliação, ilustrações e renderizações 3D partilham "
        "características estatísticas com imagens geradas. A pontuação é uma probabilidade, não uma "
        "prova; ocorrem falsos positivos."
    ),
    "faq.offline.answer_html": (
        "Sim. Depois de a primeira execução transferir o modelo para a cache do Hugging Face, um "
        "picai autoalojado não precisa de acesso à rede."
    ),
    "faq.rate_limit.answer_html": (
        "Sim: 10 análises por IP de cliente em qualquer janela deslizante de 24 horas. As respostas "
        "incluem <code>X-RateLimit-Remaining</code>, e um pedido acima do limite devolve 429 com um "
        "cabeçalho <code>Retry-After</code>."
    ),
    "nav.detector": "Detetor",
    "nav.how_it_works": "Como funciona",
    "nav.how-to-tell-if-an-image-is-ai-generated": "Guia",
    "nav.api": "API",
    "nav.self-host": "Autoalojar",
    "footer.remove-image-metadata": "Remover metadados",
    "footer.c2pa": "C2PA",
    "footer.faq": "FAQ",
    "footer.privacy": "Privacidade",
    "footer.self-host": "Autoalojar",
    "footer.about": "Sobre",
    "ui.nav_aria_label": "Navegação principal",
    "ui.loading_status": "A carregar o detetor…",
    "ui.hero_overline": "— Análise forense de imagens IA, open source",
    "ui.hero_heading_line1": "Esta fotografia é real?",
    "ui.hero_heading_line2": "Obtenha a pontuação e a prova.",
    "ui.tool_aria_label": "Detetor de imagens IA",
    "ui.dropzone_aria_label": "Enviar uma imagem para analisar",
    "ui.dropzone_title_fine": "Arraste e largue uma fotografia",
    "ui.dropzone_title_coarse": "Verificar uma fotografia",
    "ui.dropzone_sub_fine": "ou cole a partir da área de transferência, ou",
    "ui.dropzone_sub_coarse": "a partir da sua biblioteca ou câmara",
    "ui.btn_check_image_fine": "Verificar esta imagem",
    "ui.btn_choose_photo_coarse": "Escolher fotografia",
    "ui.btn_take_photo": "Tirar uma fotografia",
    "ui.dismiss_aria_label": "Fechar",
    "ui.analyzing_prefix": "A analisar",
    "ui.analyzing_suffix": "· pixels · blocos de metadados",
    "ui.verdict_overline": "— Veredito",
    "ui.meter_real": "Real",
    "ui.meter_uncertain": "Incerto",
    "ui.meter_ai": "IA",
    "ui.model_label": "Modelo",
    "ui.verdict_disclaimer_html": (
        "Os resultados são probabilidades de um classificador, não vereditos. "
        '<a href="/how-accurate">Como interpretar a pontuação.</a>'
    ),
    "ui.btn_check_another": "Verificar outra imagem",
    "ui.preview_overline": "— Pré-visualização",
    "ui.preview_alt": "Pré-visualização da imagem enviada",
    "ui.metadata_overline": "— Metadados",
    "ui.metadata_heading": "Encontrado no ficheiro.",
    "ui.jpeg_segments_label": "Segmentos JPEG",
    "ui.btn_download_clean": "Transferir a cópia limpa",
    "ui.metadata_scrub_note_html": (
        "Reconstruída a partir dos pixels, pelo que cada bloco acima desapareceu. "
        '<a href="/remove-image-metadata">Como funciona</a>'
    ),
    "ui.how_it_works_overline": "— Como funciona",
    "ui.how_it_works_heading": "Três passos. Nada é guardado.",
    "ui.how_it_works_links_html": (
        '<a href="/how-to-tell-if-an-image-is-ai-generated">Leia o guia para identificar imagens '
        'IA</a> ou <a href="/self-host">execute-o na sua própria máquina</a>.'
    ),
    "ui.faq_overline": "— FAQ",
    "ui.faq_heading": "Antes de perguntar.",
    "ui.faq_more_link": "Mais perguntas e respostas →",
    "ui.footer_tagline": "picai. · open source",
    "ui.footer_detector_label": "Detetor:",
    "ui.breadcrumb_aria_label": "Fio de Ariadne",
    "ui.last_updated_prefix": "Última atualização",
    "ui.source_on_github": "código-fonte no GitHub",
    "ui.btn_try_detector": "Experimentar o detetor",
    "ui.status_ready": "Detetor pronto",
    "ui.status_unreachable": "Servidor inacessível",
    "ui.loading_model_note": "A carregar o modelo do detetor (a primeira execução transfere ~750 MB)…",
    "ui.error_empty_file": "Este ficheiro está vazio.",
    "ui.error_file_too_large": "{name} tem {size} — o limite é de 50 MB.",
    "ui.error_server_unreachable": "Não foi possível contactar o servidor: {message}",
    "ui.verdict_ai": "Provavelmente gerada por IA",
    "ui.verdict_real": "Provavelmente uma fotografia real",
    "ui.verdict_uncertain": "Incerto",
    "ui.confidence_suffix": "confiança",
    "ui.format_unknown": "desconhecido",
    "ui.metadata_present": "Presente",
    "ui.metadata_not_present": "Ausente",
    "ui.no_jpeg_segments": "Sem segmentos JPEG APP",
    "ui.quota_remaining": "{remaining} de {limit} análises restantes hoje",
}
