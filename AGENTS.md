---
tags:
  - tooling
created_at: 2026-04-23T23:41:19
updated_at: 2026-04-23T23:41:19
recent_editor: CODEX
---

# Agent Rules — Study Repository

All agents must read their platform-specific rule file **before any action**.

| Agent | Rule File |
|-------|-----------|
| Claude Code | [CLAUDE.md](CLAUDE.md) + [rules/CLAUDE.md](rules/CLAUDE.md) |
| Codex | [rules/CODEX.md](rules/CODEX.md) |
| Kiro | [rules/KIRO.md](rules/KIRO.md) |

Shared rules (§1–§11) live in [rules/AGENTS.md](rules/AGENTS.md).  
Agent-specific rules (§12+) live in each agent's own file.

---

## Subtree Overrides

- `cloud/aws/AGENTS.md` — AWS-specific viewpoint framework
