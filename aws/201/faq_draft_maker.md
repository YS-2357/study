# CS Inquiry Draft Assistant — Scenario Design

## What It Is

고객사의 CS 인입 문의에 대해 AI가 초안을 생성하고, CS 스태프가 검토 및 수정 후 답변을 전송하는 시스템이다. 하루에 수백 건의 유사 문의를 처음부터 직접 작성하는 부담을 줄이는 것이 목표다. AI가 자동으로 답변하는 것이 아니라, CS 스태프가 최종 판단을 내린다.

Prerequisites fixed: [AWS CDK](aws_services/07_aws_cdk.md), [Bedrock AgentCore](aws_services/02_amazon_bedrock_agentcore.md), [Strands SDK](aws_services/01_strands_agents_sdk.md).

## How It Works

### Client-provided data

| Data | Detail | Role |
|------|--------|------|
| Q&A records | 10,000건. {카테고리, 제목, 내용, 답변} | RAG 검색 소스 |
| Product info | 가격, 크기, 색상 등 구체적인 정형 데이터 | RAG 검색 소스 |
| FAQ data | 정제된 FAQ 문서 | RAG 검색 소스 |
| Prompt guide | 답변 작성 지침 (톤, 포맷, 제약) | 시스템 프롬프트로 주입 |

카테고리는 9개로 사전 분류되어 있다. 고객 문의 UI도 자체 제작하며 카테고리, 제목, 내용을 입력받는다.

### Q&A selection strategy: 10,000 → 1,000

전체 10,000건을 KB에 넣지 않는다. 품질과 균형을 위해 1,000건을 선별한다.

```
Selection rule:
  - 카테고리 레코드 수가 적을수록 가중치 높게 (소수 카테고리 보호)
  - 같은 카테고리 내에서는 k-NN 유사도로 대표 레코드 선별
  - 결과: 카테고리 균형이 맞춰진 1,000건
```

선별 작업은 Lambda로 처리한다 (10,000건은 Lambda 범위 내). 선별된 1,000건은 S3로 내보내 KB에 인제스트한다.

### Storage design

**RDS MySQL (t3.micro)** — 모든 데이터의 중앙 관리 레이어

```
qa_records          원본 10,000건 저장. is_selected 플래그로 선별 여부 관리.
products            가격, 크기, 색상 등 정형 상품 데이터
inquiries           고객 문의 (category, title, content, status)
drafts              AI 생성 초안
responses           CS 스태프 최종 답변
staff               CS 스태프 계정
```

**S3** — KB 인제스트 소스

```
selected-qa/        선별된 1,000건 Q&A (RDS에서 export)
product-info/       상품 정보 문서
faq/                FAQ 문서
finalized/          완료된 답변 (일별 sync 소스)
```

**Knowledge Bases** — 검색 레이어 (S3를 소스로 읽음)

```
selected Q&A, product info, FAQ → chunk → embed → index
```

**SSM Parameter Store** — 프롬프트 가이드 저장 (코드 배포 없이 수정 가능)

### Three pipelines

```
1. 초기 인제스트 (최초 1회 또는 데이터 변경 시)

   RDS qa_records (10,000건)
     → Selection Lambda (가중치 + k-NN → 1,000건 선별)
     → S3 (selected-qa/)
     → Knowledge Bases ingestion

   Product info, FAQ
     → S3 (product-info/, faq/)
     → Knowledge Bases ingestion

2. 실시간 초안 생성 (문의 1건당)

   고객 문의 (카테고리, 제목, 내용) → EC2 UI
     → API Gateway → Lambda (Strands agent)
         → KB 검색 (같은 카테고리 필터 + 유사도)
         → Bedrock 생성 (system prompt: SSM 프롬프트 가이드)
         → 초안 생성
     → RDS: inquiries + drafts 저장 (status: pending)
     → CS 스태프 admin 페이지에서 초안 확인

3. CS 스태프 검토 및 일별 강화

   CS 스태프 → admin 페이지 (EC2)
     → 초안 수정 → 최종 답변 제출
     → RDS: responses 저장 (status: done)
     → S3: finalized/ 저장

   EventBridge (매일 02:00)
     → Batch Lambda
         → S3 finalized/ 읽기 → KB sync (Knowledge Bases 재인제스트)
```

