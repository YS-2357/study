---
tags:
  - ai
  - aws
  - ml
created_at: 2026-04-18T20:19:44
updated_at: 2026-04-19T09:11:51
recent_editor: CLAUDE
---

↑ [Overview](./00_ai_overview.md)

# Amazon Bedrock Integration Patterns

## What It Is

The Bedrock family is designed to compose — each per-service note explains one piece in isolation, but real systems stack several. This note shows the common stacks: which services you reach for together, and why.

## How It Works

### Composition Axes

Every non-trivial Bedrock system picks one service per concern:

| Concern | Service |
|---|---|
| Model inference | [Bedrock](./01_amazon_bedrock.md) |
| Safety filtering | [Guardrails](./02_amazon_bedrock_guardrails.md) |
| Grounding / RAG | [Knowledge Bases](./03_amazon_bedrock_knowledge_bases.md) |
| Agent orchestration (managed) | [Bedrock Agents](./04_amazon_bedrock_agents.md) |
| Agent orchestration (code) | [Strands Agents SDK](./11_strands_agents_sdk.md) |
| Production runtime | [AgentCore](./10_amazon_bedrock_agentcore.md) |
| Document ingestion | [Data Automation](./08_amazon_bedrock_data_automation.md) |
| Prompt versioning | [Prompt Management](./06_amazon_bedrock_prompt_management.md) |

Model and orchestration are always present. The rest are opt-in layers — add only when the concern is real.

### 2.2. Two Orchestration Paths

Bedrock forces an early fork between managed and custom orchestration:

- **Managed path** — Bedrock Agents. Console-driven, AWS owns the reasoning loop.
- **Custom path** — Strands SDK (or LangGraph, CrewAI, custom) deployed to AgentCore Runtime.

The other services (Guardrails, KB, Data Automation, Prompt Management) attach to either path.

## 3. Example

### 3.1. Pattern A — Managed Support Agent

Console-driven customer support bot, zero infrastructure code.

```
User ──► Bedrock Agents (orchestration)
            ├─► Knowledge Bases   (grounded answers)
            ├─► Lambda action     (create ticket)
            └─► Guardrails        (PII, off-topic filter)
                    └─► Bedrock (Claude)
```

The Bedrock Agents note has a worked trace: the agent queries the knowledge base for policy, calls a Lambda action when escalation is needed, and runs every turn through a guardrail before and after the model call.

When to pick: fast setup, standard FAQ + ticket flow, no custom reasoning loop.

### 3.2. Pattern B — Production Custom Agent

Code-owned agent running under production infrastructure.

```
User ──► AgentCore Runtime (serverless execution)
            ├─► Strands agent
            │      ├─► Bedrock model call
            │      └─► Guardrails (attached to model call)
            ├─► AgentCore Memory        (cross-session context)
            ├─► AgentCore Gateway       (APIs/Lambdas as tools)
            └─► AgentCore Observability (traces)
```

The Strands agent is the *logic*; AgentCore is the *infrastructure*. Around the runtime sit [Memory](./agentcore/02_memory.md) for cross-session context, [Gateway](./agentcore/03_gateway.md) for tool access, and [Observability](./agentcore/07_observability.md) for traces. Guardrails attach at the model call — Strands passes guardrail IDs into each Converse invocation, not at the runtime layer.

When to pick: custom reasoning loops, full code control, cross-session state, agents that outlive a single request.

### 3.3. Pattern C — Document Ingestion (Brief)

Data Automation extracts structured fields from PDFs and images; the output feeds Knowledge Bases for retrieval by either orchestration path above. Use when source material isn't already clean text.

## 4. Why It Matters

The hardest design decision is orchestration path, not individual services. Once managed vs. custom is chosen, the rest is layering:

| Need | Add |
|---|---|
| Factual grounding | Knowledge Bases |
| PII / topic filter | Guardrails |
| Cross-session state | AgentCore Memory (custom path only) |
| Tool APIs without code | AgentCore Gateway (custom path only) |
| Dirty input documents | Data Automation upstream of KB |
| Swap prompts without redeploy | Prompt Management |

Each layer is optional. Adding them all at once is the common mistake — start with model + orchestration, prove the loop, then bolt on the rest.

## 5. Precautions

### MAIN PRECAUTION: Bedrock Agents ≠ AgentCore

These are often confused. Bedrock Agents is a managed builder; AgentCore is production infrastructure for any framework. You don't stack them — you pick one orchestration path. The AgentCore note spells out the distinction against Strands as well.

### 1. Each Layer Has Its Own Cost and Quota

- Model tokens billed per call
- Guardrails billed per evaluated text unit
- KB billed per ingestion and per retrieval
- AgentCore Runtime billed per compute-second
- A composed system bills across all layers simultaneously — monitor each one separately

### 2. Attach Guardrails At The Model Layer

Guardrails evaluate a Bedrock model call — they don't wrap an agent globally. In the managed path, attach the guardrail to the Agent and AWS forwards it to every model call. In the custom path, pass `guardrailConfig` into each Converse call yourself. A missed call leaks unchecked output.

### 3. Memory Is Not A Free Key-Value Store

AgentCore Memory charges for storage and retrieval. Reserve it for context the agent genuinely needs to reason about across sessions; don't use it as a generic database.

---
↑ [Overview](./00_ai_overview.md)

**Related:** [Strands Agents SDK](./11_strands_agents_sdk.md), [Bedrock](./01_amazon_bedrock.md), [Guardrails](./02_amazon_bedrock_guardrails.md), [Knowledge Bases](./03_amazon_bedrock_knowledge_bases.md), [Bedrock Agents](./04_amazon_bedrock_agents.md), [AgentCore](./10_amazon_bedrock_agentcore.md), [Data Automation](./08_amazon_bedrock_data_automation.md), [Prompt Management](./06_amazon_bedrock_prompt_management.md), [Memory](./agentcore/02_memory.md), [Gateway](./agentcore/03_gateway.md), [Observability](./agentcore/07_observability.md)
**Tags:** #ai #aws #ml
