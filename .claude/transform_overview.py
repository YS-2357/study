"""Transform domain overviews: 'Study Order' -> 'Concepts', numbered list -> bullets.

Usage:
    python .claude/transform_overview.py <file> [<file> ...]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

KST_NOW = "2026-04-19T09:11:51"


def transform(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text

    # Update frontmatter
    def _fm_update(m: re.Match) -> str:
        fm = m.group(1)
        fm = re.sub(
            r"(updated_at:\s*)\S+",
            lambda _m: f"{_m.group(1)}{KST_NOW}",
            fm,
        )
        fm = re.sub(r"(recent_editor:\s*)\S+", r"\1CLAUDE", fm)
        return f"---\n{fm}\n---"

    text = re.sub(r"---\n(.+?)\n---", _fm_update, text, count=1, flags=re.DOTALL)

    # 'Study Order' heading -> 'Concepts' (associative hub, no ordering implied)
    text = re.sub(r"^## Study Order\b.*$", "## Concepts", text, flags=re.MULTILINE)

    # Numbered list items at line start -> bullets
    # Only matches top-level numbered items ("1. ", "2. ", ...), not indented ones.
    text = re.sub(r"^(\d+)\. ", "- ", text, flags=re.MULTILINE)

    if text == original:
        return False

    path.write_text(text, encoding="utf-8")
    return True


if __name__ == "__main__":
    count = 0
    for arg in sys.argv[1:]:
        p = Path(arg)
        if p.is_file() and transform(p):
            print(f"transformed: {arg}")
            count += 1
    print(f"\n{count} file(s) transformed.")
