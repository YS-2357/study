# AWS Fargate - AWS Console Guide

## Official Documentation
- [AWS Fargate on ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html)
- [AWS Fargate on EKS](https://docs.aws.amazon.com/eks/latest/userguide/fargate.html)
- [AWS Fargate FAQs](https://aws.amazon.com/fargate/faqs/)

## What It Is
AWS Fargate is a serverless compute engine for containers. You define your container and resource requirements — Fargate handles the underlying servers.

**The problem it solves:**
- You want to run containers (Docker) but don't want to manage EC2 instances
- No patching, no capacity planning, no cluster scaling to worry about
- You just define CPU, memory, and your container image — Fargate runs it

**How it fits:**
```
You build container image → Push to ECR → Define task (CPU/memory) → Fargate runs it
                                                                      (no EC2 to manage)
```

Fargate is a **launch type**, not a standalone service. It works with:
- **Amazon ECS** (Elastic Container Service) — AWS-native container orchestration
- **Amazon EKS** (Elastic Kubernetes Service) — Managed Kubernetes

### Fargate vs EC2 vs Lambda

| | Fargate | EC2 | Lambda |
|---|---|---|---|
| Unit of work | Container task | Server instance | Function invocation |
| Server management | None | You manage | None |
| Max runtime | No limit | No limit | 15 minutes |
| Startup time | Seconds (~30s) | Minutes | Milliseconds (warm) |
| Pricing | Per vCPU + memory per second | Per instance-hour | Per request + duration |
| Best for | Containerized apps, microservices | Full server control, GPU, persistent workloads | Event-driven, short tasks |
| Scaling | Task-level auto scaling | Instance-level auto scaling | Automatic per request |

**Rule of thumb:**
- Already containerized or want containers → **Fargate**
- Need server access, GPUs, or specific OS config → **EC2**
- Short event-driven functions (<15 min) → **Lambda**

## Console Access
- Search "ECS" in AWS Console
- Amazon ECS > Clusters > Create cluster (select Fargate)
- Or: Task Definitions > Create (select Fargate launch type)

---

## Key Concepts

### Task Definition
The blueprint for your container(s):
- **Container image** — Docker image from ECR, Docker Hub, etc.
- **CPU and memory** — Fixed combinations (e.g., 0.25 vCPU / 0.5 GB, up to 16 vCPU / 120 GB)
- **Task role** — IAM role the container uses to call AWS services
- **Execution role** — IAM role ECS uses to pull images and write logs
- **Networking** — Fargate tasks always use `awsvpc` mode (each task gets its own ENI)

### CPU/Memory Combinations
Fargate has fixed valid combinations:

| CPU (vCPU) | Memory options (GB) |
|---|---|
| 0.25 | 0.5, 1, 2 |
| 0.5 | 1, 2, 3, 4 |
| 1 | 2, 3, 4, 5, 6, 7, 8 |
| 2 | 4–16 (1 GB increments) |
| 4 | 8–30 (1 GB increments) |
| 8 | 16–60 (4 GB increments) |
| 16 | 32–120 (8 GB increments) |

### Service vs Task
- **Task** — A single running instance of a task definition (like running a container once)
- **Service** — Maintains a desired count of tasks, integrates with load balancers, handles rolling deployments

### Networking
- Every Fargate task gets its own ENI (Elastic Network Interface) with a private IP
- Tasks can run in public or private subnets
- Use security groups to control traffic per task
- **Best practice:** Run in private subnets, use ALB/NLB for ingress

---

## Precautions

### ⚠️ MAIN PRECAUTION: Fargate Can Be More Expensive Than EC2 at Scale
- Fargate per-vCPU pricing is higher than equivalent EC2 On-Demand
- At steady high utilization, EC2 with Reserved Instances or Savings Plans is cheaper
- Fargate wins on operational simplicity and variable workloads
- Calculate break-even point for your workload

### 1. Right-size Tasks
- Don't over-provision CPU/memory — you pay for what you allocate, not what you use
- Monitor actual usage with CloudWatch Container Insights
- Adjust task definitions based on real metrics

### 2. Networking Setup
- Fargate requires VPC, subnets, and security groups
- Tasks in public subnets need `assignPublicIp: ENABLED` to pull images from ECR
- Better pattern: private subnets + NAT Gateway or VPC endpoints for ECR/S3/CloudWatch

### 3. Image Pull Time
- Large container images = slower startup
- Use multi-stage builds to minimize image size
- Use ECR in the same region as your Fargate tasks

### 4. Logging
- Configure `awslogs` log driver to send container logs to CloudWatch
- Without this, you have no visibility into container output
- Set log retention to avoid unbounded CloudWatch costs

### 5. Always Use Tags
- Tag task definitions, services, and clusters with environment, project, team, cost center
- Essential for MSP cost tracking — container costs spread across many small tasks can be hard to attribute
