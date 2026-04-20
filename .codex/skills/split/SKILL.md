---
name: split
description: Split oversized or mixed-theme study notes into focused notes. Use when Codex needs to propose a split boundary, redistribute existing content, update navigation, repair links, and log the split without adding new content.
---

# Split

Use the canonical workflow in `rules/skills/split.md`, plus `rules/07_scalability.md` and `rules/09_ingest.md`.

Before writing:

- Run `git pull --ff-only origin main`.
- Read the target note and confirm it is oversized or mixes distinct themes.
- Propose the split boundary and new filenames to the user.
- Wait for approval before changing files.

After approval:

- Redistribute existing content only; do not add new subject content.
- Give new notes valid frontmatter, navigation, related links, and tags.
- Replace or remove the old note according to the approved split.
- Repair repo-wide links and affected `Related` lists.
- Update parent overview and README files.
- Update `updated_at` and `recent_editor: CODEX` on every Markdown file Codex edits.
- Append one `split` entry to `log.md`.

Do not modify `.claude/`.
