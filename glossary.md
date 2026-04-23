---
tags:
  - ai
  - aws
  - computing
  - container
  - database
  - git
  - graph
  - infrastructure
  - ml
  - monitoring
  - networking
  - robotics
  - sap
  - security
  - serverless
  - storage
  - tooling
created_at: 2026-04-17T14:18:47
updated_at: 2026-04-23T23:41:19
recent_editor: CODEX
---

↑ [Home](home.md)

# Glossary

Abbreviations and domain terms used across this repo, sorted alphabetically.

| Term     | Full Name                                    | Definition                                                                                                               | Note                                                          |
| -------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------- |
| ABAP     | Advanced Business Application Programming   | SAP's proprietary 4GL programming language for building ERP applications on SAP systems.                                 | [note](cloud/aws/devtools/04_sap_aws.md)                      |
| ACL      | Access Control List                          | A rule list attached to a resource that specifies which traffic or principals are allowed or denied.                     | —                                                             |
| AI       | Artificial Intelligence                      | Computer systems that perform tasks associated with human reasoning, language, perception, or decision-making.           | [note](ai/00_ai_overview.md)                                  |
| AIOps    | AI for IT Operations                         | Practice of applying AI/ML to automate monitoring, root cause analysis, and remediation in IT operations.                | [note](cloud/aws/ai/15_agentic_modernization.md)              |
| ALB      | Application Load Balancer                    | Layer 7 load balancer that routes HTTP/HTTPS traffic by host, path, or header.                                           | [note](cloud/aws/networking/01_elastic_load_balancing.md)     |
| AMI      | Amazon Machine Image                         | A snapshot of an EC2 instance's OS, config, and data used to launch new instances.                                       | —                                                             |
| API      | Application Programming Interface            | A defined way for software systems to request data or actions from each other.                                           | —                                                             |
| APJ      | Asia Pacific & Japan                         | AWS geographic market grouping covering the Asia-Pacific and Japan regions.                                              | —                                                             |
| ASG      | Auto Scaling Group                           | AWS group that automatically adds or removes EC2 instances based on demand or schedule.                                  | [note](cloud/aws/compute/02_auto_scaling.md)                  |
| ATC      | ABAP Test Cockpit                            | SAP's built-in static analysis and quality-check tool for ABAP code.                                                    | [note](cloud/aws/devtools/04_sap_aws.md)                      |
| AWS      | Amazon Web Services                          | Amazon's cloud platform for compute, storage, networking, databases, AI, security, and managed services.                 | [note](cloud/aws/00_aws_overview.md)                          |
| BAS      | Business Application Studio                  | SAP's cloud-based IDE for developing ABAP and other SAP applications, hosted on BTP.                                    | [note](cloud/aws/devtools/04_sap_aws.md)                      |
| BDA      | Bedrock Data Automation                      | AWS service that extracts structured fields from documents, images, video, and audio.                                    | [note](cloud/aws/ai/08_amazon_bedrock_data_automation.md)     |
| BFO      | Basic Formal Ontology                        | A top-level ontology providing abstract categories and relations for domain-specific ontology design.                    | [note](cloud/aws/database/07_amazon_neptune.md)               |
| BLEU     | Bilingual Evaluation Understudy              | Precision-based metric for evaluating text generation quality by comparing n-gram overlap with reference text.           | [note](cloud/aws/ai/13_llm_evaluation.md)                     |
| BTP      | Business Technology Platform                 | SAP's cloud platform for running SAP applications, integration, and AI workloads.                                       | [note](cloud/aws/devtools/04_sap_aws.md)                      |
| CDK      | Cloud Development Kit                        | AWS framework for defining cloud infrastructure in Python, TypeScript, or other languages.                               | [note](cloud/aws/devtools/01_aws_cdk.md)                      |
| CDN      | Content Delivery Network                     | A network of edge servers that cache and serve content close to end users.                                               | —                                                             |
| CI/CD    | Continuous Integration / Continuous Deployment | Practice of automatically testing and deploying code changes; CI merges and tests, CD ships to production.             | —                                                             |
| CIDR     | Classless Inter-Domain Routing               | A notation such as `10.0.0.0/16` that defines an IP address range by prefix length.                                     | —                                                             |
| CLI      | Command-Line Interface                       | A text-based interface where users run commands in a shell or terminal.                                                  | —                                                             |
| CSV      | Comma-Separated Values                       | A plain-text table format where rows are lines and columns are separated by commas.                                      | —                                                             |
| CVE      | Common Vulnerabilities and Exposures         | Public catalog of known security vulnerabilities, each with a unique CVE ID and severity score.                         | —                                                             |
| DevOps   | Development and Operations                   | Practice of combining software development and IT operations to shorten delivery cycles and improve reliability.         | —                                                             |
| EBS      | Elastic Block Store                          | AWS block storage volumes attached to a single EC2 instance, like a virtual hard drive.                                 | [note](cloud/aws/storage/02_amazon_ebs.md)                    |
| ECR      | Elastic Container Registry                   | AWS managed Docker image registry.                                                                                       | [note](cloud/aws/storage/04_amazon_ecr.md)                    |
| ECS      | Elastic Container Service                    | AWS container orchestration service that runs Docker containers on EC2 or Fargate.                                       | —                                                             |
| EFS      | Elastic File System                          | AWS managed NFS file system that can be mounted by multiple EC2 instances simultaneously.                                | [note](cloud/aws/storage/03_amazon_efs.md)                    |
| EKS      | Elastic Kubernetes Service                   | AWS managed Kubernetes service that runs control planes and nodes without manual cluster management.                     | [note](cloud/aws/ai/15_agentic_modernization.md)              |
| ELB      | Elastic Load Balancing                       | AWS service family that distributes incoming traffic across targets.                                                     | [note](cloud/aws/networking/01_elastic_load_balancing.md)     |
| EMR      | Elastic MapReduce                            | AWS managed big-data platform for running Spark, Hive, and Hadoop workloads.                                            | —                                                             |
| ENI      | Elastic Network Interface                    | A virtual network card in a VPC that can be attached to or detached from EC2 instances.                                 | —                                                             |
| ERP      | Enterprise Resource Planning                 | Integrated software system managing core business processes — finance, HR, supply chain, procurement.                   | [note](cloud/aws/devtools/04_sap_aws.md)                      |
| ETL      | Extract, Transform, Load                     | Data pipeline pattern: extract from source, transform/clean, load into target (warehouse or lake).                      | —                                                             |
| FIBO     | Financial Industry Business Ontology         | Standard ontology defining financial concepts and relationships for semantic data interoperability in finance.           | [note](cloud/aws/database/07_amazon_neptune.md)               |
| FinOps   | Financial Operations                         | Cloud financial management practice focused on optimizing cloud spend through collaboration between engineering and finance. | —                                                         |
| GenAI    | Generative AI                                | AI systems that generate new content (text, images, code, audio) from learned patterns, typically via foundation models. | [note](ai/00_ai_overview.md)                                 |
| GWLB     | Gateway Load Balancer                        | Layer 3 load balancer designed to route traffic through third-party virtual appliances such as firewalls or IDS.         | —                                                             |
| HIPAA    | Health Insurance Portability and Accountability Act | US law requiring protection of patient health information (PHI) in healthcare systems.                          | —                                                             |
| HITL     | Human in the Loop                            | Pattern where a human must review and approve an AI decision before it takes effect on critical actions.                 | —                                                             |
| HTML     | HyperText Markup Language                    | Markup language used to structure content on web pages.                                                                  | —                                                             |
| IaC      | Infrastructure as Code                       | Practice of defining and managing cloud infrastructure through machine-readable configuration files rather than manual processes. | [note](cloud/aws/devtools/01_aws_cdk.md)              |
| IAM      | Identity and Access Management               | AWS service for managing users, roles, and permissions for all AWS resources.                                            | [note](cloud/aws/identity/01_amazon_iam.md)                   |
| IGW      | Internet Gateway                             | VPC component that allows traffic between a VPC and the public internet.                                                 | —                                                             |
| IOPS     | Input/Output Operations Per Second           | A measure of storage performance indicating how many read/write operations a disk handles per second.                    | —                                                             |
| IoT      | Internet of Things                           | Network of physical devices embedded with sensors and connectivity that collect and exchange data.                       | [note](cloud/aws/ai/14_physical_ai.md)                        |
| ITIL     | IT Infrastructure Library                    | Framework of best practices for IT service management (ITSM), widely used by MSPs.                                      | —                                                             |
| KG       | Knowledge Graph                              | A graph-structured data model linking entities and their relationships using nodes and edges with semantic meaning.       | [note](cloud/aws/database/07_amazon_neptune.md)               |
| KMS      | Key Management Service                       | AWS managed service for creating and controlling encryption keys.                                                        | —                                                             |
| KST      | Korean Standard Time                         | Time zone used for this repo's frontmatter timestamps; equivalent to UTC+9.                                              | —                                                             |
| LLM      | Large Language Model                         | A neural network trained on large text corpora to generate and understand natural language.                              | [note](ai/00_ai_overview.md)                                  |
| LSP      | Language Server Protocol                     | Protocol that lets editors communicate with language analysis tools for autocomplete, go-to-definition, and diagnostics. | —                                                             |
| MCP      | Model Context Protocol                       | Open protocol for connecting LLM agents to external tools and data sources via a standard interface.                     | [note](ai/concepts/07_mcp.md)                                          |
| ML       | Machine Learning                             | AI technique where models learn patterns from data instead of being programmed only with explicit rules.                 | [note](ai/00_ai_overview.md)                                  |
| MLOps    | Machine Learning Operations                  | Practice of automating and operationalizing ML workflows — training, evaluation, deployment, monitoring.                 | —                                                             |
| MSP      | Managed Service Provider                     | A company that remotely manages a customer's IT infrastructure and services, often reselling cloud platforms like AWS.   | —                                                             |
| MVP      | Minimum Viable Product                       | The smallest useful version of a product that can prove whether the idea solves a real problem.                          | —                                                             |
| NACL     | Network Access Control List                  | Stateless firewall rules applied at the subnet level in a VPC, evaluated in order.                                       | —                                                             |
| NAT      | Network Address Translation                  | Mechanism that maps private IP addresses to a public IP so instances without public IPs can reach the internet.          | —                                                             |
| NLB      | Network Load Balancer                        | Layer 4 load balancer that routes TCP/UDP traffic with ultra-low latency and static IP support.                          | [note](cloud/aws/networking/01_elastic_load_balancing.md)     |
| OAC      | Origin Access Control                        | CloudFront mechanism that restricts S3 bucket access to CloudFront only, replacing the older OAI.                        | [note](cloud/aws/networking/02_amazon_cloudfront.md)          |
| OSI      | Open Systems Interconnection                 | Seven-layer networking model: Physical, Data Link, Network, Transport, Session, Presentation, Application.               | [note](networking/00_networking_overview.md)                  |
| OWL      | Web Ontology Language                        | W3C language for defining formal ontologies on the Semantic Web, built on RDF.                                          | [note](cloud/aws/database/07_amazon_neptune.md)               |
| PCI-DSS  | Payment Card Industry Data Security Standard | Security standard for handling cardholder data, required for any system processing credit card transactions.             | —                                                             |
| PDF      | Portable Document Format                     | File format for preserving document layout across devices and operating systems.                                         | —                                                             |
| PII      | Personally Identifiable Information          | Any data that can identify a specific individual, such as a name, email, or SSN.                                         | —                                                             |
| POC      | Proof of Concept                             | A small build or experiment used to prove that an idea is technically feasible.                                          | —                                                             |
| RAG      | Retrieval-Augmented Generation               | Pattern where an LLM retrieves relevant documents at query time and uses them as context before generating a response.   | [note](cloud/aws/ai/03_amazon_bedrock_knowledge_bases.md)     |
| RDF      | Resource Description Framework               | W3C standard for representing knowledge as subject–predicate–object triples; backbone of Semantic Web and ontologies.   | [note](cloud/aws/database/07_amazon_neptune.md)               |
| RDS      | Relational Database Service                  | AWS managed relational database service supporting MySQL, PostgreSQL, MariaDB, Oracle, and SQL Server.                   | [note](cloud/aws/database/01_amazon_rds.md)                   |
| RL       | Reinforcement Learning                       | ML training method where an agent learns by trial-and-error to maximize cumulative reward from an environment.           | [note](cloud/aws/ai/14_physical_ai.md)                        |
| ROS      | Robot Operating System                       | Open-source middleware framework for building robot software, providing drivers, libraries, and tools.                   | [note](cloud/aws/ai/14_physical_ai.md)                        |
| SDK      | Software Development Kit                     | A library and toolset that lets code interact with a platform's API, such as boto3 for AWS.                              | [note](cloud/aws/devtools/02_boto3.md)                        |
| SHACL    | Shapes Constraint Language                   | W3C language for validating RDF graphs against a set of structural constraints and conditions.                           | [note](cloud/aws/database/07_amazon_neptune.md)               |
| SLI      | Service Level Indicator                      | A quantitative measure of a service's behavior (e.g., request latency, error rate) used to assess SLO compliance.       | [note](cloud/aws/ai/15_agentic_modernization.md)              |
| SLO      | Service Level Objective                      | A target value or range for an SLI (e.g., 99.9% requests under 200ms) agreed upon by service owners and customers.      | [note](cloud/aws/ai/15_agentic_modernization.md)              |
| SME      | Subject Matter Expert                        | A person with deep domain knowledge, often used to provide ground-truth labels or evaluations in AI workflows.           | —                                                             |
| SNS      | Simple Notification Service                  | AWS managed pub/sub messaging service for fan-out notifications to SQS, Lambda, email, SMS, and HTTP endpoints.         | —                                                             |
| SOC2     | Service Organization Control 2               | Auditing standard for SaaS providers verifying controls around security, availability, and confidentiality of data.      | —                                                             |
| SPARQL   | SPARQL Protocol and RDF Query Language       | W3C query language for retrieving and manipulating data stored in RDF format.                                            | [note](cloud/aws/database/07_amazon_neptune.md)               |
| SQL      | Structured Query Language                    | Standard language for querying and manipulating relational databases (SELECT, INSERT, UPDATE, DELETE).                   | —                                                             |
| SSM      | AWS Systems Manager                          | AWS service for managing EC2 instances and storing config/secrets in Parameter Store.                                    | [note](cloud/aws/ops/02_aws_ssm_parameter_store.md)           |
| TLS      | Transport Layer Security                     | Cryptographic protocol that secures data in transit; successor to SSL.                                                   | —                                                             |
| TTL      | Time to Live                                 | A field on a record or item that sets when it expires, used in DNS caching and DynamoDB automatic deletion.              | [note](cloud/aws/database/03_amazon_dynamodb.md)              |
| UI       | User Interface                               | The screens, controls, text, and visual elements a user interacts with in software.                                      | —                                                             |
| URI      | Uniform Resource Identifier                  | A string that uniquely identifies a resource; URLs are a subset; used in RDF to identify ontology entities globally.     | —                                                             |
| UX       | User Experience                              | The overall experience a user has while using a product, including clarity, speed, friction, and usefulness.             | —                                                             |
| VLA      | Vision-Language-Action model                 | AI model that maps visual observations and language instructions directly to robot actions.                              | [note](cloud/aws/ai/14_physical_ai.md)                        |
| VLM      | Vision Language Model                        | Multimodal AI model that processes both image and text inputs to answer questions or generate descriptions.               | [note](cloud/aws/ai/14_physical_ai.md)                        |
| VM       | Virtual Machine                              | A software-based computer that runs an operating system on virtualized hardware.                                         | —                                                             |
| VPC      | Virtual Private Cloud                        | An isolated virtual network within AWS where you control IP ranges, subnets, and routing.                                | [note](cloud/aws/foundation/04_amazon_vpc.md)                 |
| W3C      | World Wide Web Consortium                    | International standards body that defines web and Semantic Web standards including RDF, OWL, SHACL, and SPARQL.         | —                                                             |
| WAF      | Web Application Firewall                     | AWS layer 7 firewall that filters HTTP requests by IP, geo, rate, or custom rules.                                       | [note](cloud/aws/networking/05_aws_waf.md)                    |
| WSL      | Windows Subsystem for Linux                  | Windows feature that runs a Linux environment natively without a VM.                                                     | [note](tooling/01_wsl_terminal_and_vscode.md)                 |
| YoY      | Year over Year                               | Comparison of a metric against the same period in the prior year, expressed as a percentage change.                      | —                                                             |

---
↑ [Home](home.md)
