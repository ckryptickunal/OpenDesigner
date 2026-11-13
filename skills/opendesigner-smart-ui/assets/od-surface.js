/* <od-surface>: OpenDesigner Smart UI renderer. Plain custom element, no framework, no dependencies besides
   od-validate.js. It clones each library component's own template (from od-components.js, generated from the
   library) and fills the marked slots with plain text only (textContent; never innerHTML with model text). Styling
   comes only from the page's tokens.css and the components' scoped CSS: the renderer has no style API.

   Use:
     <link rel="stylesheet" href="tokens.css"><link rel="stylesheet" href="od-surface.css">
     <script src="od-components.js"></script>
     <script type="module" src="od-surface.js"></script>
     <od-surface></od-surface>
     el.catalog = catalogJson;         // from smartui.py catalog
     el.source = dataTheModelWasGiven; // optional: every number must come from it (R6)
     el.process(messages, {partial}); // A2UI v1.0 messages; returns the validator's result
     el.addEventListener("od-action", e => send(e.detail));   // an A2UI action message, after the person pressed it
     el.addEventListener("od-error", e => repair(e.detail));  // A2UI error messages for the model to repair
   MIT. */
import { validate, toText, od } from "./od-validate.js";

const G = typeof window !== "undefined" ? window : globalThis;
const REG = () => ((G.ODSmartUI = G.ODSmartUI || {}).components = G.ODSmartUI.components || {});
let uid = 0;
const SCOPE = "[data-od-item],[data-od-action],[data-od-list]";

/** The one polite live region on the page that announces new surfaces (R5). */
function live() {
  let r = document.getElementById("od-live");
  if (!r) {
    r = document.createElement("div");
    r.id = "od-live";
    r.className = "od-live";
    r.setAttribute("aria-live", "polite");
    r.setAttribute("role", "status");
    document.body.appendChild(r);
  }
  return r;
}
export function announce(text) {
  const r = live();
  r.textContent = "";
  setTimeout(() => { r.textContent = text; }, 60);
}

function ensureStyle(name, def) {
  const id = "odc-style-" + def.slug;
  if (!def.css || document.getElementById(id)) return;
  const s = document.createElement("style");
  s.id = id;
  s.textContent = def.css; // trusted: generated from the library, not from the model
  document.head.appendChild(s);
}

/** Marked elements that belong to this scope: not inside a nested list item, action or list (other than scope itself). */
function marked(scope, sel) {
  const out = [];
  for (const el of scope.querySelectorAll(sel)) {
    let p = el.parentElement, ok = true;
    while (p && p !== scope) {
      if (p.matches(SCOPE)) { ok = false; break; }
      p = p.parentElement;
    }
    if (ok) out.push(el);
  }
  if (scope.matches && scope.matches(sel) && !out.includes(scope)) out.unshift(scope);
  return out;
}

const missing = (v) => v === undefined || v === null || (typeof v === "string" && v === "");

function fmt(v, locale) {
  if (typeof v === "number") return new Intl.NumberFormat(locale || undefined, { maximumFractionDigits: 2 }).format(v);
  return String(v);
}

export class ODSurface extends (G.HTMLElement || class {}) {
  constructor() {
    super();
    this.catalog = null;
    this.source = undefined;
    this.maxParts = undefined;
    this.log = [];
    this.state = {};
    this.emptyText = "Nothing to show yet.";
  }

  connectedCallback() {
    this.classList.add("od-surface");
    live();
  }

  /** Apply A2UI messages. Invalid answers render nothing new and fire od-error with repairable A2UI errors. */
  process(messages, opts = {}) {
    if (!this.catalog) throw new Error("od-surface: set .catalog first (smartui.py catalog)");
    const list = Array.isArray(messages) ? messages : [messages];
    const next = this.log.concat(list);
    const r = validate(next, this.catalog, { partial: !!opts.partial, allowEmpty: !!opts.allowEmpty, source: this.source, limits: { leaves: this.maxParts } });
    if (!r.ok) {
      this.dispatchEvent(new CustomEvent("od-error", { bubbles: true, detail: {
        errors: r.errors, a2ui: r.errors.map((e) => ({ version: "1.0", error: { code: e.code, path: e.path, message: e.message, surfaceId: e.surfaceId } })) } }));
      return r;
    }
    this.log = next;
    const isNew = !Object.keys(this.state).length;
    this.state = r.surfaces;
    this.render(!!opts.partial);
    if (!opts.partial && (isNew || opts.announce)) {
      const names = this.querySelectorAll("[data-od-component]");
      const first = names[0] && this.catalog.components[names[0].dataset.odComponent];
      if (first) announce(`${od(first).name || names[0].dataset.odComponent} shown`);
    }
    return r;
  }

