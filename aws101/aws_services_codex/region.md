# Region

## 1. Definition
An AWS Region is a separate geographic area where AWS clusters infrastructure and services.

## 2. Category / Where It Fits
Which part of AWS it belongs to:
- Networking

## 3. When To Use It
- When deciding where to place workloads and data
- When latency, compliance, or disaster recovery matters

## 4. What It Does
- Defines the physical location of AWS services
- Separates resources by geography

## 5. What AWS Manages vs What You Manage
### AWS Manages
- The data center infrastructure in each region
### You Manage
- Which region to use and how to design across regions

## 6. Console Creation Considerations
- Choose a region close to users to reduce latency.
- Check whether the region supports the services you plan to use.
- Consider data residency or compliance requirements before choosing.
- Changing region later usually means rebuilding or migrating resources.

## 7. Cost Shape
- No direct charge for choosing a region
- Cost changes because prices and data transfer differ by region

## 8. Availability / Downtime Notes
- Using multiple regions can improve disaster recovery
- Single-region designs are more exposed to regional outages

## 9. Similar Services and Differences
- Commonly confused with Availability Zone
- Region is a large geographic area; an AZ is one isolated location inside a region

## 10. Related Services
- Availability Zone
- VPC
- CloudFront

## 11. Simple Example
- Put a Korea-focused app in ap-northeast-2 to reduce user latency

## 12. Common Mistakes
- Choosing a far region and increasing latency
- Forgetting data residency or compliance requirements

## 13. One-Line Summary
- A Region is the broad geographic location where AWS resources run.

## 14. Official AWS Docs
- https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions-availability-zones.html
