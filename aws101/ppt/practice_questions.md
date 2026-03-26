# AWS 101 Practice Questions Arranged

Source files:
- `260318_practice.md`
- `260319_practice.md`
- `practice_hjp.md`
- `practice_khj.md`

## Cloud Basics and Migration
- 클라우드로 마이그레이션하면 인프라 운영이 불필요한데 기존 인프라 운영 인력 활용은 어떻게 해야 하나요?
- 클라우드 환경에서 서비스를 많이 운영하다보면 온프레미스 대비해서 비용이 더 증가하지 않나요?
- KT 직원 교육 AIVLE 서비스가 온프레미스 환경인데 AWS로 마이그레이션하고 싶습니다. 어떤 방식으로 접근하면 되나요?
- ISMS를 온프레미스에서 인증받았을 경우 클라우드에서도 인증을 따로 받아야 하나요?

## Cloud Service Models and Shared Responsibility
- ~~Lambda는 SaaS인가요, IaaS인가요, PaaS인가요?~~
- ~~Lambda는 PaaS인가요?~~
- ~~S3는 PaaS 서비스인가요?~~
- 클라우드의 공동 책임 모델은 어떻게 이해하면 되나요?
- ~~AWS 공동 책임 모델을 IaaS, PaaS, SaaS와 함께 설명하면 어떻게 되나요?~~
- 책임공유모델을 제대로 이해해야 IAM을 설명할 수 있는데, 여기서 애플리케이션은 정확히 무엇을 말하나요?
- IAM 책임공유모델에서 클라우드를 IDC에 비유하고 user로 비유한다면 어떻게 설명할 수 있나요?

## Global Infrastructure
- 가용영역은 무엇인가요?
- 중국 리전이 존재하나요?
- 중국 리전에서 글로벌 리전과 동일하게 서비스를 그대로 사용할 수 있나요?

## EC2
- 서비스 운영 중 EC2 인스턴스 타입 변경은 어떻게 하면 되나요?
- EC2 인스턴스 타입 중 T 시리즈의 버스팅이 무엇인가요?
- EC2에서 비용을 인스턴스 비용만 지출하면 되는 건가요?
- 포스코에서 EC2를 쓰고 있는데 Spot Instance를 제 케이스에 그냥 사용해도 되나요?
- Spot Instance를 프로덕션 환경에서도 사용해도 되나요?
- EC2의 과금 옵션 중 Spot Instance가 뭔가요?
- Spot Instance는 어디서 가져오는 건가요?
- 제 계정에 EC2 instance를 여러 개 돌리고 있는데, Spot Instance 사용에 문제는 없을까요?
- Spot Instance랑 Reserved Instance의 차이가 뭔가요?

## Auto Scaling
- 오토스케일링은 어떤 지표를 기준으로 설정 가능한가요?
- 오토스케일링 옵션은 어떤 것들이 있나요?
- EC2 서버 오토스케일링 시 EC2는 어떤 방식으로 복제되는 건가요?
- Auto Scaling은 EC2의 집합인가요?
- Auto Scaling Group에 NLB 같은 로드밸런서가 기본적으로 붙어 있나요?
- 오토스케일링 사용 중인데 서버나 앱이 바뀌어서 Launch Template도 중간에 바꿔야 합니다. 이 경우 어떻게 적용하나요?
- Auto Scaling은 몇 개까지 두고, 어떻게 모니터링하나요?

## Lambda
- Lambda에서 private 네트워크에 있는 DB 연결 가능한가요?
- Lambda를 VPC 안에서 사용할 수 있나요?
- Lambda의 제약은 무엇인가요?
- Lambda에 코드는 무엇을 어떻게 올리면 되나요?

## Storage
- S3는 버킷인가요, 아니면 S3 안에 버킷이 있는 구조인가요?
- S3 11 nines는 무슨 뜻인가요?
- S3 버킷별로 성능 차이가 있나요?
- 공문서를 장기 저장하고 거의 접근하지 않는 경우 어떤 스토리지를 쓰는 게 맞나요?
- 저장할 문서가 너무 많은데 온프레미스 저장소를 클라우드로 어떻게 옮겨야 하나요?
- Deep Archive와 Glacier는 어떤 경우에 선택하나요?

