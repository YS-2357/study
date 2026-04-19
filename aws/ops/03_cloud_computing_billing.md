---
tags:
  - aws
created_at: 2026-03-31T00:00:00
updated_at: 2026-04-19T09:11:51
recent_editor: CLAUDE
---

↑ [Overview](./00_ops_overview.md)

# Cloud Computing Billing

## What It Is

Cloud computing billing determines how AWS charges for resources. Whether you pay when services are "off" depends on the service type.

## How It Works

Not all AWS services stop billing when you stop using them. The billing model depends on whether the service is instance-based or usage-based.

**Instance-based services (EC2, RDS):**
- [EC2](../compute/01_amazon_ec2.md): Stopping an instance stops compute charges, but attached [EBS](../storage/02_amazon_ebs.md) storage and Elastic IP costs continue.
- [RDS](../database/01_amazon_rds.md): Stopping an instance still incurs storage and snapshot costs. The instance auto-restarts after 7 days.

**Usage-based services (Lambda, S3):**
- [Lambda](../compute/03_aws_lambda.md): No invocations = no charge at all. Billed per request + execution time (GB-seconds).
- [S3](../storage/01_amazon_s3.md): Stored data incurs ongoing storage costs regardless of access.

## Example

A team stops their EC2 dev server over the weekend. Compute charges stop, but they still pay ~$10/month for the 100 GB gp3 EBS volume and $3.65/month for the idle Elastic IP.

## Why It Matters

Understanding what keeps billing even when "off" prevents surprise charges. Serverless services (Lambda) offer true pay-per-use, while instance-based services (EC2/RDS) still incur resource-reservation costs.

## Q&A

### Q: Does AWS handle version upgrades for you?

It depends on the service type under the AWS Shared Responsibility Model:

| Service Type | OS Patches | SW Upgrades | Infrastructure |
|-------------|------------|-------------|----------------|
| EC2 (unmanaged) | Customer | Customer | AWS |
| RDS (managed) | AWS (auto) | Customer triggers major versions | AWS |
| DynamoDB (fully managed) | AWS | AWS | AWS |

- **Managed services (RDS, ElastiCache)**: AWS auto-applies minor patches within a maintenance window you configure. Major version upgrades require customer action.
- **Fully managed services (DynamoDB, Lambda, S3)**: AWS handles all infrastructure and software upgrades.
- **Unmanaged (EC2)**: Customer manages guest OS updates, security patches, and application software.

---
↑ [Overview](./00_ops_overview.md)

**Related:** [AWS SSM Parameter Store](02_aws_ssm_parameter_store.md), [AWS Support Plans](04_aws_support_plans.md), [EC2](../compute/01_amazon_ec2.md), [EBS](../storage/02_amazon_ebs.md), [RDS](../database/01_amazon_rds.md), [Lambda](../compute/03_aws_lambda.md), [S3](../storage/01_amazon_s3.md)
**Tags:** #aws
