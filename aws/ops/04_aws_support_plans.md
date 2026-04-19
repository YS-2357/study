---
tags:
  - aws
created_at: 2026-04-05T00:00:00
updated_at: 2026-04-19T09:11:51
recent_editor: CLAUDE
---

↑ [Overview](./00_ops_overview.md)

# AWS Support Plans

## What It Is

AWS Support Plans are tiered support offerings that provide varying levels of technical assistance, response times, and advisory services.

## How It Works

| Plan | Price | Technical Support | Response Time (Critical) | Key Features |
|------|-------|-------------------|--------------------------|--------------|
| **Basic** | Free | Billing/account only | — | Service health dashboard, documentation |
| **Developer** | From $29/month | Business-hours email | 12 hours (general) | 1 primary contact |
| **Business** | From $100/month | 24/7 phone, chat, email | **1 hour** (production down) | Unlimited contacts, Trusted Advisor full |
| **Enterprise** | From $15,000/month | 24/7 phone, chat, email | **15 minutes** (business-critical) | TAM (Technical Account Manager), Concierge |

When working with an AWS partner (e.g., MSP provider), the partner may handle day-to-day technical support. However, for AWS-internal service issues, the response level depends on the customer's own Support Plan tier.

## Example

A production e-commerce site goes down due to an RDS failover issue. With a Business plan, the team opens a severity-1 case and gets an AWS engineer on the phone within 1 hour. With only the Basic plan, they would have no access to technical support and would rely on documentation and forums.

## Why It Matters

Choosing the right support tier is a cost-vs-risk decision. Production workloads typically need Business or higher for the 1-hour critical response SLA. The Basic plan is only suitable for experimentation and non-critical workloads.

---
↑ [Overview](./00_ops_overview.md)

**Related:** [Cloud Computing Billing](03_cloud_computing_billing.md)
**Tags:** #aws
