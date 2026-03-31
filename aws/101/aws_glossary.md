# AWS 101 Glossary

This glossary organizes terms found across:
- `aws/101/aws_services/`

Each entry includes:
- English term
- Korean term
- English description
- Korean description

Validation note:
- AWS service names and service descriptions were checked against official AWS docs at AWS 101 level.
- Generic industry terms such as `API`, `TCP`, `UDP`, `HTTP`, and `SQL` were kept as beginner-friendly standard definitions because they are not AWS-owned terms.

## 1. Core Cloud Concepts

| English | Korean | English Description | Korean Description |
| --- | --- | --- | --- |
| AWS | 아마존 웹 서비스 | Amazon's cloud platform that provides infrastructure and many managed services. | 인프라와 다양한 관리형 서비스를 제공하는 아마존의 클라우드 플랫폼이다. |
| AWS 101 | AWS 101 | A beginner-level introduction to core AWS concepts and services. | AWS 핵심 개념과 서비스를 소개하는 입문 수준의 학습 범위이다. |
| Cloud Computing | 클라우드 컴퓨팅 | Using IT resources over the internet on demand and paying based on usage. | 인터넷을 통해 IT 자원을 필요할 때 사용하고 사용량에 따라 비용을 지불하는 방식이다. |
| On-Premises | 온프레미스 | Running infrastructure in your own physical data center or server room. | 자체 데이터센터나 서버실에서 인프라를 직접 운영하는 방식이다. |
| CAPEX | 자본적 지출 | Upfront spending on assets such as servers, networks, and data centers. | 서버, 네트워크, 데이터센터 같은 자산에 대해 처음에 크게 지출하는 비용이다. |
| OPEX | 운영비용 | Ongoing operational spending such as monthly cloud usage or maintenance. | 월별 클라우드 사용료나 운영 유지비처럼 지속적으로 발생하는 비용이다. |
| Scalability | 확장성 | The ability to increase or decrease resources to match demand. | 수요에 맞춰 자원을 늘리거나 줄일 수 있는 능력이다. |
| Elasticity | 탄력성 | The ability to scale resources up and down quickly as traffic changes. | 트래픽 변화에 따라 자원을 빠르게 확장하거나 축소할 수 있는 특성이다. |
| Availability | 가용성 | The ability of a system or service to remain accessible and usable. | 시스템이나 서비스가 계속 접근 가능하고 사용 가능한 상태를 유지하는 특성이다. |
| High Availability | 고가용성 | An architecture designed to reduce service interruption and improve resilience. | 서비스 중단을 줄이고 복원력을 높이도록 설계된 아키텍처 개념이다. |
| Latency | 지연시간 | The time it takes for a request or response to travel across a system or network. | 요청이나 응답이 시스템 또는 네트워크를 통해 전달되는 데 걸리는 시간이다. |
| Managed Service | 관리형 서비스 | A service where AWS operates much of the underlying infrastructure for you. | AWS가 하위 인프라의 많은 부분을 대신 운영해주는 서비스이다. |
| Serverless | 서버리스 | A model where you use compute or other services without managing servers directly. | 서버를 직접 운영하지 않고 컴퓨팅이나 기타 서비스를 사용하는 모델이다. |
| Shared Responsibility Model | 책임 공유 모델 | AWS secures the cloud infrastructure, while customers secure what they run in the cloud. | AWS는 클라우드 자체를 보호하고, 고객은 클라우드 위의 설정과 데이터, 접근 제어를 보호하는 모델이다. |

## 2. Global Infrastructure and Networking

