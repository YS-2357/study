# AWS IAM

## 1. Definition
AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS resources.

## 2. Category / Where It Fits
Which part of AWS it belongs to:
- Security

## 3. When To Use It
- When controlling who can access AWS resources
- When assigning permissions to users, roles, and services

## 4. What It Does
- Manages identities and permissions
- Controls authentication and authorization for AWS accounts and resources
- Lets AWS services assume roles securely

## 5. What AWS Manages vs What You Manage
### AWS Manages
- The IAM service platform
### You Manage
- Users, roles, policies, and least-privilege design

## 6. Console Creation Considerations
- Decide whether the workload needs a user, role, or policy update.
- Grant the smallest set of permissions needed for the task.
- Use roles for AWS services instead of long-term credentials when possible.
- One broad wildcard policy can affect security across the account.

## 7. Cost Shape
- IAM itself is generally not separately charged
- Indirect cost comes from security mistakes or overly broad access

## 8. Availability / Downtime Notes
- Policy changes take effect quickly
- Incorrect permissions can immediately block systems or users

## 9. Similar Services and Differences
- Commonly confused with Security Groups
- IAM controls identity permissions; Security Groups control network traffic

## 10. Related Services
- AWS Organizations
- AWS Lambda
- Amazon EC2

## 11. Simple Example
- Give a Lambda function permission to read from an S3 bucket

## 12. Common Mistakes
- Granting `*` permissions too broadly
- Using long-term credentials when roles are better

## 13. One-Line Summary
- AWS IAM controls who can do what in AWS.

## 14. Official AWS Docs
- https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html
