# Amazon SageMaker AI

## 1. Definition
Amazon SageMaker AI is a fully managed service for building, training, and deploying machine learning and foundation models.

## 2. Category / Where It Fits
Which part of AWS it belongs to:
- Analytics

## 3. When To Use It
- When building, training, and deploying ML models on AWS
- When teams want managed ML tooling instead of building everything manually

## 4. What It Does
- Supports data preparation, model training, and deployment
- Provides ML workflows and endpoints

## 5. What AWS Manages vs What You Manage
### AWS Manages
- Much of the ML infrastructure and managed service features
### You Manage
- Datasets, model code, training logic, endpoints, and permissions

## 6. Console Creation Considerations
- Choose whether you need notebooks, training jobs, or endpoints first.
- Set IAM roles and S3 access correctly before running jobs.
- Pick instance types that fit training or inference needs.
- Always-on endpoints can be expensive if they are not monitored.

## 7. Cost Shape
- Charged by notebook, training, and endpoint usage
- Large training jobs and always-on endpoints increase cost

## 8. Availability / Downtime Notes
- Managed endpoints can support stable inference workloads
- Bad scaling or deployment choices can still affect availability

## 9. Similar Services and Differences
- Commonly confused with plain EC2-based ML setups
- SageMaker offers managed ML workflows; EC2 gives more low-level control

## 10. Related Services
- Amazon S3
- AWS Lambda
- Amazon ECR

## 11. Simple Example
- Train a model on historical data and deploy an endpoint for predictions

## 12. Common Mistakes
- Leaving expensive endpoints running
- Starting with complex features before understanding the ML workflow

## 13. One-Line Summary
- Amazon SageMaker AI is a managed platform for building, training, and deploying ML models.

## 14. Official AWS Docs
- https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html
