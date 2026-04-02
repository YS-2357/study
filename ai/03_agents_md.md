# AGENTS.md

## What It Is

`AGENTS.md` is a repository-level instruction file for the [agent](01_agent.md). It tells the agent how to behave inside that repo: coding conventions, test commands, architecture notes, and workflow expectations.

## Analogy

Think of `AGENTS.md` as the local onboarding memo for a new engineer joining that repo. The engineer is capable in general, but the memo tells them how this team works, what to avoid, and what "done" means.

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

---
← Previous: [Harness](02_harness.md) | [Overview](00_overview.md) | Next: [Tools](04_tools.md) →
