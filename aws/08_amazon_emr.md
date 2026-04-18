---
tags:
  - aws
  - computing
created_at: 2026-03-13T00:00:00
updated_at: 2026-04-18T13:00:00
recent_editor: CLAUDE
---

↑ [Overview](./00_aws_overview.md)

# Amazon EMR (Elastic MapReduce)

## What It Is
Amazon EMR (Elastic MapReduce) is a managed service for running big data frameworks like Hadoop, Spark, Hive, and Presto.

**The problem it solves:**
- You have a HUGE amount of data (terabytes/petabytes)
- A single server can't process it fast enough
- Solution: split the work across many servers working in parallel
- EMR runs those frameworks for you — spin up a cluster, process data, shut it down

**Managed, not fully managed:**
- You choose instance types, cluster size, frameworks
- AWS handles provisioning, configuration, and tuning of the frameworks
- You can SSH into the nodes if needed

### Batch vs Real-time Processing
- **Batch processing** = collect a bunch of work, process it all at once, get results later
- **Real-time processing** = process each item immediately as it arrives

```
Batch:     Collect 1 million log files → process all at once → get report tomorrow morning
Real-time: Each log arrives → process immediately → see result in seconds
```

| | Batch | Real-time |
|---|---|---|
| Example | Analyze yesterday's 10TB of logs overnight | Alert when error rate spikes right now |
| AWS services | EMR, AWS Batch, Glue | Kinesis, Lambda |

EMR is primarily a **batch processing** service.

## How It Works

You create an EMR cluster, selecting a framework (Spark, Hive, etc.), node types, and instance sizes. EMR provisions EC2 instances organized into a primary node (coordinates work), core nodes (store data and run tasks), and optional task nodes (run tasks only). Jobs read input data from S3, distribute work across nodes in parallel, and write results back to S3. Clusters can be terminated after the job completes to avoid idle costs.

## Console Access
- Search "EMR" in AWS Console
- Amazon EMR > Clusters > Create cluster


## Key Concepts

### Frameworks EMR Runs
| Framework | What it does |
|---|---|
| **Hadoop** | Original big data framework (batch processing, older) |
| **Spark** | Faster than Hadoop (in-memory processing, most popular now) |
| **Hive** | SQL-like queries on big data |
| **Presto/Trino** | Fast interactive SQL queries across data sources |
| **HBase** | NoSQL database on top of Hadoop |
| **Flink** | Real-time stream processing |

### Cluster Architecture
- **Primary node** — Manages the cluster, coordinates work distribution
- **Core nodes** — Run tasks AND store data (HDFS)
- **Task nodes** (optional) — Run tasks only, no data storage (good for scaling compute)

### EMR Deployment Options
- **EMR on EC2** — Traditional, you manage the cluster on EC2 instances
- **EMR on EKS** — Run Spark on Amazon EKS (Elastic Kubernetes Service)
- **EMR Serverless** — No cluster to manage, submit jobs and AWS handles compute
  - Best for getting started, no infrastructure decisions

### EMR vs ELB (Common Name Confusion)
These are completely different services — similar abbreviations, nothing in common.

| | EMR (Elastic MapReduce) | ELB (Elastic Load Balancing) |
|---|---|---|
| Purpose | Process massive data in parallel | Distribute network traffic across servers |
| Category | Data / Analytics | Networking |
| What it does | Runs Hadoop/Spark on a cluster of servers to crunch big data | Receives incoming requests and spreads them across multiple EC2/containers |
| Input | Terabytes of data (logs, files, datasets) | User HTTP/TCP requests |
| Output | Processed results (reports, transformed data) | Routed traffic to healthy servers |
| Works with | S3, Hadoop, Spark, Hive | EC2, ECS, Lambda, any compute target |
| Example | "Analyze 10TB of clickstream logs to find user patterns" | "Spread 10,000 web requests/sec across 5 EC2 instances" |
| Runs on | EC2 cluster (or Serverless) | AWS-managed (no instances to manage) |

**EMR** = data processing tool (back-end, batch jobs)
**ELB** = traffic routing tool (front-end, real-time requests)

### EMR vs Other AWS Data Services

| Service | What it does | When to use |
|---|---|---|
| **EMR** | Process massive data with Hadoop/Spark (cluster-based) | Complex ETL, ML training on big data |
| **Kinesis** | Real-time streaming data | Live data ingestion and processing |
| **Redshift** | Data warehouse (SQL on large datasets) | BI dashboards, analytics queries |
| **Athena** | Serverless SQL queries on S3 data | Ad-hoc queries, no cluster needed |
| **Glue** | Serverless ETL (Extract, Transform, Load) | Simpler ETL jobs, data catalog |

### Common Use Cases
- Processing log files at scale
- ETL (Extract, Transform, Load) pipelines
- Machine learning model training on large datasets
- Clickstream analysis
- Genomics data processing


## Precautions

### MAIN PRECAUTION: Clusters Cost Money While Running
- EMR clusters run on EC2 instances — you pay while they're up
- Terminate clusters when processing is done
- Use EMR Serverless or auto-termination to avoid forgotten running clusters
- **Tip:** Set up billing alerts for EMR — a forgotten cluster can be very expensive

### 1. Choose the Right Deployment Option
- **EMR Serverless** — Simplest, no cluster management, good for most jobs
- **EMR on EC2** — More control, needed for complex configurations
- Start with Serverless unless you have a specific reason not to

### 2. Use Spot Instances for Task Nodes
- Task nodes only run compute (no data storage)
- Safe to use Spot Instances (up to 90% cheaper)
- Core nodes should use On-Demand (they store data)

### 3. Store Data in S3, Not HDFS
- HDFS (Hadoop Distributed File System) data is lost when cluster terminates
- Use S3 as your data lake — persistent, cheaper, decoupled from compute
- Process data from S3, write results back to S3

### 4. Security
- Run EMR clusters in a private subnet
- Use security groups to control access
- Enable encryption at rest and in transit
- Use IAM roles for cluster permissions

### 5. Always Use Tags
- Tag clusters with environment, project, team, client, cost center
- Essential for MSP cost tracking — EMR costs can add up fast

## Example

A data team spins up a 10-node EMR cluster with Spark to process 5 TB of raw clickstream logs stored in S3.
The Spark job aggregates page views by user and writes the results to a Parquet dataset in S3.
The cluster shuts down after the job completes, so they only pay for the processing time.

## Why It Matters

EMR lets you run big data frameworks at scale without managing Hadoop or Spark clusters yourself.
Spinning clusters up on demand and shutting them down after keeps costs proportional to actual processing needs.

## Official Documentation
- [Amazon EMR Documentation](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html)
- [Amazon EMR FAQs](https://aws.amazon.com/emr/faqs/)

---
← Previous: [Amazon ElastiCache](13_amazon_elasticache.md) | [Overview](./00_aws_overview.md) | Next: [Amazon Kinesis](09_amazon_kinesis.md) →
