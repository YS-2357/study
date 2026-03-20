# Auto Scaling - AWS Console Guide

## Official Documentation
- [Amazon EC2 Auto Scaling User Guide](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html)
- [AWS Auto Scaling User Guide](https://docs.aws.amazon.com/autoscaling/plans/userguide/what-is-a-scaling-plan.html)

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

## Console Access
- Search "EC2" > Auto Scaling Groups (left sidebar)
- Or search "Auto Scaling" directly

---

## Create Auto Scaling Group - Console Flow (7 Steps)

> ⚠️ No console screenshots available — based on known ASG console structure. May not match current console exactly.

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

---

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

---

## Key Concepts

### Launch Template vs Launch Configuration
- **Launch Template** (recommended) — Newer, supports versioning, more features
- **Launch Configuration** (legacy) — Older, no versioning, AWS recommends migrating to templates
- Both define: AMI, instance type, key pair, security group, user data

### Scaling In vs Scaling Out
- **Scale out** = add instances (traffic increasing)
- **Scale in** = remove instances (traffic decreasing)
- ASG decides which instance to terminate when scaling in (default: oldest launch config, then closest to billing hour)

### Multi-AZ for High Availability
- Spread ASG across multiple AZs (Availability Zones)
- If one AZ goes down, instances in other AZs keep running
- ASG automatically rebalances across AZs
- **MSP tip:** Always use at least 2 AZs for production

### Warm Pool (optional)
- Pre-initialized instances kept in a "stopped" state
- When scaling out, use warm pool instances instead of launching from scratch
- Faster scaling (skip boot time)
- You pay for stopped instances (EBS storage only, no compute)

---

## Precautions

### ⚠️ MAIN PRECAUTION: Set Maximum Carefully — It's Your Cost Ceiling
- Maximum = the most instances ASG will ever launch
- If set too high, a traffic spike (or attack) could launch many expensive instances
- Always calculate: max instances × instance cost = worst-case monthly bill
- **MSP tip:** Always discuss max instance count and cost ceiling with the client

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
