"""Generates bms.html, dps.html and privacy.html from index.html's styles,
nav and footer so the sub-pages always match the landing page.

    python3 build_pages.py

Form submissions go to acktvt@prowessz.com through FormSubmit
(https://formsubmit.co) — a no-account relay: the FIRST submission triggers
a one-time activation e-mail to that inbox; click the link once and every
later submission is delivered. See README.md.
"""
import re, os

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, 'index.html'), encoding='utf-8').read()

style = re.search(r'<style>.*?</style>', src, re.S).group(0)
head_meta = re.search(r'<link rel="icon".*?(?=<style>)', src, re.S).group(0).replace('href="assets/', 'href="../assets/')
nav = re.search(r'<header class="nav" id="nav">.*?</header>', src, re.S).group(0)
footer = re.search(r'<footer>.*?</footer>', src, re.S).group(0)
# sub-pages live beside index.html: anchor links must go back to it
def relink(h):
    h = h.replace('href="./"', 'href="../"').replace('href="#', 'href="../#')
    return (h.replace('href="bms/"', 'href="../bms/"').replace('href="dps/"', 'href="../dps/"')
             .replace('href="privacy/"', 'href="../privacy/"').replace('href="login/"', 'href="../login/"'))
nav, footer = relink(nav), relink(footer)
nav = nav.replace('class="nav" id="nav"', 'class="nav scrolled" id="nav"')

EXTRA_CSS = """
<style>
  .page{background:radial-gradient(1000px 500px at 10% -10%,#0E5A3B 0%,transparent 60%),linear-gradient(180deg,#062A1C 0%,#071F16 100%);color:#fff;padding:132px 0 56px}
  .page h1{font-size:clamp(34px,4.4vw,52px);margin:14px 0 14px}
  .page .dek{color:rgba(255,255,255,.78)}
  .lead-grid{display:grid;grid-template-columns:1.05fr .95fr;gap:36px;align-items:start;margin-top:-40px;padding-bottom:80px}
  .formcard{background:#fff;color:var(--ink);border-radius:var(--radius);box-shadow:0 30px 80px rgba(0,0,0,.25),0 0 0 1px var(--line);padding:30px 30px 26px}
  .formcard h2{font-size:24px;margin-bottom:6px}
  .formcard .sub{color:var(--ink-soft);font-size:14.5px;margin-bottom:22px}
  .q{margin-bottom:20px}
  .q label.t{display:block;font-weight:600;font-size:14.5px;margin-bottom:8px}
  .q label.t small{display:block;font-weight:400;color:var(--ink-soft);font-size:12.5px;margin-top:2px}
  .chips{display:flex;flex-wrap:wrap;gap:8px}
  .chips label{display:inline-flex;align-items:center;gap:7px;border:1px solid var(--line);border-radius:999px;padding:8px 13px;font-size:13.5px;cursor:pointer;background:var(--paper);transition:all .15s}
  .chips label:hover{border-color:var(--green)}
  .chips input{accent-color:var(--green);margin:0}
  .chips label:has(input:checked),.chips label.on{background:var(--mint-soft);border-color:var(--green);color:var(--green-deep);font-weight:600}
  .row{display:grid;grid-template-columns:1fr 1fr;gap:14px}
  .f{display:flex;flex-direction:column;gap:6px;margin-bottom:14px}
  .f label{font-size:13px;font-weight:600;color:var(--ink-2)}
  .f input,.f textarea{font:inherit;font-size:14.5px;padding:11px 13px;border:1px solid var(--line);border-radius:var(--radius-sm);background:#fff;color:var(--ink);width:100%}
  .f input:focus,.f textarea:focus{outline:2px solid var(--mint);border-color:var(--green)}
  .f textarea{min-height:96px;resize:vertical}
  .consent{display:flex;gap:10px;align-items:flex-start;font-size:12.5px;color:var(--ink-soft);margin:6px 0 18px}
  .consent input{margin-top:3px;accent-color:var(--green)}
  .actions{display:flex;gap:12px;align-items:center;flex-wrap:wrap}
  .note{font-size:12.5px;color:var(--ink-soft)}
  .ok{display:none;text-align:center;padding:36px 10px}
  .ok .tick{width:64px;height:64px;border-radius:50%;background:var(--mint-soft);color:var(--green);display:grid;place-items:center;margin:0 auto 14px;font-size:30px}
  .ok h2{font-size:26px;margin-bottom:8px}
  .ok p{color:var(--ink-soft);max-width:44ch;margin:0 auto 18px}
  .err{display:none;background:#FBE9E7;color:#A3241D;border-radius:var(--radius-sm);padding:10px 12px;font-size:13.5px;margin-bottom:12px}
  .side{color:#fff;padding-top:0}
  .side .card{background:linear-gradient(160deg,#0B3D2A,#062A1C);border:1px solid rgba(255,255,255,.12);border-radius:var(--radius);padding:22px;margin-bottom:14px;box-shadow:0 18px 50px rgba(0,0,0,.18)}
  .side h3{font-size:18px;margin-bottom:10px;color:#fff}
  .side p,.side li{font-size:14.5px;color:rgba(255,255,255,.78);line-height:1.55}
  .side ul{margin:0;padding-left:18px}
  .side li{margin:4px 0}
  .side .mods{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}
  .side .mods span{font-size:12px;background:rgba(255,255,255,.08);border:1px solid var(--line-dark);border-radius:999px;padding:4px 10px;color:rgba(255,255,255,.85)}
  .side .next{counter-reset:s}
  .side .next div{display:flex;gap:12px;padding:8px 0;border-top:1px solid var(--line-dark);font-size:14px;color:rgba(255,255,255,.8)}
  .side .next div:first-child{border:0}
  .side .next b{counter-increment:s;width:26px;height:26px;border-radius:50%;background:var(--gold);color:var(--ink);display:grid;place-items:center;font-size:12px;flex:none}
  .side .next b::before{content:counter(s)}
  .legal{background:#fff;color:var(--ink);padding:80px 0}
  .legal h1{font-size:40px;margin-bottom:10px}
  .legal h2{font-size:22px;margin:32px 0 8px}
  .legal p,.legal li{font-size:15.5px;color:var(--ink-2);line-height:1.65;max-width:76ch}
  .legal ul{padding-left:20px}
  @media (max-width:980px){.lead-grid{grid-template-columns:1fr}.side{order:2}}
  @media (max-width:640px){.formcard{padding:22px 18px}.row{grid-template-columns:1fr}.page{padding-top:112px}}
</style>
"""

