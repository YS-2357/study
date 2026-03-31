# Security Group

## 1. Definition
A security group acts as a virtual firewall to control inbound and outbound traffic to AWS resources.

## 2. Category / Where It Fits
Which part of AWS it belongs to:
- Security

## 3. When To Use It
- When controlling which traffic can reach EC2, RDS, and similar resources
- When applying network-level access rules

## 4. What It Does
- Allows or restricts traffic based on protocol, port, and source
- Protects resources at the instance or service level

## 5. What AWS Manages vs What You Manage
### AWS Manages
- The enforcement mechanism in the AWS network
### You Manage
- The actual inbound and outbound rules

## 6. Console Creation Considerations
- Allow only the specific ports and sources the service actually needs.
- Decide whether inbound and outbound rules should be restricted.
- Use security-group-to-security-group references when possible instead of broad IP ranges.
- A single overly open rule can create a major security problem.

## 7. Cost Shape
- No direct charge for security groups
- Indirect cost comes from mistakes that expose systems or require rework

## 8. Availability / Downtime Notes
- Rule changes take effect quickly
- Incorrect changes can immediately block legitimate traffic

## 9. Similar Services and Differences
- Commonly confused with Network ACLs
- Security Groups apply to resources and are stateful; NACLs apply to subnets

## 10. Related Services
- Amazon EC2
- Amazon RDS
- Amazon VPC

## 11. Simple Example
- Allow HTTPS traffic to a web server and block everything else from the internet

## 12. Common Mistakes
- Opening ports to `0.0.0.0/0` too broadly
- Forgetting outbound rules

## 13. One-Line Summary
- A Security Group controls network access to AWS resources.

## 14. Official AWS Docs
- https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html
