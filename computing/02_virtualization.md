---
tags:
  - computing
  - container
created_at: 2026-03-13T00:00:00
updated_at: 2026-04-18T13:00:00
recent_editor: CLAUDE
---

↑ [Overview](./00_computing_overview.md)

# Virtualization

## What It Is

Virtualization is running multiple virtual computers (guests) on one physical computer (host). Cloud computing wouldn't exist without it — AWS runs millions of VMs on shared physical servers.

## Analogy

One apartment building (physical server) with many apartments (virtual machines). Each apartment has its own space, but they share the building infrastructure.

## How It Works

### Hypervisors

A hypervisor creates and manages virtual machines.

**Type 1 (Bare Metal)** — runs directly on hardware. Used in production and cloud.
```
VMs (Linux, Windows, ...)
Hypervisor (Xen, KVM)
Physical Hardware
```

**Type 2 (Hosted)** — runs on top of a host OS. Used for development/testing.
```
VMs
Hypervisor (VirtualBox, Parallels)
Host OS (Windows, macOS)
Physical Hardware
```

AWS uses Type 1: Nitro (modern, KVM-based) for instances with number ≥5 (m5, c5, t3, etc.), and Xen (legacy) for older types (t2, m4, c4).

### VMs vs Containers

| Feature | Virtual Machines | Containers |
|---------|------------------|------------|
| Isolation | Strong (separate kernel) | Lighter (shared kernel) |
| Size | 1–10 GB | 10–500 MB |
| Boot time | 30–60 seconds | < 1 second |
| Density | 10–50 per host | 100–1000 per host |
| Use case | Full OS, strong isolation | Microservices, fast scaling |

**Use VMs** when you need different OSes, strong isolation, or legacy apps.
**Use containers** when you need microservices, fast scaling, or consistent dev/prod environments.

AWS services: [EC2](../aws/05_amazon_ec2.md) (VMs), ECS/EKS (container orchestration), [Fargate](../aws/26_aws_fargate.md) (serverless containers), [Lambda](../aws/07_aws_lambda.md) (serverless functions).

### AWS Nitro System

AWS's custom hypervisor + hardware. Offloads networking, storage, and security to dedicated Nitro Cards, giving your VM nearly bare-metal performance with minimal hypervisor overhead.

## Example

You launch an m6g.large [EC2](../aws/05_amazon_ec2.md) instance. AWS allocates a VM on a physical server running the Nitro hypervisor. Your VM gets dedicated CPU and memory (AWS does not overcommit). Networking and [EBS](../aws/20_amazon_ebs.md) storage are handled by Nitro Cards, so your VM's CPU is fully available for your workload.

## Why It Matters

Understanding virtualization explains why EC2 instances have specific CPU/memory allocations, why instance store data is lost when you stop an instance (the VM is deallocated), and why Nitro-based instances perform better than older Xen-based ones.

---
← Previous: [Architecture](01_architecture.md) | [Overview](./00_computing_overview.md) | Next: [Storage](03_storage.md) →
