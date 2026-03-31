## 1차 시도

### Engine options
rds에 들어갈 rdb엔진을 고르는 옵션
aurora는 aws의 자체 엔진이고 postgresql, mysql과 호환됨.
그 외에도 많은 옵션이 존재함.

### Choose a database creation method
만드는 방식을 설정하는 옵션
나는 full 방식만 기억하면 된다.

### Templates
실제 서비스 환경인지, 개발/테스트 환경인지 선택하는 옵션이다.
둘의 차이점은 고가용성과 속도, 일관성의 차이가 있다.
어떻게 이런 차이를 만들어내는지, 요금에도 차이가 나는지는 잘 모르겠다.

### Cluster scalability type
오로라에 존재하는 옵션으로 보인다.
auto scaling과 관련된 옵션으로 보인다.
서버리스의 경우는 사용자가 신경쓰지 않아도 되는 옵션일 것이다.
제한없는 db의 경우는 싱글 db 클러스터를 넘어 수평적 확장을 이뤄준다고 한다.
프로비전의 경우는 고정적인 사이즈를 제공하는 옵션으로 보인다.
그러나 수직적/수평적인 확장이 어떤 의미인지, 클러스터가 뭔지는 잘 모르겠다.

각각의 옵션을 선택하면 range나 provisioned 옵션을 선택하는 항목이 존재한다.

### Settings
엔진 버전은 선택한 엔진의 버전을 고르는 옵션이다.
rds extension은 잘 모르겠다.
요금은 더 나온다고 쓰여있다.

db 클러스터 식별자는 이름을 짓는 것으로 보인다.

### Credentials Settings
마스터 사용자이름도 이름을 짓는 것으로 보인다.

Credentials management은 aws의 secret manager를 사용할 것인지, 스스로 관리할 것인지 고를 수 있다.
secret manager와 kms의 차이점은 헷갈린다.

Select the encryption key는 암호화 방식을 어디에 보관하고 사용할 지 선택하는 옵션이다.
오로라는 aws밖에 존재하지 않는다.

### Cluster storage configuration 
Configuration options는 표준과 i/o 2가지가 존재한다.
비용최적화인지 iops최적화인지 선택할 수 있다.

### Availability & durability
multi-az인지 아닌지 선택하는 옵션이다. 

### Connectivity 
Compute resource는 ec2의 컴퓨튜 자원과 연결할 지 아닐 지 선택하는 옵션이다.
비용차이는 잘 모르겠다

Network type는 ipv4만 쓸지 ipv6도 쓸지 선택하는 옵션이다.
주소가 왜 쓰이는지, 어떤 차이가 있는지는 모르겠다.

Virtual private cloud (VPC)도 vpc와 연결하는 옵션이다.
서버리스의 경우는 vpc와 무관하게 존재할 수 있기에 선택하는 옵션인 것 같다.
그렇다면 주소도 서버리스이기에 독립적으로 존재해서 주소가 필요한 것일 수도 있을 것 같다.

DB subnet group은 어떤 서브넷에 db를 할당할 지 선택하는 옵션이다.

Public access는 퍼블릭과 연결할 지 선택하는 옵션이다.
당연하지만 db는 거의 대부분 프라이빗이다.

VPC security group (firewall)은 보안 설정을 지정하는 옵션이다.
하나 이상의 보안 그룹을 지정할 수 있다는데, 어떤 식으로 적용되는 지는 잘 모른다.

Certificate authority - optional는 모르겠다.

### Read replica write forwarding
forward가 무슨 의미인지 모르겠다.
문제가 생기면 보고하라는 의미인 것 같다.

### Tags - optional
태그 지정 옵션이다.

### Babelfish settings
전혀 모르는 것이다.

### Monitoring
고급과 표준 옵션이 존재한다.
클라우드워치와 연동되어 이상을 탐지하는 것으로 보이며, kms키를 사용해서 보안?을 신경쓰는 것 같다.

### etc
그외 옵션은 무시한다.
db의 경우 요금이 많이 나오므로 주의해야할 필요성이 있다.

이외에 aurora와 rds의 차이점은 다음과 같다.
1. rds는 rdb를 관리하는 서비스이고 aurora는 그 위의 엔진이다.
2. 둘 모두 관리형이지만 오로라의 경우 서버리스도 지원한다.
3. rds는 다른 엔진도 지원하지만 오로라는 2개 db만 호환된다.

---

## Kiro Grade: C+ (68/100)

### Per-section feedback

