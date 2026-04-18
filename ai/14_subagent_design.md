---
tags:
  - ai
  - tooling
created_at: 2026-04-10T00:00:00
updated_at: 2026-04-18T13:00:00
recent_editor: CLAUDE
---

↑ [Overview](./00_ai_overview.md)

# Subagent Design

## What It Is

Subagent design is the set of rules that govern when to spawn a separate [agent](01_agent.md), when to handle work inline, which [harness](02_harness.md) component to reach for, and how to divide agent responsibilities so each agent has one reason to exist.

The core philosophy mirrors [decomposition](../computing/09_decomposition.md): **one unit = one reason to change** — applied to agents, it becomes **one agent = one role, one context, one failure domain**. The same rule applies to harness components: each component type has one job, and picking the wrong one creates accidental coupling.

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

### Harness components: when to use what

Every capability available to an agent comes from one of these component types. Choosing the right one is the same decomposition question applied to the harness: **each component has one job**.

### Tool

A [tool](04_tools.md) is a direct, executable capability — file read, shell command, web search, browser action.

**Slogan:** use the sharpest tool for the job.

| Use a tool when | Avoid when |
|-----------------|-----------|
| The target is known (path, symbol, URL) | The same multi-step workflow recurs — use a skill instead |
| A single operation answers the question | You need cross-system integration — use a plugin |
| Speed matters and context is already present | The task has no direct built-in tool — compose via MCP |

Built-in tools (`Read`, `Grep`, `Glob`, `Bash`) cover most repo work. Reach for them before spawning anything.

### Skill

A [skill](05_skills.md) is a reusable instruction bundle — a named playbook for a recurring workflow.

**Slogan:** repeatable work gets a playbook.

| Use a skill when | Avoid when |
|-----------------|-----------|
| The same task type recurs and benefits from fixed steps | It's a one-time task — just prompt directly |
| Generic prompting produces noisy or inconsistent results | A tool can answer it in one call |
| You want structured steps enforced across sessions | The workflow is simple enough to remember |

### Plugin

A [plugin](06_plugins.md) is a capability bundle for an external platform — GitHub, Gmail, Google Drive, Vercel.

**Slogan:** platform work = plugin.

| Use a plugin when | Avoid when |
|-----------------|-----------|
| The agent needs to act on an outside system (PRs, issues, email) | The work stays entirely inside the local repo |
| Multiple tools and skills for the same platform are needed | Only one tool from that platform is needed — wire it directly |

### MCP

[MCP](07_mcp.md) is the protocol that wraps a non-native capability into a standard shape the harness can consume.

**Slogan:** any shape, one adapter.

| Use MCP when | Avoid when |
|-------------|-----------|
| A third-party service has an MCP server available | A built-in tool already covers the need |
| You need to add a new external tool without writing custom integration code | The tool is internal and can be exposed as a simple shell command instead |
| Multiple agents or harnesses need the same external capability | It's a one-off lookup — a direct API call or `curl` is simpler |

MCP is infrastructure for tools, not a tool itself. Think of it as the adapter standard — you configure it once so that tools and resources from external servers become discoverable by the harness.

### Hook

A [hook](08_hooks.md) is a script that runs automatically on a harness event — before push, after write, at session end.

**Slogan:** fail loudly, succeed quietly.

| Use a hook when | Avoid when |
|----------------|-----------|
| A check must run consistently without relying on agent memory | The check is one-time or specific to a single session |
| Failure must be visible and block progress | The action is informational only — a log or notification |
| The same enforcement applies across every agent using this repo | The logic changes frequently — keep it in a skill instead |

Hooks enforce the mechanical layer. They are not a substitute for agent judgment — they catch what the agent should not need to remember.

### Permission / Profile

A [profile](09_profiles.md) is a named runtime mode. Permissions are its building blocks: which paths are writable, which commands are allowed, whether network access is on.

**Slogan:** least privilege per role.

| Use narrow permissions when | Use broader permissions when |
|-----------------------------|------------------------------|
| Agent is a reviewer — read-only is enough | Agent is an implementer that must write and deploy |
| Agent is an advisor — no commit rights needed | Agent is an orchestrator that must coordinate across systems |
| Blast radius must be minimized before work starts | The agent's full scope is trusted and well-understood |

Set permissions before the agent starts, not reactively. A harness that is too permissive from the start cannot be narrowed mid-task without losing work.

### Decision summary

| I need to… | Reach for |
|------------|-----------|
| Read a file, search code, run a command | **Tool** (direct) |
| Run a recurring multi-step workflow | **Skill** |
| Act on GitHub, Gmail, or another platform | **Plugin** |
| Add an external service the harness doesn't support natively | **MCP** |
| Enforce a check automatically on every push or write | **Hook** |
| Limit what an agent can touch | **Permission / Profile** |
| Separate roles or parallelize independent work | **Subagent** |

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
← Previous: [Multi-Agent Orchestration](13_multi_agent_orchestration.md) | [Overview](./00_ai_overview.md) | Next: [Strands Agents SDK](15_strands_agents_sdk.md) →
