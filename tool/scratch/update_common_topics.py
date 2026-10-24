# -*- coding: utf-8 -*-
import json
import re

html_path = r"C:\Work\반도체4_AISK대비\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. 새 토픽 4개 정의
new_topics = [
    {
        "id": "t_com01",
        "category": "tech",
        "category_label": "반도체 직무 · 공통 (박막/절연)",
        "process": "COM",
        "process_label": "공통 (Common)",
        "number": 1,
        "title": "반도체 핵심 절연막 SiO2(옥사이드)의 정의, 4대 역할 및 주요 적용 레이어",
        "core_keyword": [
            "SiO2 (실리콘 옥사이드)",
            "절연 파괴 전계 (10 MV/cm)",
            "소자 분리(STI)",
            "층간 절연막(ILD/IMD)",
            "패시베이션 및 마스킹"
        ],
        "speech_1m30s": "SiO2(Silicon Dioxide, 옥사이드)는 실리콘(Si)과 산소(O)가 1:2의 원자비로 결합한 무기 절연 물질로, 약 9 eV의 넓은 밴드갭과 10 MV/cm에 달하는 높은 절연파괴전계를 지녀 반도체 집적회로의 기틀을 마련한 핵심 소재입니다. 특히 기판인 실리콘과 반응 시 계면 결함 밀도(Dit)가 극히 낮아 우수한 전기적 특성을 제공합니다.\n\nSiO2의 핵심 역할은 크게 네 가지입니다.\n첫째, '전기적 절연 및 소자 간 격리'입니다. 도체 배선이나 인접한 트랜지스터 사이에서 원치 않는 누설 전류나 기생 커패시턴스를 차단하여 소자의 오작동을 방지합니다.\n둘째, '소자 보호(Passivation)'입니다. 외부 수분, 대기 중 화학 오염 물질, 나트륨(Na+)과 같은 가동 이온이 민감한 내부 회로로 침투하는 것을 물리적·화학적으로 방어합니다.\n셋째, '공정 마스킹 및 버퍼층'입니다. 이온 주입 공정 시 도펀트가 원치 않는 영역으로 주입되는 것을 막는 마스크 역할을 하며, 고응력 질화막(SiN) 하부에서 응력을 완화해 주는 패드 옥사이드(Pad Oxide) 버퍼로 활용됩니다.\n넷째, '전하 저장 유전체'입니다. 과거 트랜지스터의 게이트 절연막 및 커패시터 유전체로서 정전용량을 형성하는 역할을 담당했습니다.\n\n주요 적용 레이어로는 소자 간을 분리하는 STI(Shallow Trench Isolation) 트렌치 매립 산화막, 금속 배선 층간을 절연하는 ILD(Inter-Layer Dielectric) 및 IMD(Inter-Metal Dielectric), 트랜지스터의 게이트 산화막, 식각 마스크 산화막, 그리고 칩 최상단의 패시베이션 오버코트 등이 있습니다.",
        "speech_alt": "SiO2는 약 9eV의 밴드갭과 10MV/cm의 절연파괴전계를 가진 반도체 최고의 절연체로, 실리콘 기판과의 계면 안정성이 매우 우수합니다. 주요 역할은 트랜지스터와 배선 간의 전기적 절연, 외부 오염물질과 가동 이온을 차단하는 패시베이션, 이온 주입 및 식각 공정의 마스킹 및 응력 완충 버퍼입니다. 적용 레이어로는 트랜지스터 간 간섭을 막는 STI 소자분리막, 다층 금속 배선 사이를 채우는 ILD/IMD 층간 절연막, 게이트 산화막 및 칩 최상단 보호막 등이 있습니다."
    },
    {
        "id": "t_com02",
        "category": "tech",
        "category_label": "반도체 직무 · 공통 (박막/절연)",
        "process": "COM",
        "process_label": "공통 (Common)",
        "number": 2,
        "title": "CVD(화학기상증착)의 메커니즘 원리·특징 및 주요 적용 레이어",
        "core_keyword": [
            "CVD (화학기상증착)",
            "전구체 & 반응가스 & 반응종",
            "Throughput 및 Step Coverage",
            "STI & ILD/IMD 절연막",
            "W 콘택트 플러그",
            "3D NAND ON 스택"
        ],
        "speech_1m30s": "CVD(Chemical Vapor Deposition, 화학기상증착)는 기체 상태의 전구체(Precursor)와 반응 가스(Reactant Gas)를 챔버 내부로 연속 주입하여, 열·플라즈마·광 에너지를 가해 화학 반응을 유도함으로써 웨이퍼 표면에 고체 박막을 증착하고 부산물은 배출하는 기술입니다. 기체 상태의 활성화된 반응종(라디칼)들이 표면으로 확산되어 반응하므로, 증착 속도(Throughput)가 빠르고 복잡한 단차에서도 비교적 양호한 단차 피복성(Step Coverage)을 제공합니다.\n\nCVD가 적용되는 주요 레이어는 절연막과 전도막으로 나뉩니다.\n첫째, '절연막 레이어'입니다. 트랜지스터 간 격리를 위해 깊고 좁은 트렌치를 메우는 STI 갭필 옥사이드(HDPCVD), 다층 금속 배선 사이를 채우는 ILD/IMD 층간 절연막(SiO2 및 Low-k SiCOH), 패턴 전사를 위한 SiN 질화막 하드마스크 및 게이트 측벽 스페이서가 대표적입니다. 특히 3D NAND에서는 옥사이드와 나이트라이드를 수백 단 교대로 쌓아 올리는 몰드(ON/ON Stack) 형성에 핵심적으로 사용됩니다.\n둘째, '전도막 레이어'입니다. 트랜지스터 게이트 전극 및 저항 배선을 형성하는 폴리실리콘(Poly-Si)과, 하부 트랜지스터와 상부 금속 배선을 전기적으로 연결해 주는 수직 비아 홀(Contact Hole)을 빈틈없이 채우는 텅스텐 플러그(W Plug, WF6 기반 W-CVD) 공정에 필수적으로 적용됩니다.",
        "speech_alt": "CVD는 전구체를 포함한 반응 가스를 주입해 열이나 플라즈마 에너지로 표면 화학 반응을 일으켜 박막을 증착하는 공정입니다. 높은 생산성과 우수한 단차 피복성이 강점입니다. 적용 레이어로는 절연막 영역에서 STI 트렌치 매립 산화막, 배선 층간 절연막(ILD/IMD), 하드마스크 질화막(SiN), 3D NAND의 수백 단 ON 몰드 스택이 있으며, 전도막 영역에서는 게이트 폴리실리콘 및 수직 콘택트 홀을 채우는 텅스텐(W) 플러그 매립에 핵심 적용됩니다."
    },
    {
        "id": "t_com03",
        "category": "tech",
        "category_label": "반도체 직무 · 공통 (박막/절연)",
        "process": "COM",
        "process_label": "공통 (Common)",
        "number": 3,
        "title": "PVD(물리적기상증착) 스퍼터링 메커니즘·특징 및 주요 적용 레이어",
        "core_keyword": [
            "PVD (물리적기상증착)",
            "스퍼터링(Sputtering)",
            "초고순도 금속막",
            "Cu 시드 레이어",
            "Ti/TiN & Ta/TaN 배리어",
            "패키징 UBM 패드"
        ],
        "speech_1m30s": "PVD(Physical Vapor Deposition, 물리적기상증착)는 화학 반응을 배제하고, 고진공 챔버 내에서 아르곤(Ar+) 플라즈마 이온을 금속 타깃(Target)에 물리적으로 충돌(Sputtering)시켜 튀어나온 금속 원자를 웨이퍼 표면에 물리적으로 증착하는 기술입니다. 화학 전구체를 쓰지 않으므로 불순물 잔류가 없어 초고순도 박막을 얻을 수 있지만, 입자가 직진하여 날아가므로 깊고 좁은 종횡비 패턴에서는 측벽과 바닥의 단차 피복성(Step Coverage)이 낮다는 물리적 한계를 갖습니다.\n\nPVD가 적용되는 주요 레이어는 다음과 같습니다.\n첫째, '금속 배선 및 시드 레이어'입니다. 최상부 파워 라인과 본딩 패드에 사용되는 알루미늄(Al) 배선 증착에 쓰이며, 구리 배선 공정(Dual Damascene)에서 전기도금(Electroplating)을 유도하기 위해 얇게 깔아주는 구리 시드 레이어(Cu Seed Layer) 증착에 필수적입니다.\n둘째, '확산 방지막 및 라이너(Barrier & Liner)'입니다. 구리가 절연막으로 확산되어 단락을 일으키는 것을 막는 Ta/TaN 배리어층, 그리고 텅스텐 콘택트 홀 바닥에서 실리콘과 접촉 저항을 낮추고(Ohmic Contact 형성) 박리를 막아주는 Ti/TiN 라이너 증착에 사용됩니다.\n셋째, '하드마스크 및 패키징 레이어'입니다. EUV 및 초미세 식각 시 PR을 지지하는 TiN 금속 하드마스크와, 후공정 패키징에서 솔더볼 범프 형성을 위한 접착·확산 방지막인 UBM(Under Bump Metallurgy) 패드 증착에 적용됩니다.",
        "speech_alt": "PVD는 고진공에서 아르곤 이온을 금속 타깃에 충돌시켜 튀어나온 원자를 쌓는 스퍼터링 공정으로, 초고순도 금속막 형성에 최적화되어 있습니다. 다만 직진성으로 인해 고종횡비 패턴에서는 Step Coverage가 제한됩니다. 주요 적용 레이어는 알루미늄 배선 및 구리 전기도금용 Cu 시드 레이어, 구리 및 텅스텐의 확산을 방지하는 Ta/TaN 및 Ti/TiN 배리어 메탈, 극미세 식각용 TiN 하드마스크, 그리고 패키징 범프 형성용 UBM 패드층입니다."
    },
    {
        "id": "t_com04",
        "category": "tech",
        "category_label": "반도체 직무 · 공통 (박막/절연)",
        "process": "COM",
        "process_label": "공통 (Common)",
        "number": 4,
        "title": "ALD(원자층증착)의 자기제어 반응 메커니즘 및 주요 적용 레이어",
        "core_keyword": [
            "ALD (원자층증착)",
            "자기제어 반응(Self-Limiting)",
            "100% Conformal 단차 피복성",
            "High-k 게이트(HKMG)",
            "DRAM ZAZ 캐패시터 유전막",
            "3D NAND ONO 채널홀",
            "다중패터닝 희생 스페이서"
        ],
        "speech_1m30s": "ALD(Atomic Layer Deposition, 원자층증착)는 전구체(Precursor) 주입 -> 퍼지(Purge) -> 반응가스(Reactant) 주입 -> 퍼지(Purge)의 4단계를 1사이클로 분할하여 반복 공급하는 화학적 박막 증착 기술입니다. 표면의 반응 활성 자리가 모두 결합하면 반응이 스스로 멈추는 자기제어적 표면 포화 반응(Self-limiting reaction)을 이용하므로, 사이클당 약 0.1nm 수준으로 원자 단위 두께를 정밀하게 제어할 수 있으며, 100:1 이상의 초고종횡비 구조에서도 100%에 가까운 완벽한 Conformal 단차 피복성(Step Coverage)을 실현합니다.\n\nALD가 적용되는 주요 레이어는 극미세·초고단화가 요구되는 최첨단 소자 영역입니다.\n첫째, '최첨단 트랜지스터 게이트 절연막(HKMG)'입니다. 5nm 이하 FinFET 및 GAA(MBCFET) 소자에서 양자역학적 터널링 누설 전류를 억제하기 위해 수 나노미터 두께로 극도로 균일하게 형성하는 HfO2, ZrO2 High-k 유전막에 필수 적용됩니다.\n둘째, 'DRAM 캐패시터 초고유전막(Capacitor Dielectric)'입니다. 깊고 좁은 필라(Pillar) 형태의 초고종횡비 구조 내벽에 정전용량 확보를 위해 증착되는 ZrO2-Al2O3-ZrO2(ZAZ) 복합 유전체 박막에 적용됩니다.\n셋째, '3D NAND 수직 채널 홀 게이트 스택(O-N-O)'입니다. 200단~300단을 관통하는 수직 채널 홀 내벽에 균일하게 깔리는 블로킹 산화막(Al2O3), 전하 트랩 질화막(SiN), 터널 산화막(SiO2) 초미세 절연막을 형성합니다.\n넷째, '포토리소그래피 한계 극복을 위한 스페이서(SADP/SAQP)'입니다. 미세 피치 구현을 위해 기존 패턴 측벽에 극도로 일정한 두께로 형성하는 희생 산화막/질화막 스페이서 증착에 활용됩니다.",
        "speech_alt": "ALD는 전구체와 반응가스를 시분할 주입하여 자기제어 표면 흡착 반응을 통해 원자층 단위로 제어하는 기술입니다. 증착 속도는 느리지만 100%에 달하는 완벽한 Step Coverage를 자랑합니다. 주요 적용 레이어는 5nm 이하 트랜지스터 누설 전류를 막는 High-k(HfO2) 게이트 절연막, DRAM 초고종횡비 캐패시터의 ZAZ 유전막, 3D NAND 채널 홀 내벽의 ONO 메모리 셀 스택, 그리고 노광 한계를 돌파하는 다중 패터닝(SADP/SAQP) 희생 스페이서입니다."
    }
]

