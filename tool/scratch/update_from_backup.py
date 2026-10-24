# -*- coding: utf-8 -*-
import json
import re

json_path = r"C:\Users\richm\Downloads\aisk_topics_backup_2026-10-24.json"
html_path = r"C:\Work\반도체4_AISK대비\index.html"

with open(json_path, "r", encoding="utf-8") as f:
    new_topics = json.load(f)

print(f"Loaded {len(new_topics)} topics from downloaded backup JSON.")

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update DEFAULT_TOPICS using exact string slicing
start_marker = "const DEFAULT_TOPICS = ["
idx_start = html.find(start_marker)
if idx_start == -1:
    raise ValueError(f"Start marker '{start_marker}' not found!")

end_marker = "    const STORAGE_KEY = 'aisk_master_topics_custom_v18_wopedimp_com';"
idx_end = html.find(end_marker, idx_start)
if idx_end == -1:
    raise ValueError(f"End marker '{end_marker}' not found!")

# Note: Before idx_end, there is '];\n\n'
formatted_json = json.dumps(new_topics, ensure_ascii=False, indent=2)

new_storage_key = "aisk_master_topics_custom_v19_wopedimp_com"
replacement = f"const DEFAULT_TOPICS = {formatted_json};\n\n    const STORAGE_KEY = '{new_storage_key}';"

html = html[:idx_start] + replacement + html[idx_end + len(end_marker):]
print("Replaced DEFAULT_TOPICS and STORAGE_KEY successfully.")

# 2. Update remaining STORAGE_KEY references if any
html = html.replace("aisk_master_topics_custom_v18_wopedimp_com", new_storage_key)

# 3. Update build-time
html = re.sub(
    r'<meta name="build-time" content="[^"]+">',
    '<meta name="build-time" content="2026-10-24T15:56:00+09:00">',
    html
)
print("Updated build-time meta tag.")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Updated {html_path} successfully! Total size: {len(html)} bytes.")
