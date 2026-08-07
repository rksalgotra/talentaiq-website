#!/usr/bin/env python3
import os
FILE = os.path.expanduser("~/Downloads/talentaiq-website/index.html")
code = open(FILE).read()

# ── 1. Nav: rebrand wordmark to show "Labs", add Products link ──────────────
OLD_NAV = '<nav><div class="nav-w"><a class="nav-logo" href="#"><div class="nav-logomark">T</div><span class="nav-wordmark">Talent<b>AIQ</b></span></a><div class="nav-links"><a class="nav-a" href="#find">Find</a><a class="nav-a" href="#hire">Hire</a><a class="nav-a" href="#grow">Grow</a><a class="nav-a" href="#how">How it works</a><a class="nav-a" href="#trust">AI Safety</a><a class="nav-a" href="#capabilities">Platform</a><a class="nav-a" href="#pricing">Pricing</a></div><div class="nav-end"><a class="nav-ghost" href="https://careers.talentaiq.in/login" target="_blank" rel="noopener">Sign in</a><a class="nav-cta" href="mailto:sales@talentaiq.in?subject=TalentAIQ%20Demo%20Request&body=Hi%20TalentAIQ%20Team%2C%0A%0AI%20would%20like%20to%20schedule%20a%20demo%20of%20TalentAIQ%20for%20our%20organisation.%0A%0AName%3A%20%0ADesignation%3A%20%0ACompany%3A%20%0AIndustry%3A%20%0AEmployee%20Count%3A%20%0ACurrent%20ATS%20(if%20any)%3A%20%0A%0APreferred%20demo%20date%2Ftime%3A%20%0A%0AKey%20requirements%3A%0A-%20%0A-%20%0A%0ALooking%20forward%20to%20hearing%20from%20you.%0A%0ABest%20regards">Request Demo</a></div></div></nav>'

NEW_NAV = '<nav><div class="nav-w"><a class="nav-logo" href="#"><div class="nav-logomark">T</div><span class="nav-wordmark">Talent<b>AIQ</b> Labs<sup style="font-size:.5em;font-weight:600;margin-left:2px">\u2122</sup></span></a><div class="nav-links"><a class="nav-a" href="#products">Products</a><a class="nav-a" href="#find">Find</a><a class="nav-a" href="#hire">Hire</a><a class="nav-a" href="#grow">Grow</a><a class="nav-a" href="#trust">AI Safety</a><a class="nav-a" href="#capabilities">Platform</a></div><div class="nav-end"><a class="nav-ghost" href="https://careers.talentaiq.in/login" target="_blank" rel="noopener">Sign in</a><a class="nav-cta" href="mailto:sales@talentaiq.in?subject=TalentAIQ%20Demo%20Request&body=Hi%20TalentAIQ%20Team%2C%0A%0AI%20would%20like%20to%20schedule%20a%20demo%20of%20TalentAIQ%20for%20our%20organisation.%0A%0AName%3A%20%0ADesignation%3A%20%0ACompany%3A%20%0AIndustry%3A%20%0AEmployee%20Count%3A%20%0ACurrent%20ATS%20(if%20any)%3A%20%0A%0APreferred%20demo%20date%2Ftime%3A%20%0A%0AKey%20requirements%3A%0A-%20%0A-%20%0A%0ALooking%20forward%20to%20hearing%20from%20you.%0A%0ABest%20regards">Request Demo</a></div></div></nav>'

if code.count(OLD_NAV) == 1:
    code = code.replace(OLD_NAV, NEW_NAV)
    print("1. Nav updated: TalentAIQ Labs\u2122 wordmark + Products link")
else:
    print("1. WARNING: nav anchor not matched exactly (count=%d)" % code.count(OLD_NAV))