  /** What this renderer supports, as A2UI's a2uiRendererCapabilities: send it to the agent with each request. */
  capabilities() { return { "1.0": { supportedCatalogIds: this.catalog ? [this.catalog.catalogId] : [] } }; }

  /** Start over (a new answer). */
  reset() { this.log = []; this.state = {}; this.replaceChildren(); }

  /** A loading skeleton of one component while its answer is on the way. */
  showLoading(componentName) {
    this.reset();
    const el = this.build({ id: "root", component: componentName }, true);
    if (el) { el.setAttribute("aria-busy", "true"); this.append(el); }
  }

  /** Text for a host that renders no UI. */
  toText() { return toText(this.state, this.catalog); }

  render(partial) {
    const frag = document.createDocumentFragment();
    for (const [sid, s] of Object.entries(this.state)) {
      const root = s.components.root;
      if (!root) continue;
      const el = this.build(root, partial, s);
      if (el) { el.dataset.odSurfaceId = sid; frag.append(el); }
    }
    this.replaceChildren(frag);
    for (const name of new Set([...this.querySelectorAll("[data-od-component]")].map((e) => e.dataset.odComponent))) {
      const def = REG()[name];
      if (def && def.wire) try { def.wire(); } catch (e) { console.warn("od-surface: wiring " + name + " failed", e); }
    }
  }

  build(c, partial, surface) {
    const schema = this.catalog.components[c.component];
    if (!schema) return null;
    if (od(schema).container) {
      const col = document.createElement("div");
      col.className = "od-column";
      col.dataset.gap = c.gap || "md";
      for (const id of c.children || []) {
        const ch = surface && surface.components[id];
        const el = ch && this.build(ch, partial, surface);
        if (el) col.append(el);
      }
      return col;
    }
    const def = REG()[c.component];
    if (!def) { console.warn("od-surface: no template for " + c.component + " (load od-components.js)"); return null; }
    ensureStyle(c.component, def);
    const t = document.createElement("template");
    t.innerHTML = def.html; // trusted library markup; model text goes in with textContent below
    const root = t.content.firstElementChild;
    if (!root) return null;
    root.querySelectorAll("[data-od-sample]").forEach((n) => n.remove());
    const meta = c["@metadata"] || {};
    if (meta.permission === "denied") return this.notice("lock", "You don't have access to this.", meta.permission_note);
    this.fill(root, c, schema, partial, c.id);
    this.uniqueIds(root);
    root.dataset.odComponent = c.component;
    root.dataset.odId = c.id;
    const acc = c["@accessibility"] || {};
    if (acc.label) root.setAttribute("aria-label", acc.label);
    if (acc.description) root.setAttribute("aria-description", acc.description);
    if (acc.hidden) root.setAttribute("aria-hidden", "true");
    if (partial) root.setAttribute("aria-busy", "true");
    if (meta.stale_since) {
      const wrap = document.createElement("div");
      wrap.className = "od-stale";
      wrap.append(this.notice("clock", `Updated ${meta.stale_since}. It may have changed since.`), root);
      return wrap;
    }
    return root;
  }

  notice(kind, text, note) {
    const d = document.createElement("p");
    d.className = "od-notice";
    d.dataset.kind = kind;
    d.textContent = text + (note ? " " + note : "");
    return d;
  }

