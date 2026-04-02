# Harness

## What It Is

The harness is the controlled runtime environment around the [agent](01_agent.md). It defines what the agent can access and how it is allowed to operate: filesystem access, network access, approval policy, sandbox mode, available [tools](04_tools.md), and [profiles](09_profiles.md).

## Analogy

If the agent is a worker, the harness is the workshop — which rooms are unlocked, which tools are on the wall, what actions require approval, and what safety rules apply.

## Example

A harness may allow reading files in a repo, editing only inside the workspace, running shell commands, and requiring approval before internet access. The same agent behaves very differently depending on the harness.

## How It Works

The harness typically includes:
- Config files such as `~/.codex/config.toml`
- Tool definitions and [MCP](07_mcp.md) server connections
- Approval and sandbox settings
- [Profiles](09_profiles.md) like `safe` or `balanced`

## Why It Matters

Many beginner questions are really harness questions: "Why could the agent read this file but not write there?" or "Why did it ask for approval?" Those are usually harness differences, not agent differences.

---
← Previous: [Agent](01_agent.md) | [Overview](00_overview.md) | Next: [AGENTS.md](03_agents_md.md) →
