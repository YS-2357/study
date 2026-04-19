---
tags:
  - tooling
created_at: 2026-04-19T09:11:51
updated_at: 2026-04-19T09:11:51
recent_editor: CLAUDE
---

# Log

Append-only chronological record of ingest, query, and lint operations.

## Format

```
## [YYYY-MM-DDTHH:MM:SS] ingest|query|lint | <source-or-topic>
- note: what was touched
- note: what was decided
```

Newest entries at the bottom. Each entry starts with `## [` so the log is parseable with plain Unix tools:

```bash
grep "^## \[" log.md | tail -5        # last 5 entries
grep "^## \[.*ingest" log.md | wc -l  # total ingests
```

## Entries

## [2026-04-19T09:11:51] bootstrap | log.md created
- Established log format.
- Part of Karpathy LLM Wiki pattern adoption.

## [2026-04-19T09:11:51] bootstrap | Karpathy LLM Wiki pattern adopted
- Source: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Added: `/ingest` and `/lint` slash commands, `rules/09_ingest.md`, `rules/10_lint.md`, root `log.md`.
- Navigation: dropped prev/next chains; new footer is `↑ Overview` + `Related` list + `Tags` list.
- Numbering: `NN_` is now an identifier only, not a study-order rank.
- Frontmatter: added optional `source:` field for ingested sources.
- Repo sync: `raw/` is now gitignored (sources local-only); only `raw/README.md` tracked.
- Migration: 98 concept notes and 19 overviews rewritten in this session.
- Pre-push: updated `.codex/hooks/pre-push` footer check to accept the new multi-line footer shape.
