---
tags:
  - aws
---
# Cloud Computing Billing

## What It Is

Cloud computing billing determines how AWS charges for resources. Whether you pay when services are "off" depends on the service type.

## How It Works

Not all AWS services stop billing when you stop using them. The billing model depends on whether the service is instance-based or usage-based.

**Instance-based services (EC2, RDS):**
- [EC2](05_amazon_ec2.md): Stopping an instance stops compute charges, but attached [EBS](20_amazon_ebs.md) storage and Elastic IP costs continue.
- [RDS](10_amazon_rds.md): Stopping an instance still incurs storage and snapshot costs. The instance auto-restarts after 7 days.

**Usage-based services (Lambda, S3):**
- [Lambda](07_aws_lambda.md): No invocations = no charge at all. Billed per request + execution time (GB-seconds).
- [S3](19_amazon_s3.md): Stored data incurs ongoing storage costs regardless of access.

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
← Previous: [AWS WAF](18_aws_waf.md) | [Overview](00_overview.md) | Next: [AWS Marketplace](29_aws_marketplace.md) →
