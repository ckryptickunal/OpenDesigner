#!/usr/bin/env python3
"""Check the built site's layout in a real browser, at every width from a small phone to a wide desktop: page overflow,
unintended scroll or clipping inside figures and cards, stacked groups that are not centred on one axis, overlapping boxes,
ragged left edges in one-column stacks, small tap targets and text that runs over an edge.

  python3 site/check_layout.py                         every page in site/dist/sitemap.xml at 13 widths
  python3 site/check_layout.py --pages /,/docs/        only these pages
  python3 site/check_layout.py --widths 600,768,900    only these widths
  python3 site/check_layout.py --base http://localhost:4173 --shots site/.cache/layout --errors-only

Serve site/dist first (the opendesigner-site config in .claude/launch.json serves it at http://localhost:4173/).
Needs Playwright and the installed Chrome. Each error gets a cropped screenshot, outlined in red, in --shots.
Exits 1 when it finds an error. Warnings (truncated text, partial gallery rows, small targets) are reported but do not fail.
"""
import argparse
import html
import json
import pathlib
import re
import sys

from playwright.sync_api import sync_playwright

SITE = pathlib.Path(__file__).resolve().parent
_url = SITE / "site-url.txt"
SITE_URL = (_url.read_text().strip() if _url.exists() else "https://opendesigner.dev").rstrip("/")
WIDTHS = [320, 360, 390, 430, 600, 768, 820, 900, 1024, 1180, 1280, 1440, 1920]
MAX_HEIGHT = 16000  # the viewport grows to the page's height, up to this

# Card-like boxes. Besides these, any element with a border and a radius that is a direct child of a flex or grid container
# counts, unless it is a control or a label (NOT_CARDS), inline, or smaller than 64 x 48 px.
CARDS = [".fig-card", ".h-step", ".bento-card", ".who-card", ".demo-panel", ".start", ".ex", ".dodont > div", ".opt", ".role",
         ".ghcard", ".x-card"]
NOT_CARDS = ["a.btn", "button", "[role=tab]", "input", "select", "textarea", ".chip", ".sticker", ".copy", ".filter", ".cmd",
             ".ui-btn", ".ui-input", ".x-btn", ".x-input", ".hh-btn", ".tag-missing", ".swatch"]  # controls, also when drawn in figures
PANELS = [".fig", ".fig-panel", ".fig-scene", ".demo-stage", ".h-end-photo", ".h-end-card", ".starts", ".tree"]  # check 2 looks inside these too
GALLERIES = [".pieces", ".ex-grid", ".bento"]  # named in a partly filled last row warning
SCROLL_OK = [".prose .code pre", ".prose .table-wrap", ".sl-track", ".filters"]  # may scroll sideways on purpose (a carousel; tag filters on phones)
STUCK_OK = [".sticker", ".piece-stuck", ".a-stamp", ".a-rstamp"]  # sit on corners on purpose: never an overlap
MARKS_OK = [".a-call", ".a-dim", ".a-crop", ".a-reg", ".a-stamp"]  # proof marks drawn outside a box on purpose: their text may pass its edge
# Scaled previews (the component library): a live component laid out at its design width and zoomed down to a card, an aisle
# tile or a device frame. Zoom makes their boxes unmeasurable here, and an aisle tile crops on purpose. They are checked
# unscaled instead, one component per page at every width (skills/opendesigner/scripts/library.py check, site/library_layout.py).
PREVIEWS = [".lib-fit", ".part-frame", ".aisle-prev"]
# Illustrations of a mistake on purpose: the "Don't" side of a do and don't figure shows drifting corners. Check 14 skips them.
NESTED_OK = [".dont"]

HINTS = {
    "page-overflow": "something is wider than the screen: let it wrap or shrink (max-width: 100%, min-width: 0), or scroll it in its own box",
    "inner-scroll": "the content is wider than its box at this width: let it wrap (white-space: pre-wrap, overflow-wrap: anywhere), make it smaller, or give the box room",
    "clipped": "overflow: hidden cuts the content off: let it wrap or shrink, or give the box room",
    "ellipsis": "text is cut with an ellipsis: check the full text is not needed here, or give it room",
    "symmetry": "the rows are not centred on one axis: centre the narrower row (margin-inline: auto, justify-content: center) or give the rows one width",
    "row-overflow": "a row is wider than its container: let it wrap or shrink (minmax(0, 1fr), min-width: 0)",
    "partial-row": "the last row is partly filled: centre it, stretch it, or change the count (decide which)",
    "overlap": "two boxes overlap: look for negative margins, absolute positions or fixed widths",
    "edge": "boxes of one kind in one column do not share a left edge: give them one width, or one alignment",
    "target": "smaller than 24 x 24 px (WCAG 2.5.8): add padding or min-height, or keep 24 px clear around it",
    "text-edge": "text runs past the edge: let it wrap (overflow-wrap: anywhere, min-width: 0 on its flex or grid item) or shorten it",
    "anchor": "a control pinned inside a box should sit on the content's first line (same centre) with equal top and side insets: reserve room beside the text, never an empty band above it",
    "under-control": "text runs under a pinned control: make room beside the control (padding) and let the text wrap instead of scrolling",
    "label-break": "a label, chip or tag broke across lines (sometimes inside a word): keep it on one line (white-space: nowrap) and let its row wrap instead",
    "actions": "opposite actions belong on one row, the secondary on the left and the primary on the right, as far apart as the row allows",
    "text-left": "text blocks that sit one under another should start on one left edge: look for an auto or leftover margin, or an indent",
    "nested-radius": "a rounded box close inside a rounded box: its radius should be the outer radius minus the gap between them, so the curves run parallel (set it with calc(outer - gap), and resolve the outer value on the outer element)",
    "preview-crop": "a library preview crops its part: scale the whole part to fit its frame with its proportions kept (site/static/library.js fitCard and fitDevice), and make sure the card is fitted once it comes near the screen",
    "widow": "the last line holds a single word: balance the text (text-wrap: balance for headings and short centred lines, pretty for paragraphs), or reword",
}

