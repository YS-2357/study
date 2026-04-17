# Codex Scope

These instructions apply to the `.codex/` subtree.

- Codex keeps its repo-local automation in `.codex/`.
- Shared Git hook entrypoints still live under `.githooks/`.

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
