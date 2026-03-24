# Interfaces & Endpoints

## What They Are
- **Interface** — how you interact with a system (the method of access)
- **Endpoint** — where you reach a system (the address)

Every time two systems communicate, there's an interface (the "how") and an endpoint (the "where").

---

## Interfaces

An interface is a boundary through which you interact with something. The key idea: you don't need to know how it works internally — you just use the interface.

### Types of Interfaces

| Type | What It Is | Example |
|------|-----------|---------|
| **API** (Application Programming Interface) | A set of rules for programs to talk to each other | REST API, AWS SDK |
| **CLI** (Command Line Interface) | Text-based interaction | `aws s3 ls`, `kubectl get pods` |
| **GUI** (Graphical User Interface) | Visual interaction | AWS Console, web browsers |
| **Network Interface** | A connection point for network communication | ENI (Elastic Network Interface) |

### API — The Most Important Interface

An API defines what operations are available and how to call them. You don't see the internal code — you just call the API.

```
Your App → API call → Service (internal logic hidden)
         ← Response ←
```

**API styles** (see [HTTP](../../networking/networking_kiro/05_http.md) for REST details):

| Style | Protocol | Format | Use Case |
|-------|----------|--------|----------|
| **REST** | HTTP | JSON | Most web APIs |
| **GraphQL** | HTTP | JSON | Frontend flexibility |
| **gRPC** | HTTP/2 | Protocol Buffers | Microservice-to-microservice |
| **SOAP** | HTTP/SMTP | XML | Legacy enterprise systems |

### Network Interface (ENI)

An Elastic Network Interface is a virtual network card in AWS.

What an ENI has:
- Private IP address (required)
- Public IP address (optional)
- MAC address
- One or more security groups
- Source/destination check flag

What uses ENIs:
- EC2 instances (at least one ENI each)
- Lambda functions (when connected to a VPC)
- NAT Gateway
- ELB (load balancer nodes)
- VPC Interface Endpoints

An EC2 instance can have multiple ENIs — useful for:
- Separate management and data traffic
- Multi-homed instances (multiple subnets)
- Network appliances (firewalls)

### Programming Interface

In software, an interface is a contract: "if you implement this interface, you must provide these methods."

```
Interface: Storable
  - save(data)
  - load(id)

Class: S3Storage implements Storable    → must have save() and load()
Class: DiskStorage implements Storable  → must have save() and load()
```

The caller doesn't care which implementation is used — it just calls `save()` and `load()`. This is the same principle as APIs: hide the internals, expose a consistent interface.

---

## Endpoints

An endpoint is a specific address where a service can be reached.

### What Endpoints Look Like

Endpoints don't always look like `*.com` — they can be any addressable format:

| Type | Format | Example |
|------|--------|---------|
| **URL (domain)** | `*.com`, `*.amazonaws.com` | `https://api.example.com/users` |
| **IP address** | `x.x.x.x:port` | `192.168.1.10:3306` (MySQL directly) |
| **IP + path** | `http://x.x.x.x/path` | `http://10.0.1.5:8080/health` |
| **Unix socket** | file path | `/var/run/docker.sock` (Docker API) |
| **localhost** | `localhost:port` | `localhost:3000` (local dev server) |

Most AWS endpoints end in `.amazonaws.com` — that's just AWS's naming convention, not a rule.

### API Endpoints

Each URL in an API is an endpoint:
```
GET  https://api.example.com/users       ← endpoint 1
POST https://api.example.com/users       ← endpoint 2 (same URL, different method)
GET  https://api.example.com/orders/123  ← endpoint 3
```

### AWS Service Endpoints

Every AWS service has a regional endpoint — the URL your SDK/CLI uses to reach that service:
```
EC2:        ec2.us-east-1.amazonaws.com
S3:         s3.us-east-1.amazonaws.com
DynamoDB:   dynamodb.us-east-1.amazonaws.com
Lambda:     lambda.us-east-1.amazonaws.com
```

When you run `aws s3 ls`, the CLI calls `s3.us-east-1.amazonaws.com` behind the scenes.

### Database Endpoints

The DNS address to connect to your database:
```
RDS:    mydb.abc123.us-east-1.rds.amazonaws.com:3306
Aurora: mydb.cluster-abc123.us-east-1.rds.amazonaws.com:3306
        mydb.cluster-ro-abc123.us-east-1.rds.amazonaws.com:3306  (read-only)
```

Aurora has separate writer and reader endpoints — the reader endpoint load-balances across read replicas.

### VPC Endpoints

A private connection from your VPC to an AWS service — traffic stays within the AWS network, never touches the internet.

| Type | How It Works | Supported Services |
|------|-------------|-------------------|
| **Gateway Endpoint** | Route table entry, no ENI | S3, DynamoDB only |
| **Interface Endpoint** | ENI + AWS PrivateLink | Most other AWS services (SQS, SNS, Lambda, etc.) |

```
Without VPC Endpoint:
  EC2 (private subnet) → NAT Gateway → Internet Gateway → S3 (public)

With VPC Gateway Endpoint:
  EC2 (private subnet) → VPC Endpoint → S3 (private, no internet)
```

Why use VPC Endpoints:
- Security — traffic doesn't leave AWS network
- Cost — no NAT Gateway data processing charges
- Compliance — some workloads require no internet exposure

For full VPC Endpoint details, see [Amazon VPC](../../aws101/aws_services_kiro/04_amazon_vpc.md).

---

## How They Connect

```
Interface (how)          Endpoint (where)
─────────────────        ─────────────────
API (REST/GraphQL)  →    API Endpoint (URL)
CLI (aws cli)       →    AWS Service Endpoint (regional URL)
GUI (Console)       →    AWS Console URL
ENI (network card)  →    IP address
VPC Endpoint        →    Private path to AWS service
```

An API is a collection of endpoints that form an interface. The interface defines what you can do, the endpoint defines where to do it.
