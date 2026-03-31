# networking
Networking study notes organized by topic.

- `README.md`: Overview of the `networking/` folder and its direct contents.
- `00_overview.md`: Overview, study order, and cross-references into AWS and computing.
- `01_protocols.md`: Core network protocols such as TCP, UDP, ICMP, HTTP, HTTPS, TLS, and SSH.
- `02_addressing.md`: Ports, IPv4, IPv6, CIDR, MAC addresses, and traffic direction.
- `03_osi_model.md`: OSI model, encapsulation, header/payload, and AWS layer mapping.
- `04_dns.md`: DNS resolution flow, record types, caching, and Route 53/VPC DNS behavior.
- `05_http.md`: HTTP methods, status codes, REST API patterns, and common AWS 5xx scenarios.

## Organizing rules

- This subtree is canonicalized in the Kiro style: broad, practical, and AWS-connected.
- Source-based parallel folders are not kept here. Reusable Codex content has been merged into the canonical topic notes where it improved clarity.
- Add new notes only when they represent a durable topic that does not fit one of the existing files.

## Recommended study order

1. `00_overview.md`
2. `01_protocols.md`
3. `02_addressing.md`
4. `05_http.md`
5. `04_dns.md`
6. `03_osi_model.md`
