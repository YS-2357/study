# PoP

## 1. Definition
PoP stands for Point of Presence, an edge location used by services such as CloudFront to deliver content closer to users.

## 2. Category / Where It Fits
Which part of AWS it belongs to:
- Networking

## 3. When To Use It
- When learning how AWS edge services reduce latency
- When understanding CloudFront and global content delivery

## 4. What It Does
- Brings content closer to end users
- Reduces response time for cached or accelerated traffic

## 5. What AWS Manages vs What You Manage
### AWS Manages
- The global edge location infrastructure
### You Manage
- Which services use the edge network and how caching is configured

## 6. Console Creation Considerations
- You usually do not create a PoP directly; you use services like CloudFront that use edge locations for you.
- The main decision is whether the workload benefits from edge delivery.
- Choose caching and origin behavior carefully through the parent service.
- Understand that PoP improves delivery speed but does not replace the origin design.

## 7. Cost Shape
- No direct charge for PoP itself
- Cost comes from services like CloudFront that use the edge network

## 8. Availability / Downtime Notes
- Edge distribution can improve resilience and performance
- Origin problems can still affect user experience

## 9. Similar Services and Differences
- Commonly confused with Region
- A PoP is an edge delivery location, not a full AWS region for running general workloads

## 10. Related Services
- Amazon CloudFront
- AWS Shield
- AWS WAF

## 11. Simple Example
- A user in Europe receives website images from a nearby CloudFront edge location

## 12. Common Mistakes
- Thinking PoP is the same as a Region
- Ignoring that the origin still matters

## 13. One-Line Summary
- A PoP is an edge location that helps deliver content faster.

## 14. Official AWS Docs
- https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html
