// Product analytics with PostHog (owner, 2026-10-23: "see where people interact, engage and drop off"; 2026-10-24: "let's
// keep session replays" and "proper attribution ... wherever the users come from"). US cloud (the project's region).
// Two modes, chosen by the visitor:
//   - default: cookieless. Nothing is stored in the browser; PostHog counts visitors with a daily server-side hash. Page
//     views (with referrer and UTM tags), page leaves and the named events below. No session recording.
//   - after "Allow" on the small banner: PostHog may keep an anonymous id in this browser and record the session (every
//     input masked, the booking page never recorded), so visits link up and first-touch attribution survives.
// The choice itself is kept in localStorage ("od-analytics"): a record of consent, needed to not ask again.
// Requests go through /ingest/ on this site (vercel.json rewrites), so the CSP stays 'self'. Loaded only when
// site/analytics.json has a key; the key is a public project key. What is counted: docs/PRIVACY.md.
(function () {
  var me = document.currentScript, key = me && me.getAttribute("data-key");
  if (!key || navigator.doNotTrack === "1" || window.doNotTrack === "1") { window.odTrack = function () {}; return; }
  var CHOICE = "od-analytics", choice = null;
  try { choice = localStorage.getItem(CHOICE); } catch (e) {}
  var full = choice === "granted";
  var noRecord = /^\/book\//.test(location.pathname);  // the booking form holds a name and an email

  var queue = [];
  window.odTrack = function (name, props) {
    if (window.posthog && window.posthog.__loaded) window.posthog.capture(name, props || {});
    else queue.push([name, props || {}]);
  };

  // where this visit came from, on every event (UTM tags, ref=, the referring site, the page they landed on)
  var q = new URLSearchParams(location.search), src = {};
  ["utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term", "ref", "via"].forEach(function (k) { if (q.get(k)) src[k] = q.get(k).slice(0, 100); });
  var refHost = ""; try { refHost = document.referrer ? new URL(document.referrer).hostname : ""; } catch (e) {}
  if (refHost === location.hostname) refHost = "";
  src.source = src.utm_source || src.ref || src.via || refHost || "direct";
  src.landing_page = location.pathname;

  var s = document.createElement("script");
  s.src = "/ingest/static/array.js"; s.async = true;
  s.onload = function () {
    if (!window.posthog || !window.posthog.init) return;
    window.posthog.init(key, {
      api_host: "/ingest", ui_host: "https://us.posthog.com",
      cookieless_mode: full ? undefined : "always",  // cookieless mode must also be on in the project settings
      persistence: full ? "localStorage+cookie" : "memory",
      disable_session_recording: !full || noRecord,
      session_recording: { maskAllInputs: true, maskTextSelector: "[data-private], .h-form" },
      disable_surveys: true, autocapture: false, capture_pageview: true, capture_pageleave: true, respect_dnt: true,
      loaded: function (ph) {
        // first touch stays with the person (full mode); this visit's source goes on every event
        if (full) {
          var first = src; try { first = JSON.parse(localStorage.getItem("od-first")) || src; localStorage.removeItem("od-first"); } catch (e) {}
          ph.register_once({ first_source: first.source, first_landing_page: first.landing_page, first_campaign: first.utm_campaign || null });
        }
        ph.register({ source: src.source, landing_page: src.landing_page, consent: full ? "granted" : (choice || "pending") });
        queue.forEach(function (e) { ph.capture(e[0], e[1]); }); queue = [];
      }
    });
  };
  document.head.appendChild(s);

  // the consent banner: shown until the visitor chooses; a quiet card in the corner, never blocking the page
  if (!choice) {
    var show = function () {
      var b = document.createElement("div");
      b.className = "od-consent"; b.setAttribute("role", "region"); b.setAttribute("aria-label", "Session recording");
      b.innerHTML = '<p>Help us improve OpenDesigner: may we record your visit anonymously? Inputs are hidden, and nothing is recorded until you say yes. <a href="https://github.com/ckryptickunal/OpenDesigner/blob/main/docs/PRIVACY.md#the-websites-product-analytics">What we collect</a></p>' +
        '<div class="od-consent-acts"><button type="button" class="btn ghost" data-v="denied">No thanks</button><button type="button" class="btn primary" data-v="granted">Allow</button></div>';
      var st = document.createElement("style");
      st.textContent = ".od-consent{position:fixed;z-index:60;inset:auto 16px 16px auto;max-width:360px;padding:16px;border:1px solid var(--border,#d9d9d9);border-radius:var(--r-card,12px);background:var(--surface-raised,#fff);color:var(--ink,#111);box-shadow:0 8px 24px rgb(0 0 0/.12);font:400 14px/20px 'Hanken Grotesk',system-ui,sans-serif}" +
        ".od-consent p{margin:0 0 12px}.od-consent a{color:inherit}.od-consent-acts{display:flex;gap:8px;justify-content:flex-end}" +
        "@media (max-width:480px){.od-consent{inset:auto 16px 16px 16px;max-width:none}}";
      document.head.appendChild(st); document.body.appendChild(b);
      b.addEventListener("click", function (e) {
        var v = e.target.closest && e.target.closest("[data-v]"); if (!v) return;
        var val = v.getAttribute("data-v");
        try { localStorage.setItem(CHOICE, val); if (val === "granted") localStorage.setItem("od-first", JSON.stringify(src)); } catch (err) {}  // the visit they allowed on is their first touch
        window.odTrack("consent_chosen", { choice: val });
        b.remove();  // recording starts from the next page, in full mode
      });
    };
    if (document.body) setTimeout(show, 1500); else document.addEventListener("DOMContentLoaded", function () { setTimeout(show, 1500); });
  }

  // site-wide intent: GitHub, install, booking and any copy button (commands, prompts)
  document.addEventListener("click", function (e) {
    var t = e.target.closest && e.target.closest("a, button"); if (!t) return;
    var href = t.getAttribute("href") || "", from = location.pathname;
    if (/github\.com\/ckryptickunal\/OpenDesigner/.test(href) && !/PRIVACY\.md/.test(href)) window.odTrack("github_click", { from: from, label: (t.textContent || "").trim().slice(0, 40) });
    else if (href.indexOf("/book") === 0) window.odTrack("book_call_click", { from: from });
    else if (href.indexOf("/docs/install") === 0) window.odTrack("install_click", { from: from });
    if (t.matches(".copy, [data-copy], [data-copy-text]")) {
      var item = t.closest("[id^='item-']"), part = item ? item.id.slice(5) : (from.match(/^\/library\/([a-z0-9-]+)\/$/) || [])[1];
      window.odTrack(part ? "prompt_copied" : "copy_clicked", { from: from, part: part || null });
    }
  }, true);
})();
