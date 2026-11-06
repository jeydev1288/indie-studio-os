# 스킬 및 워크플로 연결 계약

지정된 스킬이 현재 세션에 발견되면 해당 SKILL.md를 읽어 적용한다. 프로젝트 스킬의 자동 발견이 안 되면 파일을 직접 읽어 수동 적용한다. 아래는 자동 파이프라인이나 실행 보장이 아니라 총괄을 위한 라우팅 계약이다. 설치된 다른 스킬의 가용성은 실행 시 다시 확인한다. 고객 발송·배포·유료 행위는 사전 승인이 필요하다.

| 워크플로 | 재사용 경로 | 실행 조건 및 입력 | 출력과 완료 기준 |
| --- | --- | --- | --- |
| market-research | `.agents/skills/studio-market-research/SKILL.md` | 시장 조사 요청·주제 | 출처 URL·확인일·사실·가설·미확인 분리 |
| idea-factory | `product-app-architect:frame-opportunity` 또는 수동 | 고객 문제·시장 근거 | 후보 및 선택 기준, 가정과 근거 기록 |
| product-planning | `.agents/skills/studio-product-planning/SKILL.md` | 후보와 조사 결과 | MVP 범위·사용 흐름·수용 기준·검증 계획 |
| frontend-design | `frontend-design-premium:frontend-design` | UI 사용자·흐름 | 디자인·구현 범위 및 실제 가능한 반응형·접근성 검증 |
| development | `codex-superpowers` | 승인된 요구와 기존 코드 | 변경 결과와 실행한 적절한 테스트·남은 한계 |
| qa-gate | `codex-verification` 또는 해당 QA 스킬 | 산출물·수용 기준 | 근거별 통과·실패·미실행 판정 |
| launch-preparation | `product-app-architect:review-launch-readiness` | 출시 후보·환경 | 준비 상태·검증·위험·명시적 승인 대기 |
| growth | 기존 제품·시장 조사와 수동 기획 | 고객·목표 | 채널과 실험 가설·측정 기준, 발행 전 승인 |
| analytics | `product-app-architect:define-metrics` | 질문·지표·실제 데이터 | 산식·기간·출처·결측과 분석 결과 |
| mistake-learning | `docs/운영매뉴얼.md` | 재현된 실패와 수정 | 근거·재검증·교훈과 승격 판단 |
| lazy-genius-senior | `codex-superpowers`의 최소 변경 원칙 | 목표·제약·대안 | 최소 대안 및 요구·위험 비교 근거 |

`growth`, `mistake-learning`, `lazy-genius-senior`는 같은 이름의 별도 프로젝트 Skill이 없으며 기존 지침과 수동 작업을 조합한다. 위 계약을 기록했다고 각 워크플로가 실제 실행·검증된 것은 아니다.
