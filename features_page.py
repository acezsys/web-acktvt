# ---------------------------------------------------------------- feature pages  (acktvt.com/bms/features/, acktvt.com/dps/features/)
# Run from build_pages.py after the other pages (needs nav, footer, head_meta, style, EXTRA_CSS, HERE, WA, DEMO_BMS, LAUNCH_TRIAL).
# Nov 2026: one place for the full feature list of each suite; prowessz.com's Products page links here.
# Wording follows what is built and already described on the home page. No prices; plan contents are confirmed in the walkthrough.
import html as _h

def _deep(x):   # pages two levels down: links that go back one level must go back two
    return x.replace('href="../', 'href="../../').replace('src="../', 'src="../../')

FX_CSS = """
<style>
  .fx-hero{padding:132px 0 46px;background:radial-gradient(1200px 500px at 15% -10%,rgba(245,184,46,.16),transparent 60%),var(--navy,#0b1530);color:#fff}
  .fx-hero .eyebrow{color:var(--gold-bright,#FFD873)}
  .fx-hero h1{font-size:clamp(30px,4.2vw,50px);line-height:1.08;margin:10px 0 14px;max-width:22ch}
  .fx-hero p{max-width:66ch;opacity:.86;font-size:17px;line-height:1.6;margin:0}
  .fx-hero .acts{display:flex;gap:12px;flex-wrap:wrap;margin-top:24px}
  .fx-jump{display:flex;gap:8px;flex-wrap:wrap;margin-top:26px}
  .fx-jump a{font-size:13px;padding:6px 12px;border:1px solid rgba(255,255,255,.28);border-radius:999px;color:#fff;text-decoration:none}
  .fx-jump a:hover{border-color:var(--gold-bright,#FFD873)}
  .fx-body{padding:46px 0 70px;background:#fff}
  .fx-group{margin:0 0 44px;scroll-margin-top:96px}
  .fx-group h2{font-size:clamp(22px,2.4vw,30px);margin:0 0 6px}
  .fx-group > p{color:var(--ink-2,#4a5163);max-width:72ch;margin:0 0 18px;line-height:1.6}
  .fx-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:14px}
  .fx-card{border:1px solid var(--line,#e6e8ee);border-radius:14px;padding:18px 18px 16px;background:#fff}
  .fx-card h3{font-size:16.5px;margin:0 0 6px;display:flex;gap:8px;align-items:baseline;flex-wrap:wrap}
  .fx-card p{margin:0;color:var(--ink-2,#4a5163);font-size:14.5px;line-height:1.55}
  .fx-card ul{margin:8px 0 0;padding-left:18px;color:var(--ink-2,#4a5163);font-size:14px;line-height:1.55}
  .fx-tag{font-family:Inter,Arial,sans-serif;font-size:11px;letter-spacing:.6px;text-transform:uppercase;font-weight:700;color:var(--gold-text,#7A5200);background:rgba(245,184,46,.16);border-radius:6px;padding:2px 7px}
  .fx-note{border-left:3px solid var(--gold,#F5B82E);background:#FBF8EF;padding:14px 18px;border-radius:0 10px 10px 0;max-width:80ch;color:var(--ink-2,#4a5163);font-size:14.5px;line-height:1.6}
  .fx-cta{display:flex;gap:12px;flex-wrap:wrap;margin-top:22px}
</style>
"""

def _cards(items):
    out = []
    for title, tag, text, bullets in items:
        t = f'<span class="fx-tag">{_h.escape(tag)}</span>' if tag else ''
        b = ('<ul>' + ''.join(f'<li>{x}</li>' for x in bullets) + '</ul>') if bullets else ''
        out.append(f'<div class="fx-card"><h3>{_h.escape(title)}{t}</h3><p>{text}</p>{b}</div>')
    return '<div class="fx-grid">' + ''.join(out) + '</div>'