**Engine options** ✅ Correct.
- Aurora가 AWS 자체 엔진이고 MySQL/PostgreSQL 호환이라는 점 맞다.
- 추가: 콘솔에서 선택 가능한 엔진은 Aurora (MySQL/PostgreSQL), MySQL, MariaDB, PostgreSQL, Oracle, SQL Server, Db2 총 7가지다.
- 중요한 점: **엔진은 생성 후 변경 불가**. 처음에 잘 골라야 한다.
- 평점: `B`

**Choose a database creation method** ⚠️ Too brief.
- 2가지 옵션이 있다:
  - **Standard create** — 모든 옵션을 직접 설정
  - **Easy create** — AWS 권장 설정으로 자동 구성, 일부 옵션만 선택
- "full 방식만 기억하면 된다"는 학습 태도로는 괜찮지만, Easy create가 무엇인지는 알아야 한다.
- 평점: `C+`

**Templates** ⚠️ Partially correct.
- 3가지 옵션이 있다:
  - **Production** — Multi-AZ 기본 활성화, 고성능 스토리지, 높은 가용성
  - **Dev/Test** — Multi-AZ 비활성화, 비용 절감
  - **Free tier** — t3.micro/t4g.micro, 20GB 스토리지, Single-AZ (학습/테스트용)
- "고가용성과 속도, 일관성의 차이" — 방향은 맞지만 핵심은 **Multi-AZ 기본값과 인스턴스 크기 기본값이 달라지는 것**이다. Template은 이후 옵션들의 기본값을 바꿔주는 프리셋일 뿐, 실제로 잠기는 옵션은 아니다.
- Free tier를 빠뜨렸다.
- 평점: `C`

**Cluster scalability type** ⚠️ Direction is right, details are weak.
- 이 옵션은 Aurora 전용이 맞다. 3가지:
  - **Serverless** — 트래픽에 따라 자동 스케일링, ACU(Aurora Capacity Unit) 범위 설정
  - **Provisioned** — 고정 인스턴스 크기를 직접 선택
  - **Limitless Database** — 여러 DB 클러스터에 걸쳐 수평 확장 (매우 대규모 워크로드용)
- "수직적/수평적 확장이 어떤 의미인지 모르겠다":
  - **수직 확장(Scale up)** = 더 큰 인스턴스로 교체 (db.r5.large → db.r5.2xlarge)
  - **수평 확장(Scale out)** = 인스턴스를 추가 (read replica 추가, 또는 Limitless처럼 여러 클러스터로 분산)
- "클러스터가 뭔지 모르겠다":
  - **Aurora 클러스터** = 1개의 writer instance + 0~15개의 reader instance가 하나의 공유 스토리지를 사용하는 구조. 일반 RDS는 클러스터가 아니라 단일 인스턴스(+ optional replica).
- 평점: `C-`

**Settings** ⚠️ Incomplete.
- 엔진 버전 설명은 맞다.
- "RDS Extended Support" — 엔진의 커뮤니티 지원이 끝난 후에도 AWS가 보안 패치를 계속 제공하는 유료 옵션이다. 추가 요금이 발생한다.
- "DB 클러스터 식별자" — 맞다. AWS 내에서 이 DB를 구분하는 고유 이름이다. 리전 내에서 유일해야 한다.
- 평점: `C+`

**Credentials Settings** ⚠️ Partially correct, key confusion.
- 마스터 사용자이름 — DB의 관리자 계정 이름이다 (e.g. `admin`, `postgres`). 단순 표시용 이름이 아니라 **DB에 로그인할 때 쓰는 실제 계정**이다.
- Credentials management:
  - **AWS Secrets Manager** — DB 비밀번호를 Secrets Manager에 자동 저장 + 자동 rotation 가능
  - **Self managed** — 비밀번호를 직접 입력하고 직접 관리
- "Secret Manager와 KMS의 차이점":
  - **Secrets Manager** = 비밀번호, API 키, DB 자격증명 같은 **비밀 값 자체**를 저장하고 자동 교체하는 서비스
  - **KMS** = **암호화 키**를 관리하는 서비스. 데이터를 암호화/복호화할 때 사용하는 키를 생성하고 관리한다
  - 관계: Secrets Manager가 비밀 값을 저장할 때 KMS 키로 암호화한다. 즉 KMS는 Secrets Manager의 하위 도구다.
- 평점: `C`

