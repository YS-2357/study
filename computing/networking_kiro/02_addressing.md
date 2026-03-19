# Addressing

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
  - 3389: RDP (Windows Remote Desktop)
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

## IP Addressing

### IPv4 Address
**Definition:** 32-bit address for identifying devices on a network.

**IP = Internet Protocol** - The protocol that routes data across networks.

**Format:** Four numbers (0-255) separated by dots
- Example: 192.168.1.1
- Total: ~4.3 billion addresses (2^32)

**History:**
- Emerged in 1981 (RFC 791)
- Designed for early internet (ARPANET)
- Running out of addresses globally

**Types:**
- **Public IP** - Routable on internet (e.g., 54.123.45.67)
- **Private IP** - Only within private network (e.g., 10.0.1.5)

**Private IP Ranges (RFC 1918):**
- **10.0.0.0/8** - 10.0.0.0 to 10.255.255.255 (16 million IPs)
- **172.16.0.0/12** - 172.16.0.0 to 172.31.255.255 (1 million IPs)
- **192.168.0.0/16** - 192.168.0.0 to 192.168.255.255 (65,536 IPs)

**Special addresses:**
- **0.0.0.0** - Default route / any address
- **127.0.0.1** - Localhost (loopback)
- **255.255.255.255** - Broadcast address

---

### IPv6 Address
**Definition:** 128-bit address for identifying devices, successor to IPv4.

**IPv6 = Internet Protocol version 6** - Newer version of IP.

**Format:** Eight groups of hexadecimal separated by colons
- Example: 2001:0db8:85a3:0000:0000:8a2e:0370:7334
- Shortened: 2001:db8:85a3::8a2e:370:7334 (omit leading zeros and consecutive zeros)
- Total: 340 undecillion addresses (2^128)

**History:**
- Emerged in 1998 (RFC 2460)
- Created to solve IPv4 address exhaustion
- Slow adoption, but increasing

**Characteristics:**
- Massive address space (enough for every grain of sand on Earth)
- No need for NAT
- Built-in IPsec support
- Simplified header format

**Why adoption is slow:**
- Requires infrastructure upgrades
- Not backward compatible with IPv4
- Dual-stack (running both) is complex
- IPv4 + NAT "works" for now

---

## CIDR (Classless Inter-Domain Routing)

### What is CIDR?
**Definition:** Notation for specifying IP address ranges.

**Format:** `IP address/prefix length` (e.g., 10.0.0.0/16)

**History:**
- Introduced in 1993 (RFC 1519)
- Replaced classful networking (Class A, B, C)
- More flexible IP allocation

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

### CIDR Calculation

**Formula:** Number of IPs = 2^(32 - prefix)

- /32: 2^0 = 1 IP
- /24: 2^8 = 256 IPs
- /16: 2^16 = 65,536 IPs
- /8: 2^24 = 16,777,216 IPs

### Common AWS CIDR Usage
- **VPC:** 10.0.0.0/16 (65,536 IPs)
- **Subnet:** 10.0.1.0/24 (256 IPs, but AWS reserves 5 = 251 usable)
- **Single IP:** 1.2.3.4/32 (for security group rules)

### AWS Reserved IPs in Subnets
**AWS reserves the first 4 IPs and last 1 IP in every subnet.**

For subnet 10.0.1.0/24, AWS reserves:
- **10.0.1.0** - Network address (first IP)
- **10.0.1.1** - VPC router (second IP)
- **10.0.1.2** - DNS server (third IP)
- **10.0.1.3** - Future use (fourth IP)
- **10.0.1.255** - Broadcast address (last IP)

**Usable IPs:** 256 - 5 = 251

---

## MAC Address

### What is MAC Address?
**Definition:** Media Access Control address - physical address of network interface.

**Format:** 48-bit identifier, usually written as six groups of two hexadecimal digits
- Example: 00:1A:2B:3C:4D:5E
- Also written as: 00-1A-2B-3C-4D-5E

**Characteristics:**
- Unique per network card (burned into hardware)
- Works at Layer 2 (Data Link)
- Used for local network communication
- First 3 bytes = manufacturer ID (OUI)
- Last 3 bytes = device ID

**Use cases:**
- Ethernet and Wi-Fi communication
- ARP (Address Resolution Protocol) - maps IP to MAC
- Switch forwarding decisions
- Network access control

**In AWS:**
- ENI (Elastic Network Interface) has MAC address
- Persists when ENI is detached/reattached
- Used for licensing (some software licenses tied to MAC)

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

## ENI (Elastic Network Interface)

### What is ENI?
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
- Dual-homed instances (multiple subnets)

**Characteristics:**
- Bound to specific Availability Zone
- Can be moved between instances in same AZ
- MAC address persists
- Security groups attached to ENI, not instance

**Analogy:** Like a physical network card (NIC), but virtual and flexible.

---

## Prefix List

### What is Prefix List?
**Definition:** Managed list of CIDR blocks.

**Purpose:**
- AWS maintains lists of service IP ranges
- S3, CloudFront, EC2, etc.
- Automatically updated by AWS

**Types:**
- **AWS-managed** - Maintained by AWS (S3, CloudFront, etc.)
- **Customer-managed** - You create and maintain

**Use in Security Groups:**
- Reference AWS service IPs without manual updates
- Example: Allow outbound to S3 prefix list
- Easier than maintaining CIDR blocks manually

**Example:**
- Instead of: Allow 52.92.0.0/20, 54.231.0.0/16, ... (S3 IPs)
- Use: Allow pl-63a5400a (S3 prefix list)

**Benefits:**
- AWS updates automatically when IPs change
- Cleaner security group rules
- Reduces rule count
