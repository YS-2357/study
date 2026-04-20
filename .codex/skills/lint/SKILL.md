---
name: lint
description: Run the study wiki health check and report findings. Use when Codex needs to inspect Markdown notes for broken links, orphan notes, missing cross-references, stale claims, contradictions, missing source fields, footer shape problems, or frontmatter validity.
---

# Lint

Use the canonical workflow in `rules/skills/lint.md` and the full suite in `rules/10_lint.md`.

Inspection flow:

- Run `git pull --ff-only origin main`.
- Check Markdown wiki files while skipping `node_modules/`, `.git/`, `raw/`, and `raw/processed/`.
- Report findings grouped by check with file paths and line numbers.
- Do not fix anything until the user approves the specific fixes.

Fix flow after approval:

- Apply fixes one file at a time.
- Update `updated_at` and `recent_editor: CODEX` on every Markdown file Codex edits.
- Append one `lint` entry to `log.md` summarizing fixed and deferred items.

Keep the report short and do not modify `.claude/`.