| English | Korean | English Description | Korean Description |
| --- | --- | --- | --- |
| Region | 리전 | A separate geographic area where AWS clusters infrastructure and services. | AWS 인프라와 서비스가 배치되는 독립된 지리적 영역이다. |
| Availability Zone (AZ) | 가용 영역 | An isolated location within a Region for high availability. | 리전 안에서 고가용성을 위해 분리된 독립 인프라 위치이다. |
| Global Infrastructure | 글로벌 인프라 | AWS's worldwide network of regions, Availability Zones, and edge locations. | 전 세계에 분포한 AWS의 리전, 가용 영역, 엣지 로케이션 전체를 뜻한다. |
| Point of Presence (PoP) | 엣지 거점, 접속 지점 | An edge location used to deliver content closer to users. | 사용자와 가까운 위치에서 콘텐츠를 전달하기 위한 엣지 거점이다. |
| VPC (Virtual Private Cloud) | 가상 사설 클라우드 | A logically isolated virtual network in AWS. | AWS 안에서 논리적으로 분리된 가상 네트워크이다. |
| Subnet | 서브넷 | A range of IP addresses inside a VPC. | VPC 내부에서 나뉜 IP 주소 범위이다. |
| CIDR | CIDR 표기법 | A way to define IP address ranges for networks and subnets. | 네트워크와 서브넷의 IP 주소 범위를 표현하는 방식이다. |
| IPv4 | IPv4 | The most widely used 32-bit internet address format. | 가장 널리 사용되는 32비트 인터넷 주소 체계이다. |
| IPv6 | IPv6 | A newer address format with a much larger address space than IPv4. | IPv4보다 훨씬 큰 주소 공간을 제공하는 새로운 인터넷 주소 체계이다. |
| IP Address | IP 주소 | A network address assigned to a device or resource. | 장치나 자원에 할당되는 네트워크 주소이다. |
| Public Subnet | 퍼블릭 서브넷 | A subnet whose resources can reach or be reached from the internet through routing. | 라우팅을 통해 인터넷과 직접 연결될 수 있는 자원이 위치한 서브넷이다. |
| Private Subnet | 프라이빗 서브넷 | A subnet whose resources are not directly exposed to the internet. | 인터넷에 직접 노출되지 않는 자원이 위치한 서브넷이다. |
| Route Table | 라우트 테이블 | A set of routing rules that controls where network traffic is directed. | 네트워크 트래픽이 어디로 가는지 결정하는 라우팅 규칙 집합이다. |
| Internet Gateway | 인터넷 게이트웨이 | A VPC component that allows communication between a VPC and the internet. | VPC와 인터넷 간 통신을 가능하게 하는 VPC 구성 요소이다. |
| NAT Gateway | NAT 게이트웨이 | A managed service that lets private subnet resources access the internet outbound. | 프라이빗 서브넷 자원이 외부 인터넷으로 나가도록 해주는 관리형 서비스이다. |
| Security Group | 보안 그룹 | A virtual firewall that controls inbound and outbound traffic to AWS resources. | AWS 자원에 대한 인바운드와 아웃바운드 트래픽을 제어하는 가상 방화벽이다. |
| ACL / Network ACL | ACL / 네트워크 ACL | A subnet-level traffic filter that allows or denies traffic by rule. | 규칙에 따라 트래픽을 허용하거나 차단하는 서브넷 단위 필터이다. |
| DNS | DNS | A system that translates domain names into IP addresses. | 도메인 이름을 IP 주소로 변환하는 시스템이다. |
| Route 53 | Route 53 | AWS's managed DNS and domain routing service. | AWS의 관리형 DNS 및 도메인 라우팅 서비스이다. |
| TCP | TCP | A reliable network protocol used for ordered and checked data delivery. | 순서 보장과 오류 확인이 가능한 신뢰성 중심의 네트워크 프로토콜이다. |
| UDP | UDP | A lightweight network protocol that prioritizes speed over guaranteed delivery. | 전달 보장보다 속도를 우선하는 가벼운 네트워크 프로토콜이다. |
| HTTP | HTTP | A protocol used to transfer web requests and responses. | 웹 요청과 응답을 주고받는 데 사용되는 프로토콜이다. |
| HTTPS | HTTPS | HTTP secured with encryption for safer web communication. | 암호화를 적용해 더 안전하게 만든 HTTP 통신 방식이다. |
| SSL/TLS | SSL/TLS | Encryption protocols used to secure network communication. | 네트워크 통신을 안전하게 보호하는 암호화 프로토콜이다. |
| ALB (Application Load Balancer) | 애플리케이션 로드 밸런서 | A load balancer that routes HTTP and HTTPS traffic to targets. | HTTP와 HTTPS 트래픽을 대상으로 분산하는 로드 밸런서이다. |
| Load Balancer | 로드 밸런서 | A service that distributes incoming traffic across multiple targets. | 들어오는 트래픽을 여러 대상에 분산시키는 서비스이다. |

