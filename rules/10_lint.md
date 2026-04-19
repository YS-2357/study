---
tags:
  - tooling
created_at: 2026-04-19T09:11:51
updated_at: 2026-04-19T09:11:51
recent_editor: CLAUDE
---

# Lint

Health check over the wiki. Runs on demand — not automatic.

## 1. Trigger

Run **only when the user asks**:

- `/lint` — slash command in `.claude/commands/lint.md`
- Conversational: "lint the repo", "check for issues"

## 2. Checks

Each check runs across all `.md` files, skipping `node_modules/`, `.git/`, and `raw/`.

### 2.1. Broken Links

Find any relative-path link whose target file does not exist.

```bash
grep -rEho '\[[^]]+\]\([^)]+\.md[^)]*\)' --include='*.md' .
```

Resolve each link relative to the file it appears in. Report misses.

### 2.2. Orphan Notes

Concept notes (`NN_*.md`) with zero inbound links from any other `.md` in the repo. These break the associative navigation model — add at least one inbound link from a related note or the domain overview.

### 2.3. Missing Cross-References

A concept is "missing a cross-ref" when:
- Its canonical note exists, **and**
- Another note mentions the concept by name in prose, **and**
- That mention is not a markdown link.

For the first-mention rule, see [03_cross_linking.md §2](03_cross_linking.md). Only the first mention per file needs a link.

### 2.4. Stale Claims

A note is potentially stale when:
- Its `updated_at` predates the latest `log.md` ingest that named the same concept, **and**
- The newer ingest touched other notes on the same concept.

The check uses `log.md` as the timeline of record. Report; do not auto-rewrite.

### 2.5. Contradictions

Contradictions are surfaced during ingest (§3.1 of [09_ingest.md](09_ingest.md)). Lint re-scans any note whose frontmatter has a `contradiction:` flag and reports pairs of claims that still disagree.

### 2.6. Missing `source:`

Concept notes without any `source:` frontmatter entry. Expected for notes that predate the ingest pipeline; flag so the user can attribute retroactively when they remember the source.

### 2.7. Footer Shape

Every concept note must end with:

```
---
↑ [Overview](./00_{domain}_overview.md)

**Related:** [A](./a.md), [B](../other/b.md)
**Tags:** #tag1 #tag2
```

Flag any note with the old `← Previous | [Overview] | Next →` format or a missing footer.

### 2.8. Frontmatter Validity

Each `.md` must have:
- A frontmatter block (`---` delimited)
- At least one `tag`
- `created_at`, `updated_at` in `YYYY-MM-DDTHH:MM:SS` form
- `recent_editor` in {`CLAUDE`, `CODEX`, `KIRO`, `HUMAN`}

## 3. Output

Print a short report grouped by check, with file paths and line numbers. Do not edit files without user approval.

Example:

```
lint report (2026-04-19T09:11:51)

broken links (2):
  aws/compute/03_lambda.md:42  → ../storage/99_missing.md
  ai/07_agent.md:18            → ../../networking/99_missing.md

orphan notes (1):
  computing/05_turing.md

missing cross-refs (3):
  aws/compute/04_fargate.md:88  "ECS" → aws/compute/02_ecs.md
  ...
```

## 4. Fixing Lint Findings

After the report:

1. Ask the user which findings to fix.
2. Fix approved items one at a time.
3. Append a `lint` entry to `log.md`:

   ```
   ## [2026-04-19T09:11:51] lint | 5 broken links, 1 orphan
   - Fixed: 5 broken links
   - Deferred: 1 orphan (computing/05_turing.md)
   ```

## 5. Frequency

No schedule. Run whenever the wiki feels drifty, after a batch of ingests, or before committing to a long research session.