# 2. DEFAULT_TOPICS 파싱 및 새 토픽 삽입
start_str = "const DEFAULT_TOPICS = ["
idx_start = content.find(start_str)
idx_end = content.find("];", idx_start)

json_str = content[idx_start + len("const DEFAULT_TOPICS = "):idx_end + 1]
topics = json.loads(json_str)

# 기존 t_com 문항이 있으면 제거 후 재삽입 (중복 방지)
topics = [t for t in topics if not str(t.get("id", "")).startswith("t_com")]

# 삽입 위치: 인성 문항(p_) 끝난 직후 (첫 번째 tech 앞)
insert_pos = 0
for i, t in enumerate(topics):
    if t.get("category") == "tech":
        insert_pos = i
        break
if insert_pos == 0:
    insert_pos = len(topics)

for offset, nt in enumerate(new_topics):
    topics.insert(insert_pos + offset, nt)

new_json_str = json.dumps(topics, ensure_ascii=False, indent=2)

# content 교체
content = content[:idx_start + len("const DEFAULT_TOPICS = ")] + new_json_str + content[idx_end + 1:]

# 3. 사이드바 및 카드 렌더링에서 'COM' numStr 처리
# if (proc === 'DEV') { numStr = `소자-${String(num).padStart(2, '0')}`; }
# -> COM 처리 추가
target_render = "if (proc === 'DEV') {\n            numStr = `소자-${String(num).padStart(2, '0')}`;"
replacement_render = "if (proc === 'DEV') {\n            numStr = `소자-${String(num).padStart(2, '0')}`;\n          } else if (proc === 'COM') {\n            numStr = `공통-${String(num).padStart(2, '0')}`;"