MEASURE = r"""(cfg) => {
  const out = [], vw = document.documentElement.clientWidth, sx = scrollX, sy = scrollY;
  const R = el => el.getBoundingClientRect();
  const css = new Map(), cs = el => { if (!css.has(el)) css.set(el, getComputedStyle(el)); return css.get(el); };
  const rect = r => [Math.round(r.left + sx), Math.round(r.top + sy), Math.round(r.width), Math.round(r.height)];
  const px = v => Math.round(v * 10) / 10;
  const seen = el => !el.closest(any(cfg.previews)) && el.checkVisibility({ visibilityProperty: true, opacityProperty: true }) && R(el).width > 0 && R(el).height > 0;
  const name = el => {
    let s = el.tagName.toLowerCase();
    if (el.id) return s + "#" + el.id;
    const cl = [...el.classList].slice(0, 2);
    if (cl.length) s += "." + cl.join(".");
    const sib = el.parentElement ? [...el.parentElement.children].filter(c => c.tagName === el.tagName) : [];
    if (sib.length > 1 && (!cl.length || sib.filter(c => c.classList.contains(cl[0])).length > 1)) s += `:nth-of-type(${sib.indexOf(el) + 1})`;
    return s;
  };
  const path = el => { const p = []; for (let e = el; e && e !== document.body && p.length < 5; e = e.parentElement) { p.unshift(name(e)); if (e.id) break; } return p.join(" > "); };
  const fig = el => { const f = el.closest("figure.fig"), c = f && f.querySelector(":scope > figcaption"); return c ? c.textContent.replace(/\s+/g, " ").trim().slice(0, 48) : ""; };
  const add = (check, level, el, msg, rects) => out.push({ check, level, sel: path(el), fig: fig(el), msg, rects: rects.map(rect) });
  const any = list => list.join(",");

  const all = [...document.body.querySelectorAll("*")].filter(e => !e.closest("svg, script, style, noscript, template") && seen(e));
  const isCard = el => {
    if (el.matches(any(cfg.cards))) return true;
    if (el.matches(any(cfg.notCards)) || !el.parentElement) return false;
    const s = cs(el);
    if (s.display.startsWith("inline") || s.display === "contents" || !/flex|grid/.test(cs(el.parentElement).display)) return false;
    const border = ["Top", "Right", "Bottom", "Left"].some(k => parseFloat(s["border" + k + "Width"]) > 0);
    const r = R(el);
    return border && parseFloat(s.borderTopLeftRadius) > 0 && r.width >= 64 && r.height >= 48;
  };
  const cards = all.filter(isCard), cardSet = new Set(cards);
  const kind = el => cfg.cards.find(s => el.matches(s)) || el.tagName.toLowerCase() + (el.classList[0] ? "." + el.classList[0] : "");
  const scopeSel = any([...cfg.cards, ...cfg.panels]);
  const inScope = el => { if (el.closest(scopeSel)) return true; for (let e = el; e; e = e.parentElement) if (cardSet.has(e)) return true; return false; };
  const clips = el => cs(el).overflowX !== "visible" || cs(el).overflowY !== "visible";
  const scrolls = el => /auto|scroll/.test(cs(el).overflowX);
  const range = document.createRange();
  // a text node's ink: the union of its words, without the spaces that hang at line ends in pre-wrap text
  const ink = (n, r) => {
    const re = /\S+/g; let m, u = null;
    while ((m = re.exec(n.textContent))) {
      range.setStart(n, m.index); range.setEnd(n, m.index + m[0].length);
      for (const q of range.getClientRects()) if (q.width >= 0.5)
        u = u ? { left: Math.min(u.left, q.left), top: Math.min(u.top, q.top), right: Math.max(u.right, q.right), bottom: Math.max(u.bottom, q.bottom) } : { left: q.left, top: q.top, right: q.right, bottom: q.bottom };
    }
    return u ? { ...u, width: u.right - u.left, height: u.bottom - u.top } : r;
  };
  // how far real content (elements and text, not the empty line box under an inline svg) reaches past el's padding box
  const spill = el => {
    const b = R(el), L = b.left + el.clientLeft, T = b.top + el.clientTop, x = { r: 0, b: 0, l: 0, t: 0 };
    const visit = n => { for (const c of n.childNodes) {
      let r;
      if (c.nodeType === 3) {
        if (!c.textContent.trim()) continue;
        range.selectNodeContents(c); r = range.getBoundingClientRect();
        if (r.right > L + el.clientWidth + 1 || r.left < L - 1 || r.bottom > T + el.clientHeight + 1 || r.top < T - 1) r = ink(c, r);
      }
      else if (c.nodeType === 1 && c.checkVisibility() && cs(c).position !== "fixed") { r = R(c); if (!/^(svg|img|video|canvas|iframe)$/i.test(c.tagName) && !clips(c)) visit(c); }
      else continue;
      if (r.width < 1 && r.height < 1) continue;
      x.r = Math.max(x.r, r.right - L - el.clientWidth); x.b = Math.max(x.b, r.bottom - T - el.clientHeight);
      x.l = Math.max(x.l, L - r.left); x.t = Math.max(x.t, T - r.top);
    } };
    visit(el);
    return x;
  };

  // 1. the page scrolls sideways
  const de = document.documentElement;
  if (de.scrollWidth > de.clientWidth) {
    const free = el => { for (let e = el.parentElement; e && e !== document.body; e = e.parentElement) if (cs(e).overflowX !== "visible") return false; return true; };
    // an outer <svg> is a box like any other here (the shared element list leaves svg out, so check 1 adds it back by itself)
    const svgs = [...document.body.querySelectorAll("svg")].filter(e => !(e.parentElement && e.parentElement.closest("svg")) && seen(e));
    const offs = [...all, ...svgs].filter(e => (R(e).right > vw + 1 || R(e).left < -1) && free(e)), set = new Set(offs);
    const top = offs.filter(e => !set.has(e.parentElement)).sort((a, b) => R(b).right - R(a).right).slice(0, 3);
    add("page-overflow", "error", top[0] || de, `the page is ${de.scrollWidth} px wide in a ${de.clientWidth} px window; widest: ` +
      (top.map(e => `${path(e)} (right edge ${px(R(e).right)} px)`).join("; ") || "unknown"), top.map(R));
  }

  // text for screen readers only sits in a 1 x 1 px box that hides its overflow on purpose (.visually-hidden); it is never clipped
  // content and never runs past an edge (checker evals, 2026-10-20)
  const srOnly = el => { for (let e = el; e && e !== document.body; e = e.parentElement) { const b = R(e); if (b.width <= 1 && b.height <= 1 && /hidden|clip/.test(cs(e).overflow)) return true; } return false; };
  // 2. scroll or clipping inside a figure, card or panel; ellipsis is a warning
  for (const el of all) {
    const s = cs(el);
    if (srOnly(el) || s.display === "inline" || /^(IMG|VIDEO|IFRAME|CANVAS|INPUT|TEXTAREA|SELECT|svg)$/.test(el.tagName) || !inScope(el) || el.matches(any(cfg.scrollOk))) continue;
    const ox = s.overflowX, oy = s.overflowY;
    if (ox === "visible" && oy === "visible") continue;
    if (s.textOverflow === "ellipsis" && el.scrollWidth > el.clientWidth + 1) {
      add("ellipsis", "warning", el, `text cut with an ellipsis: "${el.textContent.trim().slice(0, 40)}" needs ${el.scrollWidth} px, has ${el.clientWidth} px`, [R(el)]);
      continue;
    }
    if (/auto|scroll/.test(ox) && el.scrollWidth > el.clientWidth + 1)
      add("inner-scroll", "error", el, `content is ${el.scrollWidth} px wide in a ${el.clientWidth} px box (${el.scrollWidth - el.clientWidth} px over, overflow-x: ${ox}), so it scrolls sideways`, [R(el)]);
    if (/auto|scroll/.test(oy) && el.scrollHeight > el.clientHeight + 1)
      add("inner-scroll", "error", el, `content is ${el.scrollHeight} px tall in a ${el.clientHeight} px box (overflow-y: ${oy}), so it scrolls`, [R(el)]);
    if (/hidden|clip/.test(ox + oy)) {
      const x = spill(el), cut = [];
      if (/hidden|clip/.test(ox)) { if (x.r > 1) cut.push(`${px(x.r)} px on the right`); if (x.l > 1) cut.push(`${px(x.l)} px on the left`); }
      if (/hidden|clip/.test(oy)) { if (x.b > 1) cut.push(`${px(x.b)} px at the bottom`); if (x.t > 1) cut.push(`${px(x.t)} px at the top`); }
      if (cut.length) add("clipped", "error", el, `overflow: ${ox === oy ? ox : ox + " " + oy} cuts off content: ${cut.join(", ")} (box ${el.clientWidth} × ${el.clientHeight} px)`, [R(el)]);
    }
  }

  // 3 and 5. stacked groups: rows centred on one axis; one-column stacks share a left edge
  const groups = new Map();
  for (const c of all) {
    const kids = [...c.children].filter(k => seen(k));
    if (!kids.some(k => cardSet.has(k))) continue;
    // in a flex or grid container, a direct card plus a wrapper of cards (the hero: a big card over a pair) form one group
    const flexy = /flex|grid/.test(cs(c).display);
    const items = kids.flatMap(k => cardSet.has(k) ? [k] : !flexy || cs(k).display.startsWith("inline") ? [] : [...k.children].filter(g => cardSet.has(g)));
    if (items.length < 2) continue;
    const key = items.map(i => all.indexOf(i)).join(",");
    if (!groups.has(key)) groups.set(key, [c, items]);
  }
  for (const [c, items] of groups.values()) {
    const rows = [];
    for (const it of [...items].sort((a, b) => R(a).top - R(b).top)) {
      const r = R(it), row = rows.find(w => r.top < w.bottom - 1 && r.bottom > w.top + 1);
      if (row) { row.items.push(it); row.bottom = Math.max(row.bottom, r.bottom); row.top = Math.min(row.top, r.top); }
      else rows.push({ items: [it], top: r.top, bottom: r.bottom });
    }
    const s = cs(c), cr = R(c), inL = cr.left + parseFloat(s.borderLeftWidth) + parseFloat(s.paddingLeft), inR = cr.right - parseFloat(s.borderRightWidth) - parseFloat(s.paddingRight);
    for (const w of rows) { w.l = Math.min(...w.items.map(i => R(i).left)); w.r = Math.max(...w.items.map(i => R(i).right)); w.c = (w.l + w.r) / 2; }
    const wide = rows.filter(w => w.l < inL - 1 || w.r > inR + 1);
    if (wide.length && !scrolls(c))
      add("row-overflow", "error", c, `${wide.length} of ${rows.length} rows reach ${px(Math.min(...wide.map(w => w.l)))}–${px(Math.max(...wide.map(w => w.r)))} px, ` +
        `outside the container's ${px(inL)}–${px(inR)} px`, [cr, ...wide.flatMap(w => w.items.map(R))]);
    if (rows.length < 2) continue;
    const ref = rows[0], gallery = c.matches(any(cfg.galleries)), column = rows.every(w => w.items.length === 1);
    const ragged = column && items.some(i => kind(i) === kind(items[0]) && Math.abs(R(i).left - R(items[0]).left) > 1);
    rows.slice(1).forEach((w, n) => {
      if (ragged) return;  // a one-column stack with ragged edges is reported once, as an edge finding
      const off = w.c - ref.c;
      if (Math.abs(off) <= 2) return;
      const last = n === rows.length - 2, partial = last && w.r - w.l < ref.r - ref.l - 1 && Math.abs(w.l - ref.l) <= 1;
      const msg = `row ${n + 2} (${w.items.length} box${w.items.length > 1 ? "es" : ""}, ${px(w.l)}–${px(w.r)} px) is centred at ${px(w.c)} px; ` +
        `row 1 (${ref.items.length}, ${px(ref.l)}–${px(ref.r)} px) at ${px(ref.c)} px: ${px(Math.abs(off))} px ${off < 0 ? "left" : "right"}`;
      if (partial) add("partial-row", "warning", c, msg + (gallery ? " (a gallery)" : ""), [cr, ...w.items.map(R)]);
      else add("symmetry", "error", c, msg, [...ref.items.map(R), ...w.items.map(R)]);
    });
    if (column) {
      const byKind = new Map();
      items.forEach(i => byKind.set(kind(i), [...(byKind.get(kind(i)) || []), i]));
      for (const [k, list] of byKind) {
        const bad = list.filter(i => Math.abs(R(i).left - R(list[0]).left) > 1);
        if (list.length > 1 && bad.length)
          add("edge", "error", c, `${list.length} ${k} boxes stacked in one column: left edges at ${list.map(i => px(R(i).left)).join(", ")} px`, list.map(R));
      }
    }
  }

  // 4. card-like boxes that overlap
  const stuck = any(cfg.stuckOk), pool = cards.filter(e => !e.closest(stuck));
  for (let i = 0; i < pool.length; i++) for (let j = i + 1; j < pool.length; j++) {
    const a = pool[i], b = pool[j];
    if (a.contains(b) || b.contains(a)) continue;
    const ra = R(a), rb = R(b), w = Math.min(ra.right, rb.right) - Math.max(ra.left, rb.left), h = Math.min(ra.bottom, rb.bottom) - Math.max(ra.top, rb.top);
    if (w > 2 && h > 2) add("overlap", "error", a, `overlaps ${path(b)} by ${px(w)} × ${px(h)} px`, [ra, rb]);
  }

  // 6. tap targets under 24 x 24 px that are not links in a sentence and have no 24 px of clear space (WCAG 2.5.8)
  const targets = [...document.querySelectorAll("a[href], button, [role=button], [role=tab], input:not([type=hidden]), select, textarea, summary")]
    .filter(t => seen(t) && R(t).right > 0 && R(t).left < vw);
  const small = t => R(t).width < 24 || R(t).height < 24;
  const inSentence = t => t.tagName === "A" && cs(t).display === "inline" && t.parentElement && t.parentElement.textContent.trim().length > t.textContent.trim().length + 2;
  const centre = r => [(r.left + r.right) / 2, (r.top + r.bottom) / 2];
  for (const t of targets) {
    if (!small(t) || inSentence(t)) continue;
    const r = R(t), [x, y] = centre(r);
    const crowd = targets.find(o => {
      if (o === t || o.contains(t) || t.contains(o)) return false;
      const q = R(o), dx = Math.max(q.left - x, 0, x - q.right), dy = Math.max(q.top - y, 0, y - q.bottom);
      if (Math.hypot(dx, dy) < 12) return true;
      const [ox, oy] = centre(q);
      return small(o) && Math.hypot(ox - x, oy - y) < 24;
    });
    if (crowd) add("target", "warning", t, `"${(t.textContent.trim() || t.getAttribute("aria-label") || "").slice(0, 30)}" is ${px(r.width)} × ${px(r.height)} px, and ${path(crowd)} is within its 24 px circle`, [r]);
  }

  // 7. text past the window or past its card
  const walk = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT), done = new Set();
  for (let n = walk.nextNode(); n; n = walk.nextNode()) {
    const el = n.parentElement;
    if (!n.textContent.trim() || !el || el.closest("svg, script, style, noscript, template") || el.closest(any(cfg.marksOk)) || !seen(el) || srOnly(el)) continue;
    range.selectNodeContents(n);
    let r = range.getBoundingClientRect();
    if (r.width < 1 || r.right <= 0 || r.left >= vw) continue;  // empty, or parked off screen on purpose (the skip link)
    let card = null, sc = false, cut = false;
    for (let e = el; e && e !== document.body; e = e.parentElement) {
      if (cardSet.has(e) || e.matches(any(cfg.cards))) { card = e; break; }
      if (scrolls(e)) sc = true;
      if (clips(e)) cut = true;
    }
    if (sc) continue;  // scrolled content belongs to check 2
    const c = card && R(card);
    if (r.right > vw + 1 || r.left < -1 || (c && (r.right > c.right + 1 || r.left < c.left - 1))) r = ink(n, r);
    const word = `"${n.textContent.trim().slice(0, 40)}"`;
    const owner = card || el.closest(any(cfg.panels)) || el.parentElement;  // one finding per card or panel: the first text that crosses it
    if (done.has(owner)) continue;
    if (r.right > vw + 1 || r.left < -1) { done.add(owner); add("text-edge", "error", el, `${word} spans ${px(r.left)}–${px(r.right)} px in a ${vw} px window`, [r]); continue; }
    if (card && !cut && !clips(card)) {
      if (r.right > c.right + 1 || r.left < c.left - 1) { done.add(owner); add("text-edge", "error", el, `${word} spans ${px(r.left)}–${px(r.right)} px, past its card's ${px(c.left)}–${px(c.right)} px`, [c, r]); }
    }
  }
  // 8. controls pinned inside a box (a copy button in a code block): centred on the content's first line, with equal insets.
  //    Owner, 2026-10-15: the Copy button floated in a 48 px band above the code ("feels out of place").
  for (const el of document.querySelectorAll("button, a.btn, .copy, [role=button]")) {
    if (cs(el).position !== "absolute" || !el.offsetParent || el.closest("dialog:not([open])") || el.closest(any(cfg.previews))) continue;  // a scaled preview is checked unscaled by library_layout.py
    const r = R(el); if (!r.width || !r.height) continue;
    const box = el.offsetParent, b = R(box);
    // text for screen readers only (a carousel's "Frame 1 of 3") is not a line the eye lines a control up with
    const tw = document.createTreeWalker(box, NodeFilter.SHOW_TEXT, { acceptNode: n => (!el.contains(n) && n.textContent.trim() && R(n.parentElement).width > 1) ? 1 : 3 });
    const t = tw.nextNode(); if (!t) continue;
    const rg = document.createRange(), i = t.textContent.search(/\S/); rg.setStart(t, i); rg.setEnd(t, i + 1);
    const line = rg.getBoundingClientRect(); if (!line.height) continue;
    const content = t.parentElement.closest("pre, p, li, div") || box, lh = parseFloat(cs(content).lineHeight) || line.height;
    const lineMid = line.top + line.height / 2, mid = r.top + r.height / 2;
    if (Math.abs(mid - lineMid) > Math.max(3, (lh - line.height) / 2 + 2)) {
      add("anchor", "error", el, `centre ${px(mid - b.top)} px from the box's top, but the first line's centre is ${px(lineMid - b.top)} px`, [b, r, line]);
      continue;
    }
    const top = r.top - b.top, side = Math.min(r.left - b.left, b.right - r.right);
    if (Math.abs(top - side) > 2) add("anchor", "warning", el, `insets differ: ${px(top)} px from the top, ${px(side)} px from the side`, [b, r]);
  }
  // 9. widows: a heading, lede or card text whose last line is one word (owner, 2026-10-15: "it." alone on the closing card's last line)
  for (const el of document.querySelectorAll("h1, h2, h3, .lede, .h-lede, .h-end-lede, .h-cmd-label, .h-step > p, .bento-card > p, .who-card > p, .craft-card > p, figure > figcaption:not(:has(.a-tags))")) {
    if (!seen(el) || el.closest(any(cfg.marksOk))) continue;
    const words = [], tw = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
    for (let n = tw.nextNode(); n; n = tw.nextNode()) {
      if (n.parentElement.closest("svg, .sr-only, [hidden]")) continue;
      for (const m of n.textContent.matchAll(/\S+/g)) {
        const rg = document.createRange(); rg.setStart(n, m.index); rg.setEnd(n, m.index + m[0].length);
        const rs = rg.getClientRects(), rr = rs[rs.length - 1]; if (rr && rr.width) words.push([Math.round(rr.top), Math.round(rr.bottom)]);  // a word belongs to the line it ends on
      }
    }
    if (words.length < 4) continue;
    const lines = []; for (const [t, b] of words) { const l = lines.find(x => Math.abs(x.t - t) < (b - t) / 2); if (l) l.n++; else lines.push({ t, n: 1 }); }
    if (lines.length < 2) continue;
    lines.sort((a, b) => a.t - b.t);
    const last = lines[lines.length - 1];
    if (last.n === 1) add("widow", /^H[1-3]$/.test(el.tagName) || el.matches(".lede, .h-lede, .h-end-lede") ? "error" : "warning", el, `${lines.length} lines, and the last holds one word`, [R(el)]);
  }
  // 10. stacked text blocks share a left edge: a heading, its lede and the next paragraph start at the same x
  //     (owner-caught class of bug, 2026-10-15: a section lede 64 px right of its heading, from a centred margin leaking in)
  for (const box of document.querySelectorAll("main *")) {
    const kids = [...box.children].filter(k => /^(P|H1|H2|H3|H4)$/.test(k.tagName) && seen(k) && cs(k).display === "block" && cs(k).position === "static"
                                         && /^(left|start)$/.test(cs(k).textAlign) && !k.closest(any(cfg.marksOk)) && !k.classList.contains("kicker") && k.textContent.trim());
    if (kids.length < 2) continue;
    const lefts = kids.map(k => R(k).left);
    if (Math.max(...lefts) - Math.min(...lefts) > 1) add("text-left", "error", box, `text blocks start at ${lefts.map(px).join(", ")} px`, kids.map(R));
  }
  // 11. no text under a pinned control (owner, 2026-10-15: long commands scrolled under the Copy button on a phone)
  for (const el of document.querySelectorAll("button, a.btn, .copy, [role=button]")) {
    if (cs(el).position !== "absolute" || !el.offsetParent || el.closest("dialog:not([open])") || el.closest(any(cfg.previews))) continue;  // a scaled preview is checked unscaled by library_layout.py
    const r = R(el); if (!r.width) continue;
    const tw = document.createTreeWalker(el.offsetParent, NodeFilter.SHOW_TEXT, { acceptNode: n => (!el.contains(n) && n.textContent.trim()) ? 1 : 3 });
    let hit = null;
    for (let n = tw.nextNode(); n && !hit; n = tw.nextNode()) {
      const rg = document.createRange(); rg.selectNodeContents(n);
      for (const q of rg.getClientRects()) if (q.width && q.right > r.left + 1 && q.left < r.right - 1 && q.bottom > r.top + 1 && q.top < r.bottom - 1) { hit = q; break; }
    }
    if (hit) add("under-control", "error", el, `text at ${px(hit.left)}–${px(hit.right)} px runs under the control at ${px(r.left)}–${px(r.right)} px`, [r, hit]);
  }
  // 12. a label never breaks across lines (owner, 2026-10-15: a "Default" chip read "Defaul / t" on a phone)
  for (const el of document.querySelectorAll(".chip:not(.wrap), .tag-missing, .a-tag, .sticker, .h-pill-tag, .x-chip, .hh-pill, .a-rstamp, .kicker.a-idx .a-idx-n, .btn")) {
    if (!seen(el)) continue;
    const tops = new Set(), tw = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);  // text only: an icon beside the label is not a line
    for (let n = tw.nextNode(); n; n = tw.nextNode()) {
      if (!n.textContent.trim()) continue;
      const rg = document.createRange(); rg.selectNodeContents(n);
      for (const q of rg.getClientRects()) if (q.width > 1) tops.add(Math.round((q.top + q.height / 2) / 6));
    }
    if (tops.size > 1) add("label-break", "error", el, `"${el.textContent.trim().slice(0, 40)}" runs over ${tops.size} lines`, [R(el)]);
  }
  // 13. opposite actions: one row, secondary left, primary right (owner, 2026-10-15)
  for (const row of document.querySelectorAll(".x-actions, .hh-actions, .dialog-actions, form .actions")) {
    if (!seen(row)) continue;
    const bs = [...row.children].filter(seen).map(R); if (bs.length < 2) continue;
    const prim = [...row.children].findIndex(c => c.matches(".primary, [type=submit]"));
    if (new Set(bs.map(b => Math.round(b.top))).size > 1) add("actions", "error", row, `${bs.length} actions on ${new Set(bs.map(b => Math.round(b.top))).size} rows`, bs);
    else if (prim >= 0 && prim !== bs.length - 1) add("actions", "error", row, "the primary action is not on the right", bs);
  }
  // 14. nested corners (owner, 2026-10-21: "this issue is everywhere"): a rounded box set close inside a rounded box takes the
  //     outer radius minus the gap between their edges (inner = outer - gap, within 2 px), so the two curves run parallel. Only
  //     where the box sits evenly in the corner (both gaps within 2 px) and the gap is smaller than the outer radius; pills and
  //     circles, whose radius comes from their size, are left out.
  {
    const rad = e => parseFloat(cs(e).borderTopLeftRadius) || 0;
    const drawn = e => { const s = cs(e); return parseFloat(s.borderTopWidth) > 0 || !/rgba\(0, 0, 0, 0\)|transparent/.test(s.backgroundColor) || s.backgroundImage !== "none" || s.boxShadow !== "none"; };
    const pill = (e, b) => rad(e) >= Math.min(b.width, b.height) / 2 - 1;
    for (const inner of all) {
      const ri = rad(inner), bi = R(inner);
      if (ri <= 0 || inner.closest(any(cfg.nestedOk)) || !drawn(inner) || bi.width < 24 || bi.height < 24 || pill(inner, bi)) continue;
      let outer = inner.parentElement;
      while (outer && outer !== document.body && !(rad(outer) >= 6 && drawn(outer))) outer = outer.parentElement;
      if (!outer || outer === document.body || !seen(outer)) continue;
      const bo = R(outer), ro = rad(outer);
      if (pill(outer, bo)) continue;
      const dx = bi.left - bo.left, dy = bi.top - bo.top;
      if (dx < 0 || dy < 0 || Math.abs(dx - dy) > 2) continue;
      const gap = (dx + dy) / 2;
      if (gap >= ro) continue;
      const want = ro - gap;
      if (Math.abs(ri - want) > 2) add("nested-radius", "error", inner, `radius ${px(ri)} px inside a ${px(ro)} px corner ${px(gap)} px away: it should be ${px(want)} px (outer minus the gap)`, [bo, bi]);
    }
  }

  // 15. A library card or device frame shows the whole part, scaled down, never a cropped slice (owner, 2026-10-24: a zoomed-in
  // slice "hinders a person's ability to even see what they are choosing"). The part's drawn box must lie inside its frame.
  // Aisle tiles are left out: they are category teasers that fade out on purpose.
  for (const box of document.querySelectorAll(".item .lib-fit, .part-frame")) {
    const live = box.querySelector(".lib-live"), part = live && live.firstElementChild;
    if (!part || !box.checkVisibility()) continue;
    const f = R(box), p = R(part);
    if (!p.width || !p.height) continue;
    const vh = Math.max(0, Math.min(f.bottom, p.bottom) - Math.max(f.top, p.top)) / p.height;
    const vw2 = Math.max(0, Math.min(f.right, p.right) - Math.max(f.left, p.left)) / p.width;
    if (vh < 0.99 || vw2 < 0.99) add("preview-crop", "error", box, `the preview shows ${Math.round(vw2 * 100)}% of the part's width and ${Math.round(vh * 100)}% of its height${live.style.zoom ? "" : " (it was never fitted)"}`, [f, p]);
  }
  return out;
}"""

