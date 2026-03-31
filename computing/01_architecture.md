# CPU Architecture - Computing Basics

**See [Computing Basics Overview](00_overview.md) for all topics.**

---

## What is CPU Architecture?

CPU architecture defines how a processor is designed and how it processes instructions. Different architectures have different instruction sets, performance characteristics, and compatibility.

---

## 32-bit vs 64-bit

### What the numbers mean

**Bit width** = How much data the CPU can process in one operation

- **32-bit:** Processes 32 bits (4 bytes) at a time
- **64-bit:** Processes 64 bits (8 bytes) at a time

### Key differences

| Feature | 32-bit | 64-bit |
|---------|--------|--------|
| **Max RAM** | 4 GB | 16 EB (exabytes) - practically unlimited |
| **Performance** | Slower for large data | Faster for large data |
| **Software compatibility** | Can't run 64-bit apps | Can run 32-bit apps (usually) |
| **Modern use** | Legacy systems only | Standard today |

### Why 32-bit is limited to 4 GB RAM

- 32 bits can represent 2^32 = 4,294,967,296 different values
- Each value represents 1 byte of memory address
- 4,294,967,296 bytes = 4 GB

### Why 64-bit matters

**Example: Processing large numbers**
- 32-bit: Max integer = 2,147,483,647 (needs multiple operations for bigger numbers)
- 64-bit: Max integer = 9,223,372,036,854,775,807 (handles much larger numbers in one operation)

**Real-world impact:**
- **Databases:** Can use more RAM for caching
- **Video editing:** Can process larger files
- **Scientific computing:** Can handle bigger datasets
- **Modern applications:** Require 64-bit for performance

### In AWS context

When choosing AMI:
- **64-bit (x86)** - Standard for most workloads (Intel/AMD processors)
- **32-bit (x86)** - Legacy only, rarely used
- **64-bit (Arm)** - AWS Graviton processors (better price/performance)

**MSP recommendation:** Always use 64-bit unless supporting legacy 32-bit-only software

---

## x86 vs ARM Architecture

### x86 (Intel/AMD)

**What it is:**
- Architecture developed by Intel (8086 processor in 1978)
- Used by Intel and AMD processors
- Dominant in desktops, laptops, servers

**Characteristics:**
- **CISC (Complex Instruction Set Computing)** - Many complex instructions
- **High performance** - Optimized for single-threaded performance
- **Power hungry** - Uses more electricity
- **Wide compatibility** - Most software written for x86

**x86 variants:**
- **x86** - Original 32-bit architecture
- **x86_64 (or x64, AMD64)** - 64-bit extension (what we use today)

### ARM (Advanced RISC Machine)

**What it is:**
- Architecture developed by ARM Holdings (1985)
- Used in mobile devices, tablets, AWS Graviton processors
- Growing in servers and desktops (Apple M1/M2/M3)

**Characteristics:**
- **RISC (Reduced Instruction Set Computing)** - Simple, efficient instructions
- **Power efficient** - Uses less electricity (better for battery, cooling, cost)
- **Good performance** - Especially for parallel workloads
- **Growing compatibility** - More software being ported to ARM

**ARM variants:**
- **ARM32** - 32-bit (older mobile devices)
- **ARM64 (or AArch64)** - 64-bit (modern devices, AWS Graviton)

### x86 vs ARM Comparison

| Feature | x86 (Intel/AMD) | ARM |
|---------|-----------------|-----|
| **Power efficiency** | Lower | Higher (30-40% less power) |
| **Cost** | Higher | Lower (AWS Graviton instances ~20% cheaper) |
| **Performance** | Excellent single-thread | Excellent multi-thread |
| **Software compatibility** | Widest | Growing (most modern software supports ARM) |
| **Use cases** | General purpose, legacy apps | Cost-sensitive, modern apps, mobile |

### CISC vs RISC

**CISC (Complex Instruction Set Computing) - x86:**
- One instruction can do multiple operations
- Example: `MULT` instruction multiplies two numbers in one step
- **Pros:** Fewer instructions needed, easier to program
- **Cons:** More complex hardware, uses more power

**RISC (Reduced Instruction Set Computing) - ARM:**
- Each instruction does one simple operation
- Example: Multiply requires multiple simple instructions (load, multiply, store)
- **Pros:** Simpler hardware, more power efficient, easier to optimize
- **Cons:** More instructions needed for same task

**Modern reality:** The distinction is blurring - both architectures borrow from each other

---

## In AWS Context

### AMI Architecture Options

When launching EC2 instance, you see:

1. **64-bit (x86)** - Intel/AMD processors
   - Most common
   - Widest software compatibility
   - Instance types: t3, m5, c5, r5, etc.

