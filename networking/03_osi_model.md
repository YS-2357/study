---
tags:
  - networking
created_at: 2026-03-13T00:00:00
updated_at: 2026-04-17T14:18:47
recent_editor: CLAUDE
---

↑ [Overview](./00_networking_overview.md)

# OSI Model

## What It Is

The OSI (Open Systems Interconnection) model is a 7-layer framework that standardizes how network communication works. Each layer has a specific responsibility.

## How It Works

### The 7 Layers

| Layer | Name | What it does | Protocols/Examples | AWS Examples |
|-------|------|-------------|-------------------|--------------|
| 7 | Application | User-facing protocols | HTTP, HTTPS, SSH, DNS | ALB, API Gateway, CloudFront |
| 6 | Presentation | Encryption, formatting | TLS/SSL | TLS at load balancers |
| 5 | Session | Connection management | Sessions, RPC | Session persistence |
| 4 | Transport | Port-based delivery | TCP, UDP | NLB, Security Groups (ports) |
| 3 | Network | IP routing | IP, ICMP | VPC, IGW, NAT, SGs (IPs) |
| 2 | Data Link | MAC addressing | Ethernet, Wi-Fi | ENI MAC addresses |
| 1 | Physical | Bits on wire | Cables, signals | AWS infrastructure, Direct Connect |

**Mnemonic (top to bottom):** All People Seem To Need Data Processing.

> **Tip:** For most AWS work, focus on Layers 3, 4, and 7. These explain Security Groups, load balancer types, and routing.

### Encapsulation

When data moves down the stack, each layer wraps the upper layer's data with its own header:

```
Layer 4: [TCP header][HTTP data]
Layer 3: [IP header][TCP header][HTTP data]
Layer 2: [Frame header][IP header][TCP header][HTTP data]
```

- **Header** — control information a layer adds (ports, IPs, MACs)
- **Payload** — the data that layer is carrying

Receiving reverses the process (decapsulation): each layer strips its header and passes the payload up.

### OSI vs TCP/IP

| OSI (7 layers) | TCP/IP (4 layers) |
|----------------|-------------------|
| Application + Presentation + Session | Application |
| Transport | Transport |
| Network | Internet |
| Data Link + Physical | Network Access |

TCP/IP is what's actually used in practice. OSI is the educational model for understanding layers.

### AWS Layer Mapping

**[Security Groups](../aws/14_security_group.md)** — Layer 3–4 only. Filter by IP addresses and TCP/UDP ports. Cannot filter by URL or HTTP headers.

**Load Balancers:**
- [NLB](../aws/16_elastic_load_balancing.md) — Layer 4. Routes by IP and port. Very fast. Can't see HTTP headers.
- [ALB](../aws/16_elastic_load_balancing.md) — Layer 7. Routes by URL path, headers, host. Can terminate TLS.

### Troubleshooting by Layer

When debugging connectivity, work bottom-up:

1. **Layer 3:** Can you ping the IP? (`ping 10.0.1.5`)
2. **Layer 4:** Is the port open? (`nc -zv 10.0.1.5 80`)
3. **Layer 7:** Is the app responding? (`curl http://example.com`)

## Example

You can't access a website. Ping works (Layer 3 OK), but connecting to port 443 fails (Layer 4 blocked). Check the Security Group — port 443 is not allowed inbound. Fix the SG rule, and the site loads.

## Why It Matters

The OSI model explains why different AWS services operate at different layers: why ALB can route by URL path but NLB cannot, why Security Groups can't filter HTTP headers, and how to systematically debug network issues layer by layer.

---
← Previous: [Addressing](02_addressing.md) | [Overview](./00_networking_overview.md) | Next: [DNS](04_dns.md) →
