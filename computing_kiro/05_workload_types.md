# Workload Types - Computing Basics

**See [Computing Basics Overview](00_overview.md) for all topics.**

This guide explains different types of computing workloads and why different hardware is optimized for each.

---

## General Purpose Workloads

### What "General Purpose" Means

**Balanced resources** - Equal emphasis on CPU, memory, and networking

**Like:** A Swiss Army knife - good at many things, not specialized

**Use cases:**
- Web servers
- Application servers
- Small/medium databases
- Development environments
- Code repositories

**Why balanced matters:**
- Web server needs: CPU (process requests) + Memory (cache data) + Network (serve users)
- No single resource dominates
- Most common workload type

**AWS families:** T (burstable), M (balanced), Mac (macOS)

---

## Burstable Performance

### What "Burstable" Means

**Baseline + burst capability** - Low baseline CPU with ability to burst higher when needed

**How it works:**
1. **Baseline:** Constant low CPU (e.g., 10% of 1 vCPU)
2. **Earn credits:** When below baseline, earn CPU credits
3. **Spend credits:** When need more CPU, spend credits to burst
4. **Run out:** If credits depleted, throttled to baseline

**Example: t3.micro**
- Baseline: 10% of 1 vCPU (always available)
- Earns: 12 credits/hour when idle
- Spends: 6 credits/minute when at 100% CPU
- Can burst: 20 minutes at 100% CPU if fully credited

**Real-world scenario:**
- Blog website: Idle 23 hours/day (earning credits)
- Traffic spike: 1 hour/day high traffic (spending credits)
- Perfect fit: Cheap baseline, burst when needed

**When to use:**
- Variable workloads (not constant high CPU)
- Development/test
- Small websites
- Microservices

**When NOT to use:**
- Sustained high CPU (will run out of credits)
- Predictable performance needed

**AWS families:** T2, T3, T4g

---

## Compute Optimized

### What "Compute Optimized" Means

**High CPU-to-memory ratio** - More powerful processors, less memory per vCPU

**Why:** Some workloads need fast CPU but not much memory

**Use cases:**
- **Batch processing** - Process millions of records (CPU-heavy, small data per record)
- **Scientific modeling** - Complex calculations (CPU-heavy math)
- **Gaming servers** - Game logic, physics calculations
- **Video encoding** - Compress video (CPU-intensive)
- **High-traffic web servers** - Many concurrent requests (CPU-bound)
- **Ad serving** - Fast response, simple logic

**Example workload: Video encoding**
- Read video file (I/O)
- Compress each frame (CPU-intensive math)
- Write compressed file (I/O)
- Bottleneck: CPU, not memory

**Comparison:**
- **Compute optimized (C family):** 2 GB RAM per vCPU
- **General purpose (M family):** 4 GB RAM per vCPU
- **Memory optimized (R family):** 8 GB RAM per vCPU

**AWS families:** C (compute), Hpc (high-performance computing)

### High-Performance Computing (HPC)

**What HPC means:** Scientific/engineering workloads requiring massive parallel computation

**Characteristics:**
- Tightly coupled parallel jobs
- Low-latency networking (MPI - Message Passing Interface)
- High network bandwidth between nodes

**Use cases:**
- Weather forecasting
- Computational fluid dynamics
- Molecular modeling
- Seismic analysis
- Financial risk modeling

**AWS families:** Hpc6a, Hpc7a, Hpc7g

---

## Memory Optimized

### What "Memory Optimized" Means

**High memory-to-CPU ratio** - Large amounts of RAM per vCPU

**Why:** Some workloads need to keep large datasets in memory

**Use cases:**
- **In-memory databases** - Redis, Memcached (entire dataset in RAM)
- **Large databases** - PostgreSQL, MySQL with large caches
- **Big data processing** - Spark, Hadoop (process data in memory)
- **Real-time analytics** - Process streaming data in memory
- **SAP HANA** - In-memory database for ERP

**Example workload: In-memory database (Redis)**
- Store 100 GB dataset in RAM
- Sub-millisecond access times
- CPU usage: Low (simple key-value lookups)
- Memory usage: High (entire dataset in RAM)
- Bottleneck: Memory, not CPU

