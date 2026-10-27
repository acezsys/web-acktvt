/* =========================================================
   acktvt.com — analytics with consent
   Paste your IDs below. Until an ID is filled in, nothing
   loads and no cookie banner is shown.
   ========================================================= */
window.PZ_ANALYTICS = {
  ga4: '',      // Google Analytics 4 Measurement ID, e.g. 'G-ABC123XYZ9'
  clarity: ''   // Microsoft Clarity project ID, e.g. 'abcd1234ef' (optional)
};

(function(){
  var CFG = window.PZ_ANALYTICS || {};
  var KEY = 'acktvt-consent-v1';
  var enabled = !!(CFG.ga4 || CFG.clarity);
  var loaded = false;

  function getChoice(){ try { return localStorage.getItem(KEY); } catch(e){ return null; } }
  function setChoice(v){ try { localStorage.setItem(KEY, v); } catch(e){} }

  function loadAnalytics(){
    if(loaded) return; loaded = true;
    if(CFG.ga4){
      var s = document.createElement('script');
      s.async = true; s.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(CFG.ga4);
      document.head.appendChild(s);
      window.dataLayer = window.dataLayer || [];
      window.gtag = function(){ dataLayer.push(arguments); };
      gtag('js', new Date());
      gtag('config', CFG.ga4, { anonymize_ip: true });
    }
    if(CFG.clarity){
      (function(c,l,a,r,i,t,y){c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
        t=l.createElement(r);t.async=1;t.src='https://www.clarity.ms/tag/'+i;
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);})(window,document,'clarity','script',CFG.clarity);
    }
  }

  /* Lead events: email, phone, WhatsApp and "book a call" clicks */
  document.addEventListener('click', function(e){
    if(!loaded || !window.gtag) return;
    var a = e.target.closest && e.target.closest('a'); if(!a) return;
    var h = a.getAttribute('href') || '', method = null;
    if(h.indexOf('mailto:') === 0) method = 'email';
    else if(h.indexOf('tel:') === 0) method = 'phone';
    else if(h.indexOf('wa.me') > -1 || h.indexOf('whatsapp') > -1) method = 'whatsapp';
    else if(/walkthrough|get started|start a .*trial|book a|live demo/i.test(a.textContent || '')) method = 'cta';
    if(method) gtag('event', 'generate_lead', { method: method, link_url: h, page_path: location.pathname });
  }, true);

  document.addEventListener('submit', function(e){ if(loaded && window.gtag) gtag('event','generate_lead',{ method:'form', page_path: location.pathname }); }, true);

  function styles(){
    if(document.getElementById('pz-consent-css')) return;
    var c = document.createElement('style'); c.id = 'pz-consent-css';
    c.textContent =
      '.pz-consent{position:fixed;left:16px;right:16px;bottom:calc(16px + env(safe-area-inset-bottom,0px));z-index:500;max-width:760px;margin-inline:auto;'+
      'background:#fff;color:var(--ink,#0F1512);border:1px solid var(--line,#DCE5DF);border-radius:12px;box-shadow:0 24px 60px -24px rgba(11,18,53,.45);'+
      'padding:18px 20px;display:flex;gap:16px;align-items:center;flex-wrap:wrap;font-family:var(--font-body,"Inter",system-ui,sans-serif);font-size:.92rem;line-height:1.5}'+
      '.pz-consent p{margin:0;flex:1 1 320px;max-width:none}'+
      '.pz-consent a{color:var(--green,#006038);font-weight:700;text-decoration:underline}'+
      '.pz-consent .pz-b{display:flex;gap:10px;flex-wrap:wrap}'+
      '.pz-consent button{font:inherit;font-weight:700;padding:.65em 1.2em;border-radius:999px;cursor:pointer;border:1.5px solid var(--green,#006038)}'+
      '.pz-consent .pz-ok{background:var(--green,#006038);color:#fff}'+
      '.pz-consent .pz-no{background:transparent;color:var(--green,#006038)}';
    document.head.appendChild(c);
  }

  function showBanner(){
    if(!enabled) return;
    styles();
    var old = document.querySelector('.pz-consent'); if(old) old.remove();
    var b = document.createElement('div');
    b.className = 'pz-consent'; b.setAttribute('role','dialog'); b.setAttribute('aria-label','Cookie choices');
    b.innerHTML = '<p>We would like to use analytics cookies to understand how visitors use this site, so we can improve it. Nothing is collected unless you agree. <a href="/privacy/">Privacy notice</a></p>'+
      '<div class="pz-b"><button type="button" class="pz-no">Decline</button><button type="button" class="pz-ok">Accept</button></div>';
    b.querySelector('.pz-ok').addEventListener('click', function(){ setChoice('granted'); b.remove(); loadAnalytics(); });
    b.querySelector('.pz-no').addEventListener('click', function(){ setChoice('denied'); b.remove(); if(loaded) location.reload(); });
    document.body.appendChild(b);
  }

  window.pzConsent = { open: showBanner };
  document.addEventListener('click', function(e){ var c = e.target.closest && e.target.closest('.pz-cookie-link'); if(c){ e.preventDefault(); showBanner(); } });

  function start(){
    if(!enabled) return;
    var c = getChoice();
    if(c === 'granted') loadAnalytics();
    else if(c !== 'denied') showBanner();
  }
  if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();
