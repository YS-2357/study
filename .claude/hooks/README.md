# .claude/hooks

Claude Code hook scripts for this repository.

- `normalize-timestamp.sh` — updates `updated_at` (KST) and `recent_editor: CLAUDE` in the first frontmatter block of any Markdown file touched by a Write/Edit/MultiEdit tool call. No Git operations.
- `pre-push` — manual push guard: presents a multiple-choice quiz drawn from the study notes being pushed. Runs only in interactive terminals; non-interactive callers pass through silently.
