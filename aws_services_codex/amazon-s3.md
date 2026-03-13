# Amazon S3

## 1. Definition
Amazon S3 is an object storage service for storing and protecting any amount of data.

## 2. Category / Where It Fits
Which part of AWS it belongs to:
- Storage

## 3. When To Use It
- When you need durable file storage
- When storing images, backups, logs, or static website assets

## 4. What It Does
- Stores objects in buckets
- Provides highly scalable storage with strong data availability, security, and performance

## 5. What AWS Manages vs What You Manage
### AWS Manages
- The storage infrastructure, durability, and scaling
### You Manage
- Bucket policies, object lifecycle, encryption choices, and access control

## 6. Console Creation Considerations
- Choose a bucket name carefully because it must be globally unique.
- Decide whether public access should stay blocked.
- Enable versioning, encryption, and lifecycle rules if needed.
- A wrong bucket policy can expose data or break application access.

## 7. Cost Shape
- Charged by stored data, requests, and data transfer
- Large storage volume and frequent access increase cost

## 8. Availability / Downtime Notes
- Designed for high durability and availability
- Misconfigured permissions can make data unavailable to users

## 9. Similar Services and Differences
- Commonly confused with Amazon EBS
- S3 stores objects, while EBS provides block storage for one server

## 10. Related Services
- Amazon CloudFront
- AWS Lambda
- Amazon S3 Glacier

## 11. Simple Example
- Store product images for a website and deliver them through CloudFront

## 12. Common Mistakes
- Making a bucket public by accident
- Using S3 like a normal file system

## 13. One-Line Summary
- Amazon S3 is scalable object storage for files and data.

## 14. Official AWS Docs
- https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html
