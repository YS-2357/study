# .codex

Codex-specific repo automation and local helper files.

- `README.md`: This file.
- `AGENTS.md`: Codex-local scope rules.
- `hooks/`: Codex-owned hook implementations invoked by Git hook entrypoints.

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

Keep these gated and do not approve them broadly:

- `git reset --hard`
- broad `git checkout -- .`
- broad `git restore .`
- `rm` or recursive delete commands
- arbitrary `python`, `powershell`, or shell scripts unrelated to the task
