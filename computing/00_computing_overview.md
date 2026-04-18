---
tags:
  - computing
created_at: 260313-000000
updated_at: 2026-04-18T11:46:13
recent_editor: CLAUDE
---

# Computing Basics — Overview

Fundamental computing concepts for understanding cloud services.

## Study Order

### Hardware & Infrastructure
1. [Architecture](01_architecture.md) — CPU architectures (x86, ARM, 32-bit vs 64-bit); applied in [EC2](../aws/05_amazon_ec2.md).
2. [Virtualization](02_virtualization.md) — Hypervisors, VMs, containers; applied in [EC2](../aws/05_amazon_ec2.md).
3. [Storage](03_storage.md) — Block, file, object storage and performance metrics; applied in [EBS](../aws/20_amazon_ebs.md), [S3](../aws/19_amazon_s3.md), and [EFS](../aws/22_amazon_efs.md).
4. [GPU](04_gpu.md) — GPU computing, CUDA, AWS accelerated instances.

### Workloads & Performance
5. [Workload Types](05_workload_types.md) — General purpose, compute, memory, storage, accelerated; see [EC2 instance types](../aws/05_amazon_ec2.md).
6. [Caching](06_caching.md) — Cache concepts, layers, patterns; applied in [ElastiCache](../aws/13_amazon_elasticache.md) and [CloudFront](../aws/21_amazon_cloudfront.md).

### Communication & Abstraction
7. [Interfaces](07_interfaces.md) — API, CLI, GUI, ENI, programming interfaces; related to [VPC](../aws/04_amazon_vpc.md) and [HTTP](../networking/05_http.md).
8. [Endpoints](08_endpoints.md) — API, AWS service, database, VPC endpoints; related to [VPC](../aws/04_amazon_vpc.md) and [HTTP](../networking/05_http.md).
9. [Decomposition](09_decomposition.md) — Dividing a system into smallest units across frontend, backend, infra, and database layers.

See also [Tooling](../tooling/00_tooling_overview.md) for developer workflow and editor notes.

---
↑ [Home](../home.md)
