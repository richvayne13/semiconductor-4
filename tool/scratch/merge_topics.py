# -*- coding: utf-8 -*-
"""
40개 문항 데이터 병합 및 검증 스크립트 (merge_topics.py)
"""
import sys
import json
import os

# 모듈 import
from p_part1 import get_personality_topics
from p_part2 import get_personality_topics_part2
from p_part3 import get_personality_topics_part3
from p_part4 import get_personality_topics_part4
from t_part1 import get_tech_topics_part1
from t_part2 import get_tech_topics_part2
from t_part3 import get_tech_topics_part3
from t_part4 import get_tech_topics_part4

def main():
    p1 = get_personality_topics()
    p2 = get_personality_topics_part2()
    p3 = get_personality_topics_part3()
    p4 = get_personality_topics_part4()
    t1 = get_tech_topics_part1()
    t2 = get_tech_topics_part2()
    t3 = get_tech_topics_part3()
    t4 = get_tech_topics_part4()

    personality_all = p1 + p2 + p3 + p4
    tech_all = t1 + t2 + t3 + t4
    all_topics = personality_all + tech_all

    print(f"[검증] 인성 문항 수: {len(personality_all)} (기대값: 20)")
    print(f"[검증] 직무 문항 수: {len(tech_all)} (기대값: 20)")
    print(f"[검증] 총 문항 수: {len(all_topics)} (기대값: 40)")

    assert len(personality_all) == 20, f"인성 문항 수 오류: {len(personality_all)}"
    assert len(tech_all) == 20, f"직무 문항 수 오류: {len(tech_all)}"
    assert len(all_topics) == 40, f"총 문항 수 오류: {len(all_topics)}"

    # 상세 필드 및 글자 수 검증
    for idx, item in enumerate(all_topics):
        speech_len = len(item["speech_1m30s"])
        title = item["title"]
        item_id = item["id"]
        # print(f"[{item_id}] {title[:20]}... | 1분30초 글자수: {speech_len}자")
        assert "id" in item and "category" in item and "speech_1m30s" in item and "deep_lecture" in item and "svg_diagram" in item
        assert "background" in item["deep_lecture"] and "action_principle" in item["deep_lecture"] and "core_points" in item["deep_lecture"]

    out_path = r"C:\Work\반도체4_AISK대비\context\data\aisk_topics.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_topics, f, ensure_ascii=False, indent=2)

    print(f"[완료] {out_path} 에 40개 문항 데이터 저장 성공!")

if __name__ == "__main__":
    main()
