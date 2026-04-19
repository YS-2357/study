"""Dedup Related: list links where the same target file appears more than once.

Normalizes paths (strips leading './') before comparing, keeps the FIRST
occurrence's link text.

Usage:
    python .claude/dedup_related.py <file> [<file> ...]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def normalize(p: str) -> str:
    p = p.strip()
    if p.startswith("./"):
        p = p[2:]
    return p


def dedup_line(line: str) -> tuple[str, bool]:
    """Return (possibly rewritten line, changed?)."""
    m = re.match(r"(\*\*Related:\*\*\s*)(.*)", line)
    if not m:
        return line, False
    prefix, rest = m.group(1), m.group(2)

    links = LINK_RE.findall(rest)
    seen_norm: set[str] = set()
    kept: list[tuple[str, str]] = []
    for title, target in links:
        key = normalize(target)
        if key in seen_norm:
            continue
        seen_norm.add(key)
        kept.append((title, target))

    if len(kept) == len(links):
        return line, False
    new_rest = ", ".join(f"[{t}]({p})" for t, p in kept)
    return prefix + new_rest, True


def process(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    new_lines = []
    changed = False
    for line in text.split("\n"):
        out, was_changed = dedup_line(line)
        if was_changed:
            changed = True
        new_lines.append(out)
    if not changed:
        return False
    path.write_text("\n".join(new_lines), encoding="utf-8")
    return True


if __name__ == "__main__":
    count = 0
    for arg in sys.argv[1:]:
        p = Path(arg)
        if p.is_file() and process(p):
            print(f"deduped: {arg}")
            count += 1
    print(f"\n{count} file(s) changed.")
