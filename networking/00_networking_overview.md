---
tags:
  - networking
created_at: 2026-03-13T00:00:00
updated_at: 2026-04-19T09:11:51
recent_editor: CLAUDE
---

# Networking Fundamentals — Overview

Foundation networking concepts needed to understand AWS services.

## Concepts

### Core Concepts
- [Protocols](01_protocols.md) — TCP, UDP, ICMP, HTTP, HTTPS, TLS, SSH, RDP.
- [Addressing](02_addressing.md) — Ports, IP addresses, CIDR, MAC addresses, traffic direction.

### Application Layer
- [HTTP](05_http.md) — Methods, status codes, REST API patterns.
- [DNS](04_dns.md) — Resolution flow, record types, Route 53 behavior.
- [Reverse Proxy](06_reverse_proxy.md) — Load balancing, TLS termination, path routing, Nginx/ALB/CloudFront.

### Reference Model
- [OSI Model](03_osi_model.md) — 7-layer model, encapsulation, AWS layer mapping.

## Quick Reference

| Port | Service |
|------|---------|
| 21 | FTP |
| 22 | SSH |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 110 | POP3 |
| 143 | IMAP |
| 443 | HTTPS |
| 3000 | React dev |
| 3306 | MySQL |
| 3389 | RDP |
| 5000 | Flask |
| 5173 | Vite |
| 5432 | PostgreSQL |
| 6379 | Redis |
| 8000 | FastAPI / Django |
| 8080 | Alt HTTP |
| 8501 | Streamlit |
| 27017 | MongoDB |

| Protocol | Reliable | Speed | Use Case |
|----------|----------|-------|----------|
| TCP | Yes | Slower | Web, SSH, databases |
| UDP | No | Faster | Streaming, gaming, DNS |
| ICMP | N/A | Fast | Diagnostics (ping) |

## Cross-references

- Protocols, Addressing → [Security Group](../aws/identity/02_security_group.md) (protocol + port rules)
- CIDR, Subnets → [Subnet](../aws/foundation/05_subnet.md), [VPC](../aws/foundation/04_amazon_vpc.md)
- HTTP → [ELB](../aws/networking/01_elastic_load_balancing.md) (ALB routes HTTP traffic)
- DNS → [VPC](../aws/foundation/04_amazon_vpc.md) (VPC DNS settings)
- Interfaces, Endpoints → [Interfaces](../computing/07_interfaces.md), [Endpoints](../computing/08_endpoints.md)

---
↑ [Home](../home.md)
