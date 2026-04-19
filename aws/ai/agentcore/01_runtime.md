---
tags:
  - ai
  - aws
  - ml
  - serverless
created_at: 2026-04-17T14:18:47
updated_at: 2026-04-19T10:00:00
recent_editor: CLAUDE
source:
  - agentcore_intro_korean_2026-04
  - agentcore_runtime_소개_2026-04
---

↑ [Overview](./00_agentcore_overview.md)

# AgentCore Runtime

## What It Is
AgentCore Runtime is the Amazon Bedrock AgentCore service for hosting and invoking agent code as production infrastructure. AWS describes AgentCore Runtime as a way to securely deploy and scale dynamic AI agents and tools using supported frameworks and protocols in the [AgentCore Runtime guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html).

## How It Works
You package the agent, deploy it to Runtime, and invoke it through the generated runtime endpoint. Runtime handles the agent execution environment while the agent code still owns the reasoning loop, model calls, and tool decisions.

### Architecture Core
- **MicroVM isolation**: each session runs in an independent MicroVM — CPU, memory, and filesystem are completely separated between sessions and users
- **Serverless scaling**: auto-scales with traffic; no infrastructure management
- **Container-based**: Docker → ECR → CodeBuild (ARM64) → Runtime auto-deploy pipeline
- **Observability built-in**: CloudWatch Logs + X-Ray tracing configured automatically

### Deployment (3 steps, all patterns)
1. **Configure** — Dockerfile (auto-generated), IAM role, ECR repo, protocol (HTTP or MCP), auth
2. **Launch** — CodeBuild ARM64 build → ECR push → Runtime creation → endpoint activation
3. **Invoke** — SDK / boto3 / HTTP with session ID for state management

## Protocol Choice: HTTP Agent vs MCP Server

| Question | Answer → Protocol |
|----------|-------------------|
| Building an agent that processes user requests and generates responses? | **HTTP Agent** |
| Providing reusable tools to other agents? | **MCP Server** |

### HTTP Agent (Tutorial 01)
```python
from bedrock_agentcore.runtime import BedrockAgentCoreApp

app = BedrockAgentCoreApp()
agent = Agent(model=BedrockModel(...), tools=[...])

@app.entrypoint  # only addition needed
def my_agent(payload):
    return agent(payload["prompt"])

app.run()  # serves /invocations on port 8080
```

### MCP Server (Tutorial 02, 03)
```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(host="0.0.0.0",
              stateless_http=True)  # required for AgentCore

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    return a + b

mcp.run(transport="streamable-http")
# deploy with configure(protocol="MCP")
```

**`stateless_http=True` is required when deploying MCP servers to AgentCore Runtime.**

## Authentication

| Inbound auth | When to use |
|---|---|
| **OAuth / Cognito JWT** | External users, cross-account, B2C, partner APIs |
| **IAM / SigV4** | Internal AWS services, same-account backends (simpler, no Cognito needed) |

## Response Patterns

### Synchronous (default)
```python
@app.entrypoint
def my_agent(payload):
    return agent(payload["prompt"])  # full response at once
```
Use for: short responses, API integrations, simple Q&A.

### Streaming SSE (Tutorial 04)
```python
@app.entrypoint
async def my_agent(payload):
    async for event in agent.stream_async(payload["prompt"]):
        yield event["data"]  # auto-converted to SSE
```
- `async def` + `yield` = automatic SSE streaming
- `Content-Type: text/event-stream`
- Use for: long content generation, real-time chat UX, multi-step reasoning display

### Large Payload / Multimodal (Tutorial 06)
```python
@app.entrypoint
def processor(payload, ctx):
    excel = b64decode(payload["excel_data"])
    image = b64decode(payload["image_data"])
    return agent([doc, img, text])
```
- Up to **100MB** payload supported
- Binary data transmitted as Base64
- For >100MB: use S3 presigned URL pattern instead

## Session Management (Tutorial 05)

| Strategy | How | When |
|---|---|---|
| **Stateless** | New `session_id` each call → new MicroVM | One-shot tasks, API-style calls |
| **Stateful** | Same `session_id` reused → same MicroVM retained | Multi-turn conversation, context persistence |

### Session Lifecycle Tuning
- **Idle timeout**: default 15 min, range 5 min – 8 hours
- **Max session lifetime**: 8 hours
- **Manual termination**: `stop_runtime_session()` API
- **Cost**: Stateful idle MicroVM incurs cost; tuning timeout saves 30–50%

For permanent state across sessions → use [AgentCore Memory](02_memory.md).

## Workload Decision Matrix

| Workload | Protocol | Auth | Response | Session | Payload |
|---|---|---|---|---|---|
| Customer-facing chatbot | HTTP | OAuth | Streaming | Stateful | Standard |
| Internal data analysis agent | HTTP | IAM | Sync | Stateless | Large |
| Shared internal tool service | MCP | IAM | Sync | Stateless | Standard |
| Partner API tool provider | MCP | OAuth | Sync | Stateless | Standard |
| Real-time report generation | HTTP | IAM | Streaming | Stateful | Large |
| One-shot image/Excel analysis | HTTP | IAM | Sync | Stateless | Large |
| Multi-agent orchestration | MCP+HTTP | IAM | Streaming | Stateful | Standard |

## Key Points

- Use Runtime when the agent needs managed production hosting instead of a local process or generic script runner.
- Keep framework code separate from Runtime concerns: the framework decides how the agent reasons, while Runtime hosts and invokes the agent.
- Add [AgentCore Observability](07_observability.md) early so runtime failures, tool calls, and latency can be traced after deployment.
- Use [AgentCore Identity](04_identity.md), [AgentCore Gateway](03_gateway.md), and [AgentCore Policy](09_policy.md) when the runtime needs governed access to external systems.
- Prototype in a notebook; production deploys via CI/CD + IaC (CDK/CloudFormation).

## Example
An agent built with [Strands Agents SDK](../11_strands_agents_sdk.md) can run locally during development, then be deployed to Runtime so application code calls a managed endpoint instead of a local process:

```python
# Local development
agentcore dev

# Deploy
agentcore deploy

# Invoke
agentcore invoke --runtime MyAgent "Summarize today's incidents"
```

## Why It Matters
Runtime is the compute anchor for AgentCore. Without it, Memory, Gateway, Identity, Observability, Evaluations, Code Interpreter, Browser, and Policy are supporting capabilities around agent execution rather than a complete production agent platform.

---
↑ [Overview](./00_agentcore_overview.md)

**Related:** [AgentCore Services Overview](./00_agentcore_overview.md), [AgentCore Memory](02_memory.md), [AgentCore Observability](07_observability.md), [AgentCore Identity](04_identity.md), [AgentCore Gateway](03_gateway.md), [AgentCore Policy](09_policy.md), [Strands Agents SDK](../11_strands_agents_sdk.md)
**Tags:** #ai #aws #ml #serverless
