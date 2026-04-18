---
tags:
  - networking
created_at: 2026-03-13T00:00:00
updated_at: 2026-04-17T14:18:47
recent_editor: CLAUDE
---

↑ [Overview](./00_networking_overview.md)

# DNS (Domain Name System)

## What It Is

DNS is a distributed system that translates human-readable domain names to IP addresses. Example: `example.com` → `93.184.216.34`.

## Analogy

Like a phone book for the internet — converts names to numbers so you don't have to memorize IP addresses.

## How It Works

### Resolution Flow

1. Browser checks its cache
2. If not cached, asks a DNS resolver (e.g., 8.8.8.8)
3. Resolver queries the hierarchy:
   - **Root servers** → "Who handles `.com`?"
   - **TLD servers** → "Who handles `example.com`?"
   - **Authoritative nameservers** → "`example.com` is `93.184.216.34`"
4. Resolver returns and caches the answer

```
Browser → Resolver → Root → TLD → Authoritative → Answer
   ↑                                                  ↓
   └──────────────── 93.184.216.34 ─────────────────┘
```

### Record Types

| Type | Purpose | Example |
|------|---------|---------|
| **A** | Domain → IPv4 | `example.com → 93.184.216.34` |
| **AAAA** | Domain → IPv6 | `example.com → 2606:2800:...` |
| **CNAME** | Alias to another domain | `www.example.com → example.com` |
| **MX** | Mail server | `example.com → mail.example.com` |
| **NS** | Authoritative nameservers | `example.com → ns1.example.com` |
| **TXT** | Arbitrary text (verification, SPF) | `"v=spf1 include:..."` |

### TTL and Caching

TTL (Time To Live) controls how long a DNS record is cached. Set by the domain owner.
- 300s (5 min) — frequent changes
- 3600s (1 hour) — normal
- 86400s (24 hours) — rarely changes

Cache levels: browser → OS → resolver → ISP. Changing DNS takes time to propagate because of caching at every level.

> **Tip:** Lower TTL before making DNS changes, then raise it after propagation.

### DNS in AWS

**Route 53** is AWS's DNS service (authoritative nameserver + domain registration).

Routing policies:
- **Simple** — single resource
- **Weighted** — distribute by percentage
- **Latency** — route to lowest latency region
- **Failover** — primary/secondary with health checks
- **Geolocation** — route based on user location

**VPC DNS:**
- AWS provides a DNS server at VPC CIDR +2 (e.g., VPC `10.0.0.0/16` → DNS at `10.0.0.2`)
- **DNS resolution** — enables name resolution within VPC (keep enabled)
- **DNS hostnames** — gives instances DNS names (enable for public instances)
- **Private hosted zones** — internal DNS (e.g., `db.internal.company.com → 10.0.2.5`)

## Example

You type `example.com` in your browser. The browser doesn't know the IP, so it asks the OS resolver, which asks `8.8.8.8`, which walks the hierarchy (root → `.com` TLD → `example.com` authoritative) and returns `93.184.216.34`. The browser connects to that IP. The whole process takes milliseconds because most steps are cached.

## Why It Matters

DNS is the first step in every network connection. Misconfigured DNS (wrong records, missing hostnames, TTL too high) causes hard-to-debug connectivity issues. In AWS, enabling VPC DNS hostnames is required for many services to work, and Route 53 routing policies enable multi-region architectures.

---
← Previous: [OSI Model](03_osi_model.md) | [Overview](./00_networking_overview.md) | Next: [HTTP](05_http.md) →
