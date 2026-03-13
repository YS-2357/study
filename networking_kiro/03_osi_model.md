# OSI Model (Open Systems Interconnection)

## What is OSI Model?
**Definition:** Conceptual framework that standardizes network communication into 7 layers.

**History:**
- Created in 1984 by ISO (International Organization for Standardization)
- Designed to standardize networking protocols
- Educational model for understanding networks

**Purpose:**
- Break down complex networking into manageable layers
- Each layer has specific responsibilities
- Layers communicate with layers above and below
- Helps troubleshoot network issues

## The 7 Layers (Top to Bottom)

### Layer 7 - Application
**What:** User-facing applications and protocols

**Examples:** HTTP, HTTPS, SSH, FTP, SMTP, DNS

**Function:** Provides network services to applications

**User interaction:** Direct (web browsers, email clients)

**In AWS:**
- Application Load Balancer operates here
- API Gateway
- CloudFront (HTTP/HTTPS)

---

### Layer 6 - Presentation
**What:** Data formatting, encryption, compression

**Examples:** TLS/SSL, JPEG, ASCII, EBCDIC

**Function:** Translates data between application and network format

**User interaction:** Transparent (happens automatically)

**In AWS:**
- TLS termination at load balancers
- Data encryption/decryption

---

### Layer 5 - Session
**What:** Manages connections between applications

**Examples:** NetBIOS, RPC, SQL sessions

**Function:** Establishes, maintains, terminates sessions

**User interaction:** Transparent

**In AWS:**
- Session persistence in load balancers
- Database connection pooling

---

### Layer 4 - Transport
**What:** End-to-end data delivery

**Examples:** TCP, UDP

**Function:** Reliable/unreliable delivery, flow control, error checking

**Ports:** Used at this layer (80, 443, 22, etc.)

**In AWS:**
- Network Load Balancer operates here
- Security Groups filter at this layer
- TCP/UDP port rules

---

### Layer 3 - Network
**What:** Routing and logical addressing

**Examples:** IP, ICMP, routers

**Function:** Routes packets across networks

**Addressing:** IP addresses (192.168.1.1)

**In AWS:**
- VPC routing tables
- Internet Gateway
- NAT Gateway
- Security Groups filter at this layer (IP addresses)

---

### Layer 2 - Data Link
**What:** Physical addressing and frame delivery

**Examples:** Ethernet, Wi-Fi, switches

**Function:** Transfers data between adjacent network nodes

**Addressing:** MAC addresses (00:1A:2B:3C:4D:5E)

**In AWS:**
- ENI (Elastic Network Interface) has MAC address
- Underlying AWS network infrastructure

---

### Layer 1 - Physical
**What:** Physical transmission of bits

**Examples:** Cables, fiber optics, radio waves, hubs

**Function:** Transmits raw bit stream over physical medium

**Hardware:** Network cables, connectors, signals

**In AWS:**
- AWS manages all physical infrastructure
- Direct Connect physical connections

---

## Mnemonic to Remember

**Top to Bottom:** "All People Seem To Need Data Processing"
- **A**pplication
- **P**resentation
- **S**ession
- **T**ransport
- **N**etwork
- **D**ata Link
- **P**hysical

**Bottom to Top:** "Please Do Not Throw Sausage Pizza Away"

---

## How Data Flows

### Sending data (top to bottom - Encapsulation)
1. **Application** creates data (Layer 7)
2. **Presentation** formats/encrypts data (Layer 6)
3. **Session** manages connection (Layer 5)
4. **Transport** adds TCP/UDP header with ports (Layer 4)
5. **Network** adds IP header with addresses (Layer 3)
6. **Data Link** adds Ethernet frame with MAC addresses (Layer 2)
7. **Physical** transmits bits (Layer 1)

### Receiving data (bottom to top - Decapsulation)
1. **Physical** receives bits (Layer 1)
2. **Data Link** removes Ethernet frame (Layer 2)
3. **Network** removes IP header (Layer 3)
4. **Transport** removes TCP/UDP header (Layer 4)
5. **Session** manages connection (Layer 5)
6. **Presentation** decrypts/formats data (Layer 6)
7. **Application** receives data (Layer 7)

