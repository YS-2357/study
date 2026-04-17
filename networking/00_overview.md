---
tags:
  - networking
created_at: 2026-03-13
updated_at: 2026-04-17
---
# Networking Fundamentals — Overview

Foundation networking concepts needed to understand AWS services.

## Study Order

### Core Concepts
1. [Protocols](01_protocols.md) — TCP, UDP, ICMP, HTTP, HTTPS, TLS, SSH, RDP.
2. [Addressing](02_addressing.md) — Ports, IP addresses, CIDR, MAC addresses, traffic direction.

### Application Layer
3. [HTTP](05_http.md) — Methods, status codes, REST API patterns.
4. [DNS](04_dns.md) — Resolution flow, record types, Route 53 behavior.
5. [Reverse Proxy](06_reverse_proxy.md) — Load balancing, TLS termination, path routing, Nginx/ALB/CloudFront.

### Reference Model
6. [OSI Model](03_osi_model.md) — 7-layer model, encapsulation, AWS layer mapping.

## Quick Reference

| Port | Service |
|------|---------|
| 22 | SSH |
| 80 | HTTP |
| 443 | HTTPS |
| 3306 | MySQL |
| 3389 | RDP |
| 5432 | PostgreSQL |

| Protocol | Reliable | Speed | Use Case |
|----------|----------|-------|----------|
| TCP | Yes | Slower | Web, SSH, databases |
| UDP | No | Faster | Streaming, gaming, DNS |
| ICMP | N/A | Fast | Diagnostics (ping) |

## Cross-references

- Protocols, Addressing → [Security Group](../aws/101/aws_services/14_security_group.md) (protocol + port rules)
- CIDR, Subnets → [Subnet](../aws/101/aws_services/03_subnet.md), [VPC](../aws/101/aws_services/04_amazon_vpc.md)
- HTTP → [ELB](../aws/101/aws_services/16_elastic_load_balancing.md) (ALB routes HTTP traffic)
- DNS → [VPC](../aws/101/aws_services/04_amazon_vpc.md) (VPC DNS settings)
- Interfaces, Endpoints → [Interfaces](../computing/07_interfaces.md), [Endpoints](../computing/08_endpoints.md)

---
↑ [Root](../00_overview.md)
