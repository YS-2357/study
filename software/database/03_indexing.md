---
tags:
  - software
  - database
created_at: 2026-04-23T15:20:41
updated_at: 2026-04-23T23:41:19
recent_editor: CODEX
---

↑ [Overview](./00_database_overview.md)

# Indexing

## What It Is

A data structure (usually a B-tree) that a database builds alongside a table to make lookups on a specific column fast. Without an index, the DB scans every row (full table scan). With an index, it jumps directly to matching rows.

## Analogy

A book index. Finding every mention of "caching" without an index means reading every page. With the index at the back, you flip to "caching → pages 42, 87, 201" and go directly there. The index costs extra pages (storage) but saves enormous read time.

## How It Works

**B-tree index** (default in PostgreSQL, MySQL):
- A balanced tree sorted by the indexed column's values
- `SELECT * FROM users WHERE email = 'alice@example.com'` → B-tree finds the email in O(log n) instead of O(n)

```sql
-- Create an index
CREATE INDEX idx_users_email ON users(email);

-- Composite index (order matters)
CREATE INDEX idx_orders_user_date ON orders(user_id, created_at);
```

**When indexes help:**
- `WHERE` clauses on the indexed column
- `JOIN` conditions
- `ORDER BY` on the indexed column

**When indexes hurt:**
- `INSERT`, `UPDATE`, `DELETE` — every write must also update the index
- Too many indexes on a write-heavy table slow down writes significantly

**Types:**

| Type | Use case |
|------|---------|
| B-tree | Default — range queries, equality, sorting |
| Hash | Equality only (exact match) |
| GIN / GiST | Full-text search, JSON, arrays (PostgreSQL) |

## Example

Table with 10M users. Query `WHERE email = 'alice@example.com'`:
- Without index: scans 10M rows (~seconds)
- With index on `email`: B-tree traversal (~milliseconds)

`EXPLAIN ANALYZE` shows whether a query uses an index:
```sql
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'alice@example.com';
-- Shows: "Index Scan using idx_users_email"
```

## Why It Matters

Indexes are the single most impactful database performance lever. Adding the right index can turn a seconds-long query into milliseconds. Adding too many can cripple write performance. The skill is knowing which queries need indexes and which don't.

---
↑ [Overview](./00_database_overview.md)

**Related:** [SQL](./01_sql.md), [Connection Pooling](./06_connection_pooling.md)
**Tags:** #software #database