### Example: Sending email
```
Layer 7: Email application (SMTP)
Layer 6: Encrypt with TLS
Layer 5: Establish session
Layer 4: TCP segments with port 587
Layer 3: IP packets with source/destination IPs
Layer 2: Ethernet frames with MAC addresses
Layer 1: Electrical signals on cable
```

---

## OSI vs TCP/IP Model

**OSI (7 layers)** - Theoretical model for education

**TCP/IP (4 layers)** - Practical implementation used in real networks

| OSI Layer | TCP/IP Layer | Protocols |
|-----------|--------------|-----------|
| Application | Application | HTTP, HTTPS, SSH, FTP, SMTP, DNS |
| Presentation | Application | TLS/SSL |
| Session | Application | - |
| Transport | Transport | TCP, UDP |
| Network | Internet | IP, ICMP |
| Data Link | Network Access | Ethernet, Wi-Fi |
| Physical | Network Access | Cables, signals |

**Key difference:**
- OSI: 7 layers (more detailed, educational)
- TCP/IP: 4 layers (simplified, practical)
- **TCP/IP is what's actually used** - OSI is for understanding

---

## Why OSI Matters for AWS

### Security Groups (Layer 3-4)
- Work at Network and Transport layers
- Filter based on:
  - IP addresses (Layer 3)
  - TCP/UDP ports (Layer 4)
- **Don't see application layer data** (can't filter by URL or HTTP headers)

### Load Balancers
- **Network Load Balancer (NLB)** - Layer 4 (TCP/UDP)
  - Routes based on IP and port
  - Very fast, low latency
  - Can't see HTTP headers
  
- **Application Load Balancer (ALB)** - Layer 7 (HTTP/HTTPS)
  - Routes based on URL path, headers, host
  - Can terminate TLS
  - Content-based routing

- **Classic Load Balancer (CLB)** - Layer 4 and 7
  - Legacy, not recommended for new applications

### Troubleshooting by Layer
**Systematic approach to debugging network issues:**

**Layer 1 (Physical):**
- Is cable plugged in?
- Is network interface up?
- Check: `ip link show` or `ifconfig`

**Layer 2 (Data Link):**
- Is MAC address correct?
- Is switch port configured?
- Check: `arp -a`

**Layer 3 (Network):**
- Can you ping the IP address?
- Is routing configured?
- Check: `ping 10.0.1.5`, `traceroute`

**Layer 4 (Transport):**
- Is the port open?
- Is firewall blocking?
- Check: `telnet 10.0.1.5 80`, `nc -zv 10.0.1.5 80`

**Layer 5-6 (Session/Presentation):**
- Is TLS handshake succeeding?
- Certificate valid?
- Check: `openssl s_client -connect example.com:443`

**Layer 7 (Application):**
- Is application running?
- Is it responding correctly?
- Check: `curl http://example.com`, application logs

### Example: Can't access website

**Troubleshoot bottom-up:**
1. **Physical:** Network connected? ✓
2. **Data Link:** Interface up? ✓
3. **Network:** Can ping server IP? ✓
4. **Transport:** Can connect to port 443? ✗ **FOUND ISSUE**
5. Check Security Group - port 443 not allowed!

---

## Layer Responsibilities Summary

| Layer | What it does | AWS Examples |
|-------|--------------|--------------|
| 7 - Application | User applications | ALB, API Gateway, CloudFront |
| 6 - Presentation | Encryption, formatting | TLS at load balancers |
| 5 - Session | Connection management | Session persistence |
| 4 - Transport | Port-based delivery | NLB, Security Groups (ports) |
| 3 - Network | IP routing | VPC, IGW, NAT, Security Groups (IPs) |
| 2 - Data Link | MAC addressing | ENI MAC addresses |
| 1 - Physical | Bits on wire | AWS infrastructure, Direct Connect |

---

## Common Misconceptions

**"Security Groups work at all layers"**
- ✗ False - Only Layer 3-4 (IP and ports)
- Can't filter by HTTP URL or headers

**"Load balancers are all the same"**
- ✗ False - NLB (Layer 4) vs ALB (Layer 7) have different capabilities

**"OSI and TCP/IP are the same"**
- ✗ False - OSI is 7 layers (theoretical), TCP/IP is 4 layers (practical)

**"Need to memorize all layers for AWS"**
- ✗ False - Focus on Layers 3, 4, and 7 for most AWS work
