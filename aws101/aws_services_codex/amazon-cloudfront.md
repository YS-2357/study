# Amazon CloudFront

## 1. Definition
Amazon CloudFront is a content delivery network service that securely delivers content with low latency and high transfer speeds.

## 2. Category / Where It Fits
Which part of AWS it belongs to:
- Networking

## 3. When To Use It
- When you want faster content delivery worldwide
- When serving static files, media, or APIs with lower latency

## 4. What It Does
- Delivers cached content from edge locations
- Reduces load on origin servers

## 5. What AWS Manages vs What You Manage
### AWS Manages
- The global edge network and cache infrastructure
### You Manage
- Distribution settings, origins, caching behavior, and security policies

## 6. Console Creation Considerations
- Choose the correct origin such as S3 bucket or load balancer.
- Decide caching behavior and TTL settings based on content type.
- Add HTTPS and certificate settings if the service is public.
- Wrong cache rules can serve stale content or break dynamic behavior.

## 7. Cost Shape
- Charged by data transfer and requests
- Global traffic and cache misses increase cost

## 8. Availability / Downtime Notes
- Can improve availability by caching content away from the origin
- Bad cache or origin settings can still break delivery

## 9. Similar Services and Differences
- Commonly confused with AWS Global Accelerator
- CloudFront focuses on cached content delivery; Global Accelerator focuses on network path optimization

## 10. Related Services
- Amazon S3
- AWS WAF
- AWS Shield

## 11. Simple Example
- Deliver website images and videos globally from S3 through CloudFront

## 12. Common Mistakes
- Caching dynamic content incorrectly
- Forgetting to invalidate cache after updates

## 13. One-Line Summary
- Amazon CloudFront delivers content from locations closer to users.

## 14. Official AWS Docs
- https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html
