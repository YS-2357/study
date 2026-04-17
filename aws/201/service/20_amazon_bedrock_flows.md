---
tags:
  - ai
  - aws
  - ml
created_at: 260417-141847
updated_at: 260417-141847
---

# Amazon Bedrock Flows

## What It Is

Amazon Bedrock Flows is a visual workflow builder that lets you chain prompts, [knowledge bases](05_amazon_bedrock_knowledge_bases.md), [agents](06_amazon_bedrock_agents.md), and Lambda functions into a multi-step pipeline — without writing orchestration code.

Where [Bedrock Agents](06_amazon_bedrock_agents.md) lets an LLM decide its own next step at runtime, Flows defines the sequence upfront as a fixed graph. The path is deterministic; the model fills in the outputs at each node.

## Analogy

A flowchart that executes itself. You draw the boxes and arrows in the console — "if the sentiment is negative, go to this node; otherwise go to that one." When a user triggers the flow, each box runs in order and passes its output to the next.

## How It Works

A flow is a directed acyclic graph (DAG) of nodes:

| Node type | What it does |
|---|---|
| **Input** | Entry point — receives the initial payload |
| **Output** | Exit point — returns the final result |
| **Prompt** | Calls a foundation model with a prompt template |
| **Knowledge base** | Queries a [Bedrock Knowledge Base](05_amazon_bedrock_knowledge_bases.md) |
| **Agent** | Invokes a [Bedrock Agent](06_amazon_bedrock_agents.md) |
| **Lambda** | Calls an AWS Lambda function for custom logic |
| **Condition** | Routes to different branches based on a rule |
| **Iterator** | Loops over a list, running downstream nodes once per item |
| **Collector** | Gathers iterator outputs back into a single list |

You connect nodes in the visual canvas. Data flows through edges as variables that downstream nodes can reference.

### Aliases and Versions

Like Bedrock Agents, Flows supports versioning:
- **Draft** — mutable, used during development
- **Numbered versions** — immutable snapshots
- **Aliases** — named pointers (e.g., `prod`) that map to a version for zero-downtime deploys

## Example

A document triage pipeline:

```
[Input: document text]
        ↓
[Prompt: classify as "complaint", "inquiry", or "feedback"]
        ↓
[Condition: if complaint]──→ [Agent: open support ticket]
          └─ [else]────────→ [Prompt: draft acknowledgement email]
        ↓
[Output: result]
```

Built in the Flows console canvas, invoked via the API:

```python
import boto3

client = boto3.client("bedrock-agent-runtime", region_name="us-east-1")

response = client.invoke_flow(
    flowIdentifier="FLOW_ID",
    flowAliasIdentifier="prod",
    inputs=[{"content": {"document": "My order never arrived."}, "nodeName": "FlowInputNode", "nodeOutputName": "document"}]
)

for event in response["responseStream"]:
    if "flowOutputEvent" in event:
        print(event["flowOutputEvent"]["content"])
```

## Why It Matters

Flows is the right tool when the steps are known in advance and must always execute in the same order. For tasks where the sequence should adapt to context at runtime, [Bedrock Agents](06_amazon_bedrock_agents.md) is more appropriate. Use Flows for pipelines; use Agents for open-ended tasks.

| Perspective | Detail |
|---|---|
| Feasibility | Supports branching, looping, Lambda, agents, and knowledge bases in one graph |
| Disruption | Version + alias pattern enables zero-downtime updates |
| Pros & Cons | Predictable and auditable; less flexible than code-based orchestration |
| Differences | Flows = fixed graph; [Agents](06_amazon_bedrock_agents.md) = LLM decides the path at runtime |

---
← Previous: [Amazon Bedrock Agents](06_amazon_bedrock_agents.md) | [Overview](00_overview.md) | Next: [Bedrock Prompt Management](21_amazon_bedrock_prompt_management.md) →
