---
tags:
  - tooling
created_at: 2026-04-17T00:00:00
updated_at: 2026-04-20T00:00:00
recent_editor: CLAUDE
---

# Claude Code

I am **Claude Code**, Anthropic's CLI agent.

## 1. Rules

All rules are in [AGENTS.md](AGENTS.md). This file contains only platform-specific notes.

## 2. Session Start

Run `git pull origin main` before any read or write operation (multi-PC sync repo).

## 3. Automation Hooks

| Hook | Trigger | Action |
|------|---------|--------|
| `PostToolUse` on `Write\|Edit` | File write/edit | Stage, commit, push |
| `Stop` | Session end | Final push (async) |

Hook scripts in `.claude/hooks/`.

## 4. Git Commands

Run git as individual calls:

```bash
git -C "C:\Users\user\study" add file.md
git -C "C:\Users\user\study" commit -m "message"
git -C "C:\Users\user\study" push origin main
```

Never chain `cd && git` commands.

## 5. Subtree Overrides

- `aws/AGENTS.md` - AWS-specific viewpoint framework
