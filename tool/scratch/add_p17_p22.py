# -*- coding: utf-8 -*-
import json
import re
import shutil

new_personality_topics = [
    {
        "id": "p_17",
        "category": "personality",
        "category_label": "인성·협업·조직 가치",
        "number": 17,
        "title": "생산 현장에서 적응이 어려울 때 대처 방법",
        "core_keyword": [
            "표준작업서(SOP) 숙지",
            "현장 선배·작업자 경청",
            "일일 오답노트 자산화",
            "작은 기여(Small Win)"
        ],
        "speech_1m30s": "낯선 설비와 빠른 현장 호흡에 적응이 어렵다면, 조급함을 버리고 '관찰·경청'과 '일일 복기 루틴'으로 돌파하겠습니다. 첫째, 표준작업지도서(SOP)와 과거 트러블 이력을 철저히 숙지해 이론과 현장의 간극을 줄이겠습니다. 둘째, 베테랑 작업자와 선배님들의 점검 동선을 관찰하고 겸손히 질문하며 현장의 암묵지를 빠르게 흡수하겠습니다. 셋째, 매일 배운 설비 특성과 실수를 오답노트로 구조화하고 데이터 정리 등 작은 업무부터 완수해 조기에 신뢰받는 현장형 엔지니어로 자리잡겠습니다."
    },
    {
        "id": "p_18",
        "category": "personality",
        "category_label": "인성·협업·조직 가치",
        "number": 18,
        "title": "부서 간에 갈등 문제가 생겼을 때 해결 방법",
        "core_keyword": [
            "상위 공동 KPI 정렬",
            "상대 부서 제약 경청",
            "데이터 시뮬레이션",
            "Win-Win 절충안"
        ],
        "speech_1m30s": "부서 간 갈등은 각자 맡은 KPI를 책임감 있게 수행하는 과정에서 발생하는 자연스러운 현상입니다. 따라서 감정을 배제하고 '상대 부서 제약 경청'과 '상위 목표 기반의 데이터 조율'로 해결하겠습니다. 먼저 설비 부하나 일정 압박 등 상대 부서의 현실적 고충을 경청하고 공감하겠습니다. 이후 판단 기준을 개별 부서의 유불리가 아닌 '라인 전체의 최종 수율과 납기'라는 상위 공동 목표로 정렬하고, 조건별 손익을 정량 데이터로 시뮬레이션해 상호 윈윈하는 실무 절충안을 도출하겠습니다."
    },
    {
        "id": "p_19",
        "category": "personality",
        "category_label": "인성·협업·조직 가치",
        "number": 19,
        "title": "생산 일정이 압박일 때 어떻게 대응할 건가요?",
        "core_keyword": [
            "품질·안전 무타협",
            "병목 공정 집중 돌파",
            "유관부서 실시간 공유",
            "우선순위 자원 재배치"
        ],
        "speech_1m30s": "생산 일정이 촉박할수록 조급함에 흔들리지 않고 '품질·안전 무타협 원칙' 아래 '병목 공정 집중 돌파'로 냉정히 대응하겠습니다. 납기에 쫓겨 표준 공정(SOP)이나 안전 수칙을 생략하면 대량 불량과 라인 셧다운이라는 더 큰 손실을 초래하기 때문입니다. 먼저 전체 흐름에서 지연을 유발하는 핵심 병목 구간을 데이터로 식별해 가용 설비 백업 라우팅과 리소스 집중 투입으로 리드타임을 단축하겠습니다. 동시에 유관 부서에 진행률과 리스크를 실시간 투명하게 공유해 납기와 품질을 함께 사수하겠습니다."
    },
    {
        "id": "p_20",
        "category": "personality",
        "category_label": "인성·협업·조직 가치",
        "number": 20,
        "title": "반복되는 문제를 개선하는 방법",
        "core_keyword": [
            "임시방편 지양",
            "5-Why 근본 원인 규명",
            "DoE 정량 검증",
            "Fool-proof 시스템화"
        ],
        "speech_1m30s": "동일한 문제가 반복되는 이유는 현상만 덮는 임시방편에 그쳐 근본 원인을 제거하지 못했기 때문입니다. 저는 '5-Why 분석'과 '시스템 표준화'로 반복 문제를 뿌리 뽑겠습니다. 먼저 공정 로그와 설비 센서 데이터를 전수 분석해 작업자 실수가 아닌 설비 마모나 공정 마진 부족 등 물리적 근본 원인을 끝까지 추적하겠습니다. 이후 DoE 검증을 거쳐 설비 인터록 설정, 알람 자동화, SOP 개정 등 실수 자체가 불가능한 Fool-proof 구조로 시스템화하여 재발률을 0%로 만들겠습니다."
    },
    {
        "id": "p_21",
        "category": "personality",
        "category_label": "인성·협업·조직 가치",
        "number": 21,
        "title": "제조/공정 조직에서 중요하게 생각하는 가치관",
        "core_keyword": [
            "기본과 원칙(SOP) 준수",
            "데이터 기반 정직성",
            "원팀(One-Team) 협업",
            "무결점 양산 책임감"
        ],
        "speech_1m30s": "제가 제조 및 공정 조직에서 가장 중요하게 생각하는 가치관은 '기본과 원칙(SOP) 준수', '데이터 앞에서의 정직성', 그리고 '유기적인 원팀 책임감'입니다. 24시간 가동되는 생산 현장에서 단 한 번의 절차 타협은 대형 품질 사고로 직결되므로 사소한 점검 루틴도 정석대로 지키는 기본기가 핵심입니다. 또한 감이 아닌 객관적 데이터로 소통하며 미세 이상 징후를 숨김없이 투명하게 공유해야 합니다. 내 공정만 보는 시야를 넘어 후공정 수율과 동료의 안전까지 배려하는 원팀 마인드로 무결점 양산을 완성하겠습니다."
    },
    {
        "id": "p_22",
        "category": "personality",
        "category_label": "인성·협업·조직 가치",
        "number": 22,
        "title": "안전과 생산성이 충돌했을 때 판단하는 기준",
        "core_keyword": [
            "안전 최우선 절대원칙",
            "선(先) 작업 중지·격리",
            "위험 요인 근본 제거",
            "지속가능한 생산성"
        ],
        "speech_1m30s": "안전과 생산성이 충돌하는 어떠한 순간에도 제 판단 기준은 '안전이 모든 생산 목표보다 절대 우선한다'는 무타협 원칙입니다. 단기 생산량을 위해 위험을 방치하면 동료의 생명을 위협할 뿐 아니라 중대 재해로 인한 라인 전면 셧다운이라는 돌이킬 수 없는 손실을 초래합니다. 따라서 위험 징후 발생 시 즉시 작업을 중단해 작업자를 대피시키고, 안전·설비 부서와 협력해 위험 요인을 물리적으로 완전 제거한 뒤 재가동하겠습니다. 불가피한 지연은 투명하게 보고하고 백업 라우팅으로 만회하겠습니다."
    }
]

