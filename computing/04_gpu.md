# GPU - Computing Basics

**See [Computing Basics Overview](00_overview.md) for all topics.**

**Sources:**
- [NVIDIA - What is a GPU?](https://www.nvidia.com/en-us/graphics-cards/what-is-a-gpu/)
- [AWS EC2 Accelerated Computing](https://aws.amazon.com/ec2/instance-types/#Accelerated_Computing)
- [NVIDIA CUDA Documentation](https://docs.nvidia.com/cuda/)
- [AWS Inferentia](https://aws.amazon.com/machine-learning/inferentia/)

---

## What is a GPU?

**GPU (Graphics Processing Unit)** = Processor designed for parallel processing of many simple tasks simultaneously

Originally designed for rendering graphics (pixels on screen), now widely used for AI/ML, scientific computing, and data processing.

---

## CPU vs GPU

### CPU (Central Processing Unit)

- **Few powerful cores** (4-128 cores)
- **Optimized for sequential tasks** - One complex task at a time, very fast
- **Large cache** - Fast access to frequently used data
- **General purpose** - Can do anything

**Analogy:** A few expert chefs who can cook any dish perfectly

### GPU (Graphics Processing Unit)

- **Thousands of small cores** (hundreds to thousands)
- **Optimized for parallel tasks** - Many simple tasks simultaneously
- **High memory bandwidth** - Move large amounts of data fast
- **Specialized** - Best for repetitive, parallel computations

**Analogy:** Thousands of line cooks who each do one simple task very fast

### Comparison

| Feature | CPU | GPU |
|---------|-----|-----|
| **Cores** | 4-128 (powerful) | 1,000-16,000+ (simple) |
| **Clock speed** | 3-5 GHz | 1-2 GHz |
| **Best for** | Sequential, complex logic | Parallel, repetitive math |
| **Memory** | System RAM (up to TBs) | VRAM (8-80 GB) |
| **Latency** | Low (fast single task) | Higher (but massive throughput) |

### When CPU is better

- Web servers
- Databases
- Business applications
- Operating system tasks
- Single-threaded workloads

### When GPU is better

- Machine learning training
- AI inference
- Video encoding/decoding
- 3D rendering
- Scientific simulations
- Cryptocurrency mining

---

## GPU Architecture

### Cores (CUDA Cores / Stream Processors)

**NVIDIA: CUDA Cores**
- Basic processing units
- Each core handles one operation per clock cycle
- Thousands of cores work in parallel

**AMD: Stream Processors**
- AMD's equivalent of CUDA cores
- Similar concept, different architecture

### VRAM (Video RAM)

**What it is:** Dedicated memory on the GPU

- **Separate from system RAM** - GPU has its own memory
- **High bandwidth** - Much faster than system RAM for GPU tasks
- **Size matters for AI/ML** - Larger models need more VRAM

**Common VRAM sizes:**
- Consumer: 8-24 GB (gaming, light ML)
- Professional: 24-80 GB (AI training, scientific computing)

**Source:** [NVIDIA A100 Datasheet](https://www.nvidia.com/en-us/data-center/a100/)
- A100: 40 GB or 80 GB HBM2e
- Memory bandwidth: 2 TB/s

### Tensor Cores (NVIDIA)

**What it is:** Specialized cores for matrix operations (AI/ML)

- **Purpose:** Accelerate deep learning training and inference
- **How:** Perform matrix multiply-and-accumulate in one operation
- **Speed:** Up to 10x faster than CUDA cores for AI workloads

**Source:** [NVIDIA Tensor Core Technology](https://www.nvidia.com/en-us/data-center/tensor-cores/)

**Generations:**
- 1st gen: Volta (V100) - 2017
- 2nd gen: Turing (T4) - 2018
- 3rd gen: Ampere (A100) - 2020
- 4th gen: Hopper (H100) - 2022
- 5th gen: Blackwell (B200) - 2024

---

## NVIDIA GPU Lineup (Data Center)

**Source:** [NVIDIA Data Center GPUs](https://www.nvidia.com/en-us/data-center/products/)

| GPU | VRAM | Tensor Cores | Use Case |
|-----|------|-------------|----------|
| **T4** | 16 GB | Yes (2nd gen) | Inference, light training |
| **V100** | 16/32 GB | Yes (1st gen) | Training (legacy) |
| **A10G** | 24 GB | Yes (3rd gen) | Graphics, inference |
| **A100** | 40/80 GB | Yes (3rd gen) | Training, HPC |
| **H100** | 80 GB | Yes (4th gen) | Large model training |
| **L4** | 24 GB | Yes (4th gen) | Inference, video |

---

## CUDA (Compute Unified Device Architecture)

**Source:** [NVIDIA CUDA Zone](https://developer.nvidia.com/cuda-zone)

**What it is:** NVIDIA's programming platform for GPU computing

- **CUDA Toolkit** - Libraries, compiler, tools for GPU programming
- **Languages:** C, C++, Fortran, Python (via libraries)
- **NVIDIA only** - Does not work on AMD GPUs

**Why it matters:**
- Most AI/ML frameworks use CUDA (PyTorch, TensorFlow)
- Industry standard for GPU computing
- Massive ecosystem of libraries

**Key CUDA libraries:**
- **cuDNN** - Deep neural network library
- **cuBLAS** - Linear algebra
- **TensorRT** - Inference optimization
- **NCCL** - Multi-GPU communication

---

## AWS GPU Instance Types

**Source:** [AWS EC2 Instance Types - Accelerated Computing](https://aws.amazon.com/ec2/instance-types/#Accelerated_Computing)

### P Family (Training / HPC)

**Purpose:** Machine learning training, high-performance computing

| Instance | GPU | VRAM | Use Case |
|----------|-----|------|----------|
| **p3.2xlarge** | 1x V100 | 16 GB | Small training jobs |
| **p3.8xlarge** | 4x V100 | 64 GB | Medium training |
| **p3.16xlarge** | 8x V100 | 128 GB | Large training |
| **p4d.24xlarge** | 8x A100 | 320 GB | Large model training |
| **p5.48xlarge** | 8x H100 | 640 GB | Largest model training |

### G Family (Graphics / Inference)

**Purpose:** Graphics rendering, video processing, ML inference

| Instance | GPU | VRAM | Use Case |
|----------|-----|------|----------|
| **g4dn.xlarge** | 1x T4 | 16 GB | Inference, light graphics |
| **g5.xlarge** | 1x A10G | 24 GB | Graphics, inference |
| **g5.48xlarge** | 8x A10G | 192 GB | Heavy graphics workloads |
| **g6.xlarge** | 1x L4 | 24 GB | Inference, video |

### Inf Family (AWS Inferentia)

**Source:** [AWS Inferentia](https://aws.amazon.com/machine-learning/inferentia/)

**Purpose:** ML inference at lowest cost

| Instance | Chip | Use Case |
|----------|------|----------|
| **inf1.xlarge** | 1x Inferentia | Cost-effective inference |
| **inf2.xlarge** | 1x Inferentia2 | Better inference performance |
| **inf2.48xlarge** | 12x Inferentia2 | Large model inference |

**AWS Inferentia:**
- Custom chip designed by AWS (not NVIDIA)
- Optimized specifically for ML inference
- Up to 70% lower cost than GPU instances for inference
- Supports PyTorch, TensorFlow via AWS Neuron SDK

### Trn Family (AWS Trainium)

**Source:** [AWS Trainium](https://aws.amazon.com/machine-learning/trainium/)

**Purpose:** ML training at lowest cost

| Instance | Chip | Use Case |
|----------|------|----------|
| **trn1.2xlarge** | 1x Trainium | Cost-effective training |
| **trn1.32xlarge** | 16x Trainium | Large model training |

**AWS Trainium:**
- Custom chip designed by AWS for training
- Up to 50% cost savings vs GPU for training
- Supports PyTorch, TensorFlow via AWS Neuron SDK

---

## Choosing GPU Instance

**For ML Training:**
1. **Small models:** p3.2xlarge (1x V100) or g5.xlarge (1x A10G)
2. **Medium models:** p3.8xlarge (4x V100) or p4d.24xlarge (8x A100)
3. **Large models (LLMs):** p5.48xlarge (8x H100)
4. **Cost-optimized:** trn1 (AWS Trainium)

**For ML Inference:**
1. **Cost-optimized:** inf2 (AWS Inferentia2) - cheapest
2. **General:** g4dn (T4) or g6 (L4)
3. **High performance:** g5 (A10G)

**For Graphics/Video:**
1. **Rendering:** g5 (A10G)
2. **Video transcoding:** g4dn (T4) or g6 (L4)
3. **Game streaming:** g5 (A10G)

**MSP recommendation:**
- **Start with smallest GPU instance** - Scale up based on actual needs
- **Use Spot Instances** for training (up to 90% savings, training can be checkpointed)
- **Consider Inferentia/Trainium** for cost savings (AWS custom chips)
- **GPU instances are expensive** - Always stop when not in use

---

## Summary

**Key points:**
- **GPU = Parallel processing** (thousands of simple cores)
- **CPU = Sequential processing** (few powerful cores)
- **VRAM** = GPU's dedicated memory (separate from system RAM)
- **CUDA** = NVIDIA's GPU programming platform (industry standard)
- **Tensor Cores** = Specialized for AI/ML matrix operations
- **AWS custom chips** (Inferentia, Trainium) = Cheaper alternative to NVIDIA for ML

**Cross-reference:**
- See [EC2 Instance Types](../aws/101/aws_services/05_amazon_ec2.md#instance-types-overview) for full instance type list
- See [CPU Architecture](01_architecture.md) for CPU fundamentals
