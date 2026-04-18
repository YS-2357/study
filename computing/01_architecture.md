---
tags:
  - computing
created_at: 2026-03-13T00:00:00
updated_at: 2026-04-18T13:00:00
recent_editor: CLAUDE
---

↑ [Overview](./00_computing_overview.md)

# CPU Architecture

## What It Is

CPU architecture defines how a processor is designed and how it processes instructions. The two main choices in AWS are x86 (Intel/AMD) and ARM (AWS Graviton).

## How It Works

### 32-bit vs 64-bit

Bit width = how much data the CPU processes in one operation.

| Feature | 32-bit | 64-bit |
|---------|--------|--------|
| Max RAM | 4 GB (2^32 bytes) | Practically unlimited |
| Performance | Slower for large data | Faster |
| Modern use | Legacy only | Standard |

> **Tip:** Always use 64-bit in AWS unless supporting legacy 32-bit-only software.

### x86 vs ARM

| Feature | x86 (Intel/AMD) | ARM (AWS Graviton) |
|---------|-----------------|-----|
| Design | CISC (complex instructions) | RISC (simple instructions) |
| Power efficiency | Lower | Higher (30–40% less power) |
| Cost | Higher | ~20% cheaper on AWS |
| Performance | Excellent single-thread | Excellent multi-thread |
| Compatibility | Widest | Growing (most modern software supports ARM) |

**CISC** (x86): one instruction can do multiple operations. More complex hardware.
**RISC** (ARM): each instruction does one simple operation. Simpler, more power-efficient.

### In AWS

| Architecture | AMI suffix | Instance examples |
|---|---|---|
| x86_64 (Intel/AMD) | — | t3, m5, c5, r5 |
| arm64 (Graviton) | `g` | t4g, m6g, c6g, r6g |
| Mac (Intel) | — | mac1.metal |
| Mac (Apple Silicon) | — | mac2.metal |

> **Tip:** Use Graviton (ARM) for new projects — better price/performance. Use x86 for legacy software or when vendors only support x86.

### Boot Mode and Virtualization

- **UEFI** — modern boot firmware (recommended). Faster boot, Secure Boot, large disk support.
- **Legacy BIOS** — old firmware. Use only for legacy AMIs.
- **HVM** — hardware virtualization (standard). All modern EC2 instances use HVM. PV (paravirtualization) is deprecated.

## Example

Choosing an AMI for a new Python web app: select 64-bit ARM (Graviton), Amazon Linux 2023, UEFI boot mode. This gives the best price/performance for a modern application. If the app used a vendor library that only ships x86 binaries, you'd choose x86_64 instead.

## Why It Matters

Architecture choice affects [EC2](../aws/05_amazon_ec2.md) instance cost, performance, and software compatibility. Graviton instances are ~20% cheaper for compatible workloads.

---
[Overview](./00_computing_overview.md) | Next: [Virtualization](02_virtualization.md) →
