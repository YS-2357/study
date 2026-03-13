# Virtualization - Computing Basics

**See [Computing Basics Overview](00_overview.md) for all topics.**

---

## What is Virtualization?

**Virtualization** = Running multiple virtual computers (guests) on one physical computer (host)

**Simple analogy:** One apartment building (physical server) with many apartments (virtual machines). Each apartment has its own space, but they share the same building infrastructure.

---

## Why Virtualization?

### Before virtualization (1990s-2000s)

- 1 application = 1 physical server
- Server utilization: 5-15% (wasting 85-95% of capacity!)
- High costs: Hardware, power, cooling, space
- Slow provisioning: Order server → Wait weeks → Install → Configure

### After virtualization (2000s-present)

- 1 physical server = 10-50 virtual machines
- Server utilization: 60-80%
- Lower costs: Share hardware, power, cooling
- Fast provisioning: Create VM in minutes

**Cloud computing wouldn't exist without virtualization** - AWS runs millions of VMs on shared physical servers

---

## Hypervisor (Virtual Machine Monitor)

**Hypervisor** = Software that creates and manages virtual machines

### Type 1 Hypervisor (Bare Metal)

**Runs directly on hardware** (no host OS)

```
┌─────────────────────────────────────┐
│  VM 1    │  VM 2    │  VM 3         │ ← Virtual Machines
│  (Linux) │ (Windows)│  (Linux)      │
├──────────┴──────────┴───────────────┤
│      Type 1 Hypervisor (Xen, KVM)   │ ← Hypervisor
├──────────────────────────────────────┤
│      Physical Hardware (CPU, RAM)    │ ← Physical Server
└──────────────────────────────────────┘
```

**Examples:**
- **VMware ESXi** - Enterprise standard
- **Xen** - Used by AWS (older instances)
- **KVM** - Used by AWS (newer instances), Linux kernel module
- **Microsoft Hyper-V** - Windows Server

**Advantages:**
- Better performance (direct hardware access)
- More efficient
- More secure (smaller attack surface)

**Use case:** Production servers, cloud providers (AWS, Azure, GCP)

### Type 2 Hypervisor (Hosted)

**Runs on top of host OS**

```
┌─────────────────────────────────────┐
│  VM 1    │  VM 2    │  VM 3         │ ← Virtual Machines
│  (Linux) │ (Windows)│  (Linux)      │
├──────────┴──────────┴───────────────┤
│   Type 2 Hypervisor (VirtualBox)    │ ← Hypervisor
├──────────────────────────────────────┤
│   Host OS (Windows, macOS, Linux)   │ ← Operating System
├──────────────────────────────────────┤
│      Physical Hardware (CPU, RAM)    │ ← Physical Computer
└──────────────────────────────────────┘
```

**Examples:**
- **VirtualBox** - Free, open source
- **VMware Workstation** - Desktop virtualization
- **Parallels Desktop** - macOS virtualization

**Advantages:**
- Easy to install (just an application)
- Good for development/testing
- Run on your laptop/desktop

**Disadvantages:**
- Lower performance (extra OS layer)
- More overhead

**Use case:** Development, testing, learning, running Windows on Mac

---

## Virtualization Types

### Full Virtualization (HVM - Hardware Virtual Machine)

**Guest OS doesn't know it's virtualized** - thinks it's running on real hardware

**How it works:**
- Uses CPU virtualization extensions (Intel VT-x, AMD-V)
- Hypervisor intercepts hardware calls
- Guest OS runs unmodified

**Advantages:**
- No OS modification needed
- Can run any OS
- Better performance (hardware acceleration)
- Standard in modern systems

**AWS:** All modern EC2 instances use HVM

### Paravirtualization (PV)

**Guest OS knows it's virtualized** - modified to work with hypervisor

**How it works:**
- Guest OS makes direct calls to hypervisor (hypercalls)
- No hardware emulation needed
- OS must be modified

**Advantages:**
- Lower overhead (no hardware emulation)
- Better performance (in the past)

