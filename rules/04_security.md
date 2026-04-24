---
tags:
  - security
  - tooling
created_at: 2026-04-17T00:00:00
updated_at: 2026-04-24T08:47:57
recent_editor: CODEX
---

# Security Rules

Security hooks and delivery rules for this repository.

## 1. Delivery Loop

**"Success should be explicit, failure must be loud"**

On success:
- Give a short explicit summary of what changed and what was verified
- Commit and push only when the task explicitly includes remote delivery

On failure:
- Explicit error message with context
- Log to system message
- Stop and fix before proceeding

After any file create/edit/rename/move/delete:
1. Update relevant docs (domain `00_{domain}_overview.md`, `home.md`, `README.md`, navigation) when structure changed
2. Verify Markdown structure and navigation rules
3. Check for security issues
4. Commit if the task calls for it
5. Push only when requested or when the task explicitly includes remote delivery

## 2. Security Checks

### 2.1. Before Every Push

Scan for these patterns:

| Pattern | Regex | Example |
|---------|-------|---------|
| Private keys | `-----BEGIN.*PRIVATE KEY-----` | RSA, EC, DSA keys |
| GitHub tokens | `ghp_[A-Za-z0-9]{36}` | `ghp_xxxx...` |
| GitHub OAuth | `gho_[A-Za-z0-9]{36}` | `gho_xxxx...` |
| OpenAI keys | `sk-[A-Za-z0-9]{48}` | `sk-xxxx...` |
| AWS access keys | `AKIA[A-Z0-9]{16}` | `AKIAIOSFODNN7EXAMPLE` |
| Slack tokens | `xox[baprs]-[A-Za-z0-9-]+` | `xoxb-xxxx...` |
| `.env` files | `\.env$` | Environment secrets |
| `.pem` files | `\.pem$` | Certificate keys |

### 2.2. Files to Never Commit

- `.env`
- `*.pem`
- `credentials.json`
- Any file with `secret`, `token`, or `password` in the name

### 2.3. If Security Issue Found

1. Stop immediately
2. Do not commit or push
3. Remove the sensitive content
4. Then continue with the task

## 3. Hook Architecture

### 3.1. Entrypoints

```text
.githooks/
  pre-push                # Main dispatcher
  pre-push-study-content  # Content acknowledgment
  git-credential-env.sh   # Credential helper
```

### 3.2. Agent-Specific Hooks

```text
.claude/hooks/    # Claude Code hooks
.codex/hooks/     # Codex hooks
.kiro/hooks/      # Kiro hooks (future)
```

### 3.3. Separation

- `.githooks/` - Shared entrypoints
- Agent folders - Agent-specific logic

## 4. Pre-Push Validation

### 4.1. Study Content Check

- Detects changed `.md` study files
- Requires `STUDY_PUSH_CONTENT_ACK=1` for non-interactive pushes
- Prompts for confirmation on interactive pushes

### 4.2. Structure Validation

- Concept notes must have required sections
- Navigation footers must be present
- READMEs must not contain study content

### 4.3. Related Docs Check

Adding, deleting, or renaming notes requires updating:
- `README.md` for the folder
- `00_{domain}_overview.md` for the domain (or `home.md` at root)

## 5. Environment Variables

### 5.1. Required in `.env`

```text
GITHUB_TOKEN=github_pat_...
GITHUB_USERNAME=your-username
GIT_USER_NAME=Your Name
GIT_USER_EMAIL=your@email.com
```

### 5.2. Never Commit

- `.env`
- `*.pem`
- `credentials.json`

## 6. Bypass Flags

| Flag | Effect |
|------|--------|
| `STUDY_PUSH_CONTENT_ACK=1` | Skip content acknowledgment |
| `CLAUDE_AUTO_PUSH=1` | Set by Claude auto-push |
| `STUDY_ALLOW_MULTI_COMMIT_PUSH=1` | Compatibility override for hooks that still check multi-commit pushes |

## 7. Commit and Push Boundaries

- One logical task per commit set
- Multiple commits in one push are allowed when they belong to one coherent task
- Do not force per-file pushes as a repo-wide rule

## 8. Windows Considerations

- Paths in `.claude/settings.json` must match the OS
- Bash scripts may need PowerShell equivalents
- Watch for `.git/index.lock` issues