PREP = r"""async () => {
  document.querySelectorAll("img[loading=lazy]").forEach(i => { i.loading = "eager"; });
  await document.fonts.ready;
  await Promise.race([Promise.all([...document.images].map(i => i.complete ? 0 : new Promise(ok => { i.onload = i.onerror = ok; }))),
                      new Promise(ok => setTimeout(ok, 8000))]);
}"""
# Measure the page at rest: entrance animations and scroll reveals are finished first, so a transform in flight is never read as a layout error.
SETTLE = """() => { document.getAnimations().forEach(a => { try { a.finish(); } catch (e) {} });
  document.querySelectorAll(".reveal-wait").forEach(el => el.classList.remove("reveal-wait"));
  document.querySelectorAll(".reveal").forEach(el => { el.style.transition = "none"; el.classList.remove("reveal"); });
  return new Promise(ok => requestAnimationFrame(() => requestAnimationFrame(ok))); }"""
TABS = r"""(k) => {  // k < 0: report the selected tab of each tablist; else select tab k where it exists
  const lists = [...document.querySelectorAll("[role=tablist]")].map(l => [...l.querySelectorAll("[role=tab]")]);
  if (k < 0) return lists.map(t => Math.max(0, t.findIndex(x => x.getAttribute("aria-selected") === "true")));
  let n = 0;
  lists.forEach((t, i) => { const j = Array.isArray(k) ? k[i] : k; if (t[j]) { t[j].click(); n++; } });
  return n;
}"""
MARK = r"""(rects) => {
  document.querySelectorAll(".__lc").forEach(e => e.remove());
  rects.forEach(([x, y, w, h], i) => { const d = document.createElement("div"); d.className = "__lc";
    d.style.cssText = `position:absolute;left:${x - 2}px;top:${y - 2}px;width:${w + 4}px;height:${h + 4}px;z-index:2147483647;pointer-events:none;` +
      `outline:2px solid ${i ? "#ff00aa" : "#e00000"};`; document.body.appendChild(d); });
}"""


