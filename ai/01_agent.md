# Agent

## What It Is

An agent is a program that takes a goal, reasons about it, and uses available capabilities to make progress toward an outcome.

It is not just a text generator. It can read files, compare options, run [tools](04_tools.md), make edits, and explain what it did.

## Analogy

Think of an agent like a junior-to-mid engineer working inside a controlled workshop (the [harness](02_harness.md)). You give the engineer a task, the workshop defines what they can touch, and the engineer decides how to use the available tools.

## Example

You open a repo and ask:

```text
Find why login is failing and fix it.
```

The agent may inspect auth-related files, search for error strings, run tests, patch code, and summarize the change. That is agent behavior — multiple steps with judgment.

## How It Works

Use an agent when the task has multiple steps or requires judgment:
- Understanding an unfamiliar codebase
- Fixing bugs across several files
- Reviewing a change for risks
- Using outside systems like GitHub or Google Drive

The agent is the decision-maker. The [harness](02_harness.md) is the environment, [tools](04_tools.md) are the capabilities, and [AGENTS.md](03_agents_md.md) provides repo-specific instructions.

## Why It Matters

If you confuse the agent with its environment, docs become hard to read. The clean split: agent = decision-maker, harness = execution environment, tools = capabilities, instructions = behavior shaping.

---
[Overview](00_overview.md) | Next: [Harness](02_harness.md) →
