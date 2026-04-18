---
tags:
  - aws
  - computing
  - infrastructure
created_at: 2026-03-16T00:00:00
updated_at: 2026-04-18T18:37:25
recent_editor: CODEX
---

↑ [Overview](./00_compute_overview.md)

# Auto Scaling

## What It Is
Auto Scaling automatically adjusts the number of resources based on demand. When traffic increases, it adds resources. When traffic decreases, it removes them.

**"Auto Scaling" usually means EC2 Auto Scaling Group (ASG)** — but it works with other services too.

### Services That Support Auto Scaling

| Service | What scales | How |
|---|---|---|
| **EC2** (most common) | Number of instances | Auto Scaling Group (ASG) |
| **ECS** | Number of tasks/containers | Service Auto Scaling |
| **DynamoDB** | Read/Write capacity units | Target tracking on RCU/WCU |
| **Aurora** | Number of read replicas (0-15) | Aurora Auto Scaling |
| **Lambda** | Concurrent executions | Automatic (built-in, no config) |
| **ElastiCache** | Number of nodes/shards | ElastiCache Auto Scaling |
| **EMR** | Number of cluster nodes | Managed scaling |

## How It Works

You create an Auto Scaling Group (ASG) by specifying a Launch Template (what to launch), a VPC with subnets across multiple AZs, and minimum/desired/maximum instance counts. Scaling policies define when to add or remove instances based on CloudWatch metrics such as CPU utilization. When a health check fails, the ASG terminates the unhealthy instance and launches a replacement automatically.

## Console Access
- Search "EC2" > Auto Scaling Groups (left sidebar)
- Or search "Auto Scaling" directly


## Create Auto Scaling Group - Console Flow (7 Steps)

> No console screenshots available — based on known ASG console structure. May not match current console exactly.

### Step 1: Choose launch template
- **Auto Scaling group name** — Name for the ASG
- **Launch template** — Select existing or create new
  - Shows: template name, version (Latest/Default/specific)
  - Defines: AMI, instance type, key pair, security group, storage, user data

### Step 2: Choose instance launch options
- **Instance type requirements** — Override launch template instance type
  - Single instance type or mixed (multiple types for cost optimization)
- **Network:**
  - **VPC** — Select VPC
  - **Availability Zones and subnets** — Select 1 or more subnets (use multiple AZs for HA)
  - **Availability Zone distribution** — Select a distribution strategy for how instances are spread across AZs

### Step 3: Configure advanced options
- **Load balancing:**
  - No load balancer
  - Attach to an existing load balancer
  - Attach to a new load balancer
- **VPC Lattice integration** — Optional service-to-service networking
- **Amazon Application Recovery Controller (ARC) zonal shift** — Shift traffic away from an impaired AZ
- **Health checks:**
  - EC2 (default)
  - ELB (recommended when using load balancer)
  - EBS health checks — Monitors and replaces instances with impaired EBS volumes
  - Health check grace period (default 300 seconds)

### Step 4: Configure group size and scaling
- **Group size:**
  - Desired capacity
  - Minimum capacity
  - Maximum capacity
- **Scaling policies:**
  - None
  - Target tracking scaling policy (other types created after ASG creation)
- **Instance maintenance policy** — Controls how instances are replaced during updates
- **Capacity Reservation preference** — Whether to use reserved capacity
- **Instance scale-in protection** — Prevent specific instances from being terminated
- **CloudWatch group metrics collection** — Toggle ASG-level CloudWatch metrics
- **Default instance warmup** — Time before a new instance's metrics count toward scaling decisions

### Step 5: Add notifications (optional)
- SNS (Simple Notification Service) topic for scaling events
- Events: launch, terminate, fail to launch, fail to terminate

### Step 6: Add tags (optional)
- Key-value pairs
- Option to tag instances launched by this ASG

### Step 7: Review
- Review all settings
- **Create Auto Scaling group**


## EC2 Auto Scaling Group (ASG) — Core Concept

### How It Works
You define 3 numbers:
- **Minimum** — Never go below this (e.g., 2)
- **Desired** — How many to run normally (e.g., 2)
- **Maximum** — Never go above this (e.g., 10)

```
e.g. Min: 2, Desired: 2, Max: 10

Normal:    2 instances running (desired)
Traffic ↑: scales to 5, 6, 7... up to 10 (max)
Traffic ↓: scales back down to 2 (min)
```

