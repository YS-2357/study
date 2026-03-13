# Amazon DynamoDB

## 1. Definition
Amazon DynamoDB is a serverless, fully managed, distributed NoSQL database service.

## 2. Category / Where It Fits
Which part of AWS it belongs to:
- Database

## 3. When To Use It
- When you need very fast, scalable key-value or document storage
- When workloads need low-latency access at large scale

## 4. What It Does
- Stores data without a relational schema
- Delivers low-latency performance at scale for key-value and document workloads
- Scales automatically for many application workloads

## 5. What AWS Manages vs What You Manage
### AWS Manages
- The database infrastructure, scaling, and much of the operational platform
### You Manage
- Data model, partition key design, access patterns, and permissions

## 6. Console Creation Considerations
- Choose the partition key design based on how the application reads and writes data.
- Decide between on-demand and provisioned capacity modes.
- Consider whether you need global tables, TTL, or streams.
- Bad key design is hard to fix later and can hurt both cost and performance.

## 7. Cost Shape
- Charged by read/write usage, storage, and optional features
- Poor key design and heavy traffic can increase cost

## 8. Availability / Downtime Notes
- Built for high availability and managed scaling
- Bad partition design can still hurt performance

## 9. Similar Services and Differences
- Commonly confused with Amazon RDS
- DynamoDB is NoSQL and access-pattern-driven; RDS is relational and SQL-based

## 10. Related Services
- AWS Lambda
- Amazon API Gateway
- Amazon CloudWatch

## 11. Simple Example
- Store user session data or shopping cart data with very fast lookup

## 12. Common Mistakes
- Designing it like a relational database
- Choosing weak partition keys

## 13. One-Line Summary
- Amazon DynamoDB is a serverless NoSQL database for low-latency access at scale.

## 14. Official AWS Docs
- https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html
