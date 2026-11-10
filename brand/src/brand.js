/* OpenDesigner brand: builds one asset from window.ASSETS by ?id=..., at its exact size. */
(function () {
  const $ = (s, el = document) => el.querySelector(s);
  const id = new URLSearchParams(location.search).get("id") || window.ASSETS[0].id;
  const A = window.ASSETS.find(a => a.id === id);
  if (!A) { document.body.textContent = "unknown asset " + id; return; }
  const W = A.w, H = A.h;
  document.title = "OpenDesigner · " + A.id;
  document.documentElement.style.width = W + "px"; document.documentElement.style.height = H + "px";
  document.body.style.width = W + "px"; document.body.style.height = H + "px";
  document.body.dataset.theme = A.theme || "ink";

  // deterministic noise
  function rng(seed) { let s = seed >>> 0 || 1; return () => ((s = Math.imul(s ^ (s >>> 15), 2246822507) ^ Math.imul(s ^ (s >>> 13), 3266489909), (s ^= s >>> 16) >>> 0) / 4294967296); }

  // the tile field: radius ramps along the x axis (square to circle); lit tiles cluster near the focus
  function tiles(o) {
    const el = document.createElement("div"); el.className = "tiles";
    const cols = Math.round((o.w + o.gap) / (o.cell + o.gap)), rows = Math.round((o.h + o.gap) / (o.cell + o.gap));
    Object.assign(el.style, { left: o.x + "px", top: o.y + "px", gap: o.gap + "px",
      gridTemplateColumns: `repeat(${cols}, ${o.cell}px)`, gridAutoRows: o.cell + "px" });
    if (o.mask) el.style.maskImage = el.style.webkitMaskImage = o.mask;
    const r = rng(o.seed || 7);
    const fx = o.fx ?? .7, fy = o.fy ?? .5, R = o.sig ?? .28, s1 = r() * 6.28, s2 = r() * 6.28;
    const aspect = rows / cols;
    for (let j = 0; j < rows; j++) for (let i = 0; i < cols; i++) {
      const dx = (i + .5) / cols - fx, dy = ((j + .5) / rows - fy) * aspect * (o.squash || 1);
      const a = Math.atan2(dy, dx), d = Math.hypot(dx, dy);
      const rr = R * (1 + .2 * Math.sin(3 * a + s1) + .1 * Math.sin(5 * a + s2));
      const lv = d / rr + (r() - .5) * (o.dither ?? .32);
      const c = document.createElement("i");
      const k = Math.max(0, Math.min(1, 1.15 - lv));            // 1 at the core, 0 outside
      c.style.borderRadius = (o.flat ? 18 : Math.round(10 + k * 40)) + "%";
      if (lv < .42) c.className = "on"; else if (lv < .7) c.className = "on2"; else if (lv < .95) c.className = "on3"; else if (lv < 1.2) c.className = "on4";
      el.appendChild(c);
    }
    return el;
  }
  const glow = (x, y, s, blur) => { const g = document.createElement("div"); g.className = "glow"; Object.assign(g.style, { left: x - s / 2 + "px", top: y - s / 2 + "px", width: s + "px", height: s + "px" }); if (blur) g.style.setProperty("--blur", blur + "px"); return g; };
  const mark = (m) => `<span class="mark" style="--m:${m}px"><i></i><i></i><i></i><i></i></span>`;
  const lockup = (m) => `<div class="lockup" style="--m:${m}px">${mark(m)}<span>OpenDesigner</span></div>`;
  const html = (s) => { const t = document.createElement("template"); t.innerHTML = s.trim(); return t.content.firstElementChild; };

  // WCAG contrast, used to print real ratios on the ramp specimen
  const lum = h => { const c = [1, 3, 5].map(i => parseInt(h.slice(i, i + 2), 16) / 255).map(v => v <= .04045 ? v / 12.92 : Math.pow((v + .055) / 1.055, 2.4)); return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]; };
  const ratio = (a, b) => { const x = lum(a), y = lum(b); return (Math.max(x, y) + .05) / (Math.min(x, y) + .05); };

  // ---------- specimens (all sized from one unit u) ----------
  const T = window.TOKENS;
  const SPEC = {
    questions(u) {
      const rows = T.questions.map((q, i) => `
        <div style="display:grid;grid-template-columns:${2.4*u}px 1fr auto;align-items:center;gap:${1.1*u}px;padding:${1.05*u}px 0;border-top:1px solid var(--rule)">
          <span class="num" style="--num:${1.05*u}px">0${i + 1}</span>
          <span style="font-size:${1.5*u}px;letter-spacing:-.02em;font-weight:500">${q[0]}</span>
          <span class="pill ${i === 4 ? "" : ""}" style="font-size:${1.08*u}px">${i === 4 ? `<i style="width:.9em;height:.9em;border-radius:50%;background:var(--ember);display:inline-block"></i>` : ""}${q[1]}</span>
        </div>`).join("");
      return `<div class="panel" style="padding:${1.6*u}px ${2*u}px ${1.4*u}px">
        <div class="meta" style="--meta:${1.05*u}px;display:flex;justify-content:space-between;margin-bottom:${.9*u}px"><span>sketch · zoom 0</span><span>5 of 5</span></div>
        ${rows}
        <div style="display:flex;align-items:center;gap:${.8*u}px;padding-top:${1.2*u}px;border-top:1px solid var(--rule);font-size:${1.35*u}px;font-weight:500;letter-spacing:-.015em">
          <span style="width:${1.7*u}px;height:${1.7*u}px;border-radius:50%;background:var(--accent);display:grid;place-items:center;color:#fffaf7;font-size:${1*u}px">✓</span>
          A complete system. Checked.</div></div>`;
    },
    dials(u) {
      const rows = T.dials.map(d => `
        <div style="display:grid;grid-template-columns:${10.5*u}px 1fr ${3.2*u}px;align-items:center;gap:${1.2*u}px;padding:${.62*u}px 0">
          <span style="font-size:${1.32*u}px;font-weight:500;letter-spacing:-.015em">${d[0]}</span>
          <span style="position:relative;height:${.36*u}px;border-radius:99px;background:var(--rule)">
            <span style="position:absolute;inset:0 ${100 - d[3]}% 0 0;border-radius:99px;background:linear-gradient(90deg,transparent,var(--accent))"></span>
            <span style="position:absolute;left:${d[3]}%;top:50%;width:${1.5*u}px;height:${1.5*u}px;transform:translate(-50%,-50%);border-radius:50%;background:var(--bg);box-shadow:0 0 0 ${.22*u}px var(--accent)"></span>
          </span>
          <span class="mono" style="font-size:${1.1*u}px;color:var(--muted);text-align:right">${d[3]}</span>
        </div>`).join("");
      return `<div class="panel" style="padding:${1.6*u}px ${2*u}px">
        <div class="meta" style="--meta:${1.05*u}px;display:flex;justify-content:space-between;margin-bottom:${.6*u}px"><span>dials</span><span>0 — 100</span></div>${rows}</div>`;
    },
    ramps(u) {
      const bar = (arr, label) => `
        <div style="margin-bottom:${1.3*u}px">
          <div class="meta" style="--meta:${1.02*u}px;display:flex;justify-content:space-between;margin-bottom:${.6*u}px"><span>${label}</span><span>12 steps</span></div>
          <div style="display:grid;grid-template-columns:repeat(12,1fr);gap:${.25*u}px;height:${5.4*u}px">
            ${arr.map((c, i) => `<span style="background:${c};border-radius:${Math.round(.25*u + i*.12*u)}px"></span>`).join("")}</div></div>`;
      const r = ratio("#ffffff", T.accent[8]).toFixed(1);
      const r2 = ratio(T.neutral[11], T.neutral[1]).toFixed(1);
      return `<div class="panel" style="padding:${1.6*u}px ${2*u}px">
        ${bar(T.accent, "accent")}${bar(T.neutral, "neutral · warm")}
        <div style="display:flex;gap:${.8*u}px;flex-wrap:wrap">
          <span class="pill" style="font-size:${1.05*u}px"><b style="background:${T.accent[8]};color:#fff;padding:.25em .5em;border-radius:.4em;font-family:var(--sans)">Aa</b> ${r} : 1 · AA</span>
          <span class="pill" style="font-size:${1.05*u}px"><b style="background:${T.neutral[1]};color:${T.neutral[11]};padding:.25em .5em;border-radius:.4em;font-family:var(--sans);box-shadow:inset 0 0 0 1px var(--rule)">Aa</b> ${r2} : 1 · AAA</span>
        </div></div>`;
    },
    files(u) {
      const L = T.files.map(f => `<div style="display:flex;justify-content:space-between;gap:${u}px;padding:${.42*u}px 0;padding-left:${f[1]*1.9*u}px;${f[3] ? "color:var(--fg)" : "color:var(--muted)"}">
          <span>${f[1] ? "└ " : ""}${f[0]}</span><span style="color:var(--accent-text);opacity:${f[2] ? 1 : 0}">${f[2] || ""}</span></div>`).join("");
      return `<div class="panel mono" style="padding:${1.6*u}px ${2*u}px;font-size:${1.22*u}px;line-height:1.25">
        <div class="meta" style="--meta:${1.02*u}px;display:flex;justify-content:space-between;margin-bottom:${.8*u}px;font-family:var(--mono)"><span>your-project/</span><span>written by your AI</span></div>${L}</div>`;
    },
    a11y(u) {
      const items = ["Text contrast, WCAG 2.2 AA", "Targets at least 24 px", "Focus you can always see", "Motion that respects “reduce”"];
      return `<div class="panel" style="padding:${2*u}px ${2.2*u}px">
        <div style="display:flex;align-items:baseline;gap:${.8*u}px"><span style="font-size:${7.4*u}px;font-weight:600;letter-spacing:-.05em;line-height:.9">4.5</span><span class="serif" style="font-size:${4*u}px;color:var(--accent-text)">: 1</span></div>
        <div class="meta" style="--meta:${1.05*u}px;margin:${.6*u}px 0 ${1.4*u}px">the floor, locked in every mode</div>
        ${items.map(t => `<div style="display:flex;align-items:center;gap:${.9*u}px;padding:${.72*u}px 0;border-top:1px solid var(--rule);font-size:${1.38*u}px;font-weight:500;letter-spacing:-.015em">
          <span style="width:${1.5*u}px;height:${1.5*u}px;border-radius:${.4*u}px;background:var(--accent);color:#fffaf7;display:grid;place-items:center;font-size:${.9*u}px;flex:none">✓</span>${t}</div>`).join("")}
        <div style="margin-top:${1.2*u}px;display:flex;gap:${1*u}px;align-items:center">
          <span style="font-size:${1.25*u}px;font-weight:500;padding:${.75*u}px ${1.4*u}px;border-radius:${.7*u}px;background:var(--fg);color:var(--bg);outline:${.2*u}px solid var(--accent);outline-offset:${.25*u}px">Continue</span>
          <span class="meta" style="--meta:${1*u}px">focus ring · 3:1 against both sides</span></div></div>`;
    },
    prompt(u) {
      return `<div class="panel" style="padding:0;overflow:hidden;background:var(--ink-2);border-color:rgb(255 240 230 / .12);color:var(--paper-text)">
        <div style="display:flex;gap:${.55*u}px;padding:${1*u}px ${1.4*u}px;border-bottom:1px solid rgb(255 240 230 / .08)">${`<i style="width:${.8*u}px;height:${.8*u}px;border-radius:50%;background:rgb(255 240 230 / .16)"></i>`.repeat(3)}</div>
        <div class="mono" style="padding:${1.6*u}px ${2*u}px ${2*u}px;font-size:${1.3*u}px;line-height:1.6">
          <div><span style="color:var(--ember-glow)">›</span> Create a design system for this project.</div>
          <div style="color:var(--paper-muted);margin-top:${1*u}px">Looking at your code and colors first…</div>
          <div style="margin-top:${1*u}px">Question 1 of 5 · <span style="color:var(--paper-text)">Who is this for?</span></div>
          <div style="display:flex;gap:${.6*u}px;margin-top:${.8*u}px;flex-wrap:wrap">
            <span class="pill" style="font-size:${1*u}px;background:var(--ember);color:#fffaf7;border-color:transparent">Everyday people  ·  recommended</span>
            <span class="pill" style="font-size:${1*u}px;background:transparent;color:var(--paper-text);border-color:rgb(255 240 230 / .18)">Experts</span>
            <span class="pill" style="font-size:${1*u}px;background:transparent;color:var(--paper-text);border-color:rgb(255 240 230 / .18)">Large text</span></div>
          <div style="color:var(--paper-muted);margin-top:${1*u}px">Why: most people, most screens. You can change it later.</div>
        </div></div>`;
    },
    scale(u) {
      const sizes = T.typeScale;
      const max = sizes[sizes.length - 1];
      return `<div class="panel" style="padding:${1.6*u}px ${2*u}px">
        <div class="meta" style="--meta:${1.02*u}px;display:flex;justify-content:space-between;margin-bottom:${1*u}px"><span>type scale</span><span>${T.typeRatio}</span></div>
        <div style="display:flex;align-items:baseline;gap:${1*u}px;height:${5.8*u}px;font-weight:600;letter-spacing:-.04em;overflow:hidden">
          ${sizes.map(s => `<span style="font-size:${(s / max) * 5.6 * u}px;line-height:1">Aa</span>`).join("")}</div>
        <div class="meta" style="--meta:${1.02*u}px;display:flex;justify-content:space-between;margin:${1.6*u}px 0 ${1*u}px"><span>radius</span><span>0 → full</span></div>
        <div style="display:flex;gap:${.9*u}px">${T.radius.map((r, i) => `<span style="flex:1;aspect-ratio:1;border:${.16*u}px solid ${i === T.radius.length - 1 ? "var(--accent)" : "var(--fg)"};border-radius:${r === "full" ? "50%" : (r / 32 * 2.4 * u) + "px"}"></span>`).join("")}</div>
        <div class="meta" style="--meta:${1.02*u}px;display:flex;justify-content:space-between;margin:${1.6*u}px 0 ${1*u}px"><span>space</span><span>4 px base</span></div>
        <div style="display:flex;align-items:flex-end;gap:${.7*u}px">${T.space.map(s => `<span style="width:${s / 80 * 4.4 * u}px;height:${s / 80 * 4.4 * u}px;background:var(--accent);opacity:${.35 + s / 80 * .65};border-radius:2px"></span>`).join("")}</div>
      </div>`;
    },
  };

  // ---------- layouts ----------
  const C = document.createElement("div"); C.className = "canvas"; document.body.appendChild(C);
  const L = {
    // wide hero: words left, tile field right
    hero() {
      const P = Math.round(H * .1), fs = A.fs || Math.round(H * .135);
      const fieldX = Math.round(W * .5);
      C.appendChild(glow(W * .8, H * .5, H * 1.1, H * .2));
      C.appendChild(tiles({ x: fieldX, y: -4, w: W - fieldX + 4, h: H + 8, cell: Math.round(H / 21), gap: Math.round(H / 72), fx: .58, fy: .5, sig: .34, seed: A.seed || 11,
        mask: "radial-gradient(ellipse 62% 80% at 64% 50%, #000 30%, transparent 98%)" }));
      C.appendChild(html(`<div style="position:absolute;left:${P}px;top:${P}px;bottom:${P}px;width:${W * .56}px;display:flex;flex-direction:column">
        <div class="eyebrow" style="--eyebrow:${Math.round(H * .026)}px"><span class="dot"></span>${A.eyebrow}</div>
        <h1 class="display" style="font-size:${fs}px;margin-top:${H * .07}px">${A.title}</h1>
        ${A.lede ? `<p class="lede" style="font-size:${Math.round(H * .042)}px;margin-top:${H * .05}px;max-width:${W * .42}px">${A.lede}</p>` : ""}
        <div style="margin-top:auto;display:flex;align-items:center;gap:${H * .04}px">${lockup(Math.round(H * .055))}
          <span class="meta" style="--meta:${Math.round(H * .024)}px">${A.meta || ""}</span></div></div>`));
    },
    // feature: words + a specimen panel; landscape = side by side, portrait = stacked
    feature() {
      const land = W > H;
      const P = Math.round(Math.min(W, H) * (land ? .09 : .085));
      const u = A.u || (land ? H / 46 : W / 50);
      C.appendChild(glow(land ? W * .78 : W * .7, land ? H * .55 : H * .72, land ? H : W * 1.1, 160));
      C.appendChild(tiles({ x: land ? W * .52 : -10, y: land ? -10 : H * .48, w: land ? W * .5 : W + 20, h: land ? H + 20 : H * .55, cell: Math.round((land ? H : W) / 24), gap: Math.round((land ? H : W) / 90), fx: land ? .82 : .85, fy: land ? .2 : .1, sig: .3, seed: A.seed || 3,
        mask: "radial-gradient(ellipse 60% 60% at 50% 50%, #000 20%, transparent 90%)" }));
      const words = `<div class="eyebrow" style="--eyebrow:${Math.round(u * 1.1)}px"><span class="num" style="--num:${Math.round(u * 1.1)}px">${A.num}</span>${A.eyebrow}</div>
        <h2 class="display" style="font-size:${A.fs || Math.round(land ? H * .118 : W * .1)}px;margin-top:${u * 2.2}px">${A.title}</h2>
        <p class="lede" style="font-size:${Math.round(land ? H * .042 : W * .039)}px;margin-top:${u * 1.8}px;max-width:${land ? W * .4 : W * .84}px">${A.lede}</p>`;
      if (land) {
        C.appendChild(html(`<div style="position:absolute;left:${P}px;top:${P}px;bottom:${P}px;width:${W * .4}px;display:flex;flex-direction:column">${words}
          <div style="margin-top:auto">${lockup(Math.round(H * .05))}</div></div>`));
        C.appendChild(html(`<div style="position:absolute;right:${P}px;top:50%;transform:translateY(-50%);width:${W * .42}px">${SPEC[A.spec](u)}</div>`));
      } else {
        C.appendChild(html(`<div style="position:absolute;left:${P}px;right:${P}px;top:${P}px;bottom:${P * .7}px;display:flex;flex-direction:column">
          <div>${words}</div>
          <div style="margin-top:auto;margin-bottom:${P * .55}px">${SPEC[A.spec](u)}</div>
          <div style="display:flex;justify-content:space-between;align-items:center">${lockup(Math.round(W * .042))}<span class="meta" style="--meta:${Math.round(u)}px">${A.page || ""}</span></div></div>`));
      }
    },
    // big statement, any shape
    statement() {
      const land = W > H, P = Math.round(Math.min(W, H) * .09);
      C.appendChild(tiles({ x: -10, y: land ? H * .5 : H * .55, w: W + 20, h: land ? H * .5 : H * .42, cell: Math.round(Math.min(W, H) / 20), gap: Math.round(Math.min(W, H) / 80), fx: .62, fy: .5, sig: .3, seed: A.seed || 5, squash: 1.4,
        mask: "linear-gradient(180deg, transparent, #000 35%, #000 55%, transparent 92%)" }));
      C.appendChild(html(`<div style="position:absolute;left:${P}px;right:${P}px;top:${P}px;bottom:${P}px;display:flex;flex-direction:column">
        <div class="eyebrow" style="--eyebrow:${Math.round(Math.min(W, H) * .028)}px"><span class="dot"></span>${A.eyebrow}</div>
        <h2 class="display" style="font-size:${A.fs || Math.round(land ? H * .15 : W * .13)}px;margin-top:${Math.min(W, H) * .07}px">${A.title}</h2>
        ${A.lede ? `<p class="lede" style="font-size:${Math.round(Math.min(W, H) * .045)}px;margin-top:${Math.min(W, H) * .05}px;max-width:${W * .7}px;color:var(--muted)">${A.lede}</p>` : ""}
        ${A.spec ? `<div style="margin-top:auto;margin-bottom:${Math.min(W, H) * .08}px">${SPEC[A.spec](A.u || Math.min(W, H) / 42)}</div>` : ""}
        <div style="margin-top:${A.spec ? 0 : "auto"};display:flex;justify-content:space-between;align-items:center">${lockup(Math.round(Math.min(W, H) * .06))}
        <span class="meta" style="--meta:${Math.round(Math.min(W, H) * .026)}px">${A.meta || ""}</span></div></div>`));
    },
    // banner strip (X header, LinkedIn): field across, lockup + line on the right of the avatar zone
    banner() {
      C.appendChild(glow(W * .72, H * .5, H * 2.4, 140));
      C.appendChild(tiles({ x: -10, y: -10, w: W + 20, h: H + 20, cell: Math.round(H / 11), gap: Math.round(H / 42), fx: .86, fy: .5, sig: .15, seed: A.seed || 21,
        mask: "linear-gradient(90deg, transparent 72%, #000 90%)" }));
      C.appendChild(html(`<div style="position:absolute;left:${W * A.textX}px;top:50%;transform:translateY(-50%)">
        <h2 class="display" style="font-size:${Math.round(H * .17)}px;">${A.title}</h2>
        <div class="meta" style="--meta:${Math.round(H * .045)}px;margin-top:${H * .08}px">${A.meta}</div></div>`));
    },
    // mosaic: real showcase renders on a tilted wall, words on top-left
    mosaic() {
      const land = W > H, P = Math.round(Math.min(W, H) * .085);
      const imgs = A.images || [];
      const cols = A.cols || (land ? 4 : 3), gap = Math.round(Math.min(W, H) * .022);
      const wallW = W * (A.wall || 1.35);
      const cw = (wallW - gap * (cols - 1)) / cols;
      const col = Array.from({ length: cols }, () => []);
      imgs.forEach((src, i) => col[i % cols].push(src));
      const wall = html(`<div style="position:absolute;left:${A.wallX ?? W * .3}px;top:${A.wallY ?? -H * .25}px;display:flex;gap:${gap}px;transform:rotate(${A.rot ?? -8}deg);transform-origin:0 0">
        ${col.map((c, k) => `<div style="display:flex;flex-direction:column;gap:${gap}px;width:${cw}px;margin-top:${(k % 2) * cw * .35}px">
          ${c.map(src => `<img src="${src}" style="width:100%;display:block;border-radius:${Math.round(cw * .035)}px;box-shadow:0 30px 60px -20px rgb(0 0 0 / .55),0 0 0 1px var(--rule)">`).join("")}</div>`).join("")}</div>`);
      C.appendChild(wall);
      C.appendChild(html(`<div style="position:absolute;inset:0;background:linear-gradient(${land ? "100deg" : "180deg"}, var(--bg) ${land ? 30 : 30}%, color-mix(in oklab, var(--bg) 60%, transparent) ${land ? 46 : 46}%, transparent ${land ? 62 : 62}%)"></div>`));
      C.appendChild(html(`<div style="position:absolute;left:${P}px;top:${P}px;bottom:${P}px;width:${land ? W * .4 : W - 2 * P}px;display:flex;flex-direction:column">
        <div class="eyebrow" style="--eyebrow:${Math.round(Math.min(W, H) * .026)}px"><span class="dot"></span>${A.eyebrow}</div>
        <h2 class="display" style="font-size:${A.fs || Math.round(land ? H * .12 : W * .11)}px;margin-top:${Math.min(W, H) * .06}px">${A.title}</h2>
        ${A.lede ? `<p class="lede" style="font-size:${Math.round(Math.min(W, H) * .04)}px;margin-top:${Math.min(W, H) * .04}px">${A.lede}</p>` : ""}
        <div style="margin-top:auto;display:flex;align-items:center;gap:${P * .4}px">${lockup(Math.round(Math.min(W, H) * .052))}<span class="meta" style="--meta:${Math.round(Math.min(W, H) * .024)}px">${A.meta || ""}</span></div></div>`));
    },
    avatar() {
      const m = Math.round(W * (A.markScale || .46));
      C.appendChild(html(`<div style="position:absolute;inset:0;display:grid;place-items:center;color:var(--fg)">${mark(m)}</div>`));
    },
    // how it works: three steps
    steps() {
      const P = Math.round(H * .11), u = H / 34;
      C.appendChild(html(`<div style="position:absolute;left:${P}px;right:${P}px;top:${P}px;display:flex;justify-content:space-between;align-items:baseline">
        <h2 class="display" style="font-size:${Math.round(H * .1)}px">${A.title}</h2><span class="meta" style="--meta:${Math.round(u * .95)}px">${A.meta}</span></div>`));
      const col = (n, t, b, viz) => `<div style="display:flex;flex-direction:column;gap:${u * .9}px">
        <div style="height:${H * .3}px;display:flex;align-items:flex-end">${viz}</div>
        <div class="rule"></div>
        <div style="display:flex;gap:${u * .8}px;align-items:baseline"><span class="num" style="--num:${u * 1.05}px">${n}</span><span style="font-size:${u * 1.75}px;font-weight:600;letter-spacing:-.03em">${t}</span></div>
        <p class="lede" style="font-size:${u * 1.2}px;max-width:${W * .25}px">${b}</p></div>`;
      const q = `<div style="display:flex;flex-direction:column;gap:${u * .5}px;width:100%">${["Who is it for?", "Where does it run?", "How should it feel?"].map((t, i) => `<span class="pill" style="font-size:${u * .95}px;align-self:flex-start;${i === 2 ? "background:var(--accent);color:#fffaf7;border-color:transparent" : ""}">${t}</span>`).join("")}</div>`;
      const z = `<div style="display:flex;gap:${u * .45}px;align-items:flex-end;width:100%">${[.3, .5, .72, 1].map((h, i) => `<span style="flex:1;height:${H * .26 * h}px;border-radius:${[0, 6, 14, 999][i]}px ${[0, 6, 14, 999][i]}px 4px 4px;background:${i === 3 ? "var(--accent)" : "var(--tile)"};box-shadow:inset 0 0 0 1px var(--tile-line)"></span>`).join("")}</div>`;
      const f = `<div class="mono" style="font-size:${u * 1}px;line-height:1.7;color:var(--muted);width:100%">${["tokens/", "build/css · theme", "DESIGN.md", "decisions.md"].map((t, i) => `<div style="display:flex;justify-content:space-between;border-bottom:1px solid var(--rule)"><span style="color:${i == 2 ? "var(--fg)" : "inherit"}">${t}</span><span style="color:var(--accent-text)">✓</span></div>`).join("")}</div>`;
      C.appendChild(html(`<div style="position:absolute;left:${P}px;right:${P}px;bottom:${P}px;display:grid;grid-template-columns:repeat(3,1fr);gap:${P * .7}px">
        ${col("01", "Answer five questions", "Plain words, one at a time. A recommendation with its reason every time.", q)}
        ${col("02", "Zoom in where it matters", "Stop at a sketch, or go deeper on color, type or motion. Only where you want.", z)}
        ${col("03", "Keep it in files", "Tokens, CSS and a DESIGN.md your code and your AI follow from then on.", f)}</div>`));
    },
  };
  L[A.layout]();
  if (A.grain !== false) C.appendChild(html(`<div class="grain"></div>`));
})();
