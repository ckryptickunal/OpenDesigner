// The component library shop and component pages: try a look, filter the shelf, fit each live component to its box, the kit
// (components and one look, kept in this browser only) and its prompts, and the device sizes on a component page. Without
// this script every component still shows, in one look. The components' own scripts follow below.
(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var DATA = {}; try { DATA = JSON.parse(($("#lib-data") || {}).textContent || "{}"); } catch (e) {}
  // analytics (site/static/ph.js; a no-op when analytics is off): what people try, open, add and copy, for funnels
  var track = function (name, props) { if (window.odTrack) window.odTrack(name, props || {}); };
  var store = { get: function (k, d) { try { var v = localStorage.getItem(k); return v ? JSON.parse(v) : d; } catch (e) { return d; } },
                set: function (k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} } };

  // Views: a part is shown at a real phone, tablet or desktop width, the same three on its card and on its own page, and a page
  // opens on the view its card was showing (owner, 2026-10-21: "it should show the same inside that it shows outside").
  var VIEWS = { desktop: 1280, tablet: 768, phone: 390 }, ORDER = ["desktop", "tablet", "phone"];
  // a part opens on the view it is designed for (narrow: phone, medium: tablet, wide: desktop); on a phone screen, on phone
  var HUG = window.matchMedia("(max-width: 640px)");
  // every card and page opens on the desktop view on a wide screen, the phone view on a phone (owner, 2026-10-23: "show desktop
  // view by default unless someone hovers"); hovering a card walks the other views
  // Scale a box with a transform, never CSS zoom (owner, 2026-10-24, Safari screenshots: cards drawn as one-letter columns).
  // Safari keeps text at a minimum size inside a small zoom while the box shrinks, so text wraps letter by letter and the part
  // grows thousands of pixels tall; a transform scales text and box together in every browser. Negative margins give the
  // box its scaled size in the layout, as zoom did. Call it again after anything inside changes the box's size.
  var scaleEl = function (el, z) {
    el.style.zoom = ""; el.style.marginRight = el.style.marginBottom = "";
    if (z >= 0.999) { el.style.transform = el.style.transformOrigin = ""; el._z = 1; return; }
    el.style.transform = "scale(" + z.toFixed(4) + ")"; el.style.transformOrigin = "0 0"; el._z = z;
    var w = el.offsetWidth, h = el.offsetHeight;  // the unscaled box (a transform does not change these)
    el.style.marginRight = (w * z - w).toFixed(2) + "px"; el.style.marginBottom = (h * z - h).toFixed(2) + "px";
  };
  var rescale = function (el) { scaleEl(el, el._z || 1); };
  var defaultView = function () { return innerWidth < 768 ? "phone" : "desktop"; };
  // lay a part out at a view's width; when the part is narrower than the view (a 420 px panel on a 1280 px screen), the frame
  // wraps the part instead of leaving it small in an empty field (owner, same day). Returns the frame width used.
  var layout = function (live, w) {
    scaleEl(live, 1); live.style.width = w + "px";
    var part = live.firstElementChild, pad = parseFloat(getComputedStyle(live).paddingLeft) * 2 || 0;
    var used = part ? Math.ceil(part.getBoundingClientRect().width + pad) : w;
    if (used < w - 1 && used > Math.min(240, w / 2)) { live.style.width = used + "px"; return used; }  // a part measuring under 240 px was not drawn: keep the view width
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
    live.style.padding = "";  // measure at the default margin; nest() below may narrow it again
    var used = layout(live, VIEWS[view]), fitBox = $(".lib-fit", item), media = $(".item-media", item);
    if (!HUG.matches) media.style.height = "";  // drop a phone fit's fixed height before measuring (it skews the 4:3 tile)
    var pad = parseFloat(getComputedStyle(media).paddingTop) || 0;
    var room = { w: media.clientWidth - 2 * pad - 12, h: media.clientHeight - 2 * pad - 12 };  // inside the bezel's 6 px rim
    var zw = room.w / used;
    // Every card shows the whole part, scaled down with its proportions kept, never a cropped slice (owner, 2026-10-24: a
    // zoomed-in slice "hinders a person's ability to even see what they are choosing").
    if (HUG.matches && item._hugW === Math.round(room.w)) {
      // one column, after the first fit: the card keeps its height whatever the view, so the page never jumps under a thumb
      // (owner, 2026-10-23); the other views are scaled to fit inside it
      room.h = item._hugH;
    } else if (HUG.matches) {
      // one column (a phone), first fit at this width: the card is as tall as the part at full width, up to 1.3 times its
      // width; a taller part is scaled down to fit that height
      room.h = Math.ceil(Math.min(live.offsetHeight * Math.min(1, zw), room.w * 1.3));
      media.style.height = (room.h + 12 + 2 * pad) + "px";
      item._hugW = Math.round(room.w); item._hugH = room.h;
    } else {
      item._hugW = null;
    }
    var z = Math.min(1, zw, room.h / Math.max(1, live.offsetHeight));
    scaleEl(live, z); fitBox.classList.remove("is-cropped");
    bezel.style.maxHeight = (room.h + 12) + "px"; fitBox.style.maxHeight = room.h + "px";
    media.style.borderRadius = "";
    var cap = (parseFloat(getComputedStyle(media).borderTopLeftRadius) || 0) * 0.8, rimR = nest(fitBox, bezel, live, z, cap);
    rescale(live);  // nest() may change the margin around the part
    // nest() may change the margin around the part (which reflows it), and text rounds up at small scales: check the drawn
    // height and scale down again until the whole part is inside the room
    for (var k = 0, drawn; k < 3 && (drawn = live.getBoundingClientRect().height) > room.h + 0.5; k++) {
      z *= room.h / drawn * 0.995; scaleEl(live, z); rimR = nest(fitBox, bezel, live, z, cap); rescale(live);
    }
    // a very round part (an overlay in a pill look): the tile's corner grows with it, up to the tile's own padding, so the frame
    // is never rounder than the tile and the gap stays at least the corner (where corners need not run parallel)
    if (rimR > cap + 0.5) media.style.borderRadius = Math.min(rimR / 0.8, pad - 0.5).toFixed(1) + "px";  // a very round part (an overlay in a pill look): the tile follows it out
    item.setAttribute("data-view", view);
    $$(".item-views i", item).forEach(function (i) { i.classList.toggle("is-on", i.getAttribute("data-v") === view); });
    var label = $(".item-view-t", item); if (label) label.textContent = view[0].toUpperCase() + view.slice(1);
    var link = $(".item-link", item); if (link) link.href = link.getAttribute("href").split("?")[0] + "?view=" + view;
  };
  // a part's first view, the same rule on its card and on its page: the part's own view, or a narrower one when the part would
  // sit as a thin band (a short, wide strip at 1280 px; at 768 px it wraps into rows). Measured on the part alone, so the card
  // and the page always agree; the click carries it as ?view=. On a phone screen, always the phone view.
  var firstView = function () { return defaultView(); };
  var bestView = function (item) { var v = firstView(item, $(".lib-live", item)); item.setAttribute("data-view-first", v); return v; };
  // aisle tiles: a part laid out at a card width and zoomed to the tile
  var fitTile = function (box) {
    var live = box.querySelector(".lib-live"); if (!live) return;
    var pv = box.closest(".aisle-prev"); if (pv) pv.style.contentVisibility = "visible";  // measured fully drawn (see fitItem)
    var w = +box.getAttribute("data-w") || 640;
    live.style.width = w + "px"; scaleEl(live, 1);
    var prev = box.closest(".aisle-prev"), z = Math.max(0.2, Math.min(1, prev.clientWidth / w));
    scaleEl(live, z);
    // a tile keeps one corner (the tile's minus its 14 px margin); the margin around the part is set so the part's corner,
    // at this scale, runs parallel to it
    var prevR = parseFloat(getComputedStyle(prev).borderTopLeftRadius) || 0;
    live.style.padding = Math.max(6, prevR / z - partR(live)).toFixed(1) + "px";
    rescale(live);
  };
  // Lazy: a card is laid out and sized only when it comes within about 600 px of the screen (91 live previews measured at
  // once cost over a second of layout on load). Photos inside previews already load lazily.
  var near = [];
  var fitItem = function (item) {
    if (item.hidden) return;
    item._fitting = true;
    // a card is measured fully drawn: under content-visibility the browser may skip a card's contents, and the part then
    // measures 0 px wide and is fitted as a sliver (Chrome and Safari, 2026-10-24)
    var m = $(".item-media", item); if (m) m.style.contentVisibility = "visible";
    var v = item.getAttribute("data-view");
    if (!v || item.getAttribute("data-view-first") !== defaultView()) v = bestView(item);  // first fit, or the screen crossed 768 px
    fitCard(item, v);
    var l = $(".item-media .lib-live", item); item._lh = l ? l.offsetHeight : 0; item._fitting = false;
  };
  var fitAll = function () {
    $$(".aisle-prev .lib-fit").forEach(fitTile);
    near.forEach(fitItem);
    fitDevice();
  };
  if (window.IntersectionObserver) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting || near.indexOf(e.target) >= 0) return;
        near.push(e.target); fitItem(e.target); io.unobserve(e.target);
      });
    }, { rootMargin: "600px 0px" });
    $$(".item").forEach(function (item) { io.observe(item); });
  } else { near = $$(".item"); }
  // refit on a real width change only (a card's own height change must not start another round)
  var lastW = innerWidth, pending = 0;
  window.addEventListener("resize", function () {
    if (innerWidth === lastW || pending) return;
    pending = requestAnimationFrame(function () { pending = 0; lastW = innerWidth; fitAll(); });
  });
  // a part that changes its own height (a tab inside it, an opened row) is fitted again, so its card still shows all of it
  if (window.ResizeObserver) {
    var liveRo = new ResizeObserver(function (entries) {
      entries.forEach(function (e) {
        var it = e.target.closest(".item"); if (!it || it._fitting || near.indexOf(it) < 0) return;
        if (Math.abs(e.target.offsetHeight - (it._lh || 0)) < 2) return;
        requestAnimationFrame(function () { fitItem(it); });
      });
    });
    $$(".item-media .lib-live").forEach(function (l) { liveRo.observe(l); });
  }
  if (window.ResizeObserver) { var ro = new ResizeObserver(function () { $$(".aisle-prev .lib-fit").forEach(fitTile); fitDevice(); }); $$(".aisle-prev, .part-stage").forEach(function (el) { ro.observe(el); }); }
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
      item.addEventListener("pointerenter", function () {
        start = setTimeout(function () { next(); timer = setInterval(next, 1600); if (!item._seenHover) { item._seenHover = 1; track("card_previewed", { part: item.id.slice(5) }); } }, 450);
      });
      item.addEventListener("pointerleave", function () {
        clearTimeout(start); clearInterval(timer);
        var home = item.getAttribute("data-view-first") || defaultView(item);
        if (item.getAttribute("data-view") !== home) swap($(".lib-live", item), function () { fitCard(item, home); });
      });
    });
  }

  // looks
  var LOOK_KEY = "od-library-look-v2";  // v2: the default moved to Nordic (2026-10-23); old saves were only the old default
  var current = store.get(LOOK_KEY, document.documentElement.getAttribute("data-default-look") || "nordic");
  var useLook = function (key) {
    if (!DATA.looks || !DATA.looks[key]) return;
    current = key; store.set(LOOK_KEY, key);
    $$(".lib-live").forEach(function (el) { el.className = el.className.replace(/odl-sys-[a-z]+/, "odl-sys-" + key); });
    $$(".look[data-look]").forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-look") === key ? "true" : "false"); });
    $$(".part-look").forEach(function (s) { s.value = key; });
    lookLabel();
    requestAnimationFrame(fitAll);
  };
  $$(".look[data-look]").forEach(function (b) { b.addEventListener("click", function () { useLook(b.getAttribute("data-look")); track("look_changed", { look: b.getAttribute("data-look"), from: location.pathname }); }); });
  $$(".item-link").forEach(function (a, i) { a.addEventListener("click", function () { var it = a.closest(".item"); track("part_opened", { part: it.id.slice(5), view: it.getAttribute("data-view"), position: i + 1, from: location.pathname }); }); });
  $$(".part-look").forEach(function (s) { s.addEventListener("change", function () { useLook(s.value); track("look_changed", { look: s.value, from: location.pathname }); }); });

  // filters: aisle tiles, type chips, style, industry and words, all at once
  var type = "all", q = $("#lib-q"), style = $("#lib-style"), industry = $("#lib-industry"), whoSel = $("#lib-who");
  var apply = function () {
    var words = q ? q.value.trim().toLowerCase().split(/\s+/).filter(Boolean) : [], shown = 0;
    $$(".shelf .item").forEach(function (c) {
      var ind = c.getAttribute("data-industries").split(" ");
      var ok = (type === "all" || c.getAttribute("data-type") === type)
        && (!style || !style.value || c.getAttribute("data-style") === style.value)
        && (!whoSel || !whoSel.value || c.getAttribute("data-who") === whoSel.value)
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
  $$(".aisle[data-aisle]").forEach(function (a) { a.addEventListener("click", function () { setType(a.getAttribute("data-aisle")); track("aisle_clicked", { type: a.getAttribute("data-aisle") }); }); });
  var filterT = 0, trackFilters = function () { clearTimeout(filterT); filterT = setTimeout(function () { track("library_filtered", { type: type, who: whoSel ? whoSel.value : "", style: style ? style.value : "", industry: industry ? industry.value : "", searched: !!(q && q.value), shown: +($(".shelf-count .n") || {}).textContent || 0 }); }, 1200); };
  [whoSel, style, industry, q].forEach(function (el) { if (el) el.addEventListener(el === q ? "input" : "change", trackFilters); });
  $$(".lib-filters .filter").forEach(function (b) { b.addEventListener("click", trackFilters); });
  [whoSel, style, industry].forEach(function (el) { if (el) el.addEventListener("change", apply); });
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
    var live = $(".lib-live", frame); scaleEl(frame, 1); frame.style.minHeight = "";
    var used = live ? layout(live, w) : w;
    live && (live.style.width = "");
    frame.style.width = used + "px";
    var avail = stage.clientWidth - parseFloat(getComputedStyle(stage).paddingLeft) * 2 - 12;  // 12: the glass rim, 6 px a side
    var z = Math.min(1, avail / used);
    scaleEl(frame, z);
    var devR = nest(frame, null, live, z); rescale(frame); dev.style.borderRadius = devR.toFixed(1) + "px";
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
    t.addEventListener("click", function (e) { pick(t.getAttribute("data-device"), e.detail > 0); track("view_switched", { part: location.pathname.split("/")[2], view: t.getAttribute("data-device") }); });  // keyboard switches stay instant
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
      var live = peek.firstChild; live.style.width = "390px"; scaleEl(live, 0.75);
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
      scaleEl(live, 56 / 390);  // the 56 px thumbnail shows the part at its phone width (fixed: the dialog may still be closed)
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
      track(i >= 0 ? "kit_removed" : "kit_added", { part: s, from: location.pathname, kit_size: kit.items.length });
      save();
    });
  });
  $$(".look-add").forEach(function (b) { b.addEventListener("click", function () { kit.look = kit.look === current ? null : current; save(); if (kit.look) bump(); track("kit_look_set", { look: kit.look || null }); }); });
  if (fab && dlg && dlg.showModal) {
    fab.addEventListener("click", function () {
      track("kit_opened", { parts: kit.items.length, look: kit.look || null, from: location.pathname });
      render(); $(".co-next", dlg).hidden = true; $(".co-star", dlg).hidden = true;
      $$(".co-pay", dlg).forEach(function (pay) { pay.classList.remove("is-done"); $("span", pay).textContent = "Copy prompt"; });
      dlg.showModal();
    });
    $(".kit-x", dlg).addEventListener("click", function () { dlg.close(); });
    var methods = $$(".co-method", dlg);
    methods.forEach(function (m, i) {
      m.addEventListener("click", function () { out = m.getAttribute("data-out"); render(); track("kit_method_chosen", { method: out }); });
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
      if (e.target.closest(".co-star-no")) { store.set(STAR_KEY, true); $(".co-star", dlg).hidden = true; track("star_ask_dismissed"); return; }
      var cmd = e.target.closest(".kit-copy-cmd");
      if (cmd) {
        var cl = cmd.querySelector("span"), ok = function () { cl.textContent = "Copied. Run them, then copy step 2"; };
        track("kit_commands_copied");
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
        track("kit_prompt_copied", { method: out, parts: kit.items.length, look: kit.look || null });
        if (navigator.clipboard) navigator.clipboard.writeText(prompt()).then(done, done); else done();
      }
    });
    $$(".co-star a", dlg).forEach(function (a) { a.addEventListener("click", function () { store.set(STAR_KEY, true); track("star_ask_clicked"); }); });
  }
  useLook(current);
  render();
})();
