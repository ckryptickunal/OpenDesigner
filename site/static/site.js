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
        Array.prototype.slice.call(node.childNodes).forEach(function (n) { if (n.nodeType === 1) walk(n); else if (n.nodeType === 3) texts.push(n); });
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

/* Home #before-after: the audit as it happens. Plays once when the page comes into view: a scan finds each issue in the
   order it meets them (a dashed box, its number and one line), then the fix sweeps down: a chip carries each token from the
   Merriweft card to its place, and the box becomes a check. Today / Audit / Fixed stop it and show that state at once;
   Replay plays it again. With reduced motion it never plays by itself. Web Animations only: transform, opacity, clip-path. */
(function () {
  "use strict";
  var root = document.querySelector("[data-au]");
  if (!root || !root.animate || !window.Promise) return;
  var D = JSON.parse(document.getElementById("au-data").textContent);
  var EASE = "cubic-bezier(0.23, 1, 0.32, 1)", MOVE = "cubic-bezier(0.77, 0, 0.175, 1)";
  var stage = root.querySelector(".au-stage"), after = stage.querySelector(".au-after"), card = stage.querySelector(".au-tokens");
  var line = stage.querySelector(".au-line"), tag = line.querySelector(".au-tag"), callout = stage.querySelector(".au-callout");
  var status = root.querySelector(".au-status"), cap = root.querySelector(".au-cap"), empty = root.querySelector(".au-empty");
  var tabs = Array.prototype.slice.call(root.querySelectorAll('[role="tab"]')), replay = root.querySelector(".au-replay");
  var by = {}, run = 0, anims = [], timers = [], N = D.marks.length;
  D.marks.forEach(function (m) {
    by[m.n] = { m: m, mk: stage.querySelector('.au-mk[data-n="' + m.n + '"]'), ok: stage.querySelector('.au-ok[data-n="' + m.n + '"]'),
                row: root.querySelector('.au-list li[data-n="' + m.n + '"]') };
  });
  root.classList.add("on");

  function A(el, kf, o) { var a = el.animate(kf, Object.assign({ fill: "forwards" }, o)); anims.push(a); return a; }
  function later(fn, ms) { timers.push(setTimeout(fn, ms)); }
  function wait(ms, id) { return new Promise(function (ok, no) { later(function () { id === run ? ok() : no("stopped"); }, ms); }); }
  function stop() {
    run++;
    timers.forEach(clearTimeout); timers = [];
    anims.forEach(function (a) { a.cancel(); }); anims = [];
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
  function reset(view) {
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
  function px(r) {
    var W = stage.clientWidth, H = stage.clientHeight;
    return { x: r[0] * W / 100, y: r[1] * H / 100, w: r[2] * W / 100, h: r[3] * H / 100, W: W, H: H };
  }
  function place(m) {  // beside its box, above it when there is room, never over a box already found
    var p = px(m.r);
    callout.innerHTML = "<b>" + m.n + "</b><span>" + m.short + "</span>";
    callout.style.left = "0px"; callout.style.top = "0px";
    var cw = callout.offsetWidth, ch = callout.offsetHeight, left = Math.min(Math.max(6, p.x), p.W - cw - 6);
    var hits = function (t) {
      return D.marks.some(function (o) {
        if (o.n === m.n || !by[o.n].shown) return false;
        var q = px(o.r);
        return left < q.x + q.w && left + cw > q.x && t < q.y + q.h && t + ch > q.y;
      });
    };
    var spots = [p.y - ch - 16, p.y + p.h + 12, p.y + 10].filter(function (t) { return t >= 6 && t + ch <= p.H - 6; });
    var top = spots.filter(function (t) { return !hits(t); })[0];
    if (top === undefined) top = spots[0] !== undefined ? spots[0] : 6;
    callout.style.left = left + "px"; callout.style.top = top + "px";
  }
  function groups() {  // issues at about the same height are found together, left to right
    var list = D.marks.slice().sort(function (a, b) { return a.r[1] - b.r[1] || a.r[0] - b.r[0]; }), out = [];
    list.forEach(function (m) { var g = out[out.length - 1]; if (g && Math.abs(g[0].r[1] - m.r[1]) < 2) g.push(m); else out.push([m]); });
    return out;
  }
  function fly(m, b) {  // a chip leaves the token card and lands where the fix goes; the check appears as it lands
    var p = px(m.a || m.r), H = stage.clientHeight, small = stage.clientWidth < 520;
    var land = function () {
      A(b.ok, [{ opacity: 0, transform: "scale(0.9)" }, { opacity: 1, transform: "scale(1)" }], { duration: 240, easing: EASE });
    };
    if (small) { land(); return; }
    var chip = document.createElement("span");
    chip.className = "au-chip";
    chip.textContent = "✓ " + m.token;
    stage.appendChild(chip);
    var x0 = 24, y0 = H - 72, x1 = Math.min(Math.max(6, p.x + 10), stage.clientWidth - chip.offsetWidth - 6), y1 = Math.max(6, p.y - 30);
    A(chip, [{ transform: "translate(" + x0 + "px," + y0 + "px) scale(0.96)", opacity: 0 },
             { transform: "translate(" + x0 + "px," + (y0 - 8) + "px) scale(1)", opacity: 1, offset: 0.15 },
             { transform: "translate(" + x1 + "px," + y1 + "px) scale(1)", opacity: 1 }], { duration: 620, easing: MOVE });
    later(function () { land(); A(chip, [{ opacity: 1 }, { opacity: 0 }], { duration: 260, delay: 520, easing: "ease" }); }, 620);
    later(function () { chip.remove(); }, 1500);
  }

  async function play() {
    stop();
    var id = run;
    reset("today");
    empty.hidden = true;
    var H = stage.clientHeight, y = 0;
    line.classList.remove("fix");
    tag.textContent = "Measuring contrast, sizes and spacing";
    say("Auditing the invoices page…");
    try {
      A(line, [{ opacity: 0 }, { opacity: 1 }], { duration: 200, easing: "ease" });
      await wait(300, id);
      var found = 0, gs = groups();
      for (var gi = 0; gi < gs.length; gi++) {
        var top = px(gs[gi][0].r).y;
        A(line, [{ transform: "translateY(" + y + "px)" }, { transform: "translateY(" + top + "px)" }], { duration: 560, easing: MOVE });
        y = top;
        await wait(580, id);
        if (!found) select("audit");
        for (var k = 0; k < gs[gi].length; k++) {
          var m = gs[gi][k], b = by[m.n];
          found++;
          b.shown = true;
          A(b.mk, [{ opacity: 0, clipPath: "inset(-16px 100% -16px -16px)" }, { opacity: 1, clipPath: "inset(-16px -16px -16px -16px)" }], { duration: 380, easing: EASE });
          A(b.mk.firstElementChild, [{ opacity: 0, transform: "scale(0.9)" }, { opacity: 1, transform: "scale(1)" }], { duration: 220, delay: 60, easing: EASE });
          b.row.hidden = false;
          A(b.row, [{ opacity: 0, transform: "translateY(6px)" }, { opacity: 1, transform: "translateY(0)" }], { duration: 240, easing: EASE });
          place(m);
          A(callout, [{ opacity: 0, transform: "translateY(4px)" }, { opacity: 1, transform: "translateY(0)" }], { duration: 200, delay: 120, easing: EASE });
          say("Found " + found + " of " + N + ": <b>" + m.title + "</b>");
          caption(m);
          await wait(1250, id);
          A(callout, [{ opacity: 1 }, { opacity: 0 }], { duration: 140, easing: "ease" });
        }
      }
      A(line, [{ transform: "translateY(" + y + "px)", opacity: 1 }, { transform: "translateY(" + H + "px)", opacity: 0 }], { duration: 520, easing: MOVE });
      caption(null);
      say("<b>" + N + " issues found.</b> Fixing them with Merriweft's design system…");
      A(card, [{ opacity: 0, transform: "translateY(6px)" }, { opacity: 1, transform: "translateY(0)" }], { duration: 260, delay: 300, easing: EASE });
      await wait(1000, id);

      var SWEEP = 3200, fixed = 0;
      line.classList.add("fix");
      tag.textContent = "Applying Merriweft's tokens";
      A(line, [{ opacity: 0, transform: "translateY(0)" }, { opacity: 1, transform: "translateY(0)" }], { duration: 160, easing: "ease" });
      await wait(180, id);
      A(line, [{ transform: "translateY(0)" }, { transform: "translateY(" + H + "px)" }], { duration: SWEEP, easing: "linear" });
      A(after, [{ clipPath: "inset(0 0 100% 0)" }, { clipPath: "inset(0 0 0% 0)" }], { duration: SWEEP, easing: "linear" });
      D.marks.slice().sort(function (a, b) { return a.r[1] - b.r[1] || a.r[0] - b.r[0]; }).forEach(function (m, i) {
        var b = by[m.n], at = Math.min(px(m.r).y, px(m.a || m.r).y) / H * SWEEP + i * 90;
        later(function () {
          if (id !== run) return;
          fixed++;
          A(b.mk, [{ opacity: 1 }, { opacity: 0 }], { duration: 160, easing: "ease" });
          fly(m, b);
          b.row.classList.add("done");
          tag.textContent = "✓ " + m.token;
          say("Fixed " + fixed + " of " + N + ": <b>" + m.title + "</b>");
          caption(m, true);
          if (fixed === 1) select("fixed");
        }, at);
      });
      await wait(SWEEP + 1300, id);
      A(line, [{ opacity: 1 }, { opacity: 0 }], { duration: 200, easing: "ease" });
      A(card, [{ opacity: 1 }, { opacity: 0 }], { duration: 200, easing: "ease" });
      await wait(260, id);
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

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  show(reduce ? "audit" : "today");
  if (!reduce && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (es) {
      if (es.some(function (e) { return e.isIntersecting; })) { io.disconnect(); play(); }
    }, { threshold: 0.45 });
    io.observe(stage);
  }
})();
