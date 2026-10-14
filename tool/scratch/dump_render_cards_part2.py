# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('function renderCards()')
with open('tool/scratch/render_cards_part2.txt', 'w', encoding='utf-8') as out:
    out.write(html[idx+2000:idx+5500])

print("Written render_cards_part2.txt")
