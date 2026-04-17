---
tags:
  - ai
  - aws
  - ml
created_at: 260417-141847
updated_at: 260417-141847
---

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

## How It Works
You define the agent's model, prompt, and tools in code. At runtime, the model decides whether to answer directly or call a tool, then continues iterating until it has enough information to produce a final response.

## Example
```python
from strands import Agent
from strands.models.bedrock import BedrockModel
from strands_tools import calculator

agent = Agent(
    model=BedrockModel(model_id="anthropic.claude-sonnet-4-20250514-v1:0"),
    system_prompt="You are a careful math tutor.",
    tools=[calculator]
)

agent("What is 144 divided by 12?")
```

## Why It Matters
Strands gives you full code-level control over agent behavior without forcing you into a console-first builder. That makes it the right layer for custom orchestration, while deployment choices such as [Amazon Bedrock AgentCore](02_amazon_bedrock_agentcore.md) or Lambda remain separate infrastructure decisions.

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

### Memory and State
- **Conversation management** — built-in `SlidingWindowConversationManager` for context window control
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
- For production: deploy to AgentCore Runtime, Lambda, Fargate, EKS, App Runner, Docker, Kubernetes, or Terraform. These are deployment options, not equivalent architecture choices. If you need managed agent infrastructure rather than generic compute, prefer [Amazon Bedrock AgentCore](02_amazon_bedrock_agentcore.md).
- Don't run production agents on a notebook or local machine

### 5. Model Selection
- Not all models handle tool-use equally well
- Claude Sonnet/Opus and GPT-4 class models work best for complex multi-tool agents
- Smaller models may struggle with multi-step reasoning

---
← Previous: [Overview](00_overview.md) | [Overview](00_overview.md) | Next: [Amazon Bedrock AgentCore](02_amazon_bedrock_agentcore.md) →