content = content.replace(target_render, replacement_render)

# 4. 상단 숏컷 버튼에 '공통' chip 추가
# <button class="proc-chip active" data-proc="ALL" title="직무 전체 (45문항)" onclick="selectProcessFilter('ALL')">ALL</button>
target_chip = '<button class="proc-chip active" data-proc="ALL"'
replacement_chip = '<button class="proc-chip active" data-proc="ALL"'

# 칩 컨테이너 찾기
chip_match = re.search(r'(<button class="proc-chip active" data-proc="ALL"[^>]*>ALL</button>)', content)
if chip_match:
    old_btn = chip_match.group(1)
    new_btn = old_btn + '\n        <button class="proc-chip chip-com" data-proc="COM" title="공통: 박막·절연 핵심 총람 (4문항)" onclick="selectProcessFilter(\'COM\')">공통</button>'
    content = content.replace(old_btn, new_btn, 1)

# 5. chip-com 스타일 추가
style_target = ".proc-chip.chip-dev {"
style_com = """    .proc-chip.chip-com {
      min-width: 40px;
    }
    .proc-chip.chip-com.active {
      background: linear-gradient(135deg, #059669 0%, #10b981 100%);
      border-color: #34d399;
      box-shadow: 0 0 10px rgba(16, 185, 129, 0.4);
    }
    """
content = content.replace(style_target, style_com + style_target)

# 6. STORAGE_KEY 버전 업데이트 (캐시 방지 및 즉시 반영)
content = re.sub(
    r"const STORAGE_KEY = '[^']+';",
    "const STORAGE_KEY = 'aisk_master_topics_custom_v18_wopedimp_com';",
    content
)

# 7. build-time 갱신
content = re.sub(
    r'<meta name="build-time" content="[^"]+">',
    '<meta name="build-time" content="2026-10-23T22:38:00+09:00">',
    content
)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Successfully updated index.html with {len(topics)} topics!")