FORM_JS = """
<script>
  document.getElementById('year').textContent = new Date().getFullYear();
  document.getElementById('burger')?.addEventListener('click', () => { const n = document.getElementById('nav'); const open = n.classList.toggle('open'); document.getElementById('burger').setAttribute('aria-expanded', open); });
  const form = document.getElementById('lead'), ok = document.getElementById('ok'), err = document.getElementById('err'), btn = document.getElementById('send');
  const TO = 'acktvt@prowessz.com';
  // highlight chosen chips on browsers without :has() (older Firefox/Safari)
  const paint = () => form.querySelectorAll('.chips label').forEach(l => l.classList.toggle('on', l.querySelector('input').checked));
  form.addEventListener('change', paint); paint();
  const HOME = new URL(document.querySelector('.brand').getAttribute('href'), location.href).href;   // https://acktvt.com/ on the live site
  form.querySelector('[name=_next]').value = HOME + '?sent=1';
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    if (!form.reportValidity()) return;
    err.style.display = 'none'; btn.disabled = true; btn.textContent = 'Sending…';
    const fd = new FormData(form); const body = {};
    for (const [k, v] of fd.entries()) { if (k === '_next') continue; body[k] = body[k] ? body[k] + ', ' + v : v; }
    body._replyto = body.email;
    try {
      const r = await fetch('https://formsubmit.co/ajax/' + TO, { method: 'POST', headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' }, body: JSON.stringify(body) });
      const j = await r.json().catch(() => ({}));
      if (!r.ok || String(j.success) === 'false') throw new Error(j.message || 'Could not send');
      form.style.display = 'none'; ok.style.display = 'block'; window.scrollTo({ top: 0, behavior: 'smooth' });
      setTimeout(() => { location.href = HOME + '?sent=1'; }, 2200);
    } catch (ex) {
      // network or relay hiccup: fall back to the classic POST, which redirects back here with ?sent=1
      btn.disabled = false; btn.textContent = 'Send';
      err.textContent = 'Sending the long way round — one moment…'; err.style.display = 'block';
      setTimeout(() => HTMLFormElement.prototype.submit.call(form), 600);
    }
  });
</script>
"""