### Infrastructure

| Component | Service | Spec | Why |
|-----------|---------|------|-----|
| UI (고객 문의 + CS 어드민) | [EC2](../../aws/101/aws_services/05_amazon_ec2.md) | t3.micro | Advisor 권고 — production 경험 |
| DB (중앙 데이터 관리) | [RDS MySQL](../../aws/101/aws_services/10_amazon_rds.md) | t3.micro | Advisor 권고 — 관계형 스키마 필요 |
| KB 소스 스토리지 | [S3](../../aws/101/aws_services/19_amazon_s3.md) | — | KB가 S3를 데이터 소스로 요구 |
| RAG 검색 | [Knowledge Bases](aws_services/05_amazon_bedrock_knowledge_bases.md) | — | chunking, embedding, 검색 관리 |
| 초안 생성 | [Bedrock](aws_services/04_amazon_bedrock.md) + [Strands](aws_services/01_strands_agents_sdk.md) | — | Fixed prerequisite |
| 서버리스 처리 | [Lambda](aws_services/09_aws_lambda.md) | — | 선별, 인제스트, 초안 생성, batch |
| API 라우팅 | [API Gateway](aws_services/10_amazon_api_gateway.md) | — | EC2 UI → Lambda 연결 |
| 프롬프트 가이드 | [SSM Parameter Store](aws_services/14_aws_ssm_parameter_store.md) | — | 코드 배포 없이 수정 가능 |
| 일별 sync 트리거 | EventBridge | — | 매일 KB 강화 |
| 모니터링 | [CloudWatch](aws_services/08_amazon_cloudwatch.md) | — | Lambda 로그, 초안 지연, RDS 쿼리 |

### RDS schema

```sql
-- 원본 Q&A (클라이언트 제공)
qa_records (id PK, category, title, content, answer, is_selected BOOL, created_at)

-- 상품 정보 (클라이언트 제공)
products (id PK, name, price, size, color, description, updated_at)

-- 고객 문의 라이프사이클
inquiries  (id PK, category, title, content, status ENUM(pending/done), created_at)
drafts     (id PK, inquiry_id FK, content, created_at)
responses  (id PK, inquiry_id FK, staff_id FK, final_content, sent_at, s3_key)
staff      (id PK, name, email)
```

### Security

| Boundary | Enforce |
|----------|---------|
| 고객 → UI | 인증, rate limiting, WAF |
| CS 스태프 → admin | 역할 기반 접근 제어 |
| Lambda → Bedrock / KB | IAM role, 최소 권한 |
| Lambda → RDS | IAM 인증, 자격증명 SSM 저장 |
| 고객 문의 입력 | 프롬프트 인젝션 방어를 위한 입력 검증 |
| 프롬프트 가이드 | SSM 저장 — 사용자가 직접 수정 불가 |

## Example

```
[고객]
  문의 제출 (카테고리: 배송, 제목: 배송 지연, 내용: 주문한 지 5일이 지났는데...)
  → EC2 UI → API Gateway → Lambda

[Lambda: Strands agent]
  → KB 검색 (카테고리: 배송 필터 + 유사도)
      → 관련 Q&A, 상품 정보, FAQ 반환
  → Bedrock Claude Sonnet
      (system prompt: SSM 프롬프트 가이드)
      (context: 검색 결과)
  → 초안 생성: "안녕하세요. 현재 물류 지연이 발생하고 있으며..."
  → RDS: inquiries + drafts 저장 (status: pending)

[CS 스태프]
  → admin 페이지 (EC2)에서 초안 확인
  → 수정: "죄송합니다. 현재 택배사 파업으로 인해..."
  → 제출 → API Gateway → Lambda
      → RDS: responses 저장 (status: done)
      → S3: finalized/ 저장

[매일 02:00 EventBridge]
  → Batch Lambda → S3 finalized/ 읽기 → KB 재인제스트
```

