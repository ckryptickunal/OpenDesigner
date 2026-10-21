// The component library shop and component pages: try a look, filter the shelf, fit each live component to its box, the kit
// (components and one look, kept in this browser only) and its prompts, and the device sizes on a component page. Without
// this script every component still shows, in one look. The components' own scripts follow below.
(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var DATA = {}; try { DATA = JSON.parse(($("#lib-data") || {}).textContent || "{}"); } catch (e) {}
  var store = { get: function (k, d) { try { var v = localStorage.getItem(k); return v ? JSON.parse(v) : d; } catch (e) { return d; } },
                set: function (k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} } };

  // Views: a part is shown at a real phone, tablet or desktop width, the same three on its card and on its own page, and a page
  // opens on the view its card was showing (owner, 2026-10-21: "it should show the same inside that it shows outside").
  var VIEWS = { desktop: 1280, tablet: 768, phone: 390 }, ORDER = ["desktop", "tablet", "phone"];
  // a part opens on the view it is designed for (narrow: phone, medium: tablet, wide: desktop); on a phone screen, on phone
  var HUG = window.matchMedia("(max-width: 640px)");
  var defaultView = function (el) { return innerWidth < 768 ? "phone" : (el && el.getAttribute("data-view0")) || "desktop"; };
  // lay a part out at a view's width; when the part is narrower than the view (a 420 px panel on a 1280 px screen), the frame
  // wraps the part instead of leaving it small in an empty field (owner, same day). Returns the frame width used.
  var layout = function (live, w) {
    live.style.zoom = 1; live.style.width = w + "px";
    var part = live.firstElementChild, pad = parseFloat(getComputedStyle(live).paddingLeft) * 2 || 0;
    var used = part ? Math.ceil(part.getBoundingClientRect().width + pad) : w;
    if (used < w - 1) { live.style.width = used + "px"; return used; }
    return w;
  };
  // Nested corners at every size (owner, 2026-10-21: "the edges are not adapted to the screen size"). A part is scaled to fit,
  // so its own corner shrinks with it; the frames around it follow from the inside out: the screen's radius is the part's
  // corner plus the margin around it, both at the shown scale, and the glass rim adds its 6 px.
  // the part's visible outer box: its root, or the first box inside it that is drawn and nearly as wide (a wrapper's card)
  var partR = function (live) {
    var c = live.firstElementChild, w = c ? c.offsetWidth : 0;
    for (var depth = 0; c && depth < 4; depth++) {
      var cs = getComputedStyle(c), drawn = parseFloat(cs.borderTopWidth) > 0 || !/rgba\(0, 0, 0, 0\)|transparent/.test(cs.backgroundColor) || cs.boxShadow !== "none";
      if (drawn && c.offsetWidth >= w * 0.9) return Math.min(parseFloat(cs.borderTopLeftRadius) || 0, c.offsetHeight / 2, c.offsetWidth / 2);
      c = c.firstElementChild;
    }
    return 0;
  };
  // cap: the most the rim may be, so it is never rounder than the tile around it; when the part's own corner would push past it,
  // the margin around the part shrinks instead (down to 4 px), keeping every curve parallel from the part out to the tile
  var nest = function (screen, rim, live, z, cap) {
    live.style.padding = "";
    var pr = partR(live), pad = parseFloat(getComputedStyle(live).paddingTop) || 0, r = Math.max(4, (pr + pad) * z);
    if (cap && r + 6 > cap) { pad = Math.max(4, (cap - 6) / z - pr); live.style.padding = pad.toFixed(1) + "px"; r = Math.max(4, (pr + pad) * z); }
    screen.style.borderRadius = r.toFixed(1) + "px";
    if (rim) rim.style.borderRadius = (r + 6).toFixed(1) + "px";
    return r + 6;
  };
  var fitCard = function (item, view) {
    var live = $(".lib-live", item), bezel = $(".item-in", item); if (!live || !bezel) return;
    var used = layout(live, VIEWS[view]), fitBox = $(".lib-fit", item), media = $(".item-media", item);
    var pad = parseFloat(getComputedStyle(media).paddingTop) || 0;
    var room = { w: media.clientWidth - 2 * pad - 12, h: media.clientHeight - 2 * pad - 12 };  // inside the bezel's 6 px rim
    var z, crop, zw = room.w / used;
    if (HUG.matches) {
      // one column (a phone): the card is as tall as the part at full width, up to 1.3 times its width, then cropped at the bottom
      z = Math.min(1, zw); var h = live.offsetHeight * z, cap = room.w * 1.3;
      crop = h > cap; room.h = Math.ceil(Math.min(h, cap));
      media.style.height = (room.h + 12 + 2 * pad) + "px";
    } else {
      media.style.height = "";
      // fit the whole part, centred; if that would make it too small to read, fit the width and crop the bottom instead
      var zh = room.h / Math.max(1, live.offsetHeight);
      z = Math.min(1, zw, zh); crop = z < Math.min(zw, 1) * 0.72;
      if (crop) z = Math.min(1, zw);
    }
    live.style.zoom = z.toFixed(3); fitBox.classList.toggle("is-cropped", crop);
    bezel.style.maxHeight = (room.h + 12) + "px"; fitBox.style.maxHeight = room.h + "px";  // a cropped part stays inside the rim
    media.style.borderRadius = "";
    var cap = (parseFloat(getComputedStyle(media).borderTopLeftRadius) || 0) * 0.8, rimR = nest(fitBox, bezel, live, z, cap);
    if (rimR > cap + 0.5) media.style.borderRadius = (rimR / 0.8).toFixed(1) + "px";  // a very round part (an overlay in a pill look): the tile follows it out
    item.setAttribute("data-view", view);
    $$(".item-views i", item).forEach(function (i) { i.classList.toggle("is-on", i.getAttribute("data-v") === view); });
    var label = $(".item-view-t", item); if (label) label.textContent = view[0].toUpperCase() + view.slice(1);
    var link = $(".item-link", item); if (link) link.href = link.getAttribute("href").split("?")[0] + "?view=" + view;
  };
  // a part's first view, the same rule on its card and on its page: the part's own view, or a narrower one when the part would
  // sit as a thin band (a short, wide strip at 1280 px; at 768 px it wraps into rows). Measured on the part alone, so the card
  // and the page always agree; the click carries it as ?view=. On a phone screen, always the phone view.
  var firstView = function (el, live) {
    var start = defaultView(el); if (!live || innerWidth < 768) return start;
    for (var i = ORDER.indexOf(start); i < ORDER.length; i++) {
      var used = layout(live, VIEWS[ORDER[i]]);
      if (used > 700 && i < ORDER.length - 1) continue;  // 1280 and 768 px layouts shrink to about 0.4 in a card, too small to read: one hover or tab away
      if (live.offsetHeight / used >= 0.34 || i === ORDER.length - 1) { live.style.width = ""; return ORDER[i]; }
    }
    return start;
  };
  var bestView = function (item) { var v = firstView(item, $(".lib-live", item)); item.setAttribute("data-view-first", v); return v; };
  // aisle tiles: a part laid out at a card width and zoomed to the tile
  var fitTile = function (box) {
    var live = box.querySelector(".lib-live"); if (!live) return;
    var w = +box.getAttribute("data-w") || 640;
    live.style.width = w + "px"; live.style.zoom = 1;
    var prev = box.closest(".aisle-prev"), z = Math.max(0.2, Math.min(1, prev.clientWidth / w));
    live.style.zoom = z.toFixed(3);
    // a tile keeps one corner (the tile's minus its 14 px margin); the margin around the part is set so the part's corner,
    // at this scale, runs parallel to it
    var prevR = parseFloat(getComputedStyle(prev).borderTopLeftRadius) || 0;
    live.style.padding = Math.max(6, prevR / z - partR(live)).toFixed(1) + "px";
  };
  var fitAll = function () {
    $$(".aisle-prev .lib-fit").forEach(fitTile);
    $$(".item").forEach(function (item) { if (!item.hidden) fitCard(item, item.getAttribute("data-view") || bestView(item)); });
    fitDevice();
  };
  if (window.ResizeObserver) { var ro = new ResizeObserver(function () { fitAll(); }); $$(".item-media, .aisle-prev, .part-stage").forEach(function (el) { ro.observe(el); }); }
  window.addEventListener("load", fitAll);

  // a soft change of view: the old layout fades and blurs out fast, the new one fades in (Emil Kowalski: crossfade with a 2 px
  // blur so two states read as one; ease-out; exit faster than enter; under 300 ms)
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  // Web Animations, not a class: nothing can be left half-faded if views change quickly (owner saw a card stuck blurred)
  var swap = function (live, apply) {
    if (reduce || !live.animate) { apply(); return; }
    if (live._swap) { live._swap.cancel(); }
    var out = live.animate([{ opacity: 1, filter: "blur(0)" }, { opacity: 0, filter: "blur(2px)" }], { duration: 120, easing: "cubic-bezier(0.23, 1, 0.32, 1)", fill: "forwards" });
    live._swap = out;
    out.onfinish = function () {
      apply();
      var inn = live.animate([{ opacity: 0, filter: "blur(2px)" }, { opacity: 1, filter: "blur(0)" }], { duration: 200, easing: "cubic-bezier(0.23, 1, 0.32, 1)" });
      out.cancel(); live._swap = inn;
      inn.onfinish = inn.oncancel = function () { live._swap = null; };
    };
  };
  // hovering a card walks through the views; leaving goes back. Only with a real pointer, and never with reduced motion.
  if (window.matchMedia("(hover: hover) and (pointer: fine)").matches && !reduce) {
    $$(".shelf .item, .part-more .item").forEach(function (item) {
      var timer = null, start = null;
      var next = function () {
        var v = ORDER[(ORDER.indexOf(item.getAttribute("data-view") || defaultView(item)) + 1) % ORDER.length];
        swap($(".lib-live", item), function () { fitCard(item, v); });
      };
      item.addEventListener("pointerenter", function () { start = setTimeout(function () { next(); timer = setInterval(next, 1600); }, 450); });
      item.addEventListener("pointerleave", function () {
        clearTimeout(start); clearInterval(timer);
        var home = item.getAttribute("data-view-first") || defaultView(item);
        if (item.getAttribute("data-view") !== home) swap($(".lib-live", item), function () { fitCard(item, home); });
      });
    });
  }

  // looks
  var LOOK_KEY = "od-library-look";
  var current = store.get(LOOK_KEY, "billerwick");
  var useLook = function (key) {
    if (!DATA.looks || !DATA.looks[key]) return;
    current = key; store.set(LOOK_KEY, key);
    $$(".lib-live").forEach(function (el) { el.className = el.className.replace(/odl-sys-[a-z]+/, "odl-sys-" + key); });
    $$(".look[data-look]").forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-look") === key ? "true" : "false"); });
    $$(".part-look").forEach(function (s) { s.value = key; });
    lookLabel();
    requestAnimationFrame(fitAll);
  };
  $$(".look[data-look]").forEach(function (b) { b.addEventListener("click", function () { useLook(b.getAttribute("data-look")); }); });
  $$(".part-look").forEach(function (s) { s.addEventListener("change", function () { useLook(s.value); }); });

  // filters: aisle tiles, type chips, style, industry and words, all at once
  var type = "all", q = $("#lib-q"), style = $("#lib-style"), industry = $("#lib-industry");
  var apply = function () {
    var words = q ? q.value.trim().toLowerCase().split(/\s+/).filter(Boolean) : [], shown = 0;
    $$(".shelf .item").forEach(function (c) {
      var ind = c.getAttribute("data-industries").split(" ");
      var ok = (type === "all" || c.getAttribute("data-type") === type)
        && (!style || !style.value || c.getAttribute("data-style") === style.value)
        && (!industry || !industry.value || ind.indexOf(industry.value) >= 0 || ind.indexOf("any") >= 0)
        && words.every(function (w) { return c.getAttribute("data-search").indexOf(w) >= 0; });
      c.hidden = !ok; if (ok) shown++;
    });
    var n = $(".shelf-count .n"); if (n) n.textContent = shown;
    var none = $(".lib-none"); if (none) none.hidden = shown > 0;
    requestAnimationFrame(fitAll);
  };
  var setType = function (t) {
    type = t;
    $$(".lib-filters .filter").forEach(function (x) { var on = x.getAttribute("data-type") === t; x.classList.toggle("is-on", on); x.setAttribute("aria-pressed", on ? "true" : "false"); });
    apply();
  };
  $$(".lib-filters .filter").forEach(function (b) { b.addEventListener("click", function () { setType(b.getAttribute("data-type")); }); });
  $$(".aisle[data-aisle]").forEach(function (a) { a.addEventListener("click", function () { setType(a.getAttribute("data-aisle")); }); });
  [style, industry].forEach(function (el) { if (el) el.addEventListener("change", apply); });
  if (q) q.addEventListener("input", function () { if (q.value && type !== "all") setType("all"); else apply(); });
  $$(".shop-pop [data-q]").forEach(function (b) {  // popular searches fill the search and jump to the results
    b.addEventListener("click", function () { q.value = b.getAttribute("data-q"); setType("all"); var sh = $("#shelf"); if (sh) sh.scrollIntoView({ block: "start" }); });
  });
  var hashAisle = (location.hash.match(/^#aisle-(\w+)/) || [])[1]; if (hashAisle) setType(hashAisle);
  $$("[data-goto-aisle]").forEach(function (a) { a.href = "/library/#aisle-" + a.getAttribute("data-goto-aisle"); });

  // views on a component page: the same three widths as the cards, opening on the view the card showed (?view=)
  var dev = $(".part-device"), frame = $(".part-frame"), stage = $(".part-stage");
  var pageView = (location.search.match(/[?&]view=(desktop|tablet|phone)/) || [])[1] || (dev ? firstView(dev, $(".lib-live", frame)) : "desktop");
  if (pageView === "desktop" && innerWidth <= 640) pageView = "phone";  // no desktop tab on a phone screen: it would not read
  function fitDevice() {
    if (!dev || !frame) return;
    var view = dev.getAttribute("data-device") || pageView, w = VIEWS[view];
    var live = $(".lib-live", frame); frame.style.zoom = 1; frame.style.minHeight = "";
    var used = live ? layout(live, w) : w;
    live && (live.style.width = "");
    frame.style.width = used + "px";
    var avail = stage.clientWidth - parseFloat(getComputedStyle(stage).paddingLeft) * 2 - 12;  // 12: the glass rim, 6 px a side
    var z = Math.min(1, avail / used);
    frame.style.zoom = z.toFixed(3);
    var devR = nest(frame, null, live, z) ; dev.style.borderRadius = devR.toFixed(1) + "px";
    // if the device sits close to the stage's corner (a phone screen), the stage's corner follows it too
    var sr = stage.getBoundingClientRect(), dr = dev.getBoundingClientRect(), gap = Math.min(dr.left - sr.left, dr.top - sr.top);
    stage.style.borderRadius = gap < 40 ? (devR + gap).toFixed(1) + "px" : "";
    // the frame hugs the part's height too (post-change audit, rule 6): no forced phone shape around a short part
  }
  var pick = function (view, animate) {
    $$(".part-devices [role='tab']").forEach(function (t) { var on = t.getAttribute("data-device") === view; t.setAttribute("aria-selected", on ? "true" : "false"); t.tabIndex = on ? 0 : -1; });
    if (!dev) return;
    var go = function () { dev.setAttribute("data-device", view); fitDevice(); };
    if (animate) swap($(".lib-live", frame), go); else go();
    if (history.replaceState) history.replaceState(null, "", location.pathname + "?view=" + view);
  };
  pick(pageView, false);
  $$(".part-devices [role='tab']").forEach(function (t, i, all) {
    t.addEventListener("click", function (e) { pick(t.getAttribute("data-device"), e.detail > 0); });  // keyboard switches stay instant
    t.addEventListener("keydown", function (e) {
      var j = e.key === "ArrowRight" ? i + 1 : e.key === "ArrowLeft" ? i - 1 : null; if (j === null) return;
      e.preventDefault(); var n = all[(j + all.length) % all.length]; if (getComputedStyle(n).display === "none") n = all[(j + (e.key === "ArrowRight" ? 1 : -1) + all.length) % all.length];
      n.click(); n.focus();
    });
  });

  // the kit: components and one look, kept in this browser
  var KIT_KEY = "od-library-kit";
  var kit = store.get(KIT_KEY, { items: [], look: null });
  kit.items = (kit.items || []).filter(function (s) { return DATA.items && DATA.items[s]; });
  var fab = $(".kit-fab"), dlg = $("#kit"), out = "parts";
  var save = function () { store.set(KIT_KEY, kit); render(); };
  var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); };
  var url = function (s) { return DATA.site + "/library/r/" + s + ".html"; };
  var prompt = function () {
    var parts = kit.items, look = kit.look && DATA.looks[kit.look];
    var list = parts.map(function (s) { return "- " + DATA.items[s].name + ": " + url(s); }).join("\n");
    var addParts = parts.length ? "Add these OpenDesigner components to this project, one small file each:\n" + list +
      "\nKeep their markup and states, and map their --ds-* variables to my design tokens. Turn each into a component in this project's framework." : "";
    if (out === "parts") return addParts || "Add a component to your kit first.";
    var sys = look
      ? "Use OpenDesigner (" + DATA.gh + ") to make this project's design system in the " + look.name + " look (" + look.plain + "). Run, with my product's name" +
        (look.home ? "" : " and brand colour") + " in place of the sample ones:\n" + look.commands.map(function (c) { return "  python3 <skill>/scripts/" + c; }).join("\n") +
        "\n  python3 <skill>/scripts/engine.py build\n(<skill> is the folder where the OpenDesigner skill is installed.) Ask me only what the recipe leaves open."
      : "Use OpenDesigner (" + DATA.gh + ") to make a design system for this project: ask me its five sketch questions, then build it.";
    var then = parts.length ? "\nThen add these components with library.py add, one at a time: " + parts.join(", ") + ". They already use the system's tokens, so nothing needs restyling." : "";
    var text = sys + then;
    return text;  // for Claude Code the two install commands are a separate step 1 with their own copy button: one paste, one action
  };
  var STAR_KEY = "od-library-star-asked";
  // the look button says what it will do, and shows when the look on show is already in the kit
  function lookLabel() {
    $$(".look-add").forEach(function (b) {
      var nm = DATA.looks[current] ? DATA.looks[current].name : "", inKit = !!(kit && kit.look === current);
      b.setAttribute("aria-pressed", inKit ? "true" : "false");
      b.querySelector("span").textContent = inKit ? nm + " is in your kit" : "Add " + nm + " to your kit";
      var ic = b.querySelector("svg"); if (ic) ic.innerHTML = inKit ? '<path d="m4 8.5 2.5 2.5L12 5.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>' : (b._plus || (b._plus = ic.innerHTML));
      if (!b._plus && ic) b._plus = ic.innerHTML;
    });
  }
  function render() {
    lookLabel();
    var n = kit.items.length + (kit.look ? 1 : 0);
    if (fab) { fab.hidden = false; fab.classList.toggle("is-empty", n === 0); $(".kit-n", fab).textContent = n; fab.setAttribute("aria-label", "Your kit, " + n + (n === 1 ? " item" : " items")); }
    $$("[data-kit-add]").forEach(function (b) { b.setAttribute("aria-pressed", kit.items.indexOf(b.getAttribute("data-kit-add")) >= 0 ? "true" : "false"); });
    if (!dlg) return;
    $(".kit-empty", dlg).hidden = n > 0;
    $(".kit-items", dlg).innerHTML = kit.items.map(function (s) {
      var it = DATA.items[s];
      return '<li><span class="kit-thumb" data-thumb="' + s + '" aria-hidden="true"></span><span class="k-name"><strong>' + esc(it.name) + '</strong><small>' + esc(it.type) + ' · ' + it.kb + ' KB · MIT</small></span>'
        + '<button type="button" class="kit-rm" data-rm="' + s + '" aria-label="Remove ' + esc(it.name) + '">×</button></li>';
    }).join("");
    var lk = kit.look && DATA.looks[kit.look];
    $(".kit-look", dlg).innerHTML = lk
      ? '<span class="look-sw odl-sys-' + kit.look + '" aria-hidden="true"><i></i></span><span class="k-name"><strong>' + esc(lk.name) + ' look</strong><small>' + esc(lk.plain) + '</small></span><button type="button" class="kit-rm kit-rm-look" aria-label="Remove the look">×</button>'
      : (DATA.looks[current] ? '<span class="look-sw odl-sys-' + current + '" aria-hidden="true"><i></i></span><span class="k-name"><strong>No look yet</strong><small>You keep your own tokens, or add the one you are trying on.</small></span><button type="button" class="btn text look-add-in">Add ' + esc(DATA.looks[current].name) + '</button>' : "");
    var kb = kit.items.reduce(function (t, s) { return t + DATA.items[s].kb; }, 0);
    $(".co-n-parts", dlg).textContent = kit.items.length + (kit.look ? " + a look" : "");
    $(".co-kb", dlg).textContent = (Math.round(kb * 10) / 10) + " KB";
    $(".kit-prompt", dlg).textContent = prompt();
    $$(".co-method", dlg).forEach(function (t) { var on = t.getAttribute("data-out") === out; t.setAttribute("aria-checked", on ? "true" : "false"); t.tabIndex = on ? 0 : -1; });
    $$(".co-pay", dlg).forEach(function (pay) { pay.disabled = n === 0; });
    $(".co-step1", dlg).hidden = out !== "claude";
    $(".co-prompt-l", dlg).textContent = out === "claude" ? "Step 2 · then paste this prompt" : "Your prompt";
    $(".co-bar-n", dlg).textContent = " · " + kit.items.length + (kit.items.length === 1 ? " part" : " parts") + (kit.look ? " and a look" : "");
    $$(".kit-thumb[data-thumb]", dlg).forEach(thumb);
  }
  // hovering a thumbnail opens a bigger look at the part beside it (a popover: grows from the thumbnail, 160 ms ease-out in,
  // quicker out; pointer only, the names already say what each part is)
  var peek = dlg && $(".kit-peek", dlg), peekTimer = null;
  if (peek && window.matchMedia("(hover: hover) and (pointer: fine)").matches) {
    dlg.addEventListener("pointerover", function (e) {
      var t = e.target.closest(".kit-thumb[data-thumb]"); if (!t) return;
      clearTimeout(peekTimer);
      var s = t.getAttribute("data-thumb"), markup = thumbCache[s]; if (!markup) return;
      peek.innerHTML = '<span class="lib-live odl-sys-' + current + '" inert>' + markup + '</span><span class="kit-peek-n">' + esc(DATA.items[s].name) + '</span>';
      var live = peek.firstChild; live.style.width = "390px"; live.style.zoom = "0.75";
      var r = t.getBoundingClientRect(), h = Math.min(innerHeight - 32, 440);
      peek.style.left = Math.round(r.right + 12) + "px";
      peek.style.top = Math.round(Math.max(16, Math.min(r.top - 8, innerHeight - h - 16))) + "px";
      peek.style.transformOrigin = "left " + Math.round(r.top + r.height / 2 - parseFloat(peek.style.top)) + "px";
      peek.classList.add("is-open");
    });
    dlg.addEventListener("pointerout", function (e) {
      if (!e.target.closest(".kit-thumb[data-thumb]")) return;
      peekTimer = setTimeout(function () { peek.classList.remove("is-open"); }, 60);
    });
  }
  // a small live picture of each part in the kit: copied from its card when the page has one, else fetched from its own file
  var thumbCache = {};
  function thumb(box) {
    var s = box.getAttribute("data-thumb");
    var put = function (markup) {
      box.innerHTML = '<span class="kit-thumb-in lib-live odl-sys-' + current + '" inert>' + markup + '</span>';
      var live = box.firstChild; live.style.width = "390px";
      live.style.zoom = (56 / 390).toFixed(3);  // the 56 px thumbnail shows the part at its phone width (fixed: the dialog may still be closed)
    };
    if (thumbCache[s]) return put(thumbCache[s]);
    var card = document.querySelector("#item-" + s + " .lib-live");
    if (card) { thumbCache[s] = card.innerHTML; return put(thumbCache[s]); }
    fetch("/library/r/" + s + ".html").then(function (r) { return r.ok ? r.text() : ""; }).then(function (t) {
      var m = t.replace(/<style>[\s\S]*?<\/style>|<script>[\s\S]*?<\/script>/g, "").replace(/\s(id|for|name|aria-[a-z]+)="[^"]*"/g, "").replace(/<a\b/g, "<span").replace(/<\/a>/g, "</span>");
      thumbCache[s] = m; put(m);
    }).catch(function () {});
  }
  var bump = function () { if (!fab) return; fab.classList.remove("bump"); void fab.offsetWidth; fab.classList.add("bump"); };
  $$("[data-kit-add]").forEach(function (b) {
    b.addEventListener("click", function () {
      var s = b.getAttribute("data-kit-add"), i = kit.items.indexOf(s);
      if (i >= 0) kit.items.splice(i, 1); else { kit.items.push(s); bump(); }
      save();
    });
  });
  $$(".look-add").forEach(function (b) { b.addEventListener("click", function () { kit.look = kit.look === current ? null : current; save(); if (kit.look) bump(); }); });
  if (fab && dlg && dlg.showModal) {
    fab.addEventListener("click", function () {
      render(); $(".co-next", dlg).hidden = true; $(".co-star", dlg).hidden = true;
      $$(".co-pay", dlg).forEach(function (pay) { pay.classList.remove("is-done"); $("span", pay).textContent = "Copy prompt"; });
      dlg.showModal();
    });
    $(".kit-x", dlg).addEventListener("click", function () { dlg.close(); });
    var methods = $$(".co-method", dlg);
    methods.forEach(function (m, i) {
      m.addEventListener("click", function () { out = m.getAttribute("data-out"); render(); });
      m.addEventListener("keydown", function (e) {
        var j = (e.key === "ArrowRight" || e.key === "ArrowDown") ? i + 1 : (e.key === "ArrowLeft" || e.key === "ArrowUp") ? i - 1 : null;
        if (j === null) return; e.preventDefault(); var n = methods[(j + methods.length) % methods.length]; n.click(); n.focus();
      });
    });
    dlg.addEventListener("click", function (e) {
      if (e.target === dlg) { dlg.close(); return; }
      if (e.target.closest(".look-add-in")) { kit.look = current; save(); return; }
      if (e.target.closest(".kit-rm-look")) { kit.look = null; save(); $(".kit-x", dlg).focus(); return; }
      var rm = e.target.closest("[data-rm]");
      if (rm) {
        var at = kit.items.indexOf(rm.getAttribute("data-rm")); kit.items.splice(at, 1); save();
        var next = $$(".kit-items .kit-rm", dlg)[Math.min(at, kit.items.length - 1)];
        (next || $(".kit-x", dlg)).focus(); return;  // focus stays in the open checkout
      }
      if (e.target.closest(".kit-clear")) { kit = { items: [], look: null }; save(); $(".kit-x", dlg).focus(); return; }
      if (e.target.closest(".co-star-no")) { store.set(STAR_KEY, true); $(".co-star", dlg).hidden = true; return; }
      var cmd = e.target.closest(".kit-copy-cmd");
      if (cmd) {
        var cl = cmd.querySelector("span"), ok = function () { cl.textContent = "Copied. Run them, then copy step 2"; };
        if (navigator.clipboard) navigator.clipboard.writeText($(".kit-cmd", dlg).textContent).then(ok, ok); else ok();
        return;
      }
      var c = e.target.closest(".kit-copy");
      if (c) {
        var lab = c.querySelector("span"), done = function () {
          c.classList.add("is-done"); lab.textContent = "Copied. Paste it into your agent";
          $(".co-next", dlg).hidden = false;
          if (!store.get(STAR_KEY, false)) $(".co-star", dlg).hidden = false;  // a soft ask, once, after it helped; never a wall
        };
        if (navigator.clipboard) navigator.clipboard.writeText(prompt()).then(done, done); else done();
      }
    });
    $$(".co-star a", dlg).forEach(function (a) { a.addEventListener("click", function () { store.set(STAR_KEY, true); }); });
  }
  useLook(current);
  render();
})();
