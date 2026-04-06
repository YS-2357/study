# AI Agents — Overview

Foundation concepts for understanding how coding agents (like Codex) work.

## Study Order

### Core Runtime
1. [Agent](01_agent.md) — The decision-maker and executor.
2. [Harness](02_harness.md) — The controlled environment around the agent.
3. [AGENTS.md](03_agents_md.md) — Repo-level instructions for the agent.

### Working Components
4. [Tools](04_tools.md) — Capabilities the agent can call.
5. [Skills](05_skills.md) — Reusable instruction bundles for specialized tasks.
6. [Plugins](06_plugins.md) — Platform capability packs (GitHub, Gmail, etc.).

### Protocol and Automation
7. [MCP](07_mcp.md) — The protocol layer behind external tool integrations.
8. [Profiles](09_profiles.md) — Named runtime modes (safe, balanced, permissive).
9. [Hooks](08_hooks.md) — Event-triggered automation.

### LLM Internals
10. [Attention (Q, K, V)](10_attention.md) — How tokens decide which other tokens matter.
11. [KV Cache](11_kv_cache.md) — Avoiding redundant computation during generation.
12. [Prompt Caching](12_prompt_caching.md) — Reusing computation across API calls.

### Multi-Agent Systems
13. [Multi-Agent Orchestration](13_multi_agent_orchestration.md) — Role separation, review loops, and why a single agent can't catch its own mistakes.


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

## Cross-references

- Attention, KV Cache → [Caching](../computing/06_caching.md) for general caching concepts
- Tools, MCP → [Interfaces](../computing/07_interfaces.md) for API and protocol concepts
