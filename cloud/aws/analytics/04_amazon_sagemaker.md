---
tags:
  - aws
  - ml
  - computing
created_at: 2026-03-31T00:00:00
updated_at: 2026-04-23T23:41:19
recent_editor: CODEX
source:
  - aws-partner-summit-seoul-2026
---

↑ [Overview](./00_analytics_overview.md)

# Amazon SageMaker AI

## What It Is
Amazon SageMaker AI is a fully managed platform for building, training, and deploying machine learning models.

**The problem it solves:**
- ML workflows have many moving parts: data prep, training, tuning, deployment, monitoring
- Doing this on raw [EC2](../compute/01_amazon_ec2.md) means managing instances, frameworks, scaling, endpoints yourself
- SageMaker provides managed tooling for the entire ML lifecycle

**ML workflow in SageMaker:**
```
Prepare data → Build/train model → Tune hyperparameters → Deploy endpoint → Monitor
     ↑                                                                         |
     └─────────────────── retrain with new data ──────────────────────────────┘
```

### SageMaker vs Other ML Options

| Option | What it does | When to use |
|---|---|---|
| **SageMaker** | Full ML platform (build, train, deploy) | Custom models, full control over training/deployment |
| **[Bedrock](../ai/01_amazon_bedrock.md)** | Managed foundation models (API access) | Use pre-built LLMs without training, GenAI apps |
| **EC2 + frameworks** | DIY ML on raw compute | Maximum control, existing pipelines, custom environments |
| **Comprehend/Rekognition/etc.** | Pre-built AI services (no ML knowledge needed) | Specific tasks (NLP, image analysis) without building models |

## How It Works

You prepare training data in [S3](../storage/01_amazon_s3.md), then launch a managed training job specifying the algorithm, instance type, and S3 paths for input data and output artifacts. SageMaker provisions the instances, runs the training code, saves the model artifact to S3, and terminates the instances. You then create an endpoint from the trained model artifact; SageMaker deploys the model on managed instances that serve real-time predictions via an HTTPS API.

## Console Access
- Search "SageMaker" in AWS Console
- Amazon SageMaker > Studio, Notebooks, Training jobs, or Endpoints


## Key Concepts

### Core Components
- **SageMaker Studio** — Web-based IDE for the full ML workflow (notebooks, experiments, deployment)
- **Notebooks** — Jupyter notebooks for data exploration and prototyping
- **Training jobs** — Managed compute for model training (spins up instances, trains, shuts down)
- **Endpoints** — Managed inference endpoints for serving predictions in real-time
- **Model Registry** — Version and track trained models

### Deployment Options
| Option | Latency | Cost model | When to use |
|---|---|---|---|
| **Real-time endpoints** | Milliseconds | Pay while endpoint is running | Production APIs needing instant responses |
| **Serverless inference** | Cold start possible | Pay per request | Intermittent traffic, cost-sensitive |
| **Batch transform** | Minutes | Pay per job | Large batch predictions, no real-time need |
| **Async inference** | Seconds–minutes | Pay while endpoint is running | Large payloads, queued processing |

### Built-in Algorithms
- SageMaker includes built-in algorithms for common tasks (XGBoost, Linear Learner, Image Classification, etc.)
- You can also bring your own training code in a Docker container
- Supports popular frameworks: PyTorch, TensorFlow, Hugging Face, MXNet


## Precautions

### MAIN PRECAUTION: Endpoints Cost Money While Running
- Real-time endpoints run 24/7 on dedicated instances — you pay even with zero traffic
- A forgotten `ml.p3.2xlarge` endpoint costs ~$900/month
- Use Serverless Inference for dev/test or low-traffic workloads
- Set up auto-scaling or delete endpoints when not needed

### 1. Right-size Training Instances
- Don't default to the largest GPU instance
- Start small, profile, then scale up
- Use Spot Training (managed spot instances) for up to 90% savings on training jobs

### 2. IAM and S3 Access
- SageMaker needs an execution role with S3 access for data and model artifacts
- Follow least-privilege: only grant access to specific buckets/prefixes
- Don't use overly broad `s3:*` permissions

