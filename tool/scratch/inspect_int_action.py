# -*- coding: utf-8 -*-
with open(r"C:\Work\반도체4_AISK대비\index.html", "r", encoding="utf-8") as f:
    html = f.read()

idx = html.find('class="interview-action-group"')
if idx != -1:
    print(html[idx:idx+600])
