# -*- coding: utf-8 -*-
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

REMOVE_ELEMENT_AFTER_KOR = {'Cu', 'Al', 'Si', 'Sn', 'Ru', 'Mo', 'Co', 'W', 'Ti', 'Ni', 'Au', 'B', 'P', 'As'}

def clean_korean_text(text):
    if not text:
        return ""
    # Standalone unwanted phrases
    unwanted = [
        r'\(\s*METAL\s+ION\s*\)',
        r'\(\s*IONIZED\s+PVD\s*\)',
        r'\(\s*OVERHANG\s*\)',
        r'\(\s*Overhang\s*\)',
        r'\(\s*Ionized\s+PVD\s*\)',
        r'\(\s*Metal\s+Ion\s*\)'
    ]
    for p in unwanted:
        text = re.sub(p, '', text, flags=re.IGNORECASE)

    def replacer(m):
        kor = m.group(1)
        content = m.group(2).strip()

        # Check for acronyms in content
        parts = [p.strip() for p in re.split(r'[,/]', content)]
        found_acronyms = [p for p in parts if p in KEEP_EXACT_ACRONYMS and p not in REMOVE_ELEMENT_AFTER_KOR]
        if found_acronyms:
            acr_str = ", ".join(found_acronyms)
            return f"{kor}({acr_str})"

        if content in KEEP_EXACT_ACRONYMS:
            if content in REMOVE_ELEMENT_AFTER_KOR:
                return kor
            return f"{kor}({content})"

        return kor

    text = re.sub(r'([가-힣]+)\s*\(([A-Za-z0-9\s\-_/,\.\'\+\*]+)\)', replacer, text)
    # clean extra spaces
    text = re.sub(r'[ \t]{2,}', ' ', text)
    return text

test_samples = [
    '화학증폭형 감광액(CAR, Chemically Amplified Resist)의 동작 메커니즘',
    '일렉트로마이그레이션(Electromigration, EM) 억제',
    '구리(Cu) 다마신(Damascene / Dual Damascene) 공정',
    'F-N 터널링(Fowler-Nordheim Tunneling)을 유도',
    '초고종횡비(HARC, Aspect Ratio > 70:1) 채널 홀',
    '피복성(Step Coverage)과 오버행(OVERHANG) 발생',
    '메탈 이온(METAL ION)과 이온화 PVD(IONIZED PVD)의 차이',
    '단차 피복성(Step Coverage)이 100%에 수렴'
]

for s in test_samples:
    print('ORIGINAL:', s)
    print('CLEANED :', clean_korean_text(s))
    print('-'*50)
