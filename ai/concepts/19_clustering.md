---
tags:
  - ai
  - ml
created_at: 2026-04-27T08:33:02
updated_at: 2026-04-27T08:33:02
recent_editor: CODEX
---

# Clustering

## What It Is

Clustering is unsupervised learning that groups similar data points without pre-existing labels. k-means is a classic clustering algorithm that partitions data into `k` groups, where each group is represented by a centroid.

## Analogy

Sorting a pile of mixed notes into stacks by similarity. You do not start with labels like "billing" or "networking"; you group items that look close to each other, then inspect the stacks to understand what each group means.

## How It Works

k-means requires choosing the number of clusters, `k`, before training.

1. Initialize `k` centroids.
2. Assign each point to the nearest centroid.
3. Recompute each centroid as the mean of the points assigned to it.
4. Repeat assignment and update steps until the centroids stop moving much.

scikit-learn describes k-means as minimizing **inertia**, also called within-cluster sum of squares: points should be close to the centroid of their assigned cluster. [scikit-learn clustering guide](https://scikit-learn.org/stable/modules/clustering.html#k-means)

### Practical Constraints

k-means works best when clusters are compact, distance-based, and roughly similar in size. It can perform poorly when clusters are long, nested, unevenly sized, or separated by density rather than distance.

The result also depends on feature representation. For text, documents are usually vectorized first with [text vectorization](./18_text_vectorization.md) or [embedding models](./17_embedding_models.md), then clustered in that vector space.

## Example

A team has 10,000 support tickets and no labels. They vectorize each ticket, run k-means with `k = 20`, then inspect the top terms or nearest examples in each cluster. Some clusters may correspond to login issues, billing questions, deployment failures, or API rate limits.

## Why It Matters

Clustering helps explore unlabeled data. It is useful for document organization, duplicate detection, topic discovery, customer segmentation, anomaly triage, and finding structure before a supervised labeling workflow exists.

---
[Overview](./00_concepts_overview.md)

**Related:** [Text Vectorization](./18_text_vectorization.md), [Embedding Models](./17_embedding_models.md), [RAG](./16_rag.md)
**Tags:** #ai #ml