def chips(name, options, multi=False):
    t = 'checkbox' if multi else 'radio'
    return '<div class="chips">' + ''.join(f'<label><input type="{t}" name="{name}" value="{o}"{" required" if (not multi and i == 0) else ""}> {o}</label>' for i, o in enumerate(options)) + '</div>'


def page(fname, title, eyebrow, h1, dek, form_title, form_sub, questions, side, subject, ok_text, name_ph, org_ph):
    qhtml = ''.join(f'<div class="q"><label class="t">{q}{("<small>" + hint + "</small>") if hint else ""}</label>{chips(name, opts, multi)}</div>' for q, hint, name, opts, multi in questions)
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title} · acktvt</title>
<meta name="description" content="{dek}" />
<meta name="robots" content="index,follow" />
{head_meta}{style}{EXTRA_CSS}
</head>
<body>
{nav}
<section class="page">
  <div class="wrap">
    <span class="eyebrow" style="color:var(--gold-bright)">{eyebrow}</span>
    <h1>{h1}</h1>
    <p class="dek">{dek}</p>
  </div>
</section>
<section class="light" style="padding:0">
  <div class="wrap lead-grid">
    <div class="formcard">
      <div id="ok" class="ok"><div class="tick">✓</div><h2>Thank you — we have it.</h2><p>{ok_text}</p><p class="note">Taking you back to acktvt.com…</p></div>
      <form id="lead" action="https://formsubmit.co/acktvt@prowessz.com" method="POST" novalidate>
        <input type="hidden" name="_subject" value="{subject}">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_next" value="">
        <input type="hidden" name="suite" value="{title}">
        <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
        <h2>{form_title}</h2>
        <p class="sub">{form_sub}</p>
        <div id="err" class="err"></div>
        {qhtml}
        <div class="row">
          <div class="f"><label for="name">Your name</label><input id="name" name="name" required autocomplete="name" placeholder="{name_ph}"></div>
          <div class="f"><label for="org">Organisation</label><input id="org" name="organisation" required autocomplete="organization" placeholder="{org_ph}"></div>
        </div>
        <div class="row">
          <div class="f"><label for="email">Work e-mail</label><input id="email" name="email" type="email" required autocomplete="email" placeholder="you@yourcompany.in"></div>
          <div class="f"><label for="phone">Phone / WhatsApp</label><input id="phone" name="phone" type="tel" required autocomplete="tel" placeholder="+91 …"></div>
        </div>
        <div class="f"><label for="comment">Anything else you'd like us to know</label><textarea id="comment" name="comment" placeholder="Optional — a line or two is plenty."></textarea></div>
        <label class="consent"><input type="checkbox" name="consent" value="yes" required> I agree that Prowessz Consulting may contact me about acktvt using these details. See the <a href="../privacy/" style="text-decoration:underline">privacy notice</a>.</label>
        <div class="actions"><button class="btn btn-green" id="send" type="submit">Send</button><span class="note">Goes straight to acktvt@prowessz.com · we reply within one working day.</span></div>
      </form>
    </div>
    <aside class="side">{side}</aside>
  </div>
