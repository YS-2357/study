"""Migrate concept-note footers from prev/next format to associative format.

Usage:
    python .claude/migrate_footer.py <file> [<file> ...]

For each file:
- Updates frontmatter updated_at and recent_editor.
- Replaces old `← Previous: | [Overview] | Next →` footer with:
    ↑ [Overview](...)
    **Related:** [A](...), [B](...)
    **Tags:** #tag1 #tag2
- Related derives from prev/next targets + inline body links (minus overviews/readmes).
- Tags mirror frontmatter tags.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

KST_NOW = "2026-04-19T09:11:51"

OV_LINK_RE = re.compile(r"\[Overview\]\(([^)]+)\)")
PREV_RE = re.compile(r"Previous:\s*\[([^\]]+)\]\(([^)]+)\)")
NEXT_RE = re.compile(r"Next:\s*\[([^\]]+)\]\(([^)]+)\)")
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+\.md)\)")


def migrate(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")

    # --- frontmatter: bump updated_at, set recent_editor ---
    def _fm_update(m: re.Match) -> str:
        fm = m.group(1)
        fm = re.sub(r"(updated_at:\s*)\S+", lambda _m: f"{_m.group(1)}{KST_NOW}", fm)
        fm = re.sub(r"(recent_editor:\s*)\S+", r"\1CLAUDE", fm)
        return f"---\n{fm}\n---"

    text, n = re.subn(r"---\n(.+?)\n---", _fm_update, text, count=1, flags=re.DOTALL)
    if n == 0:
        print(f"skipped {path}: no frontmatter", file=sys.stderr)
        return False

    # --- extract tags ---
    fm_match = re.match(r"---\n(.+?)\n---", text, re.DOTALL)
    fm = fm_match.group(1)
    tag_block = re.search(r"tags:\s*\n((?:\s+-.*\n)+)", fm)
    tags = re.findall(r"-\s*(\S+)", tag_block.group(1)) if tag_block else []

    # --- find footer divider (last standalone `---` line) ---
    lines = text.split("\n")
    sep_indices = [i for i, l in enumerate(lines) if l == "---"]
    if len(sep_indices) < 3:
        print(f"skipped {path}: no footer divider", file=sys.stderr)
        return False
    last_sep = sep_indices[-1]

    footer_text = "\n".join(lines[last_sep + 1 :]).strip()

    ov = OV_LINK_RE.search(footer_text)
    if not ov:
        print(f"skipped {path}: no Overview link in footer", file=sys.stderr)
        return False
    overview_path = ov.group(1)

    # --- related: prev/next + inline body links ---
    related: list[tuple[str, str]] = []
    seen_paths: set[str] = set()

    def _add(title: str, p: str) -> None:
        if p in seen_paths:
            return
        seen_paths.add(p)
        related.append((title, p))

    prev = PREV_RE.search(footer_text)
    if prev:
        _add(prev.group(1), prev.group(2))
    nxt = NEXT_RE.search(footer_text)
    if nxt:
        _add(nxt.group(1), nxt.group(2))

    body_text = "\n".join(lines[:last_sep])
    for title, lpath in MD_LINK_RE.findall(body_text):
        base = lpath.rsplit("/", 1)[-1]
        if "_overview" in base or base in {"README.md", "home.md", "glossary.md"}:
            continue
        if lpath.startswith("http"):
            continue
        _add(title, lpath)

    # --- build new footer ---
    if related:
        related_line = "**Related:** " + ", ".join(
            f"[{t}]({p})" for t, p in related
        )
    else:
        related_line = "**Related:** _(none yet)_"

    if tags:
        tags_line = "**Tags:** " + " ".join(f"#{t}" for t in tags)
    else:
        tags_line = "**Tags:**"

    new_footer_lines = [
        "---",
        f"↑ [Overview]({overview_path})",
        "",
        related_line,
        tags_line,
    ]

    new_lines = lines[:last_sep] + new_footer_lines
    new_text = "\n".join(new_lines).rstrip() + "\n"

    path.write_text(new_text, encoding="utf-8")
    return True


if __name__ == "__main__":
    count = 0
    for arg in sys.argv[1:]:
        p = Path(arg)
        if p.is_file() and migrate(p):
            print(f"migrated: {arg}")
            count += 1
    print(f"\n{count} file(s) migrated.")
