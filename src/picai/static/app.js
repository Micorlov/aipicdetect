(() => {
  const MAX_UPLOAD_BYTES = 50 * 1024 * 1024;
  const STATUS_POLL_MS = 2000;
  const BLOCKS = ["EXIF", "XMP", "IPTC", "C2PA", "ICC"];
  const VERDICTS = {
    AI: { text: "Likely AI-generated", tone: "ai" },
    Real: { text: "Likely a real photo", tone: "real" },
    Uncertain: { text: "Uncertain", tone: "uncertain" },
  };

  const $ = (id) => document.getElementById(id);
  const el = {
    status: $("status"), dropzone: $("dropzone"), file: $("file"), camera: $("camera"),
    pick: $("pick"), snap: $("snap"), note: $("dz-note"),
    error: $("error"), errorText: $("error-text"), errorClose: $("error-close"),
    loading: $("loading"), loadingName: $("loading-name"), result: $("result"),
    verdictLabel: $("verdict-label"), percent: $("percent"), confidence: $("confidence"), marker: $("marker"),
    model: $("model"), footerModel: $("footer-model"), footerQuota: $("footer-quota"), preview: $("preview"),
    previewFrame: $("preview").parentElement, previewCaption: $("preview-caption"),
    metadata: $("metadata"), segments: $("segments"), reset: $("reset"), download: $("download"),
  };
  const READY_NOTE = el.note.textContent;

  let originalUrl = null;

  function setState(state) {
    document.body.dataset.state = state;
    const busy = state === "analyzing";
    const disabled = state === "loading-model";
    el.dropzone.classList.toggle("is-busy", busy);
    el.dropzone.classList.toggle("is-disabled", disabled);
    el.pick.disabled = el.snap.disabled = busy || disabled;
    el.loading.hidden = !busy;
    el.result.hidden = state !== "result";
    el.note.textContent = disabled ? "Loading detector model (first run downloads ~750 MB)…" : READY_NOTE;
  }

  async function pollStatus() {
    try {
      const res = await fetch("/status");
      if (!res.ok) throw new Error(res.statusText);
      const status = await res.json();
      el.footerModel.textContent = status.model;
      el.status.classList.remove("is-offline");
      if (status.model_loaded) {
        el.status.textContent = "Detector ready";
        if (document.body.dataset.state === "loading-model") setState("idle");
        return;
      }
      el.status.textContent = "Loading detector…";
    } catch {
      el.status.textContent = "Server unreachable";
      el.status.classList.add("is-offline");
    }
    setTimeout(pollStatus, STATUS_POLL_MS);
  }

  function fmt(bytes) {
    if (bytes < 1024) return `${bytes} B`;
    if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`;
    return `${(bytes / 1024 / 1024).toFixed(2)} MB`;
  }

  function showError(message) {
    el.errorText.textContent = message;
    el.error.hidden = false;
    setState("error");
  }

  function clearError() {
    el.error.hidden = true;
    if (document.body.dataset.state === "error") setState("idle");
  }

  function releaseOriginal() {
    if (originalUrl) URL.revokeObjectURL(originalUrl);
    originalUrl = null;
  }

  function reset() {
    releaseOriginal();
    el.file.value = "";
    el.camera.value = "";
    el.previewFrame.classList.remove("unavailable");
    el.error.hidden = true;
    setState("idle");
    el.dropzone.scrollIntoView({ behavior: "smooth", block: "center" });
  }

  async function parseError(res) {
    try {
      const body = await res.json();
      if (typeof body.detail === "string") return body.detail;
      if (Array.isArray(body.detail)) return body.detail.map((d) => d.msg).join("; ");
    } catch { /* non-JSON body */ }
    return `${res.status} ${res.statusText}`;
  }

  function handleFiles(list) {
    const file = list && list[0];
    if (!file) return;
    if (file.size === 0) return showError("That file is empty.");
    if (file.size > MAX_UPLOAD_BYTES) return showError(`${file.name} is ${fmt(file.size)} — the limit is 50 MB.`);
    analyze(file);
  }

  async function analyze(file) {
    releaseOriginal();
    el.error.hidden = true;
    el.loadingName.textContent = file.name;
    setState("analyzing");

    const body = new FormData();
    body.append("file", file);
    try {
      const res = await fetch("/analyze", { method: "POST", body });
      if (!res.ok) return showError(await parseError(res));
      const result = await res.json();
      originalUrl = URL.createObjectURL(file);
      renderResult(file, result);
      setState("result");
      el.result.scrollIntoView({ behavior: "smooth", block: "start" });
    } catch (err) {
      showError(`Could not reach the server: ${err.message}`);
    }
  }

  function renderResult(file, r) {
    renderVerdict(r.detection);
    renderPreview(file, r.input);
    renderMetadata(r.metadata);
    renderDownload(r);
    renderQuota(r.quota);
  }

  function renderDownload(r) {
    el.download.href = r.download_url;
    el.download.setAttribute("download", r.download_name);
    el.download.hidden = false;
  }

  function renderQuota(q) {
    if (!q) return;
    el.footerQuota.textContent = `${q.remaining} of ${q.limit} analyses left today`;
    el.footerQuota.hidden = false;
  }

  function renderVerdict(d) {
    const verdict = VERDICTS[d.classification] || VERDICTS.Uncertain;
    el.verdictLabel.textContent = verdict.text;
    el.verdictLabel.className = `v-label ${verdict.tone}`;
    el.percent.textContent = `${d.percent}%`;
    el.confidence.textContent = `${d.confidence} confidence`;
    el.confidence.className = `chip ${verdict.tone}`;
    el.marker.className = `meter-marker ${verdict.tone}`;
    el.marker.style.left = `${Math.round(d.ai_likelihood * 1000) / 10}%`;
    el.model.textContent = d.model;
  }

  function renderPreview(file, input) {
    el.previewFrame.classList.remove("unavailable");
    el.preview.onerror = () => el.previewFrame.classList.add("unavailable");
    el.preview.src = originalUrl;
    el.previewCaption.textContent =
      `${input.width}×${input.height} · ${input.format || file.type || "unknown"} · ${fmt(input.bytes)}`;
  }

  function renderMetadata(m) {
    el.metadata.replaceChildren(...BLOCKS.map((block) => metadataRow(block, m.removed[block])));
    const counts = new Map();
    for (const seg of m.jpeg_app_segments) counts.set(seg, (counts.get(seg) || 0) + 1);
    if (counts.size === 0) {
      const empty = document.createElement("span");
      empty.className = "empty";
      empty.textContent = "No JPEG APP segments";
      el.segments.replaceChildren(empty);
      return;
    }
    el.segments.replaceChildren(...[...counts].map(([seg, n]) => {
      const chip = document.createElement("span");
      chip.textContent = n > 1 ? `${seg} ×${n}` : seg;
      return chip;
    }));
  }

  function metadataRow(block, signatures) {
    const li = document.createElement("li");
    const found = Array.isArray(signatures) && signatures.length > 0;
    li.className = found ? "found" : "absent";
    const name = document.createElement("span");
    name.className = "name";
    name.textContent = block;
    const state = document.createElement("span");
    state.className = "state";
    state.textContent = found ? "Present" : "Not present";
    li.append(name, state);
    if (found) {
      const sigs = document.createElement("span");
      sigs.className = "sigs";
      sigs.replaceChildren(...signatures.map((s) => {
        const code = document.createElement("code");
        code.textContent = s.replace(/\0/g, "\\0").trim();
        return code;
      }));
      li.append(sigs);
    }
    return li;
  }

  function pickFile() {
    if (el.pick.disabled) return;
    el.file.click();
  }

  el.dropzone.addEventListener("click", pickFile);
  el.pick.addEventListener("click", (e) => { e.stopPropagation(); pickFile(); });
  el.snap.addEventListener("click", (e) => {
    e.stopPropagation();
    if (!el.snap.disabled) el.camera.click();
  });
  el.dropzone.addEventListener("keydown", (e) => {
    if (e.key === "Enter" || e.key === " ") { e.preventDefault(); pickFile(); }
  });
  el.file.addEventListener("change", () => handleFiles(el.file.files));
  el.camera.addEventListener("change", () => handleFiles(el.camera.files));

  ["dragenter", "dragover"].forEach((type) => el.dropzone.addEventListener(type, (e) => {
    e.preventDefault();
    el.dropzone.classList.add("is-over");
  }));
  ["dragleave", "drop"].forEach((type) => el.dropzone.addEventListener(type, () => el.dropzone.classList.remove("is-over")));
  el.dropzone.addEventListener("drop", (e) => {
    e.preventDefault();
    if (!el.pick.disabled) handleFiles(e.dataTransfer.files);
  });
  document.addEventListener("paste", (e) => {
    if (!el.pick.disabled && e.clipboardData.files.length) handleFiles(e.clipboardData.files);
  });

  el.errorClose.addEventListener("click", clearError);
  el.reset.addEventListener("click", reset);

  setState("loading-model");
  pollStatus();
})();
