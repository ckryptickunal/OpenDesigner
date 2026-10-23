// Product analytics with PostHog (owner, 2026-10-23: "see where people interact, engage and drop off").
// Cookieless: nothing is stored in the browser (persistence "memory"), no session replay, no surveys, no automatic capture of
// clicks or inputs; only the page views and the named events below. Requests go to /ingest/ on this site, which Vercel
// forwards to PostHog's EU cloud, so the site's Content-Security-Policy stays 'self'. Loaded only when site/analytics.json
// has a key; the key is a public project key. What is counted: docs/PRIVACY.md, "The website".
(function () {
  var me = document.currentScript, key = me && me.getAttribute("data-key");
  if (!key || navigator.doNotTrack === "1" || window.doNotTrack === "1") { window.odTrack = function () {}; return; }
  var queue = [];
  window.odTrack = function (name, props) {
    if (window.posthog && window.posthog.__loaded) window.posthog.capture(name, props || {});
    else queue.push([name, props || {}]);
  };
  var s = document.createElement("script");
  s.src = "/ingest/static/array.js"; s.async = true;
  s.onload = function () {
    if (!window.posthog || !window.posthog.init) return;
    window.posthog.init(key, {
      api_host: "/ingest", ui_host: "https://eu.posthog.com",
      persistence: "memory", cookieless_mode: "always", disable_session_recording: true, disable_surveys: true,  // cookieless mode must also be on in the project settings
      autocapture: false, capture_pageview: true, capture_pageleave: true, respect_dnt: true,
      loaded: function (ph) { queue.forEach(function (e) { ph.capture(e[0], e[1]); }); queue = []; }
    });
  };
  document.head.appendChild(s);

  // site-wide intent: GitHub, install, booking and any copy button (commands, prompts)
  document.addEventListener("click", function (e) {
    var t = e.target.closest && e.target.closest("a, button"); if (!t) return;
    var href = t.getAttribute("href") || "", from = location.pathname;
    if (/github\.com\/ckryptickunal\/OpenDesigner/.test(href)) window.odTrack("github_click", { from: from, label: (t.textContent || "").trim().slice(0, 40) });
    else if (href.indexOf("/book") === 0) window.odTrack("book_call_click", { from: from });
    else if (href.indexOf("/docs/install") === 0) window.odTrack("install_click", { from: from });
    if (t.matches(".copy, [data-copy], [data-copy-text]")) {
      var item = t.closest("[id^='item-']"), part = item ? item.id.slice(5) : (from.match(/^\/library\/([a-z0-9-]+)\/$/) || [])[1];
      window.odTrack(part ? "prompt_copied" : "copy_clicked", { from: from, part: part || null });
    }
  }, true);
})();
