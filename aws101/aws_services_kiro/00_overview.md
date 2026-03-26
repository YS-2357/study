# DELETED - Content moved to networking_kiro folder

This file has been split into:
- [networking_kiro/00_overview.md](../networking_kiro/00_overview.md) - Overview and index
- [networking_kiro/01_protocols.md](../networking_kiro/01_protocols.md) - TCP, UDP, ICMP, HTTP, HTTPS, SSH, etc.
- [networking_kiro/02_addressing.md](../networking_kiro/02_addressing.md) - IP, CIDR, ports, MAC
- [networking_kiro/03_osi_model.md](../networking_kiro/03_osi_model.md) - 7 layers
- [networking_kiro/04_dns.md](../networking_kiro/04_dns.md) - DNS deep dive
Fundamental networking concepts needed to understand AWS services like VPC, Security Groups, and Load Balancers.

**Referenced by:**
- [Subnet](03_subnet.md) - CIDR, IPv4/IPv6, NACL vs SG
- [VPC](04_amazon_vpc.md) - DNS, CIDR, IPv6
- [Security Group](23_security_group.md) - Protocols, ports, traffic

## Protocols

### TCP (Transmission Control Protocol)
**Definition:** Connection-oriented protocol that guarantees reliable data delivery.

**How it works:**
1. Establishes connection (3-way handshake)
2. Sends data in segments
3. Waits for acknowledgment
4. Retransmits if packet lost
5. Ensures correct order

**History:**
- Created in 1974 by Vint Cerf and Bob Kahn
- Designed for reliable transmission over unreliable networks (ARPANET)
- Foundation of modern internet

**Characteristics:**
- Reliable (guarantees delivery)
- Ordered (packets arrive in sequence)
- Error-checked (detects corruption)
- Slower (due to overhead)

**Use cases:**
- Web browsing (HTTP/HTTPS)
- Email (SMTP, IMAP)
- File transfer (FTP, SFTP)
- SSH (remote access)
- Databases (MySQL, PostgreSQL)

**Analogy:** Like registered mail - you get confirmation of delivery.

---

### UDP (User Datagram Protocol)
**Definition:** Connectionless protocol that sends data without guarantees.

**How it works:**
1. Just sends packets
2. No handshake
3. No acknowledgment
4. No retransmission
5. No order guarantee

**History:**
- Created in 1980 by David P. Reed
- Designed for speed when reliability isn't critical
- Simpler than TCP

**Characteristics:**
- Fast (no overhead)
- Unreliable (packets may be lost)
- Unordered (packets may arrive out of sequence)
- No error recovery

**Use cases:**
- Video streaming (YouTube, Netflix)
- Online gaming
- Voice calls (VoIP)
- DNS queries
- Live broadcasts

**Analogy:** Like shouting across a room - fast but might miss some words.

---

### ICMP (Internet Control Message Protocol)
**Definition:** Protocol for network diagnostics and error messages.

**How it works:**
- Sends control and error messages
- Not used for data transfer
- Works at network layer (IP level)

**History:**
- Created in 1981 (RFC 792)
- Designed for network troubleshooting
- Part of IP suite

**Message types:**
- Echo Request/Reply (ping)
- Destination Unreachable
- Time Exceeded (TTL expired)
- Redirect

**Use cases:**
- **Ping** - Test if host is reachable
- **Traceroute** - Trace network path
- **Network diagnostics** - Identify connectivity issues

**Analogy:** Like asking "are you there?" and getting "yes" back.

---

## Ports

### What is a Port?
**Definition:** Virtual endpoint for network connections, numbered 0-65535.

**Purpose:** Allows multiple services to run on same IP address.

**How it works:**
- IP address identifies the computer
- Port identifies the specific service/application
- Combination: IP:Port (e.g., 192.168.1.1:80)

**Analogy:** 
- IP address = building address
- Port = apartment number
- You need both to reach the right destination

### Port Ranges

**Well-Known Ports (0-1023)**
- Reserved for standard services
- Require admin/root privileges to use
- Examples:
  - 20, 21: FTP (File Transfer Protocol)
  - 22: SSH (Secure Shell)
  - 23: Telnet
  - 25: SMTP (Email)
  - 53: DNS (Domain Name System)
  - 80: HTTP (Web)
  - 110: POP3 (Email)
  - 143: IMAP (Email)
  - 443: HTTPS (Secure Web)
  - 3306: MySQL
  - 5432: PostgreSQL

