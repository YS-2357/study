# Endpoints

## What It Is
An endpoint is where a service can be reached.

If an interface defines the method of access, an endpoint defines the actual address or target used for that access.

---

## What Endpoints Look Like

Endpoints do not always look like `*.com`. They can be any addressable format:

| Type | Format | Example |
|------|--------|---------|
| **URL (domain)** | `*.com`, `*.amazonaws.com` | `https://api.example.com/users` |
| **IP address** | `x.x.x.x:port` | `192.168.1.10:3306` |
| **IP + path** | `http://x.x.x.x/path` | `http://10.0.1.5:8080/health` |
| **Unix socket** | file path | `/var/run/docker.sock` |
| **localhost** | `localhost:port` | `localhost:3000` |

Most AWS endpoints end in `.amazonaws.com`, but that is AWS naming convention, not a general rule.

---

## API Endpoints

Each URL in an API is an endpoint:

```text
GET  https://api.example.com/users       <- endpoint 1
POST https://api.example.com/users       <- endpoint 2 (same URL, different method)
GET  https://api.example.com/orders/123  <- endpoint 3
```

An API usually contains multiple endpoints that together form one interface.

---

## AWS Service Endpoints

Every AWS service has a regional endpoint that the SDK or CLI calls:

```text
EC2:        ec2.us-east-1.amazonaws.com
S3:         s3.us-east-1.amazonaws.com
DynamoDB:   dynamodb.us-east-1.amazonaws.com
Lambda:     lambda.us-east-1.amazonaws.com
```

When you run `aws s3 ls`, the CLI calls the S3 endpoint behind the scenes.

---

## Database Endpoints

A database endpoint is the DNS address used by clients to connect:

```text
RDS:    mydb.abc123.us-east-1.rds.amazonaws.com:3306
Aurora: mydb.cluster-abc123.us-east-1.rds.amazonaws.com:3306
        mydb.cluster-ro-abc123.us-east-1.rds.amazonaws.com:3306
```

Aurora separates writer and reader endpoints, and the reader endpoint load-balances across replicas.

---

## VPC Endpoints

A VPC endpoint gives your VPC a private path to an AWS service so traffic stays within the AWS network.

| Type | How It Works | Supported Services |
|------|-------------|-------------------|
| **Gateway Endpoint** | Route table entry, no ENI | S3, DynamoDB only |
| **Interface Endpoint** | ENI + AWS PrivateLink | Most other AWS services |

```text
Without VPC Endpoint:
  EC2 (private subnet) -> NAT Gateway -> Internet Gateway -> S3 (public)

With VPC Gateway Endpoint:
  EC2 (private subnet) -> VPC Endpoint -> S3 (private, no internet)
```

Why use VPC endpoints:
- Security - traffic does not leave the AWS network
- Cost - no NAT Gateway data processing charges
- Compliance - some workloads require no internet exposure

For full VPC endpoint details, see [Amazon VPC](../aws/101/aws_services/04_amazon_vpc.md).

---

## How They Connect

```text
Interface (how)          Endpoint (where)
-----------------        -----------------
API (REST/GraphQL)  ->   API Endpoint (URL)
CLI (aws cli)       ->   AWS Service Endpoint (regional URL)
GUI (Console)       ->   AWS Console URL
ENI (network card)  ->   IP address
VPC Endpoint        ->   Private path to AWS service
```

An API is a collection of endpoints that form an interface. The interface defines what you can do, and the endpoint defines where to do it.

See [Interfaces](07_interfaces.md) for the access-method side of the same concept.
