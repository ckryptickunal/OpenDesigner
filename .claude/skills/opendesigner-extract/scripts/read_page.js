// OpenDesigner reference reader. Paste into a browser tool's JavaScript runner on a page the person
// approved (Claude in Chrome javascript_tool, Playwright page.evaluate, DevTools console). It only reads
// computed styles and same-origin stylesheets and returns JSON; it sends nothing anywhere. Save the
// result as page.json, then run:  python3 css_scan.py --from-json page.json --json
//
// It records values by role, so css_scan.py can tell body text from headings and buttons from links:
//   text sizes weighted by characters of visible text: body (running text), heading, nav, caption
//     (footer, small print, legal), control, code, label (short UI text and link lists)
//   corner radii of controls (buttons, inputs), containers (cards, dialogs, menus), inline links,
//     decoration (badges, pills, dots) and media
//   colors on buttons, links, selected states and :focus rules (accent candidates)
//   box shadows (text shadows are never read), transitions and animations split per layer
// Motion is only what CSS declares; JavaScript-driven motion and hover, focus or open states need
// interaction. Under Node this file only exports its pure helpers (used by test_extract.py).
(() => {
  // ---------- pure helpers ----------
  const splitTop = s => { // split on commas that are not inside parentheses: cubic-bezier(a, b, c, d), linear(...)
    const out = []; let depth = 0, cur = '';
    for (const ch of String(s == null ? '' : s)) {
      if (ch === '(') depth++;
      else if (ch === ')') depth = Math.max(0, depth - 1);
      if (ch === ',' && depth === 0) { if (cur.trim()) out.push(cur.trim()); cur = ''; } else cur += ch;
    }
    if (cur.trim()) out.push(cur.trim());
    return out;
  };
  const toMs = t => { t = String(t).trim(); const v = parseFloat(t); if (isNaN(v)) return 0; return t.endsWith('ms') ? v : v * 1000; };
  const parseRgb = c => { // computed sRGB colors: rgb(r, g, b) / rgba(r, g, b, a) / rgb(r g b / a)
    const m = String(c || '').match(/^rgba?\(([^()]*)\)$/); if (!m) return null;
    const p = m[1].split(/[\s,\/]+/).filter(Boolean); if (p.length < 3) return null;
    const ch = p.slice(0, 3).map(v => v.endsWith('%') ? parseFloat(v) * 2.55 : parseFloat(v));
    if (ch.some(isNaN)) return null;
    const a = p.length > 3 ? (p[3].endsWith('%') ? parseFloat(p[3]) / 100 : parseFloat(p[3])) : 1;
    return { hex: '#' + ch.map(v => Math.max(0, Math.min(255, Math.round(v))).toString(16).padStart(2, '0')).join(''), a };
  };
  const radiusValue = (r, w, h) => { // "6px" -> 6, pills and circles -> "full", "50%" -> "full"
    const first = String(r || '').trim().split(/\s+/)[0]; const v = parseFloat(first);
    if (isNaN(v)) return null;
    const side = Math.min(w || 0, h || 0);
    const px = first.endsWith('%') ? v / 100 * side : v;
    if ((first.endsWith('%') && v >= 50) || px >= 999 || (px > 0 && side > 0 && px >= side / 2 - 0.5)) return 'full';
    return Math.round(px);
  };
  const bump = (o, k, n = 1) => { if (k !== '' && k != null) o[k] = (o[k] || 0) + n; };
  const bumpIn = (o, group, k, n = 1) => { if (k === '' || k == null) return; (o[group] = o[group] || {}); bump(o[group], k, n); };
  const solid = c => c && c.a >= 0.5;
  const shadowVisible = sh => splitTop(sh === 'none' ? '' : sh).some(l => { // any outer layer with color and size
    const m = l.match(/rgba?\([^()]*\)/); const c = m ? parseRgb(m[0]) : null;
    const sizes = (l.replace(/rgba?\([^()]*\)/, '').match(/-?\d*\.?\d+px/g) || []).map(parseFloat);
    return !/\binset\b/.test(l) && (!c || c.a > 0) && sizes.some(n => n !== 0); });

  // Text role: headings, navigation, small print, controls and code are kept apart from running text;
  // link text outside a paragraph (link lists, card links) and short text are UI labels.
  const textRole = d => d.ctx || (d.linkText ? 'label' : (d.prose || d.own >= 40) ? 'body' : 'label');

  // Radius role: only controls and containers describe a system's corner style, and only when the
  // corner is visible (a fill, a border or a shadow); a transparent text button has no visible corner.
  const radiusRole = (d, r, vw) => {
    if (d.media) return 'media';
    const surface = solid(d.bg) || (d.border && d.border.w > 0 && d.border.a > 0) || shadowVisible(d.boxShadow);
    if (d.buttonLike || d.formField) return surface ? 'control' : 'bare';
    if (d.link) return 'link';
    const sized = d.w >= 120 && d.h >= 48 && (!vw || d.w < 0.95 * vw);
    if (surface && sized && (r !== 0 || d.containerHint)) return 'container';
    return r ? 'decor' : null;
  };

  // d = one element described by describe() below (or a plain object in tests).
  function collect(items, vw) {
    const V = { colors: {}, fontFamilies: {}, fontSizes: {}, lineHeights: {}, fontWeights: {}, spacing: {},
      radii: {}, shadows: {}, durations: {}, easings: {},
      textSizes: {}, textElements: {}, radiiByRole: {}, accentSources: {} };
    let under24 = 0;
    for (const d of items) {
      if (d.own > 0 && d.fontSize > 0) {
        const role = textRole(d), px = Math.round(d.fontSize);
        bumpIn(V.textSizes, role, px, d.own); bumpIn(V.textElements, role, px, 1);
        bump(V.fontSizes, px); bump(V.fontFamilies, d.fontFamily, d.own);
        bump(V.fontWeights, d.fontWeight); bump(V.lineHeights, d.lineHeight);
        if (d.color && d.color.a > 0) bump(V.colors, d.color.hex);
      }
      if (d.bg && d.bg.a > 0) bump(V.colors, d.bg.hex);
      if (d.border && d.border.w > 0 && d.border.a > 0) bump(V.colors, d.border.hex);
      for (const v of d.spacing || []) { const n = Math.round(v); if (n > 0 && n <= 160) bump(V.spacing, n); }
      const r = radiusValue(d.radius, d.w, d.h);
      const rr = r === null ? null : radiusRole(d, r, vw);
      if (rr && (r !== 0 || rr === 'control' || rr === 'container')) { bumpIn(V.radiiByRole, rr, r); if (r !== 0) bump(V.radii, r); }
      if (d.boxShadow && d.boxShadow !== 'none' && shadowVisible(d.boxShadow)) bump(V.shadows, d.boxShadow);
      // accent candidates: colors that mark interaction
      if (d.buttonLike) {
        if (solid(d.bg)) bumpIn(V.accentSources, 'button', d.bg.hex);
        if (d.border && d.border.w > 0 && solid(d.border)) bumpIn(V.accentSources, 'buttonBorder', d.border.hex);
        if (solid(d.color)) bumpIn(V.accentSources, 'buttonText', d.color.hex);
      } else if (d.link && solid(d.color)) bumpIn(V.accentSources, 'link', d.color.hex);
      if (d.selected) for (const c of [d.bg, d.color, d.border]) if (solid(c) && (c !== d.border || d.border.w > 0)) bumpIn(V.accentSources, 'selected', c.hex);
      if (d.formField && solid(d.accentColor)) bumpIn(V.accentSources, 'control', d.accentColor.hex);
      // motion: one entry per distinct (duration, easing) on each element
      const seen = new Set();
      for (const [props, durs, fns] of [d.transition || [], d.animation || []]) {
        const P = splitTop(props), D = splitTop(durs), F = splitTop(fns);
        P.forEach((p, i) => {
          if (p === 'none' || !D.length) return;
          const ms = Math.round(toMs(D[i % D.length])); const fn = F.length ? F[i % F.length] : 'ease';
          if (ms > 0 && !seen.has(ms + fn)) { seen.add(ms + fn); bump(V.durations, ms); bump(V.easings, fn); }
        });
      }
      if ((d.buttonLike || d.formField) && (d.w < 24 || d.h < 24)) under24++;
    }
    return { values: V, targetsUnder24: under24 };
  }

  const api = { splitTop, toMs, parseRgb, radiusValue, shadowVisible, textRole, radiusRole, collect };
  if (typeof document === 'undefined' || typeof window === 'undefined') {
    if (typeof module !== 'undefined' && module.exports) module.exports = api;
    return api;
  }

  // ---------- browser adapter ----------
  const cvs = document.createElement('canvas'); cvs.width = cvs.height = 1;
  const cx = cvs.getContext('2d', { willReadFrequently: true }); const cache = new Map();
  const color = c => { // any CSS color (rgb, oklch, color(), lab) -> {hex, a}
    if (!c || c === 'transparent') return null; if (cache.has(c)) return cache.get(c);
    let out = parseRgb(c);
    if (!out && cx) { cx.clearRect(0, 0, 1, 1); cx.fillStyle = '#000'; cx.fillStyle = c; cx.fillRect(0, 0, 1, 1);
      const p = cx.getImageData(0, 0, 1, 1).data;
      out = p[3] ? { hex: '#' + [p[0], p[1], p[2]].map(v => v.toString(16).padStart(2, '0')).join(''), a: p[3] / 255 } : null; }
    cache.set(c, out); return out;
  };
  const styles = new Map(); const cs = e => { if (!styles.has(e)) styles.set(e, getComputedStyle(e)); return styles.get(e); };
  const CTX = [['code', 'pre,code,kbd,samp'], ['heading', 'h1,h2,h3,h4,h5,h6,[role=heading]'],
    ['control', 'button,[role=button],input,select,textarea,label,[role=tab],[role=menuitem],[role=option],[role=switch]'],
    ['caption', 'small,figcaption,caption,footer,sup,sub,[role=contentinfo],[class*=legal i],[class*=disclaimer i],[class*=footnote i],[class*=caption i],[class*=copyright i]'],
    ['nav', 'nav,[role=navigation],[role=menubar],[role=menu],[role=tablist],[role=banner]']];
  const FIELD = 'input:not([type=hidden]):not([type=submit]):not([type=button]):not([type=reset]):not([type=image]),select,textarea';
  const CONTAINER = /(^|[\s_-])(card|modal|dialog|popover|panel|sheet|tile|dropdown|toast|tooltip|menu|popup|drawer)([\s_-]|$)/i;
  const buttonLike = (e, s, b) => {
    if (e.matches('button,[role=button],input[type=submit],input[type=button],input[type=reset]')) return true;
    if (!e.matches('a[href]') || s.display === 'inline' || b.height < 24 || parseFloat(s.paddingLeft) < 8) return false;
    const bg = color(s.backgroundColor), bc = color(s.borderTopColor);
    return solid(bg) || (parseFloat(s.borderTopWidth) >= 1 && solid(bc));
  };
  const ownText = e => { let n = 0; for (const c of e.childNodes) if (c.nodeType === 3) n += c.textContent.replace(/\s+/g, ' ').trim().length; return n; };
  const describe = e => {
    const s = cs(e), b = e.getBoundingClientRect();
    const btn = buttonLike(e, s, b);
    let ctx = null;
    for (const [role, sel] of CTX) { if (e.closest(sel)) { ctx = role; break; } }
    const a = e.closest('a[href]');
    if (!ctx && a && buttonLike(a, cs(a), a.getBoundingClientRect())) ctx = 'control';
    return {
      tag: e.tagName.toLowerCase(), w: b.width, h: b.height, own: ownText(e), ctx,
      prose: !!e.closest('p,li,dd,dt,td,th,blockquote'), linkText: !!a && !e.closest('p,dd,td,th,blockquote'),
      buttonLike: btn, link: !btn && e.matches('a[href]'), formField: e.matches(FIELD),
      selected: e.matches('[aria-selected=true],[aria-current]:not([aria-current=false]),[aria-pressed=true],[aria-checked=true],:checked'),
      media: e.matches('img,video,picture,svg,canvas,iframe'),
      containerHint: e.matches('dialog,[role=dialog],[role=alertdialog],[role=menu],[role=listbox],[role=tooltip],[popover]') || CONTAINER.test(e.getAttribute('class') || ''),
      fontSize: parseFloat(s.fontSize), fontFamily: s.fontFamily.split(',')[0].replace(/["']/g, '').trim(),
      fontWeight: s.fontWeight, lineHeight: s.lineHeight,
      color: color(s.color), bg: color(s.backgroundColor),
      border: (() => { const c = color(s.borderTopColor); return c ? { ...c, w: parseFloat(s.borderTopWidth) || 0 } : null; })(),
      accentColor: s.accentColor && s.accentColor !== 'auto' ? color(s.accentColor) : null,
      radius: s.borderTopLeftRadius, boxShadow: s.boxShadow,
      spacing: ['paddingTop', 'paddingLeft', 'marginTop', 'marginBottom', 'rowGap', 'columnGap'].map(k => parseFloat(s[k]) || 0),
      transition: [s.transitionProperty, s.transitionDuration, s.transitionTimingFunction],
      animation: s.animationName && s.animationName !== 'none' ? [s.animationName, s.animationDuration, s.animationTimingFunction] : null,
    };
  };

  // Sample across the whole page (not only the header): every visible element, evenly thinned past 6000.
  const all = [...document.body.getElementsByTagName('*')];
  const step = Math.max(1, Math.ceil(all.length / 6000));
  const els = all.filter((e, i) => {
    if (i % step) return false;
    const s = cs(e), b = e.getBoundingClientRect();
    return b.width > 1 && b.height > 1 && s.visibility !== 'hidden' && s.display !== 'none' && parseFloat(s.opacity) > 0;
  });
  const vw = document.documentElement.clientWidth;
  const { values: V, targetsUnder24 } = collect(els.map(describe), vw);

  // Stylesheets: :root custom properties, :focus and selected-state rules (states the page is not in now).
  const root = getComputedStyle(document.documentElement);
  const resolve = v => v.replace(/var\((--[\w-]+)\s*(?:,([^()]*))?\)/g, (_, n, fb) => root.getPropertyValue(n).trim() || (fb || '').trim());
  const COLOR_TOKEN = /#[0-9a-f]{3,8}\b|(?:rgba?|hsla?|oklch|oklab|lab|lch|color)\([^()]*\)/gi;
  const props = {}, media = new Set();
  const walk = rules => { for (const r of rules) {
    if (r.media) media.add(r.media.mediaText);
    if (r.selectorText && r.style) {
      if (/(^|,)\s*(:root|html)\b/.test(r.selectorText)) for (const n of r.style) if (n.startsWith('--')) props[n] = r.style.getPropertyValue(n).trim();
      const focus = /:focus/.test(r.selectorText);
      const sel = /\[aria-(selected|current|pressed|checked)|:checked|\.(active|selected|is-active|is-selected)\b|\[data-state=?["']?(active|checked|on)/.test(r.selectorText);
      if (focus || sel) {
        const keys = focus ? ['outline-color', 'outline', 'box-shadow', 'border-color'] : ['background-color', 'background', 'color', 'border-color'];
        for (const k of keys) for (const t of resolve(r.style.getPropertyValue(k) || '').match(COLOR_TOKEN) || []) {
          const c = color(t); if (solid(c)) bumpIn(V.accentSources, focus ? 'focus' : 'selected', c.hex); }
      }
    }
    if (r.cssRules) walk(r.cssRules);
  } };
  for (const sh of document.styleSheets) { try { walk(sh.cssRules); } catch (_) { /* cross-origin sheet */ } }

  return JSON.stringify({ source: location.href, method: 'computed', elements: els.length, totalElements: all.length,
    viewport: [vw, window.innerHeight], values: V, customProperties: props, media: [...media].slice(0, 30),
    targetsUnder24 }, null, 1);
})();
