// OpenDesigner site: copy buttons, live GitHub numbers, showcase tag filters and the gallery lightbox. Pages read fine without it.
(function () {
  document.querySelectorAll("[data-copy], [data-copy-text]").forEach(function (btn) {
    var label = btn.textContent;
    btn.addEventListener("click", function () {
      var text = btn.getAttribute("data-copy-text") || (btn.parentElement.querySelector("code") || {}).innerText || "";
      var done = function () { btn.textContent = "Copied"; setTimeout(function () { btn.textContent = label; }, 1600); };
      if (navigator.clipboard) navigator.clipboard.writeText(text).then(done, function () {}); else done();
    });
  });

  if (document.querySelector("[data-stars]")) {
    fetch("https://api.github.com/repos/ckryptickunal/OpenDesigner", { headers: { Accept: "application/vnd.github+json" } })
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (j) {
        if (!j) return;
        var set = function (sel, v) { document.querySelectorAll(sel).forEach(function (el) { el.textContent = v; }); };
        set("[data-stars]", j.stargazers_count.toLocaleString("en"));
        set("[data-forks]", j.forks_count.toLocaleString("en"));
        set("[data-issues]", j.open_issues_count.toLocaleString("en"));
        set("[data-pushed]", (j.pushed_at || "").slice(0, 10));
      })
      .catch(function () {});
  }

  // tabs (home: examples and install). Without this script every panel shows, one after another.
  document.querySelectorAll("[data-tabs]").forEach(function (box) {
    var tabs = Array.prototype.slice.call(box.querySelectorAll('[role="tab"]'));
    var pick = function (t, focus, animate) {
      tabs.forEach(function (x) {
        var on = x === t;
        x.setAttribute("aria-selected", on ? "true" : "false");
        x.tabIndex = on ? 0 : -1;
        var panel = document.getElementById(x.getAttribute("aria-controls"));
        if (!panel) return;
        var was = panel.hidden;
        panel.hidden = !on;
        panel.classList.remove("is-entering");
        if (on && was && animate) { void panel.offsetWidth; panel.classList.add("is-entering"); }
      });
      if (focus) t.focus();
    };
    tabs.forEach(function (t, i) {
      t.addEventListener("click", function (e) { pick(t, false, e.detail > 0); });  // e.detail is 0 for Enter or Space: keyboard stays instant
      t.addEventListener("keydown", function (e) {
        var j = e.key === "ArrowRight" ? i + 1 : e.key === "ArrowLeft" ? i - 1 : e.key === "Home" ? 0 : e.key === "End" ? tabs.length - 1 : null;
        if (j === null) return;
        e.preventDefault();
        pick(tabs[(j + tabs.length) % tabs.length], true);
      });
    });
    pick(tabs.filter(function (t) { return t.getAttribute("aria-selected") === "true"; })[0] || tabs[0], false, false);
  });

  // home headline, "look like it belongs together": the letters arrive a little loose and settle together, as if tracking
  // tightened. They start 70% of the way home (owner, 2026-10-15: the first version moved too much) and take 0.7 s.
  // Each line gathers on its own centre, so the centred axis never moves. Transform and opacity only (Web Animations),
  // once per load. The original markup comes back at the end, so kerning and text selection are exactly as before.
  var title = document.querySelector(".h-title.g-wait");
  if (title && title.animate && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    var gather = function () {
      var original = title.innerHTML, chars = [], texts = [], kerned = [];
      (function walk(node) {
        Array.prototype.slice.call(node.childNodes).forEach(function (n) {
          if (n.nodeType === 1) { if (!n.classList.contains("h-eyebrow")) walk(n); }  // the small category line above stays still
          else if (n.nodeType === 3 && (n.textContent.trim() || texts.length)) texts.push(n);
        });
      })(title);
      // where each letter sits in the real, kerned text, measured before splitting
      texts.forEach(function (n) {
        var r = document.createRange(), at = 0;
        Array.from(n.textContent).forEach(function (ch) {
          r.setStart(n, at); r.setEnd(n, at + ch.length); at += ch.length;
          if (!/\s/.test(ch)) kerned.push(r.getBoundingClientRect().left);
        });
      });
      texts.forEach(function (n) {
        var frag = document.createDocumentFragment();
        n.textContent.split(/(\s+)/).forEach(function (part) {
          if (!part) return;
          if (/^\s+$/.test(part)) return frag.appendChild(document.createTextNode(part));
          var w = document.createElement("span"); w.className = "g-w";
          Array.from(part).forEach(function (ch) { var c = document.createElement("span"); c.className = "g-c"; c.textContent = ch; w.appendChild(c); chars.push(c); });
          frag.appendChild(w);
        });
        n.parentNode.replaceChild(frag, n);
      });
      // separate boxes lose the font's kerning; give each pair its kerning back as a margin, so the split headline wraps and sits
      // exactly like the real one and the swap back at the end is invisible
      var split = chars.map(function (c) { return c.getBoundingClientRect().left; });
      chars.forEach(function (c, i) {
        if (i + 1 < chars.length && chars[i + 1].parentNode === c.parentNode) c.style.marginRight = ((kerned[i + 1] - kerned[i]) - (split[i + 1] - split[i])).toFixed(2) + "px";
      });
      // group the letters into lines, counting each space as one step, the way letter-spacing does
      var lines = [], top = null, prevWord = null;
      chars.forEach(function (c) {
        var t = Math.round(c.offsetTop);
        if (t !== top) { lines.push([]); top = t; prevWord = null; }
        var line = lines[lines.length - 1], step = line.length ? line[line.length - 1].i + 1 + (c.parentNode !== prevWord ? 1 : 0) : 0;
        line.push({ el: c, i: step }); prevWord = c.parentNode;
      });
      var gap = parseFloat(getComputedStyle(title).fontSize) * 0.048, ease = "cubic-bezier(0.23, 1, 0.32, 1)", runs = [];
      lines.forEach(function (line, li) {
        var mid = line[line.length - 1].i / 2;
        line.forEach(function (ch) {
          runs.push(ch.el.animate([{ transform: "translateX(" + ((ch.i - mid) * gap).toFixed(1) + "px)", opacity: 0 }, { opacity: 1, offset: 0.4 }, { transform: "none", opacity: 1 }],
            { duration: 700, delay: 60 + li * 50, easing: ease, fill: "both" }).finished);
        });
      });
      runs.push(title.animate([{ filter: "blur(2px)" }, { filter: "blur(0)" }], { duration: 500, delay: 60, easing: ease, fill: "backwards" }).finished);
      title.classList.remove("g-wait");
      title.style.animation = "none";
      Promise.all(runs).then(function () { title.innerHTML = original; }, function () {});  // the CSS rise stays off, or it would replay
    };
    // measure only in the real font, both weights (preloaded, so usually there at once). If it takes longer than 400 ms, skip the
    // effect and let the title rise as usual: letters measured in a fallback font would jump when the font swaps in.
    var strong = title.querySelector("strong"), late = false, wait = setTimeout(function () { late = true; title.classList.remove("g-wait"); }, 400);
    if (document.fonts && document.fonts.load) {
      var font = function (el) { var c = getComputedStyle(el); return c.fontStyle + " " + c.fontWeight + " " + c.fontSize + " " + c.fontFamily; };
      Promise.all([document.fonts.load(font(title)), document.fonts.load(font(strong || title))])
        .then(function () { if (!late) { clearTimeout(wait); gather(); } }, function () {});
    } else { clearTimeout(wait); title.classList.remove("g-wait"); }
  }

  // reveal on scroll: content below the fold fades and rises once as it comes into view. Content already on screen is left alone,
  // and with reduced motion nothing is hidden at all. Printing shows everything.
  window.addEventListener("beforeprint", function () { document.querySelectorAll(".reveal-wait").forEach(function (el) { el.classList.remove("reveal-wait"); }); });
  if ("IntersectionObserver" in window && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    var groups = ".h-head, .h-steps > li, .who > a, .bento > article, .craft > a, .ex-grid > a, .demo, .tabs:not(.demo), .h-split > *, .faq, .h-zoom, .h-end-card, .home .fig:not(.home-hero)";
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target;
        el.classList.remove("reveal-wait");
        io.unobserve(el);
        setTimeout(function () { el.classList.remove("reveal"); el.style.removeProperty("--i"); }, 900);  // hand back to hover transitions
      });
    }, { rootMargin: "0px 0px -8% 0px" });
    document.querySelectorAll(".home " + groups.split(", ").join(", .home ")).forEach(function (el) {
      if (el.getBoundingClientRect().top < window.innerHeight) return;
      var sibs = el.parentElement ? Array.prototype.indexOf.call(el.parentElement.children, el) : 0;
      el.style.setProperty("--i", String(Math.min(sibs, 5)));
      el.classList.add("reveal", "reveal-wait");
      io.observe(el);
    });
  }

  // showcase: a piece with several frames scrolls between them in its own frame (scroll snap, so touch swipes natively).
  // Chevrons step one frame; the longer dot glides to the frame that is showing; frames out of view leave the tab order.
  var calm = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  document.querySelectorAll("[data-slides]").forEach(function (box) {
    var track = box.querySelector(".sl-track"), slides = Array.prototype.slice.call(track.children), at = -1,
        prev = box.querySelector(".sl-prev"), next = box.querySelector(".sl-next"), pill = box.closest(".piece").querySelector(".sl-pill"), status = box.querySelector(".sl-status");
    var show = function (i) {
      if (i === at) return;
      at = i;
      slides.forEach(function (s, n) { s.inert = n !== i; });
      var lost = document.activeElement === prev || document.activeElement === next;
      prev.disabled = i === 0; next.disabled = i === slides.length - 1;
      if (lost && document.activeElement.disabled) (prev.disabled ? next : prev).focus();  // a chevron that disappears hands focus to the other one
      pill.style.transform = "translateX(" + i * 16 + "px)";
      status.textContent = "Frame " + (i + 1) + " of " + slides.length;
    };
    var go = function (i) { track.scrollTo({ left: i * track.clientWidth, behavior: calm ? "auto" : "smooth" }); };
    prev.addEventListener("click", function () { go(Math.max(0, at - 1)); });
    next.addEventListener("click", function () { go(Math.min(slides.length - 1, at + 1)); });
    var frame = 0;
    track.addEventListener("scroll", function () {
      cancelAnimationFrame(frame);
      frame = requestAnimationFrame(function () { show(Math.round(track.scrollLeft / track.clientWidth)); });
    }, { passive: true });
    show(0);
  });

  // showcase: tag filters
  var filters = document.querySelector(".filters");
  if (filters) {
    filters.addEventListener("click", function (e) {
      var b = e.target.closest(".filter");
      if (!b) return;
      var tag = b.getAttribute("data-tag");
      filters.querySelectorAll(".filter").forEach(function (x) { x.classList.toggle("is-on", x === b); });
      document.querySelectorAll(".piece").forEach(function (p) {
        var tags = (p.getAttribute("data-tags") || "").split(" ");
        p.hidden = !!tag && tags.indexOf(tag) < 0;
      });
      document.querySelectorAll(".show-cat").forEach(function (s) {
        s.hidden = !s.querySelector(".piece:not([hidden])");
      });
    });
  }

  // showcase: lightbox over <dialog>, with keyboard and swipe
  var lb = document.getElementById("lightbox");
  var links = Array.prototype.slice.call(document.querySelectorAll("a[data-gallery]"));
  if (lb && links.length && typeof lb.showModal === "function") {
    var img = lb.querySelector(".lb-img"), title = lb.querySelector(".lb-title"), blurb = lb.querySelector(".lb-blurb"),
        tags = lb.querySelector(".lb-tags"), open = lb.querySelector(".lb-open"), current = 0;
    var visible = function () { return links.filter(function (a) { return !a.closest(".piece").hidden; }); };
    var show = function (i) {
      var list = visible(); if (!list.length) return;
      current = (i + list.length) % list.length;
      var a = list[current];
      img.src = a.getAttribute("href"); img.alt = a.getAttribute("data-title") || "";
      title.textContent = a.getAttribute("data-title") || ""; blurb.textContent = a.getAttribute("data-blurb") || "";
      tags.textContent = a.getAttribute("data-tags") || ""; open.href = a.getAttribute("href");
      [list[(current + 1) % list.length], list[(current - 1 + list.length) % list.length]].forEach(function (n) { var p = new Image(); p.src = n.getAttribute("href"); });
    };
    links.forEach(function (a) {
      a.addEventListener("click", function (e) {
        e.preventDefault();
        show(visible().indexOf(a));
        lb.showModal();
        lb.querySelector(".lb-close").focus();
      });
    });
    lb.querySelector(".lb-prev").addEventListener("click", function () { show(current - 1); });
    lb.querySelector(".lb-next").addEventListener("click", function () { show(current + 1); });
    lb.querySelector(".lb-close").addEventListener("click", function () { lb.close(); });
    lb.addEventListener("click", function (e) { if (e.target === lb || e.target.classList.contains("lb-stage")) lb.close(); });
    lb.addEventListener("keydown", function (e) {
      if (e.key === "ArrowRight") { show(current + 1); e.preventDefault(); }
      if (e.key === "ArrowLeft") { show(current - 1); e.preventDefault(); }
    });
    var x0 = null;
    lb.addEventListener("touchstart", function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener("touchend", function (e) {
      if (x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0; x0 = null;
      if (Math.abs(dx) > 48) show(dx < 0 ? current + 1 : current - 1);
    }, { passive: true });
  }
})();

