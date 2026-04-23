---
tags:
  - software
  - database
created_at: 2026-04-23T15:20:41
updated_at: 2026-04-23T23:41:19
recent_editor: CODEX
---

↑ [Overview](./00_database_overview.md)

# SQL

## What It Is

A language for querying and manipulating relational databases — data stored in tables with rows and columns, linked by relationships (foreign keys). SQL stands for Structured Query Language.

## Analogy

A spreadsheet with superpowers. A table is a spreadsheet tab. SQL is the formula language — but instead of cell references, you write queries that join sheets, filter rows, and aggregate data across millions of records instantly.

## How It Works

**Core operations:**

```sql
-- Select: retrieve data
SELECT name, email FROM users WHERE age > 18 ORDER BY name;

-- Insert: add a row
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');

-- Update: modify rows
UPDATE users SET email = 'new@example.com' WHERE id = 42;

-- Delete: remove rows
DELETE FROM users WHERE id = 42;
```

**JOIN — combine data from multiple tables:**

```sql
SELECT orders.id, users.name
FROM orders
JOIN users ON orders.user_id = users.id
WHERE orders.status = 'pending';
```

| Join type | Returns |
|-----------|---------|
| `INNER JOIN` | Only rows that match in both tables |
| `LEFT JOIN` | All rows from left table, matched rows from right (NULL if no match) |
| `RIGHT JOIN` | Opposite of LEFT |

**Aggregate functions:**

```sql
SELECT COUNT(*), AVG(price), MAX(price)
FROM orders
GROUP BY category;
```

## Example

E-commerce: find the top 5 customers by total spend:

```sql
SELECT users.name, SUM(orders.total) AS total_spent
FROM orders
JOIN users ON orders.user_id = users.id
GROUP BY users.id
ORDER BY total_spent DESC
LIMIT 5;
```

## Why It Matters

SQL is used by virtually every system that stores structured data. PostgreSQL, MySQL, SQLite, and cloud databases (Amazon RDS, Aurora) all speak SQL. It's one of the most durable skills in software engineering.

---
↑ [Overview](./00_database_overview.md)

**Related:** [ACID](./02_acid.md), [Indexing](./03_indexing.md), [ORM](./07_orm.md)
**Tags:** #software #database