  fill(scope, data, schema, partial, compId, ctx = {}) {
    data = data || {};
    const props = (schema && schema.properties) || {};
    const locale = this.closest("[lang]")?.getAttribute("lang") || document.documentElement.lang || undefined;
    for (const el of marked(scope, "[data-od-when]")) {
      const [name, vals] = el.dataset.odWhen.split("=");
      if (!vals.split("|").includes(data[name])) el.remove();
    }
    for (const el of marked(scope, "[data-od-slot]")) {
      const name = el.dataset.odSlot;
      if (scope.matches("[data-od-action]") && name === "label") continue;
      const v = data[name];
      if (missing(v)) { el.textContent = ""; el.setAttribute(partial ? "data-od-pending" : "data-od-missing", ""); }
      else el.textContent = fmt(v, locale);
    }
    for (const el of marked(scope, "[data-od-var]")) {
      const name = el.dataset.odVar, v = data[name];
      if (!missing(v)) el.setAttribute("data-" + name, v);
    }
    for (const el of marked(scope, "[data-od-label]")) {
      const v = data[el.dataset.odLabel];
      if (!missing(v)) el.setAttribute("aria-label", String(v)); else el.removeAttribute("aria-label");
    }
    for (const el of marked(scope, "[data-od-input]")) {
      const n = data[el.dataset.odInput];
      if (missing(n)) continue;
      el.name = String(n);
      if (el.tagName === "SELECT" && Array.isArray(data.options)) {
        el.replaceChildren(...data.options.map((o) => { const op = document.createElement("option"); op.value = String(o.value); op.textContent = String(o.label); return op; }));
      }
      if (el.type === "checkbox") el.checked = data.value === true || data.value === "true";
      else if (!missing(data.value)) el.value = String(data.value);
      else if (el.tagName !== "SELECT") el.value = "";
      el.required = data.required === true;
      if (typeof data.min === "number") el.min = String(data.min);
      if (typeof data.max === "number") el.max = String(data.max);
    }
    for (const el of marked(scope, "[data-od-media]")) {
      const v = data[el.dataset.odMedia];
      if (!v || missing(v.src)) { this.missingImage(el, v && v.alt, partial); continue; }
      el.alt = v.alt || "";
      el.addEventListener("error", () => this.missingImage(el, v.alt, false), { once: true });
      el.src = v.src; // the validator allowed this host (R4)
    }
    for (const el of marked(scope, "[data-od-measure]")) {
      const name = el.dataset.odMeasure, v = data[name], p = props[name] || {};
      const max = p.maximum ?? (ctx.max && ctx.max[name]) ?? (typeof v === "number" ? v : 1);
      if (typeof v !== "number") { el.style.setProperty("--od-ratio", "0"); el.setAttribute(partial ? "data-od-pending" : "data-od-missing", ""); }
      else el.style.setProperty("--od-ratio", String(Math.max(0, Math.min(1, max ? v / max : 0))));
    }
    for (const el of marked(scope, "[data-od-action]")) {
      if (el === scope) continue;
      const name = el.dataset.odAction, a = data[name], p = props[name] || {};
      if (!a || !a.label) { if (partial) { el.disabled = true; el.setAttribute("data-od-pending", ""); } else el.remove(); continue; }
      this.fillAction(el, a, p, compId, ctx.itemName, partial);
    }
    for (const el of marked(scope, "[data-od-list]")) {
      const name = el.dataset.odList, items = Array.isArray(data[name]) ? data[name] : [], p = props[name] || {};
      const tpl = el.querySelector(":scope > [data-od-template]") || el.querySelector(":scope > [data-od-item]");
      el.querySelectorAll(":scope > [data-od-item]").forEach((n) => n.remove());
      if (!tpl) continue;
      tpl.removeAttribute("hidden");
      tpl.removeAttribute("data-od-template");
      const itemSchema = p.items || {}, nf = itemSchema["x-od-name-from"];
      const max = {};
      for (const [k, ps] of Object.entries(itemSchema.properties || {})) {
        if (ps["x-od-measure"]) max[k] = Math.max(0, ...items.map((x) => (x && typeof x[k] === "number" ? x[k] : 0)));
      }
      if (!items.length && partial) {
        for (let i = 0; i < 2; i++) { const n = tpl.cloneNode(true); this.fill(n, {}, itemSchema, true, compId, { max }); el.append(n); }
        continue;
      }
      if (!items.length) { el.append(this.emptyItem(tpl)); continue; }
      items.forEach((it, i) => {
        const n = tpl.cloneNode(true);
        n.dataset.odIndex = String(i);
        this.uniqueIds(n);
        this.fill(n, it, itemSchema, partial, compId, { max, itemName: nf && it && typeof it[nf] === "string" ? it[nf] : ctx.itemName });
        el.append(n);
      });
    }
    // optional parts with nothing in them go; a renderer never shows an empty label or a dangling separator
    for (const el of marked(scope, "[data-od-optional]").reverse()) {
      if (partial) continue;
      const own = el.matches("[data-od-missing]");
      const inner = [...el.querySelectorAll("[data-od-slot],[data-od-measure],[data-od-media],[data-od-action]")];
      const anyValue = inner.some((n) => !n.matches("[data-od-missing]"));
      if (own || (inner.length && !anyValue)) el.remove();
    }
  }

