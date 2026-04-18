---
tags:
  - git
  - tooling
created_at: 2026-04-17T00:00:00
updated_at: 2026-04-18T12:05:11
recent_editor: CLAUDE
---

# Git Guide

Git workflow and push commands for this repository.

## 1. Environment Setup

Required variables in `.env`:

| Variable | Purpose |
|----------|---------|
| `GITHUB_TOKEN` | Personal access token for authentication |
| `GITHUB_USERNAME` | GitHub account name |
| `GIT_USER_NAME` | Commit author name |
| `GIT_USER_EMAIL` | Commit author email |

Example `.env`:

```
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

For scripts or when credential helper is unavailable:

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
| `STUDY_ALLOW_MULTI_COMMIT_PUSH=1` | Allow multiple commits in one push |

## 4. Git Identity Setup

If git identity is missing:

```bash
set -a && source .env && set +a
git config --local user.name "$GIT_USER_NAME"
git config --local user.email "$GIT_USER_EMAIL"
```

## 5. Commit Style

### 5.1. Message Format

```
<type>: <description>

<optional body>
```

Types:
- `add` - New file or feature
- `update` - Changes to existing content
- `fix` - Bug fix or correction
- `refactor` - Restructuring without changing behavior
- `docs` - Documentation only
- `auto` - Automated commits from hooks

### 5.2. Auto-Commit Messages

Claude auto-push generates one commit per Write/Edit, so single-file is the norm:
- `auto: update <file>` — normal PostToolUse commit (one tool call, one file)
- `auto: update <file> and N more` — only on Stop-event cleanup when several files were left unstaged

## 6. Auto-Push Staging Behavior

`.claude/hooks/auto-push.sh` reads the PostToolUse JSON from stdin and stages only the file the agent just touched, instead of `git add -A`:

```
┌─ PostToolUse (Write|Edit) ─────────────────┐
│  stdin JSON → jq .tool_input.file_path     │
│  git add -A -- "$file_path"                │
│  → one commit, one file                    │
└────────────────────────────────────────────┘

┌─ Stop (session end) ───────────────────────┐
│  no file_path in stdin                     │
│  git add -A       (sweep any leftovers)    │
│  → may produce "and N more"                │
└────────────────────────────────────────────┘
```

**Why per-file staging:** when several agents edit simultaneously, a blanket `git add -A` would fold in another agent's in-progress files, causing cross-agent commits and race conditions on push. Per-file staging keeps each agent's commits scoped to its own work.

## 6. Example Workflow

```bash
# Load environment
set -a && source .env && set +a

# Make changes
# ... edit files ...

# Stage and commit
git add file.md
git commit -m "update: improve Lambda section"

# Push with acknowledgment
STUDY_PUSH_CONTENT_ACK=1 git push origin main
```

## 7. Hooks

| Location | Purpose |
|----------|---------|
| `.githooks/pre-push` | Main dispatcher |
| `.githooks/pre-push-study-content` | Content acknowledgment |
| `.githooks/git-credential-env.sh` | Credential helper |
| `.claude/hooks/auto-push.sh` | Claude auto-push |
| `.codex/hooks/pre-push` | Codex validation |