## Why It Matters

CS 스태프는 느린 것이 아니라 매번 처음부터 작성해야 한다는 것이 문제다. RAG 초안이 80% 정확하면, 스태프의 일은 작성이 아니라 검토와 수정이 된다.

피드백 루프가 핵심이다. 완료된 답변이 매일 KB에 쌓이면, 비슷한 문의에 대한 초안 품질이 계속 높아진다. 시스템이 사용될수록 좋아진다.

> **Tip:** 프롬프트 가이드는 SSM에 저장한다. CS 매니저가 코드 배포 없이 톤과 포맷을 수정할 수 있다.

## Decomposition

**One unit = one reason to change.**

| Unit | One reason to change |
|------|----------------------|
| Selection Lambda | 선별 기준 (가중치, k-NN 파라미터) 변경 시 |
| KB ingestion | 임베딩 모델 또는 청킹 전략 변경 시 |
| Draft generation Lambda | 검색 전략 또는 Bedrock 모델 변경 시 |
| RDS schema | 문의 라이프사이클 구조 변경 시 |
| SSM prompt guide | 답변 톤, 포맷, 제약 변경 시 |
| EventBridge daily sync | KB 강화 주기 또는 배치 로직 변경 시 |
| EC2 UI | 화면 구성 또는 UX 변경 시 |

## Design Decisions

### D1 — 사용 목적 재정의

**처음 생각:** FAQ 문서 자동 생성 도구.

**수정:** 실시간 CS 문의 초안 생성 도구.

**이유:** 고객사의 실제 문제는 하루 수백 건의 유사 문의를 처음부터 작성하는 것이다. AI가 초안을 만들고 CS가 수정하면 된다.

---

### D2 — 10,000건에서 1,000건 선별

**이유:** 10,000건 전체를 KB에 넣으면 노이즈가 많아진다. 카테고리 균형을 맞추고 대표성 있는 1,000건만 사용한다.

**전략:** 카테고리 수가 적을수록 가중치 높게 (소수 카테고리 보호), 같은 카테고리 내 k-NN으로 유사 레코드 제거.

---

### D3 — RDS를 중앙 데이터 관리 레이어로

**이유:** 10,000건 Q&A, 상품 정보, 문의 라이프사이클을 한 곳에서 관리해야 한다. Advisor가 production 경험을 위해 RDS MySQL t3.micro를 권고했다.

**S3 역할:** KB 인제스트 소스 전용. RDS에서 선별된 데이터를 S3로 export해 KB에 인제스트한다.

---

### D4 — EC2 t3.micro for UI

**이유:** Advisor가 production 경험을 위해 권고. S3+CloudFront(정적)나 Lambda(서버리스)와 달리 실제 서버 운영 경험을 쌓을 수 있다.

**트레이드오프:** 항상 켜져 있는 비용 발생. 단, t3.micro는 비용이 낮다.

---

### D5 — Knowledge Bases for retrieval

**이유:** 선별된 Q&A, 상품 정보, FAQ를 KB 하나로 관리. 청킹과 임베딩을 자동 처리한다.

**카테고리 필터:** KB 검색 시 카테고리 메타데이터로 사전 필터링해 관련 카테고리만 검색.

---

### D6 — Prompt guide in SSM

**이유:** CS 매니저가 답변 톤이나 포맷을 바꿀 때 코드 배포가 필요 없다. SSM에서 값만 수정하면 된다.

---
← [AWS 201](00_overview.md) | [Overview](00_overview.md) | Next: [Overview](00_overview.md) →
