---
tags:
  - software
  - database
created_at: 2026-04-23T15:20:41
updated_at: 2026-04-23T23:41:19
recent_editor: CODEX
---

↑ [Overview](./00_database_overview.md)

# ACID

## What It Is

Four guarantees that relational databases provide for transactions. A **transaction** is a group of operations that must all succeed or all fail together. ACID ensures transactions are safe even when things go wrong.

## Analogy

A bank transfer. Moving $100 from Alice to Bob is two operations: debit Alice, credit Bob. ACID guarantees: either both happen, or neither does. You'll never have the money disappear from Alice without arriving at Bob.

## How It Works

| Property | Guarantee | Example |
|----------|-----------|---------|
| **Atomicity** | All operations in a transaction succeed, or none do | Debit + Credit: if credit fails, debit is rolled back |
| **Consistency** | A transaction brings the DB from one valid state to another | Account balance can't go below 0 if that's a constraint |
| **Isolation** | Concurrent transactions don't interfere with each other | Two users buying the last item don't both succeed |
| **Durability** | Once committed, data survives crashes | After commit, a power failure doesn't lose the data |

**Transaction syntax (SQL):**

```sql
BEGIN;
  UPDATE accounts SET balance = balance - 100 WHERE id = 1;
  UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;   -- both succeed → saved
-- or
ROLLBACK; -- something failed → both reversed
```

**Isolation levels** (trade-off between safety and performance):

| Level | Prevents |
|-------|---------|
| Read Uncommitted | Nothing (dirty reads possible) |
| Read Committed | Dirty reads |
| Repeatable Read | Dirty + non-repeatable reads |
| Serializable | All anomalies (slowest) |

## Example

Without atomicity: Alice's $100 is debited but the credit to Bob crashes mid-transaction. $100 vanishes. With atomicity, the debit is rolled back automatically.

## Why It Matters

ACID is why relational databases are trusted for financial, medical, and legal data. NoSQL databases often sacrifice some ACID properties for speed and scale — understanding ACID explains exactly what you're giving up.

---
↑ [Overview](./00_database_overview.md)

**Related:** [SQL](./01_sql.md), [NoSQL](./04_nosql.md), [CAP Theorem](./05_cap_theorem.md)
**Tags:** #software #database
