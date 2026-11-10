// What a page renders: the computed colours, font sizes, spacing, radii and box shadows of every visible element,
// counted. Read-only; independent of any extractor's logic. Run with capture.py.
(() => {
  const C = {color: {}, fontSize: {}, spacing: {}, radius: {}, shadow: {}};
  const bump = (cat, v) => { C[cat][v] = (C[cat][v] || 0) + 1; };
  const hex = s => { const m = s.match(/rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)/); if (!m) return null;
    const a = m[4] === undefined ? 1 : +m[4]; if (a === 0) return null;
    const h = '#' + [m[1], m[2], m[3]].map(x => Math.round(+x).toString(16).padStart(2, '0')).join('');
    return a >= 0.999 ? h : h + Math.round(a * 255).toString(16).padStart(2, '0'); };
  const ownText = el => [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
  for (const el of document.querySelectorAll('body *')) {
    const r = el.getBoundingClientRect(); if (r.width < 1 || r.height < 1) continue;
    const cs = getComputedStyle(el); if (cs.visibility === 'hidden' || cs.display === 'none' || +cs.opacity === 0) continue;
    if (ownText(el)) { const c = hex(cs.color); if (c) bump('color', c); bump('fontSize', parseFloat(cs.fontSize)); }
    const bg = hex(cs.backgroundColor); if (bg) bump('color', bg);
    for (const s of ['Top', 'Right', 'Bottom', 'Left']) if (parseFloat(cs['border' + s + 'Width']) > 0 && cs['border' + s + 'Style'] !== 'none') { const b = hex(cs['border' + s + 'Color']); if (b) bump('color', b); }
    for (const p of ['paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft', 'marginTop', 'marginRight', 'marginBottom', 'marginLeft', 'rowGap', 'columnGap']) {
      const v = parseFloat(cs[p]); if (v > 0 && !(p.startsWith('margin') && cs[p] === 'auto')) bump('spacing', Math.round(v * 100) / 100); }
    for (const p of ['borderTopLeftRadius', 'borderTopRightRadius', 'borderBottomRightRadius', 'borderBottomLeftRadius']) { const v = parseFloat(cs[p]); if (v > 0) { bump('radius', Math.round(v * 100) / 100); break; } }
    if (cs.boxShadow && cs.boxShadow !== 'none') bump('shadow', cs.boxShadow);
  }
  // Optional (issue #110): how many :focus rules resolve to one colour, and how many of them match an element on the page
  const FOCUS = '__FOCUS__'.toLowerCase(); let focusRules = 0, focusMatched = 0;
  if (FOCUS) {
    const strip = s => s.replace(/:focus(-visible|-within)?/g, '').trim() || '*';
    const root = getComputedStyle(document.documentElement);
    const res = v => v.replace(/var\((--[\w-]+)\s*(?:,([^()]*))?\)/g, (_, n, fb) => root.getPropertyValue(n).trim() || (fb || '').trim());
    const walk = rules => { for (const r of rules) {
      if (r.selectorText && /:focus/.test(r.selectorText) && r.style) {
        const t = ['outline-color', 'outline', 'box-shadow', 'border-color'].map(k => res(r.style.getPropertyValue(k) || '')).join(' ').toLowerCase();
        if (t.includes(FOCUS)) { focusRules++; let n = 0;
          for (const part of r.selectorText.split(',')) { try { n += document.querySelectorAll(strip(part)).length; } catch (_) {} }
          if (n) focusMatched++; } }
      if (r.cssRules) walk(r.cssRules); } };
    for (const sh of document.styleSheets) { try { walk(sh.cssRules); } catch (_) {} }
  }
  return JSON.stringify({rendered: C, focus: FOCUS ? {colour: FOCUS, rules: focusRules, matchSomethingOnPage: focusMatched} : null});
})()
