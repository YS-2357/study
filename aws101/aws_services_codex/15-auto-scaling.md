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
- Launches new EC2 instances from a launch template when scaling out
- Replaces unhealthy instances automatically when health checks fail

## 5. What AWS Manages vs What You Manage
### AWS Manages
- The automation engine that performs scaling actions
### You Manage
- The launch template or launch template version used to create instances
- Scaling policies, metrics, min size, max size, and desired capacity
- Health check settings, warmup behavior, and load balancer integration

## 6. Console Creation Considerations
- Choose a launch template because new instance types are no longer supported in legacy launch configurations.
- Review the launch template contents carefully: AMI, instance type, security groups, IAM role, key pair, and user data.
- Set reasonable `Desired capacity`, `Min desired capacity`, and `Max desired capacity` values.
- Choose subnets and Availability Zones where the Auto Scaling group can launch instances.
- Attach the correct target group or load balancer if traffic distribution and health checks depend on Elastic Load Balancing.
- Pick a scaling policy that matches real demand. For AWS 101, target tracking is the most important one to understand first.
- Understand which metric drives scaling, such as average CPU utilization or `ALBRequestCountPerTarget`.
- Set health check type and health check grace period so new instances are not replaced before they finish booting.
- Set default instance warmup so new instances are not counted too early in scaling metrics.
- Enable group metrics or CloudWatch monitoring when you need better visibility into scaling behavior.
- Use tags consistently and decide whether they should propagate to launched instances.

## 7. Cost Shape
- No major separate cost for the concept itself
- Cost changes because scaled resources increase or decrease

## 8. Availability / Downtime Notes
- Can reduce downtime by replacing unhealthy instances
- Poor thresholds can still cause instability
- Auto Scaling by itself does not guarantee zero downtime; it is usually combined with multi-AZ design and a load balancer
- A bad launch template or slow application startup can still cause failed replacements

## 9. Similar Services and Differences
- Commonly confused with load balancing
- Auto Scaling changes capacity; a load balancer distributes traffic
- Commonly confused with cloning a running server
- Auto Scaling does not copy the live EC2 instance state. It launches new instances from the launch template configuration

## 10. Related Services
- Amazon EC2
- CloudWatch
- Elastic Load Balancing
- Launch Templates

## 11. Simple Example
- Add more EC2 instances during daytime traffic and reduce them at night
- Keep average CPU near 50% by using a target tracking policy
- Launch new web server instances from the same launch template and register them behind an Application Load Balancer

## 12. Common Mistakes
- Setting thresholds too aggressively
- Forgetting to test scale-in behavior
- Confusing Auto Scaling with load balancing
- Using the wrong scaling metric for the workload
- Setting `Max desired capacity` too low to handle peak traffic
- Forgetting that new instances need startup time before health checks and metrics behave normally
- Thinking Auto Scaling duplicates the current live server instead of launching from a launch template
- Forgetting to update the launch template version when the application image or instance settings change

## 13. One-Line Summary
- Amazon EC2 Auto Scaling changes EC2 instance count automatically to match demand.

## 14. Official AWS Docs
- https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html
- https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-launch-template.html
- https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html
- https://docs.aws.amazon.com/autoscaling/ec2/userguide/enable-default-instance-warmup.html
- https://docs.aws.amazon.com/autoscaling/ec2/userguide/health-check-grace-period.html
- https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-configurations.html
