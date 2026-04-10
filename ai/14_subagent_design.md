# Subagent Design

## What It Is

Subagent design is the set of rules that govern when to spawn a separate [agent](01_agent.md), when to handle work inline, and how to divide agent responsibilities so each agent has one reason to exist.

The core philosophy mirrors [decomposition](../computing/09_decomposition.md): **one agent = one coherent job**. When an agent's scope grows to cover two unrelated concerns, it becomes a candidate to split — for the same reason a function that does two things should be divided.

## How It Works

### The spawn decision

Before spawning a subagent, answer two questions:

1. **Is the work independent?** — Does it require information not yet in the current context?
2. **Would spawning protect the main context or parallelize real work?** — Or is it just delegation for its own sake?

| Condition | Spawn? |
|-----------|--------|
| Task is independent and context-heavy | Yes |
| Task can run in parallel with current work | Yes — spawn in background |
| Task requires a specialized agent type | Yes |
| Task is a simple, directed lookup (file path, function name known) | No — use tools directly |
| You already have the context to answer | No — handle inline |
| Result is needed before the next step | No — spawning cold adds overhead |

### When to divide an agent

Divide an agent when it would have to play two conflicting roles in the same task.

The clearest case is **context contamination**: an agent that implemented something cannot objectively review it. It built the system, justified the choices, and believes the output is correct — because it did the work. A separate reviewer has no implementation history and can evaluate purely against the rules. See [Multi-Agent Orchestration](13_multi_agent_orchestration.md) for the full role taxonomy.

Other split signals:

| Signal | What to do |
|--------|-----------|
| Agent is both writer and judge of its own output | Separate implementer and reviewer |
| Two subtasks are independent and slow | Spawn both in parallel |
| Subtask requires a different permission level | Give it its own harness |
| One agent's failure should not block the other | Isolate them |
| Task needs a fresh context with no prior bias | Spawn cold |

### When not to spawn

Spawning starts cold — the subagent has no memory of the current conversation and must re-derive context from the prompt. This is expensive. Avoid it when:

- The target is already known (file path, symbol name, line number). Use `Read`, `Grep`, or `Glob` directly.
- The task is short and the answer fits in a few tool calls.
- The work must happen sequentially and there is nothing to parallelize.
- You would just be moving work to the subagent without giving it enough context to do it well.

### Parallel vs foreground

| Mode | Use when |
|------|---------|
| Foreground (default) | You need the result before the next step |
| Background | You have genuinely independent work to do while waiting |

Do not spawn background agents and then sleep-poll for results. The system notifies when done.

### Harness philosophy

The [harness](02_harness.md) defines what an agent can touch. When dividing agents, match the harness to the role:

- A reviewer agent should be read-only — it has no reason to write.
- An infra agent needs deploy permissions that a frontend agent should not have.
- An advisor agent should have network access but no commit rights.

Giving a narrow harness to each role is the enforcement mechanism for role separation. Without it, a reviewer could accidentally mutate what it is reviewing.

## Example

A search feature is being built and reviewed.

**Wrong:** one agent writes the backend, then reviews its own output.
- The agent knows why it made every decision. It cannot be adversarial toward its own work.

**Right:** implementer agent writes the backend → reviewer agent scores against the checklist → supervisor agent decides.

```
Orchestrator assigns TASK-001
  → Implementer: writes search handler, repo fn, DB query
  → Reviewer: scores against 15-item checklist (no implementation context)
    → 11/15 — items 3, 7 failed (auth not separated, query not parameterized)
  → Supervisor: conditional approve — fix items 3 and 7
  → Implementer: fixes and resubmits as TASK-001b
  → Reviewer: 15/15
  → Supervisor: approve
```

The reviewer's clean context is the point. It has no stake in the work passing.

## Why It Matters

The slogan for agent design is the same as for code decomposition: **one unit = one reason to change** — but applied to agents, it becomes **one agent = one role, one context, one failure domain**.

When agents share too much scope:
- Context contamination makes self-review unreliable.
- A failure in one concern blocks an unrelated concern.
- Permissions bleed across roles, increasing blast radius.

When agents are divided well:
- Each can be replaced, re-prompted, or retried independently.
- Review is adversarial by construction, not by coincidence.
- Parallel agents finish faster than a single serial agent.

> **Tip:** If you can describe what an agent does without using "and", the scope is right. "Implements the backend" is one role. "Implements the backend and reviews it" is two — split them.

---
← Previous: [Multi-Agent Orchestration](13_multi_agent_orchestration.md) | [Overview](00_overview.md) | Next: [Overview](00_overview.md) →
