# Protocols

## Core Network Protocols

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

**Port:** 22 (TCP)

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
- Server administration (AWS EC2 Linux instances)
- Git operations (GitHub, GitLab)
- File transfers
- Remote development

**Authentication methods:**
- **Password** - Username + password (less secure)
- **Key-based** - Public/private key pair (more secure, recommended)

**AWS EC2 usage:**
- Linux instances use SSH for remote access
- Requires key pair (.pem file) downloaded at instance creation
- Security group must allow port 22 from your IP
- Default usernames: ec2-user (Amazon Linux), ubuntu (Ubuntu), admin (Debian)

**Analogy:** Like having a secure phone line to control a remote computer.

---

### RDP (Remote Desktop Protocol)
**Definition:** Protocol for remote graphical access to Windows computers.

**Port:** 3389 (TCP)

**History:**
- Created by Microsoft in 1996
- Built into Windows operating systems
- Current version: RDP 10+

**How it works:**
- Client connects to server on port 3389
- Authentication (username + password)
- Encrypted connection established
- Full graphical desktop transmitted

**What it does:**
- **Remote desktop** - See and control Windows desktop remotely
- **Clipboard sharing** - Copy/paste between local and remote
- **File transfer** - Drag and drop files
- **Printer redirection** - Use local printers on remote machine
- **Audio redirection** - Hear remote computer's audio

**Use cases:**
- Windows server administration (AWS EC2 Windows instances)
- Remote work (access office computer from home)
- Technical support (help users remotely)
- Application access (run Windows apps remotely)

**Authentication:**
- Username + password (required)
- Network Level Authentication (NLA) for extra security

**AWS EC2 usage:**
- Windows instances use RDP for remote access
- Requires key pair to decrypt administrator password
- Security group must allow port 3389 from your IP
- Get password: EC2 Console → Connect → RDP client → Get Password (upload .pem file)

**RDP clients:**
- **Windows:** Built-in (Remote Desktop Connection - mstsc.exe)
- **macOS:** Microsoft Remote Desktop (App Store)
- **Linux:** Remmina, Vinagre, xfreerdp

**Security considerations:**
- **Never allow 0.0.0.0/0 on port 3389** - Common brute force target
- Use strong passwords (AWS generates random 20+ character passwords)
- Enable Network Level Authentication (NLA)
- Use VPN or bastion host for production access
- Consider AWS Session Manager instead (no open ports needed)

**Analogy:** Like having a remote control for a Windows computer - you see and control everything as if sitting in front of it.

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

## Protocol Comparison

| Aspect | TCP | UDP | ICMP |
|--------|-----|-----|------|
| **Connection** | Connection-oriented | Connectionless | Connectionless |
| **Reliability** | Reliable | Unreliable | N/A |
| **Speed** | Slower | Faster | Fast |
| **Order** | Ordered | Unordered | N/A |
| **Use case** | Web, email, files | Streaming, gaming | Diagnostics |
| **Overhead** | High | Low | Low |

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
