// Kleine dingen: diavoorstelling op home, foto groot bekijken.
(function () {
  var slides = document.querySelectorAll('.hero .slide');
  var still = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (slides.length > 1 && !still) {
    var i = 0;
    setInterval(function () {
      slides[i].classList.remove('on');
      i = (i + 1) % slides.length;
      var img = slides[i].querySelector('img');
      if (img && img.loading === 'lazy') img.loading = 'eager';
      slides[i].classList.add('on');
    }, 4500);
  }

  // beeldenrij op home: steeds een ander tegeltje wisselt naar een ander beeld
  var mos = document.querySelector('.mosaic'), poolEl = document.getElementById('pool');
  if (mos && poolEl && !still) {
    var pool = JSON.parse(poolEl.textContent), tiles = mos.querySelectorAll('a'), last = -1;
    var shown = function () { return [].map.call(tiles, function (a) { return a.getAttribute('data-k'); }); };
    var swap = function () {
      if (document.hidden) return;
      var t; do { t = Math.floor(Math.random() * tiles.length); } while (t === last && tiles.length > 1);
      last = t;
      var cur = shown(), cand = pool.filter(function (p) { return cur.indexOf(p[0]) < 0; });
      if (!cand.length) return;
      var p = cand[Math.floor(Math.random() * cand.length)], a = tiles[t], img = a.querySelector('img');
      var pre = new Image();
      pre.onload = function () {
        a.classList.add('fade');
        setTimeout(function () {
          img.removeAttribute('srcset'); img.src = pre.src; img.alt = p[2];
          a.href = mos.getAttribute('data-root') + 'werk/' + p[1] + '.html'; a.title = p[2];
          a.setAttribute('data-k', p[0]);
          a.className = p[0].indexOf('poster') === 0 ? 'poster' : 'scene';
        }, 600);
      };
      pre.src = mos.getAttribute('data-img') + p[0] + '-sm.jpg';
    };
    setInterval(swap, 2200);
  }

  // wisselende citaten op home
  var qEl = document.getElementById('quotes'), qBox = document.querySelector('.quote');
  if (qEl && qBox && !still) {
    var Qs = JSON.parse(qEl.textContent), qi = 0;
    var order = Qs.map(function (_, i) { return i; }).slice(1);
    for (var k = order.length - 1; k > 0; k--) { var r = Math.floor(Math.random() * (k + 1)); var tmp = order[k]; order[k] = order[r]; order[r] = tmp; }
    order.unshift(0);
    setInterval(function () {
      if (document.hidden) return;
      qi = (qi + 1) % order.length;
      var q = Qs[order[qi]];
      qBox.classList.add('fade');
      setTimeout(function () {
        var ln = qBox.querySelector('.line'); ln.innerHTML = q.t; ln.className = q.l ? 'line long' : 'line';
        var a = qBox.querySelector('.who'); a.href = q.u;
        a.querySelector('.n').innerHTML = q.n; a.querySelector('.p').innerHTML = q.p;
        qBox.classList.remove('fade');
      }, 700);
    }, 9000);
  }

  var box = document.querySelector('.lightbox');
  if (!box) return;
  var big = box.querySelector('img');
  var btn = box.querySelector('button');
  var last = null;
  function close() { box.hidden = true; big.removeAttribute('src'); if (last) last.focus(); }
  document.addEventListener('click', function (e) {
    var t = e.target;
    if (t.matches && t.matches('img[data-full]')) {
      last = t; big.src = t.getAttribute('data-full'); big.alt = t.alt || '';
      box.hidden = false; btn.focus();
    } else if (t === box || t === btn) { close(); }
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !box.hidden) close(); });
})();
