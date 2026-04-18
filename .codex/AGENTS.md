---
tags:
  - tooling
created_at: 2026-04-18T11:51:15
updated_at: 2026-04-18T19:41:34
recent_editor: CODEX
---

# Codex Scope

These instructions apply to the `.codex/` subtree.

- Codex keeps its repo-local automation in `.codex/`.
- Codex keeps repo-local MCP server dependencies in `.codex/mcp/`.
- Shared Git hook entrypoints still live under `.githooks/`.
- Codex does not use Claude-style repo-local auto-push hooks unless the Codex harness explicitly supports them.
- Keep `.claude/` out of scope unless the user explicitly asks for Claude-specific changes.

## Repository Rules

Before creating or editing Markdown study content, Codex must read the applicable rules:

- Root `AGENTS.md`
- `rules/AGENTS.md`
- Relevant rule files under `rules/`
- Any subtree override, such as `aws/AGENTS.md`

For Markdown note edits, use the `karpathy-guidelines` skill when available. Keep the scope concrete before editing: name the files, preserve existing style, and avoid nearby cleanup that the user did not request.

## Markdown Edits

On every Markdown edit Codex makes:

- Set `updated_at` to the current local timestamp.
- Set `recent_editor: CODEX`.
- Preserve valid frontmatter, heading order, and navigation footers.
- Update related README, overview, and navigation files when adding, moving, renaming, or deleting notes.
- Do not touch `.claude/` files as part of routine Codex compliance work.

## Permission Requests

Codex should ask for persistent approval only for recurring, bounded Git actions:

- `git add <specific paths>`
- `git commit -m "<message>"`
- `git restore <specific paths>`
- the repository token-based `git push origin main` command from `.codex/README.md`

Codex should not request broad persistent approval for destructive or overly general commands:

- `git reset --hard`
- broad `git checkout -- .`
- broad `git restore .`
- `rm` or recursive delete commands
- arbitrary `python`, `powershell`, or shell scripts unrelated to the task

Non-mutating inspection such as `rg`, `Get-Content`, `git status`, `git diff`, and `git log` normally does not need elevated permission.

Claude permissions in `.claude/settings.local.json` do not apply to Codex. Codex approval reuse depends on the exact command shape sent to the harness.

## Git And GitHub CLI Command Style

To make Codex auto-approval rules match reliably, run Git and GitHub CLI commands as simple, single-purpose commands:

1. Run `git status --short` by itself before staging or committing.
2. Run `git add <specific paths>` by itself. Do not use `git add .` unless the user explicitly asks to stage everything.
3. Run `git commit -m "<message>"` by itself with a clear message.
4. Run `git push origin main` by itself after a successful commit.
5. Run `git pull --ff-only origin main` by itself when updating from remote.
6. Run read-only GitHub CLI checks such as `gh auth status`, `gh pr view`, `gh pr list`, `gh issue view`, or `gh issue list` as standalone commands.

Do not wrap these commands in PowerShell scripts, environment-variable setup blocks, command chains, pipes, heredocs, or command substitutions unless the task specifically requires that shape. Complex wrappers are less likely to match saved approval prefixes and will usually prompt again.

Prefer plain `git push origin main` after configuring the repo-local credential helper. Use token-wrapped push commands only when plain push cannot authenticate.

Run Git commands that write repository metadata with escalated permissions immediately instead of first trying them in the sandbox. This applies to `git add`, `git commit`, `git push`, `git pull`, and `git restore`; otherwise Windows may fail on `.git/index.lock` before Codex retries with approval. Use a broad bounded `prefix_rule` such as `["git", "commit", "-m"]`, not a full commit-message-specific prefix.
