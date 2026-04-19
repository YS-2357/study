---
tags:
  - aws
  - database
created_at: 2026-04-05T00:00:00
updated_at: 2026-04-19T09:11:51
recent_editor: CLAUDE
---

↑ [Overview](./00_analytics_overview.md)

# AWS Data Pipeline

## What It Is
AWS Data Pipeline is a web service for scheduling and orchestrating data movement and transformation between AWS services and on-premises sources.

**Legacy service.** For new projects, AWS recommends using **AWS Glue**, **Step Functions**, or **EventBridge** instead. Data Pipeline is still supported but is not receiving major new features.

**The problem it solves:**
- You need to move data between S3, RDS, DynamoDB, EMR, Redshift on a schedule
- You want retry logic and dependency tracking built in
- Data Pipeline automates these recurring data workflows

**When you'd still encounter it:**
- Maintaining existing pipelines built before Glue/Step Functions existed
- Simple scheduled S3-to-Redshift or S3-to-RDS copy jobs that are already running

### Data Pipeline vs Modern Alternatives

| Service | What it does | When to use |
|---|---|---|
| **Data Pipeline** | Scheduled data movement with retry logic (legacy) | Existing pipelines, simple scheduled copies |
| **AWS Glue** | Serverless ETL + data catalog + crawlers | New ETL jobs, schema discovery, Spark-based transforms |
| **Step Functions** | Workflow orchestration (any AWS service) | Complex multi-step workflows, conditional logic |
| **EventBridge** | Event-driven scheduling and routing | Cron-based triggers, event-driven architectures |
| **MWAA (Airflow)** | Managed Apache Airflow | Complex DAGs, teams already using Airflow |

## How It Works

You define a pipeline as a JSON document specifying data nodes (S3, RDS, DynamoDB, Redshift), activities (copy, EMR job, shell command), preconditions (checks before running), and a schedule. Data Pipeline provisions EC2 instances to execute activities, tracks dependencies, and retries on failure. On the defined schedule, the pipeline checks preconditions and runs activities in order, moving or transforming data between the configured sources and destinations.

## Console Access
- Search "Data Pipeline" in AWS Console
- AWS Data Pipeline > Pipelines


## Key Concepts

### Components
- **Pipeline definition** — JSON that describes the data flow: source, destination, schedule, activities
- **Activities** — The work to perform (copy data, run EMR job, run shell command)
- **Preconditions** — Checks that must pass before an activity runs (e.g., "does this S3 path exist?")
- **Schedule** — When and how often the pipeline runs
- **Data nodes** — Source and destination (S3, RDS, DynamoDB, Redshift)
- **Resources** — Compute that runs the activities (EC2 instances managed by Data Pipeline)

### How It Works
```
Schedule triggers → Preconditions checked → Activity runs on EC2 → Data moves source → destination
                                                    ↓ (failure)
                                              Retry logic kicks in
```


## Precautions

### MAIN PRECAUTION: Consider Newer Services First
- For any new project, evaluate Glue, Step Functions, or EventBridge before choosing Data Pipeline
- Data Pipeline is not deprecated but is effectively in maintenance mode
- Migration path: Glue for ETL, Step Functions for orchestration

### 1. Retry and Error Handling
- Configure retry counts and failure alerts
- Pipelines can silently fail if notifications aren't set up
- Use SNS notifications for pipeline failures

### 2. EC2 Resources
- Data Pipeline spins up EC2 instances to run activities
- These instances cost money — make sure pipelines terminate cleanly
- Use `terminateAfter` settings to avoid runaway instances

### 3. IAM Roles
- Requires two roles: pipeline role (what the pipeline can do) and resource role (what the EC2 instance can do)
- Follow least-privilege for both

### 4. Always Use Tags
- Tag pipelines with environment, project, team, cost center
- Helps track costs from the EC2 instances Data Pipeline creates

## Example

A nightly Data Pipeline job copies new records from an RDS MySQL table to S3 in CSV format.
A precondition checks that the RDS instance is available before starting.
If the copy fails, the pipeline retries three times and sends an SNS alert on final failure.

## Why It Matters

Data Pipeline automates recurring data movement between AWS services with built-in retry and scheduling.
While newer services like Glue and Step Functions are preferred for new projects, existing Data Pipeline jobs are still common in production.

## Official Documentation
- [AWS Data Pipeline Developer Guide](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/what-is-datapipeline.html)

---
↑ [Overview](./00_analytics_overview.md)

**Related:** [Amazon EMR (Elastic MapReduce)](./02_amazon_emr.md), [Amazon SageMaker AI](./04_amazon_sagemaker.md)
**Tags:** #aws #database
