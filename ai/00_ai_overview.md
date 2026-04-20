---
tags:
  - ai
created_at: 2026-04-01T00:00:00
updated_at: 2026-04-20T13:50:42
recent_editor: CLAUDE
---

# AI — Overview

AI concepts, models, and tools.

## Concepts

Core LLM and agent concepts:

### Core Runtime
- [Agent](concepts/01_agent.md) — The decision-maker and executor.
- [Harness](concepts/02_harness.md) — The controlled environment around the agent.
- [AGENTS.md](concepts/03_agents_md.md) — Repo-level instructions for the agent.

### Working Components
- [Tools](concepts/04_tools.md) — Capabilities the agent can call.
- [Skills](concepts/05_skills.md) — Reusable instruction bundles for specialized tasks.
- [Plugins](concepts/06_plugins.md) — Platform capability packs (GitHub, Gmail, etc.).

### Protocol and Automation
- [MCP](concepts/07_mcp.md) — The protocol layer behind external tool integrations.
- [Hooks](concepts/08_hooks.md) — Event-triggered automation.
- [Profiles](concepts/09_profiles.md) — Named runtime modes (safe, balanced, permissive).

### LLM Internals
- [Attention (Q, K, V)](concepts/10_attention.md) — How tokens decide which other tokens matter.
- [KV Cache](concepts/11_kv_cache.md) — Avoiding redundant computation during generation.
- [Prompt Caching](concepts/12_prompt_caching.md) — Reusing computation across API calls.

### Multi-Agent Systems
- [Multi-Agent Orchestration](concepts/13_multi_agent_orchestration.md) — Role separation and review loops.
- [Subagent Design](concepts/14_subagent_design.md) — When to spawn and how to scope permissions.
- [LangChain / LangGraph](concepts/15_langchain_langgraph.md) — Agent frameworks from chains to state graphs.

For AWS-specific agent frameworks (Strands Agents SDK, Bedrock Agents, AgentCore), see [cloud/aws/ai/](../cloud/aws/ai/00_ai_overview.md).

## Products & Tools

| Product | Focus |
|---------|-------|
| [Claude](claude/00_claude_overview.md) | Anthropic's AI assistant — models, API, Claude Code |
| [Codex](codex/00_codex_overview.md) | OpenAI's AI coding agent |
| [Gemini](gemini/00_gemini_overview.md) | Google's AI model family |
| [Perplexity](perplexity/00_perplexity_overview.md) | AI-powered search |
| [Copilot](copilot/00_copilot_overview.md) | GitHub Copilot — IDE coding assistant |
| [Kiro](kiro/00_kiro_overview.md) | AWS Kiro — AI coding agent (tool-usage angle) |

---
↑ [Home](../home.md)
