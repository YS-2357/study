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

## Git And GitHub CLI Command Style

To make Codex auto-approval rules match reliably, run Git and GitHub CLI commands as simple, single-purpose commands:

1. Run `git status --short` by itself before staging or committing.
2. Run `git add <specific paths>` by itself. Do not use `git add .` unless the user explicitly asks to stage everything.
3. Run `git commit -m "<message>"` by itself with a clear message.
4. Run `git push origin main` by itself after a successful commit.
5. Run `git pull --ff-only origin main` by itself when updating from remote.
6. Run read-only GitHub CLI checks such as `gh auth status`, `gh pr view`, `gh pr list`, `gh issue view`, or `gh issue list` as standalone commands.

Do not wrap these commands in PowerShell scripts, environment-variable setup blocks, command chains, pipes, heredocs, or command substitutions unless the task specifically requires that shape. Complex wrappers are less likely to match saved approval prefixes and will usually prompt again.
