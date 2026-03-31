## 1차 시도

### Create function 

1. Author from scratch
사용자가 직접 만드는 경우
2. Use a blueprint
청사진을 통해서 만드는 경우
3. Container image
container의 이미지를 배포하는 경우

3가지의 경우가 존재한다.
어느 경우를 가장 많이 사용하는지는 잘 모르겠다.

### Basic information

#### Function name
이름 설정의 단계
겹치지 않으면서 구별이 쉬운 규칙을 통해 만들기를 권장

#### Runtime
프로그래밍 언어를 선택하는 단계
노드js부터 파이썬, 루비 등 다양한 언어를 지원한다.

#### Architecture
arm프로세서인지, x86프로세서인지 선택하는 단계
어떤 아키텍처 위에서 런타임이 돌아갈 지 선택한다.

#### Permissions 
기본적으로 클라우드워치에 연동되어 처리한다.
assumeRole을 위해 필요한 권한으로 보인다.
처리하는 작업이 무엇인지에 따라 임시권한을 붙여서 맡기면 된다.

#### Additional configurations

##### Networking

###### Function URL
람다를 위한 endpoint url을 선택하는 옵션
이게 존재하면 http/https 호출이 가능한건가?

###### VPC
람다는 서버리스이므로 vpc와 무관하지만 아키텍쳐 흐름상 vpc내부에서만 사용되는 경우가 존재한다.
이를 위해서 prviate 자원과 연동을 선택하는 옵션

##### Security & governance

###### Tenant isolation mode - new
람다를 위해 서버? 컴퓨팅 자원? 하나를 온전히 할당하는 지를 선택하는 옵션

###### Code signing
코드 서명으로 코드가 변경되지 않도록 관리하는 옵션

###### Encryption with an AWS KMS customer managed key
기본적인 aws의 키로 암호화하는 것이 아니라 사용자가 관리하는 키로 암호화하는 방식을 선택하는 옵션

###### Tags
태그 관리 옵션

---

## Kiro Grade: B (76/100)

### Per-section feedback

**Create function (3 options)** ✅ Correct.
- 3가지 옵션 모두 맞다.
- "어느 경우를 가장 많이 사용하는지 모르겠다" — **Author from scratch**가 가장 많이 사용된다. Blueprint는 학습/프로토타입용, Container image는 복잡한 의존성이 있을 때 사용한다.
- 평점: `B+`

**Function name** ✅ Correct.
- 추가: 리전 내에서 유일해야 한다. 최대 64자. 공백 불가.
- 평점: `B+`

**Runtime** ✅ Correct.
- "프로그래밍 언어를 선택하는 단계" — 맞다.
- 추가: 콘솔 코드 에디터는 Node.js, Python, Ruby만 지원한다. Java, .NET, Go는 코드를 로컬에서 작성 후 zip 또는 container로 업로드해야 한다.
- 평점: `A-`

**Architecture** ✅ Correct.
- arm(Graviton)과 x86 선택이라는 점 맞다.
- 추가: **arm64 (Graviton2)가 x86 대비 ~20% 저렴하고 성능도 비슷하거나 더 좋다.** 특별한 이유가 없으면 arm64를 권장한다.
- 평점: `A-`

**Permissions** ⚠️ Partially correct.
- "클라우드워치에 연동되어 처리한다" — 맞다. 기본 실행 역할(execution role)에 CloudWatch Logs 권한이 포함된다.
- "assumeRole을 위해 필요한 권한" — 방향은 맞지만 더 정확히는: Lambda 함수가 실행될 때 **IAM execution role을 assume**한다. 이 role에 붙은 정책이 Lambda가 할 수 있는 일을 결정한다.
- 콘솔에서의 옵션:
  - **Create a new role with basic Lambda permissions** (기본) — CloudWatch Logs 권한만 포함
  - **Use an existing role** — 이미 만든 role을 선택
  - **Create a new role from AWS policy templates** — 템플릿에서 선택 (S3 read, DynamoDB access 등)
