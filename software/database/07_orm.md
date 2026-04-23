---
tags:
  - software
  - database
created_at: 2026-04-23T15:20:41
updated_at: 2026-04-23T23:41:19
recent_editor: CODEX
---

↑ [Overview](./00_database_overview.md)

# ORM

## What It Is

Object-Relational Mapper. A library that maps database tables to classes in your code, so you can query the database using your programming language instead of writing SQL. ORM stands for Object-Relational Mapping.

## Analogy

A translation service between two languages. Your code speaks Python/JavaScript (objects). Your database speaks SQL (tables). The ORM translates: `User.findOne({ id: 42 })` → `SELECT * FROM users WHERE id = 42`. You write in your language; the ORM handles the SQL.

## How It Works

Each table becomes a class; each row becomes an instance:

```python
# SQLAlchemy (Python)
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

# Query — no SQL written
user = session.query(User).filter(User.id == 42).first()
print(user.name)
```

Generated SQL (happens invisibly):
```sql
SELECT * FROM users WHERE id = 42 LIMIT 1;
```

**Common ORMs:**

| Language | ORM |
|----------|-----|
| Python | SQLAlchemy, Django ORM |
| JavaScript/TS | Prisma, TypeORM, Sequelize |
| Java | Hibernate |
| Ruby | ActiveRecord |

## When to Avoid ORMs

ORMs generate SQL automatically — which can be dangerously inefficient for complex queries:

```python
# This looks innocent but may generate N+1 queries:
for user in session.query(User).all():
    print(user.orders)  # separate query per user!
```

For complex joins, aggregations, or performance-critical paths, write raw SQL. Most ORMs let you drop to raw SQL when needed.

## Example

Django ORM — find users with at least one pending order:

```python
users = User.objects.filter(orders__status='pending').distinct()
```

vs raw SQL:
```sql
SELECT DISTINCT users.* FROM users
JOIN orders ON orders.user_id = users.id
WHERE orders.status = 'pending';
```

Both return the same result; the ORM version is more readable but obscures what SQL runs.

## Why It Matters

ORMs speed up development and prevent SQL injection (queries are parameterized automatically). The risk: developers who don't know SQL can't diagnose the slow queries the ORM generates. Know SQL first, then use an ORM.

---
↑ [Overview](./00_database_overview.md)

**Related:** [SQL](./01_sql.md), [Indexing](./03_indexing.md), [Connection Pooling](./06_connection_pooling.md)
**Tags:** #software #database