**Cluster storage configuration** ⚠️ Partially correct.
- Aurora 전용 옵션이다. 2가지:
  - **Aurora Standard** — 범용. I/O 요청당 과금. 대부분의 워크로드에 적합.
  - **Aurora I/O-Optimized** — I/O 비용 없음, 대신 인스턴스/스토리지 요금이 ~30% 높음. I/O가 많은 워크로드에 유리.
- "비용최적화인지 iops최적화인지" — 방향은 맞지만, 정확히는 **I/O 과금 방식의 차이**다.
- 평점: `C+`

**Availability & durability** ⚠️ Too brief.
- Multi-AZ 선택이라는 점은 맞다.
- 하지만 Aurora의 경우 옵션이 더 구체적이다:
  - **Create an Aurora Replica in a different AZ** — 다른 AZ에 reader를 만들어 failover 대비
  - **Don't create an Aurora Replica** — writer만 생성, failover 없음
- 일반 RDS의 경우:
  - **Multi-AZ DB instance** — standby를 다른 AZ에 생성 (동기 복제, failover용)
  - **Multi-AZ DB cluster** — 1 writer + 2 reader (3개 AZ)
  - **Single-AZ** — 하나의 AZ에만 존재, failover 없음
- 평점: `D+`

**Connectivity** ⚠️ Several misunderstandings.
- Compute resource — EC2와 자동 연결 설정을 해줄지 선택하는 옵션이다. **비용 차이는 없다** — 보안 그룹 규칙을 자동으로 설정해주는 편의 기능일 뿐이다.
- Network type — IPv4/IPv6 선택은 맞다. DB에 접근할 때 사용하는 IP 프로토콜이다.
- VPC — "서버리스의 경우 VPC와 무관하게 존재할 수 있다"는 **틀렸다**. Aurora Serverless도 VPC 안에 존재한다. 모든 RDS/Aurora 인스턴스는 반드시 VPC 안에 있어야 한다.
- DB subnet group — 맞다. 최소 2개 AZ의 서브넷을 포함해야 한다.
- Public access — 맞다. 거의 항상 No.
- Security group — 여러 보안 그룹을 지정하면 **모든 규칙이 합쳐진다(union)**. 예: SG1이 port 3306 허용, SG2가 port 5432 허용이면 둘 다 허용된다.
- Certificate authority — DB 연결 시 SSL/TLS 암호화에 사용할 인증서를 선택하는 옵션이다. 전송 중 데이터 암호화(encryption in transit)와 관련된다.
- 평점: `D+`

**Read replica write forwarding** ❌ Wrong.
- "문제가 생기면 보고하라는 의미" — 아니다.
- Write forwarding은 Aurora 전용 기능으로, **reader instance에서 write 쿼리를 실행하면 자동으로 writer instance로 전달(forward)해주는 기능**이다.
- 장점: 애플리케이션이 reader endpoint만 사용해도 write가 가능해진다. 코드 변경 없이 read/write를 하나의 endpoint로 처리 가능.
- 평점: `F`

**Babelfish settings** — skip은 이해하지만 한 줄 정도는 알아두면 좋다:
- Babelfish는 Aurora PostgreSQL 전용 기능으로, **SQL Server용으로 작성된 애플리케이션을 코드 변경 최소화로 PostgreSQL에서 실행할 수 있게 해주는 호환 레이어**다.
- 평점: `N/A`

**Monitoring** ⚠️ Vague.
- 2가지 옵션:
  - **Standard monitoring** — CloudWatch 기본 메트릭 (CPU, memory, storage, connections 등)
  - **Enhanced monitoring** — OS 수준의 상세 메트릭 (process list, memory breakdown 등). 추가 비용 발생.
- "KMS키를 사용해서 보안을 신경쓰는 것 같다" — 모니터링과 KMS는 관련 없다. KMS는 별도의 encryption 옵션에서 나온다.
- 평점: `D+`

**Aurora vs RDS 차이점** ⚠️ Partially correct.
- "rds는 rdb를 관리하는 서비스이고 aurora는 그 위의 엔진이다" — 맞다.
- "둘 모두 관리형이지만 오로라의 경우 서버리스도 지원한다" — 맞다.
- "rds는 다른 엔진도 지원하지만 오로라는 2개 db만 호환된다" — 맞다.
- 빠진 핵심 차이: Aurora는 **공유 클러스터 스토리지** (6 copies, 3 AZs, auto-grow), 일반 RDS는 **인스턴스별 EBS 볼륨**.
- 평점: `B-`

### Missing console sections

