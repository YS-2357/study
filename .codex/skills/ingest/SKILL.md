---
name: ingest
description: Ingest raw source files into the study repo wiki. Use when Codex needs to process a file from raw/, summarize the scope, update or create focused notes, add source frontmatter, move the source to raw/processed/, and append log.md.
---

# Ingest

Use the canonical workflow in `rules/skills/ingest.md` and the full procedure in `rules/09_ingest.md`.

Before writing:

- Run `git pull --ff-only origin main`.
- Locate the raw source under `raw/`.
- Read enough of the source to identify scope.
- Summarize the intended note changes to the user in 2-4 bullets and confirm scope.

While writing:

- Search existing notes first and prefer updating over creating.
- Create or split notes only when the canonical rules require it.
- Add the raw source slug to every touched note's `source:` frontmatter.
- Update `updated_at` and `recent_editor: CODEX` on every Markdown file Codex edits.
- Move the raw source to `raw/processed/`.
- Append one concise ingest entry to `log.md`.

Do not touch unrelated notes, do not commit raw source content, and do not modify `.claude/`.