</section>
{footer}
{FORM_JS}
</body>
</html>
"""
    os.makedirs(os.path.join(HERE, fname), exist_ok=True)
    open(os.path.join(HERE, fname, 'index.html'), 'w', encoding='utf-8').write(html)
    print('wrote', fname + '/index.html', len(html) // 1024, 'KB')


WA = 'https://wa.me/918080255000?text=Hi%2C%20I%27m%20interested%20in%20acktvt%20products%2C%20Let%27s%20connect..'

# The launcher (acktvt-launch repo) that wakes the Render service and forwards
# once it answers. Sign-in links go through it so the client sees a branded
# page for those 30–50 seconds instead of a blank tab. The real product
# addresses live in that page's CONFIG block, in one place.
LAUNCH     = 'https://acktvt.prowessz.com/'
LAUNCH_DPS = LAUNCH + '?app=dps'
LAUNCH_BMS = LAUNCH + '?app=bms'
LAUNCH_TRIAL = LAUNCH + '?app=dps&next=/signup'

# ---------------------------------------------------------------- DPS
page('dps', 'Data Protection Suite', 'Data Protection Suite · DPDP Act 2023 · Rules 2025',
     'Tell us where your organisation stands. <em style="color:var(--mint)">We\'ll show you the gap.</em>',
     'Three quick questions and your contact details. We reply within one working day with a readiness view for an organisation like yours, a walkthrough slot, and — if you want it — a 14-day trial with sample data loaded.',
     'Start with the Data Protection Suite', 'Takes about a minute. Nothing here is a commitment.',
     [
         ('Do you think your organisation is DPDP-compliant today — or will be by 13 May 2027?', 'The date the substantive obligations of the Act and Rules come into force.', 'compliance_status',
          ['Yes, already compliant', 'On track for May 2027', 'Not sure where we stand', 'No plan yet'], False),
         ('What is the biggest challenge right now?', 'Pick everything that applies.', 'challenges',
          ['Knowing what personal data we hold and why', 'Notices and consent where we collect data', 'Vendors and processors — DPAs', 'Breach readiness (72-hour clock)', 'Employee, contract-worker and CCTV data', 'NABH / ABDM or ISO 27001 alignment', 'Staff awareness and training', 'Proving it to an auditor or the Board'], True),
         ('Which describes you best?', None, 'organisation_type',
          ['Hospital, under 50 beds', 'Hospital, 50–200 beds', 'Hospital, 200+ beds', 'Diagnostic lab or lab chain', 'Manufacturing company', 'Other business', 'Consultant / advisor'], False),
     ],
     f"""
      <div class="card"><h3>What happens next</h3><div class="next">
        <div><b></b><span>We read your answers and reply by e-mail within one working day — a short readiness view for an organisation like yours.</span></div>
        <div><b></b><span>A 20-minute walkthrough on a call or WhatsApp, on your data if you like.</span></div>
        <div><b></b><span>If it fits, a 14-day trial with sample data loaded — no card, nothing lost when you choose a plan.</span></div>
      </div></div>
      <div class="card"><h3>What the suite covers</h3><p>Twenty-three modules across three tiers, with sector packs for healthcare and manufacturing. Standard alone meets every obligation the Act and Rules place on a Data Fiduciary.</p>
        <div class="mods"><span>Data map &amp; RoPA</span><span>Notices</span><span>Consent ledger</span><span>Rights desk · 90-day clock</span><span>Privacy page</span><span>Vendors &amp; DPAs</span><span>Safeguards</span><span>Retention &amp; erasure</span><span>Parental consent</span><span>Breach · 72-hr clock</span><span>Grievances</span><span>Gap assessment</span><span>Reviews &amp; reminders</span><span>Training</span><span>DPIA</span><span>Evidence pack</span><span>Regulatory watch</span><span>NABH / ISO 27001 crosswalk</span><span>Groups</span></div></div>
      <div class="card"><h3>Prefer to talk first?</h3><p>Message us on WhatsApp and we'll call back.</p><p style="margin-top:12px"><a class="btn btn-primary" href="{WA}" target="_blank" rel="noopener">WhatsApp +91 80802 55000</a></p></div>
     """,
     '[acktvt] Data Protection Suite enquiry',
     'Your details are on their way to acktvt@prowessz.com. Expect a reply within one working day; if it is urgent, WhatsApp +91 80802 55000.',
     'Your full name', 'Hospital, lab or company name')

# ---------------------------------------------------------------- BMS
page('bms', 'Business Management Suite', 'Business Management Suite · for growing Indian manufacturers',
     'Tell us how the business runs today. <em style="color:var(--mint)">We\'ll show you what changes.</em>',
     'Three quick questions and your contact details. We reply within one working day with a walkthrough on your own order flow — enquiry to invoice to payment — and a plain answer on what it would take to move.',
     'Get started with the Business Management Suite', 'Takes about a minute. Nothing here is a commitment.',
     [
         ('What runs the business today?', 'Pick everything that applies.', 'runs_on',
          ['Tally + Excel', 'An ERP we have outgrown', 'Custom / in-house software', 'Registers and WhatsApp', 'Nothing central yet'], True),
         ('Where does it hurt most?', 'Pick everything that applies.', 'challenges',
          ['Order status across production', 'Material planning and stock', 'GST, e-invoice and e-way bills', 'Receivables and follow-ups', 'Tenders, quotes and CRM', 'Quality, lab and TPI records', 'Retyping between systems', 'HR, attendance and payroll'], True),
         ('How big is the team?', None, 'size',
          ['Under 25 people', '25–100', '100–300', '300+', 'More than one plant'], False),
     ],
     f"""
      <div class="card"><h3>What happens next</h3><div class="next">
        <div><b></b><span>We reply by e-mail within one working day with the two or three modules that would change your week first.</span></div>
        <div><b></b><span>A 30-minute walkthrough on your own order flow — on a call, or at your plant if you are near Mumbai.</span></div>
        <div><b></b><span>A written scope with what we set up, what your team enters, and when you go live. No retyping, no surprises.</span></div>
      </div></div>
      <div class="card"><h3>What the suite covers</h3><p>Nine modules that run a growing company end to end, built around GST and the way Indian manufacturing actually works.</p>
        <div class="mods"><span>Sales &amp; GST invoicing</span><span>Tender / bid &amp; CRM</span><span>Production stages</span><span>Lean material planning</span><span>Purchase &amp; inventory</span><span>Quality &amp; lab reports</span><span>Dispatch &amp; e-way bills</span><span>Receivables &amp; finance</span><span>HR &amp; roles</span></div></div>
      <div class="card"><h3>Prefer to talk first?</h3><p>Message us on WhatsApp and we'll call back.</p><p style="margin-top:12px"><a class="btn btn-primary" href="{WA}" target="_blank" rel="noopener">WhatsApp +91 80802 55000</a></p></div>
     """,
     '[acktvt] Business Management Suite enquiry',
     'Your details are on their way to acktvt@prowessz.com. Expect a reply within one working day; if it is urgent, WhatsApp +91 80802 55000.',
     'Rohan Deshmukh', 'Precision Gears Pvt Ltd / Apex Engineering Works')

# ---------------------------------------------------------------- privacy
priv = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Privacy notice · acktvt</title>
<meta name="description" content="How Prowessz Consulting Services LLP handles personal data collected through acktvt.com." />
{head_meta}{style}{EXTRA_CSS}
</head>
<body>
{nav}
<section class="page" style="padding-bottom:40px"><div class="wrap"><span class="eyebrow" style="color:var(--gold-bright)">acktvt.com</span><h1>Privacy notice</h1><p class="dek">What we collect on this website, why, and what you can ask of us. Written the way we ask our clients to write theirs.</p></div></section>
<section class="legal"><div class="wrap">
  <p><b>Who we are.</b> acktvt is a product line of Prowessz Consulting Services LLP, Mumbai ("Prowessz", "we"). For the purposes of the Digital Personal Data Protection Act, 2023, Prowessz is the Data Fiduciary for personal data collected through this website.</p>
  <h2>What we collect and why</h2>
  <ul>
    <li><b>Enquiry forms</b> (Data Protection Suite and Business Management Suite pages): your name, organisation, work e-mail, phone number, your answers to the short questions, and anything you write in the comment box. <i>Purpose:</i> to reply to your enquiry, arrange a walkthrough and, if you ask for one, set up a trial. <i>Basis:</i> your consent, given by ticking the box before you send.</li>
    <li><b>WhatsApp and e-mail</b> you send us: the contents of your message and your contact details, for the same purpose.</li>
    <li><b>Website visits:</b> this site is a static page hosted on GitHub Pages. We do not set cookies and do not run analytics or advertising trackers. The hosting provider may keep standard server logs (IP address, browser, pages requested) for security and operations.</li>
  </ul>
  <h2>Who processes it</h2>
  <p>Form submissions are relayed to our inbox by FormSubmit (a form-to-e-mail service) and stored in our business e-mail. WhatsApp messages are handled by WhatsApp under its own terms. We do not sell personal data and do not share it with anyone else unless the law requires it.</p>
  <h2>How long we keep it</h2>
  <p>Enquiry details are kept for as long as we are talking, and for up to 24 months after the last contact so that we can pick up the conversation if you come back. If you become a client, your details move to our client records under the engagement letter. You can ask us to delete them sooner at any time.</p>
  <h2>Your rights</h2>
  <p>You may ask us for a summary of the personal data we hold about you, ask us to correct or erase it, withdraw your consent, or nominate someone to exercise these rights on your behalf. Write to <a href="mailto:acktvt@prowessz.com" style="text-decoration:underline">acktvt@prowessz.com</a>; we respond within the time the Rules allow and usually much sooner. If you are not satisfied with our response, you may approach the Data Protection Board of India.</p>
  <h2>Contact</h2>
  <p>Prowessz Consulting Services LLP, Mumbai · <a href="mailto:acktvt@prowessz.com" style="text-decoration:underline">acktvt@prowessz.com</a> · WhatsApp <a href="{WA}" style="text-decoration:underline">+91 80802 55000</a> · <a href="https://prowessz.com" style="text-decoration:underline">prowessz.com</a>.</p>
  <p style="margin-top:28px;font-size:13px;color:var(--ink-soft)">Last updated September 2026. Changes are posted on this page.</p>
</div></section>
{footer}
<script>document.getElementById('year').textContent = new Date().getFullYear(); document.getElementById('burger')?.addEventListener('click', () => {{ const n = document.getElementById('nav'); n.classList.toggle('open'); }});</script>
</body>
</html>
"""
os.makedirs(os.path.join(HERE, 'privacy'), exist_ok=True)
open(os.path.join(HERE, 'privacy', 'index.html'), 'w', encoding='utf-8').write(priv)
print('wrote privacy/index.html')

