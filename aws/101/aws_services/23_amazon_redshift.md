---
tags:
  - aws
  - database
---
# Amazon Redshift

## What It Is
Amazon Redshift is a fully managed data warehouse service for large-scale analytics using SQL.

**The problem it solves:**
- You have massive amounts of structured data (sales records, clickstreams, logs)
- You need to run complex analytical queries across billions of rows
- A regular database (RDS/Aurora) is too slow or expensive for this scale
- Redshift is built for OLAP (Online Analytical Processing), not OLTP (Online Transaction Processing)

**OLAP vs OLTP:**
```
OLTP (RDS/Aurora): "Insert this order" / "Update customer address" — many small, fast transactions
OLAP (Redshift):   "What were total sales by region for the last 3 years?" — few large, complex queries
```

### Redshift vs Other Analytics Services

| Service | What it does | When to use |
|---|---|---|
| **Redshift** | Data warehouse, complex SQL on massive structured data | BI dashboards, historical analytics, data modeling |
| **Athena** | Serverless SQL directly on S3 | Ad-hoc queries, no infrastructure, pay per query |
| **EMR** | Hadoop/Spark cluster for big data processing | ETL, ML training, unstructured data |
| **Glue** | Serverless ETL + data catalog | Data preparation, schema discovery |
| **QuickSight** | BI visualization/dashboards | Charts and reports on top of Redshift/Athena/etc. |

## How It Works

Data is loaded into Redshift tables from S3 using the `COPY` command, which parallelizes the load across compute nodes. Redshift stores data in columnar format on disk and distributes rows across nodes according to a distribution key. When you run a SQL query, the leader node builds an execution plan and sends parallel query fragments to compute nodes. Each compute node processes its local data slice and returns results to the leader, which aggregates and returns the final result.

## Console Access
- Search "Redshift" in AWS Console
- Amazon Redshift > Clusters (Provisioned) or Serverless


## Key Concepts

### Deployment Options
- **Redshift Provisioned** — You choose node type and count. Best for predictable, steady workloads.
- **Redshift Serverless** — AWS manages capacity automatically. Best for variable or getting-started workloads.

### Architecture (Provisioned)
- **Leader node** — Receives queries, builds execution plans, coordinates compute nodes
- **Compute nodes** — Store data and execute queries in parallel
- **Node types:** RA3 (managed storage, recommended), DC2 (local SSD, older)

### Key Design Concepts
- **Distribution key** — Determines how rows are spread across nodes. Good choice = less data shuffling = faster queries.
- **Sort key** — Determines row order on disk. Good choice = fewer blocks scanned = faster queries.
- **Columnar storage** — Data stored by column, not row. Analytical queries that read a few columns across many rows are much faster.

### Redshift Spectrum
- Query data directly in S3 without loading it into Redshift
- Extends your warehouse to your data lake
- Useful for infrequently accessed data you don't want to store in Redshift


## Precautions

### MAIN PRECAUTION: Redshift Is Not a Transactional Database
- Do NOT use Redshift for your application's primary database
- It's optimized for analytical reads, not high-frequency inserts/updates
- Use RDS/Aurora for OLTP, Redshift for OLAP

### 1. Distribution and Sort Key Design Matters
- Poor key choices cause data skew and slow queries
- Plan your schema before loading data
- Test with representative queries

### 2. Cost Management
- Provisioned clusters run 24/7 — you pay even when idle
- Use Redshift Serverless for variable workloads
- Pause provisioned clusters during off-hours if possible
- RA3 nodes separate compute from storage — scale independently

### 3. Security
- Deploy in a private subnet within your VPC
- Enable encryption at rest (AES-256 or KMS)
- Use IAM roles for S3 access, not embedded credentials
- Enable audit logging

### 4. Loading Data
- Use `COPY` command from S3 for bulk loads (fastest method)
- Avoid row-by-row `INSERT` — extremely slow at scale
- Compress data files before loading

### 5. Always Use Tags
- Tag clusters with environment, project, team, cost center
- Essential for MSP cost tracking — Redshift clusters can be expensive

## Example

A retail company loads daily sales data from S3 into a Redshift cluster using the `COPY` command.
Analysts run SQL queries joining billions of transaction rows with product and customer dimension tables.
Queries that would take minutes on RDS complete in seconds thanks to columnar storage and parallel execution.

## Why It Matters

Redshift is purpose-built for analytical queries over large datasets.
It fills the gap between transactional databases (RDS/Aurora) and raw data lakes (S3 + Athena) for structured, high-performance analytics.

## Official Documentation
- [Amazon Redshift Getting Started](https://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html)
- [Amazon Redshift FAQs](https://aws.amazon.com/redshift/faqs/)

---
← Previous: [Amazon Kinesis](09_amazon_kinesis.md) | [Overview](00_overview.md) | Next: [Amazon SageMaker](24_amazon_sagemaker.md) →
