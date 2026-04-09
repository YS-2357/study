# Computing Basics — Overview

Fundamental computing concepts for understanding cloud services.

## Study Order

### Hardware & Infrastructure
1. [Architecture](01_architecture.md) — CPU architectures (x86, ARM, 32-bit vs 64-bit).
2. [Virtualization](02_virtualization.md) — Hypervisors, VMs, containers.
3. [Storage](03_storage.md) — Block, file, object storage and performance metrics.
4. [GPU](04_gpu.md) — GPU computing, CUDA, AWS accelerated instances.

### Workloads & Performance
5. [Workload Types](05_workload_types.md) — General purpose, compute, memory, storage, accelerated.
6. [Caching](06_caching.md) — Cache concepts, layers, patterns.

### Communication & Abstraction
7. [Interfaces](07_interfaces.md) — API, CLI, GUI, ENI, programming interfaces.
8. [Endpoints](08_endpoints.md) — API, AWS service, database, VPC endpoints.
9. [WSL Terminal and VS Code Workflow](09_wsl_terminal_and_vscode.md) — Navigate folders, inspect files, and open the repo in VS Code from WSL.
10. [Vim and Neovim](10_vim_and_neovim.md) — Terminal editors, WSL feasibility, pros/cons, and differences from VS Code and nano.
11. [Cucumber](11_cucumber.md) — Plain-language acceptance tests and why Behavior-Driven Development can clarify ideas even in solo projects.
12. [Obsidian vs Notion](12_obsidian_vs_notion.md) — File-first notes versus workspace-first collaboration for Git and AI-assisted workflows.

## Cross-references

- Architecture, Virtualization → [EC2](../aws/101/aws_services/05_amazon_ec2.md)
- Storage → [EBS](../aws/101/aws_services/20_amazon_ebs.md), [S3](../aws/101/aws_services/19_amazon_s3.md), [EFS](../aws/101/aws_services/22_amazon_efs.md)
- Caching → [ElastiCache](../aws/101/aws_services/13_amazon_elasticache.md), [CloudFront](../aws/101/aws_services/21_amazon_cloudfront.md)
- Interfaces, Endpoints → [VPC](../aws/101/aws_services/04_amazon_vpc.md), [HTTP](../networking/05_http.md)
- Workload Types → [EC2 Instance Types](../aws/101/aws_services/05_amazon_ec2.md)
