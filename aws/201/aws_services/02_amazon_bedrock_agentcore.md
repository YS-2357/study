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

### Where AgentCore Fits

| Layer | What | Example |
|---|---|---|
| **Model** | The LLM | Claude, Nova, GPT, Gemini, Llama, Mistral via Bedrock or direct |
| **Framework** | Agent logic | Strands, LangGraph, CrewAI, Google ADK, OpenAI Agents SDK, custom |
| **Infrastructure** | **AgentCore** | Runtime, Memory, Gateway, Policy, Identity, Observability, Evaluations, Code Interpreter, Browser |

---

## Key Concepts

### The 9 Services

AgentCore is composable — use any combination of these services:

| Service | What it does |
|---|---|
| **Runtime** | Serverless execution environment for agents |
| **Memory** | Persistent context across sessions |
| **Gateway** | Convert APIs/Lambda into MCP-compatible tools, connect to MCP servers |
| **Policy** | Deterministic control over agent actions using natural language or Cedar |
| **Identity** | Agent-to-service authentication with existing IdPs |
| **Observability** | Tracing, debugging, monitoring via CloudWatch |
| **Evaluations** | Automated agent quality assessment |
| **Code Interpreter** | Sandboxed code execution (Python, JavaScript, TypeScript) |
| **Browser** | Managed headless web browsing for agents |

### Runtime
The core hosting service. Deploys your agent as a serverless endpoint.

**Key features:**
- Serverless — no instances to manage
- Fast cold starts for real-time interactions
- Up to 8-hour execution windows for long-running agents
- Complete session isolation (each invocation runs in its own sandbox)
- Supports Agent-to-Agent (A2A) and MCP protocols
- Works with any Python agent framework
- Supports multi-modal and multi-agent workloads
- Deployable with code upload or containers

**Deployment flow with AgentCore CLI:**
```bash
# Install the CLI (it's an npm package)
npm install -g @aws/agentcore

# Create a new project (interactive wizard or defaults)
agentcore create --name MyAgent --defaults

# Test locally
agentcore dev

# Deploy to AgentCore Runtime
agentcore deploy

# Invoke your deployed agent
agentcore invoke --runtime MyAgent "Hello, what can you do?"
```

### Memory
Persistent, managed memory for agents across sessions.

**Why it matters:**
- Agents are stateless by default — they forget everything between invocations
- Memory lets agents remember user preferences, past conversations, context
- Managed by AWS — no database to set up

**Memory strategies:**
- **SEMANTIC** — stores and retrieves facts/knowledge via vector-based search
- **SUMMARIZATION** — summarizes and stores conversation history
- **USER_PREFERENCE** — learns and stores user preferences over time
- Supports sharing memory stores across agents
- Per-user memory isolation available

### Gateway
Secure access layer that converts existing capabilities into agent-ready tools.

**What it does:**
- Converts APIs and Lambda functions into MCP-compatible tools
- Connects to existing MCP servers
- Enables intelligent tool discovery through semantic search
- Makes tools available to agents through Gateway endpoints with minimal code

**Supports:**
- REST APIs / OpenAPI specs
- AWS Lambda functions
- MCP servers
- Popular integrations (Salesforce, Zoom, JIRA, Slack, etc.)

### Policy
Deterministic control over agent actions with real-time enforcement.

**What it does:**
- Integrates with Gateway to intercept every tool call before execution
- Define which tools agents can access, what actions they can perform, and under what conditions
- Author fine-grained rules using natural language (auto-converts to Cedar) or Cedar directly
- Ensures agents operate within defined boundaries without slowing them down

### Identity
Agent-to-service authentication without embedding credentials.

**The problem:** Your agent needs to call S3, DynamoDB, or external APIs — how does it authenticate?

**Solution:** AgentCore Identity provides:
- Managed credentials for agents
- OAuth 2.0 token management
- Automatic credential rotation
- Compatible with existing identity providers (Amazon Cognito, Okta, Microsoft Azure Entra ID, Auth0, etc.)
- No secrets in agent code

### Observability
End-to-end visibility into agent execution.

**Provides:**
- Distributed tracing of every model call, tool invocation, and decision
- CloudWatch dashboards for agent metrics (token usage, latency, session duration, error rates)
- OpenTelemetry compatible — integrates with existing monitoring tools
- Trace across multi-agent systems
- Issue detection and analysis

### Evaluations
Automated, continuous agent quality assessment.

**What it does:**
- Sample and score live interactions using built-in and custom evaluators
- Measures task execution, edge cases, and output reliability
- Evaluates correctness, helpfulness, safety, and goal success rate
- Supports evaluations on sessions, traces, and spans from Strands or LangGraph
- Results integrated into AgentCore Observability via CloudWatch

### Code Interpreter
Sandboxed environment for agents to write and execute code safely.

- Agent generates code → executes in isolated sandbox
- Supports multiple languages: Python, JavaScript, TypeScript
- No risk to your infrastructure
- Useful for data analysis, calculations, file processing, visualizations

### Browser
Managed headless web browsing for agents.

- Agent can navigate web pages, extract content, fill forms
- Runs in a managed headless browser with reduced CAPTCHA interruptions
- Auto-scales from zero to hundreds of sessions
- Compatible with Playwright and BrowserUse frameworks

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
│  ┌─────────┐ ┌────────┐ ┌───────┐ ┌──────┐ │
│  │ Runtime  │ │ Memory │ │Gateway│ │Policy│ │
│  └─────────┘ └────────┘ └───────┘ └──────┘ │
│  ┌──────────┐ ┌─────────────┐ ┌───────────┐│
│  │ Identity │ │Observability│ │Evaluations││
│  └──────────┘ └─────────────┘ └───────────┘│
│  ┌───────────────┐ ┌─────────┐              │
│  │Code Interpreter│ │ Browser │              │
│  └───────────────┘ └─────────┘              │
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
- Consumption-based pricing, no upfront commitments or minimum fees

### 3. Region Availability
- Check the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/) for current availability
- Start development in `us-east-1` or `us-west-2` for broadest availability

### 4. Security
- Use Identity instead of embedding credentials in agent code
- Gateway + Policy provides centralized access control — don't let agents call arbitrary endpoints
- Session isolation in Runtime prevents cross-tenant data leaks
- Enable audit logging via Observability
- Supports VPC connectivity and AWS PrivateLink

### 5. Start Simple
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
