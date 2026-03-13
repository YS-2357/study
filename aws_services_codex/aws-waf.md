# AWS WAF

## 1. Definition
AWS WAF is a web application firewall that lets you monitor and control HTTP(S) requests to protected web applications.

## 2. Category / Where It Fits
Which part of AWS it belongs to:
- Security

## 3. When To Use It
- When protecting web apps and APIs from malicious requests
- When blocking patterns like SQL injection or abusive bots

## 4. What It Does
- Filters web traffic using rules
- Allows, blocks, or counts requests based on conditions
- Protects resources such as CloudFront, API Gateway, and Application Load Balancer

## 5. What AWS Manages vs What You Manage
### AWS Manages
- The WAF platform and managed rule capabilities
### You Manage
- Rules, associations, tuning, and false-positive handling

## 6. Console Creation Considerations
- Decide which resource to associate with the web ACL, such as CloudFront or ALB.
- Choose managed rules, custom rules, or both.
- Test rules carefully to avoid blocking normal traffic.
- More rules and more traffic can increase both complexity and cost.

## 7. Cost Shape
- Charged by web ACLs, rules, and request volume
- More traffic and more rules increase cost

## 8. Availability / Downtime Notes
- Helps keep apps available by filtering bad requests
- Bad rules can block valid traffic

## 9. Similar Services and Differences
- Commonly confused with AWS Shield
- WAF filters application requests; Shield focuses on DDoS protection

## 10. Related Services
- Amazon CloudFront
- Application Load Balancer
- AWS Shield

## 11. Simple Example
- Block suspicious traffic patterns before requests reach a web application

## 12. Common Mistakes
- Enabling strict rules without testing
- Ignoring false positives

## 13. One-Line Summary
- AWS WAF filters web requests to protect applications and APIs.

## 14. Official AWS Docs
- https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html