## 3. Compute

| English | Korean | English Description | Korean Description |
| --- | --- | --- | --- |
| Amazon EC2 | 아마존 EC2 | A service that provides scalable virtual servers called instances. | 인스턴스라고 부르는 확장 가능한 가상 서버를 제공하는 서비스이다. |
| Elastic Compute Cloud | 엘라스틱 컴퓨트 클라우드 | The full name of Amazon EC2. | Amazon EC2의 풀네임이다. |
| Instance | 인스턴스 | A virtual server running in AWS. | AWS에서 실행되는 가상 서버이다. |
| AMI (Amazon Machine Image) | AMI, 머신 이미지 | A template used to launch EC2 instances with an OS and software configuration. | OS와 소프트웨어 구성이 포함된 EC2 인스턴스 시작용 템플릿이다. |
| Instance Family | 인스턴스 패밀리 | A category of EC2 instance types optimized for certain workload patterns. | 특정 워크로드에 맞게 최적화된 EC2 인스턴스 유형 분류이다. |
| On-Demand | 온디맨드 | A pricing model where you pay for compute usage without long-term commitment. | 장기 약정 없이 사용한 컴퓨팅만큼 비용을 지불하는 방식이다. |
| Reserved Instance (RI) | 예약 인스턴스 | A pricing benefit for committing to a certain level of usage over time. | 일정 사용량을 장기간 약정해 비용을 절감하는 구매 방식이다. |
| Savings Plans | 세이빙 플랜 | A flexible pricing model that offers lower cost in exchange for a usage commitment. | 일정 사용량 약정을 통해 비용 할인을 제공하는 유연한 요금 모델이다. |
| Spot Instance | 스팟 인스턴스 | Spare AWS compute capacity offered at discounted prices with interruption risk. | 중단 가능성이 있지만 할인된 가격으로 제공되는 여유 컴퓨팅 자원이다. |
| Auto Scaling | 오토 스케일링 | Automatic scaling of EC2 capacity based on conditions you define. | 사용자가 정한 조건에 따라 EC2 용량을 자동으로 늘리거나 줄이는 기능이다. |
| Amazon EC2 Auto Scaling | 아마존 EC2 오토 스케일링 | A service that helps ensure you have the correct number of EC2 instances available for your application load. | 애플리케이션 부하를 처리할 수 있도록 적절한 수의 EC2 인스턴스를 유지하게 도와주는 서비스이다. |
| AWS Lambda | AWS 람다 | A compute service that runs code without provisioning or managing servers. | 서버를 직접 준비하거나 관리하지 않고 코드를 실행할 수 있는 컴퓨팅 서비스이다. |
| Event Source | 이벤트 소스 | A service or action that triggers a Lambda function or workflow. | Lambda 함수나 워크플로를 실행시키는 서비스나 이벤트이다. |
| Cold Start | 콜드 스타트 | Extra startup latency when a serverless function runs in a new execution environment. | 서버리스 함수가 새로운 실행 환경에서 시작될 때 발생하는 추가 지연이다. |
| AWS Fargate | AWS 파게이트 | A serverless, pay-as-you-go compute engine for containers. | 컨테이너를 위한 서버리스, 사용량 기반 컴퓨팅 엔진이다. |
| Amazon ECS | 아마존 ECS | AWS's container orchestration service for running Docker-style containers. | 컨테이너를 실행하고 관리하는 AWS의 컨테이너 오케스트레이션 서비스이다. |
| Amazon EKS | 아마존 EKS | AWS's managed Kubernetes service. | AWS의 관리형 쿠버네티스 서비스이다. |
| Container | 컨테이너 | A packaged application unit that includes code and runtime dependencies. | 코드와 실행 의존성을 함께 담아 배포하는 애플리케이션 단위이다. |
| Virtual Machine | 가상 머신 | A software-based computer that behaves like a physical machine. | 물리 서버처럼 동작하는 소프트웨어 기반 컴퓨터이다. |
| OS (Operating System) | 운영체제 | The core software layer that manages hardware and system resources. | 하드웨어와 시스템 자원을 관리하는 핵심 소프트웨어 계층이다. |
| CPU | CPU | The processor resource used for computation. | 계산 처리를 담당하는 프로세서 자원이다. |
| GPU | GPU | A processor optimized for graphics and parallel workloads such as AI training. | 그래픽 처리와 AI 학습 같은 병렬 작업에 최적화된 프로세서이다. |
| RAM / Memory | 메모리 | Short-term working memory used by running programs. | 실행 중인 프로그램이 사용하는 단기 작업 메모리이다. |

