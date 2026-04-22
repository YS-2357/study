---
tags:
  - aws
  - devtools
  - sap
created_at: 2026-04-22T00:00:00
updated_at: 2026-04-22T09:57:48
recent_editor: CLAUDE
source:
  - aws-partner-summit-seoul-2026
---

↑ [Overview](./00_devtools_overview.md)

# SAP + AWS Integration

AWS tools for SAP data analysis, ABAP development, and agentic automation of SAP workflows.

## Amazon Q Developer for SAP

ABAP code and unit test generation via LLM, integrated into SAP IDEs.

**Supported IDEs:** Eclipse + SAP ABAP Development Tools, VS Code + BAS (Business Application Studio)

### AWS ABAP Accelerator MCP Server

```
IDEs → Amazon Q plug-in → MCP Server → SAP RISE / On-Prem
```

Functions:
- ECC → S/4HANA migration analysis
- ATC (ABAP Test Cockpit) automation
- Clean Core enforcement
- Auto unit test generation
- ABAP dependency analysis

## Amazon Quick

Enterprise AI platform for natural language business intelligence and workflow automation.

**Core features:** Spaces, Chat Agents, Research, QuickSight, Flows, Automate
**Data connectors:** 40+ sources, user files, QuickSight datasets

### Quick + SAP Architecture

```
Amazon Quick (Chat agents + MCP Client)
  → OAuth
  → Bedrock AgentCore Gateway
  → Runtime (SAP MCP Server)
  → SAP RISE / Native (OData / HTTPS)
```

## Strands Agents for SAP

Multi-agent workflows for SAP process automation. Example — Credit Management:

```
Sales User → Web Chat UI → API Gateway → Lambda → DynamoDB → SNS
  → CreditAgent (Strands) → SAP S/4HANA (OData) → UpdateAgent
```

Use cases: credit limit increase, blocked order release, demand forecasting.

## AWS SDK for SAP ABAP

Call 200+ AWS services directly from SAP RISE, On-Prem, or BTP ABAP code.

Key services accessible from SAP:
- **AI/ML:** Bedrock, SageMaker, Textract, Rekognition, Translate, Forecast, Personalize
- **Integration:** Lambda, AppFlow, Kinesis, AppSync, IoT Core
- **Analytics:** EMR, Lookout, IoT TwinMaker, Location

## Key Tool Summary

| Use Case | Tools |
|----------|-------|
| ABAP coding acceleration | Amazon Q + ABAP Dev Tools + ABAP Accelerator MCP |
| SAP data analysis | Amazon Quick + QuickSight |
| SAP process automation | Strands Agent SDK |
| Direct AWS calls from ABAP | AWS SDK for SAP ABAP |

---
↑ [Overview](./00_devtools_overview.md)

**Related:** [Strands Agents SDK](../ai/11_strands_agents_sdk.md), [AgentCore Gateway](../ai/agentcore/03_gateway.md), [Bedrock](../ai/01_amazon_bedrock.md)
**Tags:** #aws #devtools #sap
