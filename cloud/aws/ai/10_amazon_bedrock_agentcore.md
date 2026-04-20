---
tags:
  - ai
  - aws
  - ml
created_at: 2026-04-17T14:18:47
updated_at: 2026-04-19T09:11:51
recent_editor: CLAUDE
---

↑ [Overview](./00_ai_overview.md)

# Amazon Bedrock AgentCore

## Official Documentation
- [AgentCore Developer Guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html)
- [AgentCore Product Page](https://aws.amazon.com/bedrock/agentcore/)
- [AgentCore FAQs](https://aws.amazon.com/bedrock/agentcore/faqs/)
- [Intro Blog Post](https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-agentcore-securely-deploy-and-operate-ai-agents-at-any-scale/)
- [Getting Started with AgentCore CLI](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-get-started-toolkit.html)
- [AgentCore CLI GitHub](https://github.com/aws/agentcore-cli)

## What It Is
Amazon Bedrock AgentCore is a managed platform for deploying, scaling, and operating AI agents in production — without managing infrastructure.

**The problem it solves:**
- You built an agent with Strands, LangGraph, or your own code — it works on your laptop
- Now you need to run it in production: scaling, security, identity, memory, monitoring
- AgentCore provides all of that as composable managed services

**Think of it as:**
```
Your agent code (Strands, LangGraph, CrewAI, Google ADK, OpenAI Agents SDK, custom)
        ↓
AgentCore = serverless runtime + memory + gateway + policy + identity + observability + evaluations
        ↓
Production-ready agent at scale
```

**Framework-agnostic:** AgentCore doesn't care what framework you used to build the agent. It works with any open-source framework including CrewAI, LangGraph, LlamaIndex, Google ADK, OpenAI Agents SDK, and Strands Agents, and with any foundation model.

## How It Works
You build the agent logic in your framework of choice, then deploy that code into AgentCore Runtime. AgentCore adds the managed runtime and optional services around it, such as Memory, Gateway, Policy, Identity, Observability, and Evaluations.

## Example
```bash
# Local development
agentcore dev

# Deploy the agent runtime
agentcore deploy

# Invoke the deployed agent
agentcore invoke --runtime MyAgent "Summarize today's incidents"
```

## Why It Matters
AgentCore is the layer that turns custom agent code into production infrastructure. That is why replacing it with Lambda changes the architecture: Lambda is generic compute, while AgentCore is managed agent operations with agent-native services around the runtime.

### Where AgentCore Fits

| Layer | What | Example |
|---|---|---|
| **Model** | The LLM | Claude, Nova, GPT, Gemini, Llama, Mistral via Bedrock or direct |
| **Framework** | Agent logic | Strands, LangGraph, CrewAI, Google ADK, OpenAI Agents SDK, custom |
| **Infrastructure** | **AgentCore** | Runtime, Memory, Gateway, Policy, Identity, Observability, Evaluations, Code Interpreter, Browser |

## Key Concepts

### The 9 Services

AgentCore is composable — use any combination of these services:

| Service | What it does |
|---|---|
| [Runtime](agentcore/01_runtime.md) | Serverless execution environment for agents |
| [Memory](agentcore/02_memory.md) | Persistent context across sessions |
| [Gateway](agentcore/03_gateway.md) | Convert APIs and Lambda functions into agent tools |
| [Identity](agentcore/04_identity.md) | Agent-to-service authentication with existing identity providers |
| [Code Interpreter](agentcore/05_code_interpreter.md) | Sandboxed code execution for generated code |
| [Browser](agentcore/06_browser.md) | Managed browser automation for agents |
| [Observability](agentcore/07_observability.md) | Tracing, debugging, and monitoring through CloudWatch |
| [Evaluations](agentcore/08_evaluations.md) | Automated agent quality assessment |
| [Policy](agentcore/09_policy.md) | Deterministic control over agent actions |

Use [AgentCore services and capabilities](agentcore/00_agentcore_overview.md) as the canonical split-out notes for these services and capabilities.

## AgentCore + Strands: How They Work Together

```
┌─────────────────────────────────────────────┐
│  Your Code (Strands Agent)                  │
│  ┌─────────┐  ┌──────────┐  ┌───────────┐   │
│  │  Model  │  │  Prompt  │  │   Tools   │   │
│  └─────────┘  └──────────┘  └───────────┘   │
└──────────────────┬──────────────────────────┘
                   │ deploy
┌──────────────────▼──────────────────────────┐
│  AgentCore                                  │
│  ┌─────────┐ ┌────────┐ ┌───────┐ ┌──────┐  │
│  │ Runtime │ │ Memory │ │Gateway│ │Policy│  │
│  └─────────┘ └────────┘ └───────┘ └──────┘  │
│  ┌──────────┐ ┌─────────────┐ ┌───────────┐ │
│  │ Identity │ │Observability│ │Evaluations│ │
│  └──────────┘ └─────────────┘ └───────────┘ │
│  ┌────────────────┐ ┌─────────┐             │
│  │Code Interpreter│ │ Browser │             │
│  └────────────────┘ └─────────┘             │
└─────────────────────────────────────────────┘
```

**Typical workflow:**
1. Build agent with Strands SDK locally
2. Test with `agentcore dev` on your machine
3. Deploy to AgentCore Runtime with `agentcore deploy`
4. Add Memory for cross-session context
5. Add Gateway for secure tool access
6. Add Policy for deterministic guardrails
7. Enable Observability and Evaluations for monitoring
8. Invoke via API endpoint or `agentcore invoke`

## Precautions

### MAIN PRECAUTION: AgentCore Is Infrastructure, Not a Framework
- AgentCore does NOT build your agent logic — that's Strands/LangGraph/your code
- AgentCore runs, scales, and secures your agent
- Don't confuse it with Bedrock Agents (the managed no-code agent builder)

### 1. Three Different "Agent" Services — Know the Difference

| Service | What it is | When to use |
|---|---|---|
| **Bedrock Agents** | Managed, console-based agent builder | Quick setup, no custom code, action groups via Lambda |
| **Strands Agents SDK** | Open-source code framework | Custom agent logic, full control, any model |
| **Bedrock AgentCore** | Production infrastructure | Deploy any agent at scale with security/observability |

They are evolutionary layers, not competitors:
- Bedrock Agents = easiest, least flexible
- Strands = most flexible code framework
- AgentCore = production infrastructure for any framework

### 2. EC2 vs Lambda vs AgentCore — Why They Aren't Interchangeable

All three can host an agent. Only AgentCore bundles the services an agent typically needs. EC2 and Lambda give you compute only — anything agent-specific, you build yourself.

|  | EC2 | Lambda | AgentCore |
|---|---|---|---|
| **Type** | Virtual machine | Function | Managed agent platform |
| **Max single session** | Unlimited | 15 min | 8 h |
| **State between calls** | You build it | None (stateless) | Memory service |
| **Scaling** | Manual / ASG | Automatic | Automatic |
| **Billing** | Instance-hour | Per invocation + duration | Compute-second |
| **Cold starts** | None (always on) | Yes | Minimal |
| **Agent-native services** | None | None | Memory, Gateway, Identity, Policy, Observability, Evaluations, Code Interpreter, Browser |
| **Best fit** | Steady 24/7, GPU, custom networking | Short tool backends, bursty / event-driven | Production agents needing memory + governance |

**Why AI flattens these together:**
- AgentCore Runtime and Lambda both look like "serverless compute"; EC2 looks like "just give the agent a VM." Written vaguely, an architecture goal lets an AI treat any of the three as interchangeable compute.
- The [Strands Agents SDK note](./11_strands_agents_sdk.md) correctly lists AgentCore / Lambda / Fargate / EC2 / EKS / App Runner as deployment targets — so an AI may overgeneralize that "any target works" even when the system was intentionally designed around AgentCore features.
- [Bedrock Agents](./04_amazon_bedrock_agents.md) commonly uses Lambda-backed action groups, which makes "agent on AWS" and "Lambda" look tightly coupled even though Bedrock Agents, Strands, and AgentCore are separate layers.
- The [AgentCore developer guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) positions AgentCore as managed infrastructure for deploying and operating agents, not as a generic function host. Neither Lambda nor EC2 automatically replaces AgentCore Memory, Gateway, Policy, Identity, Observability, Evaluations, Code Interpreter, or Browser.

**Rule of thumb:**
- Agent needs memory, long sessions, managed tool access, or monitoring → **AgentCore** as the primary runtime.
- A short tool the agent calls (e.g., "create ticket", "query DB") → **Lambda** as an action backend.
- Full control, steady 24/7 workload, GPU, or custom networking → **EC2**.

### 3. Cost Awareness
- Runtime charges per compute-second
- Memory charges per storage and retrieval
- Gateway charges per request
- Long-running agents (up to 8 hours) can accumulate significant cost
- Monitor with Observability dashboards
- Consumption-based pricing, no upfront commitments or minimum fees

### 4. Region Availability
- Check the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/) for current availability
- Start development in `us-east-1` or `us-west-2` for broadest availability

### 5. Security
- Use Identity instead of embedding credentials in agent code
- Gateway + Policy provides centralized access control — don't let agents call arbitrary endpoints
- Session isolation in Runtime prevents cross-tenant data leaks
- Enable audit logging via Observability
- Supports VPC connectivity and AWS PrivateLink

### 6. Start Simple
- Don't enable all 9 services at once
- Start with Runtime + Observability
- Add Memory when you need cross-session context
- Add Gateway when you need secure tool access
- Add Policy when you need deterministic guardrails
- Add Evaluations when you need quality monitoring
- Add Identity when you need agent-to-service auth

## References
- [AgentCore Samples (GitHub)](https://github.com/awslabs/amazon-bedrock-agentcore-samples)
- [AgentCore CLI (GitHub)](https://github.com/aws/agentcore-cli)
- [Strands + AgentCore Integration](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/using-any-agent-framework.html)
- [AWS Prescriptive Guidance: AgentCore](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/amazon-bedrock-agentcore.html)

---
↑ [Overview](./00_ai_overview.md)

**Related:** [Amazon Bedrock Custom Models](./09_amazon_bedrock_custom_models.md), [Strands Agents SDK](./11_strands_agents_sdk.md), [Runtime](agentcore/01_runtime.md), [Memory](agentcore/02_memory.md), [Gateway](agentcore/03_gateway.md), [Identity](agentcore/04_identity.md), [Code Interpreter](agentcore/05_code_interpreter.md), [Browser](agentcore/06_browser.md), [Observability](agentcore/07_observability.md), [Evaluations](agentcore/08_evaluations.md), [Policy](agentcore/09_policy.md), [Bedrock Agents](./04_amazon_bedrock_agents.md)
**Tags:** #ai #aws #ml
