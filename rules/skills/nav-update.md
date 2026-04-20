# nav-update

Sync structural documents after adding, moving, renaming, or deleting notes.

**Argument:** `<brief description of what changed>`

Run the structural-document update flow defined in [rules/AGENTS.md §9](../AGENTS.md) and [rules/02_navigation.md §7](../02_navigation.md).

Trigger: any file was added, moved, renamed, or deleted. The argument should describe what changed (e.g., "added cloud/aws/compute/05_ecs.md").

Steps:

1. Identify the affected domain(s) from the argument or by asking the user if unclear.
2. Update `00_{domain}_overview.md` in the affected domain:
   - Add/remove the note entry.
   - If a subdomain was created, add a subdomain entry instead.
3. Update `README.md` in the affected folder(s) to reflect the current file list.
4. If the domain layout changed (new domain, new subdomain, removed domain), update the table in `rules/02_navigation.md §6`.
5. For renames: run the sed pattern from [rules/07_scalability.md §8](../07_scalability.md) to fix all cross-references repo-wide.
6. For deletions: remove the note from every `Related` list that referenced it; repair or remove inline cross-links.
7. For additions: add an entry to the `Related` list of any existing note whose topic connects; ensure at least one inbound link exists so the new note is not an orphan.
8. Update `updated_at` and `recent_editor` in the frontmatter of every touched file.
9. Append one entry to `log.md`:
   ```
   ## [TIMESTAMP] nav-update | <what changed>
   - Touched: <list of files>
   ```

Do not touch notes outside the structural scope confirmed above.
