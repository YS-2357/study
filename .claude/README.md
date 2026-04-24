---
tags:
  - tooling
created_at: 2026-04-17T14:51:28
updated_at: 2026-04-24T00:24:20
recent_editor: CLAUDE
---

# .claude

Claude Code automation for this repository.

- `settings.json`: hook configuration for edit-time metadata normalization on Write/Edit/MultiEdit.
- `settings.local.json`: personal permission overrides. This file is local and should not be committed unless explicitly requested.
- `hooks/`: Claude-owned hook scripts invoked by `settings.json`.

## Permissions

Claude usually does not need elevated permission for non-mutating inspection:

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
set -a && source .env && set +a && git -c credential.helper= -c "http.https://github.com/.extraheader=AUTHORIZATION: basic $(printf '%s:%s' "$GITHUB_USERNAME" "$GITHUB_TOKEN" | base64 -w0)" push origin main
```

Keep these gated and do not approve them broadly:

- `git reset --hard`
- broad `git checkout -- .`
- broad `git restore .`
- `rm` or recursive delete commands
- arbitrary `python`, `powershell`, or shell scripts unrelated to the task
