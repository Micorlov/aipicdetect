"""Simplified Chinese translation table.

Falls back to English (see :func:`aipicdetect.content.locales.t`) for any key not defined here, but
every key from :mod:`aipicdetect.content.locales.en` is translated below.
"""

from __future__ import annotations

STRINGS: dict[str, str] = {
    # Page metadata
    "page.home.title": "AiPicDetect — 开源 AI 图像检测与元数据清除工具",
    "page.home.description": (
        "使用 AiPicDetect——一款免费的开源检测工具——检测图片是否由 AI 生成。可在浏览器中直接使用，"
        "也可通过 Docker 或 Python 在自己的设备上运行。"
    ),
    "page.home.h1": "这张照片是真的吗？获取分数和证据。",
    "page.faq.title": "AI 图像检测常见问题：准确性、隐私、格式、模型",
    "page.faq.description": (
        "关于 AiPicDetect 的常见问题解答：AI 图像检测的准确度如何、图片在哪里处理、支持哪些格式、"
        "如何更换模型以及使用频率限制。"
    ),
    "page.faq.h1": "AiPicDetect 常见问题",
    "page.faq.intro_suffix": "以下是大家最常问到的问题：它是如何工作的、准确度如何，以及上传的图片会发生什么。",
    "page.faq.still_unsure_html": (
        '仍有疑问？请在 <a href="https://github.com/Micorlov/aipicdetect/issues" rel="noopener">GitHub</a> 上提交 issue。'
    ),
    # Home page copy
    "home.entity_sentence": (
        "AiPicDetect 是一款免费的开源工具，用于评估图像由 AI 生成的可能性并清除隐藏的元数据——"
        "无论是使用托管实例还是自行部署，任你选择。"
    ),
    "home.lead": (
        "AiPicDetect 运行一个开放的 AI 检测模型，读取照片携带的每一个 EXIF、C2PA 和 IPTC 字段，"
        "然后为你提供一份清除了全部这些信息的干净副本。无需注册，没有黑箱。"
    ),
    "home.dropzone_note": "JPEG、PNG、WebP、HEIC · 最大 50 MB · 在内存中处理，绝不写入磁盘",
    "home.summary": (
        "AiPicDetect 是一款免费的开源工具，用于评估图像由 AI 生成的可能性并清除隐藏的元数据——"
        "无论是使用托管实例还是自行部署，任你选择。它使用开放的 Hugging Face 分类器评估图片由 "
        "AI 生成器生成的可能性，还可以重新渲染图像以清除 EXIF、XMP、IPTC、ICC 和 C2PA 元数据。"
        "可使用托管实例，也可通过 Docker 或 Python 自行部署。"
    ),
    "home.stat.0": "开放模型，<br>无第三方 API",
    "home.stat.1": "无需<br>注册",
    "home.stat.2": "MB<br>最大上传",
    # Detect steps
    "steps.detect.upload.name": "上传。",
    "steps.detect.upload.text": (
        "拖放、粘贴或选择一张图片。图片会发送到你正在使用的 AiPicDetect 服务器"
        "（自行部署时即为你自己的设备），保存在内存中，绝不写入磁盘。"
    ),
    "steps.detect.detect.name": "检测。",
    "steps.detect.detect.text": "一个开源图像分类器会评估这些像素由生成器生成的可能性。",
    "steps.detect.decide.name": "判断。",
    "steps.detect.decide.text": (
        "你将获得 AI 生成的可能性、置信区间，以及文件携带的元数据信息块——"
        "这是一种概率，而不是定论。"
    ),
    # Scrub steps — <code> blocks contain literal shell commands and must stay untranslated
    "steps.scrub.inspect.name": "检查。",
    "steps.scrub.inspect.text": (
        "运行 <code>aipicdetect inspect photo.jpg</code>，列出文件携带的 EXIF、XMP、IPTC、"
        "C2PA 和 ICC 信息块。"
    ),
    "steps.scrub.scrub.name": "清除。",
    "steps.scrub.scrub.text": (
        "运行 <code>aipicdetect scrub photo.jpg</code>（或调用 <code>POST /scrub</code>）。"
        "AiPicDetect 会解码像素、应用 EXIF 方向信息，并从原始像素缓冲区重新构建一张全新的图像。"
    ),
    "steps.scrub.verify.name": "验证。",
    "steps.scrub.verify.text": (
        "运行 <code>aipicdetect inspect photo.clean.jpg</code>；应输出"
        "「no metadata signatures found」。"
    ),
    # FAQ (home slugs)
    "faq.accuracy.question": "这个检测器有多准确？",
    "faq.accuracy.answer_html": (
        "它给出的是概率，而不是定论。接近 50% 的分数会被标记为<em>不确定</em>；"
        "请将任何单次结果视为一个参考信号，并结合其他证据一起判断。"
        '更多内容请参阅<a href="/how-accurate">AI 图像检测器的准确性说明</a>。'
    ),
    "faq.leaves_computer.question": "我的图片会离开我的电脑吗？",
    "faq.leaves_computer.answer_html": (
        "在这个公共实例上，会的：图片会上传到 AiPicDetect 服务器（由作者运行的 Google Cloud Run "
        "容器），在内存中完成评分，绝不写入磁盘。清除后的副本只会保存在内存中，"
        "直到被 100 条更新的结果替换，或容器重启为止，且不会发送给任何第三方 API。"
        '如果你希望任何内容都不离开你的设备，可以<a href="/self-host">自行运行 AiPicDetect</a>，'
        '只需一条 Docker 命令。详情见<a href="/privacy">隐私页面</a>。'
    ),
    "faq.open_source.question": "这是开源的吗？",
    "faq.open_source.answer_html": (
        "是的。代码、Docker 镜像、命令行工具（CLI）和 GitHub Action 都在"
        '<a href="https://github.com/Micorlov/aipicdetect" rel="noopener">AiPicDetect 代码仓库</a>中，'
        "遵循 MIT 许可证。检测器使用的是一个开放的 Hugging Face 模型，你可以查看或替换它。"
    ),
    "faq.remove_metadata.question": "我可以移除 C2PA 和其他元数据吗？",
    "faq.remove_metadata.answer_html": (
        "可以。检测完图片后，使用<em>下载干净副本</em>功能即可。AiPicDetect 会根据图片的像素"
        "重新构建图像，因此 EXIF、XMP、IPTC、C2PA 以及 ICC 配置文件都会被完全去除。"
        '<a href="/remove-image-metadata">了解清除功能的工作原理</a>。'
    ),
    "faq.formats.question": "支持哪些格式？",
    "faq.formats.answer_html": (
        "支持 JPEG、PNG、WebP、HEIC/HEIF 以及 Pillow 库能够解码的大多数格式，"
        "文件大小最高 50 MB。"
    ),
    "faq.why_metadata.question": "为什么会列出元数据？",
    "faq.why_metadata.answer_html": (
        "C2PA 内容凭证和编辑软件标签是关于图片来源的线索。面板会显示文件携带了哪些信息块"
        "（EXIF、XMP、IPTC、C2PA、ICC），以便你结合检测分数一起权衡。"
        '参见<a href="/c2pa">C2PA 内容凭证</a>与'
        '<a href="/remove-image-metadata">如何移除图像元数据</a>。'
    ),
    "faq.different_model.question": "我可以使用其他模型吗？",
    "faq.different_model.answer_html": (
        "可以。将 <code>PICAI_DETECTOR_MODEL</code> 设置为任意一个 Hugging Face "
        "图像分类模型，只要它的标签能够区分 AI/伪造 与 人类/真实 内容即可。"
    ),
    # FAQ (more slugs)
    "faq.free.question": "AiPicDetect 是免费的吗？",
    "faq.free.answer_html": (
        "是的。AiPicDetect 是遵循 MIT 许可证的开源项目。托管实例可免费使用，"
        "限制为每个 IP 地址每 24 小时 10 次检测；自行部署的版本没有此限制。"
    ),
    "faq.screenshots.question": "它能处理截图或高度压缩的图片吗？",
    "faq.screenshots.answer_html": (
        "可以运行，但重新编码、缩放和截图会去除分类器所依赖的部分像素级痕迹，"
        "因此置信度可能较低，出现<em>不确定</em>结果的概率也会更高。"
    ),
    "faq.which_generator.question": "它能判断图片是由哪个生成器制作的吗（例如 Midjourney、DALL·E、Stable Diffusion）？",
    "faq.which_generator.answer_html": (
        "不能。AiPicDetect 评估的是生成图像与真实图像在像素统计特征上的整体差异；"
        "它不会识别具体的生成器，也不了解在其模型训练数据收集之后发布的生成器。"
    ),
    "faq.false_positive.question": "为什么一张真实照片被判定为 AI 生成？",
    "faq.false_positive.answer_html": (
        "强力滤镜、HDR 处理、放大、插画和 3D 渲染都与生成图像在统计特征上有相似之处。"
        "该分数是一种概率，而不是证据；误判是可能发生的。"
    ),
    "faq.offline.question": "我可以离线使用它吗？",
    "faq.offline.answer_html": (
        "可以。首次运行会将模型下载到 Hugging Face 缓存中，之后自行部署的 AiPicDetect "
        "无需联网即可使用。"
    ),
    "faq.rate_limit.question": "托管实例有使用频率限制吗？",
    "faq.rate_limit.answer_html": (
        "有：在任意滚动的 24 小时窗口内，每个客户端 IP 限制 10 次检测。响应中会携带 "
        "<code>X-RateLimit-Remaining</code> 头，超出限制的请求会返回 429 状态码，"
        "并附带 <code>Retry-After</code> 头。"
    ),
    # Navigation
    "nav.detector": "检测器",
    "nav.how_it_works": "工作原理",
    "nav.how-to-tell-if-an-image-is-ai-generated": "指南",
    "nav.api": "API",
    "nav.self-host": "自行部署",
    # Footer
    "footer.remove-image-metadata": "移除元数据",
    "footer.c2pa": "C2PA",
    "footer.faq": "常见问题",
    "footer.privacy": "隐私政策",
    "footer.self-host": "自行部署",
    "footer.about": "关于",
    # UI strings
    "ui.nav_aria_label": "主导航",
    "ui.loading_status": "正在加载检测器…",
    "ui.hero_overline": "— 开源 AI 图像取证",
    "ui.hero_heading_line1": "这张照片是真的吗？",
    "ui.hero_heading_line2": "获取分数和证据。",
    "ui.tool_aria_label": "AI 图像检测器",
    "ui.dropzone_aria_label": "上传一张图片进行检测",
    "ui.dropzone_title_fine": "拖放照片到此处",
    "ui.dropzone_title_coarse": "检测一张照片",
    "ui.dropzone_sub_fine": "或从剪贴板粘贴，或",
    "ui.dropzone_sub_coarse": "从相册或相机选择",
    "ui.btn_check_image_fine": "检测这张图片",
    "ui.btn_choose_photo_coarse": "选择照片",
    "ui.btn_take_photo": "拍摄照片",
    "ui.dismiss_aria_label": "关闭",
    "ui.analyzing_prefix": "分析中",
    "ui.analyzing_suffix": "· 像素 · 元数据信息块",
    "ui.verdict_overline": "— 结果",
    "ui.meter_real": "真实",
    "ui.meter_uncertain": "不确定",
    "ui.meter_ai": "AI",
    "ui.model_label": "模型",
    "ui.verdict_disclaimer_html": (
        "结果是分类器给出的概率，而不是定论。"
        '<a href="/how-accurate">了解如何解读分数。</a>'
    ),
    "ui.btn_check_another": "检测另一张图片",
    "ui.preview_overline": "— 预览",
    "ui.preview_alt": "已上传图片的预览",
    "ui.metadata_overline": "— 元数据",
    "ui.metadata_heading": "文件中发现的信息。",
    "ui.jpeg_segments_label": "JPEG 信息段",
    "ui.btn_download_clean": "下载干净副本",
    "ui.metadata_scrub_note_html": (
        "图像已从像素重新渲染，因此以上所有信息块均已移除。"
        '<a href="/remove-image-metadata">了解工作原理</a>'
    ),
    "ui.how_it_works_overline": "— 工作原理",
    "ui.how_it_works_heading": "三个步骤，不保存任何内容。",
    "ui.how_it_works_links_html": (
        '<a href="/how-to-tell-if-an-image-is-ai-generated">阅读识别 AI 图像的指南</a>，'
        '或<a href="/self-host">在自己的设备上运行</a>。'
    ),
    "ui.faq_overline": "— 常见问题",
    "ui.faq_heading": "在你提问之前。",
    "ui.faq_more_link": "更多问题与解答 →",
    "ui.footer_tagline": "AiPicDetect. · 开源",
    "ui.footer_detector_label": "检测器：",
    "ui.breadcrumb_aria_label": "面包屑导航",
    "ui.last_updated_prefix": "最后更新",
    "ui.source_on_github": "在 GitHub 上查看源码",
    "ui.btn_try_detector": "试用检测器",
    "ui.status_ready": "检测器已就绪",
    "ui.status_unreachable": "无法连接服务器",
    "ui.loading_model_note": "正在加载检测模型（首次运行需下载约 750 MB）…",
    "ui.error_empty_file": "该文件为空。",
    "ui.error_file_too_large": "{name} 大小为 {size}——限制为 50 MB。",
    "ui.error_server_unreachable": "无法连接服务器：{message}",
    "ui.verdict_ai": "很可能是 AI 生成的",
    "ui.verdict_real": "很可能是真实照片",
    "ui.verdict_uncertain": "不确定",
    "ui.confidence_suffix": "置信度",
    "ui.format_unknown": "未知",
    "ui.metadata_present": "存在",
    "ui.metadata_not_present": "不存在",
    "ui.no_jpeg_segments": "没有 JPEG APP 信息段",
    "ui.quota_remaining": "今天还剩 {remaining} / {limit} 次检测",
}
