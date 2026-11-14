// The Smart UI demo on opendesigner.dev (/smart-ui/demo/), from examples/smart-ui-chat/chat.js with the site's paths.
// Each turn is recorded (turns.json): the person's message, the assistant's text, and its answer as A2UI messages. Every
// answer goes through <od-surface>, which validates it against the catalog before anything renders.
// ?mini (the home page's preview): plays the first answer only, with no controls, and takes no input.
import "./od-surface.js";

const base = new URL(".", import.meta.url);
const catalog = await (await fetch(new URL("catalog.json", base))).json();
const { turns, broken } = await (await fetch(new URL("turns.json", base))).json();
const mini = new URLSearchParams(location.search).has("mini");
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

// Scroll the conversation itself, never the page around the frame (scrollIntoView would move the parent page too).
function scrollTo(node) {
  if (mini || !node) return;
  log.scrollTop = Math.max(0, node.offsetTop - log.offsetTop - 8);
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
  if (!mini) wrap.append(el("p", "checked", r.ok ? "Checked before it showed: no errors." : "Not shown: it failed the checks."));
}

function play(i) {
  const turn = turns[i];
  const wrap = el("section", "turn");
  wrap.setAttribute("aria-label", `Turn ${i + 1}`);
  wrap.append(el("p", "me", turn.user));
  log.append(wrap);
  show(turn, wrap);
  played = Math.max(played, i + 1);
  offer();
  scrollTo(wrap);
}

function offer() {
  if (mini) return;
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
  const wrap = surface.closest(".turn");
  const line = el("p", "sys");
  line.append("Sent to the assistant: ", el("code", "", action.name + (Object.keys(action.context).length ? " " + JSON.stringify(action.context) : "")));
  wrap.append(line);
  const follow = turns.findIndex((t) => t.after === action.name);
  if (follow < 0) { scrollTo(line); return; }
  const btn = surface.querySelector(`[data-od-event="${action.name}"]`);
  if (btn) surface.setActionState(btn, "pending", action.name.startsWith("book") ? "Booking" : "Sending");
  setTimeout(() => {
    if (btn) surface.setActionState(btn, "done", "Done");
    const w = el("section", "turn");
    log.append(w);
    show(turns[follow], w);
    scrollTo(w);
  }, 900);
  scrollTo(line);
}

if (mini) {
  document.documentElement.classList.add("mini");
  document.body.inert = true;  // a picture of the demo: nothing in it can be tabbed to or pressed
  play(0);
} else {
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
    scrollTo(wrap);
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

  play(0);
}
