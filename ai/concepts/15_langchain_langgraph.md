---
tags:
  - ai
  - agents
created_at: 2026-04-20T08:29:39
updated_at: 2026-04-23T23:41:19
recent_editor: CODEX
source:
  - langchain_langgraph_2026_meaning
---

↑ [Overview](./00_concepts_overview.md)

# LangChain / LangGraph

LangChain and LangGraph are part of the same agent-building stack, but they sit at different abstraction levels.

## Official Documentation

- [LangChain overview](https://docs.langchain.com/oss/python/langchain/overview)
- [LangChain agents](https://docs.langchain.com/oss/python/langchain/agents)
- [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview)
- [LangChain middleware](https://docs.langchain.com/oss/python/langchain/middleware/overview)
- [LangChain MCP](https://docs.langchain.com/oss/python/langchain/mcp)
- [Deep Agents overview](https://docs.langchain.com/oss/python/deepagents/overview)

## What Changed

The early LangChain mental model was a **chain**: pass input through a prompt, a model, maybe a retriever, and an output parser. That works when the application is a mostly deterministic data flow.

Agent applications need a different shape. The model may need to call tools, inspect results, retry, branch, ask for approval, or persist state before it can finish. That moves the center of gravity from a linear chain to an **agent loop**.

The 2026 interpretation from the source is:

| Layer | Main idea | When it matters |
|---|---|---|
| Workflow | Linear pipeline | Deterministic prompt/retrieval/output flows |
| LangGraph | State graph | Custom control flow, loops, branching, persistence |
| LangChain agent | Standard agent loop | Quick production-ready tool-calling agents |
| Middleware | Hook points | Context engineering around model/tool calls |
| MCP adapters | Pluggable tools | Runtime discovery and use of external tools |
| Deep Agents | Harness stack | Complex work needing planning, files, subagents, memory |

## LangGraph

LangGraph is the low-level orchestration layer. It represents an agent as a graph of nodes and edges, with shared state passed through the graph.

Use LangGraph when the agent flow itself is the product:

- You need explicit control over branching and loops.
- Nodes need to read and write shared state.
- The agent must survive long runs, interruptions, retries, or process restarts.
- Human approval or state inspection is part of the workflow.
- A simple ReAct-style loop is not enough structure.

In this framing, LangGraph is not just "LangChain with diagrams." It is the control-flow runtime underneath more convenient agent APIs.

## LangChain Agents

LangChain's current agent entry point is `create_agent`. It gives a standard loop around a model and tools:

```python
from langchain.agents import create_agent

agent = create_agent(
    model="anthropic:claude-sonnet-4-6",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)
```

The agent runs until the model produces a final answer or an iteration limit stops it. Under the hood, LangChain agents use LangGraph so they can inherit durable execution, streaming, persistence, and human-in-the-loop support.

Use LangChain agents when you want the standard tool-calling loop without designing the whole graph yourself.

## Middleware and Context Engineering

Middleware is the slot system around the agent loop. Instead of treating the loop as a black box, middleware lets you intercept important moments:

- before a model call
- around a model call
- after a model call
- before or after tool execution

That is why middleware is central to context engineering. A reliable agent is less about sending one perfect prompt and more about controlling what context, tools, memory, and guardrails are available at each step.

Common middleware jobs:

- Mask or filter sensitive information before a model call.
- Trim old conversation history.
- Inject user or project context.
- Retry or fallback after model/tool failures.
- Validate outputs before returning them.
- Pause for human approval before risky tool calls.

## Memory, HITL, and Harness

The source distinguishes the loop from the surrounding **[harness](./02_harness.md)**.

The loop is the repeated LLM/tool/observation cycle. The harness is the system around that loop: memory, approval, files, permissions, observability, and runtime state.

Examples:

- A **checkpointer** stores short-term state so the agent can resume after an interrupt or restart.
- A **store** holds longer-term memory, user preferences, or retrieved facts across sessions.
- **Human-in-the-loop** approval can pause execution before sensitive actions.
- A filesystem or virtual workspace lets the agent manage large context outside the model window.

The source's main warning is that the loop alone is not the whole agent. Production agents are usually harnessed loops.

## MCP and Tools

The Model Context Protocol ([MCP](./07_mcp.md)) changes tool integration from hardcoded wiring to runtime discovery. With `langchain-mcp-adapters`, a LangChain agent can load tools from one or more MCP servers and pass them into `create_agent`.

This matters because tools become data supplied by the runtime, not only functions compiled into the agent code. Adding a Slack, database, filesystem, or internal API tool can become an integration problem rather than a code rewrite.

## Deep Agents and Skills

Deep Agents package a higher-level harness on top of the LangChain/LangGraph stack. They include patterns such as planning, a virtual filesystem, subagents, memory, permissions, and human approval.

Skills are different from tools:

| Concept | Role |
|---|---|
| Tool | Action the agent can execute |
| Skill | Knowledge or workflow loaded when relevant |

A skill is progressive disclosure for context. The agent sees lightweight metadata first, then loads the deeper instructions only when the task needs them.

## How To Choose

| Need | Use |
|---|---|
| Simple deterministic prompt or retrieval pipeline | Plain code or a small LangChain chain |
| Standard tool-calling agent | LangChain `create_agent` |
| Custom state machine or long-running stateful workflow | LangGraph |
| Runtime tool discovery from external systems | LangChain MCP adapters |
| Complex project agent with files, planning, memory, and subagents | Deep Agents |

## Why It Matters

The practical question for 2026 is not "Should I use LangChain?" The better question is which layer of the LangChain ecosystem matches the problem:

- Use **LangChain** when the standard agent abstraction is enough.
- Use **LangGraph** when control flow and state need to be explicit.
- Use **middleware** when reliability depends on context shaping at each loop step.
- Use **MCP adapters** when external tools should be pluggable.
- Use **Deep Agents** when the harness itself is the value.

The trend is from chains to agent harnesses: less focus on one linear LLM call, more focus on controlled loops with state, tools, memory, approval, and context management.

---
↑ [Overview](./00_concepts_overview.md)

**Related:** [Agent](./01_agent.md), [Harness](./02_harness.md), [Tools](./04_tools.md), [Skills](./05_skills.md), [MCP](./07_mcp.md), [Subagent Design](./14_subagent_design.md)
**Tags:** #ai #agents
