# -*- coding: utf-8 -*-
with open(r'C:\Work\반도체4_AISK대비\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# find header and main structure
pos_main = html.find('<main>')
print("Main area preview:")
print(html[pos_main:pos_main+1500])

# check top bar and mobile bar
pos_mob = html.find('class="mobile-top-bar"')
print("\nMobile top bar:")
print(html[pos_mob:pos_mob+600])

# check sidebar header
pos_side = html.find('class="sidebar-header"')
print("\nSidebar header:")
print(html[pos_side:pos_side+600])
