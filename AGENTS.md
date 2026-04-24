---
tags:
  - tooling
created_at: 2026-04-23T23:41:19
updated_at: 2026-04-24T16:30:47
recent_editor: CODEX
---

# Agent Rules

Behavioral guidelines to reduce common agent mistakes. Merge these with the full repo rule files below.

Tradeoff: these guidelines bias toward caution over speed. For trivial tasks, use judgment.

## Think Before Coding

Don't assume. Don't hide confusion. Surface tradeoffs.

- State assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them instead of picking silently.
- If a simpler approach exists, say so.
- If something is unclear, stop and name what is confusing.

## Simplicity First

Minimum change that solves the problem. Nothing speculative.

- No features beyond what was asked.
- No abstractions for single-use code.
- No flexibility or configurability that was not requested.
- No defensive logic for impossible scenarios.
- If the solution is larger than it needs to be, simplify it.

## Surgical Changes

Touch only what you must. Clean up only the mess your change creates.

- Don't improve adjacent content, comments, or formatting without a task reason.
- Don't refactor things that are not broken.
- Match existing repo style even if you would do it differently.
- If you notice unrelated dead code or issues, mention them instead of deleting them.
- Every changed line should trace directly to the request.

## Goal-Driven Execution

Define success criteria. Loop until verified.

- Turn vague requests into concrete, checkable outcomes.
- For multi-step tasks, state a brief plan and how each step will be verified.
- Prefer tests, diffs, searches, or direct checks over "should work" assumptions.

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
