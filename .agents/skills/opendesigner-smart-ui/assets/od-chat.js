/* A reference chat client for Smart UI: a message list, a composer and suggestion chips, talking to a server that runs
   the Smart UI turn (live.py: POST /api/chat, POST /api/press). Each answer's text shows as a message; its part shows in
   an <od-surface> that validates it again before drawing. Buttons the person presses go back to /api/press; changes
   only after the approval prompt (od-surface adds approved: true). Copy it, or read it as an example. MIT.

   The server streams each turn (one JSON object per line): the chosen part's skeleton first, then the words as they
   arrive, then the checked answer. A server that doesn't stream answers with one JSON object, which works too.

   <od-chat data-catalog="/system/smart-ui/catalog.json" data-placeholder="Ask about your billing"></od-chat>
   (needs od-surface.js loaded) */
import { announce } from "./od-surface.js";

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
    this.classList.add("od-chat");
    const loading = el("p", "od-chat-wait", "Loading the assistant…");
    this.setAttribute("aria-busy", "true");
    this.replaceChildren(loading);
    try {
      const res = await fetch(this.dataset.catalog || "/system/smart-ui/catalog.json");
      if (!res.ok) throw new Error(res.status);
      this.catalog = await res.json();
    } catch {
      this.removeAttribute("aria-busy");
      const retry = el("button", "od-chat-chip", "Try again");
      retry.type = "button";
      retry.addEventListener("click", () => { this._ready = false; this.connectedCallback(); });
      this.replaceChildren(el("p", "od-chat-error", "The assistant didn't load. Check your connection, then try again."), retry);
      return;
    }
    this.removeAttribute("aria-busy");
    loading.remove();
    let info = {};
    try { info = await (await fetch("/api/info")).json(); } catch { info = { provider: "none" }; }
    this.info = info;
    const head = el("p", "od-chat-mode",
      info.provider && info.provider !== "recorded" ? `Live: ${info.model || info.provider}` : "Recorded answers (no model key found)");
    this.log = el("div", "od-chat-log");
    this.log.setAttribute("aria-label", "Conversation");
    this.chips = el("div", "od-chat-chips");
    const form = el("form", "od-chat-form");
    const input = el("input");
    input.type = "text";
    input.name = "message";
    input.placeholder = this.dataset.placeholder || "Type your question";
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
    let r, early = null;
    try {
      const res = await fetch(url, { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify({ ...body, stream: true }) });
      if ((res.headers.get("content-type") || "").includes("ndjson") && res.body) {
        const reader = res.body.getReader(), dec = new TextDecoder();
        let buf = "";
        for (;;) {
          const { value, done } = await reader.read();
          if (done) break;
          buf += dec.decode(value, { stream: true });
          let i;
          while ((i = buf.indexOf("\n")) >= 0) {
            const ev = JSON.parse(buf.slice(0, i));
            buf = buf.slice(i + 1);
            if (ev.type === "done") r = ev;
            else if (ev.type === "error") throw new Error(ev.error);
            else early = this.early(early, ev);
          }
        }
        if (!r) throw new Error("the answer stopped early");
      } else {
        r = await res.json();
        if (!res.ok) throw new Error(r.error || res.status);
      }
    } catch (e) {
      this.busy(false);
      early?.turn.remove();
      this.log.append(el("p", "od-chat-error", "The assistant couldn't answer: " + (e.message || e)));
      return;
    }
    this.busy(false);
    this.show(r, early);
  }

  /** While the answer is on its way: the chosen part's skeleton, then the words. Hidden from screen readers until the
   *  checked answer replaces it (one announcement per turn). */
  early(state, ev) {
    if (!state) {
      const turn = el("div", "od-chat-turn od-chat-pending");
      turn.setAttribute("aria-hidden", "true");
      this.wait?.remove();
      this.log.append(turn);
      state = { turn, text: null, surface: null };
      this.reveal(turn, true);
    }
    if (ev.type === "text") {
      if (!state.text) { state.text = el("p", "od-chat-bot"); state.turn.prepend(state.text); }
      state.text.textContent = ev.text;
    } else if (ev.type === "skeleton" && !state.surface) {
      const s = document.createElement("od-surface");
      s.catalog = this.catalog;
      state.turn.append(s);
      s.showLoading(ev.part);
      state.surface = s;
    }
    return state;
  }

  show(r, early) {
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
    if (log.repaired && log.first_errors && log.first_errors.length) {  // only a real second model call; a case fix made here isn't one
      turn.append(el("p", "od-chat-note", `Repaired once: the first answer failed ${log.first_errors.length} check${log.first_errors.length > 1 ? "s" : ""} (${log.first_errors.slice(0, 2).join("; ")}).`));
    }
    if (early) early.turn.replaceWith(turn); else this.log.append(turn);
    this.reveal(turn);
    if (!r.answer && r.text) announce(r.text.slice(0, 200));  // a part announces itself; a text-only reply is read here
  }

  /** Bring the newest answer's top into view, in the log and on the page (a phone shows the reply, not the old turns). */
  reveal(turn, quick) {
    const still = quick || matchMedia("(prefers-reduced-motion: reduce)").matches;
    requestAnimationFrame(() => turn.isConnected && turn.scrollIntoView({ block: "start", behavior: still ? "auto" : "smooth" }));
  }
}

if (!customElements.get("od-chat")) customElements.define("od-chat", ODChat);
export default ODChat;
