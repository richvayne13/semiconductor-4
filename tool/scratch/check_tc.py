# -*- coding: utf-8 -*-
with open(r'C:\Work\반도체4_AISK대비\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('topicContainer')
print("Around topicContainer:")
print(html[pos-300:pos+300])
