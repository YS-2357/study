---
tags:
  - aws
  - tooling
created_at: 2026-04-23T23:41:19
updated_at: 2026-04-23T23:41:19
recent_editor: CODEX
---

# AWS Study Subtree Guide

This file provides shared guidance for all notes under `aws/`.

## Scope

- Use the root [AGENTS.md](../../AGENTS.md), [CLAUDE.md](../../CLAUDE.md), and [README.md](../../README.md) as the base rules.
- This file adds AWS-specific note expectations only.

## AWS Service Note Rule

- For AWS notes anywhere under `aws/`, explain the service or feature from these four viewpoints whenever relevant:
- 가능여부: whether a design, operation, or requirement is possible with the service, including important limits and quotas
- 중단/무중단: whether setup, migration, scaling, or change work causes interruption or can be done with little or no downtime
- 장단점: the main trade-offs such as cost, performance, and operational burden
- 차이점: how it differs from nearby or commonly confused AWS services
- For AWS Q&A-style notes, include only the viewpoints that are actually relevant. Do not force all four into every answer.
- When a compact summary helps, format the applicable viewpoints as a table near the end of the note or section.

| Perspective | Detail |
|-------------|--------|
| Feasibility | ... |
| Disruption | ... |
| Pros & Cons | ... |
| Differences | ... |

## Writing Guidance

- Keep the existing repository note structure from the root [README.md](../../README.md). Do not introduce a new mandatory heading schema just for AWS notes.
- Work the four viewpoints into the existing sections such as `How It Works`, `Example`, and `Why It Matters`.
- When a comparison already exists in another AWS note, link to it instead of duplicating the same explanation.
- Prefer concrete operational comparisons such as `EC2` vs `Lambda`, `RDS` vs `Aurora`, or `CloudFront` vs `Global Accelerator` when discussing 차이점.
