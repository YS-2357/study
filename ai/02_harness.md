# Harness

## What It Is

The harness is the controlled runtime environment around the [agent](01_agent.md). It defines what the agent can access and how it is allowed to operate: filesystem access, network access, approval policy, sandbox mode, available [tools](04_tools.md), and [profiles](09_profiles.md).

## Analogy

If the agent is a worker, the harness is the workshop — which rooms are unlocked, which tools are on the wall, what actions require approval, and what safety rules apply.

## How It Works

The harness is usually made of these concrete pieces:

| Component | What it controls | Example |
|-----------|------------------|---------|
| **Workspace / filesystem policy** | Which paths the agent can read or write | Read the repo, but only edit files under the current workspace |
| **Sandbox** | How shell commands are isolated from the host machine | Block writes outside allowed folders, restrict risky operations |
| **Network policy** | Whether the agent can access the internet or external APIs | Disable network by default, allow it only after approval |
| **Approval policy** | Which actions require user confirmation | Ask before pushing to GitHub or running a destructive command |
| **Tool registry** | Which [tools](04_tools.md) the agent can call | Shell commands, file search, browser automation, GitHub tools |
| **[MCP](07_mcp.md) connections** | Which external tool/data servers are attached | Connect Notion, GitHub, docs, or internal services through MCP |
| **[Profiles](09_profiles.md) / config** | Named runtime modes and default settings | `safe` = more read-only, `balanced` = normal workspace editing |
| **Working directory and session state** | Where commands start and what turn context the agent sees | Run commands from `/home/ys2357/study` and keep recent chat context |

This is why two sessions using the same model can behave differently: the agent may be identical, but the harness may expose different tools, permissions, and approval rules.

### Instruction-reading chain

At startup, the harness assembles the agent's context by reading instruction files in a fixed order. In Claude Code, that order is:

```
CLAUDE.md (user global) → CLAUDE.md (project root) → AGENTS.md files → session prompt
```

Only what the harness reads and passes in becomes part of the agent's active context. A rule written in `AGENTS.md` reaches the agent only if the harness picks it up. A rule written in `CLAUDE.md` is always read first.

This has one critical consequence: **if a rule is not in the file the harness reads at the root, it may never reach the agent at all.**

Real example — Kiro and rule injection:

Kiro's workflow rules were written in `AGENTS.md`. But the harness started from `CLAUDE.md`. The rules were never loaded into Kiro's context, so Kiro ignored them — not because Kiro was broken, but because the rules were placed outside the harness's read path. Moving the rules into `CLAUDE.md` fixed it immediately.

```
harness reads CLAUDE.md
  → loads rules ✓
    → Kiro sees rules ✓
      → Kiro follows rules ✓

harness reads CLAUDE.md (rules not here)
  → AGENTS.md loaded conditionally
    → Kiro may or may not see rules ✗
```

> **Tip:** When an agent ignores its own rules, check the instruction-reading chain before debugging the agent. The rule is probably real — it's just not in the path the harness reads.

## Example

In one harness, an agent can read all repo files, edit only Markdown notes under `/home/ys2357/study`, run `rg` and `git status`, but must ask before `git push` or internet access. In another harness, the same agent may be read-only with no network and no GitHub tools, so it can explain code but cannot publish changes.

## Why It Matters

Many beginner questions are really harness questions: "Why could the agent read this file but not write there?" or "Why did it ask for approval?" Those are usually harness differences, not agent differences.

The instruction-reading chain adds another class of harness question: "Why did the agent ignore its own rules?" The answer is almost always that the rule was written in a file outside the harness's read path — not that the agent or the rule was wrong.

---
← Previous: [Agent](01_agent.md) | [Overview](00_overview.md) | Next: [AGENTS.md](03_agents_md.md) →
