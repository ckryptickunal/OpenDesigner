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