## 4. Storage and Content Delivery

| English | Korean | English Description | Korean Description |
| --- | --- | --- | --- |
| Amazon S3 | 아마존 S3 | An object storage service for storing and protecting data. | 데이터를 저장하고 보호하는 객체 스토리지 서비스이다. |
| Simple Storage Service | 심플 스토리지 서비스 | The full name of Amazon S3. | Amazon S3의 풀네임이다. |
| Bucket | 버킷 | A top-level container for objects stored in Amazon S3. | Amazon S3에서 객체를 담는 최상위 저장 단위이다. |
| Object Storage | 객체 스토리지 | A storage model that stores data as objects rather than blocks or filesystems. | 데이터를 블록이나 파일시스템이 아니라 객체 단위로 저장하는 방식이다. |
| Amazon EBS | 아마존 EBS | A scalable block storage service mainly used with EC2. | 주로 EC2와 함께 사용하는 확장형 블록 스토리지 서비스이다. |
| Block Storage | 블록 스토리지 | Storage presented as disk volumes for servers or operating systems. | 서버나 운영체제에 디스크 볼륨처럼 제공되는 저장 방식이다. |
| Snapshot | 스냅샷 | A point-in-time backup copy of a storage volume or resource. | 스토리지 볼륨이나 자원의 특정 시점 백업 복사본이다. |
| Amazon CloudFront | 아마존 클라우드프런트 | A CDN service that securely delivers content with low latency. | 콘텐츠를 낮은 지연으로 안전하게 전달하는 CDN 서비스이다. |
| CDN (Content Delivery Network) | 콘텐츠 전송 네트워크 | A distributed network that delivers content from locations closer to users. | 사용자와 가까운 위치에서 콘텐츠를 전달하는 분산 네트워크이다. |
| Cache | 캐시 | Temporary storage used to serve repeated requests faster. | 반복 요청을 더 빠르게 처리하기 위해 사용하는 임시 저장 공간이다. |
| TTL (Time to Live) | TTL, 캐시 유지 시간 | The time a cached object stays valid before refresh. | 캐시된 객체가 새로고침되기 전까지 유효한 시간이다. |
| Amazon Glacier / S3 Glacier | 아마존 글레이셔 / S3 글레이셔 | Low-cost archival storage designed for long-term retention. | 장기 보관을 위한 저비용 아카이브 스토리지이다. |
| S3 Standard | S3 스탠더드 | The standard storage class for frequently accessed S3 objects. | 자주 접근하는 S3 객체를 위한 기본 스토리지 클래스이다. |
| S3-IA | S3-IA, 저빈도 접근 | An S3 storage class for infrequently accessed data that still needs fast retrieval. | 자주 접근하지 않지만 빠른 조회가 필요한 데이터를 위한 S3 스토리지 클래스이다. |

## 5. Databases, Analytics, and AI

