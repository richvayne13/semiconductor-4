# -*- coding: utf-8 -*-
"""
직무 질문 1~5문항 데이터 생성 스크립트 (t_part1.py)
"""

def get_tech_topics_part1():
    topics = [
        {
            "id": "t_01",
            "category": "tech",
            "category_label": "반도체 소자·공정 실전 핵심",
            "number": 1,
            "title": "EUV 노광 장비 광학계가 굴절 렌즈 대신 Mo/Si 다층막 반사경(Mirror)만으로 구성된 물리적 이유와 집광 원리",
            "core_keyword": ["13.5nm 강한 흡수율", "굴절률 n≈1", "Mo/Si 브래그 반사 (Bragg Reflection)"],
            "speech_1m30s": (
                "EUV 노광 광학계가 전량 반사경으로만 구성된 이유는 13.5nm 파장의 극자외선이 지구상의 모든 물질에서 극심하게 흡수되기 때문입니다. "
                "EUV 영역에서 물질의 굴절률(n)은 진공(1.0)과 거의 같은 0.99 수준에 수렴하여 굴절 현상 자체가 거의 일어나지 않으며, 광자가 석영 유리나 공기 분자에 흡수되어 투과 렌즈를 통과하지 못합니다. "
                "따라서 빛을 투과시켜 굴절시키는 기존 DUV 광학계는 원천적으로 사용이 불가능하며, 고진공 상태에서 Mo(몰리브덴)과 Si(실리콘)을 40~50주기로 적층한 '다층막 브래그 반사경'을 사용합니다. "
                "굴절률 차이가 있는 Mo와 Si 계면마다 반사되는 빛의 위상을 보강 간섭(Constructive Interference)시켜 최대 약 70%의 반사율을 얻어냅니다. "
                "반사경을 10여 매 거치면 웨이퍼 도달 광량이 1~2%로 급감하므로, 고출력 주석 플라즈마 소스와 수소 퍼지 기반의 반사면 오염 방지가 핵심입니다. "
                "EUV의 물리적 한계를 극복하는 정밀 광학 제어로 선단 메모리의 미세 패턴 한계를 돌파하겠습니다."
            ),
            "deep_lecture": {
                "background": "ASML의 EUV 장비는 기존 ArF 침지(Immersion)의 193nm 한계를 넘어 13.5nm 단파장을 사용합니다. 하지만 광자 에너지가 높아(약 91.8 eV) 모든 매질에 흡수되므로 렌즈 대신 진공 반사 광학계가 필수적입니다.",
                "action_principle": "1. 광학적 제약: 13.5nm 광자의 높은 흡수율(Absorption) 및 n ≈ 1 로 굴절 불가\n2. 브래그 반사 원리: $n\\lambda = 2d\\sin\\theta$, Mo(산란체, 약 2.8nm)와 Si(스페이서, 약 4.2nm) 교번 적층\n3. 시스템적 트레이드오프: 1회 반사 시 약 70% 반사율 ➔ 11매 거치면 $(0.7)^{11} \\approx 2\\%$ 광량 도달 ➔ 광원 고출력화 필수\n4. 보호 및 제어: 주석(Sn) 데브리 오염 방지 및 수소 가스 에칭 클리닝",
                "core_points": [
                    "‘투과형 렌즈 불가’의 광학적 본질(n ≈ 1 및 강한 흡수)을 물리학적으로 설명",
                    "브래그 반사 법칙($2d\\sin\\theta = \\lambda$)과 Mo/Si 다층 박막(40~50 pair) 구조 명시",
                    "광량 손실(Throughput) 문제와 고출력 EUV 소스(250W~500W)의 상호작용 제시"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="40" y="45" width="220" height="150" fill="#1e293b" stroke="#ef4444" stroke-width="2" rx="8"/>
  <text x="150" y="80" fill="#ef4444" font-size="15" font-weight="bold" text-anchor="middle">굴절 렌즈 불가</text>
  <text x="150" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">13.5nm 극심한 광 흡수</text>
  <text x="150" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">굴절률 n ≈ 0.999 (굴절 제로)</text>
  <text x="150" y="165" fill="#f87171" font-size="12" text-anchor="middle">석영 렌즈 내 광자 소멸</text>

  <path d="M 275 120 L 315 120" stroke="#38bdf8" stroke-width="3"/>

  <rect x="330" y="45" width="230" height="150" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="445" y="80" fill="#38bdf8" font-size="15" font-weight="bold" text-anchor="middle">Mo/Si 브래그 반사경</text>
  <text x="445" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">Mo(산란체) + Si(스페이서)</text>
  <text x="445" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">40~50쌍 다층막 위상 보강</text>
  <text x="445" y="165" fill="#38bdf8" font-size="12" text-anchor="middle">단일경 반사율 약 70%</text>

  <path d="M 575 120 L 615 120" stroke="#f59e0b" stroke-width="3"/>

  <rect x="630" y="45" width="130" height="150" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="695" y="80" fill="#f59e0b" font-size="15" font-weight="bold" text-anchor="middle">고진공 챔버</text>
  <text x="695" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">공기 흡수 차단</text>
  <text x="695" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">H2 플라즈마</text>
  <text x="695" y="165" fill="#f59e0b" font-size="12" text-anchor="middle">Sn 오염 세정</text>
</svg>"""
        },
        {
            "id": "t_02",
            "category": "tech",
            "category_label": "반도체 소자·공정 실전 핵심",
            "number": 2,
            "title": "박막응력(Thin Film Stress)의 인장(Tensile)과 압축(Compressive) 발생 원인 및 웨이퍼 보잉 제어 방식",
            "core_keyword": ["진성 응력(Intrinsic)", "열응력(Thermal CTE)", "웨이퍼 보잉(Bowing) & 스트레인 공학"],
            "speech_1m30s": (
                "박막응력은 증착 과정에서 원자 간 결합이 재배열되며 생기는 '진성 응력'과, 기판과 박막 간 열팽창계수(CTE) 차이로 생기는 '열응력'의 합으로 결정됩니다. "
                "박막이 주변보다 수축하려는 인장 응력(Tensile)은 웨이퍼를 오목(Concave)하게 휘게 만들고, 팽창하려는 압축 응력(Compressive)은 볼록(Convex)하게 만듭니다. "
                "이 응력은 양면의 성격을 지닙니다. 한편으로는 소자 채널에 의도적으로 가해 NMOS에는 인장 응력으로 전자 이동도를 높이고, PMOS에는 SiGe 압축 응력으로 정공 이동도를 끌어올리는 스트레인 공학에 활용됩니다. "
                "반면 다층 적층 시 웨이퍼 보잉(Bowing)이 수백 ㎛ 이상 발생하면 후속 포토 공정에서 초점 심도(DOF) 마진이 무너지고 오버레이 불량이 발생합니다. "
                "이를 제어하기 위해 플라즈마 이온 에너지(Ion Bombardment)와 증착 온도를 튜닝하고, 웨이퍼 후면에 반대 극성의 응력 보상막을 증착하여 기계적 평탄도를 유지합니다. "
                "물리적 응력을 소자 특성과 공정 마진 관점에서 정밀 통제하겠습니다."
            ),
            "deep_lecture": {
                "background": "선단 DRAM 및 초고단 3D NAND에서는 수십~수백 층의 박막이 누적되면서 발생하는 총 누적 응력이 웨이퍼 파손, 패턴 붕괴, 노광 초점 에러를 유발합니다. 소자 성능(이동도 향상)과 수율(보잉 제어)의 절충이 필수적입니다.",
                "action_principle": "1. 응력의 기원: $\\sigma_{total} = \\sigma_{intrinsic} + \\sigma_{thermal}$\n- Intrinsic: 결정립계 합체(Tensile) vs 원자 피닝/샷피닝(Compressive)\n- Thermal: $\\sigma_{th} = \\frac{E_f}{1-\\nu_f}(\\alpha_s - \\alpha_f)\\Delta T$\n2. 스트레인 공학: NMOS(채널 방향 Tensile ➔ 전자 유효질량 $m^*$ 감소) / PMOS(채널 방향 Compressive ➔ Heavy/Light 홀 밴드 스플리팅)\n3. 보잉 억제 기술: PECVD RF 바이어스로 압축력 부여, 후면 SiN 보상막(Backside compensation), CMP 평탄화",
                "core_points": [
                    "진성 응력(결정립 성장)과 열응력(CTE 차이) 메커니즘을 명확히 구분",
                    "웨이퍼 보잉(Stoney's equation)이 포토 오버레이/DOF에 미치는 악영향 서술",
                    "NMOS Tensile / PMOS Compressive 스트레인 엔지니어링의 양면성 연결"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="40" y="45" width="210" height="150" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="145" y="80" fill="#38bdf8" font-size="15" font-weight="bold" text-anchor="middle">인장 응력 (Tensile)</text>
  <text x="145" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">박막 수축 경향 (오목 Concave)</text>
  <text x="145" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">NMOS 채널 전자 이동도 ↑</text>
  <text x="145" y="165" fill="#38bdf8" font-size="12" text-anchor="middle">유효 질량 감소</text>

  <path d="M 265 120 L 305 120" stroke="#f59e0b" stroke-width="3"/>

  <rect x="320" y="45" width="210" height="150" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="425" y="80" fill="#f59e0b" font-size="15" font-weight="bold" text-anchor="middle">압축 응력 (Compressive)</text>
  <text x="425" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">박막 팽창 경향 (볼록 Convex)</text>
  <text x="425" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">PMOS SiGe 정공 이동도 ↑</text>
  <text x="425" y="165" fill="#f59e0b" font-size="12" text-anchor="middle">홀 밴드 분리 효과</text>

  <path d="M 545 120 L 585 120" stroke="#10b981" stroke-width="3"/>

  <rect x="600" y="45" width="160" height="150" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="680" y="80" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">보잉 제어 기술</text>
  <text x="680" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">웨이퍼 휨 억제</text>
  <text x="680" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">후면 응력 보상막</text>
  <text x="680" y="165" fill="#10b981" font-size="12" text-anchor="middle">포토 DOF 마진 확보</text>
</svg>"""
        },
        {
            "id": "t_03",
            "category": "tech",
            "category_label": "반도체 소자·공정 실전 핵심",
            "number": 3,
            "title": "금속 배선에서 알루미늄(Al)과 구리(Cu)의 물리적 특성 비교 및 다마신(Damascene) 공정 도입 배경",
            "core_keyword": ["비저항 (1.7 vs 2.7 μΩ·cm)", "일렉트로마이그레이션(EM)", "다마신(Damascene) & CMP"],
            "speech_1m30s": (
                "구리(Cu)가 알루미늄(Al)을 대체한 이유는 '낮은 비저항으로 인한 RC 딜레이 개선'과 '우수한 일렉트로마이그레이션(EM) 내성' 때문이며, 그 대가로 '다마신 공정'이 탄생했습니다. "
                "구리의 비저항은 약 1.7μΩ·cm로 알루미늄의 2.7μΩ·cm보다 약 40% 낮아 선폭 미세화 시 신호 지연을 획기적으로 줄입니다. "
                "또한 구리는 녹는점이 1,085도로 알루미늄보다 훨씬 높아 고전류 밀도에서 원자가 전자 충돌에 밀려 이동하는 EM 수명이 수십 배 우수합니다. "
                "하지만 구리는 상온에서 휘발성 부산물을 형성하지 않아 기존 알루미늄처럼 RIE 건식 식각이 불가능하다는 치명적 난제가 있었습니다. "
                "이를 해결하기 위해 절연막(IMD)에 먼저 배선 트렌치와 비아를 파내고, 구리를 전기화학도금(ECD)으로 채운 뒤 화학기계적연마(CMP)로 깎아내는 '다마신 공정'이 표준으로 안착했습니다. "
                "여기에 구리가 실리콘으로 빠르게 침투 확산되는 것을 막는 Ta/TaN 배리어 메탈 기술이 융합되어 초미세 배선의 신뢰성을 완성했습니다."
            ),
            "deep_lecture": {
                "background": "소자 스케일링이 0.13㎛ 이하로 진입하면서 트랜지스터 게이트 지연보다 인터커넥트(배선)의 RC 지연이 칩 전체 성능을 지배하기 시작했습니다. Al에서 Cu로의 전환은 반도체 배선 공정의 최대 기술 패러다임 변화였습니다.",
                "action_principle": "1. 물리적 우위: 비저항(Cu 1.67 vs Al 2.65), 융점(Cu 1085℃ vs Al 660℃ ➔ EM 활성화 에너지 $E_a$ 높음)\n2. 공정상 난제: 구리 염화물($CuCl_x$)의 증기압이 낮아 상온 건식 식각 불가\n3. 다마신 혁신: 패터닝(Etch) ➔ 도금(Electroplating) ➔ 평탄화(CMP)의 발상 전환\n4. 확산 배리어: 구리의 깊은 준위(Deep Level Trap) 형성 방지를 위해 Ta/TaN 스퍼터링 필수",
                "core_points": [
                    "RC 지연 시간 공식($\\tau = RC$)과 비저항 차이 수치 명확 제시",
                    "구리의 식각 불가(낮은 증기압) 물성과 다마신(Damascene) 공정의 필연적 연계",
                    "실리콘 내부 침투를 방어하는 확산 방지막(Ta/TaN) 역할 명시"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="40" y="45" width="210" height="150" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="145" y="80" fill="#38bdf8" font-size="15" font-weight="bold" text-anchor="middle">물리 특성 비교</text>
  <text x="145" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">비저항: 1.7 vs 2.7 μΩ·cm</text>
  <text x="145" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">RC 딜레이 40% 개선</text>
  <text x="145" y="165" fill="#38bdf8" font-size="12" text-anchor="middle">EM 내성 10~100배 향상</text>

  <path d="M 265 120 L 305 120" stroke="#ef4444" stroke-width="3"/>

  <rect x="320" y="45" width="210" height="150" fill="#1e293b" stroke="#ef4444" stroke-width="2" rx="8"/>
  <text x="425" y="80" fill="#ef4444" font-size="15" font-weight="bold" text-anchor="middle">건식 식각 불가 난제</text>
  <text x="425" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">Cu-Cl 부산물 증기압 결여</text>
  <text x="425" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">상온 RIE 식각 원천 불가</text>
  <text x="425" y="165" fill="#f87171" font-size="12" text-anchor="middle">Si 오염(Deep Trap) 리스크</text>

  <path d="M 545 120 L 585 120" stroke="#10b981" stroke-width="3"/>

  <rect x="600" y="45" width="160" height="150" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="680" y="80" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">다마신 &amp; 배리어</text>
  <text x="680" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">트렌치 식각 ➔ Cu 도금</text>
  <text x="680" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">CMP 평탄화로 완성</text>
  <text x="680" y="165" fill="#10b981" font-size="12" text-anchor="middle">Ta/TaN 확산 차단막</text>
</svg>"""
        },
        {
            "id": "t_04",
            "category": "tech",
            "category_label": "반도체 소자·공정 실전 핵심",
            "number": 4,
            "title": "현대 컴퓨팅 시스템(폰 노이만 구조)에서 메모리의 역할과 '메모리 월(Memory Wall)' 극복을 위한 HBM 혁신",
            "core_keyword": ["폰 노이만 병목", "메모리 월 (Memory Wall)", "HBM 1024-bit TSV 초광대역"],
            "speech_1m30s": (
                "현대 폰 노이만 구조에서 메모리는 초고속 연산 장치인 GPU/CPU와 대용량 저장 장치인 스토리지 사이의 속도 격차를 메우는 '주작업대(Main Workspace)' 역할을 합니다. "
                "그러나 연산 장치의 속도는 기하급수적으로 발전한 반면, 메모리와 프로세서를 연결하는 버스 대역폭의 발전 속도는 물리적 배선 한계로 인해 이를 따라가지 못하는 '메모리 월(Memory Wall)' 병목이 발생했습니다. "
                "GPU가 데이터를 기다리며 연산 코어를 놀려야 하는 starvation 현상이 심화된 것입니다. "
                "SK하이닉스는 이를 극복하기 위해 기존 평면 PCB 기반의 32비트/64비트 버스 구조를 파괴하고, TSV 관통 전극을 이용해 DRAM 다이를 수직 적층한 HBM을 선보였습니다. "
                "1,024비트의 초광대역 버스와 실리콘 인터포저 초단거리 연결을 통해 초당 1.2TB 이상의 압도적 대역폭을 전력 효율적으로 구현했습니다. "
                "HBM은 단순한 저장 장치를 넘어 AI 연산 장치의 연산 성능을 온전히 끌어올리는 시스템의 핵심 심장입니다."
            ),
            "deep_lecture": {
                "background": "생성형 AI 모델(LLM)의 파라미터가 수천억 개로 폭증하면서 시스템 성능은 FLOPS(연산량)보다 Memory Bandwidth(초당 전송량)에 의해 100% 결정되는 Memory Bound 환경으로 전환되었습니다.",
                "action_principle": "1. 폰 노이만 병목: CPU/GPU와 Memory가 단일 버스를 공유하여 데이터 전송 지연 발생\n2. 종래 GDDR의 한계: 핀 수 증가 시 신호 왜곡(Crosstalk) 및 전력 소모 급증 ($P \\propto C V^2 f$)\n3. HBM 아키텍처 혁신: 핀당 속도를 무리하게 올리는 대신, 1,024개 TSV 채널을 병렬로 연결하는 '와이드 I/O' 전략\n4. MR-MUF 패키징 연계: 고방열 에폭시 몰딩으로 열 저항 40% 이상 개선",
                "core_points": [
                    "‘저장’이 아닌 ‘프로세서 starvation 방지 및 주작업대’로서의 메모리 역할 정의",
                    "연산 능력 대비 대역폭 지연(Memory Wall)의 본질적 개념 규명",
                    "HBM의 광대역(1024-bit Wide I/O)과 저전력 초단거리 연결 물리 메커니즘"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="40" y="45" width="210" height="150" fill="#1e293b" stroke="#ef4444" stroke-width="2" rx="8"/>
  <text x="145" y="80" fill="#ef4444" font-size="15" font-weight="bold" text-anchor="middle">메모리 월 (Memory Wall)</text>
  <text x="145" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">GPU 연산 속도 &gt;&gt; DRAM 버스</text>
  <text x="145" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">데이터 병목에 의한 놀림 현상</text>
  <text x="145" y="165" fill="#f87171" font-size="12" text-anchor="middle">폰 노이만 병목의 극치</text>

  <path d="M 265 120 L 305 120" stroke="#38bdf8" stroke-width="3"/>

  <rect x="320" y="45" width="210" height="150" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="425" y="80" fill="#38bdf8" font-size="15" font-weight="bold" text-anchor="middle">기존 GDDR 한계</text>
  <text x="425" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">좁은 버스 (32~64 bit)</text>
  <text x="425" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">주파수 상승에 따른 발열 급증</text>
  <text x="425" y="165" fill="#38bdf8" font-size="12" text-anchor="middle">기생 커패시턴스 한계</text>

  <path d="M 545 120 L 585 120" stroke="#10b981" stroke-width="3"/>

  <rect x="600" y="45" width="160" height="150" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="680" y="80" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">HBM 수직 적층</text>
  <text x="680" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">1024-bit TSV 광대역</text>
  <text x="680" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">초당 1.2TB+ 대역폭</text>
  <text x="680" y="165" fill="#10b981" font-size="12" text-anchor="middle">MR-MUF 고방열 융합</text>
</svg>"""
        },
        {
            "id": "t_05",
            "category": "tech",
            "category_label": "반도체 소자·공정 실전 핵심",
            "number": 5,
            "title": "USJ(Ultra Shallow Junction)와 LDD(Lightly Doped Drain)의 접합 깊이(Xj) 상관관계 및 단채널 효과(SCE) 억제 메커니즘",
            "core_keyword": ["LDD Extension 접합 깊이", "횡방향 공핍층 전계 제어", "DIBL 억제"],
            "speech_1m30s": (
                "USJ(초미세 접합)의 핵심 타겟은 소스/드레인 전체가 아니라, 채널과 바로 맞닿아 있는 'LDD(익스텐션) 영역의 접합 깊이(Xj)'를 수십 nm 이하로 극초박화하는 것입니다. "
                "게이트 길이가 수십 nm 이하로 줄어들면 드레인의 전계가 게이트를 우회하여 소스 쪽 전위 장벽을 낮추는 DIBL과 전치 펀치스루가 발생합니다. "
                "이때 LDD의 접합 깊이 Xj를 극도로 얕게 형성하면, 드레인 전압에 의해 채널 밑바닥으로 침투하는 횡방향 공핍층의 체적이 현저히 줄어듭니다. "
                "결과적으로 게이트 전극이 채널 전하를 장악하는 정전기적 지배력이 회복되어 문턱전압 롤오프와 누설 전류를 완벽히 통제할 수 있습니다. "
                "다만 접합이 얕아질수록 필연적으로 기생 직렬 저항이 급증하므로, LDD 바깥쪽에는 깊고 농도가 높은 Deep S/D과 실리사이드를 형성하는 이중 접합 아키텍처와 레이저 스파이크 어닐링을 결합하여 성능과 수율을 동시에 사수합니다."
            ),
            "deep_lecture": {
                "background": "단채널 효과(SCE)는 소스/드레인 접합 깊이($X_j$), 게이트 산화막 두께($t_{ox}$), 공핍폭($W_d$)의 비율에 의해 지배됩니다. 접합 깊이를 줄이는 USJ는 평면 MOSFET부터 FinFET까지 모든 트랜지스터의 핵심 스케일링 지표입니다.",
                "action_principle": "1. 접합 위치 규명: Deep S/D은 콘택 저항을 위해 깊게 형성하되, 채널 하부로 파고드는 LDD(Extension)의 $X_j$를 10~20nm 이하로 극소화하는 것이 USJ의 실체\n2. 공핍층 축소 메커니즘: $X_j$ 감소 ➔ 드레인 공핍 영역의 채널 하부 침투 방지 ➔ DIBL 및 서브스레숄드 누설 차단\n3. 공정 제약 극복: 극저에너지 이온 주입(sub-keV) 및 밀리초 어닐링(MSA/LSA)으로 열확산에 의한 접합 깊이 팽창(TED: Transient Enhanced Diffusion) 억제\n4. 트레이드오프: 저항 증가($R_{sheet} \\propto 1/X_j$)를 Co/Ni 실리사이드와 Raised S/D로 보상",
                "core_points": [
                    "USJ의 직접적 대상이 'LDD(익스텐션) 영역'임을 명쾌하게 정의",
                    "접합 깊이 축소가 횡방향 공핍 영역을 제한하여 게이트 지배력을 회복시키는 원리 설명",
                    "기생 저항 증가와 밀리초 어닐링(LSA) 등 양산 기술 솔루션 연계"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="40" y="45" width="210" height="150" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="145" y="80" fill="#38bdf8" font-size="15" font-weight="bold" text-anchor="middle">USJ의 본질</text>
  <text x="145" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">LDD Extension 영역</text>
  <text x="145" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">접합 깊이 Xj &lt; 15nm 극소화</text>
  <text x="145" y="165" fill="#38bdf8" font-size="12" text-anchor="middle">채널 하부 침투 원천 차단</text>

  <path d="M 265 120 L 305 120" stroke="#f59e0b" stroke-width="3"/>

  <rect x="320" y="45" width="210" height="150" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="425" y="80" fill="#f59e0b" font-size="15" font-weight="bold" text-anchor="middle">단채널 효과 억제</text>
  <text x="425" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">횡방향 공핍 전계 축소</text>
  <text x="425" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">DIBL 및 펀치스루 억제</text>
  <text x="425" y="165" fill="#f59e0b" font-size="12" text-anchor="middle">게이트 정전 제어력 복원</text>

  <path d="M 545 120 L 585 120" stroke="#10b981" stroke-width="3"/>

  <rect x="600" y="45" width="160" height="150" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="680" y="80" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">공정 솔루션</text>
  <text x="680" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">레이저 스파이크 어닐링</text>
  <text x="680" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">Deep S/D 실리사이드</text>
  <text x="680" y="165" fill="#10b981" font-size="12" text-anchor="middle">기생 저항 극소화</text>
</svg>"""
        }
    ]
    return topics