/* Home #before-after: the audit as it happens, on the demo pages themselves. Both pages are live HTML in shadow roots, laid
   out at their design width and scaled to the stage, so every box is measured on the page as drawn. Plays once when the
   section comes into view: a scan finds each issue in the order it meets them (a dashed box, its number and one line), then
   the fix sweeps down and the fixed page builds itself as the line passes (bars grow, the sparkline draws, totals count up,
   rows and labels arrive) while a chip carries each token from the Merriweft card to its place and each box becomes a check.
   Today / Audit / Fixed stop it and show that state at once; Replay plays it again. With reduced motion it never plays by
   itself. On a small stage a camera shows part of the page at the size it reads on a desktop and moves the view: to each
   issue, out for the sweep, then onto the Collected chart (making.md section 6). Web Animations only: transform, opacity,
   clip-path. */
(function () {
  "use strict";
  var root = document.querySelector("[data-au]");
  if (!root || !root.animate || !window.Promise) return;
  var stage = root.querySelector(".au-stage"), cam = stage.querySelector(".au-cam"), after = stage.querySelector(".au-after");
  var pb = stage.querySelector(".au-page.b"), pa = stage.querySelector(".au-page.a");
  if (!pb || !pa || !pb.shadowRoot || !pa.shadowRoot) return;  // the list beside the page still says what the audit found
  var D = JSON.parse(document.getElementById("au-data").textContent);
  var EASE = "cubic-bezier(0.23, 1, 0.32, 1)", MOVE = "cubic-bezier(0.77, 0, 0.175, 1)";
  var card = stage.querySelector(".au-tokens"), line = stage.querySelector(".au-line"), tag = line.querySelector(".au-tag");
  var callout = stage.querySelector(".au-callout"), status = root.querySelector(".au-status"), cap = root.querySelector(".au-cap");
  var empty = root.querySelector(".au-empty"), replay = root.querySelector(".au-replay");
  var tabs = Array.prototype.slice.call(root.querySelectorAll('[role="tab"]'));
  var by = {}, run = 0, anims = [], timers = [], undo = [], busy = false, N = D.marks.length;
  var KVIEW = 0.58, Z = 1, camW = 0, camH = 0, cur = "", spot = {}, view = "today";  // KVIEW: the page's scale on a desktop stage
  var all = function (sr, sel) { return Array.prototype.slice.call(sr.querySelectorAll(sel)); };
  D.marks.forEach(function (m) {
    by[m.n] = { m: m, mk: stage.querySelector('.au-mk[data-n="' + m.n + '"]'), ok: stage.querySelector('.au-ok[data-n="' + m.n + '"]'),
                row: root.querySelector('.au-list li[data-n="' + m.n + '"]') };
  });
  root.classList.add("on");

  function box(sr, sel) {  // every match as one box, in the camera's pixels (the page fitted to the stage), a little larger
    if (!sel) return null;
    var c = cam.getBoundingClientRect(), sx = c.width / cam.offsetWidth, sy = c.height / cam.offsetHeight, pad = 4 / Z;
    var x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
    all(sr, sel).forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (!r.width || !r.height) return;
      x0 = Math.min(x0, r.left); y0 = Math.min(y0, r.top); x1 = Math.max(x1, r.right); y1 = Math.max(y1, r.bottom);
    });
    if (x1 < x0) return null;
    return { x: (x0 - c.left) / sx - pad, y: (y0 - c.top) / sy - pad, w: (x1 - x0) / sx + 2 * pad, h: (y1 - y0) / sy + 2 * pad };
  }
  function centre(r) { return [r.x + r.w / 2, r.y + r.h / 2]; }
  function put(el, r) { el.style.left = r.x + "px"; el.style.top = r.y + "px"; el.style.width = r.w + "px"; el.style.height = r.h + "px"; }
  function ink(sr) {  // what a check must never cover: every line of text, control, icon and chart on the page, in the camera's pixels
    var c = cam.getBoundingClientRect(), sx = c.width / cam.offsetWidth, sy = c.height / cam.offsetHeight, out = [];
    var add = function (r) { if (r.width > 2 && r.height > 2) out.push({ x: (r.left - c.left) / sx, y: (r.top - c.top) / sy, w: r.width / sx, h: r.height / sy }); };
    var walk = document.createTreeWalker(sr, NodeFilter.SHOW_TEXT), range = document.createRange(), n;
    while ((n = walk.nextNode())) {
      if (!/\S/.test(n.data)) continue;
      var p = n.parentElement && n.parentElement.getBoundingClientRect();
      if (p && (p.width <= 2 || p.height <= 2)) continue;  // text only screen readers get takes no room
      range.selectNodeContents(n);
      Array.prototype.forEach.call(range.getClientRects(), add);
    }
    all(sr, "button, .search, .avatar, .pill, svg, .weeks, .meter, .days").forEach(function (el) { add(el.getBoundingClientRect()); });
    return out;
  }
  function gutter(b, taken) {  // a check goes where it covers nothing: on its box's top-left corner, else along its top edge
    // (a column's is the line under its header), else in the gutter above, else on the other corner, beside, an edge, below
    var r = b.a, el = b.ok.firstElementChild, s = el.offsetWidth, h = s / 2 + 3 / Z, o = s / 2 + 2 / Z;  // h: half the badge and some air
    if (!(s > 0)) return;  // a hidden stage has no size to place anything in
    var x0 = r.x, y0 = r.y, x1 = r.x + r.w, y1 = r.y + r.h, p = 4 / Z, spots = [[x0, y0], [x0 + p, y0 + p]], t;  // p: box() padding
    for (t = s; t < r.w; t += s / 2) spots.push([x0 + t, y0 + p]);
    for (t = o; t <= r.w - o; t += s / 2) spots.push([x0 + t, y0 - o]);
    spots.push([x1, y0], [x1 - p, y0 + p]);
    for (t = o; t <= r.h - o; t += s / 2) spots.push([x0 - o, y0 + t], [x1 + o, y0 + t]);
    for (t = s; t < r.h; t += s / 2) spots.push([x0, y0 + t], [x1, y0 + t]);
    for (t = o; t <= r.w - o; t += s / 2) spots.push([x0 + t, y1 + o]);
    spots.push([x0, y1], [x1, y1]);
    var cover = function (p) {  // how much of the page the badge would hide there; off the page counts as hidden
      var ax = p[0] - h, ay = p[1] - h, a = 0;
      if (ax < 0 || ay < 0 || ax + 2 * h > camW || ay + 2 * h > camH) return Infinity;
      taken.forEach(function (q) { a += Math.max(0, Math.min(ax + 2 * h, q.x + q.w) - Math.max(ax, q.x)) * Math.max(0, Math.min(ay + 2 * h, q.y + q.h) - Math.max(ay, q.y)); });
      return a;
    };
    var best = spots[0], least = Infinity, graze = s * s / 100;  // the air around a check may graze a line by a pixel
    for (var i = 0; i < spots.length && least > graze; i++) { var a = cover(spots[i]); if (a < least) { least = a; best = spots[i]; } }
    el.style.left = best[0] - r.x - s / 2 + "px"; el.style.top = best[1] - r.y - s / 2 + "px";
    taken.push({ x: best[0] - s / 2, y: best[1] - s / 2, w: s, h: s });  // and no two checks on one spot
  }
  function fit() {  // fit both pages to the stage's width, choose the camera's zoom, and measure every box
    var W = stage.clientWidth, k = W / D.width, ph = Math.max(pb.offsetHeight, pa.offsetHeight);
    Z = KVIEW / k > 1.15 ? KVIEW / k : 1;
    camW = W; camH = ph * k;
    stage.style.setProperty("--k", k);
    stage.style.aspectRatio = Z > 1 ? "4 / 5" : D.width + " / " + ph;  // not a height: that would size the width too
    cam.style.height = camH + "px";
    cam.style.setProperty("--zs", 1 / Z);  // marks and the line keep their size on screen at the camera's zoom
    D.marks.forEach(function (m) {
      var b = by[m.n];
      b.r = box(pb.shadowRoot, m.sel) || { x: 0, y: 0, w: 0, h: 0 };
      b.a = box(pa.shadowRoot, m.asel) || b.r;
      put(b.mk, b.r); put(b.ok, b.a);
    });
    var taken = ink(pa.shadowRoot);
    D.marks.forEach(function (m) { gutter(by[m.n], taken); });
    var t = box(pa.shadowRoot, ".t-cash"), g = groups()[0];
    spot = { today: [0, 0], audit: g ? centre(by[g[0].n].r) : [0, 0], fixed: t ? [t.x - 8 / Z + W / Z / 2, t.y + t.h / 2] : [0, 0] };  // the chart's left edge in view
  }
  function shot(c, z) {  // the camera transform that centres the page's point c at zoom z, kept inside the page
    var W = stage.clientWidth, H = stage.clientHeight;
    var x = Math.min(0, Math.max(W - camW * z, W / 2 - c[0] * z)), y = Math.min(0, Math.max(H - camH * z, H / 2 - c[1] * z));
    return "translate(" + x + "px, " + y + "px) scale(" + z + ")";
  }
  function zFor(r) {  // close enough to read, and out far enough that the whole box shows
    return Math.max(1, Math.min(Z, 0.94 * stage.clientWidth / r.w, 0.9 * stage.clientHeight / r.h));
  }
  function aim(c, z, ms) {  // move the camera; with the whole page on the stage there is nothing to move
    if (Z === 1) return;
    var to = shot(c, z || Z);
    if (ms && cur) A(cam, [{ transform: cur }, { transform: to }], { duration: ms, easing: MOVE });
    cur = to;
  }

  function A(el, kf, o) { var a = el.animate(kf, Object.assign({ fill: "forwards" }, o)); anims.push(a); return a; }
  function later(fn, ms) { timers.push(setTimeout(fn, ms)); }
  function wait(ms, id) { return new Promise(function (ok, no) { later(function () { id === run ? ok() : no("stopped"); }, ms); }); }
  function stop() {
    run++; busy = false;
    timers.forEach(clearTimeout); timers = [];
    anims.forEach(function (a) { a.cancel(); }); anims = [];
    undo.forEach(function (fn) { fn(); }); undo = [];
    Array.prototype.slice.call(stage.querySelectorAll(".au-chip")).forEach(function (c) { c.remove(); });
  }
  function select(view) {
    tabs.forEach(function (t) { var on = t.getAttribute("data-view") === view; t.setAttribute("aria-selected", on ? "true" : "false"); t.tabIndex = on ? 0 : -1; });
  }
  function say(html) { status.innerHTML = html; }
  function caption(m, ok) {
    if (!m) { cap.hidden = true; return; }
    cap.hidden = false;
    cap.className = "au-cap" + (ok ? " ok" : "");
    cap.innerHTML = "<b>" + m.n + "</b><span>" + (ok ? m.token : m.short) + "</span>";
  }
  function reset(v) {
    view = v;
    cam.style.transform = Z > 1 ? shot(spot[v], Z) : "";
    cur = cam.style.transform;
    select(view);
    after.style.clipPath = view === "fixed" ? "inset(0 0 0 0)" : "inset(0 0 100% 0)";
    line.style.opacity = "0"; callout.style.opacity = "0"; card.style.opacity = "0";
    empty.hidden = view !== "today";
    D.marks.forEach(function (m) {
      var b = by[m.n];
      b.shown = view === "audit";
      b.mk.style.opacity = view === "audit" ? "1" : "0";
      b.ok.style.opacity = view === "fixed" ? "1" : "0";
      b.row.hidden = view === "today";
      b.row.classList.toggle("done", view === "fixed");
    });
    say(view === "today" ? "The page as it is today."
      : view === "audit" ? "<b>" + N + " issues</b> found on this page."
      : "<b>Fixed " + N + " of " + N + ".</b> Every color, size and corner now comes from Merriweft's tokens.");
    caption(null);
  }
  function show(view) { stop(); reset(view); }
  function place(m) {  // beside its box, above it when there is room, never over a box already found
    var p = by[m.n].r, W = stage.clientWidth, H = stage.clientHeight;
    callout.innerHTML = "<b>" + m.n + "</b><span>" + m.short + "</span>";
    callout.style.left = "0px"; callout.style.top = "0px";
    var cw = callout.offsetWidth, ch = callout.offsetHeight, left = Math.min(Math.max(6, p.x), W - cw - 6);
    var hits = function (t) {
      return D.marks.some(function (o) {
        var q = by[o.n].r;
        return o.n !== m.n && by[o.n].shown && left < q.x + q.w && left + cw > q.x && t < q.y + q.h && t + ch > q.y;
      });
    };
    var spots = [p.y - ch - 16, p.y + p.h + 12, p.y + 10].filter(function (t) { return t >= 6 && t + ch <= H - 6; });
    var top = spots.filter(function (t) { return !hits(t); })[0];
    if (top === undefined) top = spots[0] !== undefined ? spots[0] : 6;
    callout.style.left = left + "px"; callout.style.top = top + "px";
  }
  function groups() {  // issues at about the same height are found together, left to right
    var out = [];
    D.marks.slice().sort(function (a, b) { return by[a.n].r.y - by[b.n].r.y || by[a.n].r.x - by[b.n].r.x; }).forEach(function (m) {
      var g = out[out.length - 1];
      if (g && Math.abs(by[g[0].n].r.y - by[m.n].r.y) < camH * 0.02) g.push(m); else out.push([m]);
    });
    return out;
  }
  function fly(m, b) {  // a chip leaves the token card and lands where the fix goes; the check appears as it lands
    var p = b.a, H = stage.clientHeight, small = Z > 1 || stage.clientWidth < 520;
    var land = function () { A(b.ok, [{ opacity: 0, transform: "scale(0.9)" }, { opacity: 1, transform: "scale(1)" }], { duration: 240, easing: EASE }); };
    if (small) { land(); return; }
    var chip = document.createElement("span");
    chip.className = "au-chip";
    chip.textContent = "✓ " + m.token;
    stage.appendChild(chip);
    var x0 = 24, y0 = H - 72, x1 = Math.min(Math.max(6, p.x + 10), stage.clientWidth - chip.offsetWidth - 6), y1 = Math.max(6, p.y - 30);
    A(chip, [{ transform: "translate(" + x0 + "px," + y0 + "px) scale(0.96)", opacity: 0 },
             { transform: "translate(" + x0 + "px," + (y0 - 8) + "px) scale(1)", opacity: 1, offset: 0.15 },
             { transform: "translate(" + x1 + "px," + y1 + "px) scale(1)", opacity: 1 }], { duration: 560, easing: MOVE });
    later(function () { land(); A(chip, [{ opacity: 1 }, { opacity: 0 }], { duration: 200, delay: 240, easing: "ease" }); }, 560);
    later(function () { chip.remove(); }, 1100);
  }

  // How the fixed page builds itself as the line reaches each part: [selector, motion, stagger (ms), delay after reached (ms)]
  var BUILD = [
    [".top .nav a, .search, .avatar", "fade", 30, 0], [".head .h1, .head .sub", "rise", 60, 0], [".acts .btn", "pop", 70, 60],
    [".money .tile", "rise", 80, 0], [".wk .b", "grow", 90, 140], [".wk .v", "rise", 90, 420], [".avg", "widen", 0, 640],
    [".xs span, .keys li", "fade", 40, 320], [".spark", "draw", 0, 180], [".meter i", "widen", 180, 220],
    [".rows li, .late-list li", "rise", 70, 260], [".t-late .btn", "pop", 0, 480], [".day i", "grow", 40, 180], [".next", "fade", 0, 460],
    [".bar .seg, .bar .count", "fade", 60, 0], ["thead th", "fade", 25, 0], ["tbody tr", "rise", 0, 0], [".pill", "pop", 0, 160]
  ];
  var MOTION = {
    fade: { o: 260 }, rise: { o: 260, t: ["translateY(8px)", "translateY(0)"], d: 460 }, pop: { o: 220, t: ["scale(0.94)", "scale(1)"], d: 320 },
    grow: { t: ["scaleY(0)", "scaleY(1)"], d: 680, origin: "50% 100%" }, widen: { t: ["scaleX(0)", "scaleX(1)"], d: 620, origin: "0 50%" },
    draw: { clip: ["inset(-4px 100% -4px -4px)", "inset(-4px -4px -4px -4px)"], d: 1000 }
  };
  function build(id, SWEEP) {
    var c = cam.getBoundingClientRect();
    var reach = function (el) { return Math.max(0, (el.getBoundingClientRect().top - c.top) / c.height * SWEEP); };
    var F = pa.shadowRoot;
    BUILD.forEach(function (step) {
      var mo = MOTION[step[1]];
      all(F, step[0]).forEach(function (el, i) {
        var at = reach(el) + step[3] + i * step[2];
        if (mo.o) A(el, [{ opacity: 0 }, { opacity: 1 }], { duration: mo.o, delay: at, easing: "ease", fill: "both" });
        if (mo.origin) { var was = el.style.transformOrigin; el.style.transformOrigin = mo.origin; undo.push(function () { el.style.transformOrigin = was; }); }
        if (mo.t) A(el, [{ transform: mo.t[0] }, { transform: mo.t[1] }], { duration: mo.d, delay: at, easing: EASE, fill: "both", composite: "add" });
        if (mo.clip) A(el, [{ clipPath: mo.clip[0] }, { clipPath: mo.clip[1] }], { duration: mo.d, delay: at, easing: MOVE, fill: "both" });
      });
    });
    all(F, ".money .fig").forEach(function (el) {  // each total counts up to its value as its tile arrives
      var t = el.firstChild;
      if (!t || t.nodeType !== 3 || !/\d/.test(t.data)) return;
      var text = t.data, n = parseInt(text.replace(/\D/g, ""), 10), num = text.match(/[\d,]+/)[0];
      t.data = text.replace(num, "0");
      undo.push(function () { t.data = text; });
      later(function () {
        var t0 = performance.now();
        requestAnimationFrame(function step(now) {
          if (id !== run) return;
          var p = Math.min(1, (now - t0) / 900), e = 1 - Math.pow(1 - p, 3);
          t.data = text.replace(num, Math.round(n * e).toLocaleString("en-US"));
          if (p < 1) requestAnimationFrame(step);
        });
      }, reach(el) + 120);
    });
  }

  async function play() {
    stop();
    var id = run;
    reset("today");
    fit();
    busy = true;
    empty.hidden = true;
    var H = camH, y = 0;
    line.classList.remove("fix");
    tag.textContent = "Measuring contrast, sizes and spacing";
    say("Auditing the invoices page…");
    try {
      A(line, [{ opacity: 0 }, { opacity: 1 }], { duration: 200, easing: "ease" });
      await wait(300, id);
      var found = 0, gs = groups();
      for (var gi = 0; gi < gs.length; gi++) {
        var top = by[gs[gi][0].n].r.y;
        aim(centre(by[gs[gi][0].n].r), zFor(by[gs[gi][0].n].r), 620);
        A(line, [{ transform: "translateY(" + y + "px)" }, { transform: "translateY(" + top + "px)" }], { duration: 560, easing: MOVE });
        y = top;
        await wait(580, id);
        if (!found) select("audit");
        for (var k = 0; k < gs[gi].length; k++) {
          var m = gs[gi][k], b = by[m.n];
          if (k > 0 && Z > 1) {  // zoomed in, the next issue in a row can be off screen: go to it before showing it
            aim(centre(b.r), zFor(b.r), 520);
            await wait(560, id);
          }
          found++;
          b.shown = true;
          A(b.mk, [{ opacity: 0, clipPath: "inset(-16px 100% -16px -16px)" }, { opacity: 1, clipPath: "inset(-16px -16px -16px -16px)" }], { duration: 380, easing: EASE });
          A(b.mk.firstElementChild, [{ opacity: 0, transform: "scale(0.9)" }, { opacity: 1, transform: "scale(1)" }], { duration: 220, delay: 60, easing: EASE });
          b.row.hidden = false;
          A(b.row, [{ opacity: 0, transform: "translateY(6px)" }, { opacity: 1, transform: "translateY(0)" }], { duration: 240, easing: EASE });
          if (Z === 1) {  // the callout sits beside its box; zoomed in, the caption under the page says it
            place(m);
            A(callout, [{ opacity: 0, transform: "translateY(4px)" }, { opacity: 1, transform: "translateY(0)" }], { duration: 200, delay: 120, easing: EASE });
          }
          say("Found " + found + " of " + N + ": <b>" + m.title + "</b>");
          caption(m);
          await wait(1250, id);
          if (Z === 1) A(callout, [{ opacity: 1 }, { opacity: 0 }], { duration: 140, easing: "ease" });
        }
      }
      A(line, [{ transform: "translateY(" + y + "px)", opacity: 1 }, { transform: "translateY(" + H + "px)", opacity: 0 }], { duration: 520, easing: MOVE });
      caption(null);
      say("<b>" + N + " issues found.</b> Fixing them with Merriweft's design system…");
      A(card, [{ opacity: 0, transform: "translateY(6px)" }, { opacity: 1, transform: "translateY(0)" }], { duration: 260, delay: 300, easing: EASE });
      aim([camW / 2, camH / 2], Math.max(1, stage.clientHeight / camH), 760);  // out to see the whole sweep
      await wait(1000, id);

      var SWEEP = 3400, fixed = 0;
      line.classList.add("fix");
      tag.textContent = "Applying Merriweft's tokens";
      A(line, [{ opacity: 0, transform: "translateY(0)" }, { opacity: 1, transform: "translateY(0)" }], { duration: 160, easing: "ease" });
      await wait(180, id);
      A(line, [{ transform: "translateY(0)" }, { transform: "translateY(" + H + "px)" }], { duration: SWEEP, easing: "linear" });
      A(after, [{ clipPath: "inset(0 0 100% 0)" }, { clipPath: "inset(0 0 0% 0)" }], { duration: SWEEP, easing: "linear" });
      build(id, SWEEP);
      var row = -1, inRow = 0, rowY = -Infinity;  // fixes on one row land one after another, so their chips never overlap
      D.marks.slice().sort(function (a, b) { return Math.min(by[a.n].r.y, by[a.n].a.y) - Math.min(by[b.n].r.y, by[b.n].a.y); }).forEach(function (m) {
        var b = by[m.n], y0 = Math.min(b.r.y, b.a.y);
        if (y0 - rowY > H * 0.03) { row++; inRow = 0; rowY = y0; } else inRow++;
        var at = y0 / H * SWEEP + inRow * 760;
        later(function () { A(b.mk, [{ opacity: 1 }, { opacity: 0 }], { duration: 160, easing: "ease" }); }, b.r.y / H * SWEEP);  // the old page's box goes as the line passes it
        later(function () {
          if (id !== run) return;
          fixed++;
          fly(m, b);
          b.row.classList.add("done");
          say("Fixed " + fixed + " of " + N + ": <b>" + m.title + "</b>");
          caption(m, true);
          if (fixed === 1) select("fixed");
        }, at);
      });
      await wait(SWEEP + 2200, id);
      A(line, [{ opacity: 1 }, { opacity: 0 }], { duration: 200, easing: "ease" });
      A(card, [{ opacity: 1 }, { opacity: 0 }], { duration: 200, easing: "ease" });
      aim(spot.fixed, Z, 900);  // back in, onto the Collected chart
      await wait(Z > 1 ? 920 : 260, id);
      show("fixed");
    } catch (e) { /* a tab or Replay stopped it */ }
  }

  tabs.forEach(function (t, i) {
    t.addEventListener("click", function () { show(t.getAttribute("data-view")); });
    t.addEventListener("keydown", function (e) {
      var j = e.key === "ArrowRight" ? i + 1 : e.key === "ArrowLeft" ? i - 1 : e.key === "Home" ? 0 : e.key === "End" ? tabs.length - 1 : null;
      if (j === null) return;
      e.preventDefault();
      var next = tabs[(j + tabs.length) % tabs.length];
      next.focus(); show(next.getAttribute("data-view"));
    });
  });
  replay.addEventListener("click", play);
  D.marks.forEach(function (m) {
    var b = by[m.n];
    b.row.addEventListener("mouseenter", function () { b.mk.classList.add("hl"); });
    b.row.addEventListener("mouseleave", function () { b.mk.classList.remove("hl"); });
  });

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches, width = 0;
  fit();
  show(reduce ? "audit" : "today");
  if ("ResizeObserver" in window) {
    new ResizeObserver(function () {  // a new width moves every box: measure again (mid-play, skip to the end)
      if (stage.clientWidth === width) return;
      width = stage.clientWidth;
      if (busy) { stop(); view = "fixed"; }
      fit();
      reset(view);
    }).observe(stage);
  }
  if (document.fonts) document.fonts.ready.then(function () { if (!busy) { fit(); reset(view); } });  // the checks avoid text as it is finally set
  if (!reduce && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (es) {
      if (es.some(function (e) { return e.isIntersecting; })) { io.disconnect(); play(); }
    }, { threshold: 0.45 });
    io.observe(stage);
  }
})();
