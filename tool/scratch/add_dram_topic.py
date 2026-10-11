import json
import re
import os

new_topic = {
    "id": "t_07",
    "category": "tech",
    "category_label": "반도체 소자·공정 실전 핵심",
    "number": 7,
    "title": "DRAM의 기본 동작 원리 (1T-1C 셀 구조 및 Write / Read / Refresh 메커니즘)",
    "core_keyword": [
        "1T-1C 셀 구조",
        "커패시터 전하 충·방전",
        "전하 공유(Charge Sharing)",
        "센스 앰프(BLSA) 증폭",
        "리프레시(tRET)"
    ],
    "speech_1m30s": "DRAM은 1개의 트랜지스터와 커패시터(1T-1C)로 구성되어 전하 충·방전으로 데이터를 저장하는 휘발성 메모리입니다. 기본 동작은 3단계입니다. 첫째, 쓰기(Write)는 워드라인을 턴온하고 비트라인 전압으로 커패시터에 전하를 채우거나 비웁니다. 둘째, 읽기(Read)는 비트라인을 프리차지한 후 워드라인을 열어 전하 공유(Charge Sharing)를 유도합니다. 이때 발생하는 미세 전위차를 센스 앰프(BLSA)가 감지해 '0'과 '1'로 증폭 판독하며, 소실된 전하를 즉시 채우는 재저장(Restore)을 병행합니다. 셋째, 커패시터 전하는 자연 방전되므로 데이터 보존 시간(tRET) 내에 주기적으로 재충전하는 리프레시(Refresh)가 필수적입니다. 미세화 한계 속에서 충분한 커패시턴스(Cs) 확보와 트랜지스터 누설 억제가 DRAM 양산 수율의 핵심입니다."
}

# 1. Update index.html
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Extract DEFAULT_TOPICS
m = re.search(r'const DEFAULT_TOPICS = (\[.*?\]);', content, re.DOTALL)
if not m:
    raise ValueError("DEFAULT_TOPICS not found in index.html")

topics = json.loads(m.group(1))

# Check if t_07 already exists
if any(t['id'] == 't_07' for t in topics):
    print("t_07 already in DEFAULT_TOPICS")
else:
    topics.append(new_topic)
    print(f"Appended t_07. Total topics now: {len(topics)}")

new_json_str = json.dumps(topics, ensure_ascii=False, indent=2)
content = content[:m.start(1)] + new_json_str + content[m.end(1):]

# Update loadTopics to auto-merge new topics
old_load = """    function loadTopics() {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved) {
        try {
          currentTopics = JSON.parse(saved);
        } catch (e) {
          console.error('로컬스토리지 파싱 실패, 기본값 사용', e);
          currentTopics = JSON.parse(JSON.stringify(DEFAULT_TOPICS));
        }
      } else {
        currentTopics = JSON.parse(JSON.stringify(DEFAULT_TOPICS));
      }
    }"""

new_load = """    function loadTopics() {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved) {
        try {
          currentTopics = JSON.parse(saved);
          let updated = false;
          DEFAULT_TOPICS.forEach(dt => {
            if (!currentTopics.some(ct => ct.id === dt.id)) {
              currentTopics.push(JSON.parse(JSON.stringify(dt)));
              updated = true;
            }
          });
          if (updated) {
            saveTopicsToStorage();
          }
        } catch (e) {
          console.error('로컬스토리지 파싱 실패, 기본값 사용', e);
          currentTopics = JSON.parse(JSON.stringify(DEFAULT_TOPICS));
        }
      } else {
        currentTopics = JSON.parse(JSON.stringify(DEFAULT_TOPICS));
      }
    }"""

if old_load in content:
    content = content.replace(old_load, new_load)
    print("Successfully replaced loadTopics with smart merge logic")
else:
    print("loadTopics pattern not exact match, verifying...")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

with open("result/261010_v1.0/index.html", "w", encoding="utf-8") as f:
    f.write(content)

# Save curated topics to context/data/aisk_curated_topics.json and context/data/aisk_topics.json
with open("context/data/aisk_curated_topics.json", "w", encoding="utf-8") as f:
    json.dump(topics, f, ensure_ascii=False, indent=2)

print("Saved index.html, result/261010_v1.0/index.html, context/data/aisk_curated_topics.json")
