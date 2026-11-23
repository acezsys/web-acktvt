# ---------------------------------------------------------------- "Is your business in control?" check  (acktvt.com/check/)
# Run from build_pages.py (exec), which provides nav, footer, style, head_meta, EXTRA_CSS, SEO_HEAD, HERE, src, WA, DEMO_BMS.
# Answers go to the console database through two public functions (migration 0103):
#   public_survey_submit  -> score, band and tips worked out on the server, plus a one-time token
#   public_survey_contact -> optional name / company / WhatsApp / e-mail with consent, using that token
CHECK_TEXT = json.load(open(os.path.join(HERE, 'check', 'survey_text.json'), encoding='utf-8'))
_ms = re.search(r"const MS_URL = '(https://[^']+?)/rest/v1/rpc/public_milestones'", src)
_mk = re.search(r"const MS_KEY = '([^']+)'", src)
CHECK_API = (_ms.group(1) + '/rest/v1/rpc/') if _ms else 'REPLACE-WITH-SUPABASE-URL/rest/v1/rpc/'
CHECK_KEY = _mk.group(1) if _mk else 'REPLACE-WITH-ANON-KEY'

CHECK_CSS = """
<style>
  .chk-wrap{max-width:780px;margin:-48px auto 0;padding:0 20px 90px;position:relative}
  .chk-card{background:#fff;color:var(--ink);border-radius:var(--radius);box-shadow:0 30px 80px rgba(0,0,0,.18),0 0 0 1px var(--line);padding:30px 32px 28px}
  .chk-top{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:10px;font-size:13.5px;color:var(--ink-soft)}
  .chk-bar{height:6px;border-radius:99px;background:var(--paper);overflow:hidden;margin-bottom:24px;box-shadow:inset 0 0 0 1px var(--line)}
  .chk-bar i{display:block;height:100%;width:0;background:linear-gradient(90deg,var(--green),#2FA36F);border-radius:99px;transition:width .3s}
  .chk-q{border:0;margin:0;padding:0;min-width:0}
  .chk-q[hidden]{display:none}
  .chk-q legend{font-family:inherit;font-size:clamp(21px,2.6vw,26px);font-weight:700;line-height:1.3;color:var(--ink);margin-bottom:6px;padding:0}
  .chk-hint{font-size:14px;color:var(--ink-soft);margin:0 0 16px}
  .chk-hint b{color:var(--green-deep)}
  .chk-opts{display:grid;gap:10px;margin-top:14px}
  .chk-opt{display:flex;align-items:center;gap:14px;border:1.5px solid var(--line);border-radius:14px;padding:14px 16px;cursor:pointer;background:#fff;transition:border-color .15s,background .15s;min-height:56px}
  .chk-opt:hover{border-color:var(--green)}
  .chk-opt input{position:absolute;opacity:0;width:1px;height:1px}
  .chk-opt .dot{width:22px;height:22px;border-radius:50%;border:2px solid #9AA8A1;flex:none;display:grid;place-items:center;transition:all .15s}
  .chk-opt.multi .dot{border-radius:6px}
  .chk-opt .txt b{display:block;font-size:16px;font-weight:600;color:var(--ink)}
  .chk-opt .txt small{display:block;font-size:13px;color:var(--ink-soft);margin-top:2px}
  .chk-opt.on{border-color:var(--green);background:var(--mint-soft)}
  .chk-opt.on .dot{border-color:var(--green);background:var(--green)}
  .chk-opt.on .dot::after{content:"";width:8px;height:8px;border-radius:50%;background:#fff}
  .chk-opt.multi.on .dot::after{width:10px;height:6px;border-radius:0;background:none;border:2.5px solid #fff;border-top:0;border-right:0;transform:rotate(-45deg) translate(1px,-1px)}
  .chk-opt:has(input:focus-visible){outline:3px solid var(--mint);outline-offset:2px}
  .chk-opt.off{opacity:.55}
  .chk-msg{min-height:22px;margin:14px 0 0;font-size:14px;color:#A3241D;font-weight:500}
  .chk-nav{display:flex;justify-content:space-between;align-items:center;gap:12px;margin-top:18px}
  .chk-nav .btn[disabled]{opacity:.45;cursor:not-allowed;transform:none;box-shadow:none}
  .chk-ghost{background:#fff;border:1.5px solid var(--line);color:var(--ink-2);box-shadow:none}
  .chk-ghost:hover{border-color:var(--ink-soft);background:#fff}
  .chk-res[hidden],.chk-quiz[hidden],.chk-wait[hidden]{display:none}
  .chk-wait{text-align:center;padding:50px 0;color:var(--ink-soft)}
  .chk-score{display:flex;gap:26px;align-items:center;padding-bottom:22px;border-bottom:1px solid var(--line);margin-bottom:22px}
  .chk-ring{--p:0;width:132px;height:132px;border-radius:50%;flex:none;display:grid;place-items:center;background:conic-gradient(var(--ring) calc(var(--p)*1%),#E8EEEA 0)}
  .chk-ring div{width:104px;height:104px;border-radius:50%;background:#fff;display:grid;place-items:center;text-align:center}
  .chk-ring b{font-size:34px;line-height:1;color:var(--ink)}
  .chk-ring small{display:block;font-size:11.5px;color:var(--ink-soft);margin-top:4px;letter-spacing:.3px}
  .chk-band{display:inline-block;font-size:13px;font-weight:700;letter-spacing:.4px;text-transform:uppercase;padding:5px 12px;border-radius:99px;margin-bottom:8px}
  .chk-score h2{font-size:clamp(22px,2.8vw,28px);margin:0 0 6px}
  .chk-score p{margin:0;color:var(--ink-2);font-size:15.5px;line-height:1.55}
  .chk-tips h3{font-size:19px;margin:0 0 12px}
  .chk-tip{border:1px solid var(--line);border-radius:14px;padding:16px 18px;margin-bottom:12px;background:#FCFCFA}
  .chk-tip b{display:block;font-size:16.5px;margin-bottom:4px;color:var(--ink)}
  .chk-tip p{margin:0;font-size:15px;color:var(--ink-2);line-height:1.55}
  .chk-tip .how{margin-top:8px;font-size:13.5px;color:var(--green-deep)}
  .chk-tip .how em{font-style:normal;font-weight:600}
  .chk-lead{margin-top:24px;padding:22px;border-radius:16px;background:linear-gradient(160deg,#0B3D2A,#062A1C);color:#fff}
  .chk-lead h3{color:#fff;font-size:20px;margin:0 0 4px}
  .chk-lead .sub{color:rgba(255,255,255,.78);font-size:14.5px;margin:0 0 16px}
  .chk-lead .f label{color:rgba(255,255,255,.9)}
  .chk-lead .f input{border-color:transparent}
  .chk-lead .consent{color:rgba(255,255,255,.8)}
  .chk-lead .consent a{color:#FFD873}
  .chk-lead .err{display:none}
  .chk-lead .note{color:rgba(255,255,255,.7)}
  .chk-done{text-align:center;padding:10px 0}
  .chk-done b{display:block;font-size:19px;margin-bottom:6px}
  .chk-guide{margin:18px auto 0;max-width:460px;text-align:left;border:1px solid rgba(255,216,115,.45);border-radius:12px;padding:14px 16px;background:rgba(255,255,255,.04)}
  .chk-guide span{display:block;font-size:11.5px;letter-spacing:1px;text-transform:uppercase;color:#FFD873;font-weight:700}
  .chk-guide b{display:block;font-size:18px;margin:6px 0 2px}
  .chk-guide p{margin:0 0 12px;font-size:14px;opacity:.85}
  .chk-share{display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin-top:22px;font-size:14px;color:var(--ink-soft)}
  .chk-share a,.chk-share button{font:inherit;font-size:13.5px;font-weight:600;border:1.5px solid var(--line);border-radius:99px;padding:8px 14px;background:#fff;color:var(--ink-2);cursor:pointer;text-decoration:none}
  .chk-share a:hover,.chk-share button:hover{border-color:var(--green);color:var(--green-deep)}
  .chk-foot{margin-top:16px;font-size:12.5px;color:var(--ink-soft)}
  @media (max-width:640px){
    .chk-wrap{padding:0 12px 70px;margin-top:-36px}
    .chk-card{padding:22px 18px 20px}
    .chk-score{flex-direction:column;align-items:flex-start;gap:16px}
    .chk-lead{padding:18px 16px}
    .page.chk-hero{padding-bottom:64px!important}
  }
</style>
"""

