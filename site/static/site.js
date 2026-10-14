// OpenDesigner site: copy buttons and live GitHub numbers. The page reads fine without it.
(function () {
  document.querySelectorAll("[data-copy], [data-copy-text]").forEach(function (btn) {
    var label = btn.textContent;
    btn.addEventListener("click", function () {
      var text = btn.getAttribute("data-copy-text") || (btn.parentElement.querySelector("code") || {}).innerText || "";
      var done = function () { btn.textContent = "Copied"; setTimeout(function () { btn.textContent = label; }, 1600); };
      if (navigator.clipboard) navigator.clipboard.writeText(text).then(done, function () {}); else done();
    });
  });
  if (!document.querySelector("[data-stars], [data-gh-card]")) return;
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
})();
