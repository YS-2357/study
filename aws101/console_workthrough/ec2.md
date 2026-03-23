## 1차 시도
1. Name and tag
이름과 태그를 다는 옵션

2. AMI
리눅스, 맥, 우분투, 윈도우 등의 os를 선택하는 옵션.

3. 인스턴스 타입
인스턴스의 타입을 결정하는 옵션으로 명명 규칙에 따라 다양한 패밀리, 세대, 속성, 사이즈를 고를 수 있다.
범용, 컴퓨팅, 메모리, 버스팅용, GPU, iops, 디스크 타입등 다양한 패밀리가 존재하고,
세대가 높을수록 성능은 좋아지는데 비용은 줄어든다.
속성은 프로세서 amd, intel, graviton이 존재하는데 a, i는 호환되지만 g는 아마존 자체의 프로세서라 호환되지 않는다.
사이즈는 가상 cpu의 개수를 고르는 옵션으로 이해하면 되는데 사이즈가 2배가 되면 가격도 거의 2배로 늘어난다.

4. 키페어
이는 아직 잘모르겠으나 보안을 위한 옵션으로 보인다.
로그인과 관련되는데 정확히 어떤 로그인 옵션과 어울리는지 모르겠다.

5. 네트워크 세팅
라우팅 테이블과 서브넷, igw등 어떤 네트워크와 어떤 보안을 통해 연결하는 지를 고르는 옵션이다.
연결은 라우팅테이블을 통해서 cidr블럭과 연결하고 ipv4로 연결하는 것으로 알고 있으나,
보안의 ssh, https, http가 어떤 식으로 다른 지는 모르겠다.
secure shell이 어떻게 보안을 책임지는지?
http의 프로토콜과 secure가 붙은 https가 어떻게 보안을 책임지는지?
aws가 아닌 networking에 관한 근본적인 물음이다.

6. Configure storage
임시 소토리지의 옵션을 고르는 항목이다.
임시 스토리지는 중단되거나 종료되면 데이터가 모두 사라진다.

7. 인스턴스의 옵션을 바꾸려면?
    - 스냅샷이 아니라 그냥 ec2 서비스를 중단하고 옵션을 변경하면 된다.
    그러나 서비스가 중단되니 서비스 이용 시간이 아니거나 사전 고지가 필요할 수 있다.

---

### Kiro Grade: C+

#### Per-section feedback

**1. Name and tag** ✅ Correct but brief.
- You could add: tags are key-value pairs used for cost tracking, access control, and organization — not just names.

**2. AMI** ⚠️ Partially correct.
- AMI is more than just OS selection. It includes pre-installed software, root volume configuration (EBS vs instance store), virtualization type (HVM vs PV), and boot mode.
- You can also use custom AMIs, AWS Marketplace AMIs, and community AMIs — not just the default OS list.

**3. Instance type** ⚠️ Has errors.
- Families, generations, size scaling — mostly correct.
- **Error**: "a, i는 호환되지만 g는 호환되지 않는다" is wrong. In the naming convention, `a` = AMD, `g` = Graviton (ARM-based). There is no `i` for Intel — Intel is the **default** (no letter suffix). So `m7i` means Intel, `m7a` means AMD, `m7g` means Graviton. Graviton is ARM architecture, so x86 software won't run on it without recompilation.
- Size determines both vCPU **and memory**, not just vCPU count.

**4. Key pair** ⚠️ Incomplete.
- A key pair is an SSH public/private key pair. AWS stores the public key on the instance, you keep the private key. You use it to SSH into Linux instances (or decrypt Windows admin password).
- Without a key pair, you cannot connect to the instance unless the AMI has another login method configured.

**5. Network settings** ⚠️ Partially correct, some confusion.
- The main options are: VPC, Subnet, Auto-assign Public IP, and Security Group (firewall rules).
- SSH (port 22) = encrypted remote terminal access to the instance.
- HTTP (port 80) = unencrypted web traffic.
- HTTPS (port 443) = encrypted web traffic using TLS/SSL certificates.
- These are **security group inbound rules**, not routing table settings. Routing tables and IGW are VPC-level config, not directly set during EC2 launch.

**6. Configure storage** ❌ Incorrect.
- The default storage for EC2 is **EBS (Elastic Block Store)**, which is **persistent** — data survives stop/start.
- **Instance store** is the temporary storage where data is lost on stop/terminate, but it's NOT the default and only available on certain instance types.
- You also missed: volume type (gp3, io2, etc.), size, IOPS, encryption, and delete-on-termination options.

#### Missing console sections
- **Advanced details** — a large section including: IAM instance profile, user data (startup scripts), Spot Instance purchasing, placement groups, tenancy, termination/stop protection, CloudWatch monitoring, metadata settings, and more.
- **Summary** — number of instances to launch.

