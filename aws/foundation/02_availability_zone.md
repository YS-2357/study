---
tags:
  - aws
  - infrastructure
created_at: 2026-03-13T00:00:00
updated_at: 2026-04-19T09:11:51
recent_editor: CLAUDE
---

↑ [Overview](./00_foundation_overview.md)

# Availability Zone

## What It Is
An **Availability Zone (AZ)** is one or more physical data centers within a Region. Each AZ has its own power, cooling, and networking, physically separated from other AZs.

## How It Works

Each AZ is a physically separate data center with its own power, cooling, and networking. When you create resources like EC2 instances or subnets, you select an AZ. Deploying across multiple AZs means a failure in one AZ does not affect resources in another.

## Console Access
**No dedicated console page** - AZs are shown within other service consoles.

**Where you see/select AZs:**
- **EC2** - Choose AZ when launching instances
- **VPC/Subnets** - Each subnet must be in one AZ
- **EBS** - Volumes are AZ-specific
- **RDS** - Select AZ for database, Multi-AZ option
- **ELB** - Choose which AZs to enable load balancer in
- **EFS** - Mount targets in each AZ
- **ElastiCache** - Choose AZ for cache nodes
- **Redshift** - Cluster placed in specific AZ

**NOT AZ-related:**
- S3 (Regional service)
- CloudFront, IAM, Route 53 (Global services)

## Console Options

### When Creating Resources
- **Select specific AZ** - Choose which AZ (e.g., us-east-1a, us-east-1b)
- **Let AWS choose** - "No preference" option
- **Multi-AZ options** - Some services offer automatic multi-AZ deployment

### EC2 Console
- Filter instances by AZ
- See which AZ each instance is in
- Select AZ during launch

### VPC Console
- Assign subnet to specific AZ (cannot change later)
- View which AZ each subnet uses

### RDS Console
- Multi-AZ deployment option (automatic failover)
- Choose primary AZ
- AWS selects standby AZ automatically

## Precautions

### MAIN PRECAUTION: Use Multiple AZs for Production
- **Single AZ = single point of failure**
- Always deploy across at least 2 AZs for high availability
- AZ failures are rare but do happen

### 1. AZ Names Are Account-Specific
- us-east-1a in your account ≠ us-east-1a in another account
- AWS randomizes mapping per account
- Use AZ IDs (use1-az1) for cross-account coordination

### 2. Cannot Move Resources Between AZs
- EC2 instances locked to their AZ
- EBS volumes cannot move between AZs
- Must snapshot and recreate in different AZ

### 3. Data Transfer Between AZs Costs Money
- Small charge (~$0.01-0.02 per GB)
- Can add up for high-traffic applications

### 4. EBS Volumes Are AZ-Specific
- Volume must be in same AZ as EC2 instance to attach
- Cannot attach us-east-1a volume to us-east-1b instance

### 5. Subnet-AZ Relationship Is Permanent
- Each subnet exists in exactly one AZ
- Cannot change after creation

### 6. RDS Multi-AZ Costs Double
- Runs standby instance in different AZ
- Roughly doubles instance cost
- Worth it for production databases

### 7. Always Use Tags
- **Tag all resources** with at least a Name tag
- Without tags, hard to identify which AZ resources are in
- Common tags: Name, Environment, Project, Owner

## Example

A web application runs two EC2 instances: one in `ap-northeast-2a` and one in `ap-northeast-2c`.
An ALB distributes traffic across both. If `2a` loses power, the instance in `2c` keeps serving requests
while Auto Scaling replaces the failed one.

## Why It Matters

Single-AZ deployments are a single point of failure.
Spreading resources across at least two AZs is the foundation of high availability on AWS.

## Official Documentation
- [AWS Regions and Availability Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)

---
↑ [Overview](./00_foundation_overview.md)

**Related:** [Region](01_region.md), [Points of Presence (PoP)](03_pop.md)
**Tags:** #aws #infrastructure
