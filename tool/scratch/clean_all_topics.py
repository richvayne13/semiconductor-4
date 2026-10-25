# -*- coding: utf-8 -*-
import json
import re

KEEP_EXACT_ACRONYMS = {
    'ICP', 'EUV', 'ALD', 'CVD', 'PVD', 'DRAM', 'NAND', 'HBM', 'TSV', 'CMP', 'PR',
    'BARC', 'CAR', 'MOR', 'CTF', 'BLSA', 'DOF', 'DoF', 'EL', 'GAA', 'MIM', 'ZAZ',
    'HARC', 'BSPDN', 'CXL', 'PIM', 'PNM', 'ISPP', 'LDPC', 'ECC', 'PUC', 'COP',
    'GIDL', 'TRR', 'BCAT', 'VCT', 'EM', 'RIE', 'ECD', 'PEB', 'PAG', 'LER', 'LWR',
    'NTD', 'OAI', 'PSM', 'RET', 'UHV', 'CNT', 'CTE', 'PECVD', 'HF', 'LF', 'RF',
    'SEG', 'SCE', 'SILC', 'TLC', 'QLC', 'MLC', 'SLC', 'MR-MUF', 'NCF', 'TCB', 'EMC',
    'SOH', 'ACL', 'STI', 'ILD', 'IMD', '1T-1C', '1T1C', 'MAC', 'TCO', 'EOT', 'CD',
    'NA', 'SOP', 'SPC', 'FMEA', 'OOC', 'OOS', 'IP', 'PIR', 'HDP', 'TEOS', 'BL', 'WL',
    'DIP', 'QFP', 'BGA', 'WLP', 'FOWLP', 'RDL', 'SiP', 'CoWoS', 'PLP', 'SADP', 'SAQP',
    'OPC', 'DSA', 'EBR', 'HMDS', 'TMAH', 'PFC', 'GWP', 'SWAP', 'LPP', 'AI', 'GPU',
    'CPU', 'NPU', 'LLM', 'PCIe', 'DMA', 'OS', 'ALU', 'DDR', 'GDDR', 'SONOS', 'ONO',
    'CMOS', 'NMOS', 'PMOS', 'FinFET', 'MBCFET', 'MOSFET', 'FET', 'SiGe', 'eSiGe'
}

# Elements that should be removed if immediately following Korean word
# e.g., 구리(Cu) -> 구리, 알루미늄(Al) -> 알루미늄, 실리콘(Si) -> 실리콘, 주석(Sn) -> 주석
REMOVE_ELEMENT_AFTER_KOR = {'Cu', 'Al', 'Si', 'Sn', 'Ru', 'Mo', 'Co', 'W', 'Ti', 'Ni', 'Au', 'B', 'P', 'As'}

def clean_script_text(text):
    if not text:
        return ""

    # 1. Standalone English phrases in parentheses that user explicitly requested to remove
    unwanted_standalone = [
        r'\(\s*METAL\s+ION\s*\)',
        r'\(\s*IONIZED\s+PVD\s*\)',
        r'\(\s*OVERHANG\s*\)',
        r'\(\s*Overhang\s*\)',
        r'\(\s*Ionized\s+PVD\s*\)',
        r'\(\s*Metal\s+Ion\s*\)',
    ]
    for p in unwanted_standalone:
        text = re.sub(p, '', text, flags=re.IGNORECASE)

    # 2. Korean + Parentheses: e.g. 단어(Word)
    def replacer(m):
        kor = m.group(1)
        content = m.group(2).strip()

        # Split content by comma, slash or space if it contains acronyms
        # e.g., (CAR, Chemically Amplified Resist) -> CAR
        parts = [p.strip() for p in re.split(r'[,/]', content)]
        found_acronyms = [p for p in parts if p in KEEP_EXACT_ACRONYMS and p not in REMOVE_ELEMENT_AFTER_KOR]
        if found_acronyms:
            acr_str = ", ".join(found_acronyms)
            return f"{kor}({acr_str})"

        # If the whole content is an allowed acronym
        if content in KEEP_EXACT_ACRONYMS:
            if content in REMOVE_ELEMENT_AFTER_KOR:
                return kor
            return f"{kor}({content})"

        # If it's pure Korean inside parentheses, e.g. (옥사이드) or (인장 응력)
        # Check if it has English letters
        if not re.search(r'[A-Za-z]', content):
            # Keep Korean-only parentheses as is, e.g. (1) 또는 (인성)
            return f"{kor}({content})"

        # Otherwise, English repetition / explanation -> remove parenthesis!
        return kor

    # Match Korean word right before parenthesis
    text = re.sub(r'([가-힣]+)\s*\(([^()]+)\)', replacer, text)

    # 3. Clean up extra spaces around removed parentheses
    text = re.sub(r'[ \t]{2,}', ' ', text)
    return text

# Load index.html
html_path = r"C:\Work\반도체4_AISK대비\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

m = re.search(r'const DEFAULT_TOPICS = (\[.*?\]);', html, re.DOTALL)
topics = json.loads(m.group(1))

changed_count = 0
changed_samples = []

for t in topics:
    orig_speech = t.get('speech_1m30s', '')
    orig_alt = t.get('speech_alt', '')
    orig_title = t.get('title', '')

    new_speech = clean_script_text(orig_speech)
    new_alt = clean_script_text(orig_alt)
    new_title = clean_script_text(orig_title)

    if new_speech != orig_speech or new_alt != orig_alt or new_title != orig_title:
        changed_count += 1
        if len(changed_samples) < 10:
            changed_samples.append((t['id'], orig_speech, new_speech))
        t['speech_1m30s'] = new_speech
        t['speech_alt'] = new_alt
        t['title'] = new_title

print(f"Total topics modified: {changed_count} / {len(topics)}")
for tid, old_s, new_s in changed_samples[:5]:
    print(f"\n=== Topic {tid} ===")
    print("BEFORE:\n", old_s[:250])
    print("AFTER :\n", new_s[:250])

print("Checking tech topic diffs...")
sample_ids = ['t_m01', 't_m02', 't_05', 't_w01', 't_d01', 't_p06']
for t in topics:
    if t['id'] in sample_ids:
        print(f"=== {t['id']} ===")
        s_old = t['speech_1m30s']
        s_new = clean_script_text(s_old)
        lines_old = s_old.splitlines()
        lines_new = s_new.splitlines()
        for lo, ln in zip(lines_old, lines_new):
            if lo != ln:
                print("OLD:", lo[:120])
                print("NEW:", ln[:120])
        print()
