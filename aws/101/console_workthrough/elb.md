## 1차 시도

### ALB

#### How Application Load Balancers work
1. Clients make requests to your application.
2. The listeners in your load balancer receive requests matching the protocol and port that you configure.
3. The receiving listener evaluates the incoming request against the rules you specify, and if applicable, routes the request to the appropriate target group. You can use an HTTPS listener to offload the work of TLS encryption and decryption to your load balancer.
4. Healthy targets in one or more target groups receive traffic based on the load balancing algorithm, and the routing rules you specify in the listener.

#### Basic configuration

##### Load balancer name
이름을 짓는 항목

##### Scheme
한 번 만들어지면 바꿀 수 없는 항목
인터넷과 맞닿은 퍼블릭 또는 내부 서버용 프라이빗 스키마를 결정할 수 있다.

##### Load balancer IP address type
ipv4/6을 결정하는 옵션

#### Network mapping

##### VPC
로드 밸런서를 vpc에 연결할 지 결정하는 옵션
결정하면 어떻게 밸런싱을 하는지 감이 잘 안잡힌다.
vpc와 연결된 네트워크의 트래픽을 조절하는 것으로 이해된다.

##### IP pools
ipam 풀을 선택하는 옵션
pool내부에서 자동으로 선택하는 것인데 이것도 alb에 똑같이 적용되는지를 모르겠다.

##### Availability Zones and subnets
az와 서브넷을 2개 이상을 골라야 로드 밸런싱이 의미있게 작동하기에 선택하는 옵션

#### Security groups 
보안 그룹
어떤 곳에서 오는 트래픽을 받을 지 선택할 수 있다.

#### Listeners and routing
리스너는 잘 모르는 개념이다.
"A listener is a process that checks for connection requests using the port and protocol you configure. The rules that you define for a listener determine how the load balancer routes requests to its registered targets."
L3의 SYN, ACK와 비슷한 개념으로 이해하고자 한다.
Default action을 통해 forward/redirect/return을 결정할 수 있고 어디에 어떤 내용을 담아 전달할지도 선택 가능하다.

#### Load balancer tags - optional
언제나 그렇듯 태그는 적절한 관리에 필수적이다.

#### Optimize with service integrations - optional
1. Amazon CloudFront + AWS Web Application Firewall (WAF) 
캐싱에 도움을 주는 클라우드 프론트와 L7보안의 waf를 섞은 개념
2. AWS Web Application Firewall (WAF)
L7보안의 waf
3. AWS Global Accelerator 
글로벌 단위의 캐싱을 돕는 서비스

1번과 3번은 중첩이 되지 않는다.
그러나 왜 안되는 지는 모르겠다.

### NLB

#### How Network Load Balancers work
1. Clients make requests to your application.
2. The load balancer receives the request either directly or through an endpoint for private connectivity (via AWS PrivateLink).
3. The listeners in your load balancer receive requests of matching protocol and port, and route these requests based on the default action that you specify. You can use a TLS listener to offload the work of encryption and decryption to your load balancer.
4. Healthy targets in one or more target groups receive traffic according to the flow hash algorithm.

#### Basic configuration

##### Load balancer name
이름 설정하는 곳

##### Scheme
퍼블릭과 맞닿을지, 내부 서버의 부하를 조절할 지 선택하는 옵션

##### Load balancer IP address type
다시 읽어보니 로드밸런서가 맞닿을 지 결정하면, 연결하기 위한 주소가 필요한 것 같다.
따라서 어떤 타입의 주소를 설정할지(보통은 ipv4) 결정이 필요한 것 같다.
옵션상에서는 aws가 자동적으로 할당하는 것으로 보인다.

#### Network mapping 

##### VPC
어느 vpc의 부하를 조절할 지 선택하는 옵션

##### Availability Zones and subnets
어느 az와 subnet의 부하를 조절할 지 선택하는 옵션

두개 옵션 모두 트래픽을 분산해서 전달할 타겟을 선택하는 옵션

#### Security groups
어디에서 오는 트래픽을 받을 지 선택하는 옵션이다.
서버 내부는 ip주소와 포트를 고정시킬 수 있는데, 외부의 경우는 어떻게 특정하는 지 모르겠다.

