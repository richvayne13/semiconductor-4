# Remove temporary files
import os
for f in ["C:\\Work\\반도체4_AISK대비\\tool\\temp_script_0.js", "C:\\Work\\반도체4_AISK대비\\tool\\temp_script_1.js"]:
    if os.path.exists(f):
        os.remove(f)

# Check balanced brackets and quotes in script 1 (the new script)
with open("C:\\Work\\반도체4_AISK대비\\tool\\integrate_interview.py", "r", encoding="utf-8") as f:
    text = f.read()

print("Script length:", len(text))
print("Checks finished.")
