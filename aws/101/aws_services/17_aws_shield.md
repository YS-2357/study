---
tags:
  - aws
  - security
created_at: 2026-03-20
updated_at: 2026-04-17
---
# AWS Shield

## What It Is
AWS Shield is a DDoS (Distributed Denial of Service) protection service.

**DDoS attack** = thousands/millions of fake requests flood your app to overwhelm it and make it unavailable for real users.

Shield has two tiers: Standard (free, automatic) and Advanced (paid, opt-in).

## How It Works

Shield Standard is always active at the AWS network edge. It learns your normal traffic baseline and uses anomaly detection plus known attack signature matching to identify DDoS floods. When an attack is detected, Shield drops malicious packets before they reach your resources. Shield Advanced adds 24/7 support from the Shield Response Team (SRT) and detailed real-time metrics for protected resources such as CloudFront, Route 53, and ELB.

## Console Access
- Search "Shield" in AWS Console
- AWS Shield > Getting started
- No "create" page — Shield Standard is automatic, Shield Advanced is a subscription


## How Shield Prevents DDoS

Shield sits at the **network entry point** of AWS — before traffic reaches your resources. It inspects all incoming traffic and filters out the bad stuff before it hits your app.

```
Normal traffic:
Internet → AWS network edge → Your app yes

DDoS attack (without Shield):
1 million fake requests → AWS network edge → Your app → overwhelmed → crashes no

DDoS attack (with Shield):
1 million fake requests → AWS network edge → Shield detects abnormal pattern
                                             → drops fake traffic
                                             → only real traffic passes → Your app yes
```

**How Shield detects DDoS:**
1. **Baseline learning** — Shield knows your normal traffic patterns (e.g., 1,000 requests/sec)
2. **Anomaly detection** — Sudden spike to 1,000,000 requests/sec? That's not normal
3. **Pattern matching** — Known attack signatures (SYN floods, UDP reflection have recognizable patterns)
4. **Filtering** — Drop the bad traffic, let good traffic through

**Why Shield specifically (not a firewall or WAF):**
- **Firewall/Security Group** = checks rules per connection (too slow for millions of requests)
- **WAF** = inspects request content (SQL injection, XSS) — good for Layer 7, but can't handle raw volume
- **Shield** = operates at network infrastructure level, can absorb and filter massive traffic volumes before they even reach your firewall or WAF

**Shield works because of AWS's scale:**
- AWS has massive global network bandwidth (multiple Tbps)
- A DDoS attack that would crush your single server is a tiny fraction of AWS's total capacity
- Shield uses that scale to absorb the flood and filter it

**Layered defense — each layer handles a different threat:**

| Layer | Service | What it stops |
|---|---|---|
| Network edge | **Shield** | Volume floods (millions of packets) |
| Application edge | **WAF** | Malicious requests (SQL injection, bad bots) |
| Resource level | **Security Group** | Unauthorized connections (wrong IP/port) |


## Two Tiers

| | Shield Standard | Shield Advanced |
|---|---|---|
| Cost | **Free** (automatic) | **$3,000/month** + data transfer fees |
| Protection | Basic DDoS (Layer 3/4) | Advanced DDoS (Layer 3/4/7) |
| Enabled | Automatically on ALL AWS accounts | You opt in (subscribe) |
| Response team | No | Yes — AWS Shield Response Team (SRT), 24/7 |
| Cost protection | No | Yes — AWS credits you for DDoS-caused scaling costs |
| Visibility | Basic | Detailed attack diagnostics, real-time metrics |
| WAF integration | No | Yes — AWS WAF included at no extra cost |
| Works with | All AWS resources | CloudFront, Route 53, ELB, EC2, Global Accelerator |

### Shield Standard (Free)
- You already have it — every AWS account gets it automatically
- Handles common network/transport layer DDoS attacks
- No configuration needed, no console page to manage
- Protects against SYN floods, UDP reflection attacks, etc.

### Shield Advanced ($3,000/month)
- Subscribe via console (subscription page)
- 1-year commitment required
- What you get:
  - **24/7 Shield Response Team (SRT)** — AWS DDoS experts help during attacks
  - **Cost protection** — If DDoS causes Auto Scaling/CloudFront to spike, AWS credits you
  - **AWS WAF included** — No additional WAF charges for resources protected by Shield Advanced
  - **Advanced metrics** — Real-time attack visibility, detailed diagnostics
  - **Health-based detection** — Uses Route 53 health checks for faster, more accurate detection


## Key Concepts

