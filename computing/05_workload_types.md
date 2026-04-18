---
tags:
  - computing
created_at: 2026-03-13T00:00:00
updated_at: 2026-04-18T18:37:25
recent_editor: CODEX
---

↑ [Overview](./00_computing_overview.md)

# Workload Types

## What It Is

Different workloads need different hardware ratios. AWS [EC2](../aws/compute/01_amazon_ec2.md) instance families are designed around these workload categories.

## How It Works

### Summary

| Category | CPU:Memory | Families | Use case |
|----------|-----------|----------|----------|
| **General Purpose** | 1:4 | T (burstable), M (balanced) | Web servers, app servers, small DBs |
| **Compute Optimized** | 1:2 | C, Hpc | Batch processing, video encoding, gaming servers |
| **Memory Optimized** | 1:8+ | R, X, Z | In-memory DBs, [large caches](06_caching.md), big data |
| **Storage Optimized** | Varies | I (NVMe SSD), D (HDD), H (HDD) | NoSQL DBs, data warehouses, log processing |
| **Accelerated** | Varies | P, G, Inf, Trn | ML training/inference, graphics, video |

### Burstable (T family)

Low baseline CPU with ability to burst higher when needed. Earns CPU credits when idle, spends them during spikes.

Use when workload is variable (idle most of the time, occasional spikes). Don't use for sustained high CPU — credits will run out.

### Instance Naming

Format: `[Family][Generation][Suffix].[Size]`

| Suffix | Meaning | Example |
|--------|---------|---------|
| `g` | Graviton (ARM) | m6g, c7g |
| `a` | AMD | m5a, c5a |
| `i` | Intel | m6i, c6i |
| `n` | Enhanced networking | m5n, c5n |
| `d` | Instance store (local NVMe) | m5d, c5d |

> **Tip:** Graviton (`g` suffix) instances are ~20% cheaper. See [Architecture](01_architecture.md) for x86 vs ARM details.

## Example

A Redis cache holding 50 GB of data with low CPU usage: choose R family (memory optimized) like r6g.xlarge. A video encoding pipeline that's CPU-bound: choose C family (compute optimized) like c6g.2xlarge.

## Why It Matters

Choosing the wrong instance family wastes money or causes performance problems. A memory-heavy workload on a compute-optimized instance will run out of RAM. A CPU-heavy workload on a memory-optimized instance pays for unused RAM.

---
← Previous: [GPU](04_gpu.md) | [Overview](./00_computing_overview.md) | Next: [Caching](06_caching.md) →