#### Listeners and routing
alb와 같은 개념으로 이해된다.
잘 주고 받음을 확인하는 기능과, 어떤 메시지를 전달할 지 선택하는 옵션인 것 같다.

#### Load balancer tags - optional
태그 옵션

#### Optimize with service integrations - optional
이 경우에는 AWS Global Accelerator만 존재한다.
L7이 아니니 클라우드프론트와 waf가 필요하지 않기 때문이다.
가속화하는 기능은 필요할 수 있다.

### GWLB

#### How Gateway Load Balancers work
1. Clients make requests to your application.
2. The load balancer receives the request based on the route table configurations that are set within your VPC, Internet Gateway, or Transit Gateway.
3. The load balancer routes requests to a target group consisting of a scalable fleet of appliances (for example, firewalls, deep packet inspection systems, URL filtering systems etc.) to process traffic flows.
4. The virtual appliance processes the traffic, and forwards it back to the load balancer, or drops the traffic based on its configuration. This type of load balancer acts as a bump-in-the-wire between the source and destination.
5. The load balancer forwards the traffic to its destination.

#### Basic configuration

##### Load balancer name
이름 옵션

##### Load balancer IP address type
ipv4/v6를 선택하는 옵션

#### Network mapping 

##### VPC
어떤 vpc의 트래픽을 분산할 지 결정하는 옵션

##### Availability Zones and subnets
어떤 az와 서브넷의 트래픽을 분산할 지 선택하는 옵션

선택하지 않는다면 로드밸런서를 만들 수 없는가?

#### IP listener routing

앞의 두 로드밸런서와 다르게 forward만 가능하다.

#### Load balancer tags - optional
태그 옵션

### 그외
alb는 웹 서비스 중심의 트래픽 분산, nlb는 더 빠른 네트워크 트래픽에 사용되며, GWLB는 보안장비 연동이 필요하다고 알고 있다.
결국 로드밸런서는 오토스케일링과 주로 연동이 되어 사용된다. 
로드밸런서는 모니터링이 필요한 것으로 알아 요금이 부과된다.

---


## Kiro Grade: B- (74/100)

### Per-section feedback

#### ALB

**How Application Load Balancers work** ✅ Correct.
- 공식 문서에서 가져온 설명이다. 정확하다.
- 평점: `A`

**Load balancer name** ✅ Correct.
- 추가: 생성 후 변경 불가. 최대 32자.
- 평점: `B+`

**Scheme** ✅ Correct.
- "한 번 만들어지면 바꿀 수 없는 항목" — 맞다. 좋은 포인트.
- Internet-facing = public IP, public subnet 필요 / Internal = private IP
- 평점: `A-`

**Load balancer IP address type** ✅ Correct but brief.
- 추가: Dualstack (IPv4 + IPv6), Dualstack without public IPv4 옵션도 있다.
- 평점: `B`

**VPC** ⚠️ Partially correct.
- "vpc에 연결할 지 결정하는 옵션" — 모든 로드밸런서는 반드시 VPC 안에 존재해야 한다. "연결할지"가 아니라 "어떤 VPC에 배치할지" 선택하는 것이다.
- "어떻게 밸런싱을 하는지 감이 잘 안잡힌다" — 로드밸런서는 선택한 VPC의 서브넷에 노드를 배치하고, 그 VPC 안의 타겟(EC2 등)으로 트래픽을 분산한다.
- 평점: `C`

**IP pools** ⚠️ Incomplete.
- IPAM 풀에서 public IPv4 주소를 할당받는 옵션이다. 대부분의 경우 사용하지 않는다 — AWS가 자동으로 IP를 할당한다.
- 평점: `C`

**Availability Zones and subnets** ✅ Correct.
- "2개 이상을 골라야 로드 밸런싱이 의미있게 작동" — 맞다. 각 AZ에 로드밸런서 노드가 하나씩 배치된다.
- 평점: `A-`

**Security groups** ✅ Correct but brief.
- 추가: 최대 5개 보안 그룹 지정 가능. 여러 개 지정 시 규칙이 합쳐진다(union).
- 평점: `B`

