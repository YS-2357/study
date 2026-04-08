# .codex

Codex-specific repo automation and local helper files.

- Codex must not touch `.claude/` or `CLAUDE.md`. Claude-owned files are out of scope for Codex-managed workflows.
- `README.md`: This file.
- `AGENTS.md`: Codex-local scope rules.
- `hooks/`: Codex-owned hook implementations invoked by Git hook entrypoints.
