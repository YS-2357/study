---
tags:
  - ai
created_at: 2026-04-01T00:00:00
updated_at: 2026-04-18T11:46:13
recent_editor: CLAUDE
---

↑ [Overview](./00_ai_overview.md)

# Skills

## What It Is

A skill is a reusable instruction bundle that teaches the [agent](01_agent.md) how to handle a specialized kind of task. A skill usually contains a `SKILL.md`, optional scripts, and optional references.

## Analogy

If the agent is a worker and [tools](04_tools.md) are the instruments, a skill is a playbook for a recurring job — like how to debug CI failures or how to work from a Figma design.

## Example

A CI-debugging skill adds a repeatable workflow: inspect failing checks, read logs, isolate likely cause, reproduce locally, patch the minimal fix. That is more structured than a normal free-form prompt.

## How It Works

Use a skill when:
- The task type repeats often
- The workflow benefits from fixed steps
- Generic prompting would be noisy or inconsistent

Most people use built-in skills for specialized workflows and no skill at all for ordinary repo work. Agent + [tools](04_tools.md) + [AGENTS.md](03_agents_md.md) cover most work. Skills become useful when the workflow gets specialized.

## Why It Matters

Skills are important but not the main thing you interact with every minute. Don't over-focus on them as a beginner.

---
← Previous: [Tools](04_tools.md) | [Overview](./00_ai_overview.md) | Next: [Plugins](06_plugins.md) →
