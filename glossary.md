---
tags:
  - ai
  - aws
  - computing
  - container
  - database
  - git
  - infrastructure
  - ml
  - monitoring
  - networking
  - security
  - serverless
  - storage
  - tooling
created_at: 2026-04-17T14:18:47
updated_at: 2026-04-19T01:37:43
recent_editor: CODEX
---

↑ [Home](home.md)

# Glossary

Abbreviations and domain terms used across this repo, sorted alphabetically.

| Term | Full Name | Definition | Note |
|------|-----------|------------|------|
| ACL | Access Control List | A rule list attached to a resource that specifies which traffic or principals are allowed or denied. | — |
| AI | Artificial Intelligence | Computer systems that perform tasks associated with human reasoning, language, perception, or decision-making. | [note](ai/00_ai_overview.md) |
| ALB | Application Load Balancer | Layer 7 load balancer that routes HTTP/HTTPS traffic by host, path, or header. | [note](aws/networking/01_elastic_load_balancing.md) |
| AMI | Amazon Machine Image | A snapshot of an EC2 instance's OS, config, and data used to launch new instances. | — |
| API | Application Programming Interface | A defined way for software systems to request data or actions from each other. | — |
| ASG | Auto Scaling Group | AWS group that automatically adds or removes EC2 instances based on demand or schedule. | [note](aws/compute/02_auto_scaling.md) |
| AWS | Amazon Web Services | Amazon's cloud platform for compute, storage, networking, databases, AI, security, and managed services. | [note](aws/00_aws_overview.md) |
| BDA | Bedrock Data Automation | AWS service that extracts structured fields from documents, images, video, and audio. | [note](aws/ai/08_amazon_bedrock_data_automation.md) |
| CDK | Cloud Development Kit | AWS framework for defining cloud infrastructure in Python, TypeScript, or other languages. | [note](aws/devtools/01_aws_cdk.md) |
| CDN | Content Delivery Network | A network of edge servers that cache and serve content close to end users. | — |
| CIDR | Classless Inter-Domain Routing | A notation such as `10.0.0.0/16` that defines an IP address range by prefix length. | — |
| CLI | Command-Line Interface | A text-based interface where users run commands in a shell or terminal. | — |
| CSV | Comma-Separated Values | A plain-text table format where rows are lines and columns are separated by commas. | — |
| EBS | Elastic Block Store | AWS block storage volumes attached to a single EC2 instance, like a virtual hard drive. | [note](aws/storage/02_amazon_ebs.md) |
| ECR | Elastic Container Registry | AWS managed Docker image registry. | [note](aws/storage/04_amazon_ecr.md) |
| ECS | Elastic Container Service | AWS container orchestration service that runs Docker containers on EC2 or Fargate. | — |
| EFS | Elastic File System | AWS managed NFS file system that can be mounted by multiple EC2 instances simultaneously. | [note](aws/storage/03_amazon_efs.md) |
| ELB | Elastic Load Balancing | AWS service family that distributes incoming traffic across targets. | [note](aws/networking/01_elastic_load_balancing.md) |
| EMR | Elastic MapReduce | AWS managed big-data platform for running Spark, Hive, and Hadoop workloads. | — |
| ENI | Elastic Network Interface | A virtual network card in a VPC that can be attached to or detached from EC2 instances. | — |
| GWLB | Gateway Load Balancer | Layer 3 load balancer designed to route traffic through third-party virtual appliances such as firewalls or IDS. | — |
| HTML | HyperText Markup Language | Markup language used to structure content on web pages. | — |
| IAM | Identity and Access Management | AWS service for managing users, roles, and permissions for all AWS resources. | [note](aws/identity/01_amazon_iam.md) |
| IGW | Internet Gateway | VPC component that allows traffic between a VPC and the public internet. | — |
| IOPS | Input/Output Operations Per Second | A measure of storage performance indicating how many read/write operations a disk handles per second. | — |
| KMS | Key Management Service | AWS managed service for creating and controlling encryption keys. | — |
| KST | Korean Standard Time | Time zone used for this repo's frontmatter timestamps; equivalent to UTC+9. | — |
| LLM | Large Language Model | A neural network trained on large text corpora to generate and understand natural language. | [note](ai/00_ai_overview.md) |
| LSP | Language Server Protocol | Protocol that lets editors communicate with language analysis tools for autocomplete, go-to-definition, and diagnostics. | — |
| MCP | Model Context Protocol | Open protocol for connecting LLM agents to external tools and data sources via a standard interface. | [note](ai/07_mcp.md) |
| ML | Machine Learning | AI technique where models learn patterns from data instead of being programmed only with explicit rules. | [note](ai/00_ai_overview.md) |
| MSP | Managed Service Provider | A company that remotely manages a customer's IT infrastructure and services, often reselling cloud platforms like AWS. | — |
| MVP | Minimum Viable Product | The smallest useful version of a product that can prove whether the idea solves a real problem. | — |
| NACL | Network Access Control List | Stateless firewall rules applied at the subnet level in a VPC, evaluated in order. | — |
| NAT | Network Address Translation | Mechanism that maps private IP addresses to a public IP so instances without public IPs can reach the internet. | — |
| NLB | Network Load Balancer | Layer 4 load balancer that routes TCP/UDP traffic with ultra-low latency and static IP support. | [note](aws/networking/01_elastic_load_balancing.md) |
| OAC | Origin Access Control | CloudFront mechanism that restricts S3 bucket access to CloudFront only, replacing the older OAI. | [note](aws/networking/02_amazon_cloudfront.md) |
| OSI | Open Systems Interconnection | Seven-layer networking model: Physical, Data Link, Network, Transport, Session, Presentation, Application. | [note](networking/00_networking_overview.md) |
| PDF | Portable Document Format | File format for preserving document layout across devices and operating systems. | — |
| PII | Personally Identifiable Information | Any data that can identify a specific individual, such as a name, email, or SSN. | — |
| POC | Proof of Concept | A small build or experiment used to prove that an idea is technically feasible. | — |
| RAG | Retrieval-Augmented Generation | Pattern where an LLM retrieves relevant documents at query time and uses them as context before generating a response. | [note](aws/ai/03_amazon_bedrock_knowledge_bases.md) |
| RDS | Relational Database Service | AWS managed relational database service supporting MySQL, PostgreSQL, MariaDB, Oracle, and SQL Server. | [note](aws/database/01_amazon_rds.md) |
| SDK | Software Development Kit | A library and toolset that lets code interact with a platform's API, such as boto3 for AWS. | [note](aws/devtools/02_boto3.md) |
| SSM | AWS Systems Manager | AWS service for managing EC2 instances and storing config/secrets in Parameter Store. | [note](aws/ops/02_aws_ssm_parameter_store.md) |
| TLS | Transport Layer Security | Cryptographic protocol that secures data in transit; successor to SSL. | — |
| TTL | Time to Live | A field on a record or item that sets when it expires, used in DNS caching and DynamoDB automatic deletion. | [note](aws/database/03_amazon_dynamodb.md) |
| UI | User Interface | The screens, controls, text, and visual elements a user interacts with in software. | — |
| UX | User Experience | The overall experience a user has while using a product, including clarity, speed, friction, and usefulness. | — |
| VM | Virtual Machine | A software-based computer that runs an operating system on virtualized hardware. | — |
| VPC | Virtual Private Cloud | An isolated virtual network within AWS where you control IP ranges, subnets, and routing. | [note](aws/foundation/04_amazon_vpc.md) |
| WAF | Web Application Firewall | AWS layer 7 firewall that filters HTTP requests by IP, geo, rate, or custom rules. | [note](aws/networking/05_aws_waf.md) |
| WSL | Windows Subsystem for Linux | Windows feature that runs a Linux environment natively without a VM. | [note](tooling/01_wsl_terminal_and_vscode.md) |

---
↑ [Home](home.md)