# ---------------------------------------------------------------- client portal (login chooser)
PORTAL_CSS = """
<style>
  .portal{max-width:980px;margin:0 auto;padding:0 32px 70px}
  .pgrid{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:-30px}
  .pcard{background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:28px 28px 24px;box-shadow:0 24px 60px rgba(6,42,28,.10);display:flex;flex-direction:column}
  .pcard .eyebrow{color:var(--green);font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;font-weight:700}
  .pcard h2{font-size:22px;margin:8px 0 8px}
  .pcard p{color:var(--ink-soft);font-size:14px;line-height:1.55;margin:0 0 18px}
  .pcard .btn{align-self:flex-start}
  .pcard .fine{font-size:12.5px;color:var(--ink-faint);margin-top:14px}
  .pnew{background:var(--paper);border:1px solid var(--line);border-radius:var(--radius);padding:26px 28px;margin-top:18px;display:flex;gap:20px;align-items:center;flex-wrap:wrap;justify-content:space-between}
  .pnew h3{font-size:18px;margin:0 0 4px}
  .pnew p{color:var(--ink-soft);font-size:13.5px;margin:0;max-width:56ch}
  .pnew .acts{display:flex;gap:10px;flex-wrap:wrap}
  .psafe{font-size:12.5px;color:var(--ink-soft);margin-top:22px;text-align:center;line-height:1.6}
  @media (max-width:860px){.pgrid{grid-template-columns:1fr}.portal{padding:0 20px 56px}}
</style>
"""

