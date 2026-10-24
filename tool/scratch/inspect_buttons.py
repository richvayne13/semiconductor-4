# -*- coding: utf-8 -*-
with open(r'C:\Work\반도체4_AISK대비\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect where main header buttons and sidebar action buttons are
pos_header = html.find('class="header-btn-group"')
print("Header btn group:")
print(html[pos_header:pos_header+500])

pos_sidebar_act = html.find('class="sidebar-action-bar"')
print("\nSidebar action bar:")
print(html[pos_sidebar_act:pos_sidebar_act+500])
