#!/usr/bin/env python3
"""
Patch: remove target="_blank" from internal /career links on the main site
(Products card + footer) so clicking Career stays in the same tab.

Run from ~/Downloads/talentaiq-website:
    python3 patch_career_same_tab.py
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

    # 1. Products card link
    content = apply(
        content,
        '<a href="https://talentaiq.in/career" target="_blank" rel="noopener" style="text-decoration:none;display:block;padding:2.25rem;',
        '<a href="/career" style="text-decoration:none;display:block;padding:2.25rem;',
        "Products card: same-tab, relative /career link"
    )

    # 2. Footer link
    content = apply(
        content,
        '<a href="https://talentaiq.in/career" target="_blank" rel="noopener">TalentAIQ Career</a>',
        '<a href="/career">TalentAIQ Career</a>',
        "Footer: same-tab, relative /career link"
    )

    if content == original:
        print("⚠️ No changes were made (unexpected). Nothing written.")
        sys.exit(1)

    FILE.write_text(content, encoding="utf-8")
    print("\n✅ Both links updated. index.html saved.")

if __name__ == "__main__":
    main()
