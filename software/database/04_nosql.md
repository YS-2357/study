---
tags:
  - software
  - database
created_at: 2026-04-23T15:20:41
updated_at: 2026-04-23T15:20:41
recent_editor: CLAUDE
---

↑ [Database Overview](./00_database_overview.md)

# NoSQL

## What It Is

Databases that don't use the relational (table + SQL) model. "NoSQL" means "not only SQL" — they trade some ACID guarantees for flexibility in data shape, horizontal scalability, or specialized access patterns.

## Analogy

Different filing systems for different jobs. A relational DB is a spreadsheet — great for structured, linked data. NoSQL types are like: a folder of JSON files (document), a dictionary (key-value), a whiteboard with sticky-note connections (graph), or a time-series log (column-store). Each fits a different shape of data.

## How It Works

**Four main types:**

| Type | Data model | Best for | Examples |
|------|-----------|---------|---------|
| **Document** | JSON/BSON documents | Flexible schemas, nested data | MongoDB, Firestore |
| **Key-Value** | Key → value (any type) | Caching, sessions, counters | Redis, DynamoDB |
| **Graph** | Nodes + edges | Relationships, recommendations, fraud | Neo4j, Amazon Neptune |
| **Column-store** | Columns grouped by family | Time-series, analytics, wide tables | Cassandra, BigTable |

**Document store example (MongoDB):**
```json
{
  "_id": "42",
  "name": "Alice",
  "orders": [
    { "item": "laptop", "price": 1200 },
    { "item": "mouse", "price": 30 }
  ]
}
```
No joins needed — related data nested in one document.

**Key-value example (Redis):**
```
SET session:abc123 '{"userId": 42}' EX 3600
GET session:abc123
```
Extremely fast, in-memory.

## Example

User profile with varying fields (some users have GitHub, some have Twitter, some have both):
- SQL: you'd need nullable columns or a separate `social_links` table
- Document DB: each document just includes whatever fields exist — no schema migration

## Why It Matters

NoSQL databases power caching (Redis), mobile backends (Firestore), social graphs (Neo4j), and IoT time-series (Cassandra). Choosing the right type for the data shape is more important than choosing a specific product. AWS DynamoDB (key-value/document) and Amazon Neptune (graph) are the AWS equivalents.

---
↑ [Database Overview](./00_database_overview.md)

**Related:** [ACID](./02_acid.md), [CAP Theorem](./05_cap_theorem.md), [AWS Database](../../cloud/aws/database/00_database_overview.md)
**Tags:** #software #database
