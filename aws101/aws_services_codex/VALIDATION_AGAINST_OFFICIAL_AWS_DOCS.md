# Validation Against Official AWS Docs

This folder was reviewed against official AWS documentation pages on the internet.

## Result Summary
- `25/25` service and concept files were validated against official AWS docs
- `25/25` files now include an `Official AWS Docs` section with a primary AWS documentation link
- `25/25` files now include a `Console Creation Considerations` section for practical AWS Console setup decisions
- All files were kept at AWS 101 level, but weaker definitions were reinforced to align more closely with AWS’s own service framing
- On `2026-03-13`, all `25/25` linked official AWS documentation URLs returned `HTTP 200` during the verification pass

## Reinforcement Applied Across The Folder
- Added an `Official AWS Docs` section to every file
- Added a `Console Creation Considerations` section to every file
- Tightened beginner-facing definitions where the previous wording was too generic or drifted from AWS’s official positioning
- Preserved the original AWS 101 structure so the notes stay easy to study

## Notable Augmentations Applied
- `amazon-ec2.md`
  - Refined the definition to match AWS’s “on-demand, scalable computing capacity” wording
  - Added explicit mention of major pricing models
  - Official doc: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html
- `amazon-s3.md`
  - Strengthened the definition from “file storage” language to official object-storage language
  - Added emphasis on scalability, availability, security, and performance
  - Official doc: https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html
- `amazon-dynamodb.md`
  - Updated the definition to reflect the official “serverless, fully managed, distributed NoSQL” positioning
  - Added low-latency-at-scale wording
  - Official doc: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html
- `amazon-redshift.md`
  - Updated the definition to “fully managed data warehouse”
  - Added mention of both provisioned and serverless options
  - Official doc: https://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html
- `amazon-elasticcache.md`
  - Updated the definition from only “cache” to “in-memory data store and cache”
  - Added mention of serverless caches and node-based clusters
  - Official doc: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html
- `amazon-iam.md`
  - Updated the definition to align with the official secure access-control framing
  - Added explicit authentication/authorization language
  - Reflected the official service name as `AWS IAM`
  - Official doc: https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html
- `amazon-sagemaker.md`
  - Reflected the current AWS service name as `Amazon SageMaker AI`
  - Official doc: https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html
- `aws-waf.md`
  - Updated the definition to match AWS’s “monitor and control HTTP(S) requests” framing
  - Added protected-resource examples
  - Official doc: https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html
- `aws-shield.md`
  - Clarified Shield Standard vs Shield Advanced
  - Clarified that Shield Standard is included automatically at no extra charge
  - Official doc: https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html

## Concept and Service Mapping

### Global Infrastructure and Networking Concepts
- `region.md`
  - Official doc: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions-availability-zones.html
  - Validation note: reinforced and linked
- `availability-zone.md`
  - Official doc: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions-availability-zones.html
  - Validation note: reinforced and linked
- `subnet.md`
  - Official doc: https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html
  - Validation note: reinforced and linked
- `amazon-vpc.md`
  - Official doc: https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html
  - Validation note: reinforced and linked
- `security-group.md`
  - Official doc: https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html
  - Validation note: reinforced and linked
- `pop.md`
  - Official doc: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html
  - Validation note: reinforced and linked

### Compute
- `amazon-ec2.md`
  - Official doc: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html
  - Validation note: reinforced and linked
- `auto-scaling.md`
  - Official doc: https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html
  - Validation note: reinforced and linked
- `aws-lambda.md`
  - Official doc: https://docs.aws.amazon.com/lambda/latest/dg/welcome.html
  - Validation note: reinforced and linked
- `aws-fargate.md`
  - Official doc: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html
  - Validation note: reinforced and linked

### Storage and Content Delivery
- `amazon-s3.md`
  - Official doc: https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html
  - Validation note: reinforced and linked
- `amazon-ebs.md`
  - Official doc: https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html
  - Validation note: reinforced and linked
- `amazon-cloudfront.md`
  - Official doc: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html
  - Validation note: reinforced and linked

### Databases
- `amazon-rds.md`
  - Official doc: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html
  - Validation note: reinforced and linked
- `amazon-aurora.md`
  - Official doc: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html
  - Validation note: reinforced and linked
- `amazon-dynamodb.md`
  - Official doc: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html
  - Validation note: reinforced and linked
- `amazon-elasticcache.md`
  - Official doc: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html
  - Validation note: reinforced and linked

### Analytics and Data
- `amazon-redshift.md`
  - Official doc: https://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html
  - Validation note: reinforced and linked
- `amazon-emr.md`
  - Official doc: https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html
  - Validation note: reinforced and linked
- `aws-data-pipeline.md`
  - Official doc: https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/what-is-datapipeline.html
  - Validation note: reinforced and linked
- `amazon-kinesis.md`
  - Official doc: https://docs.aws.amazon.com/streams/latest/dev/introduction.html
  - Validation note: reinforced and linked
- `amazon-sagemaker.md`
  - Official doc: https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html
  - Validation note: reinforced, linked, and renamed to match current AWS terminology

### Security
- `amazon-iam.md`
  - Official doc: https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html
  - Validation note: reinforced, linked, and renamed to match current AWS terminology
- `aws-shield.md`
  - Official doc: https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html
  - Validation note: reinforced and linked
- `aws-waf.md`
  - Official doc: https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html
  - Validation note: reinforced and linked

## Caveats
- The notes are intentionally concise and remain AWS 101-level summaries, not full service references.
- Official AWS docs contain much more detail on quotas, pricing details, regional availability, configuration steps, and advanced caveats.
- A useful next pass would be to add one small `Must-Know Limits or Caveats` section to each file using the linked official docs as the source.
