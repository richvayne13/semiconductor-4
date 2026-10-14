# -*- coding: utf-8 -*-
"""
apply_user_t01.py
사용자가 지정한 정확한 본문으로 1번(t_01)을 교체하고 온라인 배포:
"""

import json
import re

USER_T01_SPEECH = """NAND 플래시 메모리는 전자를 가두어 두는 '저장층'을 활용해, 전자가 들어있을 때와 없을 때 트랜지스터가 켜지는 기준 전압인 '문턱전압(Vth)'이 달라지는 원리로 데이터를 저장하는 비휘발성 메모리입니다. 현재 SK하이닉스가 양산하는 3D NAND는 전자가 옆으로 도망가지 못하도록 비전도성 질화막(SiN)에 전자를 안전하게 가두는 CTF(Charge Trap Flash) 구조를 표준으로 채택하고 있습니다.

핵심 동작은 프로그램(쓰기), 이레이즈(지우기), 리드(읽기) 세 가지로 이루어집니다.

첫째, 프로그램 동작은 전자를 트랩층 방 안에 집어넣는 과정입니다. 선택한 워드라인에 약 18~20V의 높은 전압을 걸어주면, 강한 전기장에 의해 전자가 절연막을 뚫고 넘어가는 F-N 터널링(Fowler-Nordheim Tunneling) 현상이 일어납니다. 이렇게 넘어간 전자가 질화막 트랩층에 갇히게 되면, 음전하의 영향으로 셀을 켜기 위한 문턱전압이 높아지면서 데이터 '0' 상태가 기록됩니다. 이때 전압을 한 번에 세게 걸면 셀마다 편차가 커지기 때문에, 전압 펄스를 계단식으로 조금씩 높여가며 검증하는 ISPP(Incremental Step Pulse Programming) 방식을 사용해 문턱전압을 아주 균일하고 정밀하게 맞춰줍니다.

둘째, 이레이즈 동작은 반대로 갇혀 있던 전자를 밖으로 빼내어 방을 비우는 과정입니다. 3D NAND는 지우기를 블록 단위로 진행하는데, 게이트는 0V로 두고 기판 쪽에 약 20V의 높은 전압을 걸어줍니다. 그러면 반대 방향으로 전기장이 형성되면서 트랩층에 있던 전자가 기판 쪽으로 빠져나가거나 정공이 들어와 중성화됩니다. 전자가 빠져나가면 문턱전압이 다시 원래대로 낮아지면서, 초기 상태인 데이터 '1'로 깨끗하게 리셋됩니다.

셋째, 리드 동작은 셀에 전자가 들어있는지 없는지를 전류가 흐르는지로 확인하는 과정입니다. NAND 플래시는 셀들이 직렬로 줄줄이 연결된 구조이기 때문에, 내가 읽고 싶은 셀 외의 다른 셀들은 무조건 다 켜져 있어야 전기가 통할 수 있습니다. 그래서 비선택 셀들에는 높은 패스 전압(Vpass)을 걸어 길을 열어두고, 내가 확인하려는 선택 셀에만 기준 읽기 전압(Vread)을 걸어봅니다. 만약 전자가 비어 있다면 문턱전압이 낮으니 채널이 켜져 전류가 흐르고(데이터 '1'), 전자가 차 있다면 문턱전압이 높아 전류가 흐르지 못하고 차단됩니다(데이터 '0'). 이 전류의 유무를 센스 앰프가 감지해 데이터를 읽어냅니다.

최근 SK하이닉스의 300단 이상 초고단 3D NAND에서는 셀이 수직으로 수백 층 쌓이다 보니, 위층과 아래층 셀들이 모두 똑같은 문턱전압 특성을 갖도록 채널 홀과 박막의 균일도를 완벽하게 맞추는 것이 양산 수율의 핵심입니다. 이러한 기본 동작 원리를 바탕으로 공정 산포를 제어하여 고신뢰성 메모리 양산에 기여하겠습니다."""

# 1. Update context/data/aisk_curated_topics.json
json_path = "context/data/aisk_curated_topics.json"
with open(json_path, "r", encoding="utf-8") as f:
    topics = json.load(f)

for t in topics:
    if t.get("id") == "t_01":
        t["speech_1m30s"] = USER_T01_SPEECH
        print(f"Updated t_01 in json (length: {len(USER_T01_SPEECH)} chars)")
        break

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(topics, f, ensure_ascii=False, indent=2)
print("Saved context/data/aisk_curated_topics.json")

# 2. Update HTML files
topics_json_str = json.dumps(topics, ensure_ascii=False, indent=2)

for html_path in ["index.html", "result/261010_v1.0/index.html"]:
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Replace DEFAULT_TOPICS
    m = re.search(r'const DEFAULT_TOPICS = (\[.*?\]);', html, re.DOTALL)
    if not m:
        raise ValueError(f"DEFAULT_TOPICS not found in {html_path}")

    html = html[:m.start(1)] + topics_json_str + html[m.end(1):]

    # Bump STORAGE_KEY to v8 so user's browser updates immediately without cache issues!
    html = re.sub(
        r"const STORAGE_KEY = 'aisk_master_topics_custom_v\d+';",
        "const STORAGE_KEY = 'aisk_master_topics_custom_v8';",
        html
    )

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Updated {html_path} with STORAGE_KEY v8!")

# 3. Update master.md table
md_path = "result/261010_v1.0/261010_AISK_master.md"
with open(md_path, "r", encoding="utf-8") as f:
    md_text = f.read()

char_len = len(USER_T01_SPEECH)
pattern = r"(\| \*\*T-01\*\* \| .*? \| .*? \| )(\d+자[^\n\|]*)( \|)"
replacement = rf"\g<1>{char_len}자 (사용자 지정 3분 답변)\g<3>"
md_text, count = re.subn(pattern, replacement, md_text)
print(f"Updated T-01 in master.md (subs: {count})")

with open(md_path, "w", encoding="utf-8") as f:
    f.write(md_text)
print("Saved 261010_AISK_master.md")
