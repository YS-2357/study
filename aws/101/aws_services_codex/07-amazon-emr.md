# Amazon EMR

## 1. Definition
Amazon EMR is a managed cluster platform for running big data frameworks such as Apache Hadoop and Apache Spark on AWS.

## 2. Category / Where It Fits
Which part of AWS it belongs to:
- Analytics

## 3. When To Use It
- When running big data frameworks like Hadoop or Spark
- When large-scale batch data processing is needed

## 4. What It Does
- Creates clusters for big data processing
- Runs distributed analytics jobs on large datasets

## 5. What AWS Manages vs What You Manage
### AWS Manages
- Cluster provisioning and much of the infrastructure management
### You Manage
- Framework configuration, job logic, scaling choices, and data pipelines

## 6. Console Creation Considerations
- Choose the right frameworks such as Spark or Hadoop for the job.
- Decide whether the cluster should be long-running or transient.
- Set instance types and cluster size based on data volume.
- Leaving clusters running after jobs finish can waste money quickly.

## 7. Cost Shape
- Charged mainly by cluster resources and storage used
- Long-running clusters and large nodes increase cost

## 8. Availability / Downtime Notes
- Job interruption can happen if clusters are not designed for resilience
- Transient clusters can reduce always-on risk and cost

## 9. Similar Services and Differences
- Commonly confused with AWS Glue
- EMR gives more framework control; Glue is more serverless and ETL-focused

## 10. Related Services
- Amazon S3
- Amazon EC2
- AWS Glue

## 11. Simple Example
- Run nightly Spark jobs to aggregate clickstream data from S3

## 12. Common Mistakes
- Keeping clusters running when not needed
- Choosing EMR when a simpler managed ETL service would work

## 13. One-Line Summary
- Amazon EMR runs big data processing frameworks on AWS.

## 14. Official AWS Docs
- https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html