**Listeners and routing** ⚠️ Misunderstanding.
- "L3의 SYN, ACK와 비슷한 개념" — 아니다. SYN/ACK는 TCP 3-way handshake (L4)이고, listener는 그것과 다른 개념이다.
- **Listener = 특정 포트와 프로토콜로 들어오는 요청을 기다리는 설정**이다. 예: "HTTP:80으로 들어오는 요청을 받아서 target group A로 forward해라."
- Default action 3가지 (forward/redirect/return fixed response) 언급은 좋다.
- 빠진 핵심: **Target Group**이 무엇인지 설명이 없다. Target group = 트래픽을 받을 대상(EC2, IP, Lambda)의 묶음이다. Listener가 "어디로 보낼지" 결정하면, target group이 "누가 받을지"를 결정한다.
- 평점: `C-`

**Service integrations** ⚠️ Partially correct.
- CloudFront + WAF, WAF 단독, Global Accelerator 구분은 좋다.
- "L7보안의 waf" — 맞다.
- "글로벌 단위의 캐싱을 돕는 서비스" — **틀렸다**. Global Accelerator는 캐싱이 아니다. AWS의 글로벌 네트워크를 통해 트래픽을 최적 경로로 라우팅하는 서비스다. 고정 IP 2개를 제공하고, 가장 가까운 AWS 리전으로 트래픽을 보낸다. 캐싱은 CloudFront의 역할이다.
- "1번과 3번은 중첩이 되지 않는다" — 맞다. CloudFront와 Global Accelerator는 둘 다 "ALB 앞에 서는" 서비스이므로 동시에 쓸 수 없다.
- 평점: `C+`

#### NLB

**How Network Load Balancers work** ✅ Correct.
- 공식 문서 기반. PrivateLink 언급도 좋다.
- 평점: `A`

**Basic configuration** ✅ Correct.
- ALB와 동일한 구조를 잘 파악했다.
- "연결하기 위한 주소가 필요한 것 같다" — 맞다. Internet-facing이면 public IP가 필요하고, NLB는 **고정 IP(Elastic IP)**를 AZ별로 할당할 수 있다는 점이 ALB와의 큰 차이다.
- 평점: `B`

**Network mapping** ✅ Correct.
- "트래픽을 분산해서 전달할 타겟을 선택하는 옵션" — 맞다.
- 평점: `B+`

**Security groups** ⚠️ Incomplete.
- "외부의 경우는 어떻게 특정하는지 모르겠다" — 보안 그룹에서 source를 `0.0.0.0/0` (모든 IP)으로 설정하거나, 특정 CIDR 범위로 제한할 수 있다. 또는 다른 보안 그룹을 source로 지정할 수도 있다.
- 참고: NLB는 원래 보안 그룹을 지원하지 않았으나, 2023년부터 지원하기 시작했다.
- 평점: `C`

**Listeners and routing** ⚠️ Vague.
- "잘 주고 받음을 확인하는 기능" — 이건 listener가 아니라 **health check**에 가까운 설명이다.
- NLB listener는 ALB와 같은 개념이지만 프로토콜이 다르다: TCP, UDP, TLS (ALB는 HTTP, HTTPS).
- NLB의 default action은 **forward만 가능**하다 (redirect/return fixed response 없음).
- 평점: `D+`

**Service integrations** ✅ Good reasoning.
- "L7이 아니니 CloudFront와 WAF가 필요하지 않기 때문이다" — 맞다. CloudFront와 WAF는 L7 서비스이므로 L4인 NLB와는 맞지 않는다. Global Accelerator는 L4에서도 동작하므로 NLB와 사용 가능하다.
- 평점: `A-`

#### GWLB

**How Gateway Load Balancers work** ✅ Correct.
- 공식 문서 기반. "bump-in-the-wire" 개념 포함.
- 평점: `A`

**Basic configuration** ✅ Correct.
- GWLB에는 Scheme 옵션이 없다는 점을 암묵적으로 파악한 것 같다 — 맞다. GWLB는 항상 internal이다.
- 평점: `B+`

**Network mapping** ✅ Correct.
- "선택하지 않는다면 로드밸런서를 만들 수 없는가?" — 맞다. 최소 1개 AZ/서브넷을 선택해야 한다.
- 평점: `B`

