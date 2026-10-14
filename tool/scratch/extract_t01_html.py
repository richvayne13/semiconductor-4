# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('"id": "t_01"')
if idx != -1:
    start = text.rfind('{', 0, idx)
    # find end of this object
    depth = 0
    end = start
    for i in range(start, len(text)):
        if text[i] == '{': depth += 1
        elif text[i] == '}':
            depth -= 1
            if depth == 0:
                end = i + 1
                break
    with open('tool/scratch/t01_html_dump.txt', 'w', encoding='utf-8') as out:
        out.write(text[start:end])
    print("Found t_01 in index.html, length:", end-start)
else:
    print("t_01 not found in index.html")
