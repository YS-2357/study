# Amazon Kinesis

## 1. Definition
Amazon Kinesis is a service family for collecting, processing, and analyzing real-time streaming data. In AWS 101 notes, this most often refers to Amazon Kinesis Data Streams.

## 2. Category / Where It Fits
Which part of AWS it belongs to:
- Analytics

## 3. When To Use It
- When data arrives continuously and needs near-real-time processing
- When handling logs, clickstreams, or IoT events

## 4. What It Does
- Ingests streaming data
- Enables real-time processing and delivery to other systems

## 5. What AWS Manages vs What You Manage
### AWS Manages
- The streaming service infrastructure
### You Manage
- Stream design, retention choices, consumers, and scaling settings

## 6. Console Creation Considerations
- Choose the correct Kinesis service or stream mode for the workload.
- Estimate throughput before setting shard or capacity choices.
- Plan consumers and retention needs early.
- Underestimating volume can create lag or throttling.

## 7. Cost Shape
- Charged by stream capacity, data volume, and processing usage
- Higher event throughput increases cost

## 8. Availability / Downtime Notes
- Designed for continuous data flow
- Poor consumer design can create lag or data processing delays

## 9. Similar Services and Differences
- Commonly confused with Amazon SQS
- Kinesis is for streaming data processing; SQS is for decoupled message queues

## 10. Related Services
- AWS Lambda
- Amazon S3
- Amazon Redshift

## 11. Simple Example
- Process website click events in real time for live dashboards

## 12. Common Mistakes
- Underestimating scaling needs
- Treating streams like simple queues

## 13. One-Line Summary
- Amazon Kinesis handles real-time streaming data.

## 14. Official AWS Docs
- https://docs.aws.amazon.com/streams/latest/dev/introduction.html
