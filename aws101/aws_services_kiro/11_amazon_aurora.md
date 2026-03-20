# Amazon Aurora - AWS Console Guide

## Official Documentation
- [Amazon Aurora User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)
- [Amazon Aurora FAQs](https://aws.amazon.com/rds/aurora/faqs/)

## What It Is
Amazon Aurora is AWS's cloud-native relational database engine, compatible with MySQL and PostgreSQL. It runs on the same RDS platform but uses a completely different storage architecture — shared cluster storage that auto-replicates across 3 AZs (Availability Zones).

Aurora is NOT standard MySQL/PostgreSQL — it's AWS's re-engineered version. Same SQL compatibility, different engine underneath.

**"Fully managed" — what AWS means:**
- AWS official docs call Aurora "a fully managed relational database engine" ([source](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html))
- Standard RDS is called just "managed" — not "fully managed" ([source](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html))
- Aurora is more managed than standard RDS because storage is fully abstracted (auto-grows, auto-replicates 6 copies across 3 AZs)
- But you still choose instance classes and engine versions — so it's not as hands-off as DynamoDB (where you don't think about instances at all)
- In practice, Aurora sits between standard RDS and DynamoDB on the management spectrum:
  - **Standard RDS** — managed (you pick instance, storage type, storage size)
  - **Aurora** — fully managed per AWS docs (storage abstracted, but you still pick compute)
  - **DynamoDB** — fully managed, serverless-first (no instance or storage decisions at all)

## Aurora vs Standard RDS — Pros and Cons

### Pros of Aurora (over standard RDS)
- **Shared cluster storage** — auto-replicates 6 copies across 3 AZs, always
- **Auto-growing storage** — up to 128 TiB, no need to pre-provision or manage
- **Up to 15 read replicas** (vs 5 for standard RDS), near-zero replication lag
- **Faster failover** — ~30 sec (vs ~60-120 sec for standard RDS)
- **Serverless v2** — auto-scales compute, pay only for what you use
- **Aurora-only features** — Babelfish, Limitless Database, Data API, write forwarding
- **Higher durability** — survives loss of up to 2 copies without affecting writes

### Cons of Aurora (over standard RDS)
- **~20% more expensive** than standard RDS baseline
- **MySQL and PostgreSQL only** — no Oracle, SQL Server, MariaDB, Db2
- **AWS-only** — can't run Aurora outside AWS, harder to migrate away
- **More complex** — cluster concept (writer + readers) vs single instance
- **I/O costs can surprise you** — Aurora Standard charges per I/O request (use I/O-Optimized if I/O heavy)

### When to Pick Aurora
- Production workloads needing high availability
- Read-heavy applications (15 replicas, shared storage)
- Don't want to manage storage sizing
- Need fast failover
- Budget allows the premium

### When to Stick with Standard RDS
- Need Oracle, SQL Server, MariaDB, or Db2
- Want portability (easier to migrate off AWS later)
- Simple workload, budget-sensitive
- Dev/test environments (standard RDS with t classes is cheaper)

### Comparison Table

| | Standard RDS | Aurora |
|---|---|---|
| Storage | EBS per instance | Shared cluster storage |
| Auto-grows | You set size (with auto-scaling option) | Automatic (up to 128 TiB) |
| Data copies | 2 (Multi-AZ) | 6 (across 3 AZs, always) |
| Read replicas | Up to 5 | Up to 15 |
| Replica lag | Asynchronous (has lag) | Near-zero (shared storage) |
| Failover time | ~60-120 sec | ~30 sec |
| Serverless option | No | Yes (Serverless v2) |
| Compatible with | MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, Db2 | MySQL, PostgreSQL only |
| Cost | Lower baseline | ~20% more |
| Portability | Standard engines, easy to migrate | AWS-only |

> For standard RDS details, see [19_amazon_rds.md](./19_amazon_rds.md)

## What to Remember (Console Create Summary)

Same console as RDS, same core decisions apply. Plus Aurora-specific ones:

