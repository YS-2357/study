---
tags:
  - computing
  - storage
created_at: 260313-000000
updated_at: 260417-141847
---

# Storage

## What It Is

Storage in computing comes in three types: block (raw disk), file (shared network filesystem), and object (files via API). Performance is measured by IOPS, throughput, and latency.

## How It Works

### Storage Types

| Type | What it is | Access | AWS Service |
|------|-----------|--------|-------------|
| **Block** | Raw storage blocks, OS formats with filesystem | Attached to one instance | [EBS](../aws/101/service/20_amazon_ebs.md) |
| **File** | Network filesystem, multiple servers access simultaneously | NFS/SMB protocol | [EFS](../aws/101/service/22_amazon_efs.md) |
| **Object** | Files stored as objects with metadata, accessed via API | HTTP/API | [S3](../aws/101/service/19_amazon_s3.md) |

### Performance Metrics

| Metric | What it measures | When it matters |
|--------|-----------------|-----------------|
| **IOPS** | Read/write operations per second | Databases, random access |
| **Throughput** (MB/s) | Data transferred per second | Large files, sequential access |
| **Latency** | Time for a single operation | Real-time apps, interactive workloads |

Typical latencies: local SSD < 1ms, EBS SSD 1–3ms, EBS HDD 10–20ms, S3 100–200ms.

### HDD vs SSD

| | HDD | SSD |
|---|-----|-----|
| Mechanism | Spinning magnetic platters | Flash memory (no moving parts) |
| IOPS | 100–200 | 3,000–64,000 |
| Use case | Archives, big data (sequential) | OS drives, databases (random) |
| Cost | Cheaper | More expensive |

### AWS EBS Volume Types

| Type | IOPS | Throughput | Cost | Use case |
|------|------|-----------|------|----------|
| **gp3** (General SSD) | 3,000–16,000 | 125–1,000 MB/s | $0.08/GB | Most workloads (default) |
| **io2** (Provisioned SSD) | Up to 64,000 | Up to 1,000 MB/s | $0.125/GB + IOPS | Mission-critical databases |
| **st1** (Throughput HDD) | Up to 500 | Up to 500 MB/s | $0.045/GB | Big data, logs |
| **sc1** (Cold HDD) | Up to 250 | Up to 250 MB/s | $0.015/GB | Archives (cheapest) |

> **Tip:** gp3 is the right default. Use io2 only for databases that need guaranteed high IOPS. HDD types (st1, sc1) cannot be boot volumes.

## Example

A PostgreSQL database on EC2 needs fast random reads: choose gp3 with provisioned IOPS. A Hadoop cluster processing large log files sequentially: choose st1 for throughput at lower cost.

## Why It Matters

Storage type and performance directly affect application behavior. Choosing the wrong EBS volume type causes either wasted money (io2 for a dev server) or poor performance (sc1 for a database).

---
← Previous: [Virtualization](02_virtualization.md) | [Overview](00_overview.md) | Next: [GPU](04_gpu.md) →
