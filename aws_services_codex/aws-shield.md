# AWS Shield

## 1. Definition
AWS Shield is a managed service that helps protect AWS resources against DDoS attacks.

## 2. Category / Where It Fits
Which part of AWS it belongs to:
- Security

## 3. When To Use It
- When protecting internet-facing applications from denial-of-service attacks
- When using services like CloudFront, Route 53, or load balancers

## 4. What It Does
- Detects and mitigates DDoS attacks
- Helps keep public services available during attack traffic
- Includes Shield Standard automatically, with optional higher protection through Shield Advanced

## 5. What AWS Manages vs What You Manage
### AWS Manages
- The DDoS protection mechanisms and mitigation platform
### You Manage
- Which resources to protect and how to combine Shield with broader security controls

## 6. Console Creation Considerations
- Check whether Shield Standard is already enough or whether Shield Advanced is justified.
- Identify which public resources actually need DDoS protection.
- Use it together with CloudFront, Route 53, or load balancers where appropriate.
- Shield does not replace WAF rules or secure application design.

## 7. Cost Shape
- Shield Standard protections are included automatically at no extra charge
- Advanced features add extra cost

## 8. Availability / Downtime Notes
- Helps reduce outage risk from DDoS attacks
- It does not replace secure application design

## 9. Similar Services and Differences
- Commonly confused with AWS WAF
- Shield focuses on DDoS protection; WAF filters application-layer web requests

## 10. Related Services
- AWS WAF
- Amazon CloudFront
- Elastic Load Balancing

## 11. Simple Example
- Protect a public website behind CloudFront from large-scale attack traffic

## 12. Common Mistakes
- Assuming Shield alone solves all web security problems
- Not pairing it with WAF and good architecture

## 13. One-Line Summary
- AWS Shield protects public AWS applications from DDoS attacks.

## 14. Official AWS Docs
- https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html