Auto Scaling + ELB (Elastic Load Balancing) work together:
```
Users → ELB (distributes traffic) → EC2 instances (managed by ASG)
                                     ↑ ASG adds/removes instances based on demand
```

### What You Need to Create an ASG
1. **Launch Template** — Defines what to launch (AMI, instance type, key pair, security group, etc.)
2. **VPC and Subnets** — Where to launch instances (use multiple AZs for high availability)
3. **Scaling policies** — When to scale (see below)
4. **Load Balancer** (optional but recommended) — Distributes traffic across instances

### Scaling Policies (4 types)

| Policy | How it works | Example |
|---|---|---|
| **Target tracking** | Maintain a metric at a target value | "Keep average CPU at 50%" |
| **Step scaling** | Add/remove based on metric thresholds | "If CPU > 70% add 2, if > 90% add 4" |
| **Scheduled** | Scale at specific times | "Scale to 10 every Monday 9AM" |
| **Predictive** | ML-based, predicts traffic patterns | Auto-learns your weekly traffic pattern |

**Most common:** Target tracking (simplest, works well for most cases).

### Health Checks
- ASG monitors instance health
- **EC2 health check** — Is the instance running? (default)
- **ELB health check** — Is the instance responding to requests? (recommended when using ELB)
- Unhealthy instance → ASG terminates it → launches a replacement automatically

### Cooldown Period
- After a scaling action, ASG waits before scaling again
- Default: 300 seconds (5 minutes)
- Prevents rapid scale up/down (thrashing)

### Instance Refresh
- Update all instances in an ASG to a new launch template version
- Rolling update — replaces instances gradually (e.g., 20% at a time)
- No downtime if configured properly


## Load Balancer Types (used with ASG)

ASG is commonly paired with a load balancer to distribute traffic across instances. Quick reference:

| Type | Layer | Use Case with ASG |
|------|-------|-------------------|
| ALB | L7 (HTTP/HTTPS) | Web apps — path/host routing, WAF integration |
| NLB | L4 (TCP/UDP) | High performance, static IPs, non-HTTP protocols |
| GWLB | L3 (GENEVE) | Security appliance inspection before traffic reaches ASG |
| CLB | L4/L7 | **Previous generation** — don't use for new projects |

> For full console flow, screenshots, pricing, and detailed comparison, see [Elastic Load Balancing](../networking/01_elastic_load_balancing.md).


## Key Concepts

### Launch Template vs Launch Configuration
- **Launch Template** (recommended) — Newer, supports versioning, more features
- **Launch Configuration** (legacy) — Older, no versioning, AWS recommends migrating to templates
- Both define: AMI, instance type, key pair, security group, user data
- Launch Template is **EC2/ASG only** — other services have their own equivalents:

| Service | "Template" equivalent | What it defines |
|---------|----------------------|-----------------|
| **EC2 / ASG** | Launch Template | AMI, instance type, SG, key pair, storage, user data |
| **ECS** | Task Definition | Container image, CPU/memory, env vars, IAM role |
| **Lambda** | Function configuration | Runtime, code, memory, timeout |
| **RDS** | Parameter Group + Option Group | DB engine settings |
| **CloudFormation** | CloudFormation Template | Entire infrastructure as code |

### Scaling In vs Scaling Out vs Scaling Up
- **Scale out** (horizontal) = add more instances (traffic increasing). ASG does this automatically. No downtime.
- **Scale in** (horizontal) = remove instances (traffic decreasing). ASG does this automatically.
- **Scale up** (vertical) = make instance bigger (e.g., t3.micro → t3.large). ASG does NOT do this. Requires instance stop → change type → start = downtime.
- ASG decides which instance to terminate when scaling in (default: oldest launch config, then closest to billing hour)

### Applying Launch Template Changes to Existing Instances

Updating the Launch Template only affects **new** instances. Existing running instances keep their old config. To apply changes (e.g., new instance type, new AMI):

**Option 1: Instance Refresh (recommended)**
- ASG built-in feature that automatically replaces existing instances with new ones using the updated Launch Template
- Set "minimum healthy percentage" (e.g., 90%) — ASG terminates old instances in batches and launches new ones
- Rolling update, no full downtime
```
Before: 4x t3.micro (old template)
During: 3x t3.micro + 1x t3.large (rolling)
After:  4x t3.large (new template)
```

