---
tags:
  - ai
  - aws
  - ml
  - security
created_at: 260417-141847
updated_at: 260417-141847
---

# Amazon Bedrock Guardrails

## Official Documentation
- [Bedrock Guardrails Documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
- [Bedrock Guardrails Pricing](https://aws.amazon.com/bedrock/pricing/#Guardrails)

## What It Is
Bedrock Guardrails is a filtering layer that sits between users and models, checking both input and output to block or redact unwanted content.

**Where it sits:**
```
User prompt → [Guardrail: check input] → Model → [Guardrail: check output] → Response
                    ↓ (blocked)                          ↓ (blocked/redacted)
              "Sorry, I can't help"              Redact PII / block response
```

**Key point:** Guardrails are model-agnostic. You can apply the same guardrail to any Bedrock model, and even to models outside Bedrock via the ApplyGuardrail API.

## How It Works

Every request passes through the guardrail twice — once on the way in (input check) and once on the way out (output check). Each check evaluates the text against all configured filters in sequence: content filters by category and strength, denied topic classifiers, PII detectors, word blockers, and contextual grounding checks. If any filter triggers a block action, the request or response is replaced with a configured denial message. If the action is anonymize, detected PII is replaced with a placeholder before the content is passed along.

## Console Access
- Amazon Bedrock > Guardrails > Create guardrail

## Key Concepts

### Filter Types

| Filter | What it does | Example |
|---|---|---|
| **Content filters** | Block harmful content by category | Hate, violence, sexual, misconduct, prompt attacks |
| **Denied topics** | Block custom topics you define | "Don't discuss competitor products" |
| **PII detection** | Detect and redact/block PII | SSN, phone, email, credit card, name, address |
| **Word filters** | Block specific words/phrases | Profanity, internal project names |
| **Contextual grounding** | Check if response is grounded in source | Prevent hallucination in RAG apps |

### Content Filter Strengths
Each content category can be set to different sensitivity levels:
- **None** → no filtering
- **Low** → block only the most obvious violations
- **Medium** → balanced
- **High** → aggressive filtering (may over-block)

### PII Handling
Two modes:
- **Block** — reject the entire request/response if PII is detected
- **Anonymize** — replace PII with placeholders (`[NAME]`, `[PHONE]`, `[SSN]`)

Supported PII types: name, email, phone, SSN, credit card, address, age, driver's license, passport, IP address, and more.

### PII Still Reaches AWS
Guardrails process data *within* AWS. They protect the model from seeing PII, not AWS from receiving it.

```
User sends PII → AWS receives it → Guardrail detects → Redacts before model sees it
                  ↑
                  PII already at AWS
```

What protects data at the AWS level:
- AWS does not train on your Bedrock inputs/outputs
- Encryption in transit (TLS) and at rest (KMS)
- VPC endpoints keep traffic off public internet
- Compliance certifications (SOC, HIPAA eligible, etc.)
- Data stays in your region

If PII must never leave your network → on-premises models, not cloud LLMs.

### How to Apply
- **Bedrock console** — attach guardrail to a model in the playground
- **API** — pass `guardrailIdentifier` and `guardrailVersion` in `InvokeModel` calls
- **Agents** — attach guardrail to a Bedrock Agent
- **ApplyGuardrail API** — use guardrails standalone, even with non-Bedrock models

## Precautions

### MAIN PRECAUTION: Guardrails Add Latency and Cost
- Every request is evaluated twice (input + output) = extra processing time
- Charged per policy assessment (per 1,000 text units)
- High-sensitivity filters may over-block legitimate content

### 1. Test Before Production
- Overly strict filters block valid user requests
- Overly loose filters miss harmful content
- Use the Bedrock console test feature to tune sensitivity levels

### 2. Not a Replacement for Application-Level Validation
- Guardrails are one layer of defense
- Still validate inputs in your application code
- Still sanitize outputs before displaying to users

### 3. PII Detection Is Not Perfect
- ML-based detection can miss edge cases or produce false positives
- Don't rely solely on Guardrails for regulatory PII compliance
- Layer with application-level PII scrubbing for sensitive workloads

### 4. Version Your Guardrails
- Guardrails support versioning — use it
- Test new versions before promoting to production
- Keep a working version as fallback

## Example

A customer support chatbot attaches a guardrail with medium-strength content filters, a denied topic blocking competitor discussions, and PII anonymization for email and phone. When a user asks a question containing their phone number, the guardrail redacts it before the model sees it and returns the answer with `[PHONE]` in place of the actual number.

## Why It Matters

Guardrails let you enforce consistent safety and compliance rules across every Bedrock model without modifying your application code. A single guardrail version can be reused across models and updated centrally when policies change.

---
← Previous: [Amazon Bedrock AgentCore](32_amazon_bedrock_agentcore.md) | [Overview](00_overview.md) | Next: [Amazon Bedrock](34_amazon_bedrock.md) →