for item in new_personality_topics:
    length = len(item["speech_1m30s"])
    assert 220 <= length <= 320, f"{item['id']} length {length} out of range 220~320"
    print(f"{item['id']} ({item['title']}): {length}자")

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

m = re.search(r'const DEFAULT_TOPICS = (\[.*?\]);', content, re.DOTALL)
if not m:
    raise ValueError("DEFAULT_TOPICS not found in index.html")

topics = json.loads(m.group(1))
existing_p = [t for t in topics if t["category"] == "personality"]
existing_t = [t for t in topics if t["category"] == "tech"]

for nt in new_personality_topics:
    existing_idx = next((i for i, t in enumerate(existing_p) if t["id"] == nt["id"]), None)
    if existing_idx is not None:
        existing_p[existing_idx] = nt
    else:
        existing_p.append(nt)

combined_topics = existing_p + existing_t
print(f"Total topics: {len(combined_topics)} (Personality: {len(existing_p)}, Tech: {len(existing_t)})")

new_json_str = json.dumps(combined_topics, ensure_ascii=False, indent=2)
content = content[:m.start(1)] + new_json_str + content[m.end(1):]

# Update STORAGE_KEY from v10 to v11 and migrate custom items from v10
content = content.replace("const STORAGE_KEY = 'aisk_master_topics_custom_v10';", "const STORAGE_KEY = 'aisk_master_topics_custom_v11';")
content = content.replace("localStorage.getItem('aisk_master_topics_custom_v9')", "localStorage.getItem('aisk_master_topics_custom_v10')")

# Update initial filter tab numbers
content = re.sub(r'id="tabAll">전체 \(\d+\)<', f'id="tabAll">전체 ({len(combined_topics)})<', content)
content = re.sub(r'id="tabPersonality">인성·협업 \(\d+\)<', f'id="tabPersonality">인성·협업 ({len(existing_p)})<', content)
content = re.sub(r'id="tabTech">직무·소자 \(\d+\)<', f'id="tabTech">직무·소자 ({len(existing_t)})<', content)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

with open("result/261010_v1.0/index.html", "w", encoding="utf-8") as f:
    f.write(content)

with open("context/data/aisk_curated_topics.json", "w", encoding="utf-8") as f:
    json.dump(combined_topics, f, ensure_ascii=False, indent=2)

shutil.copyfile("index.html", "../index.html")
print("Successfully updated index.html, result/261010_v1.0/index.html, context/data/aisk_curated_topics.json, and ../index.html")
