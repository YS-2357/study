---
tags:
  - tooling
created_at: 2026-04-17T00:00:00
updated_at: 2026-04-18T12:00:00
recent_editor: CLAUDE
---

# Claude Code

Claude Code automation for this repository. For all rules, see [AGENTS.md](AGENTS.md).

## 1. Automation Hooks

| Hook | Trigger | Action |
|------|---------|--------|
| `PostToolUse` on `Write\|Edit` | File write/edit | Stage, commit, push |
| `Stop` | Session end | Final push (async) |

Hook scripts in `.claude/hooks/`.

## 2. Git Commands

Run git as individual calls with `-C`:

```bash
git -C "C:\Users\user\study" add file.md
git -C "C:\Users\user\study" commit -m "message"
git -C "C:\Users\user\study" push origin main
```

Never chain `cd && git` commands.

## 3. Subtree Overrides

- `aws/CLAUDE.md` - AWS four-viewpoint framework
