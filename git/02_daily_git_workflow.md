---
tags:
  - git
created_at: 2026-04-03T00:00:00
updated_at: 2026-04-18T13:00:00
recent_editor: CLAUDE
---

↑ [Overview](./00_git_overview.md)

# Daily Git Workflow

## What It Is

A daily Git workflow is the repeatable command sequence you use to check what changed, review the edits, save them as a commit, and push that commit to GitHub.

## How It Works

### Commands You Use Most Often

| Command | What it does | When to use |
|---------|--------------|-------------|
| `git status` | Shows changed, staged, and untracked files | First command before and after edits |
| `git status --short` | Shows the same state in compact form | When you want a quick summary |
| `git diff` | Shows unstaged content changes | Before staging, to review what you edited |
| `git diff --staged` | Shows all staged content changes | Before committing, to verify what will be saved |
| `git diff --staged -- <file>` | Shows staged changes for one file only | When you want to inspect one staged file |
| `git add <file>` | Stages one file | When you want to include a specific file in the next commit |
| `git add -A` | Stages all changes, including deletes and renames | When you intentionally want all current repo changes in the next commit |
| `git commit -m "message"` | Creates a commit from staged changes | When the staged changes form one meaningful unit |
| `git log --oneline -n 10` | Shows the latest 10 commits compactly | When you want to confirm recent history |
| `git push` | Uploads local commits to the remote branch | After committing, when you want GitHub to receive your changes |

### Safe One-By-One Routine

1. Run `git status`.
2. Run `git diff` and read the changes.
3. Stage only the files you intend to save with `git add <file>` or `git add -A`.
4. Run `git diff --staged`, or `git diff --staged -- <file>` for one file.
5. Commit with `git commit -m "short summary"`.
6. Confirm with `git log --oneline -n 10`.
7. Push with `git push` when the commit is ready to upload.

### How This Connects to VS Code

Use [WSL Terminal and VS Code Workflow](../tooling/01_wsl_terminal_and_vscode.md) to open the repo with `code .`, edit files in VS Code, then return to WSL and run the Git commands above. The terminal commands and the VS Code file tree are acting on the same repo folder.

### Push with `GITHUB_TOKEN` from `.env`

If `git push` cannot authenticate, this repo keeps a token-based push pattern in `.env.example`.

```bash
set -a && source .env && set +a && git -c credential.helper= -c "http.https://github.com/.extraheader=AUTHORIZATION: basic $(printf 'YS-2357:%s' "$GITHUB_TOKEN" | base64 -w0)" push origin main
```

What that means:

| Part | Meaning |
|------|---------|
| `set -a` | Automatically export variables loaded from `.env` |
| `source .env` | Load `GITHUB_TOKEN` from the local `.env` file |
| `set +a` | Stop auto-exporting variables |
| `git -c credential.helper=` | Ignore any broken local Git credential helper for this one command |
| `http.https://github.com/.extraheader=...` | Attach an Authorization header built from `YS-2357` and `$GITHUB_TOKEN` |
| `push origin main` | Push local `main` to the `origin` remote |

## Example

After editing a Markdown note in VS Code:

```bash
cd /home/ys2357/study
git status
git diff
git add git/02_daily_git_workflow.md git/00_git_overview.md git/README.md
git diff --staged -- git/README.md
git commit -m "Add daily Git workflow note"
git log --oneline -n 5
```

If you are ready to upload that commit:

```bash
git push
```

If normal `git push` fails because GitHub auth is broken, use the `.env` token push command from above instead.

## Why It Matters

This routine prevents the two most common Git mistakes: committing files you did not mean to include, and pushing without reviewing what changed. Once this sequence becomes automatic, Git becomes a safe checkpoint system instead of something you only use at the end.

> **Tip:** If `git status` shows files you did not expect, stop and inspect them before running `git add -A`.
> **Tip:** `git add <file>` usually prints nothing when it succeeds. No output is normal; run `git status` or `git diff --staged` to verify the file is staged.
> **Tip:** Never commit the real `.env` file. Keep only `.env.example` in Git.

---
← Previous: [Tracking and Status](01_tracking_and_status.md) | [Overview](./00_overview.md)