**Registered Ports (1024-49151)**
- Used by specific applications
- Don't require special privileges
- Examples:
  - 3000: Node.js development
  - 5000: Flask development
  - 8080: Alternative HTTP
  - 8443: Alternative HTTPS

**Ephemeral Ports (49152-65535)**
- Temporary ports for client connections
- Automatically assigned by OS
- Used for outbound connections
- Released when connection closes

**Note:** In practice, ephemeral range often starts at 1024 or 32768 depending on OS.

### How Ports Work in Communication

**Example: Web browsing**
1. Your browser connects from random ephemeral port (e.g., 54321)
2. To web server on port 80 or 443
3. Connection: YourIP:54321 ↔ ServerIP:80
4. Server responds to your ephemeral port
5. When done, ephemeral port is released

---

## Traffic

### What is Traffic?
**Definition:** Data flowing through a network.

### Traffic Direction

**Inbound Traffic**
- Traffic coming INTO your resource
- Example: User accessing your web server
- Controlled by inbound rules in Security Groups

**Outbound Traffic**
- Traffic going OUT from your resource
- Example: Your server downloading updates
- Controlled by outbound rules in Security Groups

### Traffic Flow Example
```
User (1.2.3.4:54321) → Internet → Your Server (10.0.1.5:80)
                    [Inbound Traffic]

Your Server (10.0.1.5:54321) → Internet → External API (8.8.8.8:443)
                    [Outbound Traffic]
```

---

## Network Interfaces

### ENI (Elastic Network Interface)
**Definition:** Virtual network card for AWS EC2 instances.

**Components:**
- Primary private IPv4 address
- One or more secondary private IPv4 addresses
- One Elastic IP per private IPv4
- One public IPv4 address
- One or more IPv6 addresses
- Security groups
- MAC address
- Source/destination check flag

**Use cases:**
- Attach/detach from instances
- Multiple network interfaces per instance
- Failover (move ENI to standby instance)
- Separate management and data networks

**Analogy:** Like a physical network card (NIC), but virtual and flexible.

---

## IP Addressing

### IPv4 Address
**Format:** Four numbers (0-255) separated by dots
- Example: 192.168.1.1
- Total: ~4.3 billion addresses

**Types:**
- **Public IP** - Routable on internet (e.g., 54.123.45.67)
- **Private IP** - Only within private network (e.g., 10.0.1.5)

**Private IP Ranges (RFC 1918):**
- 10.0.0.0/8 (10.0.0.0 to 10.255.255.255)
- 172.16.0.0/12 (172.16.0.0 to 172.31.255.255)
- 192.168.0.0/16 (192.168.0.0 to 192.168.255.255)

### IPv6 Address
**Format:** Eight groups of hexadecimal separated by colons
- Example: 2001:0db8:85a3:0000:0000:8a2e:0370:7334
- Total: 340 undecillion addresses

---

## DNS (Domain Name System)

### What is DNS?
**Definition:** System that translates domain names ↔ IP addresses.

**Example:** example.com ↔ 93.184.216.34

### How DNS Works
1. You ask: "What's the IP for example.com?"
2. DNS resolver checks cache
3. If not cached, queries hierarchy:
   - Root DNS servers → "Ask .com servers"
   - TLD (.com) servers → "Ask example.com's nameservers"
   - Authoritative nameservers → "93.184.216.34"
4. Returns answer and caches it

**DNS is a distributed hierarchical database:**
- **Root DNS servers** - Know where to find .com, .org, .net
- **TLD servers** - Know where to find specific domains under .com
- **Authoritative nameservers** - Have actual IP addresses (Route 53 in AWS)

### DNS in AWS VPC
**DNS resolver:** AWS DNS server at VPC CIDR +2 (e.g., 10.0.0.2 for 10.0.0.0/16)

**DNS resolution setting:** Enables DNS resolution within VPC

**DNS hostnames setting:** Gives instances DNS names (e.g., ec2-54-123-45-67.compute-1.amazonaws.com)

---

## CIDR (Classless Inter-Domain Routing)

### What is CIDR?
**Definition:** Notation for specifying IP address ranges.

**Format:** `IP address/prefix length` (e.g., 10.0.0.0/16)

### How CIDR Works
The number after `/` indicates how many bits are fixed (network portion).