# ── 2. Insert Products section right after <nav> closes, before hero ────────
PRODUCTS_SECTION = '''
<section id="products" style="padding:4rem 0 3rem;background:var(--bg)">
<div class="sw">
<div class="reveal" style="max-width:640px;margin:0 auto 3rem;text-align:center">
<div class="eyebrow" style="justify-content:center">OUR PRODUCTS</div>
<h2 class="s-h2">One parent brand.<br/>Two purpose-built products.</h2>
<p class="s-lead">TalentAIQ Labs\u2122 builds AI-native hiring infrastructure \u2014 for enterprises hiring at scale, and for candidates navigating their next role.</p>
</div>
<div class="reveal" style="display:grid;grid-template-columns:repeat(2,1fr);gap:1.75rem;max-width:960px;margin:0 auto">

<a href="#hero-enterprise" style="text-decoration:none;display:block;padding:2.25rem;border-radius:20px;border:1px solid var(--border);background:var(--surface);transition:transform .2s,box-shadow .2s" onmouseover="this.style.transform='translateY(-4px)';this.style.boxShadow='0 12px 32px rgba(0,0,0,.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
<div style="width:44px;height:44px;border-radius:12px;background:var(--brand);display:flex;align-items:center;justify-content:center;margin-bottom:1.25rem">
<svg width="22" height="22" fill="none" stroke="#fff" stroke-width="2" viewBox="0 0 24 24"><rect x="2" y="6" width="20" height="16" rx="2"/><path d="M2 10h20M10 6V2"/></svg>
</div>
<div style="font-size:.7rem;font-weight:700;letter-spacing:.08em;color:var(--brand);text-transform:uppercase;margin-bottom:.4rem">For Enterprises</div>
<h3 style="font-family:var(--fd);font-size:1.35rem;font-weight:700;color:var(--t1);margin-bottom:.6rem">TalentAIQ Enterprise</h3>
<p style="font-size:.9rem;color:var(--t3);line-height:1.6;margin-bottom:1rem">AI-powered hiring intelligence for regulated industries \u2014 explainable scoring, auditable pipelines, and internal mobility, all in one platform.</p>
<span style="font-size:.85rem;font-weight:600;color:var(--brand);display:inline-flex;align-items:center;gap:.35rem">Explore Enterprise <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M5 12h14M13 5l7 7-7 7"/></svg></span>
</a>

<a href="https://talentaiq.in/career" target="_blank" rel="noopener" style="text-decoration:none;display:block;padding:2.25rem;border-radius:20px;border:1px solid var(--border);background:var(--surface);transition:transform .2s,box-shadow .2s" onmouseover="this.style.transform='translateY(-4px)';this.style.boxShadow='0 12px 32px rgba(0,0,0,.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
<div style="width:44px;height:44px;border-radius:12px;background:#059669;display:flex;align-items:center;justify-content:center;margin-bottom:1.25rem">
<svg width="22" height="22" fill="none" stroke="#fff" stroke-width="2" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
</div>
<div style="font-size:.7rem;font-weight:700;letter-spacing:.08em;color:#059669;text-transform:uppercase;margin-bottom:.4rem">For Job Seekers</div>
<h3 style="font-family:var(--fd);font-size:1.35rem;font-weight:700;color:var(--t1);margin-bottom:.6rem">TalentAIQ Career</h3>
<p style="font-size:.9rem;color:var(--t3);line-height:1.6;margin-bottom:1rem">An AI job-application agent built for India \u2014 finds relevant roles, tailors applications, and applies on your behalf.</p>
<span style="font-size:.85rem;font-weight:600;color:#059669;display:inline-flex;align-items:center;gap:.35rem">Explore Career <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M5 12h14M13 5l7 7-7 7"/></svg></span>
</a>

</div>
</div>
</section>
'''

if 'id="products"' not in code:
    code = code.replace('<section class="hero">', PRODUCTS_SECTION + '\n<section class="hero" id="hero-enterprise">')
    print("2. Products section inserted before hero")
else:
    print("2. Products section already exists")

# ── 3. Hero kicker: clarify this page = Enterprise product ──────────────────
OLD_KICKER = '<div class="hero-kicker"><div class="hk-dot"></div><span class="hk-text">AI-Powered Recruitment · Enterprise</span></div>'
NEW_KICKER = '<div class="hero-kicker"><div class="hk-dot"></div><span class="hk-text">TalentAIQ Enterprise \u00b7 by TalentAIQ Labs\u2122</span></div>'
if OLD_KICKER in code:
    code = code.replace(OLD_KICKER, NEW_KICKER)
    print("3. Hero kicker updated to show product-under-parent-brand")
else:
    print("3. WARNING: hero kicker anchor not found")

