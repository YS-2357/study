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
- `gh auth status`
- `gh pr view`
- `gh pr list`
- `gh issue view`
- `gh issue list`

Safe recurring approvals for this repository:

- `git add <specific paths>` - stages intended file changes and writes Git index metadata.
- `git status` - checks repository state without changing files.
- `git commit -m "<message>"` - creates the reviewed commit.
- `git push origin main` - pushes the reviewed single commit to the repository.
- `git pull --ff-only origin main` - updates the local branch only when Git can fast-forward without creating a merge commit.
- `git restore <specific paths>` - cleans confirmed line-ending-only noise or restores specific files.
- `gh pr view <number-or-url>` - reads pull request metadata without changing GitHub state.
- `gh pr list <filters>` - lists pull requests for inspection.
- `gh issue view <number-or-url>` - reads issue metadata without changing GitHub state.
- `gh issue list <filters>` - lists issues for inspection.
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
