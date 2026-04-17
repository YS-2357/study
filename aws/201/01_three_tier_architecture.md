---
tags:
  - aws
  - networking
  - infrastructure
  - security
  - database
---

# Three-Tier Architecture

## What It Is

A three-tier architecture separates a web application into a **presentation tier**, an **application tier**, and a **data tier**. In AWS, those tiers are usually separated with an Amazon Virtual Private Cloud ([Amazon VPC](../101/aws_services/04_amazon_vpc.md)), [subnets](../101/aws_services/03_subnet.md), route tables, load balancers, security groups, and private database networking, using the same public/private subnet model described in the [Amazon VPC documentation](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html).

## Analogy

Think of a restaurant: the dining room is public, the kitchen is private, and the storage room is even more restricted. Customers can enter the dining room, staff can move between the dining room and kitchen, and only the kitchen should access the storage room.

## How It Works

The common mental model is:

```text
Internet
  -> public presentation entry point
  -> private application backend
  -> private database
```

That often maps to AWS like this:

| Tier | Network placement | AWS examples | Purpose |
|---|---|---|---|
| Presentation | Public entry point | Amazon Route 53, AWS WAF, Amazon CloudFront, internet-facing Application Load Balancer (ALB) | Accept user traffic |
| Application | Private subnets | Amazon Elastic Compute Cloud (EC2), Amazon Elastic Container Service (ECS), Amazon Elastic Kubernetes Service (EKS), AWS Lambda-connected services, internal APIs | Run business logic |
| Data | Private database subnets | Amazon Relational Database Service (Amazon RDS), Amazon Aurora, Amazon ElastiCache, private data stores | Store state and serve only trusted backend callers |

A public subnet has a route to an internet gateway, while a private subnet does not have that direct internet route ([Amazon VPC User Guide](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html)). Private application subnets can still make outbound calls through a network address translation (NAT) gateway, which lets instances initiate outbound connections while blocking unsolicited inbound internet connections ([Amazon VPC User Guide](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-nat-gateway.html)).

For web applications, the public-facing tier is often an internet-facing ALB in public subnets. AWS Prescriptive Guidance describes the pattern where internet traffic reaches an ALB associated with public subnets, and the ALB routes requests to EC2 instances in private subnets ([AWS Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/load-balancer-stickiness/subnets-routing.html)).

For databases, the data tier usually uses private subnets. Amazon RDS documents the common pattern of public-facing web servers with a database that is not publicly accessible; only the web or application servers can access the DB instance ([Amazon RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)).

### Security Group Flow

Use security groups to express tier-to-tier trust:

| Security group | Inbound rule | Reason |
|---|---|---|
| ALB security group | HTTPS `443` from the internet | Users reach only the public entry point |
| Backend security group | App port only from the ALB security group | Backend is not directly public |
| Database security group | Database port only from the backend security group | Database accepts traffic only from the app tier |

### Frontend Nuance

`public frontend` does not always mean frontend servers sit in a public subnet. A static frontend can live in private Amazon Simple Storage Service ([Amazon S3](../101/aws_services/19_amazon_s3.md)) and be served through CloudFront using origin access control (OAC), which lets CloudFront send authenticated requests to an S3 origin ([Amazon CloudFront Developer Guide](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)). In that version, CloudFront is the public presentation entry point, while the S3 bucket can stay private.

## Example

A production web app can use this layout:

```text
VPC
  Public subnets in two Availability Zones
    - Internet-facing ALB
    - NAT gateways

  Private app subnets in two Availability Zones
    - ECS service, EC2 Auto Scaling group, or application servers

  Private database subnets in two Availability Zones
    - Amazon RDS or Aurora subnet group
```

Traffic flow:

1. A user visits `https://app.example.com`.
2. Route 53 resolves the name to CloudFront or an internet-facing ALB.
3. The public entry point forwards the request to backend targets in private app subnets.
4. The backend reads or writes data through the database security group.
5. The database never accepts inbound traffic from the internet.

## Why It Matters

Three-tier architecture makes the blast radius smaller: public traffic reaches only the public entry point, backend compute can stay private, and the database can accept traffic only from the backend tier. It also makes scaling clearer because each tier can scale independently: add more ALB targets for backend load, tune database capacity for data load, and use CloudFront for global presentation caching.

| Perspective | Detail |
|---|---|
| Feasibility | Works for EC2, ECS, EKS, Lambda-backed APIs, ALB, CloudFront, RDS, Aurora, and similar AWS services |
| Disruption | Usually requires subnet, routing, and security group planning before deployment; moving an existing public database into private subnets can require connection-string, routing, and maintenance-window planning |
| Pros & Cons | Strong isolation and clear scaling boundaries, but more networking pieces to operate |
| Differences | Unlike a single-server design, each tier has a separate network boundary and trust rule |

---
← Previous: [AWS 201 Overview](00_overview.md) | [Overview](00_overview.md) | Next: [AWS Services Overview](aws_services/00_overview.md) →
