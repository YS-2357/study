---
tags:
  - ai
  - aws
created_at: 2026-04-15T00:00:00
updated_at: 2026-04-18T13:00:00
recent_editor: CLAUDE
---

↑ [Overview](./00_ai_overview.md)

# Strands Agents SDK

## What It Is

Strands Agents SDK is an open-source Python framework from AWS for building AI agents that autonomously select and invoke [tools](04_tools.md) to complete a goal.

Rather than hardcoding a sequence of steps, you give the agent a list of tools and a goal. The Large Language Model (LLM) decides which tools to call and in what order.

## Analogy

Think of it like a contractor with a toolbox. You tell the contractor what the end result should be, not which wrench to use. The contractor inspects the situation and picks the right tool at each step.

## How It Works

Strands runs a **model-driven loop** — also called a [ReAct](https://arxiv.org/abs/2210.03629) loop:

1. User sends a goal.
2. LLM reasons: "What do I need to do next?"
3. LLM selects a tool and calls it.
4. Result is added to context.
5. LLM checks: "Am I done? If not, what's next?" → repeat from step 2.
6. LLM returns the final answer when satisfied.

### Defining tools

Any Python function decorated with `@tool` becomes an agent capability. The docstring becomes the LLM's description of when and how to use it.

```python
from strands import Agent, tool

@tool
def search_docs(query: str) -> str:
    """Search internal documentation for an answer."""
    ...

@tool
def call_api(endpoint: str, payload: dict) -> dict:
    """Call an external REST API endpoint."""
    ...

agent = Agent(tools=[search_docs, call_api])
result = agent("Process customer inquiry #1234.")
# LLM decides: search_docs first, then call_api — or the reverse — based on what it finds
```

### Comparison with other approaches

| Approach | Who decides the sequence? | Example |
|---|---|---|
| Direct API call | Your code (hardcoded) | `response = requests.get(url)` |
| LangChain chain | Your code (declared pipeline) | `chain = prompt | llm | parser` |
| Strands Agent | The LLM at runtime | `agent("do this")` |
| AutoGen | Multiple LLMs negotiating | multi-agent conversation |

### AWS integration

Strands connects natively to [AWS Bedrock](../aws/) models (Claude, Llama, Titan) with no extra adapter code. It also supports [MCP](07_mcp.md) servers as tool sources.

## Example

A support agent that handles an inbound ticket:

```python
from strands import Agent, tool

@tool
def get_ticket(ticket_id: str) -> dict:
    """Retrieve a support ticket by ID."""
    ...

@tool
def search_knowledge_base(query: str) -> list[str]:
    """Search the support knowledge base."""
    ...

@tool
def reply_to_ticket(ticket_id: str, message: str) -> None:
    """Send a reply to the customer."""
    ...

agent = Agent(tools=[get_ticket, search_knowledge_base, reply_to_ticket])
agent("Resolve ticket #5678 and reply to the customer.")
```

The agent fetches the ticket, searches for a solution, and sends a reply — without any if/else logic in your code.

## Why It Matters

Traditional automation breaks when the situation doesn't match the hardcoded path. A Strands agent adapts: if `search_knowledge_base` returns nothing useful, the LLM can try a different strategy or ask for clarification rather than failing silently.

The tradeoff is predictability. A hardcoded pipeline always follows the same steps; a model-driven loop may take a different path each run. Use Strands when flexibility matters more than determinism.

---
← Previous: [Subagent Design](14_subagent_design.md) | [Overview](./00_ai_overview.md)
