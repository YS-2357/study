# DNS (Domain Name System)

## What is DNS?
**Definition:** Distributed system that translates human-readable domain names to IP addresses.

**Example:** example.com ↔ 93.184.216.34

**Analogy:** Like a phone book for the internet - converts names to numbers.

**History:**
- Created in 1983 by Paul Mockapetris
- Replaced HOSTS.TXT file (manual list)
- Hierarchical, distributed database

---

## How DNS Works

### DNS Resolution Process

**Example: Looking up example.com**

1. **You type:** example.com in browser
2. **Browser checks cache:** Do I already know the IP?
3. **If not cached, asks DNS resolver** (like 8.8.8.8 or your ISP's DNS)
4. **Resolver checks its cache:** Do I know it?
5. **If not, resolver queries hierarchy:**
   - **Root servers:** "Who handles .com?"
   - **TLD servers (.com):** "Who handles example.com?"
   - **Authoritative nameservers:** "example.com is 93.184.216.34"
6. **Resolver returns answer** to browser
7. **Resolver caches answer** for future requests
8. **Browser connects** to 93.184.216.34

### Visual Flow
```
Browser → Resolver → Root → TLD → Authoritative → Answer
   ↑                                                  ↓
   └──────────────── 93.184.216.34 ─────────────────┘
```

---

## DNS Hierarchy

### The Distributed Database

**Root DNS Servers (13 worldwide)**
- Top of DNS hierarchy
- Know where to find TLD servers
- Operated by different organizations
- Named a.root-servers.net through m.root-servers.net

**TLD (Top Level Domain) Servers**
- Handle .com, .org, .net, .edu, country codes (.uk, .jp)
- Know where to find authoritative nameservers for domains
- Example: .com TLD servers know where example.com's nameservers are

**Authoritative Nameservers**
- Have the actual IP addresses for domains
- Final source of truth
- Example: example.com's nameservers have the IP 93.184.216.34

**DNS Resolvers (Recursive Resolvers)**
- Do the work of querying hierarchy
- Cache results
- Examples: 8.8.8.8 (Google), 1.1.1.1 (Cloudflare), ISP DNS

### Example Hierarchy
```
                    Root (.)
                       |
        ┌──────────────┼──────────────┐
        |              |              |
      .com           .org           .net
        |              |              |
    example.com    wikipedia.org   archive.net
        |
   93.184.216.34
```

---

## DNS Record Types

### A Record (Address)
- Maps domain name to IPv4 address
- Example: example.com → 93.184.216.34
- Most common record type

### AAAA Record (IPv6 Address)
- Maps domain name to IPv6 address
- Example: example.com → 2606:2800:220:1:248:1893:25c8:1946

### CNAME Record (Canonical Name)
- Alias from one domain to another
- Example: www.example.com → example.com
- Cannot be used for root domain

### MX Record (Mail Exchange)
- Specifies mail servers for domain
- Example: example.com → mail.example.com (priority 10)
- Has priority number (lower = higher priority)

### TXT Record (Text)
- Arbitrary text data
- Used for verification, SPF, DKIM
- Example: example.com → "v=spf1 include:_spf.google.com ~all"

### NS Record (Name Server)
- Specifies authoritative nameservers for domain
- Example: example.com → ns1.example.com, ns2.example.com

### SOA Record (Start of Authority)
- Administrative information about zone
- Primary nameserver, email, serial number, timers

---

## DNS Caching

### Why Caching?
- Reduces DNS query load
- Faster responses
- Reduces internet traffic

### TTL (Time To Live)
- How long to cache DNS record (in seconds)
- Set by domain owner
- Examples:
  - 300 (5 minutes) - Frequent changes
  - 3600 (1 hour) - Normal
  - 86400 (24 hours) - Rarely changes

### Cache Levels
1. **Browser cache** - Your browser remembers
2. **OS cache** - Your computer remembers
3. **Resolver cache** - DNS server remembers
4. **ISP cache** - Your ISP remembers

**Problem:** Changing DNS takes time to propagate due to caching.

---

## DNS in AWS

### Route 53
**AWS's DNS service** - Authoritative nameserver

**Features:**
- Domain registration
- DNS hosting (authoritative nameserver)
- Health checks and failover
- Traffic routing policies
- Integration with AWS services

**Routing policies:**
- **Simple** - Single resource
- **Weighted** - Distribute traffic by percentage
- **Latency** - Route to lowest latency region
- **Failover** - Primary/secondary with health checks
- **Geolocation** - Route based on user location
- **Geoproximity** - Route based on resource location
- **Multivalue** - Multiple IPs with health checks

### VPC DNS

**DNS Resolution in VPC:**
- AWS provides DNS server at VPC CIDR +2
- Example: VPC 10.0.0.0/16 → DNS at 10.0.0.2
- Resolves public DNS names and VPC internal names

**VPC DNS Settings:**

**DNS resolution:**
- Enables DNS resolution within VPC
- Usually keep enabled
- Allows instances to resolve domain names

**DNS hostnames:**
- Gives instances DNS names
- Example: ec2-54-123-45-67.compute-1.amazonaws.com → 54.123.45.67
- **Must enable for instances with public IPs to get DNS names**
- Required for many AWS services

**Private Hosted Zones:**
- Internal DNS for VPC
- Example: db.internal.company.com → 10.0.2.5
- Not accessible from internet
- Multiple VPCs can use same hosted zone

---

## DNS Query Types

### Recursive Query
- Resolver does all the work
- Queries hierarchy until it gets answer
- Returns final answer to client
- Most common type

### Iterative Query
- Resolver asks, gets referral, asks next server
- Client does the work of following referrals
- Less common

### Forward Lookup
- Domain name → IP address
- Example: example.com → 93.184.216.34
- Most common

### Reverse Lookup
- IP address → domain name
- Example: 93.184.216.34 → example.com
- Uses PTR records in special domain (in-addr.arpa)

---

## Common DNS Issues

### DNS Propagation Delay
**Problem:** Changed DNS but old IP still showing

**Cause:** Caching at various levels

**Solution:**
- Wait for TTL to expire
- Lower TTL before making changes
- Clear local DNS cache: `ipconfig /flushdns` (Windows) or `sudo dscacheutil -flushcache` (Mac)

### NXDOMAIN (Non-Existent Domain)
**Problem:** Domain doesn't exist

**Cause:** Typo, domain not registered, or DNS not configured

**Solution:** Check domain spelling, verify DNS records

### DNS Timeout
**Problem:** DNS query takes too long or fails

**Cause:** DNS server down, network issue, firewall blocking port 53

**Solution:** Check DNS server, try different resolver (8.8.8.8)

### Split-Horizon DNS
**Problem:** Internal and external users need different IPs for same domain

**Solution:** 
- Public hosted zone for external users
- Private hosted zone for VPC users
- Same domain, different IPs

---

## DNS Security

### DNS Spoofing/Cache Poisoning
**Attack:** Attacker provides fake DNS response

**Protection:** DNSSEC (DNS Security Extensions)

### DDoS on DNS
**Attack:** Overwhelm DNS servers with queries

**Protection:** 
- AWS Shield (automatic)
- Route 53 is highly distributed
- Anycast routing

### DNS Tunneling
**Attack:** Use DNS queries to exfiltrate data or establish C&C

**Protection:** Monitor DNS query patterns, use DNS firewall

---

## DNS Tools

### Command Line Tools

**nslookup** - Query DNS records
```bash
nslookup example.com
nslookup example.com 8.8.8.8  # Use specific DNS server
```

**dig** - Detailed DNS information (Linux/Mac)
```bash
dig example.com
dig example.com A  # Query A record
dig example.com MX  # Query MX record
dig @8.8.8.8 example.com  # Use specific DNS server
```

**host** - Simple DNS lookup
```bash
host example.com
host 93.184.216.34  # Reverse lookup
```

### Online Tools
- DNS Checker - Check DNS propagation worldwide
- MXToolbox - DNS and email diagnostics
- WhatsMyDNS - Global DNS propagation checker

---

## DNS Best Practices

### For AWS
1. **Enable DNS hostnames** in VPC for public instances
2. **Use Route 53** for domain hosting (integrated with AWS)
3. **Set appropriate TTLs** - Lower before changes, higher for stability
4. **Use health checks** with failover routing
5. **Private hosted zones** for internal services
6. **Alias records** for AWS resources (free, better than CNAME)

### General
1. **Use multiple nameservers** (redundancy)
2. **Monitor DNS query patterns** (detect issues early)
3. **Keep DNS records updated** (remove old entries)
4. **Use DNSSEC** for security (if supported)
5. **Document DNS changes** (know what changed when)

---

## DNS Analogy Summary

**DNS is like:**
- **Phone book** - Converts names to numbers
- **Post office** - Routes messages to right address
- **Directory assistance** - Helps you find contact information

**Without DNS:**
- Would need to remember 93.184.216.34 instead of example.com
- Internet would be unusable for humans
- Like having to remember phone numbers for everyone
