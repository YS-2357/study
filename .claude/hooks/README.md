# .claude/hooks

Claude Code hook scripts for this repository.

- `auto-push.sh` — stages all changes, commits, and pushes to origin/main. Runs after every Write/Edit and at session end. Sets `CLAUDE_AUTO_PUSH=1` so the interactive review is skipped. Silent on success; surfaces a system message on failure.
- `pre-push` — placeholder for Claude-only push checks. Shared study-content review now lives in `.githooks/pre-push-study-content`.
