<div align="center">

<img src="./assets/heechan-industrial-ai-profile-banner-v6.jpg" alt="Industrial AI portfolio connecting semiconductor manufacturing, smart ports, and operational decision systems" width="100%" />

<br>

# HEECHAN CHOI

### INDUSTRIAL AI · SMART MANUFACTURING · TRUSTWORTHY SYSTEMS

**반도체 제조를 중심으로 현장 데이터를 분석하고, 사람이 검토할 수 있는 AI 의사결정 지원 시스템을 만듭니다.**

*I build reviewable Industrial AI systems for semiconductor manufacturing,<br>operational decision support, and autonomous-system reliability.*

<br>

[![Explore Projects](https://img.shields.io/badge/EXPLORE-PROJECTS-00D4AA?style=for-the-badge&labelColor=111827)](#selected-work)
[![Live Product](https://img.shields.io/badge/VIEW-LIVE_DEMO-7C3AED?style=for-the-badge&labelColor=111827&logo=vercel&logoColor=white)](https://fabguard-ai.vercel.app/)
[![Collaborate](https://img.shields.io/badge/OPEN_TO-COLLABORATION-2563EB?style=for-the-badge&labelColor=111827)](#lets-build-together)

<br>

**BUILD → VALIDATE → EXPLAIN → IMPROVE**

</div>

---

## 01 / PROFILE

<table>
<tr>
<td width="50%" valign="top">

### 무엇을 만드는가

반도체 품질관리, 산업 데이터 운영, 해양 최적화와 자율시스템 보안 문제를 **검증 가능한 소프트웨어와 실험**으로 구현합니다.

모델의 높은 숫자보다 실제 사용자가 무엇을 판단할 수 있는지, 어떤 조건에서 실패하는지를 더 중요하게 봅니다.

</td>
<td width="50%" valign="top">

### What I bring

- Industrial problem framing
- Reproducible ML experiments
- Human-in-the-loop decision support
- Data-quality and drift controls
- Technical documentation and GitHub review
- Cross-domain system integration

</td>
</tr>
</table>

> **Current focus —** Semiconductor Manufacturing AI → Fledge edge operations → long-horizon time-series data quality → field-ready validation in Australia

<a id="selected-work"></a>

## 02 / SELECTED WORK

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

## 03 / ENGINEERING PRINCIPLES

| 01 — FRAME | 02 — FREEZE | 03 — TRACE | 04 — REPORT |
|---|---|---|---|
| 모델보다 먼저 현장의 판단 문제를 정의합니다. | 데이터 분할·기준선·지표·금지할 주장을 먼저 기록합니다. | 테스트·해시·결과·문서·PR을 연결합니다. | 성능뿐 아니라 실패 조건과 한계도 공개합니다. |
| Define the operational decision first. | Freeze the experiment contract. | Make every result reviewable. | Report failures explicitly. |

### Evidence, not decoration

| Project | Reviewable artifact | Ownership | Honest boundary |
|---|---|---|---|
| FabGuard AI | experiment · web demo · tests | owner and validation lead | no real-fab KPI claim |
| Bunkering AI | simulator · policy evaluation | project lead and integrator | synthetic cost is not field cost |
| Adversarial AI | clean/FGSM evidence bundle | implementation contributor | team-owned repository |
| TriGuard AI | public-data MVP · audit tests | project lead and designer | risk score is not an official order |

## 04 / FOUNDATION

<table>
<tr>
<td width="50%" valign="top">

### Background

- **Electronic Engineering**
- **Interdisciplinary Smart Factory**
- Industrial R&D experience, Dayou A-Tech
- Semiconductor career track, 44 hours
- Semiconductor equipment-engineering bootcamp
- Smart Maritime Logistics × ICT mentoring
- Korea–Vietnam EV battery supply-chain project

</td>
<td width="50%" valign="top">

### Working stack

**Data & ML**  
Python · pandas · scikit-learn · TensorFlow · PyTorch

**Systems & Validation**  
Fledge · Gymnasium · pytest · Git · data contracts

**Delivery**  
HTML · CSS · JavaScript · Streamlit · Vercel

> Tools demonstrated in linked projects—not a claim of equal mastery.

</td>
</tr>
</table>

<a id="lets-build-together"></a>

## 05 / LET'S BUILD TOGETHER

<div align="center">

### Open to focused technical collaboration

*Industrial AI · Semiconductor Manufacturing · Edge Data · AI Reliability*

</div>

해외 개발자·연구자·현장 엔지니어와 작게 시작해 검증 가능한 결과를 함께 만드는 협업을 선호합니다.

I welcome focused, issue-based collaboration in:

- industrial-data quality, missingness, drift, and leakage controls
- semiconductor manufacturing and edge-data adapters
- uncertainty-aware risk ranking and human-in-the-loop evaluation
- maritime decision simulation and autonomous-system AI robustness
- reproducibility tests, experiment review, and technical documentation

**Start with a focused GitHub issue:**

`target problem` → `data boundary` → `expected evidence` → `acceptance criteria`

## 06 / NOW

- Building **FabGuard Australia-ready v1**
- Expanding FabGuard through **Fledge edge operations**
- Evaluating reusable **Solar Data Tools data-quality methods** for industrial time series
- Completing evidence and publication packages for maritime AI projects
- Preparing English demos for international engineering collaboration

---

<div align="center">

### BUILD SYSTEMS PEOPLE CAN QUESTION — AND TRUST.

**현장의 문제를 만들고, 검증하고, 누구나 이해할 수 있게 설명합니다.**

[FabGuard Live Demo](https://fabguard-ai.vercel.app/) · [GitHub Projects](https://github.com/heechan9?tab=repositories)

</div>
