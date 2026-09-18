# acktvt — product landing page

Static, single-file site for the acktvt product line (Business Management Suite + Data Protection Suite) by Prowessz Consulting Services LLP.

- `index.html` — the whole page (HTML, CSS and JS inline; only external request is Google Fonts).
- `assets/` — brand icon, wordmark, favicon and touch icon.
- `.nojekyll` — tells GitHub Pages to serve the files as-is.

## Publish on GitHub Pages

1. Create a repository (e.g. `acktvt-site`), push these files to the `main` branch.
2. Repository → Settings → Pages → Source: **Deploy from a branch** → Branch `main`, folder `/ (root)` → Save.
3. The site is live at `https://<org-or-user>.github.io/acktvt-site/` within a minute.
4. Custom domain (recommended: `acktvt.com` or `www.acktvt.com`): add the domain in Settings → Pages → Custom domain, tick "Enforce HTTPS", and at your DNS provider add a `CNAME` record `www → <org-or-user>.github.io` (and the four GitHub `A` records for the apex domain). GitHub writes a `CNAME` file into the repo for you.

## Before you publish — three links to set

Open `index.html` and edit the `LINKS` block near the bottom (the only place they live):

```js
const LINKS = {
  dpsApp: 'https://dps.acktvt.com',      // Data Protection Suite sign-in; "/signup" is appended for the trial button
  contact: 'https://wa.me/918080255000?text=...',   // WhatsApp link for "Book a walkthrough"
  privacy: 'https://prowessz.com/privacy',
};
```

The Business Management Suite links to `https://erp.acktvt.com` directly.

## Editing

Everything is plain HTML — sections are marked with `<!-- ==== NAME ==== -->` comments. Tier descriptions sit in the `#tiers` section (no prices — commercials are settled in the workshop); module lists in `#bms` and `#dps`. No build step.


## Pages

| File | What it is |
|---|---|
| `index.html` | Landing page (both suites) |
| `bms/index.html` | Business Management Suite — enquiry form, served as **acktvt.com/bms/** |
| `dps/index.html` | Data Protection Suite — enquiry form, served as **acktvt.com/dps/** |
| `privacy/index.html` | Privacy notice, served as **acktvt.com/privacy/** |
| `404.html` | Branded not-found page (GitHub Pages serves it automatically) |
| `build_pages.py` | Regenerates the three sub-pages from `index.html`'s styles, nav and footer. Run `python3 build_pages.py` after changing the nav, footer or colours in `index.html`. |

## Enquiry forms → acktvt@prowessz.com

The two forms post to **FormSubmit** (formsubmit.co), a form-to-e-mail relay
that needs no account and no server. One-time setup:

1. Publish the site, open acktvt.com/dps/, fill the form with your own details and
   press Send.
2. FormSubmit e-mails **acktvt@prowessz.com** once with an *"Activate form"*
   link. Click it.
3. Every later submission (from either page) arrives as an e-mail with the
   answers in a table; the visitor's address is set as Reply-To so you can
   answer directly. The visitor sees a thank-you for two seconds and is then
   returned to the home page (never a FormSubmit page). Do step 1 once more from `bms.html` if the second form's
   first submission also asks for activation (open acktvt.com/bms/).

The address is set in two places in `build_pages.py` (`TO` and the form
`action`) — change both if the inbox ever changes, then rebuild.

## Clean addresses

Pages live in folders (`dps/index.html`) so the address bar shows
`acktvt.com/dps/` — never a `.html` file name. In-page section links scroll
without leaving `#section` in the address, and the logo returns to
`acktvt.com/`. Delete any old `dps.html` / `bms.html` / `privacy.html` from
the repo if they are still there.
