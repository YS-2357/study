# Amazon EC2 Auto Scaling

## 1. Definition
Amazon EC2 Auto Scaling helps you maintain application availability and automatically add or remove EC2 instances according to conditions you define.

## 2. Category / Where It Fits
Which part of AWS it belongs to:
- Compute

## 3. When To Use It
- When traffic changes over time
- When you want better availability and cost control

## 4. What It Does
- Adds or removes instances automatically
- Helps keep enough capacity running during load changes

## 5. What AWS Manages vs What You Manage
### AWS Manages
- The automation engine that performs scaling actions
### You Manage
- Scaling policies, min and max size, and alarms

## 6. Console Creation Considerations
- Set reasonable minimum, maximum, and desired capacity values.
- Choose scaling policies that match real traffic patterns.
- Make sure health checks and load balancing are configured correctly.
- Poor thresholds can cause unstable scaling or unnecessary cost.

## 7. Cost Shape
- No major separate cost for the concept itself
- Cost changes because scaled resources increase or decrease

## 8. Availability / Downtime Notes
- Can reduce downtime by replacing unhealthy instances
- Poor thresholds can still cause instability

## 9. Similar Services and Differences
- Commonly confused with load balancing
- Auto Scaling changes capacity; a load balancer distributes traffic

## 10. Related Services
- Amazon EC2
- CloudWatch
- Elastic Load Balancing

## 11. Simple Example
- Add more EC2 instances during daytime traffic and reduce them at night

## 12. Common Mistakes
- Setting thresholds too aggressively
- Forgetting to test scale-in behavior

## 13. One-Line Summary
- Amazon EC2 Auto Scaling changes EC2 instance count automatically to match demand.

## 14. Official AWS Docs
- https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html
