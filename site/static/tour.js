/* The tour page (/tour/). Each diagram marked data-play plays once as it comes into view (tour.css holds the motion); one already
   on screen when the page loads, or any diagram under reduced motion, shows its final state at once. The file list is a vertical
   tab list, so Up and Down move through it as well as Left and Right (site.js handles the tabs themselves). */
(function () {
  var items = Array.prototype.slice.call(document.querySelectorAll("[data-play]"));
  var calm = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (calm || !("IntersectionObserver" in window)) {
    items.forEach(function (el) { el.classList.add("is-in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        en.target.classList.add("is-in");
        io.unobserve(en.target);
      });
    }, { rootMargin: "0px 0px -12% 0px" });
    items.forEach(function (el) {
      if (el.getBoundingClientRect().top < window.innerHeight) el.classList.add("is-in");
      else io.observe(el);
    });
    document.documentElement.classList.add("tr-js");
  }
  window.addEventListener("beforeprint", function () { items.forEach(function (el) { el.classList.add("is-in"); }); });

  document.querySelectorAll('[role="tablist"][aria-orientation="vertical"]').forEach(function (list) {
    var tabs = Array.prototype.slice.call(list.querySelectorAll('[role="tab"]'));
    list.addEventListener("keydown", function (e) {
      var i = tabs.indexOf(document.activeElement);
      if (i < 0 || (e.key !== "ArrowDown" && e.key !== "ArrowUp")) return;
      e.preventDefault();
      var next = tabs[(i + (e.key === "ArrowDown" ? 1 : -1) + tabs.length) % tabs.length];
      next.click();
      next.focus();
    });
  });
})();
