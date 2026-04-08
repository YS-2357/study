# Codex Scope

These instructions apply to the `.codex/` subtree.

- Codex owns `.codex/` and shared Git hook entrypoints under `.githooks/`.
- `.claude/` and `CLAUDE.md` are out of scope for Codex. Do not inspect, edit, move, organize, or validate Claude-owned files from Codex-managed workflows.
- If a Codex-managed push includes `.claude/` or `CLAUDE.md` changes, fail loudly and stop the push.
- Exception: when `CLAUDE_AUTO_PUSH=1`, treat the push as Claude-owned and do not block `.claude/` or `CLAUDE.md` changes from the Codex pre-push guard.