def _page(slug, title, desc, eyebrow, h1, lede, acts, groups, closing):
    jump = ''.join(f'<a href="#{gid}">{_h.escape(gname)}</a>' for gid, gname, _, _ in groups)
    body = ''.join(f'<div class="fx-group" id="{gid}"><h2>{_h.escape(gname)}</h2><p>{gintro}</p>{_cards(items)}</div>' for gid, gname, gintro, items in groups)
    url = f'https://acktvt.com/{slug}/features/'
    head = (f'<title>{_h.escape(title)}</title>\n<meta name="description" content="{_h.escape(desc)}" />\n'
            f'<meta name="robots" content="index, follow, max-image-preview:large" />\n<link rel="canonical" href="{url}" />\n'
            f'<meta property="og:type" content="website" />\n<meta property="og:site_name" content="acktvt" />\n<meta property="og:locale" content="en_IN" />\n'
            f'<meta property="og:title" content="{_h.escape(title)}" />\n<meta property="og:description" content="{_h.escape(desc)}" />\n'
            f'<meta property="og:url" content="{url}" />\n<meta property="og:image" content="https://acktvt.com/assets/og-image.jpg" />\n'
            f'<meta name="twitter:card" content="summary_large_image" />\n')
    page_html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
{head}{_deep(head_meta)}{style}{EXTRA_CSS}{FX_CSS}
</head>
<body>
{_deep(nav)}
<section class="fx-hero"><div class="wrap">
  <span class="eyebrow">{eyebrow}</span>
  <h1>{h1}</h1>
  <p>{lede}</p>
  <div class="acts">{acts}</div>
  <div class="fx-jump" aria-label="Jump to">{jump}</div>