def _esc(t):
    return (t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;'))

def _q_html(i, q):
    multi = q['multi']
    t = 'checkbox' if multi else 'radio'
    hint = f'<p class="chk-hint" id="{q["id"]}-hint">{_esc(q["hint"])} · <b class="cnt">0 of {q.get("max", 1)} picked</b></p>' if multi else '<p class="chk-hint">Choose one</p>'
    opts = ''.join(
        f'<label class="chk-opt{" multi" if multi else ""}"><input type="{t}" name="{q["id"]}" value="{v}"><span class="dot" aria-hidden="true"></span>'
        f'<span class="txt"><b>{_esc(lbl)}</b>{("<small>" + _esc(sub) + "</small>") if sub else ""}</span></label>'
        for v, lbl, sub in q['options'])
    return (f'<fieldset class="chk-q" data-q="{q["id"]}" data-multi="{1 if multi else 0}" data-max="{q.get("max", 1)}"{"" if i == 0 else " hidden"}>'
            f'<legend>{_esc(q["text"])}</legend>{hint}<div class="chk-opts">{opts}</div></fieldset>')

CHECK_JS = """
<script>
(() => {
  document.getElementById('year').textContent = new Date().getFullYear();
  document.getElementById('burger')?.addEventListener('click', () => { const n = document.getElementById('nav'); const open = n.classList.toggle('open'); document.getElementById('burger').setAttribute('aria-expanded', open); });
  const T = __TEXT__, API = '__API__', KEY = '__KEY__';
  const QS = T.questions, N = QS.length;
  const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const sets = $$('.chk-q'), bar = $('#chk-bar'), step = $('#chk-step'), msg = $('#chk-msg'), back = $('#chk-back'), next = $('#chk-next');
  const quiz = $('#chk-quiz'), wait = $('#chk-wait'), res = $('#chk-res');
  let cur = 0, started = 0, sent = null;
  const params = new URLSearchParams(location.search);
  const source = (params.get('src') || params.get('utm_source') || (document.referrer && !document.referrer.includes(location.host) ? 'other-link' : 'direct')).toLowerCase().slice(0, 40);
  const campaign = (params.get('c') || params.get('utm_campaign') || 'none').toLowerCase().slice(0, 40);
  const coarse = matchMedia('(pointer: coarse)').matches;
  const device = coarse ? (Math.min(screen.width, screen.height) >= 600 ? 'tablet' : 'mobile') : 'laptop-desktop';

  // ---- answers: exactly one for single-choice questions, 1 to max for multiple-choice
  const picked = (fs) => $$('input:checked', fs).map(i => i.value);
  const check = (k) => {
    const fs = sets[k], v = picked(fs), multi = fs.dataset.multi === '1', max = +fs.dataset.max;
    if (multi) { if (v.length === 0) return 'Please pick at least one.'; if (v.length > max) return 'Please pick up to ' + max + '.'; return ''; }
    return v.length === 1 ? '' : 'Please choose one answer.';
  };
  const answers = () => { const a = {}; sets.forEach(fs => { const v = picked(fs); a[fs.dataset.q] = fs.dataset.multi === '1' ? v : (v[0] || null); }); return a; };

  const paint = (fs) => {
    const multi = fs.dataset.multi === '1', max = +fs.dataset.max, n = picked(fs).length;
    $$('.chk-opt', fs).forEach(l => { const on = l.querySelector('input').checked; l.classList.toggle('on', on); l.classList.toggle('off', multi && !on && n >= max); });
    if (multi) { const c = $('.cnt', fs); c.textContent = n + ' of ' + max + ' picked'; }
  };
  const show = (k, focus) => {
    cur = k; sets.forEach((fs, i) => { fs.hidden = i !== k; });
    step.textContent = 'Question ' + (k + 1) + ' of ' + N;
    bar.style.width = (k / N * 100) + '%';
    back.disabled = k === 0;
    next.textContent = k === N - 1 ? 'See my score' : 'Next';
    next.disabled = !!check(k);
    msg.textContent = '';
    if (focus) sets[k].querySelector('legend').focus?.();
  };
  sets.forEach((fs, k) => {
    fs.querySelector('legend').tabIndex = -1;
    fs.addEventListener('change', (e) => {
      if (!started) started = Date.now();
      const multi = fs.dataset.multi === '1', max = +fs.dataset.max;
      if (multi && picked(fs).length > max) { e.target.checked = false; msg.textContent = 'You can pick up to ' + max + '. Untick one to choose another.'; }
      else msg.textContent = '';
      paint(fs); next.disabled = !!check(k);
      // single choice: move on by itself after a short pause, so a tap is enough
      if (!multi && !check(k) && k < N - 1) setTimeout(() => { if (cur === k) show(k + 1, true); }, 260);
    });
  });
  back.addEventListener('click', () => { if (cur > 0) show(cur - 1, true); });
  next.addEventListener('click', () => {
    const m = check(cur); if (m) { msg.textContent = m; return; }
    if (cur < N - 1) { show(cur + 1, true); return; }
    // before sending: every question checked again; jump to the first one that is not right
    for (let k = 0; k < N; k++) { const mk = check(k); if (mk) { show(k, true); msg.textContent = mk; return; } }
    submit();
  });

  // ---- the same scoring as the database (survey_evaluate), used if the network fails
  const PTS = {}; QS.forEach(q => { if (q.id !== 'q1' && !q.multi) q.options.forEach((o, i) => { PTS[q.id + ':' + o[0]] = 3 - i; }); });
  const evaluate = (a) => {
    let score = 0; const w = [];
    ['q2','q3','q4','q5','q6','q7'].forEach(q => { const p = PTS[q + ':' + a[q]]; score += p; if (p < 3) w.push([p, q]); });
    w.sort((x, y) => x[0] - y[0] || (x[1] < y[1] ? -1 : 1));
    const tips = w.slice(0, 2).map(x => x[1]);
    for (const h of a.q8) { if (tips.length >= 3) break; tips.push('h_' + h); }
    const percent = Math.round(score * 100 / 18);
    return { score, max: 18, percent, band: percent <= 40 ? 'firefighting' : percent <= 75 ? 'partly' : 'in_control', tips };
  };
  const rpc = async (fn, body) => {
    const r = await fetch(API + fn, { method: 'POST', headers: { apikey: KEY, Authorization: 'Bearer ' + KEY, 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
    const j = await r.json().catch(() => ({}));
    if (!r.ok) throw new Error(j.message || 'Could not reach acktvt.com');
    return j;
  };
  async function submit() {
    const a = answers();
    quiz.hidden = true; wait.hidden = false; bar.style.width = '100%';
    let out;
    try {
      out = await rpc('public_survey_submit', { p: { survey: 'control-check-v1', answers: a, source, campaign, device, secs: Math.round((Date.now() - (started || Date.now())) / 1000), hp: $('#chk-hp').value } });
      sent = out.id && out.token ? { id: out.id, token: out.token } : null;
    } catch (e) { out = evaluate(a); sent = null; }
    render(out);
  }
  const BAND_COLOR = { firefighting: ['#C2410C', '#FFF1E6'], partly: ['#B7791F', '#FFF7E0'], in_control: ['#007A4D', '#E6F5EE'] };
  function render(o) {
    wait.hidden = true; res.hidden = false;
    const [c, bg] = BAND_COLOR[o.band], b = T.bands[o.band];
    const ring = $('#chk-ring'); ring.style.setProperty('--ring', c); ring.style.setProperty('--p', o.percent);
    $('#chk-pct').textContent = o.percent + '%';
    const band = $('#chk-band'); band.textContent = b[0]; band.style.color = c; band.style.background = bg;
    $('#chk-band-h').textContent = 'Your efficiency score is ' + o.percent + '%';
    $('#chk-band-p').textContent = b[1];
    $('#chk-tiplist').innerHTML = '';
    o.tips.forEach(k => {
      const t = T.tips[k]; const d = document.createElement('div'); d.className = 'chk-tip';
      const h = document.createElement('b'); h.textContent = t[0];
      const p = document.createElement('p'); p.textContent = t[1];
      const how = document.createElement('p'); how.className = 'how'; how.innerHTML = '<em>How acktvt BMS does this:</em> '; how.append(t[2]);
      d.append(h, p, how); $('#chk-tiplist').append(d);
    });
    if (!sent) { $('#chk-form').hidden = true; $('#chk-offline').hidden = false; }
    res.querySelector('h2').setAttribute('tabindex', '-1'); res.querySelector('h2').focus();
    window.scrollTo({ top: $('.chk-wrap').offsetTop - 90, behavior: 'smooth' });
  }

  // ---- optional contact form
  const form = $('#chk-form'), ferr = $('#chk-ferr'), send = $('#chk-send');
  const phoneOk = (v) => { const d = v.replace(/[\\s().-]/g, ''); return /^(\\+91|0091|91|0)?[6-9]\\d{9}$/.test(d) || /^\\+[1-9]\\d{7,14}$/.test(d); };
  form.addEventListener('submit', async (e) => {
    e.preventDefault(); ferr.style.display = 'none';
    const f = Object.fromEntries(new FormData(form).entries());
    const bad = (m, el) => { ferr.textContent = m; ferr.style.display = 'block'; form.elements[el]?.focus(); };
    if ((f.name || '').trim().length < 2) return bad('Please enter your name.', 'name');
    if ((f.company || '').trim().length < 2) return bad('Please enter your company name.', 'company');
    if (!phoneOk(f.phone || '')) return bad('Please enter a valid WhatsApp number, for example 98200 12345.', 'phone');
    if (f.email && !/^[^\\s@]+@[^\\s@]+\\.[a-z]{2,}$/i.test(f.email.trim())) return bad('Please check the e-mail address.', 'email');
    if (!form.elements.consent.checked) return bad('Please tick the box to agree, so that we can send your report.', 'consent');
    send.disabled = true; send.textContent = 'Sending…';
    try {
      const c = await rpc('public_survey_contact', { p_id: sent.id, p_token: sent.token, p: { name: f.name, company: f.company, phone: f.phone, email: f.email || '', consent: 'true', updates: form.elements.updates.checked ? 'true' : 'false' } });
      const link = $('#chk-report');
      if (c && c.report_token) link.href = 'report/?id=' + encodeURIComponent(sent.id) + '&t=' + encodeURIComponent(c.report_token);
      else link.parentElement.hidden = true;
      if (c && c.emailed) { const m = $('#chk-mailed'); m.textContent = 'We have also e-mailed the link to ' + f.email.trim() + '.'; m.hidden = false; }
      form.hidden = true; $('#chk-thanks').hidden = false; $('#chk-thanks').focus();
    } catch (ex) { send.disabled = false; send.textContent = 'Get my report'; bad(ex.message || 'Could not send. Please try again.', 'name'); }
  });

  // ---- share
  const shareUrl = (s) => location.origin + location.pathname + '?src=' + s;
  const shareText = 'Is your business in control? A 2-minute check with your score and 3 practical tips: ';
  $('#sh-wa').href = 'https://wa.me/?text=' + encodeURIComponent(shareText + shareUrl('whatsapp'));
  $('#sh-li').href = 'https://www.linkedin.com/sharing/share-offsite/?url=' + encodeURIComponent(shareUrl('linkedin'));
  $('#sh-copy').addEventListener('click', async () => { try { await navigator.clipboard.writeText(shareUrl('other-link')); $('#sh-copy').textContent = 'Link copied'; } catch (e) { prompt('Copy this link:', shareUrl('other-link')); } });

  sets.forEach(paint);
  show(0, false);
})();
</script>
"""

check_html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
{SEO_HEAD("check")}{head_meta}{style}{EXTRA_CSS}{CHECK_CSS}
</head>
<body>
{nav}
<section class="page chk-hero" style="padding-bottom:84px">
  <div class="wrap">
    <span class="eyebrow" style="color:var(--gold-bright)">acktvt Business Management Suite</span>
    <h1>{_esc(CHECK_TEXT['title'])}</h1>
    <p class="dek">A 2-minute check for manufacturers and traders: 8 quick questions, an instant score and 3 practical tips. No sign-up needed.</p>
  </div>
</section>
<section class="light" style="padding:0">
  <div class="chk-wrap">
    <div class="chk-card">
      <div id="chk-quiz" class="chk-quiz">
        <div class="chk-top"><span id="chk-step" aria-live="polite">Question 1 of {len(CHECK_TEXT['questions'])}</span><span>About 2 minutes</span></div>
        <div class="chk-bar" aria-hidden="true"><i id="chk-bar"></i></div>
        <input type="text" id="chk-hp" name="website" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px;width:1px;height:1px">
        {''.join(_q_html(i, q) for i, q in enumerate(CHECK_TEXT['questions']))}
        <p class="chk-msg" id="chk-msg" role="alert"></p>
        <div class="chk-nav"><button class="btn chk-ghost" id="chk-back" type="button">Back</button><button class="btn btn-green" id="chk-next" type="button">Next</button></div>
        <p class="chk-foot">Your answers alone do not identify you. See the <a href="../privacy/" style="text-decoration:underline">privacy notice</a>.</p>
      </div>
      <div id="chk-wait" class="chk-wait" hidden>Working out your score…</div>
      <div id="chk-res" class="chk-res" hidden>
        <div class="chk-score">
          <div class="chk-ring" id="chk-ring"><div><span><b id="chk-pct">0%</b><small>EFFICIENCY</small></span></div></div>
          <div><span class="chk-band" id="chk-band"></span><h2 id="chk-band-h"></h2><p id="chk-band-p"></p></div>
        </div>
        <div class="chk-tips"><h3>Your 3 practical tips</h3><div id="chk-tiplist"></div></div>
        <div class="chk-lead">
          <h3>Get your detailed report and a free 30-minute walkthrough</h3>
          <p class="sub">Your personal report opens here straight away, and we will WhatsApp you to set up the walkthrough. Your score and tips above are yours either way. Leave your details only if you would like the report.</p>
          <form id="chk-form" novalidate>
            <div id="chk-ferr" class="err" role="alert"></div>
            <div class="row">
              <div class="f"><label for="c-name">Your name</label><input id="c-name" name="name" autocomplete="name" maxlength="80" placeholder="Rohan Deshmukh"></div>
              <div class="f"><label for="c-company">Company</label><input id="c-company" name="company" autocomplete="organization" maxlength="120" placeholder="Precision Gears Pvt Ltd"></div>
            </div>
            <div class="row">
              <div class="f"><label for="c-phone">WhatsApp number</label><input id="c-phone" name="phone" type="tel" autocomplete="tel" maxlength="20" placeholder="98200 12345"></div>
              <div class="f"><label for="c-email">E-mail (optional)</label><input id="c-email" name="email" type="email" autocomplete="email" maxlength="120" placeholder="you@yourcompany.in"></div>
            </div>
            <label class="consent"><input type="checkbox" name="consent" value="yes"><span>I agree that Prowessz Consulting may contact me about this report and acktvt BMS. See the <a href="../privacy/" style="text-decoration:underline">privacy notice</a>.</span></label>
            <label class="consent" style="margin-top:-8px"><input type="checkbox" name="updates" value="yes"><span>Also send me occasional updates from acktvt. I can stop them at any time.</span></label>
            <div class="actions"><button class="btn btn-primary" id="chk-send" type="submit">Get my report</button><span class="note">Your answers and details are kept for 12 months.</span></div>
          </form>
          <div id="chk-thanks" class="chk-done" tabindex="-1" hidden><b>Thank you. Your report is ready.</b><p style="margin:12px 0 14px"><a class="btn btn-primary" id="chk-report" href="#" target="_blank" rel="noopener">Open my report</a></p><p id="chk-mailed" style="margin:0 0 6px" hidden></p><p style="margin:0">We will WhatsApp you to set up your free 30-minute walkthrough. Meanwhile, the live demo is open: <a href="{DEMO_BMS}" target="_blank" rel="noopener" style="color:#FFD873;text-decoration:underline">see acktvt BMS with a sample company</a>.</p><div class="chk-guide"><span>A complimentary guide from Prowessz Consulting Services LLP</span><b>The Strategic Pause</b><p>35 honest questions for the people who run the business, and an hour to think about them.</p><a class="btn chk-ghost" href="/guides/the-strategic-pause.pdf" target="_blank" rel="noopener">Download the guide (PDF)</a></div></div>
          <div id="chk-offline" class="chk-done" hidden><b>Your score is ready, but we could not save it.</b>For your detailed report, WhatsApp us on <a href="{WA}" style="color:#FFD873;text-decoration:underline">+91 80802 55000</a>.</div>
        </div>
        <div class="chk-share"><span>Share this check:</span><a id="sh-wa" href="#" target="_blank" rel="noopener">WhatsApp</a><a id="sh-li" href="#" target="_blank" rel="noopener">LinkedIn</a><button id="sh-copy" type="button">Copy link</button></div>
      </div>
    </div>
  </div>
</section>
{footer}
{CHECK_JS.replace('__TEXT__', json.dumps(CHECK_TEXT, ensure_ascii=False)).replace('__API__', CHECK_API).replace('__KEY__', CHECK_KEY)}
<script src="/assets/consent.js" defer></script>
</body>
</html>
"""
check_html = check_html.replace('href="../check/"', 'href="./"')
os.makedirs(os.path.join(HERE, 'check'), exist_ok=True)
open(os.path.join(HERE, 'check', 'index.html'), 'w', encoding='utf-8').write(check_html)
print('wrote check/index.html')
