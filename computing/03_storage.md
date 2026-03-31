# Storage - Computing Basics

**See [Computing Basics Overview](00_overview.md) for all topics.**

---

## Storage Types

### Block Storage

**What it is:** Raw storage blocks that OS formats with file system

**Characteristics:**
- Low-level access (like physical hard drive)
- OS creates file system (ext4, NTFS, XFS)
- Can be partitioned, formatted
- Direct attached or network attached

**AWS:** EBS (Elastic Block Store), Instance Store

**Use case:** OS drives, databases, applications

### File Storage

**What it is:** Network file system with directory structure

**Characteristics:**
- Already has file system
- Multiple servers can access simultaneously
- Hierarchical (folders/files)
- Network protocols (NFS, SMB/CIFS)

**AWS:** EFS (Elastic File System), FSx

**Use case:** Shared files, home directories, content management

### Object Storage

**What it is:** Store files as objects with metadata

**Characteristics:**
- Flat structure (no folders, just buckets)
- Access via HTTP/API
- Highly scalable
- Metadata rich

**AWS:** S3 (Simple Storage Service)

**Use case:** Backups, media files, data lakes, static websites

---

## Storage Performance Metrics

### IOPS (Input/Output Operations Per Second)

**What it is:** Number of read/write operations per second

**Example:**
- 3000 IOPS = 3000 read or write operations per second
- Like "how many times can you open/close files per second"

**Factors affecting IOPS:**
- **Block size:** Smaller blocks = more IOPS possible
- **Storage type:** SSD > HDD
- **Workload:** Random vs sequential

**AWS EBS types:**
- gp3: 3,000-16,000 IOPS
- io2: Up to 64,000 IOPS (high performance)

**When IOPS matters:**
- Databases (many small reads/writes)
- Transactional workloads
- Random access patterns

### Throughput (MB/s)

**What it is:** Amount of data transferred per second

**Example:**
- 125 MB/s = Can transfer 125 megabytes per second
- Like "how fast can you copy a large file"

**AWS EBS types:**
- gp3: 125-1,000 MB/s
- st1: Up to 500 MB/s (throughput optimized)

**When throughput matters:**
- Large file transfers
- Video streaming
- Big data processing
- Sequential access patterns

### Latency

**What it is:** Time delay for single operation

**Example:**
- 1 ms latency = 1 millisecond to complete one read/write
- Lower is better

**Typical latencies:**
- Local SSD: <1 ms
- EBS SSD: 1-3 ms
- EBS HDD: 10-20 ms
- S3: 100-200 ms

**When latency matters:**
- Real-time applications
- Databases
- Interactive workloads

---

## HDD vs SSD

### HDD (Hard Disk Drive)

**How it works:** Spinning magnetic platters with read/write head

**Characteristics:**
- **Mechanical** - Moving parts
- **Slower** - 100-200 IOPS
- **Cheaper** - $0.045/GB/month (AWS st1)
- **Higher capacity** - Up to 16 TB per disk
- **Sequential good, random bad**

**Use case:** Backups, archives, big data (sequential access)

### SSD (Solid State Drive)

**How it works:** Flash memory chips (no moving parts)

**Characteristics:**
- **Electronic** - No moving parts
- **Faster** - 3,000-64,000 IOPS
- **More expensive** - $0.08-0.125/GB/month (AWS gp3/io2)
- **Lower capacity** - Up to 16 TB per disk
- **Good for random access**

**Use case:** OS drives, databases, applications

---

## AWS EBS Volume Types

### General Purpose SSD (gp3, gp2)

**gp3 (Current generation):**
- 3,000 IOPS baseline (can provision up to 16,000)
- 125 MB/s baseline (can provision up to 1,000 MB/s)
- $0.08/GB/month
- **Most common choice**

**gp2 (Previous generation):**
- IOPS scales with size (3 IOPS per GB)
- Burstable performance
- $0.10/GB/month

**Use case:** Boot volumes, dev/test, general workloads

### Provisioned IOPS SSD (io2, io1)

**io2 Block Express:**
- Up to 64,000 IOPS
- Up to 1,000 MB/s
- $0.125/GB/month + $0.065 per provisioned IOPS
- 99.999% durability

**Use case:** Mission-critical databases, high-performance workloads

### Throughput Optimized HDD (st1)

- Up to 500 MB/s
- Up to 500 IOPS
- $0.045/GB/month
- **Cannot be boot volume**

**Use case:** Big data, data warehouses, log processing

### Cold HDD (sc1)

- Up to 250 MB/s
- Up to 250 IOPS
- $0.015/GB/month (cheapest)
- **Cannot be boot volume**

**Use case:** Infrequent access, archives

---

## File Systems

### ext4 (Linux)

- Default Linux file system
- Journaling (crash recovery)
- Max file size: 16 TB
- Max volume size: 1 EB

### XFS (Linux)

- High-performance file system
- Better for large files
- Used by AWS for EBS
- Max file size: 8 EB

### NTFS (Windows)

- Windows file system
- Journaling, encryption, compression
- Max file size: 16 TB

### Choosing file system in AWS

- **Linux:** ext4 or XFS (XFS for large files/databases)
- **Windows:** NTFS (only option)

---

## Summary for AWS

**Storage types:**
- **EBS** - Block storage (like hard drive)
- **EFS** - File storage (shared network drive)
- **S3** - Object storage (files via API)

**EBS volume types:**
- **gp3** - General purpose (most common)
- **io2** - High performance databases
- **st1** - Big data (HDD, throughput)
- **sc1** - Archives (HDD, cheap)

**Performance:**
- **IOPS** - Operations per second (databases)
- **Throughput** - MB/s (large files)
- **Latency** - Response time (real-time apps)

**Cross-reference:**
- See [EC2 Storage](../aws/101/aws_services/05_amazon_ec2.md#configure-storage) for AWS-specific storage configuration
- See [EBS](../aws/101/aws_services/20_amazon_ebs.md) for detailed EBS documentation (when created)
