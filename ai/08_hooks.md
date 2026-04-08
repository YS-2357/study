# Hooks

## What It Is

A hook is a script or action that runs automatically when a certain runtime event happens — like a notification after an agent turn completes, a post-run formatter, or a custom logging action.

## Analogy

If the agent is the worker, a hook is the automatic bell that rings when something specific happens in the workshop. The worker doesn't need to remember to ring it — the environment does it automatically.

## How It Works

A hook is attached to an event such as "before push" or "after a task finishes." When that event happens, the hook runs a script or command that checks or updates something automatically.

## Example

In this repo, a `pre-push` hook can scan changed Markdown files, make sure related `README.md` and `00_overview.md` files were updated when notes move, and stop the push if it detects a secret. That follows the rule "fail loudly, succeed quietly" because success prints nothing, but failure explains exactly what must be fixed.

## Why It Matters

Compared with [tools](04_tools.md), [skills](05_skills.md), and [AGENTS.md](03_agents_md.md), hooks are lower priority for learning, but they are useful when you want the environment to enforce routine checks consistently instead of relying on memory.

---
← Previous: [MCP](07_mcp.md) | [Overview](00_overview.md) | Next: [Profiles](09_profiles.md) →