**Why memory matters:**
- **RAM access:** ~100 nanoseconds
- **SSD access:** ~100 microseconds (1000x slower)
- **HDD access:** ~10 milliseconds (100,000x slower)

**Keeping data in RAM = 1000-100,000x faster**

**AWS families:**
- **R** - Standard memory optimized (8 GB RAM per vCPU)
- **X** - Extra memory (16+ GB RAM per vCPU)
- **High Memory** - Massive memory (up to 24 TB RAM)
- **Z** - High frequency + memory

### High Memory Instances

**What they are:** Instances with massive amounts of RAM (up to 24 TB)

**Use cases:**
- **SAP HANA** - In-memory ERP database (requires 6-24 TB RAM)
- **Large in-memory databases**
- **Genomics** - Process entire genome in memory

**AWS instances:** u-6tb1 (6 TB), u-12tb1 (12 TB), u-24tb1 (24 TB)

**Cost:** Very expensive (~$100,000/month for u-24tb1)

---

## Storage Optimized

### What "Storage Optimized" Means

**High local storage throughput** - Fast local disks (NVMe SSD or HDD)

**Why:** Some workloads need to read/write massive amounts of data locally

**Use cases:**
- **NoSQL databases** - Cassandra, MongoDB (high I/O)
- **Data warehouses** - Redshift, Hadoop (large datasets)
- **Distributed file systems** - HDFS, Lustre
- **Log processing** - Elasticsearch, Splunk
- **Cache servers** - Large local cache

**Storage types:**
- **NVMe SSD** - Ultra-fast (millions of IOPS)
- **HDD** - High capacity, lower cost (throughput-optimized)

### I/O Performance Metrics

**IOPS (Input/Output Operations Per Second):**
- How many read/write operations per second
- Important for: Databases, random access

**Throughput (MB/s):**
- How much data transferred per second
- Important for: Big data, sequential access

**See [Storage Basics](03_storage.md) for detailed explanation.**

### AWS Storage Families

**I family (NVMe SSD):**
- **I3** - Up to 3.3 million IOPS per instance
- **I4i** - Up to 30 GB/s throughput
- Use case: High-performance databases (Cassandra, MongoDB)

**D family (Dense HDD):**
- **D3** - Up to 336 TB HDD storage per instance
- **D3en** - Up to 336 TB + enhanced networking
- Use case: Data warehouses, Hadoop, MapReduce

**H family (High throughput HDD):**
- **H1** - Up to 16 TB HDD per instance
- Use case: MapReduce, distributed file systems

---

## Accelerated Computing

### What "Accelerated Computing" Means

**Specialized hardware accelerators** - GPUs, custom chips, FPGAs for specific workloads

**Why:** Some tasks are 10-100x faster on specialized hardware

### GPU Instances (Graphics Processing Unit)

**What GPUs do:** Parallel processing (thousands of simple operations simultaneously)

**See [GPU Basics](04_gpu.md) for detailed explanation.**

**Use cases:**
- **Machine learning training** - Train neural networks
- **ML inference** - Run trained models
- **3D rendering** - Graphics, animation
- **Video processing** - Encoding, transcoding
- **Scientific computing** - Simulations, modeling

**AWS families:**
- **P** - Training (NVIDIA A100, H100)
- **G** - Graphics + inference (NVIDIA T4, A10G, L4)

### AWS Custom Chips

**Inferentia (ML Inference):**
- Custom chip designed by AWS for ML inference
- 70% lower cost than GPU for inference
- Use case: Deploy trained models at scale

**Trainium (ML Training):**
- Custom chip designed by AWS for ML training
- 50% lower cost than GPU for training
- Use case: Train large models cost-effectively

**AWS families:**
- **Inf** - Inferentia (Inf1, Inf2)
- **Trn** - Trainium (Trn1, Trn1n)

### Deep Learning Instances

**DL family:**
- Optimized for deep learning frameworks (PyTorch, TensorFlow)
- Gaudi accelerators (by Habana Labs, acquired by Intel)
- Alternative to NVIDIA GPUs

**AWS families:** DL1, DL2q

### Video Transcoding

**What transcoding is:** Convert video from one format/resolution to another

**Example:** 4K video → 1080p, 720p, 480p for different devices

**Why specialized hardware:** Video encoding is computationally intensive

**AWS family:** VT1 (Xilinx video transcoding cards)

