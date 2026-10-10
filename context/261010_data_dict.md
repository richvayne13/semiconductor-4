# SK하이닉스 AISK 심층 대비 마스터 데이터 사전 (Data Dictionary)

- **작성일자**: 2026년 10월 10일
- **대상 워크스페이스**: `C:\Work\반도체4_AISK대비`
- **프로젝트명**: SK하이닉스 AISK 심층 대비 마스터 대시보드 (반도체4_AISK대비 v1.0)

---

## 1. 개요 및 목적
본 문서는 SK하이닉스 AISK(양산기술/소자/공정 직무 및 SK 인재상 기반 심층 인성 역량 평가)를 대비하기 위해 설계된 40대 Q&A 데이터 모델의 구조와 필드 정의를 기술합니다.

---

## 2. 데이터 모델 스키마 (Question-Answer Entity Schema)

각 문항 데이터는 다음과 같은 구조화된 필드를 가집니다:

| 필드명 | 데이터 타입 | 필수 여부 | 설명 | 예시 |
| :--- | :--- | :---: | :--- | :--- |
| `id` | String | 필수 | 고유 식별자 (카테고리_순번) | `"p_01"`, `"t_01"` |
| `category` | String | 필수 | 대분류 (`"personality"`: 인성, `"technical"`: 직무) | `"personality"` |
| `category_label` | String | 필수 | 한글 분류명 | `"인성·협업·조직 가치"`, `"양산기술·소자·공정"` |
| `number` | Integer | 필수 | 카테고리 내 일련번호 (1~20) | `1`, `2` |
| `title` | String | 필수 | 질문 텍스트 (사용자 및 심층 질문 원문) | `"피드백 후 상대방이 기분 상해 말을 안 하는 상황..."` |
| `core_keyword` | String | 필수 | 3대 핵심 키워드 태그 | `["감정 공감", "전달 태도 성찰", "목표 정렬"]` |
| `speech_1m30s` | String | 필수 | **1분 30초 실전 핵심 전달** (약 380~450자 구어체 완성본) | `"상대방의 침묵은 피드백 내용보다..."` |
| `deep_lecture` | Object | 필수 | 세부 마스터 기술/행동 분석 노트 (원리, 프레임워크, 수식) | `{"background": "...", "core_logic": "...", ...}` |
| `svg_diagram` | String | 선택/권장 | 시각적 직관 이해를 돕는 풀컬러 정밀 SVG 다이어그램 | `<svg ...>...</svg>` |

---

## 3. 질문 카테고리 구성 (총 40문항)

### (1) 인성 질문군 (Personality & Culture Fit, 20문항)
- **SK 인재상 기반**: VWBE(자발적·의욕적 두뇌활용), SUPEX 추구, 패기, 팀워크, 소통
- **상황 대처(STAR/Situational)**: 갈등 해결, 피드백 수용/전달, 실패 극복, 윤리적 딜레마, 스트레스/멘탈 관리

### (2) 직무 질문군 (Technical & Fab Engineering, 20문항)
- **소자 물리 & 양산 기술**: USJ, 채널링/터널링, HKMG WFM(TiN, TaN, Pt), BCAT, DIBL, Halo, Doping Profile
- **공정 & 소모 소재**: EUV 광학계/펠리클, 박막응력, Al vs Cu 배선, CVD vs ALD, HARC 식각, CMP 디싱
- **메모리 아키텍처 & 패키징**: 메모리 월, HBM (TSV, MR-MUF), 3D NAND 고단화, 하이브리드 본딩
