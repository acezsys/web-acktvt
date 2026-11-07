/* =====================================================================
   Diwali 2026 celebration — Prowessz Consulting & Team acktvt
   ---------------------------------------------------------------------
   On every page load or refresh until 12-Nov-2026 01:00 IST:
     6 seconds of a marigold toran, glowing diyas (3 designs), rising
     aakash kandils (3 designs), small crackers (anaar fountain, chakri),
     sky fireworks (peony burst, ring burst), a rangoli bloom and gold
     sparkles; plus a slim greeting strip the visitor can close (✕).
   After the end time it does nothing at all — no need to remove it.
   Preview any time on the live site:  ?diwalitest=1   (strip + animation)
   Respects "reduce motion": then only the greeting strip is shown.
   One file, no libraries, no network requests.
   ===================================================================== */
(function () {
  'use strict';
  var END = Date.UTC(2026, 10, 11, 19, 30, 0);          // 12-Nov-2026 01:00 IST
  var MESSAGE = 'Wishing you a joyous Diwali and a prosperous New Year';
  var SIGN = 'Prowessz Consulting & Team acktvt';
  var DURATION = 6000;                                   // ms

  var test = /[?&]diwalitest=1\b/.test(location.search);
  if (!test && Date.now() >= END) return;

  var reduce = false;
  try { reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e) {}

  function ready(fn) { if (document.readyState !== 'loading') fn(); else document.addEventListener('DOMContentLoaded', fn); }

  /* ------------------------------------------------ greeting strip */
  function strip() {
    var closed = false;
    try { closed = sessionStorage.getItem('dw26-closed') === '1'; } catch (e) {}
    if (closed && !test) return;
    var css = document.createElement('style');
    css.textContent =
      '.dw26{position:relative;z-index:9999;display:flex;align-items:center;justify-content:center;gap:10px;' +
      'padding:9px 44px 9px 16px;background:linear-gradient(90deg,#5a1406,#8a2a07 30%,#b0470b 50%,#8a2a07 70%,#5a1406);' +
      'color:#fff4d6;font:500 14px/1.35 inherit;font-family:inherit;text-align:center;letter-spacing:.1px;' +
      'box-shadow:0 1px 0 rgba(255,210,120,.35) inset,0 -1px 0 rgba(0,0,0,.2) inset}' +
      '.dw26 b{color:#ffd36b;font-weight:700}' +
      '.dw26 .dw26-sig{opacity:.85;font-weight:400;white-space:nowrap}' +
      '.dw26 .dw26-diya{font-size:16px;line-height:1}' +
      '.dw26 button{position:absolute;right:8px;top:50%;transform:translateY(-50%);width:30px;height:30px;border:0;' +
      'border-radius:50%;background:rgba(255,255,255,.12);color:#fff4d6;font:400 18px/30px inherit;font-family:inherit;cursor:pointer;padding:0}' +
      '.dw26 button:hover,.dw26 button:focus-visible{background:rgba(255,255,255,.25);outline:none}' +
      '.dw26 .dw26-short{display:none}' +
      '@media (max-width:600px){.dw26{font-size:12.5px;padding:8px 40px 8px 10px;flex-wrap:wrap;gap:1px 6px}.dw26 .dw26-diya,.dw26 .dw26-long{display:none}.dw26 .dw26-short{display:inline}}';
    document.head.appendChild(css);
    var el = document.createElement('div');
    el.className = 'dw26'; el.setAttribute('role', 'note'); el.setAttribute('aria-label', 'Diwali greeting');
    el.innerHTML = '<span class="dw26-diya" aria-hidden="true">🪔</span><span class="dw26-long"><b>Happy Diwali!</b> ' + MESSAGE + '</span>' +
      '<span class="dw26-short"><b>Happy Diwali</b> and a prosperous New Year!</span>' +
      '<span class="dw26-sig">— ' + SIGN + '</span><span class="dw26-diya" aria-hidden="true">🪔</span>' +
      '<button type="button" aria-label="Close the Diwali greeting">×</button>';
    el.querySelector('button').addEventListener('click', function () {
      el.remove(); try { sessionStorage.setItem('dw26-closed', '1'); } catch (e) {}
    });
    document.body.insertBefore(el, document.body.firstChild);
  }

  /* ------------------------------------------------ the 6-second show */
  function show() {
    var cv = document.createElement('canvas');
    cv.id = 'dw26-show'; cv.setAttribute('aria-hidden', 'true');
    cv.style.cssText = 'position:fixed;inset:0;width:100vw;height:100vh;pointer-events:none;z-index:2147483000';
    document.body.appendChild(cv);
    var ctx = cv.getContext('2d');
    if (!ctx) { cv.remove(); return; }
    var W, H, DPR, S;                           // S = scale for small screens
    function size() {
      DPR = Math.min(window.devicePixelRatio || 1, 2);
      W = window.innerWidth; H = window.innerHeight;
      cv.width = Math.round(W * DPR); cv.height = Math.round(H * DPR);
      ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
      S = Math.max(0.62, Math.min(1, W / 1100));
    }
    size(); window.addEventListener('resize', size);

    var R = Math.random, PI2 = Math.PI * 2;
    var GOLD = ['#ffd36b', '#ffe9a8', '#ffc02e', '#fff6d8'];
    var FIRE = [['#ffd36b', '#ff9f1c', '#fff1c1'], ['#ff5e7e', '#ffd1dc', '#ffb703'], ['#7ae7ff', '#d6f8ff', '#ffe066'], ['#b78cff', '#f0e1ff', '#ffd36b'], ['#7dff9b', '#e2ffe9', '#ffd36b']];

    /* ---- marigold toran across the top ---- */
    function marigold(x, y, r, c1, c2) {
      ctx.fillStyle = c1; ctx.beginPath(); ctx.arc(x, y, r, 0, PI2); ctx.fill();
      ctx.fillStyle = c2;
      for (var i = 0; i < 7; i++) { var a = i / 7 * PI2; ctx.beginPath(); ctx.arc(x + Math.cos(a) * r * .55, y + Math.sin(a) * r * .55, r * .36, 0, PI2); ctx.fill(); }
      ctx.fillStyle = 'rgba(120,40,0,.35)'; ctx.beginPath(); ctx.arc(x, y, r * .25, 0, PI2); ctx.fill();
    }
    function leaf(x, y, len, ang) {
      ctx.save(); ctx.translate(x, y); ctx.rotate(ang);
      ctx.fillStyle = '#2f7d32'; ctx.beginPath(); ctx.moveTo(0, 0);
      ctx.quadraticCurveTo(len * .45, len * .32, 0, len); ctx.quadraticCurveTo(-len * .45, len * .32, 0, 0); ctx.fill();
      ctx.strokeStyle = 'rgba(200,255,190,.45)'; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(0, 2); ctx.lineTo(0, len - 2); ctx.stroke();
      ctx.restore();
    }
    function toran(t) {
      var drop = Math.min(1, t / 600), y0 = -60 * Math.pow(1 - drop, 3);             // slides in from above
      var st = document.querySelector('.dw26'); if (st) y0 += Math.max(0, st.getBoundingClientRect().bottom);   // hangs just below the greeting strip
      ctx.save(); ctx.translate(0, y0);
      var n = Math.max(4, Math.round(W / 190)), seg = W / n, r = 7.5 * S + 2, sag = 26 * S + 10;
      // mango leaves along the top edge
      for (var lx = 6; lx < W; lx += 26 * S + 6) leaf(lx, -4, 22 * S + 8, (Math.sin(lx) * .25));
      for (var s = 0; s < n; s++) {
        var xa = s * seg, xb = xa + seg;
        for (var k = 0; k <= 14; k++) {                                    // swag of flowers
          var u = k / 14, x = xa + u * seg, y = 10 + Math.sin(u * Math.PI) * sag;
          marigold(x, y, r, k % 2 ? '#ff9f1c' : '#ffc300', k % 2 ? '#ffb347' : '#ffd84d');
        }
        // hanging string at the hook with three flowers and a bell-shaped tassel
        var hx = xa, sway = Math.sin(t / 380 + s) * 3;
        for (var j = 1; j <= 3; j++) marigold(hx + sway * j / 3, 10 + j * (r * 2.1), r * .9, j % 2 ? '#ff7b00' : '#ffc300', j % 2 ? '#ff9f43' : '#ffd84d');
        ctx.fillStyle = '#c0392b'; ctx.beginPath(); ctx.arc(hx + sway, 14 + 4 * r * 2.1, r * .55, 0, PI2); ctx.fill();
      }
      ctx.restore();
    }

    /* ---- diyas along the bottom (3 designs) ---- */
    var diyas = [];
    function placeDiyas() {
      diyas = []; var gap = 120 * S + 30, n = Math.max(4, Math.floor(W / gap));
      for (var i = 0; i < n; i++) diyas.push({ x: (i + .5) * (W / n), d: i % 3, ph: R() * 10 });
    }
    placeDiyas(); window.addEventListener('resize', placeDiyas);
    function flame(x, y, h, ph, t) {
      var f = 1 + Math.sin(t / 90 + ph) * .08 + Math.sin(t / 37 + ph * 2) * .05;
      var g = ctx.createRadialGradient(x, y - h * .5, 1, x, y - h * .5, h * 2.2);
      g.addColorStop(0, 'rgba(255,200,80,.55)'); g.addColorStop(1, 'rgba(255,140,0,0)');
      ctx.fillStyle = g; ctx.beginPath(); ctx.arc(x, y - h * .5, h * 2.2, 0, PI2); ctx.fill();
      ctx.save(); ctx.translate(x, y); ctx.scale(1, f);
      var g2 = ctx.createLinearGradient(0, 0, 0, -h);
      g2.addColorStop(0, '#ff6a00'); g2.addColorStop(.55, '#ffc300'); g2.addColorStop(1, '#fff7d1');
      ctx.fillStyle = g2; ctx.beginPath(); ctx.moveTo(0, -h);
      ctx.bezierCurveTo(h * .45, -h * .45, h * .32, 0, 0, 0); ctx.bezierCurveTo(-h * .32, 0, -h * .45, -h * .45, 0, -h); ctx.fill();
      ctx.restore();
    }
    function diya(o, t) {
      var w = 46 * S + 8, x = o.x, y = H - 10;
      ctx.save();
      if (o.d === 0) {                       // classic clay diya with a pointed lip
        ctx.fillStyle = '#a0461c'; ctx.beginPath(); ctx.moveTo(x - w * .5, y - w * .28);
        ctx.quadraticCurveTo(x, y + w * .12, x + w * .62, y - w * .34); ctx.lineTo(x + w * .3, y - w * .26);
        ctx.quadraticCurveTo(x, y - w * .2, x - w * .5, y - w * .28); ctx.fill();
        ctx.fillStyle = '#d9772b'; ctx.fillRect(x - w * .42, y - w * .3, w * .8, 3);
        flame(x + w * .5, y - w * .36, 18 * S + 6, o.ph, t);
      } else if (o.d === 1) {                // painted diya: round bowl with dots
        ctx.fillStyle = '#c0392b'; ctx.beginPath(); ctx.ellipse(x, y - w * .18, w * .5, w * .24, 0, 0, Math.PI); ctx.fill();
        ctx.fillStyle = '#e8a33d'; ctx.beginPath(); ctx.ellipse(x, y - w * .18, w * .5, w * .07, 0, 0, PI2); ctx.fill();
        ctx.fillStyle = '#ffe08a';
        for (var i = -2; i <= 2; i++) { ctx.beginPath(); ctx.arc(x + i * w * .17, y - w * .06 + Math.abs(i) * -1.5, 2.2, 0, PI2); ctx.fill(); }
        flame(x, y - w * .22, 20 * S + 6, o.ph, t);
      } else {                               // brass diya on a little stand, petal rim
        ctx.fillStyle = '#b8860b'; ctx.fillRect(x - w * .1, y - w * .2, w * .2, w * .2);
        ctx.fillRect(x - w * .28, y - 4, w * .56, 4);
        ctx.fillStyle = '#d4a017';
        for (var p = 0; p < 6; p++) { var a = Math.PI + p / 5 * Math.PI; ctx.beginPath(); ctx.ellipse(x + Math.cos(a) * w * .3, y - w * .32 + Math.sin(a) * w * .1, w * .13, w * .07, a, 0, PI2); ctx.fill(); }
        ctx.fillStyle = '#f1c40f'; ctx.beginPath(); ctx.ellipse(x, y - w * .32, w * .36, w * .1, 0, 0, Math.PI); ctx.fill();
        flame(x, y - w * .36, 19 * S + 6, o.ph, t);
      }
      ctx.restore();
    }

    /* ---- aakash kandils rising (3 designs) ---- */
    var kandils = [];
    (function () {
      var n = Math.max(4, Math.min(8, Math.round(W / 220)));
      for (var i = 0; i < n; i++) kandils.push({ x: (i + .5) / n * W + (R() - .5) * 60, y: H + 40 + R() * H * .35, d: i % 3,
        v: (H * .55 + R() * H * .2) / DURATION, ph: R() * 6, c: [['#ff5e3a', '#ffd36b'], ['#ffb703', '#ff3d7f'], ['#e63946', '#ffd166'], ['#ff8800', '#7b2cbf']][i % 4] });
    })();
    function tassel(x, y, len, col) { ctx.strokeStyle = col; ctx.lineWidth = 1.5; for (var i = -2; i <= 2; i++) { ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(x + i * 2.5, y + len); ctx.stroke(); } }
    function kandil(k, t) {
      var s = (30 * S + 10), x = k.x + Math.sin(t / 700 + k.ph) * 12, y = k.y - k.v * t;
      ctx.save(); ctx.translate(x, y); ctx.rotate(Math.sin(t / 900 + k.ph) * .06);
      var glow = ctx.createRadialGradient(0, 0, 2, 0, 0, s * 1.6); glow.addColorStop(0, 'rgba(255,190,90,.45)'); glow.addColorStop(1, 'rgba(255,150,40,0)');
      ctx.fillStyle = glow; ctx.beginPath(); ctx.arc(0, 0, s * 1.6, 0, PI2); ctx.fill();
      if (k.d === 0) {                       // star kandil (5 points)
        ctx.fillStyle = k.c[0]; ctx.beginPath();
        for (var i = 0; i < 10; i++) { var a = -Math.PI / 2 + i * Math.PI / 5, rr = i % 2 ? s * .45 : s; ctx.lineTo(Math.cos(a) * rr, Math.sin(a) * rr); }
        ctx.closePath(); ctx.fill(); ctx.strokeStyle = k.c[1]; ctx.lineWidth = 2; ctx.stroke();
        ctx.fillStyle = 'rgba(255,240,180,.75)'; ctx.beginPath(); ctx.arc(0, 0, s * .22, 0, PI2); ctx.fill();
        tassel(0, s * .5, s * .9, k.c[1]);
      } else if (k.d === 1) {                // traditional hexagonal kandil with a frilled skirt
        ctx.fillStyle = k.c[0]; ctx.beginPath();
        ctx.moveTo(-s * .35, -s * .8); ctx.lineTo(s * .35, -s * .8); ctx.lineTo(s * .7, -s * .2); ctx.lineTo(s * .7, s * .2);
        ctx.lineTo(s * .35, s * .6); ctx.lineTo(-s * .35, s * .6); ctx.lineTo(-s * .7, s * .2); ctx.lineTo(-s * .7, -s * .2); ctx.closePath(); ctx.fill();
        ctx.fillStyle = k.c[1]; ctx.fillRect(-s * .7, -s * .08, s * 1.4, s * .16);
        ctx.fillStyle = 'rgba(255,245,200,.6)'; ctx.fillRect(-s * .12, -s * .7, s * .24, s * 1.2);
        for (var f = -3; f <= 3; f++) { ctx.fillStyle = f % 2 ? k.c[1] : k.c[0]; ctx.fillRect(f * s * .12 - s * .05, s * .6, s * .1, s * .55); }
      } else {                               // round paper lantern with ribs
        ctx.fillStyle = k.c[0]; ctx.beginPath(); ctx.ellipse(0, 0, s * .62, s * .75, 0, 0, PI2); ctx.fill();
        ctx.strokeStyle = 'rgba(0,0,0,.18)'; ctx.lineWidth = 1.2;
        for (var r2 = -2; r2 <= 2; r2++) { ctx.beginPath(); ctx.ellipse(0, 0, Math.abs(r2) * s * .14 + .5, s * .75, 0, 0, PI2); ctx.stroke(); }
        ctx.fillStyle = k.c[1]; ctx.fillRect(-s * .3, -s * .85, s * .6, s * .14); ctx.fillRect(-s * .3, s * .72, s * .6, s * .14);
        tassel(0, s * .86, s * .7, k.c[1]);
      }
      ctx.restore();
    }

    /* ---- particles for fireworks, crackers and sparkles ---- */
    var parts = [];
    function spark(x, y, vx, vy, life, col, sz, grav, trail) { parts.push({ x: x, y: y, vx: vx, vy: vy, life: life, max: life, c: col, s: sz, g: grav, tr: trail }); }

    // sky fireworks: rocket → burst (peony = full sphere; ring = circle with a gold core)
    var rockets = [];
    var plan = [[500, 'peony'], [1350, 'ring'], [2300, 'peony'], [3200, 'ring'], [4000, 'peony'], [4600, 'ring']];
    function launch(kind) {
      rockets.push({ x: W * (.15 + R() * .7), y: H, ty: H * (.14 + R() * .22), vy: -(H * .9) / 900, kind: kind, pal: FIRE[Math.floor(R() * FIRE.length)] });
    }
    function burst(r) {
      var n = Math.round((r.kind === 'peony' ? 70 : 46) * (0.7 + S * .3)), sp = (r.kind === 'peony' ? 3.4 : 3.0) * (0.75 + S * .25);
      for (var i = 0; i < n; i++) {
        var a = i / n * PI2 + R() * .05, v = r.kind === 'peony' ? sp * (.35 + R() * .65) : sp;
        spark(r.x, r.y, Math.cos(a) * v, Math.sin(a) * v, 1100 + R() * 500, r.pal[i % 3], (r.kind === 'peony' ? 2.6 : 2.9) * (0.8 + S * .2), .028, true);
      }
      if (r.kind === 'ring') for (var j = 0; j < 18; j++) { var b = R() * PI2, w = R() * 1.2; spark(r.x, r.y, Math.cos(b) * w, Math.sin(b) * w, 900, '#fff1c1', 1.8, .02, false); }
    }

    // small crackers: anaar (flower-pot fountain) and chakri (spinning wheel)
    var anaars = [{ x: .2, on: 700, off: 4700 }, { x: .8, on: 1100, off: 5100 }];
    var chakris = [{ x: .35, on: 1600, off: 5200 }, { x: .65, on: 2000, off: 5400 }];
    function anaarPot(x, y) {
      var w = 14 * S + 6;
      ctx.fillStyle = '#b5651d'; ctx.beginPath(); ctx.moveTo(x - w * .5, y); ctx.lineTo(x + w * .5, y); ctx.lineTo(x + w * .2, y - w); ctx.lineTo(x - w * .2, y - w); ctx.closePath(); ctx.fill();
      ctx.fillStyle = '#e9c46a'; ctx.fillRect(x - w * .35, y - w * .55, w * .7, 3);
    }

    // rangoli at the bottom centre: blooms open, turns slowly
    function rangoli(t) {
      var p = Math.min(1, t / 1400), e = 1 - Math.pow(1 - p, 3), R0 = (70 * S + 22) * e, cx = W / 2, cy = H - (54 * S + 30);
      if (R0 < 2) return;
      ctx.save(); ctx.translate(cx, cy); ctx.scale(1, .42); ctx.rotate(t / 4000);
      var rings = [['#e63946', 12, 1], ['#ffb703', 12, .78], ['#2a9d8f', 8, .56], ['#8338ec', 8, .36]];
      for (var q = 0; q < rings.length; q++) {
        var col = rings[q][0], n = rings[q][1], rr = R0 * rings[q][2];
        for (var i = 0; i < n; i++) {
          var a = i / n * PI2 + q * .2; ctx.save(); ctx.rotate(a); ctx.fillStyle = col;
          ctx.beginPath(); ctx.ellipse(rr * .62, 0, rr * .38, rr * .14, 0, 0, PI2); ctx.fill(); ctx.restore();
        }
      }
      ctx.fillStyle = '#fff'; for (var d = 0; d < 16; d++) { var b = d / 16 * PI2; ctx.beginPath(); ctx.arc(Math.cos(b) * R0 * 1.02, Math.sin(b) * R0 * 1.02, 2.4, 0, PI2); ctx.fill(); }
      ctx.fillStyle = '#ffd36b'; ctx.beginPath(); ctx.arc(0, 0, R0 * .14, 0, PI2); ctx.fill();
      ctx.restore();
    }

    /* ---- the frame loop ---- */
    var t0 = null, last = null, planned = 0;
    function frame(ts) {
      if (t0 === null) { t0 = ts; last = ts; }
      var t = ts - t0, dt = Math.min(40, ts - last), kf = dt / 16.7; last = ts;   // real time, so 60 Hz and 120 Hz screens look the same
      if (t > DURATION) { cv.remove(); window.removeEventListener('resize', size); window.removeEventListener('resize', placeDiyas); return; }
      var fade = t < 300 ? t / 300 : (t > DURATION - 800 ? (DURATION - t) / 800 : 1);
      ctx.clearRect(0, 0, W, H);
      ctx.globalAlpha = fade;

      // a light dusk wash so the lights read on white pages
      var wash = ctx.createLinearGradient(0, 0, 0, H);
      wash.addColorStop(0, 'rgba(20,8,40,.42)'); wash.addColorStop(.6, 'rgba(40,12,30,.30)'); wash.addColorStop(1, 'rgba(60,20,10,.38)');
      ctx.fillStyle = wash; ctx.fillRect(0, 0, W, H);

      while (planned < plan.length && t >= plan[planned][0]) { launch(plan[planned][1]); planned++; }

      for (var k = 0; k < kandils.length; k++) kandil(kandils[k], t);

      for (var r = rockets.length - 1; r >= 0; r--) {
        var ro = rockets[r]; ro.y += ro.vy * dt;
        spark(ro.x + (R() - .5) * 2, ro.y + 6, (R() - .5) * .3, .8, 380, '#ffd36b', 1.5, 0, false);
        if (ro.y <= ro.ty) { burst(ro); rockets.splice(r, 1); }
      }

      for (var a = 0; a < anaars.length; a++) {
        var an = anaars[a], ax = an.x * W, ay = H - (64 * S + 12);
        if (t > an.on && t < an.off) for (var m = 0; m < 5; m++) { var ang = -Math.PI / 2 + (R() - .5) * .7, v = 3 + R() * 3.4; spark(ax, ay - 12, Math.cos(ang) * v, Math.sin(ang) * v, 650 + R() * 400, GOLD[Math.floor(R() * 4)], 1.7, .09, false); }
        if (t > an.on - 400) anaarPot(ax, ay);
      }
      for (var c = 0; c < chakris.length; c++) {
        var ch = chakris[c], cx = ch.x * W, cy = H - (120 * S + 40);
        if (t > ch.on && t < ch.off) {
          var spin = t / 40;
          for (var q = 0; q < 3; q++) { var b2 = spin + q * PI2 / 3; spark(cx + Math.cos(b2) * 8, cy + Math.sin(b2) * 8, Math.cos(b2 + 1.3) * 3.2, Math.sin(b2 + 1.3) * 3.2, 420, q ? '#ffe9a8' : '#7ae7ff', 1.7, .03, false); }
          ctx.fillStyle = '#ff9f1c'; ctx.beginPath(); ctx.arc(cx, cy, 5, 0, PI2); ctx.fill();
        }
      }

      // gold sparkles twinkling across the page
      if (R() < .6) spark(R() * W, R() * H * .8, 0, 0, 500 + R() * 600, GOLD[Math.floor(R() * 4)], 1.2 + R() * 1.6, 0, false);

      // particles
      // normal blending so the sparks show on light pages as well as dark ones
      for (var i = parts.length - 1; i >= 0; i--) {
        var p = parts[i]; p.life -= dt;
        if (p.life <= 0) { parts.splice(i, 1); continue; }
        var dmp = Math.pow(.985, kf); p.vx *= dmp; p.vy = p.vy * dmp + p.g * kf; p.x += p.vx * kf; p.y += p.vy * kf;
        var al = Math.max(0, p.life / p.max);
        ctx.globalAlpha = fade * al;
        ctx.fillStyle = p.c;
        if (p.tr) { ctx.fillRect(p.x - p.vx * 2, p.y - p.vy * 2, p.s, p.s); }
        ctx.beginPath(); ctx.arc(p.x, p.y, p.s * (p.g ? 1 : (.6 + .4 * Math.sin(p.life / 60))), 0, PI2); ctx.fill();
      }
      ctx.globalAlpha = fade;

      rangoli(t);
      for (var dI = 0; dI < diyas.length; dI++) diya(diyas[dI], t);
      toran(t);

      if (parts.length > 2600) parts.splice(0, parts.length - 2600);       // keep phones smooth
      requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  }

  ready(function () {
    try { strip(); } catch (e) {}
    if (!reduce) { try { show(); } catch (e) {} }
  });
})();