**Use case:** Streaming services (Netflix-style), video platforms

### FPGA (Field-Programmable Gate Array)

**What FPGA is:** Programmable hardware - you design custom circuits

**Why:** For very specific workloads, custom hardware is 10-100x faster than CPU

**Use cases:**
- Genomics (DNA sequencing)
- Financial analytics (real-time risk calculations)
- Video processing (custom codecs)
- Network security (packet inspection)

**AWS family:** F1

**Note:** Very specialized, requires hardware design skills (Verilog/VHDL)

---

## Processor Types

### ARM vs x86

**See [CPU Architecture](01_architecture.md) for detailed explanation.**

**x86 (Intel/AMD):**
- Traditional server processors
- Widest software compatibility
- Higher cost

**ARM (AWS Graviton):**
- Power-efficient RISC architecture
- 20-40% better price/performance
- Growing software compatibility

**AWS Graviton suffix: 'g'**
- Examples: m6g, c7g, r6g
- Recommendation: Use Graviton for cost savings (if software compatible)

### AMD vs Intel

**AMD:**
- Competitive performance
- Often lower cost
- Good for compute-intensive workloads

**Intel:**
- Broad compatibility
- Consistent performance
- Industry standard

**AWS AMD suffix: 'a'**
- Examples: m5a, c5a, r5a

**AWS Intel suffix: 'i'**
- Examples: m6i, c6i, r6i

---

## Special Features (Suffixes)

### Enhanced Networking ('n' suffix)

**What it is:** Higher network bandwidth and lower latency

**How:** Uses SR-IOV (hardware-level network virtualization)

**Use cases:**
- High-throughput applications
- Distributed computing
- Network-intensive workloads

**Examples:** m5n, c5n, r5n

**Network performance:**
- Standard: Up to 10 Gbps
- Enhanced ('n'): Up to 100 Gbps

### Instance Store ('d' suffix)

**What it is:** Local NVMe SSD storage physically attached to host server

**Characteristics:**
- Very fast (low latency)
- Ephemeral (data lost when instance stops)
- Included in instance price

**Use cases:**
- Temporary data
- Cache
- Scratch space
- Databases with replication (data can be rebuilt)

**Examples:** m5d, c5d, r5d

**vs EBS:**
- **Instance store:** Fast, ephemeral, included
- **EBS:** Persistent, network-attached, separate cost

### Extra Storage/Memory ('e' suffix)

**What it is:** More storage or memory than standard variant

**Examples:**
- **r5e** - More memory than r5
- **i3en** - More storage than i3

### High Frequency ('z' suffix)

**What it is:** Higher CPU clock speed (4.0+ GHz)

**Use cases:**
- Single-threaded performance critical
- Gaming servers
- Electronic Design Automation (EDA)

**Example:** m5zn (high frequency + enhanced networking)

---

## macOS Instances

### Mac Family

**What they are:** EC2 instances running on Apple Mac hardware

**Use cases:**
- iOS app development (Xcode)
- macOS app development
- CI/CD for Apple platforms

**Requirements:**
- Minimum allocation: 24 hours (Apple licensing)
- Can't stop/start like regular instances

**AWS families:** mac1 (Intel), mac2 (Apple M1/M2)

---

## Summary Table

| Category | Families | CPU:Memory Ratio | Use Case |
|----------|----------|------------------|----------|
| **General Purpose** | T, M, Mac | 1:4 | Balanced workloads |
| **Burstable** | T2, T3, T4g | 1:4 | Variable CPU usage |
| **Compute** | C, Hpc | 1:2 | CPU-intensive |
| **Memory** | R, X, Z, High Memory | 1:8+ | Memory-intensive |
| **Storage** | I, D, H | Varies | I/O-intensive |
| **GPU** | P, G | Varies | ML, graphics |
| **Custom Chips** | Inf, Trn, DL, VT, F | Varies | Specialized workloads |

**Cross-reference:**
- See [EC2 Instance Types](../aws_services_kiro/05_amazon_ec2.md#instance-types-overview) for AWS-specific details
- See [CPU Architecture](01_architecture.md) for processor fundamentals
- See [GPU](04_gpu.md) for GPU computing details
- See [Storage](03_storage.md) for storage performance metrics