**IP listener routing** ✅ Correct.
- "forward만 가능하다" — 맞다. GWLB는 트래픽을 보안 어플라이언스로 전달하는 것이 목적이므로 redirect나 fixed response가 의미 없다.
- 평점: `B+`

#### 그외 ⚠️ Partially correct.
- ALB = 웹 서비스, NLB = 빠른 네트워크, GWLB = 보안장비 — 맞다.
- "오토스케일링과 주로 연동" — 맞다. ELB + Auto Scaling은 가장 흔한 조합이다.
- "모니터링이 필요한 것으로 알아 요금이 부과된다" — 부정확하다. ELB 요금은 모니터링 때문이 아니라 **시간당 요금 + 처리한 트래픽(LCU/NLCU)** 기준이다. CloudWatch 기본 모니터링은 무료로 포함된다.
- 평점: `C+`

### Missing console sections

- **Target Group** — ELB에서 가장 중요한 개념 중 하나인데 빠져 있다. Target group = 트래픽을 받을 대상의 묶음. 타입 (instance/IP/Lambda), health check 설정, 포트, 프로토콜을 정의한다.
- **Health Check** — 타겟이 정상인지 확인하는 설정. 경로, 간격, 임계값 등. 비정상 타겟은 자동으로 트래픽에서 제외된다. AWS 101에서 거의 반드시 나오는 주제.
- **Cross-zone load balancing** — AZ 간 트래픽 분산 방식. ALB는 기본 활성화, NLB는 기본 비활성화.
- **Sticky sessions** — 같은 클라이언트를 같은 타겟에 계속 보내는 기능. ALB에서 설정 가능.
- **ALB vs NLB 핵심 차이 비교표** — Layer, 프로토콜, 고정 IP, 성능, 가격 등

### 총평

- 3가지 로드밸런서 타입을 모두 다룬 점은 좋다. 대부분의 1차 시도에서 ALB만 다루는 경우가 많다.
- 공식 문서의 "How it works" 설명을 포함한 점도 좋다.
- 하지만 **Listener와 Target Group의 관계**가 가장 큰 gap이다 — 이것이 ELB의 핵심 구조이다.
- Global Accelerator를 캐싱으로 이해한 부분은 교정 필요.

### 가장 먼저 보완해야 할 것

1. **Target Group이 무엇인지** — instance/IP/Lambda 타겟, health check, 포트/프로토콜
2. **Listener의 정확한 의미** — 포트+프로토콜로 요청을 받아 target group으로 라우팅하는 설정
3. **Health Check** — 비정상 타겟 자동 제외, 경로/간격/임계값 설정
4. **Global Accelerator ≠ 캐싱** — 글로벌 네트워크 라우팅 최적화 서비스
5. **ELB 요금 구조** — 시간당 + LCU/NLCU 기반

---

## Codex Grade: B- (75/100)

1차 시도치고는 범위가 좋다.

- ALB, NLB, GWLB를 모두 나눠서 본 점은 좋다.
- 공식 문서의 how-it-works를 그대로 읽으면서 구조를 잡은 것도 좋다.
- 다만 `Listener`, `Target Group`, `Health Check`, `Global Accelerator` 개념이 아직 완전히 분리되지 않았다.

#### 총평

- 현재 수준은 `타입 구분은 잘함`
- 그러나 `실제 콘솔의 핵심 구조 설명은 아직 보완 필요`
- 가장 먼저 보완해야 할 것은 아래 5개다.

1. `Listener와 Target Group 관계`
2. `Health Check가 무엇인지`
3. `Global Accelerator는 캐싱이 아니라는 점`
4. `VPC와 subnet이 load balancer에서 어떤 의미인지`
5. `ELB 요금이 모니터링 때문이 아니라 처리량/시간 기반이라는 점`

#### 잘 모르겠다를 풀어서 설명

##### VPC

- `어떤 VPC에 둘지 선택`한다는 말이 더 정확하다.
- Load Balancer는 반드시 어떤 VPC 안에 생성된다.
- 그리고 그 VPC의 subnet에 load balancer node가 배치되고, 그 VPC 안의 target으로 트래픽을 분산한다.
- 즉 `VPC에 연결할지`가 아니라 `어느 VPC 안에 배치할지`를 정하는 옵션이다.

