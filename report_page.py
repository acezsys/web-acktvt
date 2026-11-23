# ---------------------------------------------------------------- the personal report  (acktvt.com/check/report/?id=…&t=…)
# Run from build_pages.py after check_page.py (needs CHECK_TEXT, CHECK_API, CHECK_KEY, src, style, head_meta, HERE, DEMO_BMS).
# The page reads one person's report through public_survey_report (migration 0104), only with the link's secret.
# It is never indexed by search engines, and "Save as PDF" uses the browser's own print-to-PDF.
_brand = re.search(r'<a class="brand" href="\./" aria-label="acktvt home">.*?</a>', src, re.S).group(0).replace('href="./"', 'href="https://acktvt.com/"')
_C = CHECK_TEXT['report']['contact']

REPORT_CSS = """
<style>
  body{background:#EEF2EF}
  .rp-bar{position:sticky;top:0;z-index:5;background:#062A1C;color:#fff}
  .rp-bar .in{max-width:860px;margin:0 auto;padding:12px 20px;display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}
  .rp-bar .brand{color:#fff}
  .rp-bar .acts{display:flex;gap:10px;flex-wrap:wrap}
  .rp-bar .btn{padding:10px 16px;font-size:14px}
  .rp-ghost{background:transparent;border:1.5px solid rgba(255,255,255,.35);color:#fff}
  .rp{max-width:860px;margin:24px auto 60px;padding:0 16px}
  .rp-doc{background:#fff;color:var(--ink);border-radius:14px;box-shadow:0 20px 60px rgba(0,0,0,.10),0 0 0 1px var(--line);overflow:hidden}
  .rp-head{background:linear-gradient(160deg,#0B3D2A,#062A1C);color:#fff;padding:28px 34px 24px}
  .rp-head .eyebrow{color:#FFD873}
  .rp-head h1{font-size:34px;margin:10px 0 4px;color:#fff}
  .rp-head p{margin:0;color:rgba(255,255,255,.8);font-size:15px}
  .rp-meta{display:grid;grid-template-columns:1.25fr 1fr;gap:0;border-bottom:1px solid var(--line)}
  .rp-meta > div{padding:18px 34px}
  .rp-meta > div + div{border-left:1px solid var(--line)}
  .rp-meta h4{margin:0 0 8px;font-size:11.5px;letter-spacing:1.2px;text-transform:uppercase;color:var(--ink-soft)}
  .rp-meta dl{margin:0;display:grid;grid-template-columns:auto 1fr;gap:5px 14px;font-size:14px}
  .rp-meta dt{color:var(--ink-soft)}
  .rp-meta dd{margin:0;font-weight:600;color:var(--ink);word-break:break-word}
  .rp-sec{padding:24px 34px;border-bottom:1px solid var(--line)}
  .rp-sec h2{font-size:21px;margin:0 0 12px}
  .rp-score{display:flex;gap:26px;align-items:center}
  .rp-ring{--p:0;width:128px;height:128px;border-radius:50%;flex:none;display:grid;place-items:center;background:conic-gradient(var(--ring) calc(var(--p)*1%),#E8EEEA 0)}
  .rp-ring > div{width:100px;height:100px;border-radius:50%;background:#fff;display:grid;place-items:center;text-align:center}
  .rp-ring b{font-size:32px;line-height:1}
  .rp-ring small{display:block;font-size:10.5px;letter-spacing:.6px;color:var(--ink-soft);margin-top:4px}
  .rp-band{display:inline-block;font-size:12.5px;font-weight:700;letter-spacing:.4px;text-transform:uppercase;padding:4px 11px;border-radius:99px;margin-bottom:6px}
  .rp-score p{margin:4px 0 0;font-size:15px;line-height:1.55;color:var(--ink-2)}
  .rp-score .small{font-size:13.5px;color:var(--ink-soft)}
  .rp-tbl{width:100%;border-collapse:collapse;font-size:13.5px}
  .rp-tbl th{text-align:left;font-size:11.5px;letter-spacing:.6px;text-transform:uppercase;color:var(--ink-soft);font-weight:600;padding:8px 8px;border-bottom:1.5px solid var(--line)}
  .rp-tbl td{padding:9px 8px;border-bottom:1px solid var(--line);vertical-align:top;line-height:1.45}
  .rp-tbl td.pts{white-space:nowrap;font-weight:700}
  .rp-dots{display:inline-flex;gap:3px;vertical-align:middle;margin-left:6px}
  .rp-dots i{width:8px;height:8px;border-radius:50%;background:#E1E7E3}
  .rp-dots i.on{background:var(--green)}
  .rp-tip{border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin-bottom:12px;break-inside:avoid}
  .rp-tip h3{font-size:16.5px;margin:0 0 4px;font-family:inherit}
  .rp-tip > p{margin:0 0 10px;font-size:14.5px;color:var(--ink-2);line-height:1.55}
  .rp-plan{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:10px}
  .rp-plan div{background:#F6F8F6;border-radius:10px;padding:10px 12px;font-size:13.5px;line-height:1.45}
  .rp-plan b{display:block;font-size:11.5px;letter-spacing:.6px;text-transform:uppercase;color:var(--green-deep);margin-bottom:3px}
  .rp-how{font-size:13.5px;color:var(--green-deep);margin:0}
  .rp-how em{font-style:normal;font-weight:700}
  .rp-next{display:flex;gap:12px;flex-wrap:wrap;align-items:center}
  .rp-guide{margin-top:18px;background:#F7F4EA;border-left:3px solid #C9A227;border-radius:10px;padding:14px 18px}
  .rp-guide span{display:block;font-size:11.5px;letter-spacing:1px;text-transform:uppercase;color:#8A6D12;font-weight:700}
  .rp-guide b{display:block;font-size:18px;color:#111E46;margin:5px 0 2px}
  .rp-guide p{margin:0 0 12px;font-size:14px;color:var(--ink-2)}
  .rp-foot{padding:20px 34px 24px;background:#F6F8F6;font-size:13px;color:var(--ink-2);line-height:1.6}
  .rp-foot .c{display:flex;flex-wrap:wrap;gap:6px 18px;font-weight:600;color:var(--ink);margin:4px 0 10px}
  .rp-foot .c a{color:var(--ink);text-decoration:none}
  .rp-msg{max-width:560px;margin:80px auto;text-align:center;background:#fff;border-radius:14px;padding:36px 28px;box-shadow:0 0 0 1px var(--line)}
  .rp-msg h1{font-size:26px;margin:0 0 10px}
  .rp-msg p{color:var(--ink-2)}
  .rp-hint{font-size:12.5px;color:var(--ink-soft);text-align:center;margin-top:10px}
  @media (max-width:640px){
    .rp{padding:0 8px;margin-top:12px}
    .rp-head,.rp-sec,.rp-foot{padding-left:18px;padding-right:18px}
    .rp-meta{grid-template-columns:1fr}
    .rp-meta > div{padding:14px 18px}
    .rp-meta > div + div{border-left:0;border-top:1px solid var(--line)}
    .rp-score{flex-direction:column;align-items:flex-start;gap:14px}
    .rp-plan{grid-template-columns:1fr}
    .rp-tbl .ideal{display:none}
    .rp-head h1{font-size:28px}
  }
  @page{size:A4;margin:12mm}
  @media print{
    body{background:#fff}
    .rp-bar,.rp-hint,.no-print{display:none!important}
    .rp{max-width:none;margin:0;padding:0}
    .rp-doc{box-shadow:none;border-radius:0}
    *{-webkit-print-color-adjust:exact;print-color-adjust:exact}
    .rp-sec{padding:14px 22px}
    .rp-sec h2{font-size:18px;margin-bottom:8px;break-after:avoid}
    .rp-tbl tr,.rp-foot,.rp-score{break-inside:avoid}
    .rp-tip{padding:10px 14px;margin-bottom:7px}
    .rp-tip h3{font-size:15px}
    .rp-tip > p{font-size:13px;margin-bottom:7px}
    .rp-plan{gap:7px;margin-bottom:7px}
    .rp-plan div{font-size:12px;padding:7px 10px}
    .rp-how{font-size:12.5px}
    .rp-foot{font-size:11.5px;padding-top:12px;padding-bottom:12px}
    .rp-foot .c{margin:2px 0 6px}
    .rp-head{padding-top:18px;padding-bottom:16px}
    .rp-head h1{font-size:28px}
    .rp-head,.rp-foot{padding-left:22px;padding-right:22px}
    .rp-meta > div{padding:12px 22px}
    a{text-decoration:none}
  }
</style>
"""