**Disadvantages:**
- Requires modified OS
- Can't run Windows (needs kernel modification)
- Deprecated technology

**AWS:** PV instances deprecated, no longer available for new instances

---

## Containers vs Virtual Machines

### Virtual Machines

**Each VM has full OS**

```
┌──────────────────────────────────────┐
│ VM 1          │ VM 2          │ VM 3 │
│ ┌──────────┐  │ ┌──────────┐  │ ...  │
│ │   App    │  │ │   App    │  │      │
│ ├──────────┤  │ ├──────────┤  │      │
│ │ Guest OS │  │ │ Guest OS │  │      │ ← Full OS per VM
│ │ (Linux)  │  │ │(Windows) │  │      │
│ └──────────┘  │ └──────────┘  │      │
├───────────────┴───────────────┴──────┤
│         Hypervisor (KVM)             │
├──────────────────────────────────────┤
│         Physical Hardware            │
└──────────────────────────────────────┘
```

**Characteristics:**
- Full OS per VM (1-2 GB+ per VM)
- Boot time: 30-60 seconds
- Strong isolation (separate kernel)
- More overhead

### Containers

**Share host OS kernel**

```
┌──────────────────────────────────────┐
│ Container 1 │ Container 2 │ Container 3│
│ ┌─────────┐ │ ┌─────────┐ │ ┌─────────┐│
│ │   App   │ │ │   App   │ │ │   App   ││
│ │  +Libs  │ │ │  +Libs  │ │ │  +Libs  ││ ← App + libraries only
│ └─────────┘ │ └─────────┘ │ └─────────┘│
├─────────────┴─────────────┴────────────┤
│      Container Runtime (Docker)        │
├────────────────────────────────────────┤
│         Host OS (Linux)                │ ← Shared OS kernel
├────────────────────────────────────────┤
│         Physical Hardware              │
└────────────────────────────────────────┘
```

**Characteristics:**
- Share OS kernel (10-100 MB per container)
- Boot time: <1 second
- Lighter isolation (same kernel)
- Less overhead

### VMs vs Containers Comparison

| Feature | Virtual Machines | Containers |
|---------|------------------|------------|
| **Size** | 1-10 GB | 10-500 MB |
| **Boot time** | 30-60 seconds | <1 second |
| **Isolation** | Strong (separate kernel) | Lighter (shared kernel) |
| **Overhead** | Higher | Lower |
| **Density** | 10-50 VMs per host | 100-1000 containers per host |
| **OS support** | Any OS | Linux containers need Linux host |
| **Use case** | Full OS needed, strong isolation | Microservices, fast scaling |

### When to use each

**Use Virtual Machines when:**
- Need different OS (Windows + Linux)
- Strong isolation required (multi-tenant)
- Legacy applications
- Full OS features needed

**Use Containers when:**
- Microservices architecture
- Fast scaling needed
- CI/CD pipelines
- Consistent environments (dev = prod)

**AWS services:**
- **EC2** - Virtual Machines
- **ECS/EKS** - Container orchestration (runs on EC2)
- **Fargate** - Serverless containers (no EC2 management)
- **Lambda** - Serverless functions (container-like, even faster)

---

## AWS Virtualization

### Nitro System (Modern AWS)

**What it is:**
- AWS custom hypervisor and hardware
- Offloads virtualization to dedicated hardware
- Introduced 2017, now standard for new instance types

**Architecture:**

```
┌────────────────────────────────────────┐
│  EC2 Instance (Your VM)                │
│  - Full CPU/Memory for your workload   │ ← No hypervisor overhead!
├────────────────────────────────────────┤
│  Nitro Hypervisor (Lightweight KVM)    │ ← Minimal overhead
├────────────────────────────────────────┤
│  Nitro Cards (Dedicated Hardware)      │
│  - Networking                          │
│  - Storage (EBS)                       │ ← Offloaded to hardware
│  - Security                            │
├────────────────────────────────────────┤
│  Physical Server                       │
└────────────────────────────────────────┘
```