  fillAction(el, a, p, compId, itemName, partial) {
    const lab = el.querySelector('[data-od-slot="label"]');
    const hasElements = [...el.children].some((c) => c.tagName.toLowerCase() !== "svg");
    if (lab) lab.textContent = a.label;
    else if (!hasElements && !el.querySelector("svg")) el.textContent = a.label;
    else if (!hasElements) el.setAttribute("aria-label", a.label);
    const name = a.a11y_label || (itemName ? `${a.label}, ${itemName}` : null);
    if (name) el.setAttribute("aria-label", name);
    this.fill(el, a, p, partial, compId, { itemName });
    if (el.tagName === "A") { el.removeAttribute("href"); el.setAttribute("role", "button"); el.tabIndex = 0; }
    el._odAction = { a, effect: p["x-od-effect"] || "none", compId };
    el.dataset.odEvent = a.event.name;
    if (partial) { el.disabled = true; return; }
    const go = (ev) => { ev.preventDefault(); this.pressed(el); };
    el.addEventListener("click", go);
    if (el.tagName === "A") el.addEventListener("keydown", (ev) => { if (ev.key === "Enter" || ev.key === " ") go(ev); });
  }

  missingImage(el, alt, partial) {
    const d = document.createElement("div");
    d.className = el.className + " od-missing-image";
    d.setAttribute("role", "img");
    d.setAttribute("aria-label", alt || "Image not available");
    if (partial) d.setAttribute("data-od-pending", "");
    else d.textContent = alt || "Image not available";
    el.replaceWith(d);
  }

  emptyItem(tpl) {
    const n = document.createElement(tpl.tagName);
    n.className = "od-empty";
    if (tpl.tagName === "TR") {
      const td = document.createElement("td");
      td.colSpan = 99;
      td.textContent = this.emptyText;
      n.append(td);
    } else n.textContent = this.emptyText;
    return n;
  }

  uniqueIds(root) {
    const n = ++uid, map = new Map();
    root.querySelectorAll("[id]").forEach((el) => { const id = el.id; el.id = `${id}-s${n}`; map.set(id, el.id); });
    if (!map.size) return;
    for (const attr of ["for", "aria-labelledby", "aria-describedby", "aria-controls", "aria-owns", "aria-activedescendant", "list", "headers"]) {
      root.querySelectorAll(`[${attr}]`).forEach((el) => el.setAttribute(attr, el.getAttribute(attr).split(/\s+/).map((x) => map.get(x) || x).join(" ")));
    }
    root.querySelectorAll('a[href^="#"]').forEach((a) => { const id = a.getAttribute("href").slice(1); if (map.has(id)) a.setAttribute("href", "#" + map.get(id)); });
  }

