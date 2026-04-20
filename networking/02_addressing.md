---
tags:
  - networking
created_at: 2026-03-13T00:00:00
updated_at: 2026-04-20T13:22:53
recent_editor: CLAUDE
---

↑ [Overview](./00_networking_overview.md)

# Addressing

## What It Is

Network addressing is how devices and services are identified on a network. It covers IP addresses (which device), ports (which service), CIDR notation (which range), and MAC addresses (which physical interface).

## How It Works

### Ports

A port is a virtual endpoint for network connections, numbered 0–65535. IP address identifies the computer; port identifies the service.

> **Tip:** Think of IP address as a building address and port as the apartment number.

| Range | Name | Examples |
|-------|------|----------|
| 0–1023 | Well-known | 21 (FTP), 22 (SSH), 25 (SMTP), 53 (DNS), 80 (HTTP), 110 (POP3), 143 (IMAP), 443 (HTTPS) |
| 1024–49151 | Registered | 3000 (React dev), 3306 (MySQL), 3389 (RDP), 5000 (Flask), 5173 (Vite), 5432 (PostgreSQL), 6379 (Redis), 8000 (FastAPI/Django), 8080 (alt HTTP), 8501 (Streamlit), 27017 (MongoDB) |
| 49152–65535 | Ephemeral | Temporary client ports, auto-assigned by OS |

When your browser connects to a web server: `YourIP:54321 ↔ ServerIP:443`. The browser uses a random ephemeral port; the server listens on a well-known port.

### IPv4

32-bit address. Format: four numbers 0–255 separated by dots (e.g., `192.168.1.1`). Total: ~4.3 billion addresses.

- **Public IP** — routable on internet (e.g., `54.123.45.67`)
- **Private IP** — only within private network

**Private IP ranges (RFC 1918):**

| Range | Size |
|-------|------|
| `10.0.0.0/8` | 16 million IPs |
| `172.16.0.0/12` | 1 million IPs |
| `192.168.0.0/16` | 65,536 IPs |

Special: `127.0.0.1` (localhost), `0.0.0.0` (any address).

### IPv6

128-bit address. Format: eight groups of hex separated by colons (e.g., `2001:db8:85a3::8a2e:370:7334`). Massive address space (2^128). Adoption is slow because IPv4 + NAT still works for most use cases.

### CIDR (Classless Inter-Domain Routing)

Notation for specifying IP address ranges: `IP/prefix` where the prefix is how many bits are fixed.

| CIDR | IPs | Formula | Common use |
|------|-----|---------|------------|
| /32 | 1 | 2^0 | Single IP (SG rules) |
| /24 | 256 | 2^8 | Subnet |
| /16 | 65,536 | 2^16 | VPC |
| /8 | 16 million | 2^24 | Large network |

**Key rule:** Smaller prefix = bigger range. `/16` is bigger than `/24`.

AWS reserves 5 IPs per [subnet](../cloud/aws/foundation/05_subnet.md) (first 4 + last 1), so a /24 subnet has 251 usable IPs.

### MAC Address

48-bit physical address of a network interface (e.g., `00:1A:2B:3C:4D:5E`). Works at Layer 2 (Data Link). Unique per network card. In AWS, [ENIs](../computing/07_interfaces.md) have MAC addresses that persist when detached/reattached.

### Traffic Direction

- **Inbound** — traffic coming into your resource (e.g., user accessing your web server)
- **Outbound** — traffic going out from your resource (e.g., server downloading updates)

Controlled by inbound/outbound rules in [Security Groups](../cloud/aws/identity/02_security_group.md).

## Example

A typical AWS [VPC](../cloud/aws/foundation/04_amazon_vpc.md) setup:
- VPC CIDR: `10.0.0.0/16` (65,536 IPs)
- Public subnet: `10.0.1.0/24` (251 usable IPs)
- Private subnet: `10.0.2.0/24` (251 usable IPs)
- Security group allows inbound TCP port 443 from `0.0.0.0/0`

## Why It Matters

Every AWS networking decision involves addressing: choosing VPC and subnet CIDRs, opening ports in security groups, understanding public vs private IPs, and configuring inbound vs outbound rules.

---
↑ [Overview](./00_networking_overview.md)

**Related:** [Protocols](01_protocols.md), [OSI Model](03_osi_model.md), [subnet](../cloud/aws/foundation/05_subnet.md), [ENIs](../computing/07_interfaces.md), [Security Groups](../cloud/aws/identity/02_security_group.md), [VPC](../cloud/aws/foundation/04_amazon_vpc.md)
**Tags:** #networking