</div></section>
<section class="fx-body"><div class="wrap">
{body}
{closing}
</div></section>
{_deep(footer)}
<script src="/assets/consent.js" defer></script>
</body>
</html>
"""
    os.makedirs(os.path.join(HERE, slug, 'features'), exist_ok=True)
    open(os.path.join(HERE, slug, 'features', 'index.html'), 'w', encoding='utf-8').write(page_html)
    print('wrote', slug + '/features/index.html', len(page_html) // 1024, 'KB')

SEC_LINK = '<a href="https://www.prowessz.com/acktvt.html#security" style="text-decoration:underline">security standards</a>'

# ---------------------------------------------------------------- BMS
_page('bms', 'acktvt BMS Features: Order to Cash, Planning, Order Intelligence | acktvt',
      'Every feature of the acktvt Business Management Suite: orders, purchase, stock, production, quality, dispatch, production planning, Order Intelligence, finance, HR, service, Scan, portals, Meet, Genuine and Origin.',
      'Business Management Suite · features',
      'Everything the Business Management Suite does, <em style="color:var(--gold-bright,#FFD873)">in one place.</em>',
      'One system from customer order to cash, built for growing Indian manufacturers and traders. Switch on the modules you need today and add more as you grow.',
      f'<a class="btn btn-green" href="{DEMO_BMS}" target="_blank" rel="noopener">Open the live demo</a><a class="btn btn-ghost" href="../" style="color:#fff;border-color:rgba(255,255,255,.4)">Book a walkthrough</a>',
      [
       ('order-to-cash', 'Order to cash', 'Every order line, purchase, inspection and dispatch links back to the order it belongs to, with a full status history on every record.', [
         ('Tender, bid & sales pipeline', '', 'GeM and private tenders, enquiries and quotations tracked from first contact to won or lost.', ['Pre-tender pipeline stages', 'Quoted-to-won tracking']),
         ('Sales orders', '', 'Customer PO to work order to order lines, each with its delivery period, payment terms and deductions.', None),
         ('Purchase', '', 'RFQ, quotation, approval, vendor PO, receipt and inspection, with rework, replacement and return.', None),
         ('Stores & inventory', '', 'Raw material, bought-out, work in progress, finished and rejected stock kept apart, across warehouses.', ['Batch and serial-number tracking', 'Trace from supplier to customer']),
         ('Production', '', 'Each part moves through its stages: stock check, cutting, machining, fabrication, assembly, inspection, lab and third-party inspection.', None),
         ('Quality', '', 'Internal inspection, external lab reports and third-party inspection, tied to the part and the order.', None),
         ('GST invoicing & receivables', '', 'GST-compliant tax invoices with an HSN-wise summary, payments received, and TDS, LD and SD deductions.', None),
       ]),
       ('planning', 'Planning & prediction', 'See what is coming before it arrives: which orders to chase, what to make and buy, and where the load will be.', [
         ('Order Intelligence', 'Order prediction', 'A Win Score for every enquiry with the next best actions, worked out from your own records.', ['Order risk register with a go / no-go before you quote', 'Order timeline with a quarter outlook']),
         ('Production planning', '', 'Put the parts you have to deliver on a plan and run it.', ['Material netted against stock and open purchase orders', 'What to make and what to buy, by when', 'A schedule on each machine\'s time, with the load on every work centre']),
         ('BOM & routing', '', 'Bills of material and the route each part takes through the shop, the base for planning and costing.', None),
         ('Management dashboard & alerts', '', 'Monthly review, delays, dues and pendency at a glance, with e-mail alerts for what slips.', None),
       ]),
       ('control', 'Control & trust', 'Know who did what, release only what is ready, and give buyers proof they can check.', [
         ('Dispatch controls', '', 'Partial dispatch with a signed release from each department head before goods leave.', None),
         ('Full history on every record', '', 'Every order, part and document carries its status history: who changed what, and when.', None),
         ('Roles & module access', '', 'Super Admin, module admins and users, each seeing only the modules they are given.', None),
         ('acktvt Genuine', 'Built in', 'A QR code on test certificates, dispatch release certificates and tax invoices that anyone can scan to check the document as issued, and whether it is still current.', None),
         ('acktvt Origin', 'Built in', 'A QR label on each batch that shows buyers where and when it was made and how it was checked. Recall a batch in one step.', None),
       ]),
       ('people-money', 'People & money', 'Management accounting and HR that sit on the same records as your orders.', [
         ('Finance', '', 'Cost centres and budgets, inventory valuation across warehouses, job costing, receivables and payables with a cash-flow projection, approvals, TDS and GST registers, and a Tally export bridge.', ['The ledger and statutory filing stay with your chartered accountant']),
         ('HR', '', 'Employee master, lifecycle and documents with access control.', ['Shifts, attendance and overtime, with biometric import', 'Leave with approvals, and self-service', 'Statutory registers and payroll export']),
         ('Projects', '', 'Project reporting for work that runs beyond a single order.', None),
       ]),
       ('service-floor', 'Service, shop floor & partners', 'Look after what you have sold, work faster on the floor, and let customers and vendors serve themselves.', [
         ('Service & AMC', '', 'Every machine you dispatch becomes a record with its warranty.', ['AMC contracts with a maintenance plan and renewal quotations', 'Service tickets with response targets, service reports and GST service invoices']),
         ('acktvt Scan', '', 'Scan QR labels and barcodes with a phone: receive goods, issue material, start and finish job cards, and check what is packed for dispatch. Prints QR labels for parts, locations, batches and job cards.', None),
         ('Customer & vendor portals', '', 'Customers see their orders, dispatches, invoices and statement; vendors confirm purchase orders, send dispatch notes and see payments. Sign-in by e-mail code, no passwords to share.', None),
         ('acktvt Meet', 'Built in', 'Call a customer, vendor or colleague from the record you are working on: work orders, enquiries, purchase orders, inspections and projects. Nothing to install, up to 50 people.', None),
       ]),
      ],
      f"""<div class="fx-note"><b>Plans and modules.</b> Modules are switched on per plan, and you add more as you grow. In a walkthrough we show which plan includes what for a business like yours.
      Security is built in: personal data is encrypted, backups are sealed and every sign-in is protected. See our {SEC_LINK}.</div>
      <div class="fx-cta"><a class="btn btn-green" href="{DEMO_BMS}" target="_blank" rel="noopener">Open the live demo</a><a class="btn btn-primary" href="{WA}" target="_blank" rel="noopener">WhatsApp +91 80802 55000</a><a class="btn btn-ghost" href="../">Back to the Business Management Suite</a></div>""")

# ---------------------------------------------------------------- DPS
_page('dps', 'acktvt DPS Features: DPDP Act Registers, Clocks and Evidence | acktvt',
      'Every feature of the acktvt Data Protection Suite for India\'s DPDP Act: data map, notices, consent, rights desk, breach response, retention, gap assessment, DPIA, evidence pack and sector packs.',
      'Data Protection Suite · features',
      'The DPDP Act as registers, clocks and evidence. <em style="color:var(--gold-bright,#FFD873)">Every feature.</em>',
      'Built for hospitals and labs, manufacturers, real estate developers and educational institutions. Standard covers the obligations the Act and Rules place on a Data Fiduciary; Advanced and Premium add continuous monitoring and Prowessz in the loop.',
      f'<a class="btn btn-green" href="{LAUNCH_TRIAL}" target="_blank" rel="noopener">Start a 14-day trial</a><a class="btn btn-ghost" href="../" style="color:#fff;border-color:rgba(255,255,255,.4)">Book a walkthrough</a>',
      [
       ('standard', 'Standard: compliant', 'Every register and workflow a Data Fiduciary needs, from the base tier.', [
         ('Data map & RoPA', 'Standard', 'Every processing activity, its purpose, basis and retention.', None),
         ('Notices', 'Standard', 'Itemised notices in English plus any Eighth Schedule language.', None),
         ('Consent ledger', 'Standard', 'Consent and withdrawal, provable per person and per purpose.', None),
         ('Rights desk & privacy page', 'Standard', 'Access, correction, erasure and nomination on a 90-day clock, with a hosted request page.', None),
         ('Vendors & DPAs', 'Standard', 'A processor register with the status of each data processing agreement and where the data is held.', None),
         ('Security safeguards', 'Standard', 'The Rule 6 minimums, each with evidence and a date.', None),
         ('Breach response', 'Standard', 'A playbook with the 72-hour report to the Board drafted from the record.', None),
         ('Retention & erasure', 'Standard', 'Rules per record category and an append-only erasure log.', None),
         ('Grievances & parental consent', 'Standard', 'A 90-day grievance clock; verifiable guardian consent, with Rule 12 exemptions recorded.', None),
         ('Website & cookie scanner', 'Standard', 'Trackers, cookies, forms and the notice on your public site, graded, with a fix for each finding.', None),
       ]),
       ('advanced', 'Advanced: continuous', 'Nothing goes stale: scores, reviews, training and an audit trail.', [
         ('Scored gap assessment', 'Advanced', '35 controls plus your sector\'s own, checked automatically from the registers, with history.', None),
         ('Reviews & reminders', 'Advanced', 'A review cadence per register and a weekly digest.', None),
         ('Policies & documents', 'Advanced', 'Versioned from Prowessz templates, with acknowledgements.', None),
         ('Staff training & undertakings', 'Advanced', 'Sessions, attendance, validity and signed undertakings.', None),
         ('Shadow-IT discovery', 'Advanced', 'Sweeps and staff reports of WhatsApp groups, drives and spreadsheets holding personal data.', None),
         ('Data Champion programme', 'Advanced', 'The Data Champion\'s first 90 days, step by step.', None),
         ('Vendor questionnaires', 'Advanced', '18 weighted questions on a no-login link, scored automatically.', None),
         ('Immutable audit log', 'Advanced', 'Every change and every export, kept 12 months or longer if your laws need it.', None),
         ('Accreditation crosswalk', 'Advanced', 'Your DPDP evidence lined up against NABH (healthcare) or ISO/IEC 27001 Annex A (manufacturing, real estate): one file for both auditors.', None),
       ]),
       ('premium', 'Premium: assured', 'The full suite with Prowessz Consulting in the loop.', [
         ('DPIA with consultant review', 'Premium', 'Structured assessment, scored risk register, mandatory Prowessz review, sign-off and an annual re-check.', None),
         ('Evidence pack', 'Premium', 'One click: every register, the score and the reviews as a dated, printable bundle, with no personal names.', None),
         ('Regulatory watch', 'Premium', 'Curated updates e-mailed on publication and acknowledged with a written trail.', None),
         ('Multi-site groups', 'Premium', 'Switch between hospitals, plants, projects or campuses, with a group dashboard, template registers and consolidated export.', None),
         ('Prowessz services', 'Premium', 'Outsourced privacy officer, quarterly health-check, breach on-call, annual drill and mock audit.', None),
       ]),
       ('sectors', 'Sector packs & add-on', 'The same suite in your sector\'s language, with a sample organisation to explore on day one.', [
         ('Healthcare', 'Sector pack', 'Patients, UHIDs, OPD and IPD records, lab reports and TPAs.', ['NABH crosswalk and ABDM readiness', 'Child-data register with the clinical exemption and verified parental consent']),
         ('Manufacturing', 'Sector pack', 'Employees, contract workers, applicants, visitors, dealers and customers.', ['ISO/IEC 27001 Annex A crosswalk', 'Biometric attendance, CCTV, contract-labour and dealer-KYC risks']),
         ('Real estate', 'Sector pack', 'Prospects, site visitors, homebuyers, co-applicants and residents.', ['Lead-consent log: partners told when a prospect says stop', 'RERA-registered channel partners with their own data clause']),
         ('Education', 'Sector pack', 'Students under eighteen, parents and enquirers, faculty and the apps.', ['Child-data register with the Fourth Schedule exemption where it applies', 'Enquiry-consent log for admissions and telecalling']),
         ('acktvt Genuine for your records', 'Add-on, any tier', 'Consent, rights-request and breach records made tamper-evident: each day\'s fingerprints are stamped on the Bitcoin blockchain. Personal data never leaves the suite, and erasure still works.', None),
       ]),
      ],
      f"""<div class="fx-note"><b>acktvt is your Data Processor, not a Consent Manager.</b> The suite helps you meet your duties under the DPDP Act and Rules; the responsibility for compliance stays with your organisation.
      Security is built in: row-level separation of every workspace, two-step verification for administrators and an append-only audit log. See our {SEC_LINK}.</div>
      <div class="fx-cta"><a class="btn btn-green" href="{LAUNCH_TRIAL}" target="_blank" rel="noopener">Start a 14-day trial</a><a class="btn btn-primary" href="{WA}" target="_blank" rel="noopener">WhatsApp +91 80802 55000</a><a class="btn btn-ghost" href="../">Back to the Data Protection Suite</a></div>""")
