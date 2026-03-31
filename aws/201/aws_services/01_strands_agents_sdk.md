# Strands Agents SDK

## Official Documentation
- [Strands Agents Official Site](https://strandsagents.com/)
- [GitHub Repository](https://github.com/strands-agents/sdk-python)
- [AWS Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/strands-agents.html)
- [Technical Deep Dive (AWS Blog)](https://aws.amazon.com/blogs/machine-learning/strands-agents-sdk-a-technical-deep-dive-into-agent-architectures-and-observability/)

## What It Is
Strands Agents is an open-source Python SDK from AWS for building AI agents with minimal code. It takes a model-driven approach — you give the agent a model, a prompt, and tools, then the LLM decides how to use them.

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

## Where It Fits in the AWS Agent Stack

| Layer | Service | What it does |
|---|---|---|
| **Framework (code)** | **Strands Agents SDK** | Build agent logic — model + prompt + tools |
| **Managed agents** | Bedrock Agents | No-code/low-code agent builder in AWS console |
| **Infrastructure** | Bedrock AgentCore | Deploy, scale, secure, observe agents in production |

**Key distinction:** Strands is the *framework* you write code with. AgentCore is the *infrastructure* you deploy to. They work together but are independent — you can use Strands without AgentCore (deploy anywhere Python runs) or use AgentCore with other frameworks (LangGraph, CrewAI, etc.).

---

## Key Concepts

### Model Providers
Strands is model-agnostic. Supported providers:

| Provider | Class | Notes |
|---|---|---|
| **Amazon Bedrock** | `BedrockModel` | Default, recommended for AWS |
| **Anthropic (direct)** | `AnthropicModel` | Direct API, not through Bedrock |
| **OpenAI** | `OpenAIModel` | GPT models |
| **LiteLLM** | `LiteLLMModel` | Proxy to 100+ providers |
| **Ollama** | `OllamaModel` | Local models |
| **Custom** | `SAGEModel` / custom | Any model with tool-use support |

### Tools
Tools are Python functions the agent can call. Strands provides built-in tools and supports custom ones.

**Built-in tools** (via `strands-agents-tools` package):
- `calculator` — math operations
- `web_search` — internet search
- `file_read` / `file_write` — file operations
- `shell` — execute shell commands
- `python_repl` — run Python code
- `retrieve` — RAG retrieval from knowledge bases
- `code_interpreter` — sandboxed code execution (via AgentCore)
- `browser` — web browsing (via AgentCore)

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

**Multi-agent (Swarm)** — multiple specialized agents coordinated by a manager:
```python
from strands.multiagent import SwarmOrchestrator

orchestrator = SwarmOrchestrator(
    agents={"researcher": researcher_agent, "writer": writer_agent},
    manager=manager_agent
)
```

**Workflow (Graph)** — structured DAG of tasks with dependencies:
```python
from strands.multiagent import GraphOrchestrator

graph = GraphOrchestrator()
graph.add_node("research", researcher_agent)
graph.add_node("write", writer_agent)
graph.add_edge("research", "write")  # write depends on research
```

### Memory and State
- **Conversation history** — automatically maintained within a session
- **Session memory** — persist across sessions using AgentCore Memory or custom storage
- Agents are stateless by default — add memory explicitly when needed

### Observability
- Built-in OpenTelemetry tracing
- Integrates with AgentCore Observability and CloudWatch
- Trace every model call, tool invocation, and decision

---

## Precautions

### ⚠️ MAIN PRECAUTION: The LLM Decides — You Must Constrain It
- Model-driven means the LLM chooses which tools to call and in what order
- A vague system prompt + powerful tools = unpredictable behavior
- Write specific, bounded system prompts
- Only give the agent tools it actually needs

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
- Strands runs locally for development (just Python)
- For production: deploy to AgentCore Runtime for scaling, security, and observability
- Don't run production agents on a notebook or local machine

### 5. Model Selection
- Not all models handle tool-use equally well
- Claude Sonnet/Opus and GPT-4 class models work best for complex multi-tool agents
- Smaller models may struggle with multi-step reasoning
