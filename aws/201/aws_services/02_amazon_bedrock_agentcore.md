# Amazon Bedrock AgentCore

## Official Documentation
- [AgentCore Developer Guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html)
- [AgentCore Product Page](https://aws.amazon.com/bedrock/agentcore/)
- [AgentCore FAQs](https://aws.amazon.com/bedrock/agentcore/faqs/)
- [Intro Blog Post](https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-agentcore-securely-deploy-and-operate-ai-agents-at-any-scale/)
- [Getting Started with Starter Toolkit](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/getting-started-starter-toolkit.html)

## What It Is
Amazon Bedrock AgentCore is a managed platform for deploying, scaling, and operating AI agents in production — without managing infrastructure.

**The problem it solves:**
- You built an agent with Strands, LangGraph, or your own code — it works on your laptop
- Now you need to run it in production: scaling, security, identity, memory, monitoring
- AgentCore provides all of that as composable managed services

**Think of it as:**
```
Your agent code (Strands, LangGraph, custom)
        ↓
AgentCore = serverless runtime + memory + gateway + identity + observability
        ↓
Production-ready agent at scale
```

**Framework-agnostic:** AgentCore doesn't care what framework you used to build the agent. It runs anything that runs in Python (or containers).

### Where AgentCore Fits

| Layer | What | Example |
|---|---|---|
| **Model** | The LLM | Claude, Nova, GPT via Bedrock |
| **Framework** | Agent logic | Strands, LangGraph, CrewAI, custom |
| **Infrastructure** | **AgentCore** | Runtime, Memory, Gateway, Identity, Observability |

---

## Key Concepts

### The 7 Services

AgentCore is composable — use any combination of these services:

| Service | What it does |
|---|---|
| **Runtime** | Serverless execution environment for agents |
| **Memory** | Persistent context across sessions |
| **Gateway** | Secure, controlled access to tools and APIs |
| **Identity** | Agent-to-service authentication |
| **Observability** | Tracing, debugging, monitoring |
| **Code Interpreter** | Sandboxed code execution |
| **Browser** | Web browsing capability for agents |

### Runtime
The core hosting service. Deploys your agent as a serverless endpoint.

**Key features:**
- Serverless — no instances to manage
- Fast cold starts for real-time interactions
- Up to 8-hour execution windows for long-running agents
- Complete session isolation (each invocation runs in its own sandbox)
- Supports Agent-to-Agent (A2A) protocol
- Works with any Python agent framework

**Deployment flow:**
```
Write agent code → Package with starter toolkit → Deploy to AgentCore Runtime → Invoke via API
```

**Starter toolkit** — CLI tool that packages and deploys your agent:
```bash
pip install bedrock-agentcore-starter-toolkit
agentcore deploy --agent my_agent.py
```

### Memory
Persistent, managed memory for agents across sessions.

**Why it matters:**
- Agents are stateless by default — they forget everything between invocations
- Memory lets agents remember user preferences, past conversations, context
- Managed by AWS — no database to set up

**Memory types:**
- **Semantic memory** — stores facts and knowledge (vector-based retrieval)
- **Episodic memory** — stores past interactions and experiences
- Per-user memory isolation — each user gets their own memory space

### Gateway
Secure access layer between agents and external tools/APIs.

**What it does:**
- Agents need to call APIs, databases, internal services
- Gateway provides authentication, rate limiting, and access control
- Centralized management of tool connections

**Supports:**
- REST APIs
- AWS services
- MCP (Model Context Protocol) servers
- Custom tool endpoints

### Identity
Agent-to-service authentication without embedding credentials.

**The problem:** Your agent needs to call S3, DynamoDB, or external APIs — how does it authenticate?

**Solution:** AgentCore Identity provides:
- Managed credentials for agents
- OAuth 2.0 token management
- Automatic credential rotation
- No secrets in agent code

### Observability
End-to-end visibility into agent execution.

**Provides:**
- Distributed tracing of every model call, tool invocation, and decision
- CloudWatch dashboards for agent metrics
- OpenTelemetry compatible
- Trace across multi-agent systems
- Latency, error rate, token usage metrics

### Code Interpreter
Sandboxed environment for agents to write and execute code safely.

- Agent generates Python code → executes in isolated sandbox
- No risk to your infrastructure
- Useful for data analysis, calculations, file processing
- Available as a built-in tool in Strands: `code_interpreter`

### Browser
Web browsing capability for agents.

- Agent can navigate web pages, extract content, fill forms
- Runs in a managed headless browser
- Available as a built-in tool in Strands: `browser`

---

## AgentCore + Strands: How They Work Together

```
┌─────────────────────────────────────────────┐
│  Your Code (Strands Agent)                  │
│  ┌─────────┐  ┌──────────┐  ┌───────────┐  │
│  │  Model   │  │  Prompt  │  │   Tools   │  │
│  └─────────┘  └──────────┘  └───────────┘  │
└──────────────────┬──────────────────────────┘
                   │ deploy
┌──────────────────▼──────────────────────────┐
│  AgentCore                                  │
│  ┌─────────┐ ┌────────┐ ┌───────┐          │
│  │ Runtime  │ │ Memory │ │Gateway│          │
│  └─────────┘ └────────┘ └───────┘          │
│  ┌──────────┐ ┌─────────────┐ ┌─────────┐  │
│  │ Identity │ │Observability│ │Code Intpr│  │
│  └──────────┘ └─────────────┘ └─────────┘  │
└─────────────────────────────────────────────┘
```

**Typical workflow:**
1. Build agent with Strands SDK locally
2. Test with `agent("your prompt")` on your machine
3. Deploy to AgentCore Runtime with starter toolkit
4. Add Memory for cross-session context
5. Add Gateway for secure tool access
6. Enable Observability for monitoring
7. Invoke via API endpoint

---

## Precautions

### ⚠️ MAIN PRECAUTION: AgentCore Is Infrastructure, Not a Framework
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

### 2. Cost Awareness
- Runtime charges per compute-second
- Memory charges per storage and retrieval
- Gateway charges per request
- Long-running agents (up to 8 hours) can accumulate significant cost
- Monitor with Observability dashboards

### 3. Region Availability
- AgentCore launched in preview (July 2025), GA (October 2025)
- Not available in all regions — check the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/)
- Start development in `us-east-1` or `us-west-2` for broadest availability

### 4. Security
- Use Identity instead of embedding credentials in agent code
- Gateway provides centralized access control — don't let agents call arbitrary endpoints
- Session isolation in Runtime prevents cross-tenant data leaks
- Enable audit logging via Observability

### 5. Start Simple
- Don't enable all 7 services at once
- Start with Runtime + Observability
- Add Memory when you need cross-session context
- Add Gateway when you need secure tool access
- Add Identity when you need agent-to-service auth

## References
- [AgentCore Samples (GitHub)](https://github.com/awslabs/amazon-bedrock-agentcore-samples)
- [Strands + AgentCore Integration](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/using-any-agent-framework.html)
- [AWS Prescriptive Guidance: AgentCore](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/amazon-bedrock-agentcore.html)
