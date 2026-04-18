---
tags:
  - networking
created_at: 2026-03-13T00:00:00
updated_at: 2026-04-17T14:18:47
recent_editor: CLAUDE
---

↑ [Overview](./00_networking_overview.md)

# Protocols

## What It Is

A network protocol is a set of rules for how data is transmitted between devices. Different protocols serve different purposes: reliable delivery, fast delivery, diagnostics, encryption, and remote access.

## How It Works

### TCP (Transmission Control Protocol)

Connection-oriented protocol that guarantees reliable, ordered delivery.

1. Establishes connection via 3-way handshake (SYN → SYN-ACK → ACK)
2. Sends data in segments, waits for acknowledgment
3. Retransmits if packets are lost

Used for: web browsing (HTTP/HTTPS), email, file transfer, SSH, databases.

> **Tip:** Think of TCP like registered mail — you get confirmation of delivery.

### UDP (User Datagram Protocol)

Connectionless protocol that sends data without guarantees. No handshake, no acknowledgment, no retransmission.

Used for: video streaming, online gaming, voice calls, DNS queries.

> **Tip:** Think of UDP like shouting across a room — fast but might miss some words.

### ICMP (Internet Control Message Protocol)

Protocol for network diagnostics and error messages. Not used for data transfer.

- **Ping** — test if host is reachable (Echo Request/Reply)
- **Traceroute** — trace network path (Time Exceeded)
- **Destination Unreachable** — target can't be reached

### TCP vs UDP vs ICMP

| Aspect | TCP | UDP | ICMP |
|--------|-----|-----|------|
| Connection | Connection-oriented | Connectionless | Connectionless |
| Reliability | Reliable | Unreliable | N/A |
| Speed | Slower | Faster | Fast |
| Use case | Web, email, SSH | Streaming, gaming | Diagnostics |

### HTTP / HTTPS

- **HTTP** — Unencrypted web protocol (port 80). Data sent in plain text.
- **HTTPS** — HTTP + [TLS](#tls-transport-layer-security) encryption (port 443). Standard for all modern websites.

See [HTTP](05_http.md) for methods, status codes, and REST API details.

### TLS (Transport Layer Security)

Cryptographic protocol that provides encryption for network communications. Successor to SSL (deprecated).

1. Client connects to server
2. TLS handshake (exchange certificates, agree on encryption)
3. Encrypted connection established

Provides: encryption (scrambles data), authentication (verifies server identity via certificate), integrity (detects tampering).

Used by: HTTPS, secure email, VPN connections.

### SSH (Secure Shell)

Protocol for secure remote access to computers (port 22). Replaced insecure Telnet.

- Remote login and command execution
- File transfer (SCP, SFTP)
- Key-based authentication (recommended) or password

Used for Linux server administration. See [EC2](../aws/05_amazon_ec2.md) for AWS-specific SSH usage.

### RDP (Remote Desktop Protocol)

Protocol for remote graphical access to Windows computers (port 3389).

- Full graphical desktop transmitted
- Clipboard sharing, file transfer, printer redirection

Used for Windows server administration. See [EC2](../aws/05_amazon_ec2.md) for AWS-specific RDP usage.

> **Tip:** Never allow 0.0.0.0/0 on port 3389 — it's a common brute force target.

## Example

A web browser loading a page uses multiple protocols:
1. **DNS** (UDP port 53) resolves the domain to an IP
2. **TCP** establishes a connection to the server (3-way handshake)
3. **TLS** encrypts the connection (HTTPS)
4. **HTTP** sends the request and receives the response

## Why It Matters

Protocols determine which ports to open in [Security Groups](../aws/14_security_group.md), which [load balancer](../aws/16_elastic_load_balancing.md) type to use (NLB for TCP/UDP, ALB for HTTP), and how to troubleshoot connectivity issues.

---
[Overview](./00_networking_overview.md) | Next: [Addressing](02_addressing.md) →
