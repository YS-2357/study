# .claude/hooks

Claude Code hook scripts for this repository.

- `auto-push.sh` — stages all changes, commits, and pushes to origin/main. Runs after every Write/Edit and at session end. Sets `CLAUDE_AUTO_PUSH=1` so the interactive review is skipped. Silent on success; surfaces a system message on failure.
- `pre-push` — interactive study content review for manual user pushes. Lists study files being pushed and asks for confirmation. Automatically skipped when `CLAUDE_AUTO_PUSH=1`.