- **DB instance class** — 인스턴스 크기 선택 (db.r6g.large 등). 비용에 가장 큰 영향을 미치는 옵션 중 하나인데 빠져 있다.
- **Storage** (일반 RDS) — 스토리지 타입 (gp3, io2), 크기, IOPS, auto-scaling 설정
- **Database authentication** — Password, IAM DB authentication, Kerberos 중 선택
- **Encryption** — 저장 데이터 암호화 (encryption at rest). KMS 키 선택.
- **Backup** — 자동 백업 보존 기간, 백업 윈도우 설정
- **Maintenance** — 자동 마이너 버전 업그레이드, 유지보수 윈도우 설정
- **Log exports** — CloudWatch Logs로 내보낼 로그 종류 선택
- **Deletion protection** — 실수로 삭제 방지 옵션

### 총평

- 콘솔의 전체 흐름을 따라간 점은 좋다.
- 하지만 여러 옵션에서 추측성 설명이 많고 ("~인 것 같다", "~로 보인다"), 핵심 옵션들이 빠져 있다.
- 특히 **DB instance class, Storage, Backup, Encryption**이 빠진 것은 큰 gap이다 — 이것들이 비용과 운영에 가장 직접적인 영향을 미친다.
- Connectivity에서 "Aurora Serverless는 VPC 밖에 존재할 수 있다"는 오해는 반드시 교정해야 한다.

### 가장 먼저 보완해야 할 것

1. **DB instance class** — 비용의 핵심. 콘솔에서 가장 중요한 선택 중 하나
2. **Connectivity의 VPC 오해** — 모든 RDS/Aurora는 VPC 안에 존재한다
3. **Read replica write forwarding** — forward의 정확한 의미
4. **Secrets Manager vs KMS 구분** — 비밀 값 저장 vs 암호화 키 관리
5. **Backup, Encryption, Deletion protection** — 운영에서 빠질 수 없는 옵션들

## Codex Grade: C+ (69/100)

1차 시도 기준으로는 전체 콘솔 흐름을 따라가려는 시도는 좋다.

- Aurora 전용 옵션과 일반 RDS 옵션을 구분하려는 방향은 있다.
- 하지만 추측성 표현이 많고, 비용과 운영에 직결되는 핵심 옵션이 빠져 있다.
- 특히 `DB instance class`, `Storage`, `Backup`, `Encryption`, `Deletion protection`이 빠진 것은 큰 공백이다.

#### 총평

- 현재 수준은 `처음 훑어본 메모`
- 그러나 `AWS 101 발표/고객 설명용으로는 아직 부족`
- 가장 먼저 보완해야 할 것은 아래 5개다.

1. `DB instance class가 무엇인지`
2. `Secrets Manager와 KMS 차이`
3. `Aurora Serverless도 VPC 안에 존재한다는 점`
4. `Read replica write forwarding의 실제 의미`
5. `Backup / Encryption / Deletion protection 같은 운영 기본 옵션`

#### 잘 모르겠다를 풀어서 설명

##### Templates

- `Production`, `Dev/Test`, `Free tier`는 DB 성격을 바꾸는 마법 옵션이 아니라, 이후 설정들의 기본값을 바꾸는 preset이다.
- 예를 들어 Production은 Multi-AZ, 더 큰 인스턴스, 더 높은 가용성 쪽으로 기본값이 잡히고, Dev/Test는 비용 절감 쪽으로 잡힌다.
- 즉 템플릿의 핵심은 `실제 차이`보다 `기본 추천값 세트`라고 이해하면 된다.

##### Cluster scalability type

- 이 옵션은 Aurora 전용이다.
- `Provisioned`는 고정된 인스턴스 크기를 선택하는 방식이다.
- `Serverless`는 사용량에 맞춰 용량이 자동으로 오르내리는 방식이다.
- `Limitless Database`는 매우 큰 규모의 Aurora 워크로드를 수평 확장하기 위한 특수 옵션이다.
- 여기서 `수직 확장`은 더 큰 인스턴스로 바꾸는 것이고, `수평 확장`은 인스턴스나 클러스터를 더 추가하는 것이다.

##### Credentials management / Secrets Manager / KMS

- `Secrets Manager`는 비밀번호 같은 비밀 값 자체를 저장하고 rotation을 도와주는 서비스다.
- `KMS`는 암호화 키를 관리하는 서비스다.
- 쉽게 말하면:
  - `Secrets Manager` = 비밀번호 보관함
  - `KMS` = 자물쇠의 열쇠 관리