| English | Korean | English Description | Korean Description |
| --- | --- | --- | --- |
| Amazon RDS | 아마존 RDS | A managed service for setting up, operating, and scaling relational databases. | 관계형 데이터베이스를 쉽게 설정, 운영, 확장할 수 있게 해주는 관리형 서비스이다. |
| Relational Database Service | 릴레이셔널 데이터베이스 서비스 | The full name of Amazon RDS. | Amazon RDS의 풀네임이다. |
| Amazon Aurora | 아마존 오로라 | A fully managed relational database engine compatible with MySQL and PostgreSQL. | MySQL과 PostgreSQL과 호환되는 완전관리형 관계형 데이터베이스 엔진이다. |
| Amazon DynamoDB | 아마존 다이나모DB | A serverless, fully managed, distributed NoSQL database service. | 서버리스이며 완전관리형이고 분산 구조를 가진 NoSQL 데이터베이스 서비스이다. |
| NoSQL | NoSQL | A non-relational database model often optimized for scale and flexible schemas. | 보통 대규모 확장과 유연한 스키마에 맞게 설계된 비관계형 데이터베이스 모델이다. |
| SQL | SQL | A language used to query and manage relational databases. | 관계형 데이터베이스를 조회하고 관리하는 데 쓰는 언어이다. |
| MySQL | 마이SQL | A popular open-source relational database engine. | 널리 사용되는 오픈소스 관계형 데이터베이스 엔진이다. |
| PostgreSQL | 포스트그레SQL | A powerful open-source relational database engine. | 기능이 강력한 오픈소스 관계형 데이터베이스 엔진이다. |
| Amazon ElastiCache | 아마존 엘라스티캐시 | A managed in-memory data store and cache service. | 관리형 인메모리 데이터 저장소 및 캐시 서비스이다. |
| Redis | 레디스 | A popular in-memory data store often used for caching or fast data access. | 캐싱이나 빠른 데이터 접근에 자주 쓰이는 인메모리 데이터 저장소이다. |
| Amazon Redshift | 아마존 레드시프트 | A fully managed data warehouse service for large-scale analytics. | 대규모 분석을 위한 완전관리형 데이터 웨어하우스 서비스이다. |
| Data Warehouse | 데이터 웨어하우스 | A database system optimized for analytics, reporting, and large-scale aggregation. | 분석, 리포팅, 대규모 집계에 최적화된 데이터베이스 시스템이다. |
| OLTP | OLTP, 온라인 트랜잭션 처리 | A workload pattern optimized for frequent transactional operations. | 빈번한 거래성 작업에 최적화된 데이터 처리 방식이다. |
| ETL | ETL | Extract, Transform, Load; the process of moving and reshaping data for analysis. | 데이터를 추출하고 변환한 뒤 적재하는 분석용 데이터 처리 과정이다. |
| Amazon EMR | 아마존 EMR | A managed cluster platform for running big data frameworks such as Hadoop and Spark. | Hadoop, Spark 같은 빅데이터 프레임워크를 실행하는 관리형 클러스터 플랫폼이다. |
| Hadoop | 하둡 | A framework for distributed storage and processing of large datasets. | 대규모 데이터를 분산 저장하고 처리하기 위한 프레임워크이다. |
| Spark | 스파크 | A fast distributed processing engine for big data workloads. | 빅데이터 워크로드를 위한 빠른 분산 처리 엔진이다. |
| AWS Data Pipeline | AWS 데이터 파이프라인 | A service for moving and processing data between AWS services and other sources. | AWS 서비스와 기타 소스 간에 데이터를 이동하고 처리하는 서비스이다. |
| Amazon Kinesis | 아마존 키네시스 | A service family for collecting, processing, and analyzing real-time streaming data. | 실시간 스트리밍 데이터를 수집, 처리, 분석하는 서비스 계열이다. |
| Streaming Data | 스트리밍 데이터 | Data that arrives continuously and is processed in near real time. | 지속적으로 들어오며 거의 실시간으로 처리되는 데이터이다. |
| Amazon SageMaker AI | 아마존 세이지메이커 AI | A fully managed machine learning service for building, training, and deploying ML models. | 머신러닝 모델을 구축, 학습, 배포할 수 있는 완전관리형 머신러닝 서비스이다. |
| ML (Machine Learning) | 머신러닝 | A method where systems learn patterns from data to make predictions or decisions. | 데이터에서 패턴을 학습해 예측이나 판단을 수행하는 기술이다. |
| Model Endpoint | 모델 엔드포인트 | A deployed network endpoint used to serve ML model predictions. | 배포된 ML 모델의 예측 결과를 제공하는 네트워크 엔드포인트이다. |
| Amazon QuickSight | 아마존 퀵사이트 | AWS's business intelligence service for dashboards and analytics visualization. | 대시보드와 분석 시각화를 위한 AWS의 BI 서비스이다. |
| AWS Glue | AWS 글루 | AWS's managed data integration and ETL service. | 데이터 통합과 ETL을 위한 AWS의 관리형 서비스이다. |
| Step Functions | 스텝 펑션스 | AWS's workflow orchestration service for coordinating multiple steps and services. | 여러 단계와 서비스를 연결하는 AWS의 워크플로 오케스트레이션 서비스이다. |

