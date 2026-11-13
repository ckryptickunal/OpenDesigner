// The demo chat. Each turn is recorded (turns.json): the person's message, the assistant's text, and its answer as A2UI
// messages. Every answer goes through <od-surface>, which validates it against the catalog before anything renders.
import { announce } from "../../skills/opendesigner-smart-ui/assets/od-surface.js";

const base = new URL(".", import.meta.url);
const catalog = await (await fetch(new URL("opendesigner/smart-ui/catalog.json", base))).json();
const { turns, broken } = await (await fetch(new URL("turns.json", base))).json();
const log = document.getElementById("log");
const next = document.getElementById("next");
let textOnly = false;
let played = 0;

function el(tag, cls, text) {
  const n = document.createElement(tag);
  if (cls) n.className = cls;
  if (text) n.textContent = text;
  return n;
}

// bring the newest turn's top into view (not just the bottom of the log: a tall answer would hide its own heading)
function scroll() {
  const last = log.lastElementChild;
  if (!last) return;
  const still = matchMedia("(prefers-reduced-motion: reduce)").matches;
  requestAnimationFrame(() => last.scrollIntoView({ block: "start", behavior: still ? "auto" : "smooth" }));
}

function surfaceFor(turn) {
  const s = document.createElement("od-surface");
  s.catalog = catalog;
  s.source = turn.data;           // R6: every number must come from the data the assistant had
  s.addEventListener("od-action", (e) => pressed(s, e.detail.action, turn));
  return s;
}

function show(turn, wrap) {
  if (turn.text) wrap.append(el("p", "bot", turn.text));
  if (!turn.answer) return;
  const s = surfaceFor(turn);
  if (textOnly) {
    // a host that shows no interface still gets the whole answer, as text
    const tmp = surfaceFor(turn);
    tmp.process(turn.answer);
    wrap.append(el("pre", "fallback", tmp.toText()));
    return;
  }
  wrap.append(s);
  const r = s.process(turn.answer);
  wrap.append(el("p", "checked", r.ok ? "Checked before it showed: no errors." : "Not shown: it failed the checks."));
}

// Live mode: when the page is served by live.py with a model, questions go to the model instead of the recordings.
let live = null;
const SID = Math.random().toString(36).slice(2, 10);
try {
  const r = await fetch(new URL("api/info", base));
  if (r.ok) { const info = await r.json(); if (info.provider && info.provider !== "recorded") live = info; }
} catch { /* recorded mode */ }

async function post(path, body) {
  const r = await fetch(new URL(path, base), { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify({ session: SID, ...body }) });
  const j = await r.json();
  if (!r.ok) throw new Error(j.error || r.status);
  return j;
}

async function liveTurn(userText, call) {
  const wrap = el("section", "turn");
  if (userText) wrap.append(el("p", "me", userText));
  const wait = el("p", "sys", "Thinking…");
  wrap.append(wait);
  log.append(wrap);
  scroll();
  let r;
  try { r = await call(); } catch (e) { wait.textContent = "The assistant couldn't answer: " + (e.message || e); return; }
  wait.remove();
  show({ text: r.text, answer: r.answer, data: r.data, live: true }, wrap);
  if (!r.answer && r.text) announce(r.text.slice(0, 200));
  const lg = r.log || {};
  if (lg.first_errors && lg.first_errors.length) wrap.append(el("p", "checked", `Repaired once: the first answer failed ${lg.first_errors.length} check(s).`));
  scroll();
}

function play(i) {
  if (live) { played = Math.max(played, i + 1); offer(); return liveTurn(turns[i].user, () => post("api/chat", { message: turns[i].user })); }
  const turn = turns[i];
  const wrap = el("section", "turn");
  wrap.setAttribute("aria-label", `Turn ${i + 1}`);
  wrap.append(el("p", "me", turn.user));
  log.append(wrap);
  show(turn, wrap);
  played = Math.max(played, i + 1);
  offer();
  scroll();
}

function offer() {
  next.replaceChildren();
  turns.forEach((t, i) => {
    if (i < played || t.after) return;
    const b = el("button", "ask", t.user);
    b.type = "button";
    b.addEventListener("click", () => play(i));
    next.append(b);
  });
}

// A button the person pressed. Changes (book, pay, cancel) arrive here only after the approval prompt said yes.
function pressed(surface, action, turn) {
  if (live) {
    const btn = surface.querySelector(`[data-od-event="${action.name}"]`);
    if (btn) surface.setActionState(btn, "pending", "Sending");
    return liveTurn(null, () => post("api/press", { action })).then(() => { if (btn) surface.setActionState(btn, "done", "Done"); });
  }
  const wrap = surface.closest(".turn");
  const line = el("p", "sys");
  line.append("Sent to the assistant: ", el("code", "", action.name + (Object.keys(action.context).length ? " " + JSON.stringify(action.context) : "")));
  wrap.append(line);
  const follow = turns.findIndex((t) => t.after === action.name);
  if (follow < 0) { scroll(); return; }
  const btn = surface.querySelector(`[data-od-event="${action.name}"]`);
  if (btn) surface.setActionState(btn, "pending", "Booking");
  setTimeout(() => {
    if (btn) surface.setActionState(btn, "done", "Done");
    const t = turns[follow];
    const w = el("section", "turn");
    log.append(w);
    show(t, w);
    scroll();
  }, 900);
  scroll();
}

document.getElementById("bad").addEventListener("click", () => {
  const wrap = el("section", "turn");
  wrap.append(el("p", "me", broken.user));
  wrap.append(el("p", "bot", broken.text));
  const s = surfaceFor(broken);
  s.addEventListener("od-error", (e) => {
    const list = el("ul", "errors");
    list.setAttribute("aria-label", "What the validator sent back to the model");
    for (const x of e.detail.errors) list.append(el("li", "", `${x.rule}: ${x.message}${x.fix ? ". Fix: " + x.fix : ""}`));
    wrap.append(el("p", "sys", "Not shown. The validator refused it and sent this back for the model to repair:"), list);
  });
  log.append(wrap);
  s.process(broken.answer);
  scroll();
});

document.getElementById("system").addEventListener("change", (e) => {
  document.getElementById("tokens").href = e.target.value;  // the same answers, another system's tokens
});
document.getElementById("theme").addEventListener("click", (e) => {
  const dark = e.currentTarget.getAttribute("aria-pressed") !== "true";
  e.currentTarget.setAttribute("aria-pressed", String(dark));
  document.documentElement.setAttribute("data-theme", dark ? "dark" : "light");
});
document.getElementById("textonly").addEventListener("click", (e) => {
  textOnly = e.currentTarget.getAttribute("aria-pressed") !== "true";
  e.currentTarget.setAttribute("aria-pressed", String(textOnly));
  const upto = played;
  log.replaceChildren();
  played = 0;
  for (let i = 0; i < upto; i++) if (!turns[i].after) play(i);
});

if (live) {
  document.querySelector(".who p").textContent = `Live: ${live.model || live.provider}`;
  document.querySelector(".note").firstChild.textContent = "Live answers from a real model. Each one is checked before it shows, and repaired once if it fails. ";
  const form = el("form", "ask-form");
  const input = el("input");
  input.type = "text"; input.placeholder = "Ask about your trip"; input.setAttribute("aria-label", "Message");
  const go = el("button", "ask", "Send"); go.type = "submit";
  form.append(input, go);
  form.addEventListener("submit", (e) => { e.preventDefault(); const m = input.value.trim(); if (m) { input.value = ""; liveTurn(m, () => post("api/chat", { message: m })); } });
  next.after(form);
  offer();
} else play(0);