**5 decisions you must get right (same as RDS — hard/impossible to change later):**
1. **Engine** — Aurora MySQL or Aurora PostgreSQL? (can't change after creation)
2. **VPC** — Which network? (⚠️ can't change after creation)
3. **KMS key** — Which encryption key? (⚠️ can't change after creation)
4. **Public access** — Yes/No? (default No is almost always correct)
5. **Multi-AZ** — Create a replica or not? (Aurora replicas = read scaling + failover)

**3 Aurora-specific decisions:**
1. **Storage config** — I/O-Optimized vs Standard? (switchable, but affects billing model)
2. **Instance class** — Serverless v2 vs provisioned? (Serverless = auto-scale, provisioned = fixed)
3. **Babelfish** — Migrating from SQL Server? (Aurora PostgreSQL only)

**Everything else** has safe defaults or is changeable after creation.

**TL;DR:** Engine, VPC, instance class (Serverless v2 or provisioned size). Get those 3 right.

## Console Access
- Search "RDS" in AWS Console
- Breadcrumb: Aurora and RDS > Databases > Create database
- Same console as RDS — selecting Aurora (MySQL Compatible) or Aurora (PostgreSQL Compatible) as engine creates an Aurora cluster

---

## Create Database - Console Flow (Aurora-specific options)

> Aurora shares the same "Create database" console as RDS. Below covers only Aurora-specific options. For the full console flow, see [19_amazon_rds.md](./19_amazon_rds.md).

![Create Database - Engine Options](../images/aws_console/rds01.png)

### Engine options
- **Aurora (MySQL Compatible)** — Compatible with MySQL
- **Aurora (PostgreSQL Compatible)** — Compatible with PostgreSQL

![Engine Version and Templates](../images/aws_console/rds02.png)

### Engine version (Aurora-specific filters)
- **Show only versions that support the Babelfish for PostgreSQL feature** — For SQL Server migration
- **Show only versions that support Aurora Limitless Database** — For automatic horizontal scaling (sharding)
- **Enable RDS Extended Support** — Paid offering for running past end-of-standard-support date

### Templates
- **Production** — High availability defaults (Multi-AZ, larger instance)
- **Dev/Test** — Development use, lower defaults

![Settings and Credentials](../images/aws_console/rds03.png)

### Settings
- **DB cluster identifier** — Name for the Aurora cluster (not just one instance)
  - Unique across all DB clusters in the current Region

### Credentials
- Same as RDS: Secrets Manager (default, recommended) or Self managed

![Storage Configuration](../images/aws_console/rds04.png)

### Cluster storage configuration (Aurora-specific)
**Configuration options (2 choices):**

1. **Aurora I/O-Optimized**
   - Predictable pricing, no additional I/O charges
   - Good when I/O costs >25% of total database costs
   - DB instance and storage prices include I/O usage

2. **Aurora Standard**
   - Pay-per-request I/O charges apply
   - Good when I/O costs <25% of total database costs
   - Cheaper baseline, but I/O costs can add up

> **MSP tip:** If unsure, start with Aurora Standard and monitor I/O costs. Switch to I/O-Optimized if I/O exceeds 25% of your bill.

### Additional credentials settings
- **IAM database authentication** — Authenticate using IAM instead of password
- **Kerberos authentication** — Authenticate through AWS Directory Service

![Instance Configuration and Availability](../images/aws_console/rds05.png)

### Instance configuration (Aurora-specific)
**DB instance class (4 categories):**
- **Serverless v2** — Auto-scales compute based on demand (Aurora-only feature)
  - Set min/max ACU (Aurora Capacity Units)
  - Pay only for capacity used
  - Good for unpredictable or variable workloads
- **Memory optimized classes** (r classes) — Production workloads
- **Burstable classes** (t classes) — Dev/test
- **Optimized Reads classes** — Read-heavy workloads

### Availability & durability
**Multi-AZ deployment:**
- **Create an Aurora Replica or Reader node in a different AZ** (recommended) — Fast failover and read scaling
- **Don't create an Aurora Replica** — Single instance, no automatic failover

> Unlike RDS Multi-AZ standby (which is NOT readable), Aurora replicas ARE readable and serve as failover targets.

![Connectivity](../images/aws_console/rds06.png)

### Connectivity
- Same as RDS: VPC, subnet group, public access, security group
- ⚠️ **"After a database is created, you can't change its VPC"**

![Public Access, Security Group, RDS Proxy](../images/aws_console/rds07.png)

### RDS Proxy
- Works with Aurora — improves connection pooling for serverless or Lambda workloads
- ⚠️ Additional costs

![Certificate Authority, Data API, Write Forwarding](../images/aws_console/rds08.png)

### RDS Data API (Aurora-specific)
- **Enable the RDS Data API** — Run SQL queries over HTTP (via CLI, AWS SDK, or RDS query editor)
- No persistent database connection needed
- Good for serverless architectures (Lambda → Data API → Aurora)

### Read replica write forwarding (Aurora-specific)
- **Turn on local write forwarding** — Reader instances can forward write operations to the writer
- Simplifies application logic (read from any endpoint, writes get forwarded)

![Tags, Babelfish, Monitoring](../images/aws_console/rds09.png)

### Babelfish settings (Aurora PostgreSQL only)
- **Turn on Babelfish** — Enables Aurora PostgreSQL to understand T-SQL (SQL Server's language)
- Makes migration from Microsoft SQL Server faster, cheaper, and lower-risk
- Applications can connect using SQL Server drivers without code changes

### Monitoring
- Same as RDS: Database Insights Advanced (15 months) vs Standard (7 days)

![Encryption and Enhanced Monitoring](../images/aws_console/rds10.png)

### Encryption
- ⚠️ **"You can't change the KMS key after you create your database"**

![Log Exports, DevOps Guru](../images/aws_console/rds11.png)

![Estimated Costs and Create](../images/aws_console/rds12.png)

### Estimated monthly costs
- Shows on-demand pricing estimate
- Does NOT include reserved instance benefits, storage IOs, or data transfer

---

## Key Concepts

### Aurora Cluster Architecture
- **Cluster** = a group of instances working together as one system
  - 1 writer instance + 0-15 reader instances + shared cluster storage
- **Writer instance** — Handles all write operations
- **Reader instances** — Handle read operations, also serve as failover targets
- **Cluster storage** — Shared across all instances, auto-replicates 6 copies across 3 AZs

### Shared Cluster Storage (Aurora's Core Innovation)

Aurora's storage is NOT EBS. It's a **custom distributed storage system built by AWS** — completely separate from EBS.

**Standard RDS (EBS, not shared):**
```
Writer instance → [its own EBS disk]
Read replica 1  → [its own EBS disk]  ← data copied from writer (lag)
Read replica 2  → [its own EBS disk]  ← data copied from writer (lag)
```
Each instance has a separate EBS volume. Writer copies data to each replica.

**Aurora (shared storage layer):**
```
Writer instance  ─┐
Reader instance 1 ─┼──→ [ONE shared storage layer]
Reader instance 2 ─┘     (6 copies across 3 AZs, managed by AWS)
```
All instances point to the same storage. Writer writes once, readers see it immediately.

**EBS vs Aurora storage:**

| | EBS (standard RDS) | Aurora storage layer |
|---|---|---|
| What is it | Disk attached to one instance | Custom distributed storage by AWS |
| Visible in console? | Yes (EC2 > EBS volumes) | ❌ No — invisible, internal infrastructure |
| Size | You choose (100GB, 500GB, etc.) | Auto-grows (up to 128 TiB) |
| Lives in | One AZ | Spread across 3 AZs |
| Managed by | You configure, AWS maintains | AWS entirely |

**You won't find Aurora storage anywhere in the console** — no service page, no EBS volume, no configuration screen. The only things you see are:
- Storage used (e.g., "45 GiB") in cluster monitoring
- Storage config choice (I/O-Optimized vs Standard)

That's why there's no "storage size" field when creating Aurora — unlike standard RDS where you pick "100 GiB gp3". Aurora just grows.

This is also why Aurora is AWS-only — this storage system is proprietary AWS infrastructure that doesn't exist anywhere else.

### Cluster Endpoints
- **Cluster endpoint (writer)** — Always points to the current writer instance
- **Reader endpoint** — Load-balances across all reader instances
- **Instance endpoints** — Direct connection to a specific instance
- Your application connects to endpoints, not instances — Aurora handles routing

### Serverless v2
- Auto-scales compute (vCPUs, RAM) based on demand
- Set minimum and maximum ACU (Aurora Capacity Units)
  - 1 ACU ≈ 2 GiB RAM
  - Range: 0.5 to 256 ACU
- Scales in seconds, no downtime
- Good for: variable workloads, dev/test, new applications with unknown traffic

### Aurora Limitless Database
- Automatic horizontal scaling (sharding) across multiple DB instances
- Handles millions of write transactions per second
- Aurora manages shard placement and routing
- Advanced feature for very large-scale workloads

### Babelfish for PostgreSQL
- Aurora PostgreSQL feature that understands T-SQL (SQL Server's language)
- Applications can connect using SQL Server drivers (TDS protocol)
- Reduces migration effort from SQL Server to Aurora PostgreSQL
- Not 100% compatible — test your application first

### Storage: I/O-Optimized vs Standard
| | Aurora I/O-Optimized | Aurora Standard |
|---|---|---|
| I/O charges | Included in price | Pay per request |
| Baseline cost | Higher | Lower |
| Best when | I/O >25% of total cost | I/O <25% of total cost |
| Switchable? | Yes, after creation | Yes, after creation |

---

## Precautions

### ⚠️ MAIN PRECAUTION: VPC and KMS Key Cannot Be Changed After Creation
- Same as RDS — choose carefully before creating
- Plan your network and encryption strategy first

### 1. I/O Costs Can Surprise You (Aurora Standard)
- Aurora Standard charges per I/O request — can add up fast with heavy workloads
- Monitor I/O costs in your bill
- Switch to I/O-Optimized if I/O exceeds 25% of total database cost

### 2. Aurora Is More Expensive Than Standard RDS
- ~20% more than equivalent standard RDS
- Factor in: instance cost + storage + I/O (if Standard) + backups + data transfer
- Use Serverless v2 for variable workloads to avoid paying for idle capacity

### 3. Aurora Is AWS-Only
- Can't run Aurora outside AWS
- If portability matters (multi-cloud, exit strategy), consider standard RDS with MySQL/PostgreSQL
- Migration away from Aurora requires exporting data to standard MySQL/PostgreSQL

### 4. Serverless v2 — Set Max ACU Carefully
- No max ACU limit means auto-scaling could spike your bill
- Always set a reasonable maximum ACU based on budget
- Monitor scaling behavior in CloudWatch

### 5. Babelfish Is Not 100% Compatible
- Test your SQL Server application thoroughly before migrating
- Some T-SQL features may not be supported
- Check AWS compatibility documentation first

### 6. Don't Skip Multi-AZ for Production
- Aurora replicas serve as both read scaling AND failover targets
- Without a replica, failover creates a new instance (slower recovery)
- At least 1 replica in a different AZ for production

### 7. Always Use Tags
- Tag with environment, project, team, client, cost center
- Up to 50 tags per cluster
- Essential for MSP cost tracking across multiple clients
