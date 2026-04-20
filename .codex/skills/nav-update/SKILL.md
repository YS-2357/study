---
name: nav-update
description: Sync study repo navigation after adding, moving, renaming, or deleting notes. Use when Codex changes note structure and must update overview files, README indexes, cross-links, inbound links, related lists, frontmatter timestamps, and log.md.
---

# Nav Update

Use the canonical workflow in `rules/skills/nav-update.md`, plus `rules/AGENTS.md` and `rules/02_navigation.md`.

When a note is added, moved, renamed, or deleted:

- Run `git pull --ff-only origin main`.
- Identify the affected domain and folder indexes.
- Update the relevant `00_*_overview.md` and `README.md` files.
- Repair cross-links and `Related` lists for renames or deletions.
- Ensure added notes have at least one inbound link.
- Update `updated_at` and `recent_editor: CODEX` on every Markdown file Codex edits.
- Append one `nav-update` entry to `log.md`.

Keep changes limited to the structural scope and do not modify `.claude/`.
