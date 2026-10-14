# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('function renderCards()')
with open('tool/scratch/render_cards.txt', 'w', encoding='utf-8') as out:
    out.write(html[idx:idx+3500])

print("Written render_cards.txt")
