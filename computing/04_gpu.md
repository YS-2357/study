---
tags:
  - computing
  - ml
---
# GPU

## What It Is

A GPU (Graphics Processing Unit) is a processor designed for parallel processing of many simple tasks simultaneously. Originally for graphics, now widely used for AI/ML, scientific computing, and video processing.

## How It Works

### CPU vs GPU

| Feature | CPU | GPU |
|---------|-----|-----|
| Cores | 4–128 (powerful) | 1,000–16,000+ (simple) |
| Best for | Sequential, complex logic | Parallel, repetitive math |
| Use case | Web servers, databases, general apps | ML training, inference, rendering |

> **Tip:** CPU = a few expert chefs. GPU = thousands of line cooks doing one simple task each.

### Key GPU Concepts

- **CUDA Cores** — NVIDIA's basic processing units. Thousands work in parallel.
- **VRAM** — Dedicated GPU memory, separate from system RAM. Larger models need more VRAM.
- **Tensor Cores** — Specialized for AI/ML matrix operations (up to 10x faster than CUDA cores for AI).
- **CUDA** — NVIDIA's programming platform. Most AI frameworks (PyTorch, TensorFlow) use it. NVIDIA-only.

### AWS GPU and Accelerator Instances

| Family | Hardware | Use case |
|--------|----------|----------|
| **P** (p4d, p5) | NVIDIA A100, H100 | ML training, HPC |
| **G** (g4dn, g5, g6) | NVIDIA T4, A10G, L4 | Graphics, inference |
| **Inf** (inf1, inf2) | AWS Inferentia | ML inference (up to 70% cheaper than GPU) |
| **Trn** (trn1) | AWS Trainium | ML training (up to 50% cheaper than GPU) |

> **Tip:** Start with the smallest GPU instance and scale up. Use Spot Instances for training (checkpointable). Consider Inferentia/Trainium for cost savings.

## Example

Training a neural network: each training step multiplies large matrices (weights × inputs). A CPU processes these sequentially. A GPU with thousands of cores processes many matrix elements in parallel, finishing the same step 10–100x faster.

## Why It Matters

GPU instance choice directly affects ML training time and cost. Understanding VRAM limits helps you pick the right instance — a model that doesn't fit in VRAM won't run. AWS custom chips (Inferentia, Trainium) offer significant savings for compatible workloads.

---
← Previous: [Storage](03_storage.md) | [Overview](00_overview.md) | Next: [Workload Types](05_workload_types.md) →