- Secrets Manager가 비밀 값을 저장할 때 내부적으로 KMS 키를 사용할 수 있다.

##### Connectivity

- `Compute resource`는 EC2와 자동 연결 설정을 도와주는 편의 기능이다. 비용 차이는 없다.
- `Network type`은 IPv4만 쓸지, IPv6도 함께 쓸지 정하는 것이다.
- `VPC`는 RDS/Aurora가 들어갈 네트워크를 정하는 것이며, 모든 RDS/Aurora는 VPC 안에 존재한다.
- `DB subnet group`은 DB를 배치할 서브넷 후보 집합이다.
- `Public access`는 외부에서 직접 접근 가능한 공개 엔드포인트를 줄지 여부다.
- `VPC security group`은 DB로 들어오는 허용 규칙을 제어하며, 여러 개를 붙이면 규칙이 합쳐진다.
- `Certificate authority`는 SSL/TLS 연결에 쓰는 인증서 체인을 정하는 옵션이다.

##### Read replica write forwarding

- `forward`는 보고(report)가 아니라 전달(forward)이다.
- Aurora의 reader에서 write 요청이 들어오면 writer로 전달하는 기능이다.
- 즉 애플리케이션이 reader endpoint에 연결되어 있어도 write를 처리할 수 있도록 돕는 기능이다.

##### Monitoring

- `Standard`는 CloudWatch 기본 메트릭이다.
- `Enhanced monitoring`은 OS 수준 메트릭을 더 자세히 보는 옵션이다.
- 이것은 보안용 KMS와는 무관하다.

##### Babelfish

- Babelfish는 Aurora PostgreSQL에서 SQL Server용 애플리케이션을 더 쉽게 옮기도록 도와주는 호환 기능이다.
- 일반적인 AWS 101에서는 `SQL Server 호환 마이그레이션 지원 기능` 정도로만 알아도 충분하다.

#### 발표용으로 바로 쓸 수 있게 고치면 좋은 표현

- `아래 콘솔 옵션 정리는 study/aws/101/images/aws_console/rds01.png 부터 rds12.png 기준으로 이해하면 된다.`

##### DB instance class

- `DB instance class는 CPU와 memory 크기를 정하는 옵션으로, 비용과 성능에 가장 직접적인 영향을 준다.`

##### Templates

- `Templates는 Production, Dev/Test, Free tier 중 하나를 선택해 기본 권장값을 빠르게 적용하는 preset이다.`

##### Credentials management

- `Secrets Manager는 DB 비밀번호 같은 비밀 값을 저장하고 rotation을 도와주고, KMS는 암호화 키를 관리하는 서비스다.`

##### Connectivity

- `RDS와 Aurora는 모두 VPC 안에 생성된다. 여기서는 어떤 VPC, subnet group, security group, public access 설정을 쓸지 정한다.`

##### Availability & durability

- `이 옵션은 Single-AZ인지, Multi-AZ인지 정해서 장애 대응 수준을 선택하는 단계다.`

##### Read replica write forwarding

- `이 기능은 Aurora reader에서 들어온 write 요청을 writer로 전달하는 기능이다.`

#### Terminology

- `RDS` = `Relational Database Service`
- `DB` = `Database`
- `AZ` = `Availability Zone`
- `VPC` = `Virtual Private Cloud`
- `KMS` = `Key Management Service`
- `ACU` = `Aurora Capacity Unit`
- `TLS` = `Transport Layer Security`
- `SSL` = `Secure Sockets Layer`
- `IOPS` = `Input/Output Operations Per Second`
- `CA` = `Certificate Authority`

#### AWS 101 수준에서 추가로 자주 나오는 질문

- RDS와 Aurora는 어떻게 다른가?
- Multi-AZ와 Read Replica는 어떻게 다른가?
- Secrets Manager와 KMS는 어떻게 다른가?
- Public access는 왜 보통 No로 두는가?
- DB subnet group은 왜 필요한가?
- RDS는 왜 VPC 안에 있어야 하는가?
- backup retention period는 왜 중요한가?
- deletion protection은 왜 운영에서 중요한가?

##### RDS와 Aurora는 어떻게 다른가?

- `RDS`는 여러 관계형 DB 엔진을 관리형으로 운영하게 해주는 서비스다.
- `Aurora`는 그 안에 포함되는 AWS 자체의 관계형 DB 엔진이다.
- Aurora는 MySQL/PostgreSQL 호환성과 고가용성, 공유 스토리지 구조를 강점으로 가진다.
- 일반 RDS는 엔진별로 인스턴스 + EBS 기반이고, Aurora는 클러스터 + 공유 스토리지 구조라는 점이 큰 차이다.