- 예: Lambda가 S3에서 파일을 읽어야 하면 execution role에 `s3:GetObject` 권한을 추가해야 한다.
- 평점: `C+`

**Function URL** ✅ Good question.
- "http/https 호출이 가능한건가?" — **맞다.** Function URL을 활성화하면 Lambda에 고유한 HTTPS endpoint가 생긴다 (e.g. `https://abc123.lambda-url.ap-northeast-2.on.aws/`).
- API Gateway 없이 직접 HTTP 호출이 가능하다.
- Auth type 2가지: **AWS_IAM** (IAM 인증 필요) / **NONE** (누구나 호출 가능 — 주의 필요)
- 간단한 webhook이나 API에 유용하다. 복잡한 라우팅이 필요하면 API Gateway를 쓴다.
- 평점: `B+`

**VPC** ✅ Correct.
- "서버리스이므로 vpc와 무관하지만 아키텍처 흐름상 vpc 내부에서만 사용되는 경우가 존재한다" — 정확하다.
- 대표적인 경우: private subnet의 RDS나 ElastiCache에 접근해야 할 때.
- 주의: VPC에 연결하면 **cold start가 길어질 수 있다** (ENI 생성 때문). 필요한 경우에만 사용 권장.
- 평점: `A-`

**Tenant isolation mode** ⚠️ Partially correct.
- "컴퓨팅 자원 하나를 온전히 할당하는지 선택" — 방향은 맞다.
- 더 정확히는: **Standard** (기본) = 다른 Lambda 함수와 하드웨어 공유 / **Dedicated** = 전용 하드웨어에서 실행. EC2의 Dedicated tenancy와 같은 개념이다.
- 규제/보안 요구가 있을 때만 사용. 비용이 더 높다.
- 평점: `B-`

**Code signing** ✅ Correct.
- 코드가 신뢰할 수 있는 소스에서 왔고 변경되지 않았음을 검증하는 기능이다.
- 평점: `B+`

**Encryption (KMS)** ✅ Correct.
- 기본은 AWS managed key로 암호화. Customer managed key를 선택하면 키 rotation, 접근 제어를 직접 관리할 수 있다.
- 환경 변수(environment variables)의 암호화에 주로 관련된다.
- 평점: `B+`

**Tags** ✅ Fine.
- 평점: `B+`

### Missing console sections

- **Environment variables** — Lambda 함수에 전달하는 key-value 설정값. DB 연결 문자열, API 키 등을 코드 밖에서 관리할 수 있다. AWS 101에서 자주 나오는 주제.
- **Memory / Timeout** — 생성 후 Configuration 탭에서 설정하지만 핵심 옵션이다:
  - **Memory**: 128MB ~ 10,240MB. 메모리를 올리면 CPU도 비례해서 올라간다.
  - **Timeout**: 최대 15분. 기본 3초. 시간 초과하면 함수가 강제 종료된다.
- **Triggers** — Lambda를 호출하는 이벤트 소스. S3 업로드, API Gateway 요청, DynamoDB stream, CloudWatch Events, SQS 메시지 등. "어떤 이벤트가 Lambda를 실행시키는가"가 Lambda의 핵심 개념이다.
- **Layers** — 공통 라이브러리를 여러 Lambda 함수에서 공유하는 기능.
- **Concurrency** — 동시 실행 수 제한. Reserved concurrency / Provisioned concurrency (cold start 방지).

### 총평

- 전체적으로 이전 서비스들보다 이해도가 높다. 특히 VPC 연결의 이유, Function URL의 의미를 스스로 추론한 점이 좋다.
- Architecture에서 arm/x86 구분을 아는 것은 computing 공부가 연결된 결과다.
- 하지만 **Triggers, Memory/Timeout, Environment variables**가 빠져 있다 — 이것들이 Lambda 운영의 핵심이다.
- Lambda에서 가장 자주 나오는 질문: "EC2와 Lambda는 언제 각각 쓰는가?", "cold start가 뭔가?", "최대 실행 시간은?" — 이 3가지는 반드시 답할 수 있어야 한다.

