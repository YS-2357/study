# OSI 7 Layers

## What Is the OSI Model?

OSI stands for Open Systems Interconnection.

It is a conceptual model that explains network communication using 7 layers.

Each layer has its own responsibility. Together, the layers describe how data moves from an application on one system to an application on another system.

## Why Study It?

The OSI model helps you:
- break networking into smaller parts
- understand where protocols belong
- troubleshoot problems more systematically

For Amazon Web Services (AWS) beginners, OSI is useful because many AWS networking services are easier to understand when you know which layer they relate to.

## Quick Mental Model

Before going into each layer, it helps to keep a simple overall picture in mind.

- `Layer 7 - Application`
  - delivers the user or application intent
  - example: request a web page, send email, look up a domain name

- `Layer 6 - Presentation`
  - decides how the data should look so both sides can use it correctly and safely
  - example: formatting, encoding, encryption, compression

- `Layer 5 - Session`
  - maintains the ongoing conversation context
  - example: whose interaction this is, whether it is still active, and what is being remembered in that interaction

- `Layer 4 - Transport`
  - delivers data to the right service or process on the destination host
  - example: ports, Transmission Control Protocol (TCP), User Datagram Protocol (UDP), reliability, ordering

- `Layer 3 - Network`
  - decides where the packet should go across networks
  - example: Internet Protocol (IP) addresses and routing

- `Layer 2 - Data Link`
  - handles local link delivery between nearby nodes
  - example: frames, Ethernet, Media Access Control (MAC) addresses

- `Layer 1 - Physical`
  - carries the raw signal through the physical medium
  - example: cable, fiber, radio signal

One useful way to read the stack is:
- Layer 7 = what the user wants
- Layer 6 = how the data should look
- Layer 5 = how the conversation continues
- Layer 4 = which service should receive it
- Layer 3 = which machine or network it should reach
- Layer 2 = how it moves on the local link
- Layer 1 = how the signal physically moves

## The 7 Layers

### Layer 7 - Application

This is the layer closest to the user and the application.

It provides network services to software such as web browsers, email clients, and API clients.

**Common examples:**
- Hypertext Transfer Protocol (HTTP)
- Hypertext Transfer Protocol Secure (HTTPS)
- Domain Name System (DNS)
- Dynamic Host Configuration Protocol (DHCP)
- Simple Mail Transfer Protocol (SMTP)
- Secure Shell (SSH)

**How to read some Layer 7 protocol names:**

- `Hypertext Transfer Protocol (HTTP)`
  - `Hypertext`: text connected by links, which was the original idea of the web
  - `Transfer`: moving that content between systems
  - `Protocol`: the agreed rules for how that transfer happens
  - meaning: the rules for transferring linked web content

- `Hypertext Transfer Protocol Secure (HTTPS)`
  - `Hypertext Transfer Protocol`: the normal web communication rules
  - `Secure`: protected communication, usually through Transport Layer Security (TLS)
  - meaning: HTTP with security added

- `Domain Name System (DNS)`
  - `Domain Name`: a human-friendly name such as `example.com`
  - `System`: the overall naming and lookup system
  - meaning: the system that maps names to network addresses

- `Dynamic Host Configuration Protocol (DHCP)`
  - `Dynamic`: assigned automatically when needed
  - `Host Configuration`: network settings for a device
  - `Protocol`: the communication rules
  - meaning: the rules for automatically giving a device network settings such as an IP address, gateway, and DNS server

- `Simple Mail Transfer Protocol (SMTP)`
  - `Simple`: originally named to emphasize a straightforward mail-sending method
  - `Mail`: email messages
  - `Transfer`: sending the message onward
  - `Protocol`: the communication rules
  - meaning: the rules for sending email between systems

- `Secure Shell (SSH)`
  - `Secure`: protected communication
  - `Shell`: command-line access to another system
  - meaning: a secure way to log in and run commands remotely

**Think of it as:**
The part where the application says, "I want to request a web page" or "I want to send an email."

**Typical problem at this layer:**
- wrong URL path
- bad HTTP response
- DNS name issue
- DHCP configuration issue
- API request format issue

**AWS connection:**
- Application Load Balancer (ALB)
- API Gateway
- Amazon CloudFront for HTTP/HTTPS traffic

---

### Layer 6 - Presentation

This layer is responsible for how data is represented.

It handles tasks such as:
- encryption
- decryption
- formatting
- compression

**Common examples:**
- Transport Layer Security (TLS) / Secure Sockets Layer (SSL)
- American Standard Code for Information Interchange (ASCII)
- JPEG

**What TLS/SSL means:**
- `Transport Layer Security (TLS)` is the modern security protocol used to protect data sent over a network
- `Secure Sockets Layer (SSL)` is the older name and older technology that came before TLS
- in practice, people still say "SSL" casually, but modern systems usually use TLS

**What TLS does:**
- encrypts data so others cannot easily read it
- helps verify that you are talking to the real server through certificates
- helps protect data integrity so the content is not changed in transit