## 6. Security and Access

| English | Korean | English Description | Korean Description |
| --- | --- | --- | --- |
| Amazon IAM | 아마존 IAM | A web service that securely controls access to AWS resources. | AWS 자원에 대한 접근을 안전하게 제어하는 웹 서비스이다. |
| Identity Access Management | 아이덴티티 및 접근 관리 | The full name of IAM. | IAM의 풀네임이다. |
| IAM Role | IAM 역할 | A set of permissions that can be assumed by users or AWS services. | 사용자나 AWS 서비스가 맡아서 사용할 수 있는 권한 집합이다. |
| IAM Policy | IAM 정책 | A JSON document that defines what actions are allowed or denied. | 어떤 작업을 허용하거나 거부할지 정의하는 JSON 문서이다. |
| Least Privilege | 최소 권한 원칙 | Giving only the minimum permissions required to perform a task. | 작업 수행에 필요한 최소한의 권한만 부여하는 원칙이다. |
| AWS Shield | AWS 쉴드 | A managed service that protects AWS resources against DDoS attacks. | AWS 자원을 DDoS 공격으로부터 보호하는 관리형 서비스이다. |
| AWS Shield Standard | AWS 쉴드 스탠다드 | The basic DDoS protection included automatically for supported AWS services. | 지원되는 AWS 서비스에 자동 포함되는 기본 DDoS 보호 기능이다. |
| AWS WAF | AWS WAF | A web application firewall that monitors and controls HTTP(S) requests. | HTTP(S) 요청을 모니터링하고 제어하는 웹 애플리케이션 방화벽이다. |
| DDoS | 디도스, 분산 서비스 거부 공격 | An attack that overwhelms a service with large volumes of traffic. | 대량의 트래픽으로 서비스를 마비시키려는 공격이다. |
| Web ACL | 웹 ACL | A set of WAF rules that determines how web requests are handled. | 웹 요청을 어떻게 처리할지 결정하는 WAF 규칙 집합이다. |
| Encryption | 암호화 | Protecting data by converting it into a form that requires a key to read. | 데이터를 키 없이는 읽을 수 없도록 변환해 보호하는 방식이다. |
| Certificate | 인증서 | A digital credential used to enable secure HTTPS communication. | 안전한 HTTPS 통신을 가능하게 하는 디지털 자격 정보이다. |

## 7. Service Integrations and Supporting Terms

