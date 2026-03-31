# AWS Lambda

## 1. Definition
AWS Lambda is a compute service that lets you run code without provisioning or managing servers.

## 2. Category / Where It Fits
Which part of AWS it belongs to:
- Compute

## 3. When To Use It
- When you want to run code without managing servers
- When workloads are event-driven or intermittent

## 4. What It Does
- Executes functions on demand in response to events
- Scales automatically for many event sources

## 5. What AWS Manages vs What You Manage
### AWS Manages
- Servers, runtime environment, and automatic scaling
### You Manage
- Function code, permissions, timeouts, memory, and event integration

## 6. Console Creation Considerations
- Set the correct runtime, memory, and timeout for the function.
- Decide what event source will trigger the function.
- Give the function only the IAM permissions it actually needs.
- Watch for timeout limits and cold-start impact on user-facing workloads.

## 7. Cost Shape
- Charged by request count and execution duration
- High request volume and long-running functions increase cost

## 8. Availability / Downtime Notes
- Usually runs without planned downtime
- Cold starts can affect latency for some workloads

## 9. Similar Services and Differences
- Commonly confused with Amazon EC2 and AWS Fargate
- Choose Lambda for event-driven serverless tasks; choose EC2 or Fargate for longer-running or more customizable workloads

## 10. Related Services
- Amazon API Gateway
- Amazon S3
- Amazon CloudWatch

## 11. Simple Example
- Resize images automatically when new files are uploaded to S3

## 12. Common Mistakes
- Using Lambda for long-running server-like workloads
- Forgetting least-privilege IAM permissions

## 13. One-Line Summary
- AWS Lambda runs code on demand without server management.

## 14. Official AWS Docs
- https://docs.aws.amazon.com/lambda/latest/dg/welcome.html