REPORT_JS = """
<script>
(() => {
  const T = __TEXT__, API = '__API__', KEY = '__KEY__', DEMO = '__DEMO__';
  const C = T.report.contact;
  const $ = (s) => document.querySelector(s);
  const esc = (v) => String(v == null ? '' : v).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const MON = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  const ist = (v, withTime = true) => {
    const d = new Date(Date.parse(v) + 5.5 * 3600e3); if (isNaN(d)) return '—';
    const dd = String(d.getUTCDate()).padStart(2, '0'), h = d.getUTCHours(), m = String(d.getUTCMinutes()).padStart(2, '0');
    const date = dd + '-' + MON[d.getUTCMonth()] + '-' + d.getUTCFullYear();
    return withTime ? date + ', ' + ((h % 12) || 12) + ':' + m + ' ' + (h < 12 ? 'am' : 'pm') + ' IST' : date;
  };
  const phone = (v) => { const m = /^\\+91(\\d{5})(\\d{5})$/.exec(v || ''); return m ? '+91 ' + m[1] + ' ' + m[2] : (v || '—'); };
  const Q = {}; T.questions.forEach((q, i) => { Q[q.id] = Object.assign({ n: i + 1 }, q); });
  const label = (qid, v) => { const o = Q[qid].options.find((x) => x[0] === v); return o ? o[1] : (v || '—'); };
  const pts = (qid, v) => { const i = Q[qid].options.findIndex((x) => x[0] === v); return i < 0 ? 0 : 3 - i; };
  const BAND = { firefighting: ['#C2410C', '#FFF1E6'], partly: ['#B7791F', '#FFF7E0'], in_control: ['#007A4D', '#E6F5EE'] };
  const fail = (title, text) => {
    $('#rp-out').innerHTML = '<div class="rp-msg"><h1>' + esc(title) + '</h1><p>' + esc(text) + '</p><p style="margin-top:18px"><a class="btn btn-green" href="' + C.whatsapp_link + '">WhatsApp ' + esc(C.whatsapp) + '</a></p><p style="margin-top:14px"><a href="../" style="text-decoration:underline">Take the check again</a></p></div>';
    document.querySelectorAll('.rp-bar .acts .btn-print').forEach((b) => b.remove());
  };
  const p = new URLSearchParams(location.search), id = p.get('id'), t = p.get('t');
  if (!id || !t) { fail('This report link is incomplete', 'Please open the link exactly as it was sent to you, or WhatsApp us for a fresh one.'); return; }
  fetch(API + 'public_survey_report', { method: 'POST', headers: { apikey: KEY, Authorization: 'Bearer ' + KEY, 'Content-Type': 'application/json' }, body: JSON.stringify({ p_id: id, p_t: t }) })
    .then(async (r) => { const j = await r.json().catch(() => ({})); if (!r.ok) throw new Error(j.message || 'Could not open the report'); return j; })
    .then(render)
    .catch((e) => fail(/expired/i.test(e.message) ? 'This report link has expired' : 'We could not open this report', e.message));

  function render(d) {
    document.title = T.report.title + ' – ' + d.company + ' | acktvt';
    const [col, bg] = BAND[d.band]; const b = T.bands[d.band];
    const ref = 'BCR-' + String(id).replace(/-/g, '').slice(0, 8).toUpperCase();
    const heads = (d.answers.q8 || []).map((h) => label('q8', h)).join(', ');
    const rows = ['q2','q3','q4','q5','q6','q7'].map((q) => {
      const v = d.answers[q], n = pts(q, v);
      return '<tr><td>' + Q[q].n + '</td><td>' + esc(Q[q].text) + '</td><td><b>' + esc(label(q, v)) + '</b></td><td class="pts">' + n + '/3<span class="rp-dots" aria-hidden="true">' + [0,1,2].map((i) => '<i class="' + (i < n ? 'on' : '') + '"></i>').join('') + '</span></td><td class="ideal">' + esc(Q[q].ideal) + '</td></tr>';
    }).join('');
    const tips = d.tips.map((k, i) => {
      const tp = T.tips[k], pl = T.plans[k];
      return '<div class="rp-tip"><h3>' + (i + 1) + '. ' + esc(tp[0]) + '</h3><p>' + esc(tp[1]) + '</p>'
        + '<div class="rp-plan"><div><b>Week 1</b>' + esc(pl[0]) + '</div><div><b>Weeks 2 to 3</b>' + esc(pl[1]) + '</div><div><b>Week 4</b>' + esc(pl[2]) + '</div></div>'
        + '<p class="rp-how"><em>How acktvt BMS does this:</em> ' + esc(tp[2]) + '</p></div>';
    }).join('');
    const wa = C.whatsapp_link + '?text=' + encodeURIComponent('Hi, I am ' + d.name + ' from ' + d.company + '. I took the "Is your business in control?" check (score ' + d.percent + '%, report ' + ref + '). I would like to book the free 30-minute walkthrough.');
    $('#rp-out').innerHTML = `
<div class="rp-doc">
  <div class="rp-head"><span class="eyebrow">Is your business in control? · 2-minute check</span><h1>${esc(T.report.title)}</h1><p>Prepared for ${esc(d.company)}</p></div>
  <div class="rp-meta">
    <div><h4>Prepared for</h4><dl>
      <dt>Company</dt><dd>${esc(d.company)}</dd>
      <dt>Contact</dt><dd>${esc(d.name)}</dd>
      <dt>E-mail</dt><dd>${d.email ? esc(d.email) : '—'}</dd>
      <dt>Mobile / WhatsApp</dt><dd>${esc(phone(d.phone))}</dd>
    </dl></div>
    <div><h4>Report</h4><dl>
      <dt>Reference</dt><dd>${ref}</dd>
      <dt>Report date</dt><dd>${ist(d.report_at)}</dd>
      <dt>Check taken</dt><dd>${ist(d.taken_at)}</dd>
      <dt>Business</dt><dd>${esc(label('q1', d.business_type))}</dd>
    </dl></div>
  </div>
  <div class="rp-sec">
    <div class="rp-score">
      <div class="rp-ring" style="--ring:${col};--p:${d.percent}"><div><span><b>${d.percent}%</b><small>EFFICIENCY</small></span></div></div>
      <div><span class="rp-band" style="color:${col};background:${bg}">${esc(b[0])}</span>
        <h2 style="margin:0">Your efficiency score is ${d.percent}%</h2>
        <p>${esc(b[1])}</p>
        <p class="small">${d.score} of ${d.max} points from questions 2 to 7. Biggest headaches you picked: ${esc(heads)}.</p></div>
    </div>
  </div>
  <div class="rp-sec">
    <h2>Your answers</h2>
    <table class="rp-tbl"><thead><tr><th>#</th><th>Question</th><th>Your answer</th><th>Points</th><th class="ideal">In control looks like</th></tr></thead><tbody>${rows}</tbody></table>
  </div>
  <div class="rp-sec">
    <h2>Your 3 practical tips and 30-day plan</h2>
    ${tips}
  </div>
  <div class="rp-sec no-print">
    <h2>Next step</h2>
    <p style="margin:0 0 14px;font-size:15px;color:var(--ink-2)">In a free 30-minute walkthrough we show how these tips would work in ${esc(d.company)}, on your own order flow.</p>
    <div class="rp-next"><a class="btn btn-green" href="${wa}" target="_blank" rel="noopener">Book my walkthrough on WhatsApp</a><a class="btn" style="border:1.5px solid var(--line)" href="${DEMO}" target="_blank" rel="noopener">See the live demo</a></div>
    <div class="rp-guide"><span>A complimentary guide from Prowessz Consulting Services LLP</span><b>The Strategic Pause</b><p>35 honest questions for the people who run the business, and an hour to think about them.</p><a class="btn" style="border:1.5px solid #C9A227" href="/guides/the-strategic-pause.pdf" target="_blank" rel="noopener">Download the guide (PDF)</a></div>
  </div>
  <div class="rp-foot">
    <div style="font-weight:700;color:var(--ink)">${esc(C.line)}</div>
    <div class="c"><a href="${C.whatsapp_link}">WhatsApp ${esc(C.whatsapp)}</a><a href="mailto:${C.email}">${esc(C.email)}</a><a href="https://acktvt.com">${esc(C.web)}</a></div>
    acktvt is a product line of Prowessz Consulting Services LLP, India. This report is private to you; its link works until ${ist(d.valid_until, false)}. Your answers are kept for 12 months and then erased; to have them erased sooner, write to privacy@prowessz.com.
  </div>
</div>
<p class="rp-hint">To keep a copy, press “Save as PDF” and choose “Save as PDF” as the printer.</p>`;
  }
  document.querySelectorAll('.btn-print').forEach((b) => b.addEventListener('click', () => window.print()));
})();
</script>
"""

report_html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{CHECK_TEXT['report']['title']} | acktvt</title>
<meta name="robots" content="noindex, nofollow" />
<meta name="referrer" content="no-referrer" />
{head_meta.replace('href="../assets/', 'href="/assets/')}{style}{REPORT_CSS}
</head>
<body>
<div class="rp-bar"><div class="in">{_brand}<div class="acts"><button class="btn btn-primary btn-print" type="button">Save as PDF</button><a class="btn rp-ghost" href="https://acktvt.com/">acktvt.com</a></div></div></div>
<main class="rp" id="rp-out"><div class="rp-msg"><p>Opening your report…</p></div></main>
{REPORT_JS.replace('__TEXT__', json.dumps(CHECK_TEXT, ensure_ascii=False)).replace('__API__', CHECK_API).replace('__KEY__', CHECK_KEY).replace('__DEMO__', DEMO_BMS)}
</body>
</html>
"""
os.makedirs(os.path.join(HERE, 'check', 'report'), exist_ok=True)
open(os.path.join(HERE, 'check', 'report', 'index.html'), 'w', encoding='utf-8').write(report_html)
print('wrote check/report/index.html')
