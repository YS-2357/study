# Agent

## What It Is
An agent is a program that takes a goal, reasons about it, and uses available capabilities to make progress toward an outcome.

In Codex, the agent is the thing you interact with when you run `codex`.

It is not just a text generator. It can:
- read files
- compare options
- run tools
- make edits
- explain what it did

## Analogy
Think of an agent like a junior-to-mid engineer working inside a controlled workshop.

You give the engineer a task, the workshop defines what they can touch, and the engineer decides how to use the available tools.

## Example
You open a repo and ask:

```text
Find why login is failing and fix it.
```

The agent may:
- inspect auth-related files
- search for error strings
- run tests
- patch code
- summarize the change

That is agent behavior, not just autocomplete.

## When You Use It

Use an agent when the task has multiple steps or requires judgment, such as:
- understanding an unfamiliar codebase
- fixing bugs
- editing several files consistently
- reviewing a change for risks
- using outside systems like GitHub or Google Drive

Do not think of the agent as a command. Think of it as the active worker for the session.

## What the Agent Is Not

- It is not the harness.
- It is not the skill.
- It is not the plugin.
- It is not the hook.

Those are surrounding pieces that shape how the agent operates.

## Why It Matters

If you confuse the agent with its environment, docs become hard to read.

The clean split is:
- agent = decision-maker and executor
- harness = execution environment
- tools = capabilities
- instructions = behavior shaping
