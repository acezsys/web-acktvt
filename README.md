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
