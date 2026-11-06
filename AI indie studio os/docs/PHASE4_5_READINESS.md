# Studio OS Phase 4.5 준비 상태

확인일: 2026-11-06. `VERIFIED`는 명시한 범위만 실제 확인, `PARTIAL`은 일부 기능만 검증, `BLOCKED`는 현재 환경·권한에서 실행 불가, `PLANNED`는 설계만 존재함을 뜻한다.

| 항목 | 상태 | 실제 근거와 한계 |
| --- | --- | --- |
| 기존 결과 확인 | VERIFIED | 요청한 다섯 문서와 Phase 4 결과를 읽었다. 기존 일반 하위 에이전트 방식과 기록을 보존한다. |
| Git 저장소·원격 | BLOCKED | `git rev-parse --show-toplevel`, `git remote -v` 모두 이 폴더는 Git 저장소가 아니라고 보고. 원격 연결 없음. 다른 기존 프로젝트는 변경하지 않았다. |
| GitHub CLI 인증 | BLOCKED | `gh auth status`에서 두 저장 계정의 토큰이 유효하지 않음. 사용자가 터미널에서 `gh auth login -h github.com`으로 계정을 선택해 정상 인증해야 한다. 자격증명을 채팅에 입력하지 않는다. |
| GitHub 앱 계정 조회 | VERIFIED | GitHub 앱의 읽기 전용 `get_user_login`이 `jeydev1288`, `mintslime1288` 두 계정에 각각 성공. 이는 CLI 인증이나 이 프로젝트와 저장소의 연결을 뜻하지 않는다. 어느 계정을 연결할지는 미결정이다. |
| GitHub 저장소 생성·연결·push | PLANNED | 사용자 승인 전 실행하지 않았다. Git 초기화도 하지 않았다. 먼저 대상 계정과 신규/기존 저장소를 확인하고, 기존 저장소의 소유권과 파일 충돌을 살핀 뒤 별도 승인을 받아야 한다. |
| 승인 정책·실제 운영 보호 | PARTIAL | AGENTS.md에 명시적 승인 요구. 실제 배포·유료 API·삭제·메시지·권한 경로에는 기술적 게이트가 없다. CI/CD 및 운영 실행기는 존재하지 않는다. [승인 게이트 설명](APPROVAL_GATE.md) 참조. |
| 격리된 모의 승인 | VERIFIED | `scripts/approval_demo.py`에 대해 `tests/test_approval_demo.py` 3개 통과. 다섯 유형별 거부·무응답·잘못된 입력, 다른 작업의 확인 문자열, 미지원 유형은 차단되고, 일치 문자열은 모의 출력만 발생한다. 신원 인증이 아니며 입력은 위조 가능하다. 실제 승인 또는 외부 작업 보호가 아니다. |
| 새 Codex 세션의 프로젝트 역할·스킬 | BLOCKED | `codex exec --ephemeral --skip-git-repo-check --sandbox read-only` 시도는 상태 DB 및 in-process app-server 접근 거부로 세션 시작 실패(exit 1). 설정 파일 5개 및 스킬 2개의 존재는 확인되지만 발견·실제 호출은 미확인. 권한을 우회하거나 임시 상태를 다른 계정으로 옮기지 않았다. |
| 일반 하위 에이전트 대체 | VERIFIED | 이번 작업에서 일반 하위 에이전트에 환경 점검, 설계, 독립 구현 계약을 전달해 결과를 받았다. 프로젝트 TOML 역할로 실행한 것은 아니다. |
| Idea Factory 저장·스키마 | PARTIAL | [운영 절차](IDEA_FACTORY_OPERATIONS.md), `ideas/idea-template.json`, 기존 `research/`를 사용한다. JSON 검사기는 제목·고객·문제·고유 ID·가설·사실별 URL/날짜·점수 형식을 검사한다. 자동 저장은 없다. |
| 중복 탐지 | VERIFIED | 정규화한 제목 또는 고객+문제의 정확 일치 후보를 로컬 JSON으로 출력하는 동작을 테스트했다. 유사 의미 탐지는 없고 병합·삭제하지 않는다. |
| 출처·평가 QA | PARTIAL | 사실의 URL·날짜 형식과 1~5/null 점수를 검사하며 QA 절차를 정의했다. URL 실재·신뢰성·사실 적합성, 점수 근거 및 누락 점수 시 합산 금지는 사람이 확인한다. |
| 실행 로그·재시도 | PLANNED | [로그 양식](../research/RUN_LOG_TEMPLATE.md)과 제한적 재시도·중단 정책만 준비했다. 자동 로그·재시도는 없다. |

## 테스트

`python -m unittest discover -s tests -v`: 8개 테스트 통과. 승인 데모 3개는 거부·무응답·불일치·허용 모의 흐름을 검증한다. 아이디어 검사 5개는 유효·잘못된 날짜/점수/출처·중복·원본 불변·CLI 출력을 검증한다. `python scripts/idea_factory.py ideas/idea-template.json` 결과 `valid_count: 1`, 중복 후보 없음. 해당 JSON은 허구의 템플릿이다. 모의 승인 시험은 실제 서비스를 실행하지 않는다.

## Phase 5에서 사용할 수 있는 것과 없는 것

- 사용 가능: 수동 조사 기록 양식, 구조 검증, 정확 일치 중복 후보 탐지, 사람이 수행하는 QA·로그·재시도 정책, 현재 세션에서 일반 하위 에이전트에 작업 계약 전달.
- 사용 불가 또는 미검증: GitHub 원격 연결과 CLI 인증, 사용자 정의 에이전트·스킬의 새 세션 자동 발견·호출, 실제 실행 경로의 기술적 승인 강제, 자동 로그·재시도, 의미적 중복 판정 및 출처 진위 자동 검증.
- Phase 5는 **로컬의 수동 보조 Idea Factory 구축에 한해 진입 가능**하다. 실제 GitHub 연결은 계정·저장소 선택과 승인, 실제 운영 자동화는 해당 플랫폼의 인증된 승인 통제와 검증이 선행되어야 한다.

이번 단계에서는 실제 시장 조사, 대량 아이디어 생성, 외부 배포, 저장소 생성·연결·push를 수행하지 않았다.
