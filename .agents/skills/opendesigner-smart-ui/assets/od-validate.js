/* OpenDesigner Smart UI validator. Dependency-free ES module; also sets globalThis.ODSmartUI.validate for plain
   <script> use. The same rules as validate() in scripts/smartui.py; both run assets/fixtures/validator/ in the tests,
   so they cannot drift. MIT. */
const A2UI_VERSION = "1.0";
const LIMITS = { components: 8, depth: 3, leaves: 1 };
const HANDLER = /^on[A-Z_]|^on(click|dblclick|load|error|abort|mouse\w*|key\w*|focus\w*|blur|change|input|submit|pointer\w*|touch\w*|wheel|scroll|drag\w*|drop|animation\w*|transition\w*)$/i;
const BANNED_KEYS = new Set(["style", "class", "classname", "css", "theme", "html", "innerhtml", "outerhtml", "dangerouslysetinnerhtml", "srcdoc"]);
const HTML = /<\s*\/?\s*[a-zA-Z!][^>]*>|<\s*[a-zA-Z]/;
const WHOLE_STYLE = /^\s*(#(?:[0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})|-?\d*\.?\d+(px|rem|em|vh|vw|pt)|(rgba?|hsla?|oklch|oklab|lab|lch|color-mix|var|calc|url|expression)\(.*)\s*$/i;
const NUM = /(?<![\w.])-?\d[\d,]*(?:\.\d+)?/g;
// copy rules (docs/COPY.md), checked when opts.copy; the same as smartui.py
const BANNED_WORDS = /\b(successfully|seamless(ly)?|effortless(ly)?|leverag(e|es|ing)|utili[sz](e|es|ing)|robust|delve|unlock(s|ing)?|empower(s|ing)?|elevate(s|d)?|streamline(s|d)?|cutting-edge|hassle-free|please note)\b/i;
const WORD = /[A-Za-z][A-Za-z'’-]*/g;
export const COPY_RULES = ["copy-word", "copy-case", "duplicate-row"];

function copyCheck(v, path, errs, sid, names) {
  const m = BANNED_WORDS.exec(v);
  if (m) err(errs, "copy-word", path, `'${m[0]}' reads as filler`, sid, `say it plainly without '${m[0]}'`);
  const words = v.match(WORD) || [];
  if (words.length >= 2 && words.length <= 8 && !/[.!?]\s/.test(v)) {
    const later = words.slice(1).filter((w) => w.length >= 3 && !([...w].filter((c) => c >= "A" && c <= "Z").length > 1));
    const caps = later.filter((w) => w[0] >= "A" && w[0] <= "Z" && !names.has(w.toLowerCase()));
    if (caps.length && later.every((w) => w[0] >= "A" && w[0] <= "Z")) err(errs, "copy-case", path, `'${v}' is in Title Case`, sid, "use sentence case: capitalise the first word and names only");
  }
}

function duplicateRows(v, path, errs, sid) {
  const seen = new Map();
  v.forEach((row, i) => {
    if (isObj(row) && "label" in row && (typeof row.value === "string" || typeof row.value === "number")) {
      const key = String(row.value).trim().toLowerCase();
      if (seen.has(key)) err(errs, "duplicate-row", `${path}/${i}`, `'${row.value}' is already shown as '${seen.get(key)}'`, sid, "keep one row for each value");
      else seen.set(key, row.label);
    }
  });
}

/** A table (columns plus rows of cells) names every column it shows: a header per cell, and no blank header. */
function tableHeaders(v, path, errs, sid) {
  const cols = v.columns, rows = v.rows;
  if (!(Array.isArray(rows) && rows.some((r) => isObj(r) && Array.isArray(r.cells)))) return;
  if (!Array.isArray(cols) || !cols.length) { err(errs, "table-headers", `${path}/columns`, "a table needs a header for each column", sid, "add columns with a label for each"); return; }
  cols.forEach((c, i) => { if (isObj(c) && typeof c.label === "string" && !c.label.trim()) err(errs, "table-headers", `${path}/columns/${i}/label`, "a column header is blank", sid, "name the column"); });
  rows.forEach((r, i) => { if (isObj(r) && Array.isArray(r.cells) && r.cells.length > cols.length) err(errs, "table-headers", `${path}/rows/${i}/cells`, `${r.cells.length} cells but ${cols.length} column headers`, sid, "add a header for each column, or drop the extra cells"); });
}

function namesIn(obj, out = new Set()) {
  if (typeof obj === "string") { for (const w of obj.match(WORD) || []) if (w[0] >= "A" && w[0] <= "Z") out.add(w.toLowerCase()); }
  else if (Array.isArray(obj)) obj.forEach((x) => namesIn(x, out));
  else if (isObj(obj)) Object.values(obj).forEach((x) => namesIn(x, out));
  return out;
}

/** Our extra facts, kept where A2UI allows them: metadata.extensions.opendesigner. */
export function od(o) { return ((o && o.metadata) || {}).extensions?.opendesigner || {}; }

function err(errs, rule, path, message, surfaceId, fix) {
  const e = { code: "VALIDATION_FAILED", rule, path, message, surfaceId };
  if (fix) e.fix = fix;
  errs.push(e);
}
const isObj = (v) => v !== null && typeof v === "object" && !Array.isArray(v);
const num = (s) => { const n = Number(String(s).replace(/,/g, "")); return Number.isFinite(n) ? n : null; };

function host(url) {
  const m = /^https:\/\/([^/?#:]+)(:\d+)?([/?#]|$)/.exec(url);
  return m ? m[1].toLowerCase() : null;
}
export function hostAllowed(h, allow) {
  return (allow || []).some((a) => h === a || (a.startsWith("*.") && h.endsWith(a.slice(1))));
}

/* This catalog takes values, not A2UI data bindings: a {"@path": ...} is refused, so what renders is what was checked. */
function resolve(value, data, path, errs, sid) {
  if (isObj(value) && "@path" in value) { err(errs, "binding", path, "this catalog takes values, not @path bindings", sid, "put the value itself here"); return undefined; }
  return value;
}

function typeOk(v, t) {
  if (t === "string") return typeof v === "string";
  if (t === "number") return typeof v === "number" && Number.isFinite(v);
  if (t === "integer") return Number.isInteger(v);
  if (t === "boolean") return typeof v === "boolean";
  if (t === "array") return Array.isArray(v);
  if (t === "object") return isObj(v);
  if (t === "null") return v === null;
  return true;
}
const pyType = (v) => (v === null ? "NoneType" : Array.isArray(v) ? "list" : typeof v === "string" ? "str" : typeof v === "boolean" ? "bool" : typeof v === "number" ? (Number.isInteger(v) ? "int" : "float") : "dict");

function checkValue(v, schema, path, errs, sid, cat, opts, ctx) {
  if (schema.$ref) schema = cat.$defs[schema.$ref.split("/").pop()];
  const types = Array.isArray(schema.type) ? schema.type : schema.type ? [schema.type] : [];
  if (v === null) {
    if (types.length && !types.includes("null")) err(errs, "type", path, `expected ${types.join(" or ")}, got null; leave it out, or the part must allow a missing value`, sid);
    return null;
  }
  v = resolve(v, ctx.data, path, errs, sid);
  if (v === undefined) return v;
  if (types.length && !types.some((t) => typeOk(v, t))) {
    err(errs, "type", path, `expected ${types.join(" or ")}, got ${pyType(v)}`, sid);
    return v;
  }
  if ("const" in schema && v !== schema.const) err(errs, "type", path, `must be '${schema.const}'`, sid);
  if (schema.enum && !schema.enum.includes(v)) {
    err(errs, schema["x-od-token"] ? "R4-token" : "enum", path, `'${v}' is not one of ${JSON.stringify(schema.enum)}`, sid, `use one of: ${schema.enum.join(", ")}`);
    return v;
  }
  if (typeof v === "string") {
    const len = [...v].length;
    if (len > (schema.maxLength ?? Infinity)) err(errs, "length", path, `text is ${len} characters, the most is ${schema.maxLength}`, sid, "shorten it");
    if (len < (schema.minLength ?? 0)) err(errs, "empty", path, "must not be empty", sid);
    if (schema.pattern && !new RegExp(`^(?:${schema.pattern.replace(/^\^|\$$/g, "")})$`).test(v)) err(errs, "pattern", path, `'${v}' does not match ${schema.pattern}`, sid);
    if (schema.format === "uri") {
      const kind = schema["x-od-url"] || "link", h = host(v);
      if (!h) err(errs, "R4-url", path, "only https URLs are allowed", sid);
      else if (!hostAllowed(h, od(cat).allow[kind === "image" ? "images" : "links"])) err(errs, "R4-url", path, `${h} is not on the allow-list for ${kind}s`, sid, "leave it out, or ask the owner to add the domain");
    } else if (!schema["x-od-code"]) {
      if (HTML.test(v)) err(errs, "R4-html", path, "text holds HTML; text is plain only", sid, "write the words without tags");
      else if (WHOLE_STYLE.test(v)) err(errs, "R4-style", path, `'${v}' is a style value (colour, size or CSS); there are no style properties`, sid);
    }
    if (opts.copy && !schema["x-od-code"] && !schema.enum && !schema.pattern && schema.format !== "uri") copyCheck(v, path, errs, sid, ctx.names || new Set());
    if (ctx.numbers && !schema["x-od-code"]) {
      for (const n of v.match(NUM) || []) if (!ctx.numbers.has(num(n))) ctx.warnings.push({ rule: "R6-text", path, message: `${n} in the text is not in the data you were given` });
    }
  }
  if (typeof v === "number") {
    if (("minimum" in schema && v < schema.minimum) || ("maximum" in schema && v > schema.maximum)) err(errs, "range", path, `${v} is outside ${schema.minimum ?? "-inf"} to ${schema.maximum ?? "inf"}`, sid);
    if (ctx.numbers && !ctx.numbers.has(v)) err(errs, "R6-number", path, `${v} is not in the data you were given`, sid, "use the value from the data, or leave it out and show it as missing");
  }
  if (Array.isArray(v)) {
    if (v.length > (schema.maxItems ?? Infinity)) err(errs, "items", path, `${v.length} items, the most is ${schema.maxItems}`, sid, "show fewer, or say how many more there are");
    if (v.length < (schema.minItems ?? 0) && !opts.partial && !opts.allowEmpty) err(errs, "items", path, `${v.length} items, the fewest is ${schema.minItems}`, sid);
    if (opts.copy) duplicateRows(v, path, errs, sid);
    return v.map((x, i) => checkValue(x, schema.items || {}, `${path}/${i}`, errs, sid, cat, opts, ctx));
  }
  if (isObj(v)) {
    const props = schema.properties || {}, addl = "additionalProperties" in schema ? schema.additionalProperties : true;
    if (Object.keys(v).length > (schema.maxProperties ?? Infinity)) err(errs, "items", path, `${Object.keys(v).length} keys, the most is ${schema.maxProperties}`, sid);
    const out = {};
    for (const [k, x] of Object.entries(v)) {
      if (BANNED_KEYS.has(k.toLowerCase()) || HANDLER.test(k)) { err(errs, "R4-key", `${path}/${k}`, `'${k}' is not allowed: no style, class, theme, HTML or event-handler keys`, sid, "remove it"); continue; }
      if (k in props) out[k] = checkValue(x, props[k], `${path}/${k}`, errs, sid, cat, opts, ctx);
      else if (isObj(addl)) out[k] = checkValue(x, addl, `${path}/${k}`, errs, sid, cat, opts, ctx);
      else if (addl === false) err(errs, "unknown-property", `${path}/${k}`, `unknown property '${k}'`, sid, `use only: ${Object.keys(props).filter((p) => !p.startsWith("@")).join(", ")}`);
      else out[k] = x;
    }
    if (!opts.partial) for (const r of schema.required || []) if (!(r in v)) err(errs, "required", `${path}/${r}`, `${r} is required`, sid);
    tableHeaders(v, path, errs, sid);
    if (schema["x-od-effect"] === "change" && isObj(v.event) && isObj(v.event.context) && "approved" in v.event.context)
      err(errs, "R3-approval", `${path}/event/context/approved`, "an action that changes data is approved by the person, never in the answer", sid, "remove approved");
    return out;
  }
  return v;
}

export function numbersIn(obj, out = new Set()) {
  if (typeof obj === "boolean" || obj === null || obj === undefined) return out;
  if (typeof obj === "number") out.add(obj);
  else if (typeof obj === "string") for (const n of obj.match(NUM) || []) { const x = num(n); if (x !== null) out.add(x); }
  else if (Array.isArray(obj)) obj.forEach((x) => numbersIn(x, out));
  else if (isObj(obj)) Object.values(obj).forEach((x) => numbersIn(x, out));
  return out;
}

/** The short form a model writes (one part, or a list of parts) wrapped in the A2UI envelope. Same as wrap() in smartui.py. */
export function wrap(components, surface = "s1") {
  let comps = Array.isArray(components) ? components : [components];
  if (comps.length === 1 && isObj(comps[0]) && !("id" in comps[0])) comps = [{ ...comps[0], id: "root" }];
  return [{ version: A2UI_VERSION, createSurface: { surfaceId: surface, components: comps } }];
}

export function normalize(answer) {
  if (isObj(answer) && "messages" in answer) answer = answer.messages;
  if (isObj(answer) && "component" in answer) return wrap(answer);
  if (Array.isArray(answer) && answer.length && answer.every((x) => isObj(x) && "component" in x)) return wrap(answer);
  if (isObj(answer)) answer = [answer];
  return Array.isArray(answer) ? answer : null;
}

function accessibleNames(comp, schema, out, base) {
  const walk = (v, s, path, itemName) => {
    if (!s || s.$ref) return;
    if (isObj(v) && s.type === "object") {
      for (const [k, x] of Object.entries(v)) {
        const ps = (s.properties || {})[k];
        if (!ps) continue;
        if (ps["x-od-effect"] !== undefined && isObj(x)) {
          const name = x.a11y_label || ((x.label || "") + (itemName ? `, ${itemName}` : ""));
          out.push([name.trim().toLowerCase(), `${path}/${k}`]);
        } else walk(x, ps, `${path}/${k}`, itemName);
      }
    } else if (Array.isArray(v) && s.type === "array") {
      const it = s.items || {}, nf = it["x-od-name-from"];
      v.forEach((x, i) => walk(x, it, `${path}/${i}`, isObj(x) && nf && typeof x[nf] === "string" ? x[nf] : itemName));
    }
  };
  walk(comp, schema, base, null);
}

function structure(sid, s, cat, opts, errs) {
  const comps = s.components, ids = Object.keys(comps);
  const limits = { ...(od(cat).limits || LIMITS) };
  for (const [k, v] of Object.entries(opts.limits || {})) if (v) limits[k] = v;
  if (!ids.length) return;
  if (ids.length > limits.components) err(errs, "R2-size", "", `${ids.length} components on one surface; the most is ${limits.components}`, sid);
  if (!("root" in comps)) { if (!opts.partial) err(errs, "root", "", 'one component needs id "root"', sid); return; }
  const seen = new Set(), leaves = [];
  const walk = (cid, depth, trail) => {
    if (trail.has(cid)) { errs.push({ code: "INTEGRITY_ERROR", rule: "cycle", path: comps[cid].path, message: `${cid} contains itself`, surfaceId: sid }); return; }
    if (!(cid in comps)) { if (!opts.partial) err(errs, "children", "", `child '${cid}' does not exist`, sid); return; }
    seen.add(cid);
    if (depth > limits.depth) { err(errs, "depth", comps[cid].path, `nested ${depth} deep; the most is ${limits.depth}`, sid); return; }
    const c = comps[cid].c;
    if (od(comps[cid].schema).container) {
      for (const ch of Array.isArray(c.children) ? c.children : []) walk(ch, depth + 1, new Set([...trail, cid]));
    } else leaves.push(cid);
  };
  walk("root", 1, new Set());
  for (const [cid, v] of Object.entries(comps)) if (!seen.has(cid) && !opts.partial) err(errs, "orphan", v.path, `${cid} is not reached from root`, sid, "add it to a Column's children or remove it");
  if (leaves.length > limits.leaves) err(errs, "R2-one", "", `${leaves.length} parts in one answer; show one unless the person asked for more`, sid, "keep the one that answers the question");
  const names = [];
  for (const cid of leaves) accessibleNames(comps[cid].c, comps[cid].schema, names, comps[cid].path);
  const count = new Map();
  for (const [n, p] of names) { if (!count.has(n)) count.set(n, []); count.get(n).push(p); }
  for (const [n, ps] of count) {
    if (!n) err(errs, "R5-name", ps[0], "an action has no name", sid, "give it a label");
    else if (ps.length > 1) err(errs, "R5-repeat", ps[1], `${ps.length} actions are all called '${n}'`, sid, 'give each a11y_label that says which one, for example "Book the 08:40 flight"');
  }
}

/** Validate one answer (a list of A2UI v1.0 messages) against a catalog. opts: {partial, source, limits}. */
export function validate(answer, cat, opts = {}) {
  const errs = [], warns = [], surfaces = {};
  const msgs = normalize(answer);
  if (!msgs) { err(errs, "shape", "", "an answer is a list of A2UI messages", ""); return { ok: false, errors: errs, warnings: warns, surfaces: {} }; }
  const numbers = opts.source !== undefined && opts.source !== null ? numbersIn(opts.source) : null;
  const names = opts.copy ? namesIn(opts.source) : new Set();
  const KINDS = ["createSurface", "updateComponents", "updateDataModel", "deleteSurface"];
  msgs.forEach((m, i) => {
    const base = `/${i}`;
    if (!isObj(m)) { err(errs, "shape", base, "each message is an object", ""); return; }
    if (m.version !== A2UI_VERSION) err(errs, "version", `${base}/version`, `version must be "${A2UI_VERSION}"`, "", 'add "version": "1.0"');
    const kinds = KINDS.filter((k) => k in m), extra = Object.keys(m).filter((k) => k !== "version" && !KINDS.includes(k));
    if (kinds.length !== 1 || extra.length) { err(errs, "shape", base, "each message has exactly one of createSurface, updateComponents, updateDataModel, deleteSurface", ""); return; }
    const kind = kinds[0], body = m[kind], sid = isObj(body) ? body.surfaceId : null;
    if (typeof sid !== "string" || !sid) { err(errs, "shape", `${base}/${kind}/surfaceId`, "surfaceId is required", ""); return; }
    let comps;
    if (kind === "createSurface") {
      if (sid in surfaces) errs.push({ code: "INTEGRITY_ERROR", rule: "integrity", path: `${base}/${kind}/surfaceId`, message: `surface ${sid} already exists`, surfaceId: sid });
      if ("theme" in body) err(errs, "R4-key", `${base}/${kind}/theme`, "A2UI v1.0 has no theme; the system's tokens style the surface", sid, "remove theme");
      if (body.catalogId !== undefined && body.catalogId !== null && body.catalogId !== cat.catalogId) err(errs, "catalog", `${base}/${kind}/catalogId`, `this renderer supports only ${cat.catalogId}`, sid);
      for (const k of Object.keys(body)) if (!["surfaceId", "catalogId", "components", "dataModel", "sendDataModel", "metadata", "theme"].includes(k)) err(errs, "unknown-property", `${base}/${kind}/${k}`, `unknown key '${k}'`, sid);
      surfaces[sid] = { components: {}, data: isObj(body.dataModel) ? body.dataModel : {} };
      comps = body.components || [];
    } else if (!(sid in surfaces)) {
      errs.push({ code: "INTEGRITY_ERROR", rule: "integrity", path: `${base}/${kind}/surfaceId`, message: `no surface ${sid}; createSurface comes first`, surfaceId: sid }); return;
    } else if (kind === "updateComponents") comps = body.components || [];
    else if (kind === "updateDataModel") {
      const path = body.path ?? "/", val = body.value;
      if (path === "/" || path === "") surfaces[sid].data = isObj(val) ? val : {};
      else {
        let cur = surfaces[sid].data;
        const parts = path.split("/").slice(1).map((p) => p.replace(/~1/g, "/").replace(/~0/g, "~"));
        for (const p of parts.slice(0, -1)) cur = isObj(cur) ? (cur[p] = isObj(cur[p]) ? cur[p] : (cur[p] ?? {})) : {};
        if (isObj(cur)) { if (val === null || val === undefined) delete cur[parts.at(-1)]; else cur[parts.at(-1)] = val; }
      }
      return;
    } else { delete surfaces[sid]; return; }
    if (!Array.isArray(comps)) { err(errs, "shape", `${base}/${kind}/components`, "components is a list", sid); return; }
    comps.forEach((c, j) => {
      const cpath = `${base}/${kind}/components/${j}`;
      if (!isObj(c)) { err(errs, "shape", cpath, "a component is an object", sid); return; }
      const schema = cat.components[c.component];
      if (!schema) { err(errs, "unknown-component", `${cpath}/component`, `unknown component '${c.component}'`, sid, "use one of: " + Object.keys(cat.components).join(", ")); return; }
      const ctx = { data: surfaces[sid].data, numbers, warnings: warns, names };
      const checked = checkValue(c, schema, cpath, errs, sid, cat, opts, ctx);
      if (typeof c.id === "string") surfaces[sid].components[c.id] = { c: isObj(checked) ? checked : c, path: cpath, schema };
    });
  });
  for (const [sid, s] of Object.entries(surfaces)) structure(sid, s, cat, opts, errs);
  const out = {};
  for (const [sid, s] of Object.entries(surfaces)) out[sid] = { data: s.data, components: Object.fromEntries(Object.entries(s.components).map(([k, v]) => [k, v.c])) };
  return { ok: !errs.length, errors: errs, warnings: warns, surfaces: out };
}

/** The A2UI messages in a model's reply: a fenced a2ui block, or JSON on its own; null for a text-only answer. */
export function extractAnswer(text) {
  const m = /```a2ui\s*([\s\S]*?)```/.exec(text);
  let body = m ? m[1] : text.trim();
  if (!m && !/^[[{]/.test(body)) return null;
  try { return JSON.parse(body); } catch (e) { return { __parse_error__: String(e.message || e) }; }
}

/** Plain text for a host that renders no UI. The same walk as to_text in smartui.py. */
export function toText(surfaces, cat) {
  const out = [];
  const val = (v, s, indent) => {
    s = s || {};
    if (isObj(v)) {
      if ("label" in v && "event" in v) return [];
      if ("src" in v && "alt" in v) return [indent + `[Image: ${v.alt}]`];
      const parts = [], nested = [];
      for (const [k, x] of Object.entries(v)) {
        if (k.startsWith("@") || ["component", "id", "children"].includes(k)) continue;
        const ps = (s.properties || {})[k] || {};
        if ((typeof x === "string" || typeof x === "number") && !ps["x-od-token"] && !ps.enum) parts.push(String(x));
        else if (Array.isArray(x) || isObj(x)) nested.push(...val(x, ps, indent + (parts.length ? "  " : "")));
      }
      return (parts.length ? [indent + parts.join(" · ")] : []).concat(nested);
    }
    if (Array.isArray(v)) {
      const lines = [];
      for (const x of v) {
        const sub = val(x, s.items || {}, "");
        if (sub.length) { lines.push(indent + "- " + sub[0].trim()); for (const y of sub.slice(1)) lines.push(indent + "  " + y.trim()); }
      }
      return lines;
    }
    return [indent + String(v)];
  };
  for (const s of Object.values(surfaces)) {
    const walk = (cid) => {
      const c = s.components[cid];
      if (!c) return;
      const schema = cat.components[c.component] || {};
      if (od(schema).container) (c.children || []).forEach(walk);
      else { out.push(...val(c, schema, "")); out.push(""); }
    };
    walk("root");
  }
  return out.join("\n").trim() + "\n";
}

const api = { od, wrap, validate, extractAnswer, toText, numbersIn, normalize, hostAllowed, A2UI_VERSION };
if (typeof globalThis !== "undefined") globalThis.ODSmartUI = Object.assign(globalThis.ODSmartUI || {}, api);
export default api;
