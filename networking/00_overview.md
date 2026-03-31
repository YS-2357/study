# Networking Fundamentals - Overview

## Purpose
Foundation networking concepts needed to understand AWS services.

## Contents

### Core Concepts
### [01. Protocols](01_protocols.md)
Core network protocols and how they work:
- **TCP** - Reliable, connection-oriented (web, SSH, databases)
- **UDP** - Fast, connectionless (streaming, gaming, DNS)
- **ICMP** - Network diagnostics (ping, traceroute)
- **HTTP/HTTPS** - Web protocols (see [05. HTTP](05_http.md) for deep dive)
- **SSH** - Secure remote access
- **TLS/SSL** - Encryption layer
- **FTP/SMTP** - File transfer and email

### [02. Addressing](02_addressing.md)
IP addressing, ports, and ranges:
- **IPv4/IPv6** - IP address formats
- **CIDR** - IP range notation (10.0.0.0/16)
- **Ports** - Service endpoints (80, 443, 22)
- **MAC Addresses** - Physical network addresses
- **Private IP Ranges** - RFC 1918 ranges
- **Ephemeral Ports** - Temporary client ports

### [03. OSI Model](03_osi_model.md)
7-layer networking model:
- Layer 7: Application (HTTP, SSH, DNS)
- Layer 4: Transport (TCP, UDP)
- Layer 3: Network (IP, ICMP)
- Layer 2: Data Link (Ethernet, MAC)
- Layer 1: Physical (cables, signals)

### Application Layer
### [04. DNS](04_dns.md)
Domain Name System deep dive:
- How DNS works (hierarchy, resolution)
- DNS in AWS VPC
- DNS records and zones
- Route 53 integration

### [05. HTTP](05_http.md)
HTTP in depth — beyond the basics in [01. Protocols](01_protocols.md):
- **HTTP Methods** - GET, POST, PUT, PATCH, DELETE (safe vs unsafe, idempotency)
- **Status Codes** - 1xx–5xx (what each means, when you see them)
- **REST API** - Principles, examples, REST vs GraphQL vs gRPC
- **AWS 5xx scenarios** - Common ALB, API Gateway, CloudFront errors

## How to Use

**For AWS beginners:**
- Start with [Protocols](01_protocols.md) - understand TCP/UDP/HTTP
- Then [Addressing](02_addressing.md) - learn CIDR and ports
- Then [HTTP](05_http.md) - status codes, REST APIs
- Skip OSI Model initially (come back later)

**If OSI feels abstract:**
- Read [OSI Model](03_osi_model.md) once for the big picture
- Re-read Layer 7, 4, and 3 first because they explain most AWS networking behavior
- Use the header/payload section in [OSI Model](03_osi_model.md) when encapsulation feels vague

**For troubleshooting:**
- [OSI Model](03_osi_model.md) - systematic debugging approach
- [DNS](04_dns.md) - name resolution issues
- [HTTP](05_http.md) - 4xx/5xx error diagnosis

**Cross-references:**
- HTTP → [Interfaces](../computing/07_interfaces.md) and [Endpoints](../computing/08_endpoints.md) (API, ENI, VPC endpoints)
- HTTP → [ELB](../aws/101/aws_services/16_elastic_load_balancing.md) (ALB routes HTTP traffic)
- DNS → [VPC](../aws/101/aws_services/04_amazon_vpc.md) (VPC DNS settings)
- Protocols → [Security Group](../aws/101/aws_services/14_security_group.md) (protocol + port rules)
- Addressing → [Subnet](../aws/101/aws_services/03_subnet.md) (CIDR, IPv4/IPv6)

## Quick Reference

### Common Ports
- 22: SSH
- 80: HTTP
- 443: HTTPS
- 3306: MySQL
- 5432: PostgreSQL
- 3389: RDP (Windows Remote Desktop)

### Private IP Ranges
- 10.0.0.0/8
- 172.16.0.0/12
- 192.168.0.0/16

### Protocol Comparison
| Protocol | Reliable | Speed | Use Case |
|----------|----------|-------|----------|
| TCP | Yes | Slower | Web, SSH, databases |
| UDP | No | Faster | Streaming, gaming |
| ICMP | N/A | Fast | Diagnostics |

### HTTP Status Code Cheat Sheet
| Range | Meaning | Key Codes |
|-------|---------|-----------|
| 2xx | Success | 200 OK, 201 Created, 204 No Content |
| 3xx | Redirect | 301 Permanent, 302 Temporary, 304 Not Modified |
| 4xx | Client error | 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found |
| 5xx | Server error | 500 Internal, 502 Bad Gateway, 503 Unavailable, 504 Timeout |