portal_html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Client login · acktvt</title>
<meta name="description" content="Sign in to your acktvt workspace — Data Protection Suite or Business Management Suite — or start a 14-day trial." />
<meta name="robots" content="index,follow" />
{head_meta}{style}{EXTRA_CSS}{PORTAL_CSS}
</head>
<body>
{nav}
<section class="page" style="padding-bottom:64px"><div class="wrap">
  <span class="eyebrow" style="color:var(--gold-bright)">Client portal</span>
  <h1>Sign in to your workspace.</h1>
  <p class="dek">Your workspace opens on its own secure address. We never ask for your password on this website — if a page on acktvt.com ever does, it is not us.</p>
</div></section>
<section class="light" style="padding:0"><div class="portal">
  <div class="pgrid">
    <div class="pcard">
      <span class="eyebrow">Data Protection Suite</span>
      <h2>DPDP compliance workspace</h2>
      <p>Registers, notices, consent, rights, breach, evidence packs — for your Data Champion and team.</p>
      <a class="btn btn-green" id="portal-dps" href="{LAUNCH_DPS}" target="_blank" rel="noopener">Client login — Data Protection Suite →</a>
      <div class="fine">Invited by a colleague? Use the link in your invitation e-mail; it works for that address only.</div>
    </div>
    <div class="pcard">
      <span class="eyebrow">Business Management Suite</span>
      <h2>Orders to cash workspace</h2>
      <p>Tenders, sales, purchase, stores, production, quality, dispatch and accounts on one traceability spine.</p>
      <a class="btn btn-primary" href="{LAUNCH_BMS}" target="_blank" rel="noopener">Client login — Business Management →</a>
      <div class="fine">Same login your team uses on the shop floor and on the Android app.</div>
    </div>
  </div>
  <div class="pnew">
    <div>
      <h3>Not a client yet?</h3>
      <p>Start a 14-day trial of the Data Protection Suite with sample data loaded — no card, nothing lost when you choose a plan. Or have us walk you through it first.</p>
    </div>
    <div class="acts">
      <a class="btn btn-green" id="portal-trial" href="{LAUNCH_TRIAL}" target="_blank" rel="noopener">Sign up for a free trial</a>
      <a class="btn btn-outline" href="dps/">Ask for a demo</a>
    </div>
  </div>
  <p class="psafe">
    Signing in happens on the product's own address over an encrypted connection. Administrators can turn on two-step verification inside the app.<br>
    Trouble signing in? Write to <a href="mailto:acktvt@prowessz.com" style="text-decoration:underline">acktvt@prowessz.com</a> or WhatsApp <a href="{WA}" style="text-decoration:underline">+91 80802 55000</a>.
  </p>
