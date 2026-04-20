---
description: Split an oversized or mixed-theme note into two focused notes
argument-hint: <note-path>
---

Run the note-split workflow defined in [rules/07_scalability.md §3/§8](../../rules/07_scalability.md) and [rules/09_ingest.md §3.3](../../rules/09_ingest.md).

Split when the target note (`$ARGUMENTS`):
- Would exceed ~150 lines of body content after an update, **or**
- Mixes ≥2 distinct themes where intra-theme links outnumber inter-theme links.

Steps:

1. Read the note and propose a split boundary: where to cut and what each new file will be named. Confirm with the user before proceeding.
2. Create the two new files:
   - Assign `NN_` prefixes that fit the existing numbering in the subdomain.
   - Copy the relevant sections; do not duplicate content.
   - Add full frontmatter (`tags`, `created_at`, `updated_at`, `recent_editor`).
   - Add nav header (`↑ [Overview](./00_*_overview.md)`) and footer (`↑ Overview`, `Related`, `Tags`).
3. Delete (or `git mv`) the original file.
4. Run the sed rename pattern from [rules/07_scalability.md §8](../../rules/07_scalability.md) for each old filename replaced:
   ```bash
   find . -name "*.md" -not -path "./.git/*" -print0 \
     | xargs -0 sed -i 's|OLD_PATH|NEW_PATH|g'
   ```
5. Update the parent overview (`00_{domain}_overview.md`) and `README.md`:
   - Remove the old entry; add the two new entries.
6. Update `Related` lists in other notes: replace any link to the old file with links to whichever new file(s) apply.
7. Update `updated_at` and `recent_editor` on every touched file.
8. Append one entry to `log.md`:
   ```
   ## [TIMESTAMP] split | <old-note> → <new-note-a>, <new-note-b>
   - Reason: <line-count or mixed-themes>
   - Touched: <list of files>
   ```

Do not add new content during a split — only redistribute existing content.
