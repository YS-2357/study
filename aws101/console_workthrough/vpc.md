## 1차 시도

### VPC settings

1. Resources to create
vpc만 생성할건지, vpc와 함께 서브넷, 라우팅 테이블, igw의 네트워크까지 다 설치할 것인지 선택하는 옵션
나는 vpc만 고려하면 된다.

2. Name tag - optional
tag는 옵션이지만 꼭 프로젝트와 상황에 맞게 적어놓아야한다.
Resource Groups & Tag Editor에서 편리하게 태그가 달린 리소스를 확인할 수 있다.

3. IPv4 CIDR block
수동으로 얼마나 많은 bit를 고정할지, 아니면 pool안에서 고정할 지 선택하는 옵션이다.
ipam의 경우 개인이 갖고 잇는 것으로 알고 있다.

4. Tenancy
테넌시의 경우는 잘 모른다.
dedicated의 경우 하나에 할당하는 것으로 아는데, 테넌시 자체의 개념이 부족하다.

### Tags
key-value를 선택하는 것인데, 키는 프로젝트 단위이고, value를 서비스 단위로 이름을 지으면 된다.

---

## Kiro Grade: B-

### Per-section feedback

**1. Resources to create** ✅ Correct.
- VPC only vs VPC and more (subnets, route tables, IGW, NAT gateway together). Good understanding.

**2. Name tag** ✅ Correct.
- Good point about Resource Groups & Tag Editor. Solid practical advice.