**Examples:**
- **/32** = 1 IP (all 32 bits fixed)
  - 10.0.0.1/32 = only 10.0.0.1
- **/24** = 256 IPs (first 24 bits fixed, last 8 bits variable)
  - 10.0.1.0/24 = 10.0.1.0 to 10.0.1.255
- **/16** = 65,536 IPs (first 16 bits fixed, last 16 bits variable)
  - 10.0.0.0/16 = 10.0.0.0 to 10.0.255.255
- **/8** = 16,777,216 IPs (first 8 bits fixed, last 24 bits variable)
  - 10.0.0.0/8 = 10.0.0.0 to 10.255.255.255

**Key rule:** Smaller prefix number = bigger range
- /16 is bigger than /24
- /24 is bigger than /32

### Common AWS CIDR Usage
- **VPC:** 10.0.0.0/16 (65,536 IPs)
- **Subnet:** 10.0.1.0/24 (256 IPs, but AWS reserves 5)
- **Single IP:** 1.2.3.4/32 (for security group rules)

### Private IP Ranges (RFC 1918)
**Definition:** Managed list of CIDR blocks.

**Purpose:**
- AWS maintains lists of service IP ranges
- S3, CloudFront, EC2, etc.
- Automatically updated by AWS

**Use in Security Groups:**
- Reference AWS service IPs without manual updates
- Example: Allow outbound to S3 prefix list
- Easier than maintaining CIDR blocks manually

**Types:**
- **AWS-managed** - Maintained by AWS (S3, CloudFront, etc.)
- **Customer-managed** - You create and maintain

---

## Common Networking Terms

### Handshake
Initial connection setup process between client and server.

**TCP 3-Way Handshake:**
1. **SYN (Synchronize)** - Client sends: "I want to connect"
2. **SYN-ACK (Synchronize-Acknowledge)** - Server responds: "OK, I'm ready"
3. **ACK (Acknowledge)** - Client confirms: "Great, let's start"

**Visual:**
```
Client                    Server
  |                          |
  |-------- SYN ------------>|  (1. Client: "Hello, let's connect")
  |                          |
  |<------ SYN-ACK ----------|  (2. Server: "OK, I'm ready")
  |                          |
  |-------- ACK ------------>|  (3. Client: "Confirmed, let's go")
  |                          |
  |<==== Data Transfer ====>|  (Now connected, send data)
```

**Why it's needed:**
- Establishes connection before sending data
- Both sides agree on initial sequence numbers
- Ensures both can send and receive

**Analogy:** Like saying "hello" and confirming you can hear each other before starting a conversation.

**UDP doesn't have handshake** - just starts sending data immediately (faster but no guarantee).

### Packet
- Unit of data transmitted over network
- Contains header (metadata) and payload (data)

### Latency
- Time delay in data transmission
- Measured in milliseconds (ms)

### Bandwidth
- Maximum data transfer rate
- Measured in bits per second (bps, Mbps, Gbps)

### Throughput
- Actual data transfer rate achieved
- Usually less than bandwidth due to overhead

### TTL (Time To Live)
- Hop limit for packets
- Prevents infinite loops
- Decremented at each router

### MAC Address
- Physical address of network interface
- 48-bit identifier (e.g., 00:1A:2B:3C:4D:5E)
- Unique per network card

---

## Application Layer Protocols

### HTTP (HyperText Transfer Protocol)
**Definition:** Protocol for transferring web pages and data over the internet.

**History:**
- Created in 1989 by Tim Berners-Lee
- Foundation of the World Wide Web
- Current version: HTTP/2 (2015), HTTP/3 (2022)

**How it works:**
- Client (browser) sends request to server
- Server responds with HTML, images, etc.
- Stateless (each request independent)
- Uses TCP port 80

**Characteristics:**
- **Unencrypted** - Data sent in plain text
- **Not secure** - Anyone can read the data
- **Fast** - No encryption overhead

**Use cases:**
- Non-sensitive websites
- Internal applications
- Development/testing

**Analogy:** Like sending a postcard - anyone can read it.

---

### HTTPS (HyperText Transfer Protocol Secure)
**Definition:** Encrypted version of HTTP using TLS/SSL.

**History:**
- Created in 1994 by Netscape
- Now standard for all websites
- Uses TLS (Transport Layer Security)

