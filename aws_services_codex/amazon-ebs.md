# Amazon EBS

## 1. Definition
Amazon EBS is an easy-to-use, scalable block storage service for Amazon EC2.

## 2. Category / Where It Fits
Which part of AWS it belongs to:
- Storage

## 3. When To Use It
- When an EC2 instance needs persistent disk storage
- When you need a virtual hard drive for a server

## 4. What It Does
- Provides attachable storage volumes to EC2
- Stores OS disks, application data, and databases on instances

## 5. What AWS Manages vs What You Manage
### AWS Manages
- The storage platform and replication inside an AZ
### You Manage
- Volume size, type, snapshots, and attachment to instances

## 6. Console Creation Considerations
- Choose the volume type based on performance and cost needs.
- Set enough size for current and near-future usage.
- Remember the volume must be created in the same AZ as the EC2 instance.
- Unused detached volumes still cost money.

## 7. Cost Shape
- Charged by provisioned volume size, type, and snapshots
- Larger and higher-performance volumes cost more

## 8. Availability / Downtime Notes
- Usually tied to one AZ
- Instance or volume changes can require planning to avoid interruption

## 9. Similar Services and Differences
- Commonly confused with Amazon S3
- EBS is block storage for EC2; S3 is object storage for files

## 10. Related Services
- Amazon EC2
- Amazon EBS Snapshot
- Auto Scaling

## 11. Simple Example
- Attach an EBS volume to an EC2 web server to store application data

## 12. Common Mistakes
- Forgetting that EBS volumes are AZ-specific
- Paying for unused detached volumes

## 13. One-Line Summary
- Amazon EBS is persistent disk storage for EC2 instances.

## 14. Official AWS Docs
- https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html
