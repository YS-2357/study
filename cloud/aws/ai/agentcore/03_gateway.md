---
tags:
  - ai
  - aws
  - ml
created_at: 2026-04-17T14:18:47
updated_at: 2026-04-23T23:41:19
recent_editor: CODEX
source:
  - agentcore_intro_korean_2026_04
  - agentcore_gateway_intro_2026_04
---

↑ [Overview](./00_agentcore_overview.md)

# AgentCore Gateway

## What It Is
AgentCore Gateway is the Amazon Bedrock AgentCore service for turning existing systems into agent-accessible tools. AWS describes Gateway as a way to connect agents to tools through APIs, Lambda functions, and Model Context Protocol (MCP) servers in the [AgentCore developer guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html).

## Analogy
AgentCore Gateway is like a controlled service desk for tools: agents ask through one desk, and the desk translates requests, checks credentials, and routes them to the right backend.

## How It Works
Gateway sits between the agent and the target system. It exposes selected capabilities as tools, then lets the agent discover and call those tools through the Gateway endpoint instead of directly wiring every backend into the agent.

### Gateway's 6 Roles

| Role | What it does |
|---|---|
| **Security Guard** | Inbound auth (OAuth/IAM) + outbound credential management |
| **Translator** | Lambda/OpenAPI/Smithy → MCP protocol auto-conversion |
| **Composer** | Combines multiple Targets into one Gateway (tool aggregation) |
| **Keychain** | Securely stores API keys, IAM roles, OAuth tokens |
| **Researcher** | Semantic search across 300+ tools to find the right one |
| **Infra Manager** | Serverless deploy, auto-scaling, monitoring built-in |

### Deployment (3 steps)
1. **Create Gateway** — create gateway resource + configure inbound auth
2. **Add Targets** — add Lambda/OpenAPI/Smithy targets + configure outbound auth
3. **Connect Agent** — agent uses MCP client to discover and call tools

## Decision 1: Target Type

Choose based on what form your existing API takes:

| Target | When to use | Zero-code change? |
|---|---|---|
| **Lambda** | Custom business logic, DB queries, complex workflows | No — write Lambda function |
| **OpenAPI** | Existing REST API with OpenAPI/Swagger spec | Yes — spec only |
| **Smithy** | AWS services (S3, DynamoDB) or Smithy IDL-based services | Yes — model only |

```python
# Lambda Target — expose a Lambda as MCP tool
@mcp.tool()
def get_order(order_id: str):
    """Retrieve order by ID."""
    return dynamodb.get_item(Key={"order_id": order_id})

# OpenAPI Target — NASA Mars Weather API example
# openapi_spec: /weather: get: summary: "화성 날씨 조회"
# Gateway auto-maps to MCP tool

# Smithy Target — S3 service operations
# service S3 { operations: [GetObject, PutObject, ListBuckets] }
# Gateway exposes S3 as MCP tools with IAM auth
```

## Decision 2: Inbound Auth (who calls the Gateway)

| Auth | Use when | MCP client |
|---|---|---|
| **OAuth / Cognito JWT** | External users, web/mobile clients, cross-account, B2C | `streamablehttp` (standard MCP) |
| **IAM / SigV4** | Internal AWS services, same-account agent backends, B2B | `streamablehttp_client_with_sigv4` |

OAuth requires Cognito User Pool pre-configuration — manage via IaC (CDK/CloudFormation).

## Decision 3: Outbound Auth (how Gateway calls the Target)

```python
# IAM Role — for AWS services and Lambda (preferred; no key management)
credential_provider = {
    "roleArn": "arn:aws:iam::123456789:role/gateway-role",
    "credentialProviderType": "GATEWAY_IAM_ROLE"
}
# Gateway uses AssumeRole automatically

# API Key — for external third-party APIs (NASA, weather, payment)
credential_provider = {
    "apiKeyCredentialProvider": {
        "apiKey": "secret-stored-in-secrets-manager",
        "credentialProviderType": "API_KEY"
    }
}
# API Key MUST be stored in Secrets Manager — never hardcoded

# OAuth Token — for enterprise SaaS (Salesforce, HubSpot, Google Workspace)
credential_provider = {
    "oauthCredentialProvider": {
        "tokenUrl": "https://...",
        "clientId": "...",
        "credentialProviderType": "OAUTH"
    }
}
# Token lifecycle auto-managed
```

**Least-privilege order: IAM Role > API Key > OAuth Token.**

## Decision 4: Tool Discovery Strategy

| Tools | Strategy | Why |
|---|---|---|
| < 100 | **Full List** | Entire list fits in LLM context |
| 100+ | **Semantic Search** | Reduces prompt context and lookup latency for large tool catalogs |

Semantic Search uses the `x-amz-bedrock-agentcore-search` tool to retrieve relevant tools from a large catalog instead of sending the full list to the model.

## Workload Decision Matrix

| Workload | Target | Inbound | Outbound | Tool Search |
|---|---|---|---|---|
| Internal Lambda → agent tool | Lambda | IAM | IAM Role | Full |
| Customer-facing order management | Lambda | OAuth | IAM Role | Full |
| External API integration (NASA) | OpenAPI | IAM | API Key | Full |
| AWS service direct (S3) | Smithy | IAM | IAM Role | Full |
| SaaS integration (Salesforce) | OpenAPI | OAuth | OAuth | Full |
| Large tool hub (100+) | Lambda | IAM | IAM Role | Search |
| Partner ecosystem tool provider | Lambda | OAuth | IAM Role | Search |

**One Gateway can hold multiple Target types simultaneously (Composer role).**

## AWS Viewpoints

| Perspective | Detail |
|-------------|--------|
| Feasibility | Use Gateway when existing APIs, Lambda functions, or Smithy-modeled services need to become controlled agent tools. |
| Disruption | Gateway can wrap existing APIs with little code change for OpenAPI or Smithy targets, while Lambda targets require explicit function implementation. |
| Pros & Cons | It centralizes tool exposure and credentials, but still requires careful target scoping and authentication design. |
| Differences | Gateway exposes tools to agents; Identity manages who the agent acts as, and Policy controls whether tool calls should be allowed. |

## Key Points

- Use Gateway to make tool access explicit instead of hiding API clients inside the agent code.
- Expose narrow operations rather than broad administrative APIs.
- Combine Gateway with [AgentCore Policy](09_policy.md) so tool calls can be checked before execution.
- Combine Gateway with [AgentCore Identity](04_identity.md) so tools are called with managed credentials instead of hard-coded secrets.
- Enable CloudWatch + X-Ray tracing on the Gateway endpoint in production.
- For 100+ tools, prefer Semantic Search so the agent does not carry the full tool catalog in every prompt.

## Example
A team can expose an internal ticket API and a Lambda refund function through Gateway, then let the agent call only those approved tools.

## Why It Matters
Gateway makes tool access explicit and central. That is easier to govern than giving an agent direct access to every API client and credential inside the application code.

---
↑ [Overview](./00_agentcore_overview.md)

**Related:** [AgentCore Memory](02_memory.md), [AgentCore Identity](04_identity.md), [AgentCore Policy](09_policy.md), [AgentCore Runtime](01_runtime.md), [MCP](../../../../ai/concepts/07_mcp.md)
**Tags:** #ai #aws #ml
