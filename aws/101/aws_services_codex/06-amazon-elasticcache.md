# Amazon ElastiCache

## 1. Definition
Amazon ElastiCache is a managed in-memory data store and cache service.

## 2. Category / Where It Fits
Which part of AWS it belongs to:
- Database

## 3. When To Use It
- When applications need faster read performance
- When reducing load on a primary database

## 4. What It Does
- Stores frequently used data in memory
- Improves response time for repeated queries or sessions
- Supports serverless caches and node-based clusters

## 5. What AWS Manages vs What You Manage
### AWS Manages
- Much of the cache infrastructure, monitoring, node replacement, and patching
### You Manage
- Cache keys, expiration strategy, client integration, engine choice, and usage patterns

## 6. Console Creation Considerations
- Choose the engine and deployment model that fits the application.
- Place the cache in the right VPC and subnet group.
- Decide expiration strategy and what data is safe to cache.
- Treat it as a cache layer, not the only source of truth.

## 7. Cost Shape
- Charged by node size, engine choice, and runtime
- Large always-on clusters increase cost

## 8. Availability / Downtime Notes
- Can improve application resilience by reducing database pressure
- Cache node failures can affect performance if the app depends too heavily on cached data

## 9. Similar Services and Differences
- Commonly confused with DynamoDB or RDS
- ElastiCache is a cache layer, not a primary system-of-record database

## 10. Related Services
- Amazon RDS
- Amazon EC2
- Amazon DynamoDB

## 11. Simple Example
- Cache popular product data so a web app responds faster

## 12. Common Mistakes
- Treating cache data as the only source of truth
- Using poor expiration policies

## 13. One-Line Summary
- Amazon ElastiCache is a managed in-memory cache for faster applications.

## 14. Official AWS Docs
- https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html
