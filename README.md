<div align="center">

<img src="./assets/heechan-industrial-ai-profile-banner-v6.jpg" alt="스마트 항만, 반도체 팹, 산업 AI 관제 시스템을 연결한 최희찬의 산업 AI 포트폴리오" width="100%" />

# Heechan Choi

### 반도체 제조를 중심으로 산업 현장의 문제를 AI 의사결정 지원 시스템으로 구현합니다

전자공학·스마트팩토리를 바탕으로 **반도체 품질관리, 해양 운항 최적화, 자율시스템 AI 보안** 프로젝트를 만들고 있습니다.<br>
데이터와 가정을 공개하고, 결과뿐 아니라 실패 조건과 한계까지 검증 가능한 형태로 기록합니다.

*I build reviewable Industrial AI systems for semiconductor manufacturing, operational decision support, and autonomous-system reliability—with reproducible experiments and clearly documented limitations.*

[![대표 프로젝트](https://img.shields.io/badge/대표_프로젝트-4개-39D6C4?style=for-the-badge&labelColor=0B1117)](#대표-프로젝트--featured-projects)
[![실행 데모](https://img.shields.io/badge/LIVE-FABGUARD_AI-E4A83D?style=for-the-badge&labelColor=0B1117&logo=vercel&logoColor=white)](https://fabguard-ai.vercel.app/)
[![협업](https://img.shields.io/badge/OPEN_TO-TECHNICAL_COLLABORATION-5A91B8?style=for-the-badge&labelColor=0B1117)](#기술-협업--technical-collaboration)

</div>

> **한 문장으로:** 반도체 제조 AI를 중심축으로, 서로 다른 산업 현장의 데이터를 사람이 검토할 수 있는 의사결정 지원 시스템으로 연결합니다.

## 무엇을 하는가 | What I build

| 분야 | 쉽게 말하면 | 기술적으로 남기는 결과 |
|---|---|---|
| 반도체 제조 AI | 불량 위험이 높은 생산 건을 먼저 점검하도록 지원 | leakage control, temporal validation, calibrated risk ranking, Top-K metrics |
| 산업 데이터 운영 | 결측·중복·시간변화가 있는 센서 데이터를 안정적으로 처리 | data contracts, drift monitoring, edge integration, failure handling |
| 해양 의사결정 | 연료 구매와 운항 판단을 시뮬레이션으로 비교 | Gymnasium environment, rule-based policies, Double DQN, safety constraints |
| 자율시스템 보안 | AI가 교란된 입력에서도 얼마나 견디는지 검증 | clean baseline, FGSM evaluation, integrity hashes, reproducible bundles |
| 프로젝트 리딩 | 문제 정의부터 실험·발표·공개 데모까지 연결 | scope decisions, documentation, GitHub review, public deployment |

## 대표 프로젝트 | Featured projects

### 01 · [FabGuard AI](https://github.com/heechan9/fabguard-ai) — 반도체 생산 위험 우선점검

<a href="https://github.com/heechan9/fabguard-ai"><img src="./assets/projects/fabguard.svg" alt="FabGuard AI 프로젝트 미리보기" width="100%" /></a>

**어떤 문제인가?**  
반도체 생산데이터는 변수와 결측치가 많고 불량 비율이 낮아, 모든 생산 건을 같은 강도로 검사하기 어렵습니다.

**무엇을 만들었나?**

- UCI SECOM 공개데이터 1,567건과 측정변수 590개를 이용해 고위험 생산 건의 점검 순위를 제시
- 누출 방지 전처리, 시간순 홀드아웃, PR-AUC와 Top-K 포착률, 확률 보정 및 walk-forward 검증 적용
- 상위 10% 점검 대상에서 실제 불량 24건 중 5건을 포착
- Fledge 기반 엣지 운영 계층과 장기 시계열 데이터 품질 분석으로 확장 중
- 자동 판정, 실제 팹 수율 개선 또는 현장 배포 성과로 과장하지 않고 공개데이터 실험 범위를 명시

**My role:** Owner · problem framing · validation direction · release decisions  
**Technical focus:** semiconductor quality risk ranking, temporal validation, edge operations, data quality and drift

**확인하기:** [실행 데모](https://fabguard-ai.vercel.app/) · [실험 계약](https://github.com/heechan9/fabguard-ai/blob/main/EXPERIMENT_CONTRACT.md) · [로드맵](https://github.com/heechan9/fabguard-ai/blob/main/ROADMAP.md)

---

### 02 · [Bunkering AI](https://github.com/heechan9/bunkering-ai) — 선박 연료 구매 의사결정

<a href="https://github.com/heechan9/bunkering-ai"><img src="./assets/projects/bunkering.svg" alt="Bunkering AI 프로젝트 미리보기" width="100%" /></a>

**어떤 문제인가?**  
선박의 연료 구매는 가격만이 아니라 잔량, 환율, 항만, 운항상태와 안전재고를 함께 판단해야 합니다.

**무엇을 만들었나?**

- Gymnasium 가상 항해 환경에서 규칙 기반 정책 3종과 Double DQN을 동일 조건으로 비교
- 연료 잔량·가격·환율·운항상태를 하나의 상태공간으로 구성
- 안전재고 위반, 급유 횟수, 합성비용과 보상을 함께 기록
- DQN이 일부 지표에서 개선됐지만 비용과 운용조건까지 포함한 전반적 우월성은 주장하지 않음
- 코드, 보고서, 발표, 시연과 논문용 실험기록을 하나의 증거 체계로 관리

**My role:** Project lead · evaluation direction · system integration  
**Technical focus:** operational simulation, reinforcement learning, safety constraints, decision support

**확인하기:** [저장소](https://github.com/heechan9/bunkering-ai) · [기여 기록](https://github.com/heechan9/bunkering-ai/blob/main/CONTRIBUTIONS.md)

---

### 03 · [Adversarial AI Security](https://github.com/th0oel/AdversarialAI_Security) — 자율운항선박 AI 강건성 검증

<a href="https://github.com/th0oel/AdversarialAI_Security"><img src="./assets/projects/adversarial.svg" alt="Adversarial AI Security 프로젝트 미리보기" width="100%" /></a>

**어떤 문제인가?**  
자율시스템의 영상 AI는 사람이 알아채기 어려운 작은 입력 교란에도 잘못 판단할 수 있습니다.

**무엇을 만들었나?**

- 선박 이미지 781장의 CNN·MobileNetV2 clean baseline 재현
- FGSM 공격 전후 성능과 attack success rate 평가 파이프라인 구축
- L∞ 섭동 경계, ε=0 smoke test, 모델 가중치 불변성 검증
- 데이터·모델 SHA-256과 결과 번들로 실험 추적성 확보
- 팀 공식 저장소와 개인 포크를 구분해 실제 기여 범위를 명확히 기록

**My role:** Experiment implementation · validation contributor  
**Technical focus:** adversarial robustness, reproducibility, test integrity, autonomous-system safety

**확인하기:** [팀 공식 저장소](https://github.com/th0oel/AdversarialAI_Security) · [내 포크](https://github.com/heechan9/AdversarialAI_Security)

---

### 04 · [TriGuard AI](https://github.com/heechan9/triguard-ai) — 공공데이터 기반 운영 위험 분석

<a href="https://github.com/heechan9/triguard-ai"><img src="./assets/projects/triguard.svg" alt="TriGuard AI 프로젝트 미리보기" width="100%" /></a>

**어떤 문제인가?**  
여러 기관에 흩어진 공공데이터는 형식과 기준이 달라 지역별 위험을 한눈에 비교하기 어렵습니다.

**무엇을 만들었나?**

- 5개 공공기관의 데이터 12종을 통합해 14개 지역의 운영 위험 신호를 점검하는 MVP 구현
- 지도·대시보드·위험점수·문서 사이의 일관성을 독립 감사와 변이 테스트로 검증
- 위험 신호와 데이터 근거를 함께 표시하고 최종 판단은 사람이 수행하도록 설계
- 위험점수가 실제 기관의 운영 명령이나 공식 예측이 아님을 명시

**My role:** Project lead · data and scenario design · MVP delivery  
**Technical focus:** multi-source public data, decision support, consistency testing, human oversight

**확인하기:** [저장소](https://github.com/heechan9/triguard-ai)

## 프로젝트 근거 한눈에 보기 | Evidence map

| 프로젝트 | 확인 가능한 결과물 | 나의 역할 | 주장하지 않는 범위 |
|---|---|---|---|
| FabGuard AI | 오프라인 실험·웹 데모·테스트 | 프로젝트 소유자·검증 방향 | 실제 팹 KPI·수율 개선 |
| Bunkering AI | 시뮬레이터·정책 비교평가 | 팀장·시스템 통합 | 합성비용과 실제 운항비용의 동일성 |
| Adversarial AI | clean/FGSM 재현성 번들 | 실험 구현·검증 기여 | 팀 프로젝트 전체의 단독 소유 |
| TriGuard AI | 공공데이터 MVP·일관성 감사 | 팀장·데이터·시나리오 설계 | 위험점수의 공식 운영 명령성 |

## 작업 방식 | How I work

1. **현장의 판단 문제부터 정의합니다.** 모델보다 먼저 누가 무엇을 판단해야 하는지 정합니다.  
   *Frame the operational decision before selecting the model.*
2. **실험 조건을 먼저 고정합니다.** 데이터 분할, 기준선, 지표와 금지할 주장을 기록합니다.  
   *Freeze the experiment contract, baselines, metrics, and claim boundaries.*
3. **다시 확인할 수 있게 만듭니다.** 테스트, 해시, 결과 파일, 문서와 PR을 연결합니다.  
   *Connect tests, hashes, result artifacts, documentation, and pull requests.*
4. **실패와 한계도 결과로 남깁니다.** 낮은 recall이나 데이터 한계를 숨기지 않습니다.  
   *Report failure modes and limitations explicitly.*
5. **사람이 최종 책임을 갖게 합니다.** AI는 결정을 대체하지 않고 검토를 지원합니다.  
   *Keep a human accountable for operational decisions.*

## 경험과 기반 | Experience

| 영역 | 경험 |
|---|---|
| 전공 | 한국공학대학교 전자공학 전공·스마트팩토리 융합전공 |
| 산업 R&D | 미래내일 일경험 — 대유에이텍 R&D 연구소 선행연구팀, 2024 |
| 반도체 | 반도체 Career Track 44시간·반도체 설비기술 직무부트캠프 5주, 2026 |
| 해양 ICT | 스마트해운물류×ICT 멘토링 — 프로젝트 팀장·AI 보안 실험 기여, 2026 |
| 국제협업 | G-STAR×Hanoi — 한·베 EV 배터리 소재 공급망 및 생산입지 분석 |

## 사용 기술 | Working stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Gymnasium](https://img.shields.io/badge/Gymnasium-0081A5?style=flat-square)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)

> 연결된 프로젝트에서 실제로 사용한 기술입니다. 모든 기술의 숙련도가 동일하다는 의미는 아닙니다.

## 기술 협업 | Technical collaboration

해외 개발자·연구자·현장 엔지니어와 다음 주제로 협업하고 싶습니다.

*I welcome focused, issue-based collaboration in:*

- industrial data quality, missingness, drift, and leakage controls
- uncertainty-aware risk ranking and human-in-the-loop evaluation
- semiconductor manufacturing and edge-data adapters
- maritime decision simulation and autonomous-system AI robustness
- reproducibility tests, technical documentation, and experiment review

**협업 방법 | How to collaborate**

관심 있는 프로젝트의 Issue에 아래 네 가지를 적어 주세요. 작은 범위의 기술 검토와 PR부터 시작하는 방식을 선호합니다.

*Open a focused issue in the relevant repository with:*

1. target problem
2. data and system boundary
3. expected evidence or measurable result
4. acceptance criteria

## 현재 방향 | Current direction

- FabGuard를 **반도체 제조 AI → Fledge 엣지 운영 → 장기 시계열 데이터 품질 분석**으로 확장
- Solar Data Tools의 재사용 가능한 데이터 품질 방법론을 검토하고 산업설비 시계열 적용 가능성 실험
- 해양 AI 프로젝트의 실험·시연·논문화 근거 완성
- 호주 산업 현장에서 활용할 수 있는 영문 데모와 외부 검증 패키지 준비
- international collaboration in Industrial AI, smart manufacturing, and trustworthy autonomous systems

---

<div align="center">

### Build it. Test it. Explain the boundary.

**현장의 문제를 만들고, 검증하고, 누구나 이해할 수 있게 설명합니다.**

</div>
