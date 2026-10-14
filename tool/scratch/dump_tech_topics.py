# -*- coding: utf-8 -*-
import json

with open('context/data/aisk_curated_topics.json', 'r', encoding='utf-8') as f:
    topics = json.load(f)

with open('tool/scratch/tech_topics_dump.txt', 'w', encoding='utf-8') as out:
    for t in topics:
        if t.get('category') == 'tech':
            out.write("="*60 + "\n")
            out.write(f"ID: {t['id']} (Number: {t.get('number')})\n")
            out.write(f"Title: {t['title']}\n")
            out.write(f"Length: {len(t.get('speech_1m30s',''))} chars\n")
            out.write(f"Keywords: {json.dumps(t.get('core_keyword',[]), ensure_ascii=False)}\n\n")
            out.write(t.get('speech_1m30s','') + "\n\n")

print("Dumped tech topics to tool/scratch/tech_topics_dump.txt")
