window.picaiAdminLogin = async function picaiAdminLogin(response) {
  const errorEl = document.getElementById("admin-error");
  try {
    const res = await fetch("/admin/session", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ credential: response.credential }),
    });
    if (res.ok) {
      window.location.reload();
      return;
    }
    const body = await res.json().catch(() => ({}));
    if (errorEl) {
      errorEl.textContent = body.detail || "Sign-in failed.";
      errorEl.hidden = false;
    }
  } catch (err) {
    if (errorEl) {
      errorEl.textContent = "Could not reach the server.";
      errorEl.hidden = false;
    }
  }
};