</div></section>
{footer}
<script>document.getElementById('year').textContent = new Date().getFullYear(); document.getElementById('burger')?.addEventListener('click', () => {{ const n = document.getElementById('nav'); n.classList.toggle('open'); }});</script>
</body>
</html>
"""
os.makedirs(os.path.join(HERE, 'login'), exist_ok=True)
open(os.path.join(HERE, 'login', 'index.html'), 'w', encoding='utf-8').write(portal_html)
print('wrote login/index.html')

# ---------------------------------------------------------------- 404
nf = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Page not found · acktvt</title>
{head_meta.replace('href="../assets/', 'href="/assets/')}{style}{EXTRA_CSS}
</head>
<body>
{nav.replace('href="../', 'href="/')}
<section class="page" style="min-height:70vh;display:flex;align-items:center"><div class="wrap"><span class="eyebrow" style="color:var(--gold-bright)">404</span><h1>That page isn't here.</h1><p class="dek">The link may be old or mistyped. Everything about both suites is one page away.</p><p style="margin-top:26px;display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn-primary" href="/">Go to acktvt.com</a><a class="btn btn-ghost" href="/dps/">Data Protection Suite</a><a class="btn btn-ghost" href="/bms/">Business Management Suite</a></p></div></section>
{footer.replace('href="../', 'href="/')}
<script>document.getElementById('year').textContent = new Date().getFullYear(); document.getElementById('burger')?.addEventListener('click', () => {{ document.getElementById('nav').classList.toggle('open'); }});</script>
</body>
</html>
"""
open(os.path.join(HERE, '404.html'), 'w', encoding='utf-8').write(nf)
print('wrote 404.html')
