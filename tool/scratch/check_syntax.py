import re
import subprocess

with open(r'C:\Work\반도체4_AISK대비\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

scripts = re.findall(r'<script>(.*?)</script>', html, re.DOTALL)
print(f"Found {len(scripts)} scripts.")

for idx, s in enumerate(scripts):
    fname = f"C:\\Work\\반도체4_AISK대비\\tool\\temp_script_{idx}.js"
    with open(fname, "w", encoding="utf-8") as fjs:
        fjs.write(s)
    res = subprocess.run(["node", "--check", fname], capture_output=True, text=True)
    if res.returncode == 0:
        print(f"Script {idx}: Syntax OK!")
    else:
        print(f"Script {idx}: Syntax ERROR!\n{res.stderr}")