# ── 4. Footer: rebrand to Labs, add Products column ──────────────────────────
OLD_FOOTER = '<footer><div class="footer-grid"><div class="footer-brand"><span class="nav-wordmark">Talent<b>AIQ</b></span><p>Find, hire, and grow talent in regulated enterprises. AI-driven decisions you can explain, audit, and defend.</p></div><div class="footer-col"><h4>Platform</h4><a href="#find">AI Matching</a><a href="#hire">ATS Pipeline</a><a href="#grow">Internal Mobility</a><a href="#capabilities">Career Portal</a><a href="#capabilities">Integrations</a></div><div class="footer-col"><h4>Company</h4><a href="#trust">AI Safety</a><a href="https://www.linkedin.com/company/talentaiq-labs" target="_blank" rel="noopener">LinkedIn</a><a href="mailto:sales@talentaiq.in?subject=TalentAIQ%20Demo%20Request&body=Hi%20TalentAIQ%20Team%2C%0A%0AI%20would%20like%20to%20schedule%20a%20demo%20of%20TalentAIQ%20for%20our%20organisation.%0A%0AName%3A%20%0ADesignation%3A%20%0ACompany%3A%20%0AIndustry%3A%20%0AEmployee%20Count%3A%20%0ACurrent%20ATS%20(if%20any)%3A%20%0A%0APreferred%20demo%20date%2Ftime%3A%20%0A%0AKey%20requirements%3A%0A-%20%0A-%20%0A%0ALooking%20forward%20to%20hearing%20from%20you.%0A%0ABest%20regards">Contact</a></div><div class="footer-col"><h4>Legal</h4><a href="#privacy">Privacy Policy</a><a href="#terms">Terms</a><a href="#privacy">Data Security</a><a href="#trust">DEI Policy</a></div></div><div class="footer-bottom"><div class="footer-copy">&copy; 2026 TalentAIQ Labs\u2122. All rights reserved. Bengaluru, India.</div><div class="footer-links"><a href="#privacy">Privacy</a><a href="#terms">Terms</a><a href="mailto:sales@talentaiq.in?subject=TalentAIQ%20Demo%20Request&body=Hi%20TalentAIQ%20Team%2C%0A%0AI%20would%20like%20to%20schedule%20a%20demo%20of%20TalentAIQ%20for%20our%20organisation.%0A%0AName%3A%20%0ADesignation%3A%20%0ACompany%3A%20%0AIndustry%3A%20%0AEmployee%20Count%3A%20%0ACurrent%20ATS%20(if%20any)%3A%20%0A%0APreferred%20demo%20date%2Ftime%3A%20%0A%0AKey%20requirements%3A%0A-%20%0A-%20%0A%0ALooking%20forward%20to%20hearing%20from%20you.%0A%0ABest%20regards">sales@talentaiq.in</a></div></div>'

NEW_FOOTER = '<footer><div class="footer-grid"><div class="footer-brand"><span class="nav-wordmark">Talent<b>AIQ</b> Labs<sup style="font-size:.5em">\u2122</sup></span><p>Building AI-native hiring infrastructure \u2014 for enterprises hiring at scale, and for candidates navigating their next role.</p></div><div class="footer-col"><h4>Products</h4><a href="#hero-enterprise">TalentAIQ Enterprise</a><a href="https://talentaiq.in/career" target="_blank" rel="noopener">TalentAIQ Career</a><a href="#products">All Products</a></div><div class="footer-col"><h4>Platform</h4><a href="#find">AI Matching</a><a href="#hire">ATS Pipeline</a><a href="#grow">Internal Mobility</a><a href="#trust">AI Safety</a></div><div class="footer-col"><h4>Company</h4><a href="https://www.linkedin.com/company/talentaiq-labs" target="_blank" rel="noopener">LinkedIn</a><a href="mailto:sales@talentaiq.in?subject=TalentAIQ%20Demo%20Request&body=Hi%20TalentAIQ%20Team%2C%0A%0AI%20would%20like%20to%20schedule%20a%20demo%20of%20TalentAIQ%20for%20our%20organisation.%0A%0AName%3A%20%0ADesignation%3A%20%0ACompany%3A%20%0AIndustry%3A%20%0AEmployee%20Count%3A%20%0ACurrent%20ATS%20(if%20any)%3A%20%0A%0APreferred%20demo%20date%2Ftime%3A%20%0A%0AKey%20requirements%3A%0A-%20%0A-%20%0A%0ALooking%20forward%20to%20hearing%20from%20you.%0A%0ABest%20regards">Contact</a><a href="#privacy">Privacy Policy</a><a href="#terms">Terms</a></div></div><div class="footer-bottom"><div class="footer-copy">&copy; 2026 TalentAIQ Labs\u2122. All rights reserved. Bengaluru, India.</div><div class="footer-links"><a href="#privacy">Privacy</a><a href="#terms">Terms</a><a href="mailto:sales@talentaiq.in?subject=TalentAIQ%20Demo%20Request&body=Hi%20TalentAIQ%20Team%2C%0A%0AI%20would%20like%20to%20schedule%20a%20demo%20of%20TalentAIQ%20for%20our%20organisation.%0A%0AName%3A%20%0ADesignation%3A%20%0ACompany%3A%20%0AIndustry%3A%20%0AEmployee%20Count%3A%20%0ACurrent%20ATS%20(if%20any)%3A%20%0A%0APreferred%20demo%20date%2Ftime%3A%20%0A%0AKey%20requirements%3A%0A-%20%0A-%20%0A%0ALooking%20forward%20to%20hearing%20from%20you.%0A%0ABest%20regards">sales@talentaiq.in</a></div></div>'

if code.count(OLD_FOOTER) == 1:
    code = code.replace(OLD_FOOTER, NEW_FOOTER)
    print("4. Footer updated: Labs branding + Products column")
else:
    print("4. WARNING: footer anchor not matched exactly (count=%d)" % code.count(OLD_FOOTER))

open(FILE, 'w').write(code)
print("\nDone. Review locally, then deploy:")
print("  cd ~/Downloads/talentaiq-website")
print("  git add -A && git commit -m 'feat: TalentAIQ Labs parent brand + Products section'")
print("  git push origin main && npx vercel --prod")
