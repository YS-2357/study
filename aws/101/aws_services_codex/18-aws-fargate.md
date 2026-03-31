# AWS Fargate

## 1. Definition
AWS Fargate is a serverless, pay-as-you-go compute engine for containers.

## 2. Category / Where It Fits
Which part of AWS it belongs to:
- Compute

## 3. When To Use It
- When you want containers without managing EC2 servers
- When your app already fits a container model

## 4. What It Does
- Runs containers for ECS or EKS
- Handles server provisioning for container workloads

## 5. What AWS Manages vs What You Manage
### AWS Manages
- Underlying compute infrastructure for the containers
### You Manage
- Container images, task definitions, networking, and scaling rules

## 6. Console Creation Considerations
- Choose CPU and memory for each task based on container needs.
- Decide whether tasks run in public or private subnets.
- Set networking, IAM roles, and image source correctly.
- Always-on tasks can become expensive if sizing is too large.

## 7. Cost Shape
- Charged by allocated CPU and memory for running tasks
- More tasks and larger task sizes increase cost

## 8. Availability / Downtime Notes
- Multi-task deployments can support low-downtime updates
- Poor deployment setup can still cause interruption

## 9. Similar Services and Differences
- Commonly confused with Amazon EC2 and AWS Lambda
- Choose Fargate for containers without server management; choose EC2 for server control and Lambda for event-driven functions

## 10. Related Services
- Amazon ECS
- Amazon EKS
- Amazon ECR

## 11. Simple Example
- Run a containerized API on ECS without managing cluster servers

## 12. Common Mistakes
- Treating Fargate as cheaper in every case
- Ignoring VPC and networking setup

## 13. One-Line Summary
- AWS Fargate runs containers without managing servers.

## 14. Official AWS Docs
- https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html
