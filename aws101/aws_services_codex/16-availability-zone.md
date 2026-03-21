# Availability Zone

## 1. Definition
An Availability Zone is an isolated location within an AWS Region.

## 2. Category / Where It Fits
Which part of AWS it belongs to:
- Networking

## 3. When To Use It
- When designing high availability inside one region
- When placing resources to avoid a single point of failure

## 4. What It Does
- Separates infrastructure within a region
- Lets services run across multiple isolated locations

## 5. What AWS Manages vs What You Manage
### AWS Manages
- The physical facilities and isolation between AZs
### You Manage
- Which AZs to use and whether to spread workloads across them

## 6. Console Creation Considerations
- Decide whether resources should be spread across multiple AZs for high availability.
- Make sure subnets are created in the AZs you plan to use.
- Remember some resources are tied to one AZ.
- Using more than one AZ can improve resilience but may add network cost.

## 7. Cost Shape
- No direct charge for choosing an AZ
- Cross-AZ traffic can increase network cost

## 8. Availability / Downtime Notes
- Multi-AZ designs reduce downtime risk
- Single-AZ designs are more likely to be interrupted by local failures

## 9. Similar Services and Differences
- Commonly confused with Region
- AZ is one isolated location inside a region, not a separate geography

## 10. Related Services
- Region
- Subnet
- Amazon RDS

## 11. Simple Example
- Run web servers in two AZs so one AZ failure does not stop the app

## 12. Common Mistakes
- Putting all resources in one AZ
- Ignoring cross-AZ traffic cost

## 13. One-Line Summary
- An Availability Zone is an isolated location inside a region for higher availability.

## 14. Official AWS Docs
- https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions-availability-zones.html
