---
tags:
  - ai
created_at: 2026-04-01T00:00:00
updated_at: 2026-04-19T09:11:51
recent_editor: CLAUDE
---

# AI Agents — Overview

Foundation concepts for understanding how coding agents (like Codex) work.

## Concepts

### Core Runtime
- [Agent](01_agent.md) — The decision-maker and executor.
- [Harness](02_harness.md) — The controlled environment around the agent.
- [AGENTS.md](03_agents_md.md) — Repo-level instructions for the agent.

### Working Components
- [Tools](04_tools.md) — Capabilities the agent can call; see [Interfaces](../computing/07_interfaces.md) for API and protocol context.
- [Skills](05_skills.md) — Reusable instruction bundles for specialized tasks.
- [Plugins](06_plugins.md) — Platform capability packs (GitHub, Gmail, etc.).

### Protocol and Automation
- [MCP](07_mcp.md) — The protocol layer behind external tool integrations; see [Interfaces](../computing/07_interfaces.md).
- [Profiles](09_profiles.md) — Named runtime modes (safe, balanced, permissive).
- [Hooks](08_hooks.md) — Event-triggered automation.

### LLM Internals
- [Attention (Q, K, V)](10_attention.md) — How tokens decide which other tokens matter; see [Caching](../computing/06_caching.md) for the general caching concept.
- [KV Cache](11_kv_cache.md) — Avoiding redundant computation during generation; see [Caching](../computing/06_caching.md).
- [Prompt Caching](12_prompt_caching.md) — Reusing computation across API calls.

### Multi-Agent Systems
- [Multi-Agent Orchestration](13_multi_agent_orchestration.md) — Role separation, review loops, and why a single agent can't catch its own mistakes.
- [Subagent Design](14_subagent_design.md) — When to spawn, when to divide, and how to match harness permissions to role.

For AWS-specific agent frameworks (Strands Agents SDK, Bedrock Agents, AgentCore), see [aws/ai/](../aws/ai/00_ai_overview.md).

## Quick Mental Model

| Term | Meaning |
|------|---------|
| Agent | The worker |
| Harness | The workshop around the worker |
| AGENTS.md | Repo instructions for the worker |
| Tools | Things the worker can use |
| Skills | Specialized playbooks |
| Plugins | Bundles for outside systems |
| MCP | Protocol for connecting tools/resources |
| Hooks | Automatic side effects |
| Profiles | Named runtime modes |

---
↑ [Home](../home.md)

