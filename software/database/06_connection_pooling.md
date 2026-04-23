---
tags:
  - software
  - database
created_at: 2026-04-23T15:20:41
updated_at: 2026-04-23T15:20:41
recent_editor: CLAUDE
---

↑ [Database Overview](./00_database_overview.md)

# Connection Pooling

## What It Is

A technique where a fixed set of database connections is kept open and shared across many application requests. Opening a new connection to a database is expensive (handshake, auth, memory). A pool reuses existing connections instead.

## Analogy

A taxi fleet. Without pooling: every passenger calls a car factory, waits for a new car to be built, takes the trip, then the car is destroyed. With pooling: a fleet of 20 taxis waits at the stand. Passengers hop in an available taxi, use it, return it to the stand. Cars are built once and reused.

## How It Works

```
App requests → Pool manager → [conn1] [conn2] [conn3] ... [connN] → DB
                                ↑ idle connections waiting
```

1. App asks pool for a connection
2. Pool returns an idle connection (or waits if all are busy)
3. App runs its query
4. App returns connection to pool (not closed — reused)

**Key settings:**

| Setting | Meaning |
|---------|---------|
| `min` / `pool_size` | Connections always kept open |
| `max` | Maximum connections the pool will open |
| `timeout` | How long to wait for a free connection before error |
| `idle_timeout` | Close connections idle longer than this |

**Common tools:**

| Language | Pool library |
|----------|-------------|
| Python | `SQLAlchemy` (built-in pool), `asyncpg` |
| Node.js | `pg` Pool, `knex` |
| Java | HikariCP |
| Managed | PgBouncer (proxy-level pooler for PostgreSQL) |

## Example

A web server handles 1000 concurrent users. Without pooling: 1000 DB connections — most DBs cap at 100–500 connections. With a pool of 20: all 1000 requests share 20 connections, queuing briefly when busy. The DB stays stable.

PostgreSQL default max connections: 100. PgBouncer lets thousands of app connections share a small pool.

## Why It Matters

Connection limits are a common production failure: app deploys at scale → DB connection limit hit → all queries fail. Connection pooling is the standard solution and is nearly always configured in production.

---
↑ [Database Overview](./00_database_overview.md)

**Related:** [SQL](./01_sql.md), [Indexing](./03_indexing.md)
**Tags:** #software #database
