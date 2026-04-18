---
tags:
  - aws
  - monitoring
created_at: 2026-04-17T14:18:47
updated_at: 2026-04-18T13:00:00
recent_editor: CLAUDE
---

↑ [Overview](./00_aws_overview.md)

# Amazon CloudWatch

## What It Is

Amazon CloudWatch is AWS's monitoring and observability service. It collects logs, metrics, and traces from your AWS resources so you can see what's happening, set alarms, and debug problems.

## Analogy

A dashboard camera for your AWS infrastructure. It records everything — how much CPU your Fargate task uses, what your Lambda logged, when an error happened. You can replay events, set alerts for anomalies, and figure out what went wrong after the fact.

## How It Works

### Three Core Features

| Feature | What it does | Your project use |
|---|---|---|
| **Metrics** | Numeric measurements over time (CPU, memory, request count) | Monitor Fargate health, Bedrock latency |
| **Logs** | Text output from your services | FastAPI logs, agent reasoning traces, errors |
| **Alarms** | Trigger actions when a metric crosses a threshold | Alert if error rate spikes or costs exceed budget |

### Who Does What

| What | Where | You configure? |
|---|---|---|
| Built-in metrics (CPU, latency, token count) | AWS sends automatically | No — just open CloudWatch and look |
| Custom metrics (draft time, approval rate) | Your application code (`put_metric_data`) | Yes |
| Fargate logs | Log driver (`awslogs`) in CDK | Yes — L3 pattern does it for you |
| Lambda / Bedrock logs | Automatic | No |
| Alarms | CloudWatch console or CDK | Yes |
| Dashboards | CloudWatch console or CDK | Yes |

### Metrics

Every AWS service automatically sends metrics to CloudWatch. You don't configure this — it just happens.

**Built-in metrics (automatic, no setup):**

| Service | Metrics |
|---|---|
| Fargate/ECS | CPUUtilization, MemoryUtilization, RunningTaskCount |
| ALB | RequestCount, TargetResponseTime, HTTPCode_2XX/4XX/5XX |
| Bedrock | InvocationCount, InvocationLatency, InputTokenCount, OutputTokenCount, InvocationThrottles |
| OpenSearch Serverless | SearchOCU, IndexingOCU, SearchableDocuments |
| S3 | BucketSizeBytes, NumberOfObjects |
| Lambda | Invocations, Duration, Errors, Throttles, ConcurrentExecutions |
| Knowledge Bases | RetrieveLatency, RetrieveCount |

**Custom metrics (you send from your code):**

| Metric | Why |
|---|---|
| DraftGenerationTime | End-to-end time from inquiry to draft |
| RetrievedArticleCount | How many articles the agent used |
| ReviewerApprovalRate | % of drafts approved vs rejected |
| PIIDetectionCount | How often Guardrails catches PII |
| TokenCostPerRequest | Estimated cost per inquiry |

```python
import boto3

cw = boto3.client("cloudwatch")
cw.put_metric_data(
    Namespace="CsAiAssistant",
    MetricData=[{
        "MetricName": "DraftGenerationTime",
        "Value": 2.3,
        "Unit": "Seconds"
    }]
)
```

- `Namespace` — groups your custom metrics together, separate from AWS built-in ones
- `put_metric_data` costs $0.30 per 1,000 custom metrics/month (first 10 free)

### Logs

Services send log output to **Log Groups**. Each log group contains **Log Streams**.

```
Log Group: /ecs/cs-ai-backend          ← your Fargate task
  └── Log Stream: task-abc123          ← one container instance
        "2026-04-03 INFO: Received inquiry"
        "2026-04-03 INFO: Retrieved 5 articles"
        "2026-04-03 ERROR: Bedrock timeout"
```

For your FastAPI backend, anything you `print()` or log goes here automatically when running on Fargate (with the `awslogs` log driver).

**Log Insights** — query your logs with SQL-like syntax:

```
fields @timestamp, @message
| filter @message like /ERROR/
| sort @timestamp desc
| limit 20
```

### Alarms

Watch a metric and trigger an action when it crosses a threshold.

```
Metric: Bedrock InvocationLatency > 10 seconds for 5 minutes
  → Action: Send SNS notification to your email
```

Useful alarms for your project:

| Alarm | Why |
|---|---|
| Fargate CPU > 80% | Backend is overloaded |
| Bedrock 5XX errors > 0 | Model calls failing |
| ALB 5XX count > 10/min | Backend returning errors to frontend |
| Estimated charges > $50 | Cost control (your assignment says 최대한 저렴하게) |

### Dashboards

Custom visual dashboards combining metrics from multiple services on one screen. You can create one for your POC showing Bedrock latency, Fargate health, and error rates together.

## Example

Your CS agent flow with CloudWatch:

```
CS staff sends inquiry
    ↓
FastAPI logs: "Received inquiry: 배송 문의"     → CloudWatch Logs
    ↓
Knowledge Base retrieval: 230ms                 → CloudWatch Metrics (custom)
    ↓
Bedrock call: 1.8s, 500 input tokens           → CloudWatch Metrics (automatic)
    ↓
FastAPI logs: "Draft generated, 3 citations"    → CloudWatch Logs
    ↓
If Bedrock latency > 10s for 5 min             → CloudWatch Alarm → email
```

### What CloudWatch Doesn't Cover

CloudWatch monitors almost all AWS services, but some things need other tools:

| Gap | What to use instead |
|---|---|
| Application-level tracing (which function called which) | **AWS X-Ray** or AgentCore Observability |
| Cost breakdown by service | **AWS Cost Explorer** / **Budgets** |
| Security audit (who did what API call) | **CloudTrail** |
| Resource inventory (what exists in my account) | **AWS Config** |
| Code-level debugging | Your IDE / local logs |

For your project: CloudWatch + AgentCore Observability covers 95%. CloudTrail is nice-to-have for auditing ("who approved which draft").

## Why It Matters

Without CloudWatch, you're blind. When the agent returns a bad draft or times out, you need logs to see what happened — which articles were retrieved, what the model received, where it failed. For your POC demo, being able to show monitoring proves the system is production-aware.

## Precautions

### MAIN PRECAUTION: Logs Cost Money and Never Auto-Delete
- CloudWatch Logs are retained forever by default
- Set a retention period (e.g., 7 or 30 days) to avoid growing costs
- In CDK: `log_group.retention = logs.RetentionDays.ONE_WEEK`

### 1. Billing Alarm First
- Create a billing alarm before deploying anything else
- Catches runaway costs from OpenSearch, Fargate, or Bedrock early

### 2. Log Levels
- Don't log everything at DEBUG in production — high volume = high cost
- Use INFO for normal flow, ERROR for failures, DEBUG only in dev

### 3. AgentCore Has Its Own Observability
- AgentCore Observability traces model calls and tool use automatically
- It feeds into CloudWatch — they complement each other, not replace

---
← Previous: [AWS CDK](37_aws_cdk.md) | [Overview](./00_aws_overview.md) | Next: [AWS Lambda](07_aws_lambda.md) →
