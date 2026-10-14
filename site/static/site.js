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