**Simple example:**
When you open an `https://` website, HTTP works together with TLS.

That means:
- HTTP defines the web request/response rules
- TLS protects that communication

So HTTPS means:
- Hypertext Transfer Protocol Secure
- or more practically, HTTP running over TLS

**Think of it as:**
Making sure the data is in the right format and can be understood on both sides.

**Typical problem at this layer:**
- TLS certificate issue
- encryption/decryption mismatch
- unsupported data format

**AWS connection:**
- TLS termination on an ALB
- HTTPS certificate handling

---

### Layer 5 - Session

This layer manages sessions between systems.

It is responsible for starting, maintaining, and ending communication sessions.

A session means an ongoing communication context between two sides.

It is not just "data is being sent." It is the idea that both sides are participating in the same conversation over time.

This layer is concerned with questions such as:
- when does the conversation start?
- how long does it stay active?
- how is state kept while the conversation continues?
- how does the conversation end or recover?

**Common examples:**
- Remote Procedure Call (RPC)-style sessions
- database sessions
- long-lived application connections

**Think of it as:**
Keeping a conversation open between two systems.

Another way to imagine it:
- Layer 4 helps data move between two hosts
- Layer 5 helps treat multiple exchanges as one continuing conversation

For example, if two systems exchange messages over time, Layer 5 thinking asks:
- are they still in the same session?
- did the session timeout?
- can the session resume?
- does the server still recognize this interaction?

**Simple example:**
Imagine you log in to a service and keep interacting with it for a while.

Even if many requests and responses happen, the system may still treat them as part of one ongoing interaction. That "ongoing conversation context" is the easiest way to think about a session.

**Simple way to picture a session:**
- `status`: is this session still active?
- `who`: whose session is this?
- `state`: what is remembered in this session?

So a session is not only on/off status.

It usually includes:
- whether the interaction is still valid
- which user or client it belongs to
- some remembered context tied to that interaction

**Typical problem at this layer:**
- session timeout
- dropped persistent connection
- session state issue
- reconnect behavior problem

**AWS connection:**
- session persistence behavior
- long-lived application or database connections

In practice, Layer 5 is harder to see directly than Layer 3, 4, or 7.

That is because real systems often blend session behavior into applications, frameworks, databases, or secure connections instead of exposing it as a clearly separate layer.

Still, the Layer 5 idea is useful because it helps explain problems where:
- the network path is fine
- the port is open
- the application exists
- but the conversation state is lost, expired, or inconsistent

---

## How Application, Presentation, and Session Are Different

These three layers are often hard to picture because in real systems they are closely connected.

A simple way to separate them is to ask three different questions:

- `Application`: what does the user or program want to do?
- `Presentation`: in what format should the data be shown, encoded, or protected?
- `Session`: how is the conversation kept open and managed?

### Simple analogy: a video call

- `Application`
  - the activity itself
  - for example: video call, chat, or file sharing

- `Presentation`
  - how the information is represented so both sides can understand it
  - if needed, how it is encrypted or formatted

- `Session`
  - how the conversation is started, maintained, and ended
  - who is connected and whether the communication is still active

### Web example

- `Application`
  - Hypertext Transfer Protocol (HTTP) says what the request means
  - example: "give me this web page"

- `Presentation`
  - Transport Layer Security (TLS) protects the communication
  - encoding and formatting also fit here

- `Session`
  - keeps the communication context alive while the systems continue talking

### Practical shortcut

- Application = what you want
- Presentation = how the data looks or is protected
- Session = how the conversation is maintained

This separation is easier to understand in the OSI model than in real systems, because real networking stacks often combine these responsibilities more tightly.

### Slightly more precise shortcut

If you want a simple but less misleading summary:

- `Layer 7 - Application`
  - carries the user or program intent
  - example: request a web page, send email, look up a domain name

- `Layer 6 - Presentation`
  - prepares the data so both sides can use it safely and correctly
  - example: encryption, encoding, formatting, compression

- `Layer 5 - Session`
  - keeps the interaction as one ongoing conversation over time
  - example: start, maintain, resume, or end the communication context

One important correction:
- `Layer 5` is not simply "connect the server"
- the actual transport connection is closer to `Layer 4`
- `Layer 5` is more about conversation continuity than basic connectivity

---

### Layer 4 - Transport

This layer provides end-to-end communication between systems.

It handles:
- segmentation
- reliability
- flow control
- ports

**Common examples:**
- Transmission Control Protocol (TCP)
- User Datagram Protocol (UDP)

**Quick note:**
In TCP, `SYN` means "start and synchronize" and `ACK` means "I received it." A `handshake` is the short exchange used to begin a reliable connection.

**Think of it as:**
How data is delivered between two hosts, and whether that delivery is reliable or fast.

**Important idea:**
Ports belong here. Examples include `80`, `443`, and `22`.

**Typical problem at this layer:**
- blocked port
- TCP connection failure
- UDP packet loss

