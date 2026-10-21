// Status filters on the shipments page
document.querySelectorAll('.filter').forEach(function (b) {
  b.addEventListener('click', function () {
    document.querySelectorAll('.filter').forEach(function (x) { x.classList.remove('on'); });
    b.classList.add('on');
    var f = b.dataset.f;
    document.querySelectorAll('#list tbody tr').forEach(function (r) {
      r.style.display = (f === 'all' || r.dataset.s === f) ? '' : 'none';
    });
  });
});

// Search
var s = document.querySelector('.search');
if (s) {
  s.addEventListener('input', function () {
    var q = s.value.toLowerCase();
    document.querySelectorAll('#list tbody tr').forEach(function (r) {
      r.style.display = r.textContent.toLowerCase().indexOf(q) > -1 ? '' : 'none';
    });
  });
}

// Settings toggles (div, not a real control)
document.querySelectorAll('.switch').forEach(function (t) {
  t.addEventListener('click', function () { t.classList.toggle('on'); });
});
