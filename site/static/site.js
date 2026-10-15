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
