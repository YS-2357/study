# 260318 Note

## Note taking 1
AWS 101 / WHY, HOW

1. 긴장해서 목소리 빠름
2. 뚝뚝/ 휙
3. IaC??? 안 넣는 것이 좋음
4. CAPTEX-OPEX를 앞으로
5. AI Stack?
6. 가용영역 질문
7. 컴퓨팅 -> Iaas/Paas/Saas 넣었으면
8. Spot instance? 요금 옵션이 좀 길었다. / 70-80점
9. 람다? Paas인가?
10. Auto Scaling은 EC2의 집합인가? -> NLB 붙이는 건가?
11. 스토리지
    - S3는 PaaS서비스인가? 버킷인가? S3안에 버킷인가?
    - 아카이브 저장소 쓰고 싶다(Deep Archive) -> 예: 저희 공문서(법원) 저장 필요 Glacier / 80점
12. EBS -> EKS에도 붙나요? okay
13. EFS -> Linux EFS, Windows SMB FSx -> Direct Connect, VPN, Transit Gateway?
14. IGW - NAT Gateway / 60점
15. ELB는? IP 사용하고 싶을 때는? ALB 인증서 붙이고 싶을 때는? / 0점
16. CloudFront - 저희 캐시 전송
17. DB - Semi-structured에는 어떤 DB?
18. RDS <-> Aurora 차이점 말하는 것 / Good!
    - 오로라와 rds의 차이점을 말하거나 rdb와 rds의 차이점을 말하는 것 중 1 선택
19. DynamoDB - 빠름
20. ElastiCache - 너무 빠름
21. 보안 - AWS 공동 책임, IaaS/Paas/SaaS
22. IAM 계정 - user, group, role, policy
23. Shield - 도메인이 뭐지? Route 53
24. WAF랑 AWS F/W - aws firewall 서비스가 있나?

## Note taking 2
q.
법원의 공문서를 저장 및 보관하는 직무 - 서기관
- 한번 저장하면 검색까지 1년 이상 걸림, 접근을 자주하지는 않을 것 같음
- 저장소를 클라우드로 옮기고 싶음
- 근데 문서가 너무 많은데 어떻게 해야할까요?
a.
옮기는 방법 설명~
고객사의 케이스에 따른 저장소 추천을 위해 역질문
q.
KT 직원 교육 AIVLE 서비스
- 온프레미스 환경인데 AWS 마이그레이션 하고 싶다
- EC2 환경이 궁금함
- 우리도 load balancer를 사용하는데
- auto scaling에 대해서 궁금하다. 어떻게 설정해야하고 어떻게 구성되어있나?
- NLB이런거는 기본적으로 탑재되어 있나요?
q.
Lambda는 SaaS인가? 아니면 IaaS? PaaS인가요?
q.
포스코에서 EC2를 쓰고 있는데 근데 그리 잘 사용하지는 않는다. Spot Instance에 대해서 언급하셨는데 제 케이스에서는 그냥 사용해도 되나요?
- 혹시 프로덕션 환경에서 사용해도 되나요?
q.
EBS에 EKS(?), ECS(?)도 붙나요?
q.
저희는 온프레미스 파일 시스템 사용하는데~
- AWS와 연동 어떻게 하나요?
- VPN? Direct Connection?
- Transit Gateway?
q.
저는 AhnLab 담당자 입니다. 네트워크 보안 연결 직무를 담당하고 있는데. AWS VPC 내에서 서로 어떻게 연결되나요? 서브넷 개념은 뭔가요?
q.
네트워크 담당자가 아닌데 네트워크 업무를 맡게되었습니다. 설명해주신 Load Balancer 중 ALB, NLB, GBLW 이런 것들은 어느 상황에서 사용해야 하는 건가요?
q.
DynamoDB를 사용하라고 전달이 떨어졌는데 제 케이스가 RDB를 사용해야 하는지 NoSQL DB를 써야하는지 모르겠다.
아이 band 데이터 사업, 경도, 위도, 날씨 등의 telemetry 값이 나옴 이런 log값들을 어떤 DB에 넣어야 최적화가 될까요?
애기들의 나이, 이름, 성별 같은 정형 데이터들은 어디다가 넣어야할까요?