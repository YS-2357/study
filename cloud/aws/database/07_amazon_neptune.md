---
tags:
  - aws
  - database
  - graph
created_at: 2026-04-22T00:00:00
updated_at: 2026-04-22T00:00:00
recent_editor: CLAUDE
source:
  - aws-partner-summit-seoul-2026
---

↑ [Overview](./00_database_overview.md)

# Amazon Neptune

Fully managed graph database supporting both Property Graph and RDF. Primary use: knowledge graphs, ontologies, and graph-based AI (GraphRAG, Text2Query).

## Graph Models Supported

| Model | Query Language | Strength |
|-------|---------------|----------|
| Property Graph | openCypher, Gremlin | Developer-friendly, complex traversals |
| RDF | SPARQL (W3C) | Semantic reasoning, data sharing, ontology |

## Ontology

A logical model capturing domain semantics — the semantic layer that prevents AI from propagating wrong intent.

**Components:** Concepts, Properties, Relationships, Constraints, Instances
**Languages:** RDF, OWL, SHACL, Property Graph

### Ontology Handling Choices

1. **Use existing** — fast, validated (FIBO for finance, SNOMED CT for clinical, schema.org for general)
2. **Extend existing** — requires understanding constraints
3. **Define custom** — most work, needs collaboration

**Public ontologies:**
- Upper: BFO (abstract), gist (practical), schema.org
- Domain: FIBO (finance), SNOMED CT (clinical), CIDOC-CRM (cultural heritage)

## Knowledge Graph Design

- Nodes (entities) + Edges (relationships) + Properties on both
- Use unique IDs; specific labels over generic (`HasEmail` not `Has`)
- Decide node vs. property: if the thing has its own properties → node; if it's a simple value → property
- Source graph via R2RML extraction from legacy relational systems

## Text2Query

Natural language → graph query (openCypher / SPARQL) via LLM, using Neptune as the backend.

Pattern: user intent → LLM interprets ontology → generates query → Neptune executes → structured result

## GraphRAG vs VectorRAG

| | VectorDB RAG | Knowledge Graph RAG |
|--|-------------|-------------------|
| Method | Chunking → embedding → cosine similarity | Entity/relationship graph → multi-hop inference |
| Strength | Speed, low cost, domain-agnostic | Reduced hallucination, explainability, reasoning |
| Weakness | No reasoning, chunk boundary loss | Setup cost, domain knowledge required |

**Best approach: Hybrid** — vector similarity for candidate retrieval + graph traversal for reasoning + LLM for generation.

GraphRAG as **Semantic Sidecar**: KG provides context/constraints; vector index handles fuzzy search.

## Use Cases

- Customer 360 profiles (multi-source entity resolution)
- Fraud detection (relationship pattern analysis)
- Digital Twin (physical-digital relationship mapping)
- Data Fabric (cross-silo entity linking via URI)
- Impact analysis (dependency traversal)

## Why Ontology for Agentic AI

Agentic AI risks amplifying errors at scale when operating on ambiguous data. A semantic layer:
- Enables governance and auditability (lineage tracking, compliance)
- Breaks data silos via URI-based identification
- Gives agents structured context instead of raw embeddings

---
↑ [Overview](./00_database_overview.md)

**Related:** [SageMaker](../analytics/04_amazon_sagemaker.md), [Bedrock Knowledge Bases](../ai/concepts/01_amazon_bedrock.md)
**Tags:** #aws #database #graph