### 가장 먼저 보완해야 할 것

1. **Triggers** — Lambda의 핵심. 어떤 이벤트가 함수를 실행시키는가
2. **Memory / Timeout** — 비용과 성능에 직접 영향. 메모리 ↑ = CPU ↑ = 비용 ↑
3. **Environment variables** — 코드 밖에서 설정값 관리
4. **Permissions의 3가지 콘솔 옵션** — new role / existing role / policy template
5. **Cold start** — VPC 연결 시 특히 중요. Provisioned concurrency로 해결 가능

---

## 2차 시도

### Create function 

1. Author from scratch
사용자가 직접 만드는 경우
2. Use a blueprint
청사진을 통해서 만드는 경우
3. Container image
container의 이미지를 배포하는 경우

보통은 from scratch방식을 많이 사용한다.

### Basic information

#### Function name
이름 설정의 단계
겹치지 않으면서 구별이 쉬운 규칙을 통해 만들기를 권장

#### Runtime
프로그래밍 언어를 선택하는 단계
노드js부터 파이썬, 루비 등 다양한 언어를 지원한다.

#### Architecture
arm프로세서인지, x86프로세서인지 선택하는 단계
어떤 아키텍처 위에서 런타임이 돌아갈 지 선택한다.

#### Permissions 
기본적으로 클라우드워치에 연동되어 처리한다.
람다 함수가 실행될 때 IAM execution role을 assume한다.
이 롤에 붙은 정책이 바로 람다가 할 수 있는 권한이다ㅓ.

#### Additional configurations

##### Networking

###### Function URL
람다를 위한 endpoint url을 선택하는 옵션
이게 존재하면 http/https 호출이 가능하다.

###### VPC
람다는 서버리스이므로 vpc와 무관하지만 아키텍쳐 흐름상 vpc내부에서만 사용되는 경우가 존재한다.
이를 위해서 prviate 자원과 연동을 선택하는 옵션
vpc와 연결하면 cold start가 길어질 수 있다. 

##### Security & governance

###### Tenant isolation mode - new
람다를 위해 서버? 컴퓨팅 자원? 하나를 온전히 할당하는 지를 선택하는 옵션
선택하지 않는다면 여러 람다가 공유하는 모양새가 된다.
규제/보안 요구가 존재하는 경우 선택한다.

###### Code signing
코드 서명으로 코드가 변경되지 않도록 관리하는 옵션
신뢰할 수 있는 소스에서 왔고 변경되지 않음을 관리하는 증명한다.

###### Encryption with an AWS KMS customer managed key
기본적인 aws의 키로 암호화하는 것이 아니라 사용자가 관리하는 키로 암호화하는 방식을 선택하는 옵션

###### Tags
태그 관리 옵션

#### Function overview 
함수를 만들고 나면 트리거와 데스티네이션, 코드소스 등을 다룰 수 있다.
트리거는 람다를 실행시키는 경우를 의미하고 데스티네이션은 람다의 결과물이 도달할 장소를 의미한다.
사이에 sqs 버퍼를 넣을 수도 있다.
코드는 실제로 코드를 만들어 넣으면된다. 
테스트, 모니터링 등등 다양한 기능을 보장한다.

---

## Codex Grade: B+ (82/100)

2차 시도는 상당히 좋아졌다.

- 1차에서 부족했던 `Function URL`, `VPC`, `cold start`, `execution role`이 모두 보완되었다.
- 전체 흐름도 Lambda를 `서버리스 compute + event driven` 관점에서 잘 따라가고 있다.
- 다만 아직 `Triggers`, `Memory / Timeout`, `Environment variables`, `Concurrency`가 빠져 있어서 운영 관점 설명은 완성되지 않았다.

#### 총평

