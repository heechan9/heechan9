# 최희찬 · Heechan Choi

한국공학대학교에서 전자공학부 임베디드시스템공학을 전공하고, 스마트팩토리를 부전공했습니다.
반도체 제조와 산업 데이터를 다루는 일에 관심이 있습니다.

요즘은 공개 제조데이터로 불량 점검 순서를 정하는 FabGuard를 만들고 있습니다.
스마트해운물류 ICT 멘토링에서는 선박 연료 구매 시뮬레이션과 선박 이미지 AI 보안 실험에 참여하고 있습니다.
프로젝트 기획, 실험 결과 검토, 문서 정리를 맡으며 구현도 함께 다듬고 있습니다.

## 프로젝트

### [FabGuard AI](https://github.com/heechan9/fabguard-ai)

반도체 제조데이터에서 어떤 생산 건을 먼저 점검할지 살펴보는 프로젝트입니다.
SECOM 공개데이터로 불량 탐지 모델을 비교하고, 시간순으로 데이터를 나눴을 때도 결과가 유지되는지 확인하고 있습니다.
최근에는 Fledge 연동과 시계열 데이터의 결측·품질 점검 작업을 이어가고 있습니다.

[웹 데모](https://fabguard-ai.vercel.app/) · [실험 조건](https://github.com/heechan9/fabguard-ai/blob/main/EXPERIMENT_CONTRACT.md)

### [Bunkering AI](https://github.com/heechan9/bunkering-ai)

선박이 언제, 얼마나 연료를 구매할지 비교하는 팀 프로젝트입니다.
가상 항해 환경에서 규칙 기반 정책과 강화학습을 비교하며, 비용과 연료 잔량을 함께 확인합니다.
저는 기획과 평가 방향 정리, 시스템 통합을 맡고 있습니다.

[저장소와 실험 결과](https://github.com/heechan9/bunkering-ai) · [팀 기여 기록](https://github.com/heechan9/bunkering-ai/blob/main/CONTRIBUTIONS.md)

### [Adversarial AI Security](https://github.com/th0oel/AdversarialAI_Security)

선박 이미지 분류 모델이 작은 이미지 교란에 얼마나 영향을 받는지 실험합니다.
CNN과 MobileNetV2에 FGSM 공격을 적용하고, 전처리 필터가 결과에 미치는 영향을 비교합니다.
팀에서 실험 범위 정리와 결과 검증, 문서 통합에 참여하고 있습니다.

[팀 저장소](https://github.com/th0oel/AdversarialAI_Security) · [개인 포크](https://github.com/heechan9/AdversarialAI_Security)

### [TriGuard AI](https://github.com/heechan9/triguard-ai)

여러 공공기관의 데이터를 모아 지역별 위험 신호를 지도와 대시보드로 살펴보는 프로젝트입니다.
데이터의 출처와 기준을 맞추고, 화면에 표시되는 점수와 계산 결과가 일치하는지 점검하고 있습니다.

각 프로젝트의 데이터, 실험 조건과 한계는 해당 저장소에 정리해 두었습니다.
제조·위험 분석은 공개데이터 실험이고, 연료 구매 비교는 시뮬레이션을 바탕으로 합니다.

## 배경과 관심사

- 한국공학대학교 전자공학부 임베디드시스템공학 전공 · 스마트팩토리 부전공
- 대유에이텍 R&D 연구소 선행연구팀 일경험 참여 (2024)
- 스마트해운물류 ICT 멘토링 참여 (2026)
- 관심 분야: 반도체 공정·품질, 제조 데이터 분석, 산업설비 시계열

프로젝트에서는 Python, pandas, scikit-learn을 중심으로 사용하고,
실험에 따라 TensorFlow, PyTorch, Gymnasium을 다루고 있습니다.

관련 주제로 이야기하거나 프로젝트를 함께 살펴보고 싶으시면 저장소 이슈에 편하게 남겨 주세요.

---

I studied embedded systems and minored in smart factory at Tech University of Korea.
I'm interested in semiconductor manufacturing and industrial data, and currently work on manufacturing data analysis and maritime AI projects.
Feel free to open an issue in any of the repositories above.
