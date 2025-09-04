#!/usr/bin/env python3
"""
sanitize_for_gemini.py

Read a text file, apply Gemini-style aggressive sanitisation,
and write `<originalname>_sanitized.<ext>` (or just `_sanitized`
appended if no extension).

Usage:
    python sanitize_for_gemini.py <input_file>
"""

import re
import unicodedata
import html
import sys
from pathlib import Path


# ---- Core sanitiser (extracted verbatim from gemini_parser.py) ----
def aggressive_sanitize_text_content(text_content: str) -> str:
    """Strip bracketed notes, normalise Unicode, remove odd chars, etc."""
    if not text_content:
        return ""

    sanitized = str(text_content)

    # 1. Unescape HTML entities
    sanitized = html.unescape(sanitized)

    # 2. Unicode normalisation
    sanitized = unicodedata.normalize("NFKC", sanitized)

    # 3. Normalise line endings
    sanitized = sanitized.replace("\r\n", "\n").replace("\r", "\n")

    # 4. Remove bracketed content like [Applause] or [ ... ]
    sanitized = re.sub(r"\[.*?\]", " ", sanitized)

    # 5. Replace literal word "foreign" (tweak to taste)
    sanitized = sanitized.replace("foreign", " ")

    # 6. Allow only ASCII letters/numbers + common punctuation & whitespace
    allowed = re.compile(r"[^a-zA-Z0-9 \t\n\.\,\!\?\'\"\:\;\(\)\-\_]")
    sanitized = allowed.sub("", sanitized)

    # 7. Strip residual C0/C1 control chars
    sanitized = re.sub(r"[\x00-\x08\x0B-\x1F\x7F-\x9F]", "", sanitized)

    # 8. Collapse multiple spaces and trim lines
    sanitized = re.sub(r" +", " ", sanitized)
    lines = [line.strip() for line in sanitized.splitlines()]
    return "\n".join(lines)
# -------------------------------------------------------------------


def main():
    if len(sys.argv) != 2:
        print("Usage: python sanitize_for_gemini.py <input_file>", file=sys.stderr)
        sys.exit(1)

    in_path = Path(sys.argv[1]).expanduser().resolve()

    if not in_path.exists():
        print(f"Error: '{in_path}' not found.", file=sys.stderr)
        sys.exit(1)

    # Determine output file name
    if in_path.suffix:
        out_path = in_path.with_name(f"{in_path.stem}_sanitized{in_path.suffix}")
    else:
        out_path = in_path.with_name(f"{in_path.name}_sanitized")

    try:
        raw = in_path.read_text(encoding="utf-8", errors="ignore")
        clean = aggressive_sanitize_text_content(raw)
        out_path.write_text(clean, encoding="utf-8")
        print(f"Sanitised file written to: {out_path}")
    except Exception as e:
        print(f"Failed to sanitise '{in_path}': {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
