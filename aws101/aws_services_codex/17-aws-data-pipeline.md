# AWS Data Pipeline

## 1. Definition
AWS Data Pipeline is a web service for processing and moving data between different AWS compute and storage services, as well as on-premises data sources.

## 2. Category / Where It Fits
Which part of AWS it belongs to:
- Analytics

## 3. When To Use It
- When orchestrating older scheduled data movement workflows
- When maintaining existing Data Pipeline-based systems

## 4. What It Does
- Schedules data transfer and processing tasks
- Connects data sources, compute, and destinations

## 5. What AWS Manages vs What You Manage
### AWS Manages
- The workflow scheduling service
### You Manage
- Pipeline definitions, resources, retries, and job logic

## 6. Console Creation Considerations
- Define source, destination, and schedule clearly before creating the pipeline.
- Choose retry and failure handling settings carefully.
- Check whether a newer service like Glue or Step Functions fits better.
- Older-service workflows may require extra review before new adoption.

## 7. Cost Shape
- Charged for pipeline usage and the resources it triggers
- More frequent workflows and attached compute increase cost

## 8. Availability / Downtime Notes
- Workflow failures can delay downstream data updates
- Reliability depends on pipeline design and dependent services

## 9. Similar Services and Differences
- Commonly confused with AWS Glue and Step Functions
- Data Pipeline is older and scheduling-focused; Glue and Step Functions are more common for new builds

## 10. Related Services
- Amazon S3
- Amazon EMR
- Amazon EC2

## 11. Simple Example
- Move logs from S3 to an analytics system every night

## 12. Common Mistakes
- Choosing it for new projects without comparing newer services
- Ignoring retries and error handling

## 13. One-Line Summary
- AWS Data Pipeline schedules and moves data between services.

## 14. Official AWS Docs
- https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/what-is-datapipeline.html
