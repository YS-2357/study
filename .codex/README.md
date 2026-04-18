---
tags:
  - tooling
created_at: 2026-04-18T11:51:15
updated_at: 2026-04-18T19:41:34
recent_editor: CODEX
---

# .codex

Codex-specific repo automation and local helper files.

- `README.md`: This file.
- `AGENTS.md`: Codex-local scope rules.
- `hooks/`: Codex-owned hook implementations invoked by Git hook entrypoints.
- `mcp/`: Codex-owned repo-local MCP server dependencies and docs.

## Workflow

Codex follows the root repository rules through explicit actions, not automatic Claude-style write hooks:

- Inspect the relevant rules before Markdown note work.
- Make surgical edits and update Markdown frontmatter with `recent_editor: CODEX`.
- Run verification before Git writes.
- Stage, commit, and push with simple single-purpose Git commands.

`.codex/hooks/pre-push` is the Codex enforcement point for push-time validation.

`.codex/mcp/` stores repo-local MCP dependencies. The root `.mcp.json` is the client entrypoint and should point at local packages under `.codex/mcp/` when possible.

## Permissions

Codex usually does not need elevated permission for non-mutating inspection:

- `rg`
- `Get-Content`
- `git status`
- `git diff`
- `git log`

Safe recurring approvals for this repository:

- `git add <specific paths>` - stages intended file changes and writes Git index metadata.
- `git commit -m "<message>"` - creates the reviewed commit.
- `git restore <specific paths>` - cleans confirmed line-ending-only noise or restores specific files.
- Token-based push:

```bash
set -a && source .env && set +a && git -c credential.helper= -c "http.https://github.com/.extraheader=AUTHORIZATION: basic $(printf 'YS-2357:%s' "$GITHUB_TOKEN" | base64 -w0)" push origin main
```

Prefer plain `git push origin main` when the repo-local credential helper is configured. Use token-wrapped push commands only as a fallback when plain push cannot authenticate.

Keep these gated and do not approve them broadly:

- `git reset --hard`
- broad `git checkout -- .`
- broad `git restore .`
- `rm` or recursive delete commands
- arbitrary `python`, `powershell`, or shell scripts unrelated to the task

## Command Shape

Saved approvals match best when Codex runs one direct command at a time:

1. `git status --short`
2. `git add <specific paths>`
3. `git commit -m "<message>"`
4. `git push origin main`
5. `git pull --ff-only origin main`
6. `gh auth status`, `gh pr view`, `gh pr list`, `gh issue view`, or `gh issue list`

Avoid PowerShell wrapper scripts, chained commands, pipes, heredocs, command substitutions, and inline environment setup unless they are truly required. Those forms are treated as different command shapes and may bypass the saved prefix rules.

Claude permissions in `.claude/settings.local.json` do not grant Codex permissions. Codex approvals are matched by the harness against the actual command shape, so direct standalone `git` and `gh` commands are the most reliable way to reuse saved approvals.