## 2차 시도
1. Name and tags
이름과 태그를 정하는 옵션
이름을 지을때는 명확한 명명규칙을 통해서 가시성을 높여야 한다.
태그는 옵션이지만 필수적으로 붙여서 관련 aws 서비스를 이용해 묶어서 살필 수 있다.
서비스를 종료할 때 이것으로 관리해 헷갈리지 않게 관리가 가능하다.

2. Application and OS Images (Amazon Machine Image)
ami는 ec2인스턴스에 필요한 모든 것을 담겨져 잇는 일종의 청사진이다.
os를 포함해 소프트웨어 disk 볼륨, 등등 다양한 옵션을 선택할 수 있다.
리눅스, 맥, 우분투, 윈도우등 다양한 옵션이 존재한다.

3. Instance type
인스턴스 명명규칙에 포함되고 패밀리, 세대, 속성, 사이즈로 나타난다.
패밀리와 속성에는 다양한 옵션이 있는데 모두 외울 필요는 없고 필요에 따라 알맞은 옵션을 선택 가능하다.
세대는 최신일수록 성능이 좋고 가격이 낮다
사이즈는 cpu와 메모리와 연관이 있는데 크기와 가격이 비례하는 편이다.

4. Key pair (login)
키 페어는 로그인과 관련된 보안 옵션이다. 
그러나 ec2와의 연결이 무엇을 의미하는 지를 모르겠다.
나의 컴퓨터에서 ec2에 접근할 때 필요한 키로 인지되는데, 어떤 때에 사용하는 지를 잘 모르겠다.

5. Network settings
네트워크 연결과 관련된 항목이다.
어떤 vpc의 서브넷과 연결할지, 퍼블릭인지 프라이빗인지, 보안은 어떤 항목으로 할 지 정할 수 있다.
보안그룹이기에 인바운드만 고려한다.

6. Storage (volumes) 
ebs의 볼륨을 어떻게 정할 지 선택하는 옵션이다.
선택하면 ec2에 붙어서 생성된다.
또한 efs와 fsx도 선택이 가능하다.

7. 그외
ec2의 옵션을 변경은 서비스를 중단하고 가능하다.
복제의 경우는 기존의 ec2의 이미지를 복제?해서 새로 생성하는 방식이다.
더 다른 101 수준의 질문이 뭐가 존재하는지 모르겠다.
고객의 입장에서 더 생각할 필요가 있다.

## Codex Grade: B- (74/100)

2차 시도는 1차보다 확실히 좋아졌다.

- `Name and tags`, `AMI`, `Storage`는 방향이 더 정확해졌다.
- 특히 `Storage`를 EBS volume 중심으로 이해한 점은 1차보다 개선되었다.
- 하지만 `Key pair`, `Network settings`, `Instance type`의 일부 표현은 아직 AWS official doc와 console option 기준으로 부정확하거나 불완전하다.
- AWS 101 발표용으로는 "설명 가능" 직전 단계이고, 아직 고객 앞에서 바로 말하기에는 몇 군데가 불안하다.

#### Section-by-section

##### 1. Name and tags

- 전반적으로 적절하다.
- 단, 태그는 단순 식별뿐 아니라 비용 추적, 자동화, 운영 분류에도 많이 쓰인다는 점까지 알면 더 좋다.
- 평점: `A-`

##### 2. Application and OS Images (Amazon Machine Image)

- `AMI는 EC2 인스턴스에 필요한 청사진`이라는 방향은 좋다.
- 다만 공식적으로는 OS뿐 아니라 소프트웨어 구성, boot에 필요한 image, root volume 관련 설정 등을 포함하는 launch template 성격의 이미지라고 이해해야 한다.
- AWS Marketplace AMI, custom AMI, community AMI도 있다는 점까지 알면 더 좋다.
- 평점: `B`

##### 3. Instance type

- 패밀리, 세대, 속성, 사이즈로 이해한 것은 좋다.
- 하지만 `최신 세대일수록 성능이 좋고 가격이 낮다`는 표현은 너무 단정적이다.
- 더 정확한 표현은 `최신 세대일수록 일반적으로 성능 효율과 price/performance가 좋아지는 경향이 있다`이다.
- 사이즈는 CPU뿐 아니라 memory와도 함께 연결된다.
- 평점: `B-`

##### 4. Key pair (login)

- 아직 가장 보완이 필요한 구간이다.
- Key pair는 `EC2에 접속할 때 사용하는 public/private key pair`로 이해하면 된다.
- Linux instance는 보통 SSH 접속에 쓰고, Windows instance는 관리자 비밀번호 복호화에 사용된다.
- 또한 최근에는 EC2 Instance Connect, Systems Manager Session Manager 같은 대체 접속 방식도 존재한다.
- `무엇을 의미하는지 모르겠다` 상태를 넘어서, 최소한 접속/인증 관점으로 정리해 둘 필요가 있다.
- 평점: `C`

