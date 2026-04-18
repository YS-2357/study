---
tags:
  - security
  - tooling
created_at: 2026-04-17T00:00:00
updated_at: 2026-04-17T00:00:00
recent_editor: CLAUDE
---

# Security Rules

Security hooks and delivery rules for this repository.

## 1. Delivery Loop

**"Success should be quiet, failure must be loud"**

On success:
- No output, silent completion
- Commit and push without fanfare

On failure:
- Explicit error message with context
- Log to system message
- Stop and fix before proceeding

After any file create/edit/rename/move/delete:
1. Update relevant docs (domain's `00_{domain}_overview.md` or root `home.md`, README.md, navigation)
2. Verify Markdown structure and navigation rules
3. Check for security issues
4. Commit and push

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

- `.env` - Contains real tokens
- `*.pem` - Private keys
- `credentials.json` - API credentials
- Any file with `secret`, `token`, `password` in name

### 2.2. If Security Issue Found

1. Stop immediately
2. Do not commit or push
3. Remove the sensitive content
4. Then proceed with commit

## 3. Hook Architecture

### 3.1. Entrypoints

```
.githooks/
├── pre-push              # Main dispatcher
├── pre-push-study-content  # Content acknowledgment
└── git-credential-env.sh   # Credential helper
```

### 3.2. Agent-Specific Hooks

```
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

Adding/deleting/renaming notes requires updating:
- `README.md` for the folder
- `00_overview.md` for the domain

## 5. Environment Variables

### 5.1. Required in .env

```
GITHUB_TOKEN=github_pat_...
GITHUB_USERNAME=your-username
GIT_USER_NAME=Your Name
GIT_USER_EMAIL=your@email.com
```

### 5.2. Never Commit

- `.env` - Contains real tokens
- `*.pem` - Private keys
- `credentials.json` - API credentials

## 6. Bypass Flags

| Flag | Effect |
|------|--------|
| `STUDY_PUSH_CONTENT_ACK=1` | Skip content acknowledgment |
| `CLAUDE_AUTO_PUSH=1` | Set by Claude auto-push |
| `STUDY_ALLOW_MULTI_COMMIT_PUSH=1` | Allow multi-commit push |

## 7. Multi-Commit Rule

Codex hooks enforce 1 file change = 1 commit. Override with `STUDY_ALLOW_MULTI_COMMIT_PUSH=1`.

## 8. Windows Considerations

- Paths in `.claude/settings.json` must match OS
- Bash scripts may need PowerShell equivalents
- Watch for `.git/index.lock` issues
