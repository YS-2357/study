---
tags:
  - aws
  - ai
  - ml
created_at: 2026-04-22T00:00:00
updated_at: 2026-04-22T00:00:00
recent_editor: CLAUDE
source:
  - aws-partner-summit-seoul-2026
---

↑ [Overview](./00_ai_overview.md)

# LLM Evaluation

Systematic methodology for measuring and comparing LLM quality — essential for safe model migration and production agent monitoring.

## Evaluation Method Taxonomy

| Method | How | Quality | Cost | Best For |
|--------|-----|---------|------|----------|
| **Programmatic** | BLEU, BERTScore, deterministic | Medium | $ | Clear-answer tasks |
| **Human** | SME review | Highest | $$$$ | Subjective, high-stakes |
| **LLM-as-Judge** | LLM scores response via rubric | High | $$ | Large-scale screening |

Best practice: LLM-as-Judge for bulk screening → Human review for critical subset.

## LLM-as-Judge

Input: prompt + response + rubric → Judge LLM → Output: score (0–1) + rationale

**Amazon Bedrock built-in metrics (12):** Correctness, Completeness, Helpfulness, Faithfulness, Logical Coherence, Harmfulness, Stereotyping, Refusal, + Custom

**Fatal limits:**
- Self-preference bias (judges favor same-family models)
- Verbosity bias (longer responses score higher regardless of quality)
- Not suitable for high-risk decisions alone

## LLM-as-Jury

Multiple different model families (GPT, Claude, Mistral, Nova) evaluate in parallel; consensus score overrides individual bias.

| | Judge | Jury |
|--|-------|------|
| Bias risk | High | Low |
| Cost | $ | $$$ |
| Trust | Medium | Very High |
| Best for | Fast screening | Migration, high-risk |

**Eval360** — AWS open-source LLM-as-Jury tool; multi-LLM judge auto-composition, Bedrock-native, free on GitHub.

## Model Migration Evaluation Pipeline

4 stages — use Jury for migration decisions, Judge for ongoing operations:

```
Baseline → Prompt Optimization → Target Evaluation → Gradual Rollout
          [Judge: speed]         [Jury: trust]        [Judge Gate: CI/CD]
```

**Golden Dataset:** 100+ curated examples; dual use — evaluation + fine-tuning (2-for-1).

## Judge Gate Pattern (CI/CD)

```
Code Change → Build → [Judge Gate] → Deploy
                            ↓ (quality drop)
                       Auto-rollback
```

Prevents regressions from reaching production without manual review.

## Best Practices

- Use different model families as judge to avoid self-preference bias
- Quarterly human cross-calibration against judge scores
- Version-control evaluation prompts
- Programmatic eval for unit tests, Judge for integration, Jury for migration

## AWS Tool Map (by stage)

| Stage | Tool |
|-------|------|
| Model selection | `bedrock-model-profiler` |
| Model comparison | `360-eval` (LLM-as-Jury) |
| Migration decision | Bedrock Model Evaluation + `360-eval` |
| Agent offline | `agent-eval` |
| Agent operations | [AgentCore Evaluations](agentcore/08_evaluations.md) |
| CI/CD gates | AgentCore Evaluations (on-demand) |

## Day 1 Roadmap

1. Build Golden Dataset [1 day]
2. Run `bedrock-model-profiler` baseline [4h]
3. Run `360-eval` comparison [1–2 days]
4. Enable AgentCore Evaluations [5 min]
5. Add CI/CD quality gates [4h]

---
↑ [Overview](./00_ai_overview.md)

**Related:** [AgentCore Evaluations](agentcore/08_evaluations.md), [Amazon Bedrock](concepts/01_amazon_bedrock.md)
**Tags:** #aws #ai #ml
