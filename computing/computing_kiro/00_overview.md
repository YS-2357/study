# Computing Basics - Overview

This folder contains fundamental computing concepts that are essential for understanding cloud services but are not specific to AWS.

## Files

### Hardware & Infrastructure
1. **[Architecture](01_architecture.md)** - CPU architectures (x86, ARM, 32-bit vs 64-bit)
2. **[Virtualization](02_virtualization.md)** - Hypervisors, VMs, containers
3. **[Storage](03_storage.md)** - Block storage, file systems, IOPS, throughput
4. **[GPU](04_gpu.md)** - Graphics processing, parallel computing, CUDA, ML acceleration

### Workloads & Performance
5. **[Workload Types](05_workload_types.md)** - General purpose, compute, memory, storage optimized workloads
6. **[Caching](06_caching.md)** - Cache concepts (hit/miss, TTL, eviction), layers (CPU → CDN), patterns (cache-aside, write-through), Valkey vs Redis vs Memcached

### Communication & Abstraction
7. **[Interfaces & Endpoints](07_interfaces_and_endpoints.md)** - Interfaces (API, CLI, GUI, ENI), endpoints (API, AWS service, database, VPC), how systems connect

---

## How to Use

**For AWS beginners:**
- Start with [Architecture](01_architecture.md) and [Virtualization](02_virtualization.md) — understand what EC2 runs on
- Then [Storage](03_storage.md) — understand EBS, S3 storage concepts
- [Workload Types](05_workload_types.md) — understand EC2 instance families

**For deeper understanding:**
- [Caching](06_caching.md) — understand ElastiCache, CloudFront, DAX
- [Interfaces & Endpoints](07_interfaces_and_endpoints.md) — understand APIs, VPC endpoints, ENIs

**Cross-references:**
- Caching → [ElastiCache](../../aws/101/aws_services_kiro/13_amazon_elasticache.md), [CloudFront](../../aws/101/aws_services_kiro/21_amazon_cloudfront.md)
- Interfaces & Endpoints → [VPC](../../aws/101/aws_services_kiro/04_amazon_vpc.md), [HTTP](../../networking/networking_kiro/05_http.md)
- Virtualization → [EC2](../../aws/101/aws_services_kiro/05_amazon_ec2.md), [Lambda](../../aws/101/aws_services_kiro/07_aws_lambda.md)
- Storage → [EBS](../../aws/101/aws_services_kiro/20_amazon_ebs.md), [S3](../../aws/101/aws_services_kiro/19_amazon_s3.md)

---

**Note:** These are general computing concepts. For AWS-specific implementations, see the main `aws_services_kiro/` folder.