**AWS connection:**
- Network Load Balancer (NLB)
- Security Group rules for TCP/UDP ports

---

### Layer 3 - Network

This layer is responsible for logical addressing and routing.

It decides how packets move between networks.

**Common examples:**
- Internet Protocol (IP)
- Internet Control Message Protocol (ICMP)

**Think of it as:**
Finding the path from one system to another using IP addresses.

**Important idea:**
IP addresses belong here.

**Typical problem at this layer:**
- wrong IP route
- no route to destination
- unreachable network

**AWS connection:**
- Amazon Virtual Private Cloud (VPC)
- Subnet routing
- Route tables
- Internet Gateway
- NAT Gateway

---

### Layer 2 - Data Link

This layer handles communication between directly connected nodes on the same local network segment.

It uses frames and physical addresses.

**Common examples:**
- Ethernet
- Media Access Control (MAC) addresses

**Think of it as:**
Local delivery on the current network.

**Important idea:**
MAC addresses belong here.

**Typical problem at this layer:**
- local network interface issue
- frame delivery issue

**AWS connection:**
- Elastic Network Interface (ENI)
- underlying virtual network behavior inside AWS

---

### Layer 1 - Physical

This is the lowest layer.

It is responsible for transmitting raw bits over a physical medium.

**Common examples:**
- cable
- fiber
- radio signal

**Think of it as:**
The actual movement of electrical, optical, or radio signals.

**Typical problem at this layer:**
- cable failure
- signal issue
- hardware transmission problem

**AWS connection:**
- AWS data center hardware
- AWS Direct Connect physical infrastructure

---

## How Data Moves Through the Layers

When sending data, it moves from Layer 7 down to Layer 1.

Example: opening a web page over HTTPS (Hypertext Transfer Protocol Secure)

1. Layer 7: the browser makes an HTTPS request
2. Layer 6: TLS encrypts the data
3. Layer 5: the session is maintained
4. Layer 4: TCP uses port 443
5. Layer 3: IP adds source and destination addresses
6. Layer 2: the frame uses local network addressing
7. Layer 1: bits are transmitted through the medium

When receiving data, the process goes in reverse from Layer 1 back to Layer 7.

## OSI vs Real Networking

OSI is mainly for understanding concepts.

Real networks are usually described using the TCP/IP model, which is simpler.

Still, OSI remains useful because it helps answer questions like:
- Is this a DNS (Domain Name System) problem?
- Is the port blocked?
- Is the route wrong?
- Is TLS (Transport Layer Security) failing?
- Is the application itself broken?

## Study Tip

When you see a protocol name, do not try to memorize it as one block.

Break it into words and ask:
- What does this word describe?
- Is it about data, delivery, security, or routing?
- What promise does this protocol make?

That makes protocol names much easier to understand and remember.

## Memory Aid

Top to bottom:

**A P S T N D P**

- Application
- Presentation
- Session
- Transport
- Network
- Data Link
- Physical

One common phrase:

**All People Seem To Need Data Processing**

## What to Remember Most

If you forget everything else, keep these three anchors:
- Layer 7 = application protocols like HTTP and DNS
- Layer 4 = TCP/UDP and ports
- Layer 3 = IP and routing

For AWS beginners, these are the most practical starting points.

## Why Layers 7, 4, and 3 Are So Important Practically

Most everyday cloud and networking problems can be narrowed down by checking these three layers first.

### Layer 7 - Is the request itself correct?

This layer is important because application behavior lives here.

Examples:
- Hypertext Transfer Protocol (HTTP) and Hypertext Transfer Protocol Secure (HTTPS)
- Domain Name System (DNS) names
- URL paths
- headers
- API requests

In AWS, this often connects to:
- Application Load Balancer routing
- API Gateway behavior
- Amazon CloudFront behavior

If traffic reaches the service but the result is still wrong, the problem is often at Layer 7.

### Layer 4 - Can the connection open?

This layer is important because transport rules live here.

Examples:
- Transmission Control Protocol (TCP) vs User Datagram Protocol (UDP)
- port `80`
- port `443`
- port `22`

In AWS, this often connects to:
- Security Group port rules
- Network Load Balancer behavior

If two systems cannot establish a connection, Layer 4 is one of the first places to check.

### Layer 3 - Can packets reach the destination?

This layer is important because network path logic lives here.

Examples:
- Internet Protocol (IP) addresses
- subnets
- route tables
- Internet Gateway
- NAT Gateway

In AWS, this often connects to:
- Amazon Virtual Private Cloud (VPC) design
- subnet routing
- public/private network path decisions

If the route is wrong or there is no path between networks, the problem is at Layer 3.

## Practical Shortcut

When troubleshooting, ask in this order:

1. Layer 3: is there a valid network path?
2. Layer 4: is the required port/protocol allowed?
3. Layer 7: is the application request or response correct?

This shortcut is one of the most useful reasons to study OSI in the first place.