##### IP pools

- 이 옵션은 IPAM pool에서 public IPv4 주소를 가져오도록 하는 옵션이다.
- 대부분의 AWS 101 수준에서는 AWS가 자동 할당하는 기본 동작만 알아도 충분하다.
- 즉 `특별한 IP 주소 관리 체계(IPAM)를 쓰는 경우에만 신경 쓰는 옵션`으로 이해하면 된다.

##### Listener

- listener는 SYN/ACK 같은 TCP handshake 개념이 아니다.
- 더 단순하게 말하면 `어떤 포트와 프로토콜로 들어오는 요청을 받을지 정하는 입구 설정`이다.
- 예: `HTTP:80`, `HTTPS:443`, `TCP:443`
- 들어온 요청을 어디로 보낼지는 listener rule과 default action이 결정한다.

##### Target Group

- target group은 실제로 트래픽을 받을 대상 묶음이다.
- 예를 들어:
  - EC2 인스턴스 묶음
  - IP 주소 묶음
  - Lambda 함수
- listener가 `어느 target group으로 보낼지`를 정하고, target group은 `누가 실제로 받을지`를 정한다.

##### Health Check

- health check는 target이 정상인지 계속 확인하는 기능이다.
- 비정상으로 판단되면 해당 target에는 트래픽을 보내지 않는다.
- 이것이 load balancer가 단순 분산기계가 아니라 가용성을 높여 주는 핵심 이유다.

##### Security group

- 외부의 경우는 source를 CIDR로 적는다.
- 예를 들어:
  - `0.0.0.0/0` = 모든 IPv4
  - `203.0.113.0/24` = 특정 회사 대역
- 또는 다른 security group 자체를 source로 지정할 수도 있다.
- 여러 security group을 붙이면 규칙이 합쳐진다.

##### Global Accelerator

- Global Accelerator는 캐싱 서비스가 아니다.
- 캐싱은 CloudFront 역할이다.
- Global Accelerator는 전 세계 사용자의 트래픽을 AWS 글로벌 네트워크를 통해 가장 가까운 edge로 받아서 최적 경로로 전달하는 네트워크 가속 서비스다.
- 즉:
  - `CloudFront` = 캐싱
  - `Global Accelerator` = 글로벌 네트워크 라우팅 최적화

#### 발표용으로 바로 쓸 수 있게 고치면 좋은 표현

- `아래 콘솔 옵션 정리는 study/aws/101/images/aws_console/elb1.png, elb2.png, alb1.png~alb7.png, nlb1.png~nlb6.png, gwlb1.png~gwlb4.png 기준으로 이해하면 된다.`

##### Listener

- `Listener는 특정 포트와 프로토콜로 들어오는 요청을 받는 설정이다. 예를 들어 HTTP 80이나 HTTPS 443으로 들어온 요청을 target group으로 전달한다.`

##### Target Group

- `Target group은 실제 요청을 받을 대상의 묶음이다. EC2, IP, Lambda 등을 target으로 둘 수 있다.`

##### ALB

- `ALB는 HTTP/HTTPS 같은 웹 트래픽을 처리하는 L7 로드 밸런서로, 경로와 호스트 규칙에 따라 요청을 나눌 수 있다.`

##### NLB

- `NLB는 TCP/UDP/TLS 같은 L4 트래픽을 빠르게 처리하는 로드 밸런서로, 고정 IP와 높은 성능이 장점이다.`

##### GWLB

- `GWLB는 방화벽 같은 네트워크 보안 장비를 중간에 넣어 트래픽을 검사하고 전달할 때 사용하는 로드 밸런서다.`

##### ELB 요금

- `로드 밸런서 요금은 모니터링 때문이 아니라 시간당 요금과 처리한 트래픽(LCU/NLCU) 기준으로 나온다.`

#### Terminology

- `ELB` = `Elastic Load Balancing`
- `ALB` = `Application Load Balancer`
- `NLB` = `Network Load Balancer`
- `GWLB` = `Gateway Load Balancer`
- `WAF` = `Web Application Firewall`
- `IPAM` = `IP Address Manager`
- `GA` = `Global Accelerator`
- `TLS` = `Transport Layer Security`
- `CIDR` = `Classless Inter-Domain Routing`
- `LCU` = `Load Balancer Capacity Unit`
- `NLCU` = `Network Load Balancer Capacity Unit`

