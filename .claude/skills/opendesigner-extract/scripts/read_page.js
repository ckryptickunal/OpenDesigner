// OpenDesigner reference reader: paste into a browser tool's JavaScript runner on a page the person
// approved (Claude in Chrome javascript_tool, Playwright page.evaluate, DevTools console). It only reads
// computed styles and returns JSON; it sends nothing anywhere. Save the result as page.json, then run
//   python3 css_scan.py --from-json page.json
// Motion is only what CSS declares on these elements; states (hover, focus, open) need interaction.
(() => {
  const bump = (o, k) => { if (k !== '' && k != null) o[k] = (o[k] || 0) + 1; };
  const V = { colors: {}, fontFamilies: {}, fontSizes: {}, lineHeights: {}, fontWeights: {}, spacing: {},
    radii: {}, shadows: {}, durations: {}, easings: {} };
  const toHex = c => { const m = c && c.match(/rgba?\(([^)]+)\)/); if (!m) return null;
    const p = m[1].split(/[\s,\/]+/).filter(Boolean).map(Number); if (p.length > 3 && p[3] === 0) return null;
    return '#' + p.slice(0, 3).map(v => Math.round(v).toString(16).padStart(2, '0')).join(''); };
  const els = [...document.querySelectorAll('body *')].filter(e => {
    const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0; }).slice(0, 500);
  const small = [];
  for (const e of els) {
    const s = getComputedStyle(e);
    for (const k of ['color', 'backgroundColor', 'borderTopColor']) { const h = toHex(s[k]); if (h) bump(V.colors, h); }
    bump(V.fontFamilies, s.fontFamily.split(',')[0].replace(/["']/g, '').trim());
    bump(V.fontSizes, Math.round(parseFloat(s.fontSize)));
    bump(V.fontWeights, s.fontWeight);
    bump(V.lineHeights, s.lineHeight);
    for (const k of ['paddingTop', 'paddingLeft', 'marginTop', 'marginBottom', 'rowGap', 'columnGap']) {
      const v = Math.round(parseFloat(s[k])); if (v > 0 && v <= 160) bump(V.spacing, v); }
    const r = parseFloat(s.borderTopLeftRadius); if (r > 0) bump(V.radii, r >= 999 ? 'full' : Math.round(r));
    if (s.boxShadow && s.boxShadow !== 'none') bump(V.shadows, s.boxShadow);
    const d = s.transitionDuration.split(',')[0]; const ms = parseFloat(d) * (d.endsWith('ms') ? 1 : 1000);
    if (ms > 0) { bump(V.durations, Math.round(ms)); bump(V.easings, s.transitionTimingFunction.split(',')[0]); }
    if (e.matches('a,button,input,select,textarea,[role=button]')) {
      const b = e.getBoundingClientRect(); if (b.width < 24 || b.height < 24) small.push(e.tagName.toLowerCase()); }
  }
  const props = {}, media = new Set();
  for (const sh of document.styleSheets) { let rules; try { rules = sh.cssRules; } catch (_) { continue; }
    for (const r of rules) {
      if (r.selectorText === ':root' || r.selectorText === 'html') for (const n of r.style) if (n.startsWith('--')) props[n] = r.style.getPropertyValue(n).trim();
      if (r.media) media.add(r.media.mediaText);
    } }
  return JSON.stringify({ source: location.href, method: 'computed', elements: els.length,
    values: V, customProperties: props, media: [...media].slice(0, 30), targetsUnder24: small.length }, null, 1);
})();
