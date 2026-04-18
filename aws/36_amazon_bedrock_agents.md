---
tags:
  - ai
  - aws
  - ml
created_at: 2026-04-17T14:18:47
updated_at: 2026-04-17T14:18:47
recent_editor: CLAUDE
---

↑ [Overview](./00_aws_overview.md)

# Amazon Bedrock Agents

## What It Is

Amazon Bedrock Agents is a managed, low-code agent builder that orchestrates multi-step tasks by combining foundation models with action groups and [knowledge bases](35_amazon_bedrock_knowledge_bases.md) — configured through the console or API, no custom orchestration code required.

## How It Works

### Core Components

```
User request
    ↓
┌──────────────────────────────────┐
│  Bedrock Agent                   │
│  ┌────────────┐ ┌─────────────┐ │
│  │ Instruction│ │    Model    │ │
│  └────────────┘ └─────────────┘ │
│  ┌────────────┐ ┌─────────────┐ │
│  │Action Groups│ │Knowledge   │ │
│  │(Lambda/API) │ │Bases (RAG) │ │
│  └────────────┘ └─────────────┘ │
│  ┌────────────┐                  │
│  │ Guardrails │                  │
│  └────────────┘                  │
└──────────────────────────────────┘
    ↓
Response (with trace showing reasoning)
```

| Component | What it does |
|---|---|
| **Instruction** | System prompt that defines the agent's role and behavior |
| **Model** | The foundation model that reasons and decides (via [Bedrock](34_amazon_bedrock.md)) |
| **Action groups** | Functions the agent can call — backed by Lambda, API schemas, or return-of-control |
| **Knowledge bases** | [RAG data sources](35_amazon_bedrock_knowledge_bases.md) the agent can query |
| **[Guardrails](33_amazon_bedrock_guardrails.md)** | Input/output filtering attached to the agent |

### Action Groups

Action groups define what the agent can *do*. Three execution modes:

| Mode | How it works | When to use |
|---|---|---|
| **Lambda** | Agent calls a Lambda function you define | Custom business logic |
| **API schema** | Agent calls an API endpoint you describe via OpenAPI spec | Existing REST APIs |
| **Return of control** | Agent returns the action to your app, you execute it and send results back | Client-side execution, human-in-the-loop |

Each action group has a description the model uses to decide when to invoke it. The model extracts parameters from the conversation and passes them to the action.

### Orchestration Flow

1. User sends a message
2. Model reads the instruction and available action groups / knowledge bases
3. Model decides: answer directly, call an action group, or query a knowledge base
4. If an action is called → execute → feed result back to model
5. Model may chain multiple actions before responding
6. Final response returned to user

The agent handles the [agentic loop](../../../ai/01_agent.md) automatically — you don't write the orchestration logic.

### Agent Versioning and Aliases

- **Draft version** — mutable, for development and testing
- **Numbered versions** — immutable snapshots for production
- **Aliases** — named pointers (e.g., `prod`, `staging`) that map to a version
- Update an alias to point to a new version for zero-downtime deployments

### Multi-Agent Collaboration

Bedrock Agents supports supervisor-worker patterns:

- A **supervisor agent** receives the user request and delegates to **sub-agents**
- Each sub-agent has its own instruction, action groups, and knowledge bases
- The supervisor orchestrates the flow and combines results
- Useful for complex workflows spanning multiple domains

## Example

Building a support agent in the console:

1. Create agent → set instruction: "You are a customer support assistant. Use the knowledge base to answer product questions. Use the create-ticket action when the customer needs escalation."
2. Attach a [knowledge base](35_amazon_bedrock_knowledge_bases.md) with your support articles
3. Create an action group `create-ticket` backed by a Lambda that writes to your ticketing system
4. Attach a [guardrail](33_amazon_bedrock_guardrails.md) to filter PII and block off-topic requests
5. Test in the console playground — the trace shows each reasoning step

User: "My order #12345 hasn't arrived and it's been 2 weeks."

Agent trace:
```
Thought: Customer has a delivery issue. Let me check the knowledge base for shipping policies.
Action: Query knowledge base → retrieves shipping policy article
Thought: Policy says orders over 10 days should be escalated. Let me create a ticket.
Action: create-ticket(order_id="12345", issue="delayed_delivery")
Response: "I've created support ticket #T-789 for your delayed order #12345.
           Per our shipping policy, orders delayed beyond 10 days are prioritized
           for investigation. A support specialist will contact you within 24 hours."
```

## Why It Matters

Bedrock Agents is the fastest path to a working agent on AWS — no orchestration code, no infrastructure management. For teams that need custom orchestration logic or framework flexibility, [Strands Agents SDK](31_strands_agents_sdk.md) with [AgentCore](32_amazon_bedrock_agentcore.md) is the alternative. Understanding where each option fits prevents over-engineering simple use cases or under-engineering complex ones.

### When to Use What

| Need | Use |
|---|---|
| Quick agent, minimal code, console-driven | **Bedrock Agents** |
| Custom orchestration, full code control, any model | **[Strands Agents SDK](31_strands_agents_sdk.md)** |
| Production deployment at scale for any framework | **[AgentCore](32_amazon_bedrock_agentcore.md)** |
| All three together | Strands for code → AgentCore for infra (Bedrock Agents is separate) |

## Precautions

### MAIN PRECAUTION: Less Flexibility Than Code-Based Frameworks
- Orchestration logic is managed by AWS — you can't customize the reasoning loop
- If you need conditional branching, custom retry logic, or non-standard tool patterns, use [Strands](31_strands_agents_sdk.md) instead
- Bedrock Agents is best for straightforward action + knowledge base patterns

### 1. Action Group Design
- Each action group needs a clear, distinct description — vague descriptions confuse the model
- Keep action groups focused (one responsibility each)
- Test that the model selects the right action group for edge-case inputs

### 2. Lambda Cold Starts
- Lambda-backed action groups are subject to cold start latency
- For latency-sensitive agents, use provisioned concurrency on critical Lambdas
- Consider API-schema action groups for external services to avoid Lambda overhead

### 3. Session Management
- Sessions expire after a configurable idle timeout (default 30 minutes)
- Session state is not persisted across sessions by default
- For cross-session memory, integrate with [AgentCore Memory](32_amazon_bedrock_agentcore.md) or your own storage

### 4. Cost Layers
- Model inference tokens (per the [Bedrock](34_amazon_bedrock.md) model you choose)
- Lambda invocations for action groups
- Knowledge Base retrieval and vector store costs
- Guardrails assessment charges
- Multi-step agents multiply all of these per reasoning step

---
← Previous: [Amazon Bedrock Knowledge Bases](35_amazon_bedrock_knowledge_bases.md) | [Overview](./00_aws_overview.md) | Next: [AWS CDK](37_aws_cdk.md) →
