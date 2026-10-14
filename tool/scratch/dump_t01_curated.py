# -*- coding: utf-8 -*-
import json

with open('context/data/aisk_curated_topics.json', 'r', encoding='utf-8') as f:
    topics = json.load(f)

t01 = [t for t in topics if t.get('id') == 't_01'][0]

with open('tool/scratch/t01_curated_dump.txt', 'w', encoding='utf-8') as out:
    out.write("ID: " + str(t01.get('id')) + "\n")
    out.write("Category: " + str(t01.get('category')) + "\n")
    out.write("Title: " + str(t01.get('title')) + "\n")
    out.write("Core Keywords: " + json.dumps(t01.get('core_keyword'), ensure_ascii=False) + "\n\n")
    out.write("=== speech_1m30s (현 3분 답변) ===\n" + str(t01.get('speech_1m30s')) + "\n\n")
    out.write("Length in chars: " + str(len(t01.get('speech_1m30s', ''))) + "\n")

print("Dumped to tool/scratch/t01_curated_dump.txt")
