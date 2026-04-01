# AGENTS.md

## What It Is
`AGENTS.md` is a repository-level instruction file for the agent.

It tells the agent how to behave inside that repo.

Common contents:
- coding conventions
- test commands
- architecture notes
- project-specific rules
- workflow expectations

## Analogy
Think of `AGENTS.md` as the local onboarding memo for a new engineer joining that repo.

The engineer is capable in general, but the memo tells them:
- how this team works
- what to avoid
- what commands matter
- what "done" means

## Example
An `AGENTS.md` might say:

```md
- Run `npm test` before finishing
- Do not edit generated files under `src/generated/`
- Prefer `rg` for search
- Keep React components under 300 LOC
```

That changes how the agent works in that repo, even though the agent itself is the same.

## What It Is Not

- It is not the global Codex config.
- It is not a skill.
- It is not a hook.

It is local instruction context tied to one repo or subtree.

## When People Mostly Use It

`AGENTS.md` is one of the most practically useful pieces for coding-agent workflows.

People use it to reduce repeated prompting about:
- style rules
- repo layout
- commands to run
- unsafe paths
- team preferences

## Why It Matters

Without `AGENTS.md`, the agent must infer more from the repo every time.

With `AGENTS.md`, the agent starts closer to the team’s expected behavior.
