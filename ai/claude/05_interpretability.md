---
tags:
  - ai
  - claude
  - research
created_at: 2026-04-20T13:59:45
updated_at: 2026-04-20T13:59:45
recent_editor: CLAUDE
source: anthropic.com
---

↑ [Overview](./00_claude_overview.md)

# Mechanistic Interpretability

## What It Is

Mechanistic interpretability is Anthropic's research program to understand what is literally happening inside large language models — which internal patterns activate for which concepts, and why. Goal: make AI safety verifiable rather than assumed.

## The Problem

Individual neurons in LLMs have no consistent meaning. A single neuron might activate for "academic citations, English dialogue, HTTP requests, and Korean text" simultaneously. This phenomenon — multiple concepts encoded in the same neuron — is called **superposition**. You can't debug what you can't read.

## The Solution: Features

Instead of studying individual neurons, Anthropic decomposes model layers into **features** — recurring patterns of *combinations* of neuron activations that correspond to coherent concepts.

Technique: **dictionary learning** (borrowed from classical ML) — find the patterns that repeat across many different inputs.

## Key Findings

**In a small transformer:** Researchers identified 4,000+ features representing concepts like DNA sequences, legal language, HTTP requests, Hebrew text, nutrition statements.

**In Claude 3 Sonnet (production model):** Tens of millions of features identified — the first detailed internal map of a modern, production-grade LLM. Examples:
- Surface features: uppercase text, Python function arguments, surnames in citations
- Semantic features: bugs in code, gender bias discussions, keeping secrets

**Targeted steering:** Artificially activating a specific feature produces predictable, causal behavior changes — proof that features represent real internal structure, not artifacts.

**Universality:** Similar features appear across different models, suggesting they capture fundamental concepts rather than model-specific quirks.

**Model introspection:** Evidence that Claude has a "limited but functional" ability to access and report on its own internal states.

## Why It Matters

If you can read a model's internals, you can verify that safety training actually changed the right things — not just the surface behavior. Interpretability is the foundation for auditable AI safety.

---
↑ [Overview](./00_claude_overview.md)

**Related:** [Constitutional AI](03_constitutional_ai.md), [RSP](04_rsp.md), [Attention](../concepts/10_attention.md), [KV Cache](../concepts/11_kv_cache.md)
**Tags:** #ai #claude #research