#### AWS 101 수준에서 추가로 자주 나오는 질문

- Listener와 target group은 어떻게 다른가?
- Health check는 왜 중요한가?
- ALB와 NLB는 언제 각각 쓰는가?
- NLB는 왜 고정 IP가 중요한가?
- GWLB는 왜 일반 웹 서비스에 잘 안 쓰는가?
- CloudFront와 Global Accelerator는 어떻게 다른가?
- Security group은 source를 어떻게 지정하는가?
- ELB와 Auto Scaling은 어떻게 같이 쓰는가?

##### Listener와 target group은 어떻게 다른가?

- `Listener`는 어떤 포트와 프로토콜로 들어오는 요청을 받을지 정하는 설정이다.
- `Target group`은 그 요청을 실제로 받을 대상 묶음이다.
- 쉽게 말하면:
  - `Listener` = 입구
  - `Target group` = 실제로 일하는 서버 묶음

##### Health check는 왜 중요한가?

- target이 정상인지 계속 확인하기 때문이다.
- 비정상 target에는 트래픽을 보내지 않아서 장애 확산을 막는다.
- 이것이 ELB가 고가용성에 중요한 이유 중 하나다.

##### ALB와 NLB는 언제 각각 쓰는가?

- `ALB`는 HTTP/HTTPS 같은 웹 트래픽을 처리할 때 적합하다.
- 경로(path), 호스트(host), 리디렉션 같은 웹 레벨 라우팅이 필요하면 ALB를 쓴다.
- `NLB`는 TCP/UDP/TLS 같은 L4 트래픽을 빠르게 처리할 때 적합하다.
- 고정 IP, 매우 높은 성능, 낮은 지연이 중요하면 NLB를 먼저 본다.

##### NLB는 왜 고정 IP가 중요한가?

- 어떤 고객이나 시스템은 특정 고정 IP만 허용하도록 방화벽을 설정한다.
- 이런 경우 NLB의 고정 IP가 있으면 화이트리스트 등록이 쉬워진다.
- 그래서 기업 네트워크 연동이나 레거시 시스템 연결에서 중요할 수 있다.

##### GWLB는 왜 일반 웹 서비스에 잘 안 쓰는가?

- GWLB는 웹 요청을 웹 서버로 잘 분산하는 것이 목적이 아니다.
- 방화벽, IDS/IPS 같은 보안 장비를 중간에 넣어 트래픽을 검사하도록 만드는 것이 목적이다.
- 그래서 일반 웹 서비스에는 보통 ALB나 NLB가 맞고, GWLB는 보안 어플라이언스 연동용이다.

##### CloudFront와 Global Accelerator는 어떻게 다른가?

- `CloudFront`는 캐싱과 콘텐츠 전송 최적화를 위한 CDN이다.
- `Global Accelerator`는 캐싱이 아니라 AWS 글로벌 네트워크를 이용해 트래픽 경로를 최적화하는 서비스다.
- 쉽게 말하면:
  - `CloudFront` = 콘텐츠를 가까운 곳에 캐시
  - `Global Accelerator` = 네트워크 경로를 더 빠르고 안정적으로 연결

##### Security group은 source를 어떻게 지정하는가?

- source는 CIDR 블록으로 지정할 수 있다.
- 예:
  - `0.0.0.0/0` = 모든 IPv4
  - `203.0.113.0/24` = 특정 대역
- 또는 다른 security group 자체를 source로 지정할 수도 있다.

##### ELB와 Auto Scaling은 어떻게 같이 쓰는가?

- ELB는 들어오는 요청을 여러 target에 분산한다.
- Auto Scaling은 target으로 쓰이는 EC2 수를 자동으로 늘리거나 줄인다.
- 즉:
  - `ELB` = 트래픽 분산
  - `Auto Scaling` = 서버 수 조절
- 둘을 같이 쓰면 트래픽이 늘 때 서버 수를 늘리고, ELB가 그 서버들에 요청을 나눠 줄 수 있다.