##### Multi-AZ와 Read Replica는 어떻게 다른가?

- `Multi-AZ`는 장애 대응과 가용성을 위한 구성이다.
- `Read Replica`는 읽기 부하 분산과 읽기 성능 향상을 위한 구성이다.
- 즉:
  - `Multi-AZ` = failover 목적
  - `Read Replica` = read scaling 목적
- 둘은 비슷해 보여도 목적이 다르다.

##### Secrets Manager와 KMS는 어떻게 다른가?

- `Secrets Manager`는 비밀번호, API key, DB 자격 증명 같은 비밀 값 자체를 저장하고 rotation을 도와준다.
- `KMS`는 그 비밀 값을 암호화할 때 쓰는 키를 관리한다.
- 쉽게 말하면:
  - `Secrets Manager` = 비밀 값 보관함
  - `KMS` = 암호화 키 관리자

##### Public access는 왜 보통 No로 두는가?

- DB는 일반적으로 애플리케이션 서버만 접근하면 되므로 인터넷에 직접 노출할 필요가 없다.
- Public access를 켜면 외부에서 직접 접근 가능한 엔드포인트가 생겨 공격 면이 커진다.
- 그래서 대부분은 private subnet + security group으로 제한하는 것이 기본이다.

##### DB subnet group은 왜 필요한가?

- DB subnet group은 RDS가 배치될 서브넷 후보 집합이다.
- AWS는 이 정보를 바탕으로 DB를 어느 AZ, 어느 subnet에 둘지 결정한다.
- 특히 Multi-AZ 구성을 하려면 여러 AZ의 subnet이 필요하다.

##### RDS는 왜 VPC 안에 있어야 하는가?

- RDS는 네트워크적으로 격리되고 통제된 환경 안에서 동작해야 하기 때문이다.
- VPC 안에 있어야 subnet, route, security group, public/private 접근을 제어할 수 있다.
- Aurora Serverless도 예외가 아니라 VPC 안에 존재한다.

##### backup retention period는 왜 중요한가?

- 자동 백업을 얼마나 오래 보관할지 정하는 값이다.
- 너무 짧으면 장애나 실수 발생 시 복구 시점이 부족할 수 있다.
- 너무 길면 백업 저장 비용이 늘어날 수 있다.
- 운영에서는 복구 요구사항(RPO)에 맞게 정해야 한다.

##### deletion protection은 왜 운영에서 중요한가?

- 실수로 DB를 삭제하는 사고를 막아준다.
- 특히 운영 DB는 삭제 한 번이 큰 장애로 이어질 수 있어서 매우 중요하다.
- AWS 101 수준에서는 `프로덕션 DB에는 거의 항상 켜두는 보호장치`로 이해하면 된다.

##### Cluster scalability type은 replica만 의미하는가?

- 아니다.
- `Cluster scalability type`은 Aurora가 전체적으로 용량을 어떻게 확장할지를 정하는 옵션이다.
- replica는 그중 일부에 불과하다.
- 예를 들어:
  - `Provisioned` = 고정된 DB 인스턴스 크기를 직접 선택
  - `Serverless` = 사용량에 따라 DB 용량이 자동으로 오르내림
  - `Limitless Database` = 매우 큰 규모에서 더 넓게 수평 확장
- 즉 `cluster scalability`는 `replica를 몇 개 둘지`만 의미하는 것이 아니라, `Aurora가 compute capacity를 어떤 방식으로 확장할지`를 뜻한다.

##### Aurora Serverless는 Auto Scaling처럼 이해해도 되는가?

- 비슷한 면은 있지만 완전히 같지는 않다.
- `EC2 Auto Scaling`은 서버 인스턴스를 더 추가하거나 줄이는 방식이다.
- 반면 `Aurora Serverless`는 DB 서비스 내부에서 용량을 자동 조절하는 방식이다.
- 즉:
  - `EC2 Auto Scaling` = 서버 수를 조절
  - `Aurora Serverless` = DB 용량을 자동 조절
- 데이터베이스는 상태를 가지므로, stateless한 웹 서버처럼 단순히 인스턴스 수만 늘리는 개념으로 보면 안 된다.
- AWS 101 수준에서는 `Aurora Serverless는 DB용 자동 확장 기능이지만, EC2 Auto Scaling과 동일한 개념은 아니다`라고 이해하면 된다.
