# Interfaces

## What It Is
An interface is how you interact with a system.

The key idea is that an interface defines the method of access without requiring you to know the internal implementation.

---

## Types of Interfaces

| Type | What It Is | Example |
|------|-----------|---------|
| **API** (Application Programming Interface) | A set of rules for programs to talk to each other | REST API, AWS SDK |
| **CLI** (Command Line Interface) | Text-based interaction | `aws s3 ls`, `kubectl get pods` |
| **GUI** (Graphical User Interface) | Visual interaction | AWS Console, web browsers |
| **Network Interface** | A connection point for network communication | ENI (Elastic Network Interface) |

---

## API - The Most Important Interface

An API defines what operations are available and how to call them. You do not see the internal code. You just call the API and handle the response.

```text
Your App -> API call -> Service (internal logic hidden)
         <- Response <-
```

**API styles** (see [HTTP](../networking/05_http.md) for REST details):

| Style | Protocol | Format | Use Case |
|-------|----------|--------|----------|
| **REST** | HTTP | JSON | Most web APIs |
| **GraphQL** | HTTP | JSON | Frontend flexibility |
| **gRPC** | HTTP/2 | Protocol Buffers | Microservice-to-microservice |
| **SOAP** | HTTP/SMTP | XML | Legacy enterprise systems |

---

## Network Interface (ENI)

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

An EC2 instance can have multiple ENIs. Common reasons:
- Separate management and data traffic
- Multi-homed instances in multiple subnets
- Network appliances such as firewalls

---

## Programming Interface

In software, an interface is a contract: if you implement the interface, you must provide the required methods.

```text
Interface: Storable
  - save(data)
  - load(id)

Class: S3Storage implements Storable    -> must have save() and load()
Class: DiskStorage implements Storable  -> must have save() and load()
```

The caller does not care which implementation is used. It just calls the interface.

---

## Interface vs Endpoint

- **Interface** = how you interact with a system
- **Endpoint** = where you reach that system

See [Endpoints](08_endpoints.md) for the address side of the same relationship.
