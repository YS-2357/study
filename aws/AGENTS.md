# AWS Study Subtree Guide

These instructions apply to the entire `aws/` subtree unless a deeper `AGENTS.md` overrides them.

## Scope

- Use the root [AGENTS.md](../AGENTS.md) and [README.md](../README.md) as the base rules.
- This file adds AWS-specific note expectations only.

## AWS Service Note Rule

- For all AWS notes anywhere under `aws/`, explain the service from these four viewpoints whenever relevant:
- 가능여부: whether a design, operation, or requirement is possible with the service
- 중단/무중단: whether setup, migration, scaling, or change work causes interruption or can be done with little or no downtime
- 장단점: the main advantages and disadvantages
- 차이점: how it differs from nearby or commonly confused AWS services
- For AWS Q&A-style notes, include only the viewpoints that are actually relevant. Do not force all four into every answer.
- When a compact summary helps, format the applicable viewpoints as a table near the end of the answer.

| Perspective | Detail |
|-------------|--------|
| Feasibility | ... |
| Disruption | ... |
| Pros & Cons | ... |
| Differences | ... |

## Writing Guidance

- Keep the existing repository note structure from the root [README.md](../README.md). Do not introduce a new mandatory heading schema just for AWS notes.
- Work the four viewpoints into the existing sections such as `How It Works`, `Example`, and `Why It Matters`.
- When a comparison already exists in another AWS note, link to it instead of duplicating the same explanation.
- Prefer concrete operational comparisons such as `EC2` vs `Lambda`, `RDS` vs `Aurora`, or `CloudFront` vs `Global Accelerator` when discussing 차이점.
