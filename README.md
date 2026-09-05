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

## 02 / SELECTED WORK

<table>
<tr>
<td width="50%" valign="top">

<a href="https://github.com/heechan9/fabguard-ai">
<img src="./assets/projects/fabguard.svg" alt="FabGuard AI" width="100%" />
</a>

### [FabGuard AI →](https://github.com/heechan9/fabguard-ai)

**반도체 생산 위험 우선점검**

공개 제조데이터를 분석해 엔지니어가 먼저 확인할 생산 건을 제시하는 의사결정 지원 시스템입니다.

- 1,567 production records · 590 measurements
- temporal validation · calibrated risk ranking
- Fledge operational slice · drift monitoring
- live product demo and reproducible evidence

**ROLE** Product owner · validation direction · release decisions

[Live demo](https://fabguard-ai.vercel.app/) · [Experiment contract](https://github.com/heechan9/fabguard-ai/blob/main/EXPERIMENT_CONTRACT.md) · [Roadmap](https://github.com/heechan9/fabguard-ai/blob/main/ROADMAP.md)

</td>
<td width="50%" valign="top">

<a href="https://github.com/heechan9/bunkering-ai">
<img src="./assets/projects/bunkering.svg" alt="Bunkering AI" width="100%" />
</a>

### [Bunkering AI →](https://github.com/heechan9/bunkering-ai)

**선박 연료 구매 의사결정**

가격·환율·연료 잔량·운항상태를 반영해 여러 급유 정책을 동일한 가상 항해 환경에서 비교합니다.

- Gymnasium operational environment
- three rule-based policies · Double DQN
- safety-stock and cost trade-offs
- experiment, report, presentation and demo package

**ROLE** Project lead · evaluation direction · system integration

[Repository](https://github.com/heechan9/bunkering-ai) · [Contributions](https://github.com/heechan9/bunkering-ai/blob/main/CONTRIBUTIONS.md)

</td>
</tr>
<tr>
<td width="50%" valign="top">

<a href="https://github.com/th0oel/AdversarialAI_Security">
<img src="./assets/projects/adversarial.svg" alt="Adversarial AI Security" width="100%" />
</a>

### [Adversarial AI Security →](https://github.com/th0oel/AdversarialAI_Security)

**자율운항선박 AI 강건성 검증**

선박 영상 AI가 미세한 적대적 입력에서 어떻게 실패하는지 재현하고 평가합니다.

- 781-image clean baseline
- CNN · MobileNetV2 · FGSM evaluation
- perturbation bounds and smoke tests
- SHA-256 integrity and reproducibility bundle

**ROLE** Experiment implementation · validation contributor

[Team repository](https://github.com/th0oel/AdversarialAI_Security) · [My fork](https://github.com/heechan9/AdversarialAI_Security)

</td>
<td width="50%" valign="top">

<a href="https://github.com/heechan9/triguard-ai">
<img src="./assets/projects/triguard.svg" alt="TriGuard AI" width="100%" />
</a>

### [TriGuard AI →](https://github.com/heechan9/triguard-ai)

**공공데이터 기반 운영 위험 분석**

서로 다른 기관의 데이터를 통합해 지역별 운영 위험 신호와 판단 근거를 보여주는 MVP입니다.

- 12 datasets · 5 public organizations
- 14-region risk intelligence
- dashboard and document consistency tests
- human oversight and explicit claim boundaries

**ROLE** Project lead · data and scenario design · MVP delivery

[Repository](https://github.com/heechan9/triguard-ai)

</td>
</tr>
</table>

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
