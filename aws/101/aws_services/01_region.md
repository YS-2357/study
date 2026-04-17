---
tags:
  - aws
  - infrastructure
---
# Region

## What It Is

An AWS Region is a distinct geographic area containing multiple [Availability Zones](02_availability_zone.md). All resources you create exist in a specific Region, and most services are Region-scoped.

## How It Works

When you use the AWS Console, a Region selector in the top-right corner determines which Region's resources are shown and where new resources are created. Global services such as IAM, CloudFront, and Route 53 display "Global" instead of a Region name.

## Console Access
**Location:** Top-right corner of AWS Console (Region selector dropdown)

**Not a dedicated service** - Region is a context selector that affects which resources you see.

## Console Options

### Region Selector Dropdown
- **View all available Regions** - Click dropdown to see full list
- **Switch Regions** - Select any Region to change console context
- **Region codes** - Shows both name and code (e.g., "US East (N. Virginia) us-east-1")
- **Search/Filter** - Type to find specific Regions quickly
- **Recently used** - Shows your most recently accessed Regions at top

### Global vs Regional
- Some services show "Global" instead of Region (IAM, CloudFront, Route 53, WAF)
- Most services are regional and require Region selection

## Precautions

### MAIN PRECAUTION: Always Check Which Region You're In
- **Most common mistake** - Creating resources in the wrong Region
- Check the Region selector (top-right) BEFORE creating anything
- Easy to accidentally be in wrong Region and waste time/money

### 1. Always Verify Current Region
- **Easy to create resources in wrong Region** - Check selector before creating anything
- Resources created in wrong Region = wasted time and potential costs

### 2. Resources Are Region-Isolated
- EC2 instance in us-east-1 won't appear when viewing eu-west-1
- Must switch Regions to see resources in different locations
- No automatic replication between Regions

### 3. Data Transfer Costs
- Moving data between Regions incurs charges
- Can become expensive for large data transfers
- Intra-region transfer is usually free or cheaper

### 4. Service Availability
- Not all services available in all Regions
- New services often launch in limited Regions first
- Check AWS Regional Services list before choosing Region

### 5. Pricing Varies by Region
- Same service costs different amounts in different Regions
- us-east-1 often cheapest, newer Regions may cost more
- Check pricing page for specific Region costs

### 6. Latency Considerations
- Choose Region closest to your users for best performance
- Cross-region latency can be 100ms+ depending on distance
- Test latency before committing to Region

### 7. Compliance and Data Residency
- Some regulations require data stay in specific countries
- GDPR, data sovereignty laws affect Region choice
- Verify compliance requirements before selecting Region

### 8. Resource Migration Difficulty
- Can't easily move some resources between Regions
- May need to recreate resources (EC2, RDS, etc.)
- Plan Region choice carefully from the start

### 9. AMIs and Snapshots Are Regional
- EC2 AMIs must be copied to other Regions manually
- EBS snapshots are Region-specific
- Add time and cost for cross-region copies

### 10. Cleanup Across All Regions
- Deleting resources in one Region doesn't affect others
- Must check all Regions when cleaning up unused resources
- Easy to forget resources in rarely-used Regions (unexpected bills)

### 11. Region Naming Confusion
- Physical location vs code (N. Virginia = us-east-1)
- Multiple Regions in same geographic area (us-east-1, us-east-2)
- Always use Region code in scripts/automation

### 12. Availability Zone Count Varies
- Different Regions have different numbers of AZs
- Affects high availability architecture options
- Check AZ count before designing multi-AZ deployments

## Example

A company based in Tokyo deploys its production app in `ap-northeast-1` for low latency to Japanese users.
Their disaster recovery environment runs in `ap-southeast-1` (Singapore).
Dev/test workloads use `us-east-1` because it has the lowest prices and earliest access to new services.

## Why It Matters

Choosing the right Region affects latency, cost, and compliance.
A wrong Region choice is hard to undo — most resources cannot be moved after creation.

## Official Documentation
- [AWS Regions and Availability Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)

---
← [Overview](00_overview.md) | [Overview](00_overview.md) | Next: [Availability Zone](02_availability_zone.md) →