- 현재 수준은 `AWS 101 발표용 초안으로는 꽤 좋음`
- 그러나 `실제 운영 질문 대응까지는 조금 더 보완 필요`
- 가장 먼저 보완해야 할 것은 아래 5개다.

1. `Trigger가 Lambda의 핵심 실행 구조라는 점`
2. `Memory와 Timeout이 비용/성능에 직접 영향 준다는 점`
3. `Environment variables`
4. `Reserved / Provisioned concurrency`
5. `Destination과 Trigger의 차이`

#### 잘 모르겠다를 풀어서 설명

##### Create function

- 세 가지 생성 방식 중에서 가장 흔한 것은 `Author from scratch`다.
- `Blueprint`는 학습이나 빠른 프로토타입용이다.
- `Container image`는 의존성이 크거나, zip 배포보다 컨테이너 방식이 편한 경우에 쓴다.

##### Permissions

- Lambda는 실행될 때 `execution role`을 assume한다.
- 이 role에 붙은 policy가 곧 Lambda가 할 수 있는 AWS 작업이다.
- 예를 들어 S3에서 파일을 읽으려면 그 role에 `s3:GetObject` 같은 권한이 있어야 한다.
- CloudWatch Logs 기록 권한은 기본적으로 많이 붙는다.

##### Function URL

- 네가 이해한 대로 맞다.
- Function URL을 켜면 Lambda에 직접 호출 가능한 HTTPS endpoint가 생긴다.
- API Gateway 없이 간단한 webhook이나 간단한 API를 만들 때 유용하다.
- 대신 인증 방식(`AWS_IAM` 또는 `NONE`)을 조심해야 한다.

##### VPC

- Lambda는 기본적으로 VPC 밖에서 단독으로 동작할 수도 있다.
- 하지만 private subnet의 RDS, ElastiCache, 내부 서비스에 접근하려면 VPC 연결이 필요하다.
- 그래서 `서버리스지만 필요하면 VPC 안으로 들어간다`고 이해하면 된다.
- VPC 연결 시 cold start가 길어질 수 있다는 점도 좋은 포인트다.

##### Tenant isolation mode

- 이 옵션은 Lambda 실행 환경을 다른 함수와 공유할지, 전용 하드웨어에서 실행할지를 고르는 개념이다.
- 기본은 공유 환경이고, 전용 격리는 규제/보안 요구가 있을 때만 본다.
- AWS 101에서는 `기본은 공유, 특수 요구 시 dedicated` 정도로 이해하면 충분하다.

##### Function overview

- `Trigger`는 Lambda를 실행시키는 원인이다.
- 예:
  - S3 업로드
  - API Gateway 요청
  - EventBridge 스케줄
  - SQS 메시지
- `Destination`은 Lambda 실행 결과를 보내는 곳이다.
- 즉:
  - `Trigger` = 시작점
  - `Destination` = 결과 도착점

#### 발표용으로 바로 쓸 수 있게 고치면 좋은 표현

- `아래 콘솔 옵션 정리는 study/aws/101/images/aws_console/lambda1.png, lambda2.png, lambda-function.png 기준으로 이해하면 된다.`

##### Permissions

- `Lambda는 실행될 때 IAM execution role을 assume하고, 이 role에 붙은 policy 범위 안에서만 AWS 작업을 수행할 수 있다.`

##### Function URL

- `Function URL을 사용하면 Lambda를 직접 호출할 수 있는 HTTPS endpoint를 만들 수 있다.`

##### VPC

- `Lambda는 기본적으로 서버리스로 동작하지만, private subnet의 RDS 같은 자원에 접근할 때는 VPC 연결이 필요하다.`

##### Trigger

- `Trigger는 어떤 이벤트가 Lambda를 실행시키는지를 의미한다. S3 업로드, API Gateway 요청, SQS 메시지 등이 대표적이다.`

##### Destination

- `Destination은 Lambda 실행 결과를 어디로 보낼지 정하는 기능이다.`

#### Terminology

