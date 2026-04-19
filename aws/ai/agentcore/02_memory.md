---
tags:
  - ai
  - aws
  - ml
created_at: 2026-04-17T14:18:47
updated_at: 2026-04-19T10:00:00
recent_editor: CLAUDE
source:
  - agentcore_intro_korean_2026-04
  - agentcore_memory_소개_2026-04
---

↑ [Overview](./00_agentcore_overview.md)

# AgentCore Memory

## What It Is
AgentCore Memory is the Amazon Bedrock AgentCore capability for storing agent context across interactions. The [AgentCore developer guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) lists Memory as a service that helps agents maintain useful context beyond a single request.

## How It Works
An agent writes useful information from a session into Memory and retrieves relevant context in later sessions. This keeps the agent code from needing to build a custom database, retrieval layer, and retention strategy before it can remember user preferences or prior work.

The flow is: store conversation events → extract insights via strategy → search relevant memories in future sessions.

## Short-term vs Long-term Memory

| Type | Purpose | Strategy needed | Key API |
|---|---|---|---|
| **Short-term** | Session continuity — raw conversation events | No | `get_last_k_turns()` |
| **Long-term** | Cross-session knowledge accumulation | Yes | `extract_memories()` + `search_memories()` |

### Short-term (Tutorial 01, 02)
```python
# Store events
client.add_session_events(memory_id, session_id,
    events=[{"role": "user",    "content": "Hello"},
            {"role": "assistant","content": "Hi there"}])

# Retrieve recent turns
turns = get_last_k_turns(memory_id, session_id, k=5)
```
Use for: in-session context, basic chatbots, fast prototyping.

### Long-term (Tutorial 03–08)
```python
# Create memory with strategy
memory = client.create_memory(
    name="long-term-memory",
    strategies=[{
        "strategy_name": "user_preference",
        "namespaces": ["food_prefs"]
    }])

# Store → extract → search
client.add_session_events(memory_id, session_id, events)
client.extract_memories(memory_id, session_id)  # async — await completion
results = client.search_memories(memory_id, query)
```
Use for: user preferences, knowledge accumulation, personalization.

**`extract_memories()` is async** — build in a wait/poll loop before searching.

## Memory Strategies

Strategies determine what gets extracted from conversations. Set at memory creation time; multiple strategies can be combined.

| Strategy | Extracts | Best for |
|---|---|---|
| `user_preference` | Preference/dislike key-value pairs | Personalization (diet, travel, shopping) |
| `semantic_memory` | Vector-embedded insights | Knowledge accumulation, long-term projects |
| `episodic_memory` | Episodes: situation → intent → reflection (3-stage pipeline) | Pattern learning, behavior tracking |
| Custom Override | UserPreference base + domain-specific extraction prompt | Medical, legal, industry-specific rules |

```python
# Episodic strategy
strategies=[{"strategy_name": "episodic_memory", "namespaces": ["episodes"]}]

# Custom Override — override the extraction prompt
strategies=[{
    "strategy_name": "user_preference",
    "override": {"extraction_prompt": "Extract only allergy information..."}
}]

# Combined strategies
strategies=[
    {"strategy_name": "user_preference", "namespaces": ["prefs"]},
    {"strategy_name": "semantic_memory",  "namespaces": ["knowledge"]}
]
```

Semantic strategy default retention: **365 days**.

## Core API Flow

```
create_memory()           → creates memory resource + sets strategies
add_session_events()      → stores user/assistant message pairs
extract_memories()        → (async) extracts insights per strategy
search_memories()         → retrieves relevant memories by query
get_last_k_turns()        → short-term: fetch last N raw turns
```

`MemoryClient` is the original API; `MemoryManager` is the newer API (Tutorial 02+).

## Framework Integration

### Strands (simplest — tool auto-injection)
```python
from bedrock_agentcore.memory import AgentCoreMemoryToolProvider

memory_tools = AgentCoreMemoryToolProvider(
    memory_id=memory_id,
    namespace="food_prefs"
).get_tools()

agent = Agent(
    model=BedrockModel("claude-sonnet-4-20250514-v1:0"),
    tools=[*my_tools, *memory_tools]  # agent uses memory as a tool
)
```

### LangGraph (fine-grained hook control)
```python
def pre_model_hook(state):
    # search relevant memories before each model call
    memories = client.search_memories(memory_id, query=state["input"])
    state["context"] = memories
    return state

def post_model_hook(state):
    # save conversation after model responds
    client.add_session_events(memory_id, session_id, events=state["messages"])
    client.extract_memories(memory_id, session_id)
    return state
```

### LlamaIndex (365-day long-term retention focus)
```python
from agentcore_memory import AgentCoreMemory

memory = AgentCoreMemory(memory_id=memory_id, namespace="research")

def search_long_term_memories(query: str) -> str:
    results = memory.search(query=query, max_results=5)
    return format_results(results)

agent = FunctionAgent(tools=[search_long_term_memories])
```

## Multi-Agent Shared Memory (Tutorial 08)

One `memory_id`, one namespace per agent — isolation without separate resources:

```
Coordinator Agent          Flight Agent           Hotel Agent
namespace: coordinator     namespace: flights     namespace: hotels
        ↕                       ↕                      ↕
                    Shared Memory (one memory_id)
                    ─────────────────────────────
                    coordinator ns | flights ns | hotels ns
```

Agents can read across namespaces when needed. Define namespace naming conventions before building.

## Key Points

- Store only information that should influence future sessions, not every transient token from every interaction.
- Separate user-specific memory from shared team or application memory when privacy and personalization matter.
- Treat Memory as agent context, not as the source of truth for business records.
- Start with Short-term; confirm requirements before switching to Long-term strategies.
- `UserPreference` is the most general-purpose strategy — covers most personalization scenarios.
- Inject memory search results into the system prompt for best results.
- Monitor Memory API call volume and latency via CloudWatch.
- Pair Memory with [AgentCore Evaluations](08_evaluations.md) to catch regressions where remembered context makes answers worse instead of better.

## Example
A support agent can remember that a user prefers concise answers and usually asks about billing incidents, then retrieve that preference during later sessions.

## Why It Matters
Agents are often stateless by default. Memory gives a production agent continuity without forcing every team to design its own persistence model.

---
↑ [Overview](./00_agentcore_overview.md)

**Related:** [AgentCore Runtime](01_runtime.md), [AgentCore Gateway](03_gateway.md), [AgentCore Evaluations](08_evaluations.md), [Strands Agents SDK](../11_strands_agents_sdk.md)
**Tags:** #ai #aws #ml