  /** The person pressed an action. One that changes data asks first (R3); the model can never press it. */
  pressed(el) {
    const { a, effect, compId } = el._odAction;
    if (el.dataset.odState === "pending") return;
    const surfaceId = el.closest("[data-od-surface-id]")?.dataset.odSurfaceId || Object.keys(this.state)[0];
    const context = { ...(a.event.context || {}) };
    if (el.closest("form")) {
      for (const [k, v] of new FormData(el.closest("form"))) if (typeof v === "string" && !(k in context)) context[k] = v.slice(0, 200);
    }
    const send = (approved) => {
      const detail = { version: "1.0", action: { name: a.event.name, surfaceId, sourceComponentId: compId, timestamp: new Date().toISOString(), context: approved ? { ...context, approved: true } : context } };
      this.dispatchEvent(new CustomEvent("od-action", { bubbles: true, detail }));
    };
    if (effect !== "change") return send(false);
    // a button inside an approval prompt the answer showed is itself the person's approval: don't ask twice
    if (el.closest('[data-od-component="ApprovalPrompt"]')) { send(true); this.setActionState(el, "pending"); return; }
    this.askApproval(el, a, context, () => send(true));
  }

  askApproval(trigger, a, context, onYes) {
    this.querySelector(".od-approval")?.remove();
    const label = a.a11y_label || a.label;
    const data = {
      id: "approval", component: "ApprovalPrompt",
      title: label.length > 60 ? label.slice(0, 59) + "…" : label,
      summary: "Nothing happens until you confirm.",
      details: Object.entries(context).filter(([, v]) => v !== "" && v !== undefined).slice(0, 6).map(([k, v]) => ({ label: k.replace(/_/g, " ").replace(/^./, (c) => c.toUpperCase()), value: String(v) })),
      approve: { label: "Confirm", event: { name: "approve" } },
      cancel: { label: "Cancel", event: { name: "cancel" } },
    };
    const schema = this.catalog.components.ApprovalPrompt;
    const def = REG().ApprovalPrompt;
    let box;
    if (schema && def) {
      ensureStyle("ApprovalPrompt", def);
      const t = document.createElement("template");
      t.innerHTML = def.html;
      box = t.content.firstElementChild;
      box.querySelectorAll("[data-od-sample]").forEach((n) => n.remove());
      this.fill(box, data, schema, false, "approval");
      this.uniqueIds(box);
      box.querySelectorAll("[data-od-action]").forEach((b) => b.replaceWith(b.cloneNode(true))); // our own handlers below
    } else {
      box = document.createElement("div");
      const p = document.createElement("p"); p.textContent = `${label}? Nothing happens until you confirm.`;
      const y = document.createElement("button"); y.type = "button"; y.dataset.odAction = "approve"; y.textContent = "Confirm";
      const n = document.createElement("button"); n.type = "button"; n.dataset.odAction = "cancel"; n.textContent = "Cancel";
      box.append(p, n, y);
    }
    const wrap = document.createElement("div");
    wrap.className = "od-approval";
    wrap.setAttribute("role", "group");
    wrap.setAttribute("aria-label", "Confirm before it happens");
    wrap.append(box);
    const close = () => { wrap.remove(); trigger.focus(); };
    wrap.addEventListener("keydown", (e) => { if (e.key === "Escape") close(); });
    wrap.querySelector('[data-od-action="cancel"]')?.addEventListener("click", close);
    wrap.querySelector('[data-od-action="approve"]')?.addEventListener("click", () => { wrap.remove(); onYes(); this.setActionState(trigger, "pending"); });
    (trigger.closest("[data-od-component]") || this).after(wrap);
    (wrap.querySelector('[data-od-action="cancel"]') || wrap.querySelector("button"))?.focus();
  }

  /** The host reports what happened to an action: pending, done or failed, with a short note for the live region. */
  setActionState(target, state, note) {
    const el = typeof target === "string" ? this.querySelector(`[data-od-event="${CSS.escape(target)}"]`) : target;
    if (!el) return;
    el.dataset.odState = state;
    el.setAttribute("aria-busy", state === "pending" ? "true" : "false");
    el.disabled = state === "pending" || state === "done";
    if (note) announce(note);
  }
}

if (G.customElements && !G.customElements.get("od-surface")) G.customElements.define("od-surface", ODSurface);
G.ODSmartUI = Object.assign(G.ODSmartUI || {}, { ODSurface, announce });
export default ODSurface;
