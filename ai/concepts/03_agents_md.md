---
tags:
  - ai
created_at: 2026-04-01T00:00:00
updated_at: 2026-04-19T09:11:51
recent_editor: CLAUDE
---

↑ [Overview](../00_ai_overview.md)

# AGENTS.md

## What It Is

`AGENTS.md` is a repository-level instruction file for the [agent](01_agent.md). It tells the agent how to behave inside that repo: coding conventions, test commands, architecture notes, and workflow expectations.

## Analogy

Think of `AGENTS.md` as the local onboarding memo for a new engineer joining that repo. The engineer is capable in general, but the memo tells them how this team works, what to avoid, and what "done" means.

## How It Works

`AGENTS.md` is only one part of the [instruction-loading path](02_harness.md). In [Claude Code](https://docs.anthropic.com/en/docs/claude-code/memory), `CLAUDE.md` files are loaded automatically in a hierarchy, and files can also import additional instruction files with `@path`. In [Kiro](https://kiro.dev/docs/steering/), `AGENTS.md` is always included, but Kiro also supports its own steering files under `.kiro/steering/`.

That creates an important practical limit: **if Codex and Kiro both read the same root `AGENTS.md`, that file is shared guidance, not a reliable place to separate agent roles.**

If you need different behavior per agent, the safer pattern is:

- Keep `AGENTS.md` limited to rules that are safe for every agent that reads the repo.
- Put harness-specific rules in the harness-specific file or mechanism that is loaded separately.
- In Claude-style workflows, that usually means `CLAUDE.md` or imported files referenced from it.
- In Kiro, that usually means dedicated steering files in `.kiro/steering/`.

So the question is usually not "How do I write conditional instructions inside one shared `AGENTS.md`?" The better question is "Which instruction file does each harness load separately?"

## Example

```md
- Run `npm test` before finishing
- Do not edit generated files under `src/generated/`
- Prefer `rg` for search
- Keep React components under 300 LOC
```

That changes how the agent works in that repo, even though the agent itself is the same.

## Why It Matters

Without `AGENTS.md`, the agent must infer repo conventions every time. With it, the agent starts closer to the team's expected behavior. It is one of the most practically useful pieces for coding-agent workflows — it reduces repeated prompting about style rules, repo layout, and commands to run.

It also prevents a common mistake: trying to split agent identity inside one shared file. If multiple harnesses load the same `AGENTS.md`, they all see the same instructions. Real separation comes from separate load paths, not from "if you are agent A, do X" text inside a single shared memo.

---
↑ [Overview](../00_ai_overview.md)

**Related:** [Harness](02_harness.md), [Tools](04_tools.md), [agent](01_agent.md)
**Tags:** #ai
