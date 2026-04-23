---
tags:
  - ai
created_at: 2026-04-20T14:15:06
updated_at: 2026-04-23T09:51:00
recent_editor: CLAUDE
---

# AI Concepts - Overview

Core LLM and agent concepts.

## Core Runtime

- [Agent](01_agent.md) - The decision-maker and executor.
- [Harness](02_harness.md) - The controlled environment around the agent.
- [AGENTS.md](03_agents_md.md) - Repo-level instructions for the agent.

## Working Components

- [Tools](04_tools.md) - Capabilities the agent can call.
- [Skills](05_skills.md) - Reusable instruction bundles for specialized tasks.
- [Plugins](06_plugins.md) - Platform capability packs such as GitHub, Gmail, and other connectors.

## Protocol and Automation

- [MCP](07_mcp.md) - The protocol layer behind external tool integrations.
- [Hooks](08_hooks.md) - Event-triggered automation.
- [Profiles](09_profiles.md) - Named runtime modes such as safe, balanced, and permissive.

## LLM Internals

- [Attention (Q, K, V)](10_attention.md) - How tokens decide which other tokens matter.
- [KV Cache](11_kv_cache.md) - Avoiding redundant computation during generation.
- [Prompt Caching](12_prompt_caching.md) - Reusing computation across API calls.

## Knowledge & Memory

- [Embedding Models](17_embedding_models.md) - Mapping text to dense vectors; the retrieval layer beneath RAG.
- [RAG](16_rag.md) - Grounding LLM responses in external documents fetched at query time.

## Multi-Agent Systems

- [Multi-Agent Orchestration](13_multi_agent_orchestration.md) - Role separation and review loops.
- [Subagent Design](14_subagent_design.md) - When to spawn and how to scope permissions.
- [LangChain / LangGraph](15_langchain_langgraph.md) - Agent frameworks from chains to state graphs.

---
[AI Overview](../00_ai_overview.md)
