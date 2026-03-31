# Amazon EC2

## 1. Definition
Amazon EC2 provides on-demand, scalable computing capacity in AWS through virtual servers called instances.

## 2. Category / Where It Fits
Which part of AWS it belongs to:
- Compute

## 3. When To Use It
- When you need full control over the server
- When your app cannot easily run in serverless form

## 4. What It Does
- Launches virtual machines in the cloud
- Provides configurable CPU, memory, storage, and networking
- Supports multiple pricing models such as On-Demand, Savings Plans, Reserved Instances, and Spot

## 5. What AWS Manages vs What You Manage
### AWS Manages
- Physical hardware and core virtualization platform
### You Manage
- OS, patches, application deployment, scaling setup, and instance security

## 6. Console Creation Considerations
- Choose the instance family and size based on CPU, memory, and workload type.
- Pick the correct AMI, key pair, and security group during launch.
- Decide whether the instance needs public access or should stay private.
- Check storage type and size carefully because overprovisioning increases cost.

## 7. Cost Shape
- Charged mainly by instance runtime, storage, and data transfer
- Larger instance types and always-on usage increase cost

## 8. Availability / Downtime Notes
- Single-instance setups can have downtime during failures or changes
- Multi-instance and load-balanced setups can reduce interruption

## 9. Similar Services and Differences
- Commonly confused with AWS Lambda and AWS Fargate
- Choose EC2 when you need server control; choose Lambda or Fargate for less server management

## 10. Related Services
- Amazon EBS
- Auto Scaling
- Security Group

## 11. Simple Example
- Run a custom web application on Linux servers behind a load balancer

## 12. Common Mistakes
- Leaving instances running unnecessarily
- Using overly broad security group rules

## 13. One-Line Summary
- Amazon EC2 provides scalable virtual servers in AWS.

## 14. Official AWS Docs
- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html
