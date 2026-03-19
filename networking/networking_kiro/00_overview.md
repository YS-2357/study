# Networking Fundamentals - Overview

## Purpose
Foundation networking concepts needed to understand AWS services.

## Contents

### [01. Protocols](01_protocols.md)
Core network protocols and how they work:
- **TCP** - Reliable, connection-oriented (web, SSH, databases)
- **UDP** - Fast, connectionless (streaming, gaming, DNS)
- **ICMP** - Network diagnostics (ping, traceroute)
- **HTTP/HTTPS** - Web protocols
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

### [04. DNS](04_dns.md)
Domain Name System deep dive:
- How DNS works (hierarchy, resolution)
- DNS in AWS VPC
- DNS records and zones
- Route 53 integration

## How to Use

**For AWS beginners:**
- Start with [Protocols](01_protocols.md) - understand TCP/UDP/HTTP
- Then [Addressing](02_addressing.md) - learn CIDR and ports
- Skip OSI Model initially (come back later)

**For troubleshooting:**
- [OSI Model](03_osi_model.md) - systematic debugging approach
- [DNS](04_dns.md) - name resolution issues

**Referenced by AWS services:**
- [Subnet](../aws_services_kiro/03_subnet.md) - CIDR, IPv4/IPv6
- [VPC](../aws_services_kiro/04_amazon_vpc.md) - DNS, CIDR, IPv6
- [Security Group](../aws_services_kiro/23_security_group.md) - Protocols, ports, traffic

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