**Benefits:**
- **Better performance** - Nearly bare-metal performance
- **More instance sizes** - Can offer smaller/larger instances
- **Enhanced security** - Hardware-level isolation
- **Faster innovation** - Easier to add features

**Instance types using Nitro:**
- All instances with number ≥5: m5, c5, r5, t3, m6g, c6g, etc.
- All Graviton instances (ARM)

### Xen (Legacy AWS)

**What it is:**
- Original AWS hypervisor (2006-2017)
- Open-source hypervisor
- Still used for older instance types

**Instance types using Xen:**
- Older generations: t2, m4, c4, r4, etc.

**AWS recommendation:** Use Nitro-based instances (better performance, newer features)

---

## CPU Features for Virtualization

### Intel VT-x / AMD-V

**What it is:**
- CPU hardware extensions for virtualization
- Allows hypervisor to run VMs efficiently
- Required for HVM (Hardware Virtual Machine)

**Without VT-x/AMD-V:**
- Hypervisor must emulate hardware (slow)
- 10-20x performance penalty

**With VT-x/AMD-V:**
- Hardware-accelerated virtualization
- Near-native performance

**In AWS:** All EC2 instances use hardware virtualization (VT-x/AMD-V)

### Nested Virtualization

**What it is:**
- Running a VM inside a VM
- Example: Run VirtualBox inside EC2 instance

**AWS support:**
- Supported on Nitro-based instances (m5, c5, r5, etc.)
- Useful for testing, development, training

**Use case:**
- Test hypervisor software
- Run Android emulator in cloud
- Development environments

---

## Memory Virtualization

### Memory Overcommitment

**What it is:**
- Allocate more memory to VMs than physically available
- Hypervisor swaps unused memory to disk

**Example:**
- Physical server: 64 GB RAM
- VM1: 32 GB, VM2: 32 GB, VM3: 32 GB = 96 GB allocated
- Works if VMs don't use all memory simultaneously

**AWS:** Does NOT overcommit memory - you get what you pay for

### Memory Ballooning

**What it is:**
- Hypervisor reclaims unused memory from VMs
- VM "balloon driver" gives memory back to hypervisor

**AWS:** Used internally, transparent to users

---

## Network Virtualization

### Virtual Network Interface

**What it is:**
- Virtual network card (NIC) for each VM
- Hypervisor routes traffic between VMs and physical network

**AWS:** Each EC2 instance has ENI (Elastic Network Interface)

### SR-IOV (Single Root I/O Virtualization)

**What it is:**
- Hardware feature that allows VM direct access to physical network card
- Bypasses hypervisor for network traffic

**Benefits:**
- Lower latency
- Higher throughput
- Lower CPU usage

**AWS:** Enhanced Networking uses SR-IOV (available on most modern instances)

---

## Storage Virtualization

### Virtual Disks

**What it is:**
- VM sees virtual disk (e.g., 100 GB)
- Actually a file on host system or network storage

**AWS:**
- **EBS (Elastic Block Store)** - Network-attached virtual disks
- **Instance Store** - Physical disks attached to host server

### Thin Provisioning

**What it is:**
- Allocate 100 GB disk, but only use space as needed
- VM sees 100 GB, but only 10 GB used on host

**Example:**
- Create 100 GB disk
- Copy 10 GB of files
- Host only uses 10 GB physical storage

**AWS EBS:** Uses thin provisioning internally

---

## Summary for AWS

**Key points:**
- AWS uses **Type 1 hypervisors** (Xen for old, Nitro for new instances)
- All modern instances use **HVM** (hardware virtualization)
- **Nitro System** provides near bare-metal performance
- **Containers** (ECS/Fargate) are lighter than VMs but less isolated
- You get **dedicated resources** (no overcommitment)

**Cross-reference:**
- See [EC2 Architecture](../aws_services_kiro/05_amazon_ec2.md) for AWS-specific instance details
- See [CPU Architecture](01_architecture.md) for processor fundamentals
