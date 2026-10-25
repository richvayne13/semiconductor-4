# -*- coding: utf-8 -*-
with open(r"C:\Work\반도체4_AISK대비\index.html", "r", encoding="utf-8") as f:
    html = f.read()

import re
matches = [m.start() for m in re.finditer(r'class="[^"]*mobile-top-bar[^"]*"', html)]
for idx in matches:
    print(html[idx-20:idx+600])
