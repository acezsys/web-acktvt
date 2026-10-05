# acktvt — product landing page

Static, single-file site for the acktvt product line (Business Management Suite + Data Protection Suite) by Prowessz Consulting Services LLP.

- `index.html` — the whole page (HTML, CSS and JS inline). No third-party requests on load: fonts are self-hosted in `assets/fonts/`, and YouTube is contacted only when a visitor presses play on a video.
- `assets/` — brand icon, wordmark, favicons (PNG + SVG), touch icon, the two video posters (`poster-dps.jpg`, `poster-bms.jpg`, 2560×1440), the 1200×630 share image (`og-image.jpg`) and `fonts/` (Fraunces, Inter, Poppins, JetBrains Mono — all SIL Open Font Licence).
- Asset links that the sub-pages share (fonts, posters, SVG favicon) are root-absolute (`/assets/…`), so the site must be served from the root of its domain — as it is at acktvt.com.
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

The Business Management Suite links to `https://bms.acktvt.com` directly.

The **Client login** button in the header and the footer's *Client portal* link both
point at `login/`. That page carries the two product sign-in links (`dps.acktvt.com`,
`bms.acktvt.com`) and the trial / demo buttons — change the addresses there when the
apps move to their own subdomains.

## Editing

Everything is plain HTML — sections are marked with `<!-- ==== NAME ==== -->` comments. Tier descriptions sit in the `#tiers` section (no prices — commercials are settled in the workshop); module lists in `#bms` and `#dps`. No build step.


## Pages

| File | What it is |
|---|---|
| `index.html` | Landing page (both suites) |
| `bms/index.html` | Business Management Suite — enquiry form, served as **acktvt.com/bms/** |
| `dps/index.html` | Data Protection Suite — enquiry form, served as **acktvt.com/dps/** |
| `privacy/index.html` | Privacy notice, served as **acktvt.com/privacy/** |
| `login/index.html` | Client portal — the sign-in chooser, served as **acktvt.com/login/**. Links out to each product's own sign-in page; no password is ever typed on this site |
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


## Regulatory clocks (2 Oct 2026)

The homepage's two clocks (hero card and timeline) have three states — *N days*,
*today*, *since <date>* — and never count below zero. The dates and wording are
read from the Data Protection Suite's milestone list (`public_milestones()` on
the DPS Supabase project) so a newly notified date appears here without a site
change; set `MS_URL` and `MS_KEY` near the end of `index.html` to the project's
REST URL and anon key. Until they are set, or if the call fails, the markup's
own dates and `data-after` wording are used, so the page never shows a blank.


## HD refresh and explainer videos (Oct 2026)

The look is set by the block headed **HD refresh** at the end of the main `<style>` in
`index.html` (self-hosted fonts, crisper surfaces, richer colour, and `zoom` steps at
2200/2800/3400/5000/7000 px wide so the page fills 2K, 4K and 8K screens instead of
floating in the middle). Delete that block to return to the previous look. Run
`python3 build_pages.py` after any change so the sub-pages pick it up.

Explainer videos (YouTube): Data Protection Suite `EF8qsiAfE6w`, Business Management
Suite `JPu1dl3rvAU`. They appear on the home page (`#watch-dps` inside the DPS section,
`#watch-bms` inside the BMS section — the hero's "Watch the explainers" button scrolls to
the first) and in the side column of `/dps/` and `/bms/`. Each is a poster button; the
YouTube player (privacy-enhanced youtube-nocookie.com) is created only when pressed. To
change a video, change the ID in `index.html` (`data-yt` and the "Watch on YouTube" link)
and in `build_pages.py` (`vid(...)` calls). The videos must have "Allow embedding" on
in YouTube Studio.
