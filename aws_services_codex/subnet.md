# Subnet

## 1. Definition
A subnet is a range of IP addresses inside a VPC.

## 2. Category / Where It Fits
Which part of AWS it belongs to:
- Networking

## 3. When To Use It
- When dividing a VPC into smaller network segments
- When separating public and private resources

## 4. What It Does
- Assigns IP ranges to groups of resources
- Controls where resources are placed within an Availability Zone

## 5. What AWS Manages vs What You Manage
### AWS Manages
- Basic subnet capability inside VPC
### You Manage
- CIDR ranges, routing, and whether a subnet is public or private

## 6. Console Creation Considerations
- Choose a CIDR range that leaves room for future growth.
- Decide early whether the subnet is public or private.
- Place the subnet in the correct Availability Zone.
- Avoid overlapping CIDR ranges with other subnets or VPCs.

## 7. Cost Shape
- No direct charge for creating a subnet
- Costs come from resources and traffic using the subnet

## 8. Availability / Downtime Notes
- Changing network design can interrupt connectivity
- Good subnet design helps avoid rework later

## 9. Similar Services and Differences
- Commonly confused with VPC
- VPC is the full private network; a subnet is one segment inside it

## 10. Related Services
- Amazon VPC
- Route Table
- Security Group

## 11. Simple Example
- Put a web server in a public subnet and a database in a private subnet

## 12. Common Mistakes
- Overlapping CIDR ranges
- Putting sensitive resources in public subnets

## 13. One-Line Summary
- A subnet is a network segment inside a VPC.

## 14. Official AWS Docs
- https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html