### DDoS Attack Layers
- **Layer 3 (Network — IP level)**
  - Attack: Send millions of packets with fake source IPs to flood bandwidth
  - Example: ICMP flood (ping flood), IP fragmentation attacks
  - Shield sees: source/destination IP addresses, packet counts
  - Shield Standard handles these

- **Layer 4 (Transport — TCP/UDP level)**
  - Attack: Exploit how TCP/UDP connections work
  - Example: **SYN flood** (millions of TCP SYN packets, never complete handshake → fills connection table), **UDP reflection** (small requests to public servers with your IP as source → huge responses sent to you)
  - Shield sees: ports, TCP flags (SYN/ACK), protocol type
  - Shield Standard handles these

- **Layer 7 (Application — HTTP level)**
  - Attack: Requests that look like real users but at massive scale
  - Example: **HTTP flood** (1 million GET requests/sec), **Slow POST** (open connections, send data very slowly to tie up resources)
  - Shield sees: HTTP headers, URLs, request patterns
  - **Shield Advanced only** — Standard can't inspect HTTP content

**Why Standard can't do Layer 7:**
- Layer 7 requires understanding HTTP (headers, URLs, cookies) — expensive to inspect at scale
- Standard only looks at packet headers (IP, port, TCP flags) — fast and cheap
- Advanced pays for the deeper inspection

```
OSI Layer    What Shield sees           Attack example         Which tier
─────────────────────────────────────────────────────────────────────────
Layer 7      HTTP headers, URLs         HTTP flood             Advanced only
Layer 4      TCP flags, ports           SYN flood              Standard + Advanced
Layer 3      IP addresses, packets      ICMP flood             Standard + Advanced
```

- See [OSI model doc](../../../networking/03_osi_model.md) for layer details

### Shield + WAF + CloudFront (Common Architecture)
```
Internet → CloudFront (edge) → WAF (filter bad requests) → ELB → EC2
              ↑                    ↑
         Shield protects      Shield protects
         at edge level        at app level
```
- **Shield** = blocks DDoS volume attacks
- **WAF** = filters malicious requests (SQL injection, XSS, bad bots)
- **CloudFront** = absorbs traffic at edge locations worldwide
- Together they form a layered defense

### Shield Advanced Protected Resources
You choose which resources to protect:
- Amazon CloudFront distributions
- Amazon Route 53 hosted zones
- Elastic Load Balancers (ELB)
- Amazon EC2 instances (Elastic IP)
- AWS Global Accelerator


## Precautions

### MAIN PRECAUTION: Shield Standard Is Already On — Don't Pay for Advanced Unless Needed
- Every AWS account already has Shield Standard for free
- Shield Advanced costs $3,000/month with 1-year commitment
- Most MSP clients do NOT need Advanced
- Only consider Advanced for high-profile targets (finance, gaming, media, government)

### 1. Shield Alone Doesn't Stop All Attacks
- Shield handles DDoS (volume attacks)
- For application-layer attacks (SQL injection, XSS), you need **AWS WAF**
- For best protection: Shield + WAF + CloudFront together

### 2. Shield Advanced Has a 1-Year Commitment
- $3,000/month, billed regardless of attacks
- Can't cancel before 1 year
- Make sure the client understands the commitment before subscribing

### 3. Use CloudFront in Front of Your App
- CloudFront absorbs DDoS traffic at 400+ edge locations worldwide
- Even with Shield Standard, CloudFront significantly improves DDoS resilience
- Free tier includes 1TB/month data transfer

### 4. Shield Advanced Cost Protection Requires Proper Setup
- Auto Scaling and CloudFront must be properly configured
- You must request credits through AWS Support after an attack
- Not automatic — you need to file for reimbursement

### 5. Always Use Tags
- Tag protected resources with environment, project, team, client
- Essential for MSP cost tracking, especially with Shield Advanced's $3,000/month

## Example

A media company enables Shield Advanced on their CloudFront distribution and ALB.
During a volumetric DDoS attack, Shield detects the anomaly and mitigates it at the edge.
The Shield Response Team (SRT) assists with fine-tuning, and cost protection credits any scaling charges caused by the attack.

## Why It Matters

DDoS attacks can take down any internet-facing application. Shield Standard provides baseline protection for free,
while Shield Advanced adds real-time visibility, SRT support, and cost protection for business-critical workloads.

## Official Documentation
- [AWS Shield Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html)
- [AWS Shield FAQs](https://aws.amazon.com/shield/faqs/)

---
← Previous: [Amazon IAM](15_amazon_iam.md) | [Overview](00_overview.md) | Next: [AWS WAF](18_aws_waf.md) →
