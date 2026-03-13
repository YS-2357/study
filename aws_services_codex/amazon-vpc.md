# Amazon VPC

## 1. Definition
Amazon VPC is a logically isolated virtual network in AWS.

## 2. Category / Where It Fits
Which part of AWS it belongs to:
- Networking

## 3. When To Use It
- When you need network isolation and control
- When running applications that require custom IP, routing, and security setup

## 4. What It Does
- Creates a private AWS network for your resources
- Lets you define subnets, route tables, and gateways

## 5. What AWS Manages vs What You Manage
### AWS Manages
- The underlying network platform
### You Manage
- IP ranges, subnets, routing, and security design

## 6. Console Creation Considerations
- Choose a CIDR block large enough for future subnet expansion.
- Decide whether you need IPv6 before creating the VPC.
- Plan public and private subnet structure before adding resources.
- Poor VPC design is hard to fix later without migration work.

## 7. Cost Shape
- A VPC itself is generally free
- Cost usually comes from NAT Gateway, traffic, endpoints, and attached resources

## 8. Availability / Downtime Notes
- Network changes can affect connectivity immediately
- Careful design reduces downtime during expansion

## 9. Similar Services and Differences
- Commonly confused with subnet
- VPC is the whole private network; subnets are pieces inside it

## 10. Related Services
- Subnet
- Security Group
- Internet Gateway

## 11. Simple Example
- Build one VPC for an app with public web subnets and private database subnets

## 12. Common Mistakes
- Poor CIDR planning
- Overusing public subnets

## 13. One-Line Summary
- Amazon VPC gives you a private, customizable network in AWS.

## 14. Official AWS Docs
- https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html
