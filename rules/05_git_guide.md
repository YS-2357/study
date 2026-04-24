---
tags:
  - git
  - tooling
created_at: 2026-04-17T00:00:00
updated_at: 2026-04-24T08:47:57
recent_editor: CODEX
---

# Git Guide

Git workflow and push commands for this repository.

The repo is designed for multi-PC sync: notes, rules, hooks, and agent configs are tracked and pushed, while local secrets and volatile UI state stay out of Git, including `.env`, `raw/`, and `.obsidian/workspace.json`.

## 1. Environment Setup

Required variables in `.env`:

| Variable | Purpose |
|----------|---------|
| `GITHUB_TOKEN` | Personal access token for authentication |
| `GITHUB_USERNAME` | GitHub account name |
| `GIT_USER_NAME` | Commit author name |
| `GIT_USER_EMAIL` | Commit author email |

Example:

```text
GITHUB_TOKEN=github_pat_...
GITHUB_USERNAME=your-username
GIT_USER_NAME=Your Name
GIT_USER_EMAIL=your@email.com
```

## 2. Push Commands

### 2.1. Standard Push

Uses `.githooks/git-credential-env.sh`:

```bash
git push origin main
```

### 2.2. Direct Token Authentication

For scripts or when the credential helper is unavailable:

```bash
set -a && source .env && set +a && git -c credential.helper= \
  -c "http.https://github.com/.extraheader=AUTHORIZATION: basic $(printf '%s:%s' "$GITHUB_USERNAME" "$GITHUB_TOKEN" | base64 -w0)" \
  push origin main
```

### 2.3. With Content Acknowledgment

For study content changes:

```bash
STUDY_PUSH_CONTENT_ACK=1 git push origin main
```

## 3. Environment Variables

| Variable | Purpose |
|----------|---------|
| `GITHUB_TOKEN` | Authentication token |
| `GITHUB_USERNAME` | GitHub account name |
| `STUDY_PUSH_CONTENT_ACK=1` | Skip content acknowledgment prompt |
| `CLAUDE_AUTO_PUSH=1` | Set by Claude auto-push hooks |
| `STUDY_ALLOW_MULTI_COMMIT_PUSH=1` | Compatibility override for hooks that still check multi-commit pushes |

## 4. Git Identity Setup

If Git identity is missing:

```bash
set -a && source .env && set +a
git config --local user.name "$GIT_USER_NAME"
git config --local user.email "$GIT_USER_EMAIL"
```

## 5. Commit Style

### 5.1. Message Format

```text
<type>: <description>

<optional body>
```

Types:
- `add` - New file or feature
- `update` - Changes to existing content
- `fix` - Bug fix or correction
- `refactor` - Restructuring without changing behavior
- `docs` - Documentation only

## 6. Example Workflow

```bash
# Inspect current state
git status --short
git diff

# Stage and commit the intended task
git add file.md
git commit -m "update: improve Lambda section"

# Push only when the task calls for remote delivery
STUDY_PUSH_CONTENT_ACK=1 git push origin main
```

Typical workflow:

1. Inspect the current state with `git status` and `git diff`.
2. Pull before mutation when the branch may be stale or the task depends on current remote content.
3. Stage only the intended paths.
4. Create one or more commits that represent one coherent task.
5. Push only when the user asks for it or the task explicitly includes remote delivery.

## 7. Hooks

| Location | Purpose |
|----------|---------|
| `.githooks/pre-push` | Main dispatcher |
| `.githooks/pre-push-study-content` | Content acknowledgment |
| `.githooks/git-credential-env.sh` | Credential helper |
| `.codex/hooks/pre-push` | Codex validation (frontmatter, structure, footer, security) |
