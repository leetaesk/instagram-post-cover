# Instagram Post Cover

실제 Instagram 탐색 게시물 **363개 중 직접 선정한 243개**를 바탕으로 만든 한국어 게시물 커버 제작 스킬입니다. 사진·캐러셀 첫 장을 다루며 릴스 썸네일은 제외합니다.

**이미지 생성과 생성형 편집은 금지합니다. 사진·일러스트 소재는 반드시 웹에서 가져옵니다.** 다운로드한 이미지의 크롭·리사이즈·색 보정, 타이포그래피와 가독성 그라디언트 조판은 허용합니다.

## 설치

Codex에서 다음과 같이 요청하세요.

```text
$skill-installer https://github.com/leetaesk/instagram-post-cover/tree/main/skills/instagram-post-cover 설치해줘
```

수동으로 설치하려면 저장소를 내려받고 `skills/instagram-post-cover` 폴더를 자신의 에이전트 스킬 폴더에 복사하세요. Codex의 기본 위치는 `~/.codex/skills/instagram-post-cover`입니다. 기존 설치가 있으면 먼저 차이를 확인하세요.

## 사용

```text
$instagram-post-cover 관심사로 영어 듣기를 주제로 인스타 게시물 커버 만들어줘.
```

```text
$instagram-post-cover 이 Figma 캐러셀의 표지를 웹 사진으로 3개 만들어줘: [Figma URL]
```

웹 검색·이미지 열람·파일 다운로드 수단이 필요합니다. Figma 편집 요청에는 Figma 편집 도구가 별도로 필요합니다. 특정 이미지 생성 서비스는 사용하지 않습니다.

## 구성

- `SKILL.md`: 웹 소재만 사용하는 제작·출처 기록·검수 절차
- `references/playbook.md`: 사진 헤드라인, 외곽선 후킹, 생활·취향, 음식·장소, 제품, 텍스트, 캡처·밈, 비교·콜라주 8가지 유형
- `references/catalog.json`: 통과243개·탈락120개의 원문 링크와 대표 유형 태그
- `scripts/list_references.py`: 조건별 참고 링크 조회. Python3 표준 라이브러리만 사용

```bash
python3 skills/instagram-post-cover/scripts/list_references.py --family photo-headline --limit 4
```

사진 파일과 개인 작업 기록은 배포하지 않습니다. 참고 링크는 원문 삭제나 로그인 요구로 열리지 않을 수 있습니다. 선택 이유를 기록한 데이터가 아니므로 유형 분석은 해석이며, 탐색 순위나 성과를 보장하지 않습니다.

## 라이선스

이 저장소의 자체 작성 지침과 코드는 MIT License입니다. 링크된 사진·게시물·브랜드 자산의 권리는 각 소유자에게 있으며, 이 라이선스로 재사용 권한이 부여되지 않습니다. 제작 소재의 출처와 이용 조건을 따로 확인하세요.
