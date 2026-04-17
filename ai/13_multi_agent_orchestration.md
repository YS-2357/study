---
tags:
  - ai
created_at: 260406-000000
updated_at: 260417-141847
---

# Multi-Agent Orchestration

## What It Is

Multi-agent orchestration is a system design where multiple specialized [agents](01_agent.md) collaborate under a shared workflow — each with a defined role, operating through a structured loop of work, review, and decision.

## How It Works

### Role taxonomy

Every agent in a multi-agent system fills one of five role types:

| Role | Job |
|------|-----|
| Orchestrator | Decides what happens next. Never implements. |
| Implementer | Does the actual work — writes code, deploys infra. |
| Reviewer | Evaluates output against rules. No stake in the work passing. |
| Supervisor | Makes the final call: approve / conditional approve / reject. |
| Advisor | Provides read-only input. No decision power. |

### The review loop

```
Orchestrator assigns task
  → Implementer works
    → Reviewer scores output
      → Supervisor decides
        → Orchestrator routes outcome
          → repeat if conditional or rejected
```

The loop runs until the supervisor approves. A conditional approval means: fix the specific issue, then resubmit — not start over.

### Why the reviewer and supervisor are separate roles

The reviewer scores and flags. The supervisor decides what to do about it. Splitting these means the reviewer can be strict without being the one who blocks the project — and the supervisor can weigh severity without having to re-examine every criterion.

## Example

An 8-agent setup for a full-stack project:

| Agent | Role type |
|-------|-----------|
| Kiro | Orchestrator |
| backend, frontend, infra | Implementers |
| reviewer | Reviewer |
| supervisor | Supervisor |
| claude advisor, codex advisor | Advisors |

Real cycle from today: infra agent submitted TASK-002a → reviewer flagged a warning → supervisor gave conditional approve → infra agent fixed it → TASK-002b passed. The SSM bug was caught the same way — reviewer found the parameter was created outside CDK, which violated the ownership rule.

## Coordination Protocol

Role separation solves the contamination problem, but agents still need a shared language to hand work off reliably. Without it, the reviewer's output is ambiguous, the supervisor can't decide, and the orchestrator can't route.

Four components make inter-agent communication effective:

### 1. Shared criteria

Every agent evaluates against the same rubric — defined upfront, visible to all roles.

Without shared criteria, the implementer builds toward one standard and the reviewer checks against a different one. The conflict is invisible until review fails with no clear reason.

Example: a 15-item checklist covering security, ownership, test coverage, CDK compliance, and cleanup. The implementer knows the checklist before building. The reviewer scores against the same checklist. There is no ambiguity about what "done" means.

### 2. Numerical scoring

Scores make evaluation objective and comparable across cycles.

"Looks good" is not actionable. "11/15 — items 3, 7, 12 failed" tells the implementer exactly what to fix, tells the supervisor the severity, and gives the orchestrator a basis for routing.

Numerical scoring also makes improvement visible: TASK-002a scored 10/15 (warning), TASK-002b scored 15/15 after the fix. The loop has a measurable exit condition.

### 3. Written grounds

Every score must cite the specific rule violated — not just the verdict.

Bad: `reviewer: FAIL — SSM issue`
Good: `reviewer: FAIL — SSM parameter created outside CDK. Violates Rule 5 (no manual console changes) and Rule 8 (no CDK-unmanaged resources). Fix: move SSM into backend_stack.py.`

Written grounds serve three purposes:
- The implementer knows exactly what to fix
- The supervisor can verify the reviewer's reasoning
- The report becomes a record of what was caught and why

### 4. Structured reports

Each agent produces a structured artifact as its output — not free text.

The report is the handoff. The next agent reads the report, not the conversation. If the report is unstructured, the next agent must interpret rather than act.

Minimum report fields for a review cycle:

| Field | Purpose |
|-------|---------|
| Task ID | Links the report to the work |
| Score | Numerical verdict |
| Passed criteria | What was verified clean |
| Failed criteria | What was violated, with rule citation |
| Decision | Approve / conditional / reject |
| Required fix | Specific action if conditional |

The orchestrator reads the decision field to route. The implementer reads the required fix field to act. Each role consumes only what it needs.

### How the four components connect

```
shared criteria → implementer knows the target
      ↓
numerical scoring → reviewer produces an objective verdict
      ↓
written grounds → supervisor can verify the reasoning
      ↓
structured report → orchestrator routes, implementer acts
```

Remove any one component and the chain degrades: no shared criteria means the score is arbitrary, no written grounds means the fix is unclear, no structured report means the next agent has to guess.

## Why It Matters

### Why not just use one strong agent?

A single agent's context gets contaminated by its own implementation decisions. It built the system, justified the choices, and believes the work is correct — because it did the work. It cannot objectively evaluate its own output.

A separate reviewer has no implementation history for that task. Its only job is to find violations. That adversarial gap is the entire point of role separation.

### What the review pipeline catches that testing misses

Automated tests catch **behavioral bugs** — crashes, wrong outputs, failed assertions.

Review gates catch **structural bugs** — ownership violations, rule violations, silent invariant breaks. The SSM parameter worked at runtime. There was no crash. A standard test loop would have passed it. Only a rule-aware reviewer asking "is every resource CDK-managed?" surfaced the violation.

| Bug type | Caught by |
|----------|-----------|
| Behavioral (crash, wrong output) | Tests |
| Structural (rule violation, ownership break) | Review gate |

> **Tip:** If something works at runtime but violates a rule, only the review gate catches it. Design your review criteria around rules, not just behavior.

---
← Previous: [Prompt Caching](12_prompt_caching.md) | [Overview](00_overview.md) | Next: [Subagent Design](14_subagent_design.md) →