- `Lambda` = `AWS Lambda`
- `IAM` = `Identity and Access Management`
- `VPC` = `Virtual Private Cloud`
- `KMS` = `Key Management Service`
- `SQS` = `Simple Queue Service`
- `SDK` = `Software Development Kit`
- `URL` = `Uniform Resource Locator`
- `HTTPS` = `Hypertext Transfer Protocol Secure`
- `CPU` = `Central Processing Unit`
- `ENI` = `Elastic Network Interface`

#### AWS 101 수준에서 추가로 자주 나오는 질문

- Lambda와 EC2는 언제 각각 쓰는가?
- Lambda의 최대 실행 시간은 얼마인가?
- cold start는 무엇인가?
- Lambda를 VPC에 붙이면 왜 느려질 수 있는가?
- Memory를 늘리면 왜 CPU도 같이 늘어나는가?
- Trigger와 Destination은 어떻게 다른가?
- Function URL과 API Gateway는 어떻게 다른가?
- execution role은 왜 필요한가?

##### Lambda와 EC2는 언제 각각 쓰는가?

- `Lambda`는 이벤트 기반, 짧은 실행, 서버 관리 최소화가 중요할 때 적합하다.
- `EC2`는 서버를 직접 제어해야 하거나, 오래 실행되는 애플리케이션, 복잡한 OS 설정이 필요할 때 적합하다.
- 쉽게 말하면:
  - `Lambda` = 서버를 덜 신경 쓰는 짧은 작업
  - `EC2` = 서버 제어가 필요한 일반적인 서버 워크로드

##### Lambda의 최대 실행 시간은 얼마인가?

- 최대 `15분`이다.
- 시간을 초과하면 함수는 강제 종료된다.

##### cold start는 무엇인가?

- Lambda가 오랜만에 호출되거나 새 실행 환경이 필요할 때 초기 실행 환경을 준비하는 시간을 말한다.
- 이때 함수 시작이 평소보다 느려질 수 있다.
- 그래서 초기 응답 지연이 생길 수 있다.

##### Lambda를 VPC에 붙이면 왜 느려질 수 있는가?

- VPC 안의 리소스와 통신하려면 네트워크 인터페이스(ENI) 같은 준비 작업이 필요하기 때문이다.
- 이 과정 때문에 cold start가 더 길어질 수 있다.
- 그래서 private 자원 접근이 꼭 필요할 때만 VPC 연결을 하는 편이 좋다.

##### Memory를 늘리면 왜 CPU도 같이 늘어나는가?

- Lambda는 메모리 설정에 비례해 CPU도 같이 할당한다.
- 그래서 메모리를 올리면 실행 속도가 빨라질 수 있다.
- 대신 비용도 함께 늘어난다.

##### Trigger와 Destination은 어떻게 다른가?

- `Trigger`는 Lambda를 실행시키는 시작 이벤트다.
- `Destination`은 Lambda 실행 결과를 보내는 곳이다.
- 즉:
  - `Trigger` = 실행 시작 원인
  - `Destination` = 실행 결과 전달 위치

##### Function URL과 API Gateway는 어떻게 다른가?

- `Function URL`은 Lambda를 바로 호출할 수 있는 간단한 HTTPS endpoint다.
- `API Gateway`는 인증, 라우팅, 요청 변환, throttling 같은 API 기능이 더 풍부하다.
- 간단한 공개/내부 호출은 Function URL로 충분할 수 있고, 복잡한 API는 API Gateway가 더 적합하다.

##### execution role은 왜 필요한가?

- Lambda가 AWS 리소스에 접근할 때 자기 권한으로 직접 접근하는 것이 아니라, execution role을 assume해서 권한을 얻기 때문이다.
- 이 role에 붙은 policy가 Lambda가 할 수 있는 일을 결정한다.
- 예를 들어 S3 읽기, DynamoDB 쓰기, CloudWatch Logs 기록 같은 권한이 여기에 들어간다.