##### 5. Network settings

- `VPC, subnet, public/private 여부를 정한다`는 방향은 맞다.
- 하지만 `보안그룹이기에 인바운드만 고려한다`는 문장은 부정확하다.
- Security group은 inbound와 outbound 규칙을 모두 가진다.
- 그리고 launch wizard의 `Network settings`는 security group만이 아니라 VPC, subnet, auto-assign public IP, network interface 등을 포함한다.
- Routing table과 IGW는 직접 이 카드에서 세세하게 설정하는 항목이 아니라 VPC 측 구성을 전제로 활용하는 것이다.
- 평점: `C-`

##### 6. Storage (volumes)

- 1차보다 훨씬 좋아졌다.
- `EBS volume을 정하는 옵션`이라는 이해는 맞다.
- 다만 console 기준으로는 size, volume type, IOPS, throughput, encryption, delete on termination, snapshot 기반 복원 등도 같이 본다는 점을 추가하면 더 정확하다.
- EFS/FSx mount 가능성을 언급한 점은 좋지만, 기본은 `EBS root/additional volume` 설명이 중심이어야 한다.
- 평점: `B-`

##### 7. 그외

- `인스턴스 옵션 변경 시 중단 후 변경`은 일부 상황에서는 맞다.
- 하지만 모든 변경을 그렇게 설명하면 안 된다.
- 예를 들어 instance type 변경은 stop 후 가능하지만, scaling/복제는 보통 launch template, AMI, Auto Scaling 같은 구조로 설명해야 더 정확하다.
- `복제 = 기존 EC2 이미지를 복제해서 생성`은 아주 거칠게는 맞지만, AWS 101에서는 `AMI나 launch template 기반으로 동일한 설정의 instance를 다시 만들 수 있다` 정도로 정리하는 편이 안전하다.
- 평점: `C+`

#### 총평

- 현재 수준은 `공부 메모로는 좋음`
- 그러나 `AWS 101 발표/고객 설명용으로는 아직 다듬어야 함`
- 가장 먼저 보완해야 할 것은 아래 4개다.

1. `Key pair가 정확히 무엇인지`
2. `Network settings가 실제로 무엇을 포함하는지`
3. `Instance generation과 가격 표현`
4. `Storage 옵션에서 EBS 세부 속성`

#### 발표용으로 바로 쓸 수 있게 고치면 좋은 표현

- `아래 콘솔 옵션 정리는 study/aws101/images/aws_console/ec2_1.png, ec2_2.png, ec2_3.png, ec2_4.png 기준으로 이해하면 된다.`

##### Key pair

- `EC2 key pair는 인스턴스 접속 시 사용하는 public/private key 쌍이다. Linux는 SSH 접속, Windows는 관리자 비밀번호 복호화에 사용된다.`

##### Network settings

- `Network settings는 인스턴스가 어떤 VPC와 subnet에 들어갈지, public IP를 받을지, 어떤 security group과 network interface를 사용할지 정하는 항목이다.`

##### Instance type

- `인스턴스 타입은 workload에 맞는 CPU, memory, network 특성을 고르는 옵션이며, 최신 세대일수록 일반적으로 더 나은 성능 효율을 제공한다.`

##### Storage

- `Storage는 기본적으로 EBS volume을 설정하는 영역이며, volume size, type, IOPS, encryption, delete on termination 여부 등을 선택할 수 있다.`

#### Terminology

- `Console screenshots` = `study/aws101/images/aws_console/ec2_1.png`, `study/aws101/images/aws_console/ec2_2.png`, `study/aws101/images/aws_console/ec2_3.png`, `study/aws101/images/aws_console/ec2_4.png`
- `EC2` = `Elastic Compute Cloud`
- `AMI` = `Amazon Machine Image`
- `SSH` = `Secure Shell`
- `RDP` = `Remote Desktop Protocol`
- `EBS` = `Elastic Block Store`
- `IAM` = `Identity and Access Management`
- `VPC` = `Virtual Private Cloud`
- `CPU` = `Central Processing Unit`
- `IOPS` = `Input/Output Operations Per Second`

#### AWS 101 수준에서 추가로 자주 나오는 질문

- EC2와 Lambda는 언제 각각 쓰는가?
- EC2와 ECS/EKS/Fargate는 어떻게 다른가?
- AMI와 snapshot은 어떻게 다른가?
- public subnet에 있는 EC2와 private subnet에 있는 EC2는 어떤 차이가 있는가?
- Security Group과 NACL은 어떻게 다른가?
- EBS와 instance store는 어떻게 다른가?
- Spot, On-Demand, Reserved/Savings Plans는 어떤 경우에 쓰는가?
- 접속은 SSH만 가능한가, Session Manager도 가능한가?
