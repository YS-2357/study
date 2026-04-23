---
tags:
  - software
  - database
created_at: 2026-04-23T15:20:41
updated_at: 2026-04-23T23:41:19
recent_editor: CODEX
---

↑ [Overview](./00_database_overview.md)

# CAP Theorem

## What It Is

Any distributed data store can guarantee at most **two** of three properties: Consistency, Availability, Partition Tolerance. Proposed by Eric Brewer in 2000; formally proved by Gilbert & Lynch (MIT) in 2002. ([Wikipedia](https://en.wikipedia.org/wiki/CAP_theorem), [MIT proof](https://groups.csail.mit.edu/tds/papers/Gilbert/Brewer2.pdf))

## Analogy

A distributed library with branches. If a branch's phone line (network) goes down (partition), you must choose: refuse to lend books until the catalogue syncs (sacrifice Availability), or lend from the local catalogue which might be out of date (sacrifice Consistency). You can't have both while the line is down.

## How It Works

| Property | Meaning |
|----------|---------|
| **Consistency (C)** | Every read gets the most recent write — all nodes see the same data at the same time |
| **Availability (A)** | Every request gets a response (not necessarily the latest data) |
| **Partition Tolerance (P)** | System keeps working even if network messages between nodes are dropped |

**The forced choice:** in a real distributed system, network partitions happen. You can't eliminate P. So the real trade-off is always **C vs A** during a partition:

- **CP** (choose Consistency): refuse requests when nodes can't agree → data is correct, but some requests fail. (e.g., HBase, Zookeeper, traditional RDBMS clusters)
- **AP** (choose Availability): always respond, even with stale data → system stays up, but reads may be outdated. (e.g., Cassandra, DynamoDB, CouchDB)

```
        C
       / \
      /   \
   CP      CA  ← impossible in practice (partitions always happen)
      \   /
       \ /
        P ─── A
         AP
```

## Example

Two database nodes, network partition between them. A user writes "Alice's balance = $100" to node 1:

- **CP system:** node 2 refuses reads until it syncs with node 1 → correct answer, but requests fail
- **AP system:** node 2 returns Alice's old balance ($80) → request succeeds, but stale

## Why It Matters

CAP explains every NoSQL database's design decision. When you see "eventual consistency" (Cassandra, DynamoDB), that's AP. When you see "strong consistency" modes that can reject requests, that's CP. Choosing a database means choosing which guarantee to give up.

---
↑ [Overview](./00_database_overview.md)

**Related:** [ACID](./02_acid.md), [NoSQL](./04_nosql.md)
**Tags:** #software #database