def figure_names():
    names = {}
    for f in sorted((SITE / "figures").glob("*.html")):
        m = re.search(r"<figcaption[^>]*>(.*?)</figcaption>", f.read_text(), re.S)
        if m:
            names[re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", m.group(1)))).strip()[:48]] = f.name
    return names


def pages_from_sitemap():
    xml = (SITE / "dist" / "sitemap.xml").read_text()
    return [u[len(SITE_URL):] or "/" for u in re.findall(r"<loc>([^<]+)</loc>", xml)]


def shoot(page, f, width, path):
    xs = [r[0] for r in f["rects"]] + [r[0] + r[2] for r in f["rects"]]
    ys = [r[1] for r in f["rects"]] + [r[1] + r[3] for r in f["rects"]]
    if not xs:
        return
    full = page.evaluate("() => [document.documentElement.scrollWidth, document.documentElement.scrollHeight]")
    x0, y0 = max(0, min(xs) - 32), max(0, min(ys) - 32)
    x1, y1 = min(max(full[0], width), max(xs) + 32), min(full[1], max(ys) + 32, y0 + 1600)
    page.evaluate(MARK, f["rects"])
    page.screenshot(path=str(path), clip={"x": x0, "y": y0, "width": max(1, x1 - x0), "height": max(1, y1 - y0)}, full_page=True)
    page.evaluate(MARK, [])


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", default="http://localhost:4173", help="where site/dist is served")
    ap.add_argument("--pages", help="comma-separated paths, for example /,/docs/ (default: every page in the sitemap)")
    ap.add_argument("--widths", default=",".join(map(str, WIDTHS)), help="comma-separated widths in CSS px")
    ap.add_argument("--shots", default=str(SITE / ".cache" / "layout"), help="folder for the error screenshots")
    ap.add_argument("--errors-only", action="store_true", help="leave warnings out of the report")
    a = ap.parse_args()
    pages = [p.strip() for p in a.pages.split(",")] if a.pages else pages_from_sitemap()
    widths = [int(w) for w in a.widths.split(",")]
    shots = pathlib.Path(a.shots)
    shots.mkdir(parents=True, exist_ok=True)
    for old in shots.glob("layout-*.png"):
        old.unlink()
    figs = figure_names()
    cfg = {"cards": CARDS, "notCards": NOT_CARDS, "panels": PANELS, "galleries": GALLERIES, "scrollOk": SCROLL_OK, "stuckOk": STUCK_OK, "marksOk": MARKS_OK, "previews": PREVIEWS, "nestedOk": NESTED_OK}
    errors = warnings = 0
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome")
        page = browser.new_page(viewport={"width": widths[0], "height": 900}, device_scale_factor=1)
        for url in pages:
            page.goto(a.base.rstrip("/") + url, wait_until="load")
            try:  # let late requests (photos, the GitHub count) land, so the layout is the one people see
                page.wait_for_load_state("networkidle", timeout=10000)
            except Exception:
                pass
            page.evaluate(PREP)
            start, tabs = page.evaluate(TABS, -1), page.evaluate("() => Math.max(0, ...[...document.querySelectorAll('[role=tablist]')].map(l => l.querySelectorAll('[role=tab]').length))")
            slug = url.strip("/").replace("/", "-") or "home"
            report = []
            for w in widths:
                page.set_viewport_size({"width": w, "height": 900})
                for _ in range(2):  # grow the window to the page's height, so nothing waits below the fold
                    page.evaluate(SETTLE)
                    h = page.evaluate("() => document.documentElement.scrollHeight")
                    page.set_viewport_size({"width": w, "height": min(max(h, 600), MAX_HEIGHT)})
                page.evaluate("() => scrollTo(0, 0)")
                found = {}
                for k in range(max(1, tabs)):  # pass k shows tab k of every tablist; findings are merged
                    if k:
                        page.evaluate(TABS, k)
                    page.evaluate(SETTLE)
                    for f in page.evaluate(MEASURE, cfg):
                        found.setdefault((f["check"], f["sel"], f["msg"]), {**f, "tab": k})
                    if k == max(1, tabs) - 1 and tabs:
                        page.evaluate(TABS, start)
                rows = sorted(found.values(), key=lambda f: (f["level"] != "error", f["check"]))
                if a.errors_only:
                    rows = [f for f in rows if f["level"] == "error"]
                for n, f in enumerate(rows, 1):
                    if f["level"] == "error":
                        errors += 1
                        shot = shots / f"layout-{slug}-{w}-{n:02d}-{f['check']}.png"
                        if f.get("tab"):
                            page.evaluate(TABS, f["tab"])
                        shoot(page, f, w, shot)
                        if f.get("tab"):
                            page.evaluate(TABS, start)
                        f["shot"] = shot
                    else:
                        warnings += 1
                if rows:
                    report.append((w, rows))
            print(f"{url}: " + ("ok at every width" if not report else f"{sum(len(r) for _, r in report)} findings"))
            for w, rows in report:
                print(f"  at {w} px")
                for f in rows:
                    where = f["sel"] + (f"  [figure {figs.get(f['fig'], f['fig'][:30] + '...')}]" if f["fig"] else "")
                    print(f"    {f['level']:<7} {f['check']:<13} {where}")
                    print(f"            {f['msg']}" + (f" (tab {f['tab'] + 1})" if f.get("tab") else ""))
                    print(f"            fix: {HINTS[f['check']]}" + (f"\n            shot: {f['shot']}" if f.get("shot") else ""))
        browser.close()
    print(f"\n{len(pages)} pages at {len(widths)} widths: {errors} errors, {warnings} warnings" + (f"; screenshots in {shots}" if errors else ""))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