**How it works:**
- HTTP + TLS encryption
- Client and server establish encrypted connection
- All data encrypted in transit
- Uses TCP port 443

**Characteristics:**
- **Encrypted** - Data scrambled, unreadable to others
- **Secure** - Protects passwords, credit cards, personal data
- **Authenticated** - Verifies server identity (SSL certificate)
- **Slightly slower** - Encryption overhead (minimal)

**Use cases:**
- All modern websites (Google, banks, e-commerce)
- Any site handling sensitive data
- Required for login pages

**Analogy:** Like sending a sealed letter - only recipient can read it.

**HTTPS = HTTP + TLS**

---

### TLS/SSL (Transport Layer Security / Secure Sockets Layer)
**Definition:** Cryptographic protocol that provides encryption for network communications.

**History:**
- **SSL** created in 1995 by Netscape (SSL 2.0, 3.0)
- **TLS 1.0** released in 1999 as SSL successor
- Current: TLS 1.3 (2018) - SSL is deprecated

**How it works:**
1. Client connects to server
2. TLS handshake (exchange certificates, agree on encryption)
3. Encrypted connection established
4. Data transmitted securely

**What it does:**
- **Encryption** - Scrambles data so only recipient can read
- **Authentication** - Verifies server identity (certificate)
- **Integrity** - Detects if data was tampered with

**Use cases:**
- HTTPS (web browsing)
- Email (SMTPS, IMAPS)
- VPN connections
- Any secure communication

**Note:** "SSL" is still commonly used term, but technically it's TLS now.

---

### SSH (Secure Shell)
**Definition:** Protocol for secure remote access to computers.

**History:**
- Created in 1995 by Tatu Ylönen
- Replaced insecure Telnet
- Current version: SSH-2

**How it works:**
- Client connects to server on port 22
- Authentication (password or key-based)
- Encrypted connection established
- Remote command execution

**What it does:**
- **Remote login** - Access server command line
- **File transfer** - SCP, SFTP
- **Port forwarding** - Tunnel other protocols
- **Encryption** - All data encrypted

**Use cases:**
- Server administration (AWS EC2)
- Git operations (GitHub, GitLab)
- File transfers
- Remote development

**Authentication methods:**
- **Password** - Username + password (less secure)
- **Key-based** - Public/private key pair (more secure, recommended)

**Analogy:** Like having a secure phone line to control a remote computer.

---

### FTP (File Transfer Protocol)
**Definition:** Protocol for transferring files between computers.

**History:**
- Created in 1971 (one of the oldest protocols)
- Predates TCP/IP
- Uses TCP ports 20 (data) and 21 (control)

**Characteristics:**
- **Unencrypted** - Data and passwords sent in plain text
- **Not secure** - Avoid for sensitive data
- **Two connections** - Control and data channels

**Use cases:**
- Legacy systems
- Internal networks
- Non-sensitive file transfers

**Secure alternatives:**
- **SFTP** - SSH File Transfer Protocol (encrypted, port 22)
- **FTPS** - FTP over TLS (encrypted, port 990)

---

### SMTP (Simple Mail Transfer Protocol)
**Definition:** Protocol for sending email.

**History:**
- Created in 1982
- Standard for email transmission
- Uses TCP port 25 (or 587 for submission)

**How it works:**
- Email client sends to SMTP server
- SMTP server forwards to recipient's server
- Recipient retrieves via IMAP/POP3

**Secure version:**
- **SMTPS** - SMTP over TLS (port 465 or 587)

---

### DNS (Domain Name System)
**Already covered in detail above** - See DNS section.

---

## OSI Model (Open Systems Interconnection)

### What is OSI Model?
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

### The 7 Layers (Top to Bottom)

**Layer 7 - Application**
- **What:** User-facing applications and protocols
- **Examples:** HTTP, HTTPS, SSH, FTP, SMTP, DNS
- **Function:** Provides network services to applications
- **User interaction:** Direct (web browsers, email clients)

**Layer 6 - Presentation**
- **What:** Data formatting, encryption, compression
- **Examples:** TLS/SSL, JPEG, ASCII, EBCDIC
- **Function:** Translates data between application and network format
- **User interaction:** Transparent (happens automatically)

**Layer 5 - Session**
- **What:** Manages connections between applications
- **Examples:** NetBIOS, RPC, SQL sessions
- **Function:** Establishes, maintains, terminates sessions
- **User interaction:** Transparent

