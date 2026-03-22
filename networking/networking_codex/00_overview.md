# OSI 7 Layers - Overview

This folder is for studying the OSI 7-layer model in a simple way.

The goal is not to memorize every protocol detail at once. The goal is to understand:
- what each layer does
- where common protocols fit
- how to think about network problems step by step
- how this connects to AWS services

## Study Order

1. Read [01. OSI 7 Layers](01_osi_7_layers.md) once from top to bottom
2. Read [02. Header and Payload](02_header_and_payload.md) after the first pass if encapsulation feels unclear
3. Read [03. Why Googling Feels Fast](03_why_googling_feels_fast.md) if you want a practical example of all layers working together
4. Read [01. OSI 7 Layers](01_osi_7_layers.md) again and focus only on Layer 7, 4, and 3 first
5. Come back to Layers 6, 5, 2, and 1 after the big picture is clear

## Why OSI Matters

OSI is a conceptual model that breaks network communication into 7 layers.

It helps you:
- organize networking concepts
- understand what a protocol is responsible for
- troubleshoot by asking "which layer is failing?"

## Quick Summary

| Layer | Name | Main Idea | Common Examples |
|-------|------|-----------|-----------------|
| 7 | Application | User-facing network services | HTTP, HTTPS, DNS, SMTP, SSH |
| 6 | Presentation | Data format, encryption, compression | TLS/SSL, JPEG, ASCII |
| 5 | Session | Connection/session management | RPC, SQL sessions |
| 4 | Transport | End-to-end delivery and ports | TCP, UDP |
| 3 | Network | IP addressing and routing | IP, ICMP |
| 2 | Data Link | Local delivery with frames and MAC | Ethernet, MAC |
| 1 | Physical | Raw signal transmission | cable, fiber, radio |

## OSI vs TCP/IP

OSI is mainly a learning model.

Real systems mostly use the TCP/IP model, which is more practical and less detailed.

Still, OSI is useful because it gives you a cleaner mental model for studying and troubleshooting.

## AWS Connection

You do not need OSI to use AWS, but it becomes very helpful when learning:
- Security Groups
- VPC routing
- Load Balancers
- DNS
- TLS/HTTPS

In practice:
- Layer 7 helps with ALB, API Gateway, HTTP routing
- Layer 4 helps with TCP/UDP and ports
- Layer 3 helps with IP, subnet, and route tables

## What to Focus On First

If you are new, remember these first:
- Layer 7 = application protocols like HTTP
- Layer 4 = TCP/UDP and ports
- Layer 3 = IP addresses and routing

Those three layers explain a large part of everyday AWS networking.

## Why Layers 7, 4, and 3 Matter Most in Practice

These three layers are the most practical starting point because many real AWS issues appear here first.

- Layer 7 asks: is the application request correct?
- Layer 4 asks: can the connection open on the required port and protocol?
- Layer 3 asks: can traffic reach the destination network at all?

In practice:
- Layer 7 helps with HTTP/HTTPS, DNS behavior, ALB routing, API Gateway, and CloudFront behavior
- Layer 4 helps with TCP/UDP, ports, Security Groups, and NLB behavior
- Layer 3 helps with IP addresses, subnets, route tables, Internet Gateway, and NAT Gateway

That is why Layer 7, 4, and 3 explain a large percentage of day-to-day AWS troubleshooting.
