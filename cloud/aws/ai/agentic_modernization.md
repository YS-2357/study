---
tags:
  - aws
  - ai
  - devops
created_at: 2026-04-22T00:00:00
updated_at: 2026-04-22T00:00:00
recent_editor: CLAUDE
source:
  - aws-partner-summit-seoul-2026
---

↑ [Overview](./00_ai_overview.md)

# Agentic AI Application Modernization

Using AWS agentic tools to modernize legacy applications — replacing manual migration with AI-driven, multi-agent workflows.

## Paradigm Shift

| Before | After |
|--------|-------|
| Manual coding | Define intent/goals |
| Manual build/deploy | AI agents plan/execute/verify |
| Reactive monitoring | Orchestrate outcomes |
| Focus: feature delivery | Focus: architecture/strategy |

## 3-Pillar Framework

```
AI-Driven Dev          Intelligent Infra       Autonomous Ops
─────────────────      ─────────────────       ─────────────────
Kiro                   EKS Auto Mode           DevOps Agent
Amazon Q Developer     ECS on Fargate          CloudWatch AIOps
AWS Transform          Lambda                  Amazon Q Developer CLI
```

## Tools

### Kiro — Spec-Driven IDE
- Natural language spec → requirements → design → code (automatic flow)
- Legacy code analysis: automated refactoring and modernization
- Continuous validation hooks throughout the cycle

### Kiro CLI — NL AWS Operations
```bash
kiro ask "why is my pod dead?"
# → log analysis → OOMKilled
```
- Auto-generates CloudWatch Logs Insights queries from natural language
- MCP server integration for safe AWS service access

### DevOps Agent — Self-Driving CI/CD
- End-to-end: source code → prod environment, complete CI/CD auto-config
- Auto IaC generation, GitHub/GitLab integration
- Intelligent incident response

### Security Agent — AI Security Automation
- Container image CVE auto-scan (ECR push triggers)
- IAM policy review: least-privilege recommendations, orphaned removal
- Runtime threat detection + auto-isolation (GuardDuty integration)
- Compliance: PCI-DSS, HIPAA, SOC2 auto-validation + reporting
- Integrates: GuardDuty, Security Hub, Inspector

### AWS Transform — Legacy Analysis
- Auto-analyze and convert Java, .NET, mainframe workloads
- Auto test generation + dependency analysis
- Microservices decomposition strategy from monolith
- Assessment: weeks → days

### EKS Auto Mode — Zero-Ops Kubernetes
- Full automation: provisioning → maintenance → patches
- 40% performance/price improvement (Graviton)
- 90% cost reduction via Spot auto-blending
- Built-in: PDB, resource management, topology spread

### AIOps
- **CloudWatch Investigations**: AI-based root cause analysis
- **Application Signals**: auto SLI/SLO measurement, no code changes
- **Gen AI Observability**: LLM token tracking, hallucination risk monitoring
- Natural language → Logs Insights queries (Korean/English)

## Harness Engineering (Guardrails + Control)

Maintaining AI autonomy while enforcing safety:

| Component | Role |
|-----------|------|
| Bedrock Guardrails | I/O filters — harmful content/PII intercept |
| EventBridge | Detect anomalous tool patterns, route/control |
| Step Functions | State machine + HITL for critical decisions |
| CloudWatch/CloudTrail | Monitor usage, hallucination risk, API history |

## Partner Service Model

| Stage | Duration | Tool | Pricing |
|-------|----------|------|---------|
| Assess | 2–4w | AWS Transform | Fixed price |
| Architect | 2–4w | Kiro | Design/prototype |
| Build | 4–12w | Kiro + DevOps Agent | Project/T&M |
| Operate | Ongoing | Q CLI + AIOps | Monthly recurring |

## Case: LG CNS

100 hours (manual) → 20 hours (agentic), 80% efficiency gain.
Stack: Bedrock, Q Developer, Lambda, EKS.

---
↑ [Overview](./00_ai_overview.md)

**Related:** [AgentCore](agentcore/00_agentcore_overview.md), [Neptune (Ontology)](../database/neptune.md), [LLM Evaluation](llm_evaluation.md)
**Tags:** #aws #ai #devops