2. **64-bit (Arm)** - AWS Graviton processors
   - 20-40% better price/performance
   - Lower cost
   - Instance types: t4g, m6g, c6g, r6g, etc. (note the 'g' suffix)

3. **64-bit (Mac)** - Apple Mac hardware
   - For iOS/macOS development
   - Instance types: mac1, mac2

4. **32-bit (x86)** - Legacy only
   - Rarely available
   - Only for old applications that can't run on 64-bit

### Choosing Architecture

**Use 64-bit (x86) when:**
- Running legacy software that only supports x86
- Need specific x86-only features
- Maximum single-threaded performance needed
- Software vendor only supports x86

**Use 64-bit (Arm) when:**
- Running modern applications (Java, Python, Node.js, Go, Rust, .NET)
- Cost optimization is priority
- Workload is multi-threaded
- Application is containerized (Docker)

**MSP recommendation:**
- **New projects:** Start with ARM (Graviton) - better cost/performance
- **Existing projects:** Test on ARM, migrate if compatible
- **Legacy apps:** Stay on x86 if migration cost > savings

### Graviton Performance Examples

AWS Graviton2/Graviton3 (ARM) vs x86:
- **Web servers:** 40% better price/performance
- **Databases:** 35% better price/performance  
- **Caching:** 50% better price/performance
- **Video encoding:** 30% better price/performance

**Real cost example:**
- m5.large (x86): $0.096/hour
- m6g.large (ARM): $0.077/hour
- Savings: 20% (~$165/month per instance)

---

## Boot Mode (UEFI vs BIOS)

### BIOS (Basic Input/Output System)

**What it is:**
- Legacy boot firmware from 1980s
- Initializes hardware and loads operating system

**Limitations:**
- 16-bit mode
- 2 TB disk size limit
- Slower boot
- MBR (Master Boot Record) partition table

### UEFI (Unified Extensible Firmware Interface)

**What it is:**
- Modern replacement for BIOS (since 2005)
- More features, faster, more secure

**Advantages:**
- 64-bit mode
- 9 ZB (zettabytes) disk size limit
- Faster boot
- GPT (GUID Partition Table)
- Secure Boot (prevents malware)
- Network boot support

### In AWS AMIs

**Boot mode options:**
- **legacy-bios** - Old BIOS mode (legacy only)
- **uefi** - UEFI mode (modern, recommended)
- **uefi-preferred** - Tries UEFI first, falls back to BIOS if needed

**MSP recommendation:** Use `uefi` or `uefi-preferred` for all new instances

---

## Virtualization Type (HVM vs PV)

### HVM (Hardware Virtual Machine)

**What it is:**
- Full hardware virtualization
- Guest OS runs as if on physical hardware
- Uses CPU virtualization extensions (Intel VT-x, AMD-V)

**Advantages:**
- Better performance
- Supports all instance types
- Can use enhanced networking
- Can use GPU
- Modern standard

### PV (Paravirtualization)

**What it is:**
- Guest OS is modified to work with hypervisor
- OS knows it's virtualized

**Status:**
- **Deprecated** - AWS no longer supports new PV instances
- Legacy only

**MSP recommendation:** Always use HVM (it's the only option for modern instances)

---

## Summary for AWS

### Architecture + OS Combinations

Architecture (CPU) and OS are two separate choices. Not all combinations exist on AWS:

| Architecture | Linux | Windows | macOS |
|---|---|---|---|
| **x86_64 (Intel/AMD)** | ✅ Most common | ✅ .NET, AD, SQL Server | ✅ mac1.metal |
| **arm64 (Graviton)** | ✅ Best price/performance | ❌ Not available | — |
| **arm64 (Apple M1/M2)** | — | — | ✅ mac2.metal |

OS cost on EC2:
- **Linux** — free (no OS license cost)
- **Windows** — extra cost (license included in hourly price)
- **macOS** — extra cost (dedicated Mac hardware, 24h minimum)

Think of it as: architecture = engine type (diesel vs electric), OS = car body (sedan vs truck). You need both.

**When choosing AMI, look for:**
- ✅ **64-bit** (not 32-bit)
- ✅ **ARM (Graviton)** for cost savings (if compatible)
- ✅ **x86** for legacy/specific software requirements
- ✅ **uefi-preferred** boot mode
- ✅ **hvm** virtualization

**Cross-reference:**
- See [EC2 Instance Types](../aws/101/aws_services/05_amazon_ec2.md#instance-types-overview) for AWS-specific instance families
- See [AMI Catalog](../aws/101/aws_services/05_amazon_ec2.md#ami-amazon-machine-image) for selecting AMIs in AWS Console
