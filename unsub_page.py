# ---------------------------------------------------------------- unsubscribe  (acktvt.com/check/unsubscribe/?id=…&t=…)
# Run from build_pages.py after report_page.py (needs REPORT_CSS, _brand, CHECK_API, CHECK_KEY, style, head_meta, HERE).
# The link at the foot of every e-mail of The Strategic Pause series (migration 0106). Nothing happens until the person
# presses the button: mail programs open links on their own to check them, and that must not unsubscribe anyone.
UNSUB_JS = """
<script>
(() => {
  const API = '__API__', KEY = '__KEY__';
  const $ = (s) => document.querySelector(s);
  const p = new URLSearchParams(location.search), id = p.get('id'), t = p.get('t');
  const box = $('#us-box');
  const show = (title, text, extra) => { box.innerHTML = '<h1></h1><p></p>' + (extra || ''); box.querySelector('h1').textContent = title; box.querySelector('p').textContent = text; };
  const GUIDE = '<p style="margin-top:18px;font-size:14px">The guide stays yours: <a href="/guides/the-strategic-pause.pdf" style="text-decoration:underline">The Strategic Pause (PDF)</a>.</p>';
  if (!id || !t) { show('This link is incomplete', 'Please open the unsubscribe link exactly as it appears in the e-mail, or reply STOP to any of our e-mails.'); return; }
  const btn = $('#us-go');
  btn.addEventListener('click', () => {
    btn.disabled = true; btn.textContent = 'One moment…';
    fetch(API + 'public_survey_unsubscribe', { method: 'POST', headers: { apikey: KEY, Authorization: 'Bearer ' + KEY, 'Content-Type': 'application/json' }, body: JSON.stringify({ p_id: id, p_t: t }) })
      .then(async (r) => { const j = await r.json().catch(() => ({})); if (!r.ok) throw new Error(j.message || 'Something went wrong'); return j; })
      .then((j) => show(j.already ? 'You were already unsubscribed' : 'You are unsubscribed',
        'You will not receive any more e-mails from The Strategic Pause series. Thank you for reading.', GUIDE))
      .catch((e) => show('We could not unsubscribe you here', e.message + ' You can also reply STOP to any of our e-mails, or write to sales@prowessz.com.'));
  });
})();
</script>
"""
unsub_html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Unsubscribe | The Strategic Pause</title>
<meta name="robots" content="noindex, nofollow" />
<meta name="referrer" content="no-referrer" />
{head_meta.replace('href="../assets/', 'href="/assets/')}{style}{REPORT_CSS}
</head>
<body>
<div class="rp-bar"><div class="in">{_brand}<div class="acts"><a class="btn rp-ghost" href="https://acktvt.com/">acktvt.com</a></div></div></div>
<main class="rp"><div class="rp-msg" id="us-box">
<h1>Stop The Strategic Pause e-mails?</h1>
<p>You will receive no more of the weekly questions from Prowessz Consulting Services LLP. Your report and the guide are not affected.</p>
<p style="margin-top:20px"><button class="btn btn-green" id="us-go" type="button">Unsubscribe</button></p>
</div></main>
{UNSUB_JS.replace('__API__', CHECK_API).replace('__KEY__', CHECK_KEY)}
</body>
</html>
"""
os.makedirs(os.path.join(HERE, 'check', 'unsubscribe'), exist_ok=True)
open(os.path.join(HERE, 'check', 'unsubscribe', 'index.html'), 'w', encoding='utf-8').write(unsub_html)
print('wrote check/unsubscribe/index.html')