**Option 2: Terminate and let ASG replace**
- Update Launch Template version, then terminate instances one by one
- ASG automatically launches replacements using the new template

**Option 3: Blue/Green**
- Create a new ASG with the new Launch Template
- Shift traffic via ELB target group, then delete old ASG

### Multi-AZ for High Availability
- Spread ASG across multiple AZs (Availability Zones)
- If one AZ goes down, instances in other AZs keep running
- ASG automatically rebalances across AZs
- **Tip:** Always use at least 2 AZs for production

### Warm Pool (optional)
- Pre-initialized instances kept in a "stopped" state
- When scaling out, use warm pool instances instead of launching from scratch
- Faster scaling (skip boot time)
- You pay for stopped instances (EBS storage only, no compute)


## Precautions

### MAIN PRECAUTION: Set Maximum Carefully — It's Your Cost Ceiling
- Maximum = the most instances ASG will ever launch
- If set too high, a traffic spike (or attack) could launch many expensive instances
- Always calculate: max instances × instance cost = worst-case monthly bill
- **Tip:** Always discuss max instance count and cost ceiling with the client

### 1. Use Multiple AZs
- Single AZ = single point of failure
- ASG across 2+ AZs = high availability
- If one AZ fails, ASG launches replacements in other AZs

### 2. Use ELB Health Checks, Not Just EC2
- EC2 health check only checks if the instance is running
- ELB health check checks if the app is actually responding
- An instance can be "running" but the app crashed — ELB health check catches this

### 3. Use Launch Templates, Not Launch Configurations
- Launch Configurations are legacy and can't be modified after creation
- Launch Templates support versioning and more features
- AWS recommends migrating to Launch Templates

### 4. Test Your Scaling Policies
- Wrong thresholds = scaling too early or too late
- Too aggressive = unnecessary cost
- Too conservative = poor performance during spikes
- Use predictive scaling or review CloudWatch metrics to tune

### 5. Cooldown Period Matters
- Too short = thrashing (rapid scale up/down)
- Too long = slow response to traffic changes
- Default 300 seconds is fine for most cases

### 6. Always Use Tags
- Tags on ASG propagate to launched instances
- Tag with environment, project, team, client, cost center
- Essential for MSP cost tracking — know which ASG belongs to which client

## Example

An e-commerce site sets up an ASG with min=2, desired=2, max=8 across two AZs.
A target tracking policy keeps average CPU at 50%. During a flash sale, traffic spikes and the ASG scales to 6 instances.
After the sale, it gradually scales back to 2.

## Why It Matters

Auto Scaling matches capacity to demand automatically, preventing both over-provisioning (wasted cost)
and under-provisioning (poor performance or outages during traffic spikes).

## Q&A

### Q: Can Auto Scaling alone prevent all outages?

No. Auto Scaling alone is insufficient. It should be combined with:

- **CloudWatch**: Metric monitoring and scaling trigger conditions
- **ELB**: Traffic distribution + health checks to remove unhealthy instances
- **Multi-AZ deployment**: Survive single-AZ failures
- **Predictive Scaling**: ML-based traffic pattern prediction for proactive scaling

Limitations of Auto Scaling:
- Instance launch takes several minutes — sudden traffic spikes may cause lag
- Application-level failures (DB bottlenecks, code bugs) are not addressed
- Poorly configured scaling policies can cause over- or under-scaling

### Q: Can Launch Templates configure public IP assignment?

Yes. In the Launch Template's network interface settings, use the `AssociatePublicIpAddress` option.

- **Options**: Enable / Disable / Follow subnet setting
- **Security best practice**: Disable public IPs for Auto Scaling instances. Use private subnets with NAT Gateway or access through an ELB instead.

## Official Documentation
- [Amazon EC2 Auto Scaling User Guide](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html)
- [AWS Auto Scaling User Guide](https://docs.aws.amazon.com/autoscaling/plans/userguide/what-is-a-scaling-plan.html)

---
← Previous: [Amazon EC2](01_amazon_ec2.md) | [Overview](./00_compute_overview.md) | Next: [AWS Lambda](03_aws_lambda.md) →
