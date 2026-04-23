---
tags:
  - tooling
created_at: 2026-04-23T23:41:19
updated_at: 2026-04-23T23:41:19
recent_editor: CODEX
---

# lint

Run the wiki health check and report findings.

Follow the full suite defined in [rules/10_lint.md](../10_lint.md):

1. **Broken links** — relative-path markdown links whose target file does not exist.
2. **Orphan notes** — concept notes (`NN_*.md`) with zero inbound links.
3. **Missing cross-references** — concepts whose canonical note exists but are mentioned in prose without a link on first mention.
4. **Stale claims** — notes whose `updated_at` predates later `log.md` ingests that touched the same concept.
5. **Contradictions** — notes with a `contradiction:` frontmatter flag that still show disagreement.
6. **Missing `source:`** — concept notes without any `source:` entry.
7. **Footer shape** — notes still carrying the legacy `← Previous | ... | Next →` format.
8. **Frontmatter validity** — missing tags/dates/`recent_editor`.

Rules:

- Skip `node_modules/`, `.git/`, `raw/`, and `raw/processed/`.
- Do not fix anything without asking the user first.
- Print a short grouped report with file paths and line numbers.
- After user approves fixes, apply them one file at a time and append a single `lint` entry to `log.md` summarizing what was fixed and what was deferred.
