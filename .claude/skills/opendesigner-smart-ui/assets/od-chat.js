/* A reference chat client for Smart UI: a message list, a composer and suggestion chips, talking to a server that runs
   the Smart UI turn (live.py: POST /api/chat, POST /api/press). Each answer's text shows as a message; its part shows in
   an <od-surface> that validates it again before drawing. Buttons the person presses go back to /api/press; changes
   only after the approval prompt (od-surface adds approved: true). Copy it, or read it as an example. MIT.

   <od-chat data-catalog="/system/smart-ui/catalog.json"></od-chat>   (needs od-surface.js loaded) */
import "./od-surface.js";

const SID = Math.random().toString(36).slice(2, 10);

function el(tag, cls, text) {
  const n = document.createElement(tag);
  if (cls) n.className = cls;
  if (text) n.textContent = text;
  return n;
}

class ODChat extends HTMLElement {
  async connectedCallback() {
    if (this._ready) return;
    this._ready = true;
    this.catalog = await (await fetch(this.dataset.catalog || "/system/smart-ui/catalog.json")).json();
    let info = {};
    try { info = await (await fetch("/api/info")).json(); } catch { info = { provider: "none" }; }
    this.info = info;
    this.classList.add("od-chat");
    const head = el("p", "od-chat-mode",
      info.provider && info.provider !== "recorded" ? `Live: ${info.model || info.provider}` : "Recorded answers (no model key found)");
    this.log = el("div", "od-chat-log");
    this.log.setAttribute("aria-label", "Conversation");
    this.chips = el("div", "od-chat-chips");
    const form = el("form", "od-chat-form");
    const input = el("input");
    input.type = "text";
    input.name = "message";
    input.placeholder = "Ask about your billing";
    input.setAttribute("aria-label", "Message");
    input.autocomplete = "off";
    const send = el("button", "", "Send");
    send.type = "submit";
    form.append(input, send);
    form.addEventListener("submit", (e) => { e.preventDefault(); const m = input.value.trim(); if (m) { input.value = ""; this.ask(m); } });
    this.append(head, this.log, this.chips, form);
    this.suggest(info.suggestions || []);
  }

  suggest(list) {
    this.chips.replaceChildren(...list.map((q) => { const b = el("button", "od-chat-chip", q); b.type = "button"; b.addEventListener("click", () => this.ask(q)); return b; }));
  }

  busy(on) {
    this.toggleAttribute("aria-busy", on);
    this.querySelectorAll(".od-chat-form button, .od-chat-chip").forEach((b) => (b.disabled = on));
    if (on) { this.wait = el("p", "od-chat-wait", "Thinking…"); this.log.append(this.wait); this.scroll(); }
    else this.wait?.remove();
  }

  scroll() { this.log.scrollTop = this.log.scrollHeight; }

  async ask(message) {
    this.log.append(el("p", "od-chat-me", message));
    await this.call("/api/chat", { session: SID, message });
  }

  async call(url, body) {
    this.busy(true);
    let r;
    try {
      const res = await fetch(url, { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify(body) });
      r = await res.json();
      if (!res.ok) throw new Error(r.error || res.status);
    } catch (e) {
      this.busy(false);
      this.log.append(el("p", "od-chat-error", "The assistant couldn't answer: " + (e.message || e)));
      return;
    }
    this.busy(false);
    this.show(r);
  }

  show(r) {
    const turn = el("div", "od-chat-turn");
    if (r.text) turn.append(el("p", "od-chat-bot", r.text));
    if (r.answer) {
      const s = document.createElement("od-surface");
      s.catalog = this.catalog;
      s.source = r.data;
      turn.append(s);
      const res = s.process(r.answer);
      if (!res.ok) { s.remove(); turn.append(el("p", "od-chat-note", "A part was refused by the checks, so only the text shows.")); }
      s.addEventListener("od-action", (e) => {
        const a = e.detail.action;
        const btn = s.querySelector(`[data-od-event="${CSS.escape(a.name)}"]`);
        if (btn) s.setActionState(btn, "pending", "Sending");
        this.call("/api/press", { session: SID, action: a }).then(() => { if (btn) s.setActionState(btn, "done", "Done"); });
      });
    }
    const log = r.log || {};
    if (log.first_errors && log.first_errors.length) {
      turn.append(el("p", "od-chat-note", `Repaired once: the first answer failed ${log.first_errors.length} check${log.first_errors.length > 1 ? "s" : ""} (${log.first_errors.slice(0, 2).join("; ")}).`));
    }
    this.log.append(turn);
    this.scroll();
  }
}

if (!customElements.get("od-chat")) customElements.define("od-chat", ODChat);
export default ODChat;
