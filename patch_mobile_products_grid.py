#!/usr/bin/env python3
"""
Patch: fix Products section card grid on mobile (forces 1 column instead
of squeezing 2 columns onto a narrow screen).

Run from ~/Downloads/talentaiq-website:
    python3 patch_mobile_products_grid.py
"""
import sys
from pathlib import Path

FILE = Path("index.html")

def apply(content, old, new, label):
    count = content.count(old)
    if count == 0:
        print(f"❌ STOPPED at step: {label}")
        print("   Anchor not found. File may have changed since this patch was written.")
        sys.exit(1)
    if count > 1:
        print(f"❌ STOPPED at step: {label}")
        print(f"   Anchor found {count} times (expected exactly 1) — not unique enough to patch safely.")
        sys.exit(1)
    print(f"✅ {label}")
    return content.replace(old, new, 1)

def main():
    if not FILE.exists():
        print("❌ index.html not found in current directory. Run this from ~/Downloads/talentaiq-website")
        sys.exit(1)

    content = FILE.read_text(encoding="utf-8")
    original = content

    content = apply(
        content,
        '@media(max-width:768px){section#trust div[style*="grid-template-columns:repeat(3"]{grid-template-columns:1fr!important}section#pricing div[style*="grid-template-columns:repeat(3"]{grid-template-columns:1fr!important}.pillars{grid-template-columns:1fr!important}',
        '@media(max-width:768px){section#trust div[style*="grid-template-columns:repeat(3"]{grid-template-columns:1fr!important}section#pricing div[style*="grid-template-columns:repeat(3"]{grid-template-columns:1fr!important}section#products div[style*="grid-template-columns:repeat(2"]{grid-template-columns:1fr!important}.pillars{grid-template-columns:1fr!important}',
        "Products card grid: 1 column on mobile"
    )

    if content == original:
        print("⚠️ No changes were made (unexpected). Nothing written.")
        sys.exit(1)

    FILE.write_text(content, encoding="utf-8")
    print("\n✅ Patch applied. index.html saved.")

if __name__ == "__main__":
    main()