**Layer 4 - Transport**
- **What:** End-to-end data delivery
- **Examples:** TCP, UDP
- **Function:** Reliable/unreliable delivery, flow control, error checking
- **Ports:** Used at this layer (80, 443, 22, etc.)

**Layer 3 - Network**
- **What:** Routing and logical addressing
- **Examples:** IP, ICMP, routers
- **Function:** Routes packets across networks
- **Addressing:** IP addresses (192.168.1.1)

**Layer 2 - Data Link**
- **What:** Physical addressing and frame delivery
- **Examples:** Ethernet, Wi-Fi, switches
- **Function:** Transfers data between adjacent network nodes
- **Addressing:** MAC addresses (00:1A:2B:3C:4D:5E)

**Layer 1 - Physical**
- **What:** Physical transmission of bits
- **Examples:** Cables, fiber optics, radio waves, hubs
- **Function:** Transmits raw bit stream over physical medium
- **Hardware:** Network cables, connectors, signals

### Mnemonic to Remember
**Top to Bottom:** "All People Seem To Need Data Processing"
- **A**pplication
- **P**resentation
- **S**ession
- **T**ransport
- **N**etwork
- **D**ata Link
- **P**hysical

**Bottom to Top:** "Please Do Not Throw Sausage Pizza Away"

### How Data Flows

**Sending data (top to bottom):**
1. Application creates data (Layer 7)
2. Each layer adds its header (encapsulation)
3. Physical layer transmits bits (Layer 1)

**Receiving data (bottom to top):**
1. Physical layer receives bits (Layer 1)
2. Each layer removes its header (decapsulation)
3. Application receives data (Layer 7)

**Example: Sending email**
```
Layer 7: Email application (SMTP)
Layer 6: Encrypt with TLS
Layer 5: Establish session
Layer 4: TCP segments with port 587
Layer 3: IP packets with source/destination IPs
Layer 2: Ethernet frames with MAC addresses
Layer 1: Electrical signals on cable
```

### OSI vs TCP/IP Model

**OSI (7 layers)** - Theoretical model
**TCP/IP (4 layers)** - Practical implementation

| OSI Layer | TCP/IP Layer |
|-----------|--------------|
| Application | Application |
| Presentation | Application |
| Session | Application |
| Transport | Transport |
| Network | Internet |
| Data Link | Network Access |
| Physical | Network Access |

**TCP/IP is what's actually used** - OSI is for understanding.

### Why OSI Matters for AWS

**Security Groups (Layer 3-4):**
- Work at Network and Transport layers
- Filter based on IP addresses and TCP/UDP ports
- Don't see application layer data

**Load Balancers:**
- **Network Load Balancer (NLB)** - Layer 4 (TCP/UDP)
- **Application Load Balancer (ALB)** - Layer 7 (HTTP/HTTPS)
- **Classic Load Balancer (CLB)** - Layer 4 and 7

**Troubleshooting:**
- Layer 1: Cable unplugged?
- Layer 2: MAC address issue?
- Layer 3: IP routing problem?
- Layer 4: Port blocked?
- Layer 7: Application error?

**Example troubleshooting:**
- Can't access website → Check each layer:
  - Physical: Network cable connected?
  - Data Link: Network interface up?
  - Network: Can ping IP address?
  - Transport: Is port 443 open?
  - Application: Is web server running?

---

## Protocol Layers Summary

| Aspect | TCP | UDP | ICMP |
|--------|-----|-----|------|
| **Connection** | Connection-oriented | Connectionless | Connectionless |
| **Reliability** | Reliable | Unreliable | N/A |
| **Speed** | Slower | Faster | Fast |
| **Order** | Ordered | Unordered | N/A |
| **Use case** | Web, email, files | Streaming, gaming | Diagnostics |
| **Overhead** | High | Low | Low |

---

## Why These Matter for AWS

**Security Groups:**
- Need to specify protocol (TCP/UDP/ICMP)
- Need to specify ports
- Need to understand inbound/outbound traffic

**VPC:**
- Need to understand IP addressing and CIDR
- Need to understand routing and traffic flow

**Load Balancers:**
- Work at different layers (TCP vs HTTP)
- Need to understand ports and protocols

**Network Troubleshooting:**
- Use ping (ICMP) to test connectivity
- Use traceroute to find network path
- Understand port blocking issues
