#!/usr/bin/env python3
"""
light_sanitize_for_gemini.py

Minimal, non-destructive clean-up for Gemini uploads.
Creates <original>_sanitized.<ext> next to the input file.
"""

import sys, html, unicodedata, re
from pathlib import Path

CONTROL_CHARS = re.compile(r'[\x00-\x08\x0B-\x1F\x7F-\x9F\u200B-\u200F\u202A-\u202E]')

def light_sanitize(text: str) -> str:
    if not text:
        return ""

    # 1) Unescape common HTML entities (&amp;, &lt;, etc.)
    text = html.unescape(text)

    # 2) Unicode normalisation (NFKC makes “ﬁ” → “fi”, homoglyph fix-ups, etc.)
    text = unicodedata.normalize("NFKC", text)

    # 3) Standardise line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # 4) Drop control / zero-width chars that break tokenisers
    text = CONTROL_CHARS.sub("", text)

    # 5) Collapse runs of spaces *within* a line (but keep intentional newlines)
    text = re.sub(r'[ \t]+', ' ', text)

    # 6) Strip trailing spaces on each line
    text = "\n".join(line.rstrip() for line in text.splitlines())

    return text

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python light_sanitize_for_gemini.py <input_file>")

    src = Path(sys.argv[1]).expanduser()
    if not src.exists():
        sys.exit(f"Error: '{src}' not found.")

    dst = src.with_name(f"{src.stem}_sanitized{src.suffix or ''}")
    try:
        raw = src.read_text(encoding="utf-8", errors="ignore")
        clean = light_sanitize(raw)
        dst.write_text(clean, encoding="utf-8")
        print(f"Sanitised file written to {dst}")
    except Exception as e:
        sys.exit(f"Failed: {e}")

if __name__ == "__main__":
    main()
