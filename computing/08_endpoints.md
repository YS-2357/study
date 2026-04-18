---
tags:
  - computing
  - networking
created_at: 2026-03-31T00:00:00
updated_at: 2026-04-18T13:00:00
recent_editor: CLAUDE
---

↑ [Overview](./00_overview.md)

# Endpoints

## What It Is

An endpoint is where a service can be reached. If an [interface](07_interfaces.md) defines the method of access, an endpoint defines the actual address.

## How It Works

### Endpoint Formats

| Type | Format | Example |
|------|--------|---------|
| URL | `*.amazonaws.com` | `https://s3.us-east-1.amazonaws.com` |
| IP:port | `x.x.x.x:port` | `192.168.1.10:3306` |
| localhost | `localhost:port` | `localhost:3000` |

### AWS Service Endpoints

Every AWS service has a regional endpoint:
```
EC2:      ec2.us-east-1.amazonaws.com
S3:       s3.us-east-1.amazonaws.com
DynamoDB: dynamodb.us-east-1.amazonaws.com
```

When you run `aws s3 ls`, the CLI calls the S3 endpoint behind the scenes.

### Database Endpoints

```
RDS:    mydb.abc123.us-east-1.rds.amazonaws.com:3306
Aurora: mydb.cluster-abc123.us-east-1.rds.amazonaws.com:3306      (writer)
        mydb.cluster-ro-abc123.us-east-1.rds.amazonaws.com:3306   (reader)
```

[Aurora](../aws/11_amazon_aurora.md) separates writer and reader endpoints. The reader endpoint load-balances across replicas.

### VPC Endpoints

A VPC endpoint gives your [VPC](../aws/04_amazon_vpc.md) a private path to an AWS service — traffic stays within the AWS network.

| Type | How it works | Services |
|------|-------------|----------|
| **Gateway** | Route table entry | S3, DynamoDB only |
| **Interface** | ENI + PrivateLink | Most other services |

```
Without:  EC2 (private) → NAT Gateway → Internet → S3
With:     EC2 (private) → VPC Endpoint → S3 (no internet)
```

Benefits: security (no internet exposure), cost (no NAT data charges), compliance.

## Example

An API has multiple endpoints: `GET /users` (list), `POST /users` (create), `GET /users/1` (read). Each URL is an endpoint. Together they form the API [interface](07_interfaces.md).

## Why It Matters

Understanding endpoints clarifies how AWS services connect: the CLI and SDK call service endpoints, databases expose connection endpoints, and VPC endpoints keep traffic private. Misconfigured endpoints cause connectivity failures.

---
← Previous: [Interfaces](07_interfaces.md) | [Overview](./00_overview.md) | Next: [Decomposition](09_decomposition.md) →