## Block and File Storage
- EBS는 EKS에도 붙나요?
- EBS는 ECS에도 붙나요?
- 온프레미스 파일 시스템을 AWS와 연동하려면 어떻게 해야 하나요?
- EFS는 Linux용이고 Windows 파일 공유는 어떤 서비스를 써야 하나요?
- 온프레미스와 AWS 파일 시스템 연동 시 VPN, Direct Connect, Transit Gateway는 각각 어떤 상황에서 쓰나요?

## Networking Basics
- AWS VPC 내에서 리소스들은 서로 어떻게 연결되나요?
- 서브넷 개념은 무엇인가요?
- IGW와 NAT Gateway의 차이는 무엇인가요?
- Direct Connect, VPN, Transit Gateway의 차이는 무엇인가요?
- Security Group과 Network ACL의 차이는 무엇인가요?
- NACL이 뭔가요?
- NAT가 뭐죠? IGW와 뭐가 다른가요?
- Private 서브넷이 왜 필요한가요? 그냥 편하게 public 서브넷만 만들어두면 안되나요?
- public 서브넷이 인터넷과 연결 가능해지기 위해서 필수적인 요소가 뭔가요?

## Load Balancing and Content Delivery
- Load Balancer 중 ALB, NLB, GWLB는 각각 어느 상황에서 사용하나요?
- ELB에서 IP를 사용하고 싶을 때는 어떤 것을 선택해야 하나요?
- ALB에 인증서를 붙이고 싶을 때는 어떻게 하나요?
- CloudFront는 어떤 역할을 하나요?
- CloudFront는 저희 캐시 전송 요구사항에 어떻게 맞나요?

## Databases
- Semi-structured 데이터에는 어떤 DB를 써야 하나요?
- RDS와 Aurora는 어떤 차이점이 있나요?
- RDB와 RDS의 차이점은 무엇인가요?
- RDS Multi-AZ와 Aurora 기능은 어떻게 정확히 비교하나요?
- RDS Read Replica와 Aurora는 성능 면에서 어떻게 다른가요?
- DynamoDB를 써야 하는지, RDB를 써야 하는지 어떻게 판단하나요?
- 아이 band 데이터 사업에서 경도, 위도, 날씨 같은 telemetry/log 값은 어떤 DB에 넣는 것이 좋나요?
- 아이들의 나이, 이름, 성별 같은 정형 데이터는 어디에 넣는 것이 좋나요?
- AWS Aurora와 AWS RDS의 차이가 뭔가요?
- DynamoDB의 프로비저닝 모드와 온디멘드 모드는 어느 상황에서 쓰면 되나요?

## Caching
- ElastiCache는 어떤 상황에서 사용하나요?

## IAM and Access Control
- IAM의 user, group, role, policy는 각각 무엇인가요?
- 실제 고객사가 애플리케이션을 구축한다고 가정했을 때 IAM으로 어디까지 컨트롤이 가능한가요?

## Security
- Shield는 도메인 서비스인가요?
- Shield와 Route 53은 어떤 관계인가요?
- WAF와 AWS 방화벽 서비스는 어떻게 다른가요?
- AWS에 방화벽 서비스가 있나요?
- WAF와 Shield Advanced는 DDoS를 막는 방식이 어떻게 다른가요?
- WAF의 허용/차단 그룹은 무엇인가요?
- WAF는 whitelist 방식으로 설명하면 되나요?
- WAF 규칙 수에 최대가 있다면 그 이상은 설정할 수 없나요?
- 온프레미스에서 사용한 WAF 설정을 그대로 AWS에서도 사용할 수 있나요?
- WAF에 기본 템플릿이 제공되나요?
- WAF는 임의로 세부 설정이 가능한가요?
- WAF 비용 구조는 어떻게 되나요?
- WAF에서 global과 region 차이는 무엇인가요?

## Bedrock and AI
- Amazon Bedrock 비용은 어떻게 구성되나요?
- Amazon Bedrock에서는 토큰 비용 외에 어떤 추가 비용이 있나요?
- Amazon Bedrock 네트워크 보안은 어떻게 설명하나요?
- AWS AI Stack은 AWS 101 수준에서 어디까지 설명하면 되나요?

## Pricing and Commercial
- Support Plan은 무엇인가요?
- Support Plan 비용은 어떻게 계산되나요?
- AWS 비용은 정확히 언제, 어느 부분에서 발생하나요?
- 메가존클라우드를 이용하면 AWS에 지출하는 비용은 그대로인가요?

## General Concepts
- 내구성과 가용성의 차이는 무엇인가요?
- 내구성이랑 가용성이 각각 무슨 의미인가요?