| English | Korean | English Description | Korean Description |
| --- | --- | --- | --- |
| API | API | An interface that allows software systems to communicate with each other. | 소프트웨어 시스템끼리 서로 통신하게 해주는 인터페이스이다. |
| Amazon API Gateway | 아마존 API 게이트웨이 | A managed service for creating, publishing, and protecting APIs. | API를 생성, 게시, 보호하는 관리형 서비스이다. |
| ARN | ARN | A unique AWS resource name used to identify resources across services. | AWS 자원을 식별하기 위해 사용하는 고유한 이름 형식이다. |
| AWS CLI | AWS CLI | A command-line tool used to manage AWS resources. | AWS 자원을 관리하는 명령줄 도구이다. |
| SDK | SDK | A software development kit used to build applications against an API or platform. | 특정 API나 플랫폼용 애플리케이션을 만들기 위한 개발 도구 모음이다. |
| Amazon CloudWatch | 아마존 클라우드워치 | AWS's monitoring and observability service. | 모니터링과 관측성을 위한 AWS 서비스이다. |
| CloudFormation | 클라우드포메이션 | AWS service for defining infrastructure as code. | 인프라를 코드로 정의하는 AWS 서비스이다. |
| ECR (Elastic Container Registry) | ECR, 컨테이너 레지스트리 | AWS's container image registry service. | 컨테이너 이미지를 저장하고 관리하는 AWS 서비스이다. |
| JSON | 제이슨 | A text format commonly used to represent structured data. | 구조화된 데이터를 표현할 때 자주 사용하는 텍스트 형식이다. |
| CSV | CSV | A simple text format for tabular data separated by commas. | 쉼표로 구분된 표 형식 데이터를 위한 간단한 텍스트 형식이다. |
| URL | URL | The address used to access a web resource. | 웹 자원에 접근할 때 사용하는 주소이다. |
| I/O | 입출력 | Input and output operations between software, memory, network, or storage. | 소프트웨어, 메모리, 네트워크, 스토리지 사이에서 발생하는 입력과 출력 작업이다. |
| Throughput | 처리량 | The amount of work or data processed in a given time. | 일정 시간 동안 처리되는 작업량이나 데이터 양이다. |

## 8. Related AWS Services Mentioned in the Docs

| English | Korean | English Description | Korean Description |
| --- | --- | --- | --- |
| AWS Organizations | AWS 오가니제이션즈 | A service for centrally managing multiple AWS accounts. | 여러 AWS 계정을 중앙에서 관리하는 서비스이다. |
| Amazon SQS | 아마존 SQS | A managed message queue service for decoupling systems. | 시스템 간 결합을 낮추기 위한 관리형 메시지 큐 서비스이다. |
| Amazon SNS | 아마존 SNS | A managed pub/sub messaging service for notifications and fan-out delivery. | 알림과 팬아웃 전달을 위한 관리형 발행/구독 메시징 서비스이다. |
| IoT | 사물인터넷 | Connected devices that generate and exchange data over networks. | 네트워크를 통해 데이터를 주고받는 연결된 장치 환경이다. |
| AWS Global Accelerator | AWS 글로벌 액셀러레이터 | A service that improves path performance to applications using the AWS global network. | AWS 글로벌 네트워크를 이용해 애플리케이션까지의 경로 성능을 높이는 서비스이다. |

## 9. Reading Tips

- If a term is a service name, first remember `what problem it solves`.
- If a term is an acronym, remember both the full name and the category it belongs to.
- If two terms are often confused, compare them by:
  - what you manage
  - how cost happens
  - whether they are for compute, storage, database, network, or security

## 10. Official AWS Docs Used For Final Validation

- Amazon EC2: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html
- Amazon EC2 Auto Scaling: https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html
- AWS Lambda: https://docs.aws.amazon.com/lambda/latest/dg/welcome.html
- Amazon S3: https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html
- Amazon VPC: https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html
- AWS Regions and Availability Zones: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions-availability-zones.html
- Amazon RDS: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html
- Amazon Aurora: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html
- Amazon DynamoDB: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html
- Amazon ElastiCache: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html
- Amazon Redshift: https://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html
- Amazon EMR: https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html
- Amazon Kinesis Data Streams: https://docs.aws.amazon.com/streams/latest/dev/introduction.html
- Amazon SageMaker AI: https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html
- AWS WAF: https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html
- AWS Shield: https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html