### 3. Data Preparation
- Garbage in = garbage out — invest time in data quality
- Use SageMaker Data Wrangler or Processing jobs for data prep
- Store training data in S3, not on notebook instance storage

### 4. Monitor Endpoints
- Enable CloudWatch metrics and alarms for endpoint health
- Monitor model drift — retrain when prediction quality degrades
- Use SageMaker Model Monitor for automated drift detection

### 5. Always Use Tags
- Tag notebooks, training jobs, endpoints with environment, project, team, cost center
- Essential for MSP cost tracking — ML workloads can be very expensive

## Example

A data scientist uses a SageMaker notebook to explore training data stored in S3.
They launch a managed training job on `ml.m5.xlarge` instances using the built-in XGBoost algorithm.
After training, they deploy the model to a real-time endpoint and test predictions via the endpoint URL.

## Why It Matters

SageMaker removes the infrastructure complexity from machine learning — managed notebooks, training jobs, and endpoints
let teams focus on model quality instead of cluster management.

## SageMaker Catalog

Unified metadata hub for all data and AI assets in SageMaker.

### Data Architecture Evolution

| Era | Architecture | Characteristics |
|-----|-------------|-----------------|
| 2000s | Data Warehouse | Structured, SQL |
| 2010s | Data Lake | Unstructured, low cost |
| 2020s | Lakehouse | Integrated, transactional |
| 2025+ | AI-Ready Platform | Metadata, governance, agents |

**Gartner 2025:** 60% of organizations will fail to realize value from AI by 2027 due to absent data preparation — the data layer is the iceberg below the visible AI/ML surface.

### Catalog Asset Types

4 types: **Data**, **Models**, **Gen AI**, **BI Dashboards** — unified in a single metadata hub integrating S3, Glue, Redshift, Athena, and SageMaker datasets.

### Metadata 6 Elements

1. Table descriptions
2. Column meaning
3. Quality reliability
4. Data lineage
5. Access controls
6. PII tags

### AI Auto-Metadata

- **Asset level:** Summary, Tags, Business Terms, Column Descriptions
- **Column level:** Glossary Terms, Custom Forms, Data Sensitivity

### SageMaker Data Agent

Natural language → analyses and ML development, without writing SQL/Python manually.

- Auto-plans multi-step analysis from a natural language prompt
- Generates SQL and Python code
- Multi-step reasoning across datasets
- Integrated with SageMaker notebook and query editor

**Example workflow:** QuickSight alerts on LINE-03 yield below baseline → IPQC/QC analysis via natural language prompt in notebook → Data Agent generates and executes the analysis automatically.

### Key Catalog Terminology

| Term | Meaning |
|------|---------|
| Metadata | Descriptive information about data assets |
| Data Assets | Datasets, models, dashboards, GenAI apps |
| Producers/Consumers | Teams that publish vs. subscribe to assets |
| Federation | Connecting external catalogs into one view |
| Business Glossary | Shared vocabulary for domain terms |
| Data Lineage | How data flows and transforms across systems |

## AWS Viewpoints

| Perspective | Detail |
|-------------|--------|
| Feasibility | Use SageMaker when you need managed training, tuning, deployment, or data/AI asset governance instead of raw EC2-based ML infrastructure. |
| Disruption | Training jobs are separate from serving endpoints; endpoint changes should be rolled out through new model versions or endpoint variants to avoid interrupting production inference. |
| Pros & Cons | It reduces ML infrastructure work, but real-time endpoints and notebooks can create steady costs if left running. |
| Differences | Bedrock is for consuming foundation models by API; SageMaker is for building, training, hosting, and governing custom ML workflows. |

## Official Documentation
- [Amazon SageMaker Documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)
- [Amazon SageMaker FAQs](https://aws.amazon.com/sagemaker/faqs/)

---
↑ [Overview](./00_analytics_overview.md)

**Related:** [AWS Data Pipeline](./03_aws_data_pipeline.md), [EC2](../compute/01_amazon_ec2.md), [Bedrock](../ai/01_amazon_bedrock.md), [S3](../storage/01_amazon_s3.md)
**Tags:** #aws #ml #computing
