---
tags:
  - ai
  - aws
  - ml
created_at: 2026-04-17T14:18:47
updated_at: 2026-04-23T23:41:19
recent_editor: CODEX
source:
  - strands_jhrhee_2026_04
---

↑ [Overview](./00_ai_overview.md)

# Strands Agents SDK

## Official Documentation
- [Strands Agents Official Site](https://strandsagents.com/)
- [GitHub Repository (Python)](https://github.com/strands-agents/sdk-python)
- [GitHub Repository (TypeScript)](https://github.com/strands-agents/sdk-typescript)
- [AWS Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/strands-agents.html)
- [Technical Deep Dive (AWS Blog)](https://aws.amazon.com/blogs/machine-learning/strands-agents-sdk-a-technical-deep-dive-into-agent-architectures-and-observability/)

## What It Is
Strands Agents is an open-source SDK from AWS for building AI agents with minimal code. Available for both Python and TypeScript. It takes a model-driven approach — you give the agent a model, a prompt, and tools, then the LLM decides how to use them.

**The core idea:**
- Instead of writing complex orchestration logic ("first do this, then do that"), you define *what* the agent can do
- The LLM figures out *how* to accomplish the task by reasoning, selecting tools, and iterating

**Three components — that's it:**
```python
from strands import Agent
from strands.models.bedrock import BedrockModel
from strands_tools import calculator, web_search

agent = Agent(
    model=BedrockModel(model_id="anthropic.claude-sonnet-4-20250514-v1:0"),
    system_prompt="You are a helpful research assistant.",
    tools=[calculator, web_search]
)

response = agent("What is the population of Tokyo divided by the area in km²?")
```

**The agentic loop:**
```
User request → Model reasons → Tool call needed? → Execute tool → Feed result back → Repeat until done → Final response
```

## Analogy

Think of it like a contractor with a toolbox. You tell the contractor what the end result should be, not which wrench to use. The contractor inspects the situation and picks the right tool at each step.

## How It Works

You define the agent's model, prompt, and tools in code. At runtime, the model decides whether to answer directly or call a tool, then continues iterating until it has enough information to produce a final response.

The loop Strands runs is the **[ReAct](https://arxiv.org/abs/2210.03629) pattern** (Reason + Act — Yao et al., 2022):

1. User sends a goal.
2. LLM reasons: "What do I need to do next?"
3. LLM selects a [tool](../../../ai/concepts/04_tools.md) and calls it.
4. Result is added to context.
5. LLM checks: "Am I done? If not, what's next?" → repeat from step 2.
6. LLM returns the final answer when satisfied.

### Who Decides The Sequence?

Different automation paradigms differ on **who controls tool/step ordering** — code, declaration, or the model:

| Approach | Who decides sequence? | Example |
|---|---|---|
| Direct API call | Your code (hardcoded) | `response = requests.get(url)` |
| LangChain chain | Your code (declared pipeline) | `chain = prompt \| llm \| parser` |
| Strands Agent | The LLM at runtime | `agent("do this")` |
| AutoGen / CrewAI | Multiple LLMs negotiating | multi-agent conversation |

Strands' value is giving the LLM the decision, which is why a vague prompt + powerful tools produces unpredictable behavior (see Precautions). It also supports [MCP](../../../ai/concepts/07_mcp.md) servers as tool sources.

## Example

A support agent that handles an inbound ticket — no if/else in your code, the LLM picks the order:

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

The agent fetches the ticket, searches for a solution, and sends a reply. If the knowledge base returns nothing useful, the LLM can try a different strategy or ask for clarification rather than failing silently.

## Why It Matters

Strands gives you full code-level control over agent behavior without forcing you into a console-first builder. That makes it the right layer for custom orchestration, while deployment choices such as [Amazon Bedrock AgentCore](./10_amazon_bedrock_agentcore.md) or Lambda remain separate infrastructure decisions.

**The tradeoff is predictability.** A hardcoded pipeline always follows the same steps; a model-driven loop may take a different path each run. Use Strands when **flexibility matters more than determinism** — automation that has to adapt to novel inputs instead of breaking on the first case the original author didn't anticipate. For strictly deterministic flows, a plain LangChain chain, Step Functions, or hand-written code is a better fit.

## Where It Fits in the AWS Agent Stack

| Layer | Service | What it does |
|---|---|---|
| **Framework (code)** | **Strands Agents SDK** | Build agent logic — model + prompt + tools |
| **Managed agents** | Bedrock Agents | No-code/low-code agent builder in AWS console |
| **Infrastructure** | Bedrock AgentCore | Deploy, scale, secure, observe agents in production |

**Key distinction:** Strands is the *framework* you write code with. AgentCore is the *infrastructure* you deploy to. They work together but are independent — you can use Strands without AgentCore (deploy anywhere Python/Node.js runs) or use AgentCore with other frameworks (LangGraph, CrewAI, Google ADK, OpenAI Agents SDK, etc.).

## Key Concepts

### Model Providers
Strands is model-agnostic. Supported providers (official):

| Provider | Python | TypeScript | Notes |
|---|---|---|---|
| **Amazon Bedrock** | yes | yes | Default, recommended for AWS |
| **Amazon Nova** | yes | no | Nova-specific optimizations |
| **Anthropic (direct)** | yes | no | Direct API, not through Bedrock |
| **Google** | yes | yes | Gemini models |
| **OpenAI** | yes | yes | GPT models |
| **OpenAI Responses API** | yes | no | Responses API variant |
| **LiteLLM** | yes | no | Proxy to 100+ providers |
| **llama.cpp** | yes | no | Local models via llama.cpp |
| **LlamaAPI** | yes | no | LlamaAPI service |
| **MistralAI** | yes | no | Mistral models |
| **Ollama** | yes | no | Local models |
| **SageMaker** | yes | no | SageMaker endpoints |
| **Vercel** | no | yes | TypeScript only |
| **Writer** | yes | no | Writer models |
| **Custom** | yes | yes | Any model with tool-use support |

Community providers also available: CLOVA Studio, Cohere, Fireworks AI, MLX, NVIDIA NIM, vLLM, xAI, and more.

### Tools
Tools are Python/TypeScript functions the agent can call. Strands provides built-in tools and supports custom ones.

**Tool categories:**
- **Community Tools Package** (`strands-agents-tools`) — community-maintained tools like `http_request`, `shell`, `python_repl`, etc.
- **Vended Tools** — officially maintained tools
- **MCP Tools** — connect to any MCP server for thousands of community tools
- **Custom tools** — your own functions

**Custom tools** — decorate any Python function:
```python
from strands import tool

@tool
def get_weather(city: str) -> str:
    """Get current weather for a city."""
    # your implementation
    return f"Weather in {city}: 22°C, sunny"
```

The `@tool` decorator automatically generates the tool schema from the function signature and docstring. The LLM uses this schema to decide when and how to call the tool.

### Agent Architectures

**Single agent** — one model + tools, handles everything:
```python
agent = Agent(model=model, tools=[tool_a, tool_b])
```

**Agents as Tools** — nest agents inside other agents:
```python
@tool
def research(query: str) -> str:
    """Research a topic thoroughly."""
    agent = Agent(tools=[search_web])
    return str(agent(query))

writer = Agent(tools=[research])
writer("Write a post about AI agents")
```

**Graph** — structured flowchart where an agent decides which path to take at each node. Developer defines nodes (agents) and edges (transitions). Supports conditional logic, branching, and cycles.

**Swarm** — dynamic collaborative team. Developer provides a pool of specialized agents. Agents autonomously hand off tasks to the most suitable peer. Supports cycles.

**Workflow** — pre-defined task DAG executed as a single tool. Developer defines tasks and dependencies. Independent tasks run in parallel. No cycles (strict DAG).

**Agent2Agent (A2A)** — protocol support for distributed multi-agent systems.

### Plugins
- **Skills** — load modular instructions on demand. Skills activate when needed instead of bloating the system prompt.
- **Steering** — middleware for the agent loop. Intercept before/after tool calls to validate, guide, or block actions. Like HTTP middleware but for agent decisions.

### Hooks
Event-based system for intercepting agent behavior:
- `BeforeToolCallEvent` — inspect/modify tool calls before execution
- `AfterToolCallEvent` — inspect results after execution
- Enables human-in-the-loop approval flows (agent pauses, waits for approval, then continues)

### Structured Output
Get typed Pydantic objects back instead of raw text:
```python
from pydantic import BaseModel

class PersonInfo(BaseModel):
    name: str
    age: int
    occupation: str

result = agent.structured_output(PersonInfo, "Extract info from: John is a 30-year-old engineer.")
# result.name == "John", result.age == 30, result.occupation == "engineer"
```
`agent.structured_output(ModelClass, prompt)` — forces the response to conform to the Pydantic model schema.

### Memory and State
- **Conversation management** — built-in `SlidingWindowConversationManager` for context window control
  ```python
  from strands.agent.conversation_manager import SlidingWindowConversationManager
  manager = SlidingWindowConversationManager(window_size=20, should_truncate_results=True)
  agent = Agent(conversation_manager=manager)
  ```
- **Session memory** — persist across sessions using AgentCore Memory or custom storage
- **Shared state** — `invocation_state` for passing context across multi-agent patterns without exposing it to the LLM
- Agents are stateless by default — add memory explicitly when needed

### Observability
- Built-in OpenTelemetry tracing, metrics, and logs
- Integrates with AgentCore Observability and CloudWatch
- Trace every model call, tool invocation, and decision
- Zero-config: just set `trace_attributes` on the agent

### Strands Evals SDK
Separate evaluation framework (`strands-evals`) for testing agents:
- Define test cases, pick evaluators, run experiments
- Built-in evaluators: Output, Trajectory, Helpfulness, Faithfulness, Goal Success Rate, Tool Selection Accuracy, Tool Parameter Accuracy
- Custom evaluators supported
- User simulation for automated testing

## Similar Libraries

Strands isn't the only code-first agent framework. Quick map of the landscape:

| Library | Vendor | Positioning | How it differs from Strands |
|---------|--------|-------------|-----------------------------|
| **LangChain** | community | Broadest LLM toolkit (chains, agents, RAG, integrations) | Much larger surface; Strands is smaller and focused on agent loop |
| **LangGraph** | LangChain Inc. | Graph-based orchestration on top of LangChain | You draw the graph explicitly; Strands lets the LLM decide the path |
| **CrewAI** | community | Role-based multi-agent teams (researcher → writer → reviewer) | Higher-level abstraction around roles and tasks; Strands is primitive |
| **AutoGen** | Microsoft | Conversational multi-agent orchestration | Agents talk to each other in rounds; Strands loops on a single agent's tool calls |
| **OpenAI Agents SDK** | OpenAI | Handoffs + tools, successor to Swarm | Closest peer in spirit — declare model + tools, run loop; OpenAI-first |
| **Google ADK** | Google | Agent Development Kit | Google's direct equivalent, Gemini-first; similar model-driven design |
| **Pydantic AI** | Pydantic | Type-safe agents built on Pydantic models | Emphasizes typed I/O and validation; Strands is more loosely typed |
| **Smolagents** | Hugging Face | Minimal code-executing agent framework | Tiny surface, focus on agents that write and run Python; niche |
| **DSPy** | Stanford | Prompts as programs you optimize | Radically different paradigm: compile prompts, don't hand-write them |
| **LlamaIndex** | community | RAG-first, agents added later | Strongest for data ingestion/indexing; Strands is agent-first |
| **Semantic Kernel** | Microsoft | SK for .NET and Python | Enterprise integration focus; Strands is agent-loop focused |
| **Agno** (ex-Phidata) | community | Batteries-included agents + memory + RAG | Opinionated stack; Strands is minimal |

**How to pick:**
- Want a managed AWS deployment target + multi-framework support? → **Strands** (deploys cleanly to AgentCore)
- Want explicit control over state-machine transitions? → **LangGraph**
- Want role-based team abstraction? → **CrewAI**
- Want rigorous type safety? → **Pydantic AI**
- Want to optimize prompts mechanically? → **DSPy**

## AWS Viewpoints

| Perspective | Detail |
|-------------|--------|
| Feasibility | Use Strands when you want code-first agent logic that can run locally or deploy onto AWS infrastructure such as AgentCore Runtime. |
| Disruption | Adopting Strands changes application code, not the hosting layer by itself; deployment disruption depends on where the agent is later run. |
| Pros & Cons | It gives flexible model-driven tool use with little framework ceremony, but the model decides the sequence so prompts, tools, and guardrails must be constrained. |
| Differences | Strands is an SDK for agent behavior; AgentCore is production infrastructure, and Bedrock Agents is a managed console-first builder. |

## Precautions

### MAIN PRECAUTION: The LLM Decides — You Must Constrain It
- Model-driven means the LLM chooses which tools to call and in what order
- A vague system prompt + powerful tools = unpredictable behavior
- Write specific, bounded system prompts
- Only give the agent tools it actually needs
- Use Steering plugins for deterministic guardrails on tool calls

### 1. Tool Safety
- Tools like `shell` and `python_repl` can execute arbitrary code
- Never expose these in user-facing agents without sandboxing
- Use AgentCore Code Interpreter for safe code execution

### 2. Cost Awareness
- Each agentic loop iteration = model API call = cost
- Complex tasks can trigger many iterations
- Set `max_iterations` to prevent runaway loops
- Monitor token usage

### 3. Error Handling
- Tools can fail — the agent will try to recover, but may loop
- Implement timeouts and fallback logic
- Test edge cases where tools return errors

### 4. Local vs Production
- Strands runs locally for development (just Python/Node.js)
- For production: deploy to AgentCore Runtime, Lambda, Fargate, EKS, App Runner, Docker, Kubernetes, or Terraform. These are deployment options, not equivalent architecture choices. If you need managed agent infrastructure rather than generic compute, prefer [Amazon Bedrock AgentCore](./10_amazon_bedrock_agentcore.md).
- Don't run production agents on a notebook or local machine

### 5. Model Selection
- Not all models handle tool-use equally well
- Claude Sonnet/Opus and GPT-4 class models work best for complex multi-tool agents
- Smaller models may struggle with multi-step reasoning

### 6. Production Checklist
- Store all secrets and API keys in **AWS Secrets Manager** — never hardcode
- Enable **OpenTelemetry tracing** via `aws-opentelemetry-distro>=0.10.0`
- Set up **CI/CD pipeline** for automated agent deployment
- Define **access control** — who/what can invoke the agent endpoint
- Write **unit tests** for individual tools and **E2E tests** for full agent flows
- Set `max_iterations` to prevent runaway loops in production

---
↑ [Overview](./00_ai_overview.md)

**Related:** [Amazon Bedrock AgentCore](./10_amazon_bedrock_agentcore.md), [Bedrock Integration Patterns](./12_amazon_bedrock_integration_patterns.md), [tool](../../../ai/concepts/04_tools.md), [MCP](../../../ai/concepts/07_mcp.md)
**Tags:** #ai #aws #ml