**3. IPv4 CIDR block** ⚠️ Partially correct.
- "수동으로 얼마나 많은 bit를 고정할지" — the concept is right (you're choosing a network range), but the phrasing is vague.
- Two options are: **IPv4 CIDR manual input** (you type a range like `10.0.0.0/16`) vs **IPAM-allocated IPv4 CIDR block** (auto-assigned from an IPAM pool).
- IPAM is not "개인이 갖고 있는 것" — it's an AWS service (VPC IP Address Manager) for centrally managing IP address allocation across your organization. It's used by enterprises to prevent CIDR overlap across multiple VPCs/accounts.

**4. Tenancy** ⚠️ Incomplete but honest.
- **Default** = instances share physical hardware with other AWS accounts (normal, cheaper)
- **Dedicated** = instances run on hardware dedicated only to your account (expensive, used for compliance/licensing requirements)
- Once set to Dedicated, all EC2 instances in this VPC run on dedicated hardware. This is hard to change later and significantly increases cost.

**5. Tags** ✅ Correct concept, but the key-value convention you described is just one approach — not a rule.

### Missing options from the console
- **IPv6 CIDR block** — option to add IPv6 support (Amazon-provided, IPAM-allocated, or BYOIP)
- **DNS options** — "Enable DNS resolution" and "Enable DNS hostnames" (both enabled by default). Important for services like RDS that rely on DNS names.

## 2차 시도

### VPC settings

1. Resources to create
vpc만 생성할건지, vpc와 함께 서브넷, 라우팅 테이블, igw의 네트워크까지 다 설치할 것인지 선택하는 옵션
내 경우는(aws sa관점) vpc만 고려하면 된다.

2. Name tag - optional
하단의 Tags에서 자세히 설명

3. IPv4 CIDR block
cidr블럭을 수동으로 결정할 지, aws의 풀에서 자동 결정을 진행할 지 정하는 옵션
cidr 자체는 서비스 상황에 맞게 넉넉하게 작성해야함
처음 4개 마지막 1개는 aws가 점유함
32비트의 몇 비트를 고정하는지가 /number에서 결정됨
ipam이 무슨 용어를 줄인 말인지는 잘 모름
그러나 기업이 사용할 때 vpc/계정 상에서 충돌이 나지 않도록 자동으로 조정해주는 서비스 -> 요금이 더 나오는지는 잘 모름

4. IPv6 CIDR block
ipv4의 단점을 해소하기 위한 ipv6인데, 보통은 필요 없고 개인이 갖고 잇는 경우도 많이 없다.
기본 옵션은 ipv4와 비슷하지만 aws 또는 개인의 ipv6를 사용 가능하다.

5. Tenancy
테넌시는 aws의 물리적인 장비에서 vpc를 사용자 한 명에게만 할당하는가, 아닌가를 결정하는 옵션이다.
보안을 위해서 고려 가능한 옵션이지만, 비용이 상당하다.

### Tags
Resource Groups & Tag Editor에서 관리가 가능한 옵션
어떤 규칙을 사용하든지, 거의 필수적으로 사용을 권장한다.

### Codex Grade: B- (76/100)

2차 시도는 1차보다 확실히 좋아졌다.

- CIDR, IPv6, tenancy까지 시야를 넓힌 점은 분명한 개선이다.
- `Resources to create`와 `Tags`는 AWS 101 수준에서 꽤 안정적이다.
- 하지만 `Tenancy` 설명, `IPAM` 정확도, `DNS options` 누락 때문에 아직 발표용으로는 덜 정리된 상태다.

#### 총평

- 현재 수준은 `공부 메모로는 괜찮음`
- 그러나 `AWS 101 발표/고객 설명용으로는 한 번 더 다듬어야 함`
- 가장 먼저 보완해야 할 것은 아래 4개다.

1. `Tenancy가 정확히 무엇을 의미하는지`
2. `IPAM이 무엇의 약자인지와 어떤 서비스인지`
3. `IPv6 CIDR block 옵션의 공식 구분`
4. `DNS resolution / DNS hostnames 옵션 추가`

#### 발표용으로 바로 쓸 수 있게 고치면 좋은 표현

- `아래 콘솔 옵션 정리는 study/aws101/images/aws_console/vpc1.png 와 vpc2.png 기준으로 이해하면 된다.`

##### Resources to create

- `VPC만 생성할 수도 있고, VPC와 함께 subnet, route table, internet gateway 등 기본 네트워크 구성을 한 번에 만들 수도 있다.`

##### IPv4 CIDR block

- `VPC의 IPv4 주소 대역을 직접 입력할 수도 있고, Amazon VPC IP Address Manager(IPAM) 풀에서 자동 할당받을 수도 있다. CIDR은 향후 subnet 확장까지 고려해 넉넉하게 설계하는 것이 중요하다.`

##### IPv6 CIDR block

- `필요하면 VPC에 IPv6 CIDR block을 추가할 수 있다. AWS 제공 IPv6, IPAM 할당, 또는 BYOIP 같은 방식이 있다.`

##### Tenancy

- `Tenancy는 이 VPC에서 실행되는 EC2 인스턴스가 기본 공유 하드웨어를 사용할지, 계정 전용 dedicated 하드웨어를 사용할지 정하는 옵션이다. Dedicated는 비용이 높고 주로 규제나 라이선스 요구가 있을 때 사용한다.`

##### DNS options

- `VPC에서는 DNS resolution과 DNS hostnames 옵션도 중요하다. EC2나 RDS 같은 리소스가 이름 기반으로 동작할 때 자주 필요하다.`

#### Terminology

- `Console screenshots` = `study/aws101/images/aws_console/vpc1.png`, `study/aws101/images/aws_console/vpc2.png`
- `VPC` = `Virtual Private Cloud`
- `CIDR` = `Classless Inter-Domain Routing`
- `IPAM` = `Amazon VPC IP Address Manager`
- `IPv4` = `Internet Protocol version 4`
- `IPv6` = `Internet Protocol version 6`
- `DNS` = `Domain Name System`
- `IGW` = `Internet Gateway`
- `NAT` = `Network Address Translation`
- `BYOIP` = `Bring Your Own IP`
- `AWS` = `Amazon Web Services`

#### AWS 101 수준에서 추가로 자주 나오는 질문

- VPC와 subnet은 어떻게 다른가?
- public subnet과 private subnet은 어떻게 구분하는가?
- route table은 어떤 역할을 하는가?
- internet gateway와 NAT gateway는 어떻게 다른가?
- security group과 NACL은 어떻게 다른가?
- VPC peering과 Transit Gateway는 언제 각각 쓰는가?
- CIDR을 너무 작게 잡으면 어떤 문제가 생기는가?
- DNS hostnames와 DNS resolution은 왜 필요한가?
