# -*- coding: utf-8 -*-
"""
직무 질문 11~15문항 데이터 생성 스크립트 (t_part3.py)
"""

def get_tech_topics_part3():
    topics = [
        {
            "id": "t_11",
            "category": "tech",
            "category_label": "반도체 소자·공정 실전 핵심",
            "number": 11,
            "title": "DIBL(Drain-Induced Barrier Lowering) 현상의 발생 원리와 문턱전압 강하 억제 설계",
            "core_keyword": ["드레인 유도 장벽 강하", "소스-채널 전위 장벽 침투", "FinFET/GAA 3차원 정전 제어"],
            "speech_1m30s": (
                "DIBL(드레인 유도 장벽 강하)은 게이트 길이가 짧아질 때, 드레인의 높은 역방향 전압이 게이트의 제어를 우회하여 소스 쪽 전위 장벽을 직접 무너뜨리는 치명적 단채널 효과입니다. "
                "장채널 소자에서는 소스에서 채널로 전자가 넘어가는 에너지 장벽 높이가 오직 게이트 전압(VG)에 의해서만 통제됩니다. "
                "그러나 채널이 수십 nm 이하로 좁혀지면 드레인 접합 공핍층의 횡방향 전계가 소스 근방까지 깊숙이 침투하여, 게이트 전압을 가하지 않아도 전위 장벽을 낮춰버립니다. "
                "그 결과 드레인 전압(VD)이 상승함에 따라 문턱전압(Vth)이 원치 않게 강하하고 오프 상태 누설 전류가 지수함수적으로 급증합니다. "
                "이를 제어하기 위해 소스/드레인 익스텐션 접합 깊이(Xj)를 극도로 얕게 만드는 USJ 공정을 적용하고, 채널 하부에 고농도 Halo 도핑을 주입하여 드레인 전계 침투를 차단합니다. "
                "나아가 채널의 3면 또는 4면을 게이트로 감싸는 FinFET과 GAA 구조로 전환하여 게이트의 정전기적 지배력을 물리적으로 극대화함으로써 DIBL을 완벽히 억제합니다."
            ),
            "deep_lecture": {
                "background": "DIBL 계수는 통상 $\\text{DIBL} = -\\frac{\\Delta V_{th}}{\\Delta V_D} \\text{ [mV/V]}$로 정의되며, 트랜지스터의 온/오프 스위칭 특성과 대기 전력(Standby Power)을 평가하는 핵심 벤치마크입니다.",
                "action_principle": "1. 장벽 강하 물리: 소스-채널 접합 전위 장벽 $\\phi_B$가 $V_D$에 의해 감소 ➔ 열전자 방출(Thermionic Emission) 전류 $I_{off} \\propto \\exp(-q\\phi_B / kT)$ 급증\n2. 억제 설계 파라미터:\n   - 자연 길이(Natural Length) 스케일링: $\\lambda = \\sqrt{\\frac{\\epsilon_{ch}}{\\epsilon_{ox}} t_{ch} t_{ox}}$ 최소화\n   - 접합 제어: USJ로 드레인 접합 깊이 $X_j$ 축소\n   - 도핑 제어: 국소 Retrograde 웰 및 Halo 임플란트\n   - 구조 전환: Planar ➔ FinFET ➔ GAA (MBCFET)로 전방위 전계 포위",
                "core_points": [
                    "드레인 전압($V_D$)의 전계 침투로 인한 소스 전위 장벽 강하 메커니즘 명시",
                    "DIBL에 의한 문턱전압 롤오프 및 대기 누설 전류 폭증 설명",
                    "USJ, Halo, FinFET/GAA로 이어지는 종합적 소자 억제 설계 제시"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="40" y="45" width="220" height="150" fill="#1e293b" stroke="#ef4444" stroke-width="2" rx="8"/>
  <text x="150" y="80" fill="#ef4444" font-size="15" font-weight="bold" text-anchor="middle">장채널 (정상 제어)</text>
  <text x="150" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">소스 장벽 = 오직 VG 제어</text>
  <text x="150" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">드레인 전계 영향 차단</text>
  <text x="150" y="165" fill="#38bdf8" font-size="12" text-anchor="middle">안정적 오프 상태 유지</text>

  <path d="M 275 120 L 315 120" stroke="#f59e0b" stroke-width="3"/>

  <rect x="330" y="45" width="230" height="150" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="445" y="80" fill="#f59e0b" font-size="15" font-weight="bold" text-anchor="middle">단채널 DIBL 발생</text>
  <text x="445" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">VD 전계가 소스 장벽 침투</text>
  <text x="445" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">전위 장벽 강하 ➔ Vth 하락</text>
  <text x="445" y="165" fill="#ef4444" font-size="12" text-anchor="middle">Off 누설 전류 폭증</text>

  <path d="M 575 120 L 615 120" stroke="#10b981" stroke-width="3"/>

  <rect x="630" y="45" width="130" height="150" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="695" y="80" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">소자 설계 대책</text>
  <text x="695" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">USJ 초박형 접합</text>
  <text x="695" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">Halo 포켓 도핑</text>
  <text x="695" y="165" fill="#10b981" font-size="12" text-anchor="middle">FinFET/GAA 전환</text>
</svg>"""
        },
        {
            "id": "t_12",
            "category": "tech",
            "category_label": "반도체 소자·공정 실전 핵심",
            "number": 12,
            "title": "Halo(Pocket) 이온 주입 메커니즘과 역 단채널 효과(Reverse Short Channel Effect, RSCE)",
            "core_keyword": ["Halo 포켓 도핑", "도펀트 프로파일 중첩(Overlap)", "역 단채널 효과(RSCE)"],
            "speech_1m30s": (
                "Halo(헤일로) 주입은 단채널 효과를 막기 위한 비장의 카드이지만, 그 부작용으로 문턱전압이 일시적으로 상승하는 '역 단채널 효과(RSCE)'를 동반합니다. "
                "헤일로는 소스/드레인 익스텐션 하단부에 기판과 동일한 전도형 도펀트를 경사각(Tilted)으로 국소 주입하여 접합 부근의 채널 농도를 의도적으로 높이는 공정입니다. "
                "이를 통해 드레인 공핍층이 채널 중앙으로 파고드는 펀치스루를 효과적으로 차단합니다. "
                "그런데 채널 길이가 충분히 긴 소자에서는 헤일로 도펀트가 양쪽 가장자리에만 머물러 전체 문턱전압에 미치는 영향이 미미하지만, 채널 길이가 수백 nm 수준으로 짧아지면 양쪽의 고농도 헤일로 영역이 채널 중심부에서 서로 겹치게 됩니다. "
                "그 결과 평균 채널 농도(NA)가 급증하여 통상적인 단채널 효과와 반대로 채널이 줄어들수록 문턱전압(Vth)이 오히려 높아지는 역 단채널 효과가 발생합니다. "
                "이후 채널이 임계값 이하로 극단적으로 짧아지면 결국 완전 공핍화로 급격한 Vth 롤오프가 발생하므로, 헤일로 도즈량과 어닐링 조건을 정밀 튜닝하여 산포를 제어해야 합니다."
            ),
            "deep_lecture": {
                "background": "스케일링 과정에서 문턱전압이 채널 길이에 따라 롤오프(Roll-off)되는 것을 방어하려다 발생하는 대표적인 비선형 물리 현상입니다. 아날로그 및 메모리 주변 회로 매칭에 직접적인 영향을 줍니다.",
                "action_principle": "1. Halo 주입 원리: NMOS 기준 p형(붕소 B) 도펀트를 15~45도 경사로 주입 ➔ S/D 에지 하부의 기판 농도 $N_A$ 국소 증가 ➔ 공핍 영역 확장 차단\n2. RSCE 메커니즘: 채널 길이 $L$ 감소 ➔ Halo 도펀트의 채널 중앙 중첩(Profile overlap) ➔ 실효 $\\overline{N_A}$ 증가 ➔ $V_{th} = V_{FB} + 2\\phi_F + \\frac{\\sqrt{2q\\epsilon_{Si}\\overline{N_A}(2\\phi_F)}}{C_{ox}}$ 에 의해 $V_{th}$ 일시적 상승\n3. TED(Transient Enhanced Diffusion) 영향: 주입 결함(Self-interstitial)에 의해 실리콘 표면으로 도펀트가 석출되는 현상도 RSCE를 심화시킴\n4. 양산 제어: 극저에너지 주입과 밀리초 어닐링으로 급격한 도펀트 경계(Steep profile) 형성",
                "core_points": [
                    "Halo 주입의 본질(국소 고농도 경사 주입을 통한 펀치스루 차단) 규명",
                    "채널 길이 축소 시 도펀트 중첩으로 인한 실효 채널 농도($\\overline{N_A}$) 증가 설명",
                    "RSCE 곡선(Vth 일시 상승 후 급격한 롤오프)의 물리적 거동 명쾌한 정리"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="40" y="45" width="220" height="150" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="150" y="80" fill="#38bdf8" font-size="15" font-weight="bold" text-anchor="middle">Halo 경사 주입</text>
  <text x="150" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">S/D 에지 하부 국소 도핑</text>
  <text x="150" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">기판과 동일 극성 주입</text>
  <text x="150" y="165" fill="#38bdf8" font-size="12" text-anchor="middle">펀치스루 1차 방어선</text>

  <path d="M 275 120 L 315 120" stroke="#f59e0b" stroke-width="3"/>

  <rect x="330" y="45" width="230" height="150" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="445" y="80" fill="#f59e0b" font-size="15" font-weight="bold" text-anchor="middle">도펀트 중첩 현상</text>
  <text x="445" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">채널 단축 시 양쪽 Halo 만남</text>
  <text x="445" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">채널 중심 유효 농도 NA 급증</text>
  <text x="445" y="165" fill="#f59e0b" font-size="12" text-anchor="middle">Vth 일시적 상승 (RSCE)</text>

  <path d="M 575 120 L 615 120" stroke="#10b981" stroke-width="3"/>

  <rect x="630" y="45" width="130" height="150" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="695" y="80" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">Vth 거동</text>
  <text x="695" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">상승 후 급락</text>
  <text x="695" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">비선형 산포</text>
  <text x="695" y="165" fill="#10b981" font-size="12" text-anchor="middle">어닐링 정밀화</text>
</svg>"""
        },
        {
            "id": "t_13",
            "category": "tech",
            "category_label": "반도체 소자·공정 실전 핵심",
            "number": 13,
            "title": "MOS 구조에서 공핍 커패시턴스(Cdep)와 접합 커패시턴스(Cj)의 차이 및 Subthreshold Swing(SS)에 미치는 영향",
            "core_keyword": ["공핍 커패시턴스 Cdep vs 접합 커패시턴스 Cj", "전압 분배기 메커니즘", "이론 한계 60 mV/dec"],
            "speech_1m30s": (
                "공핍 커패시턴스(Cdep)와 접합 커패시턴스(Cj)는 모두 반도체의 공간 전하 영역에서 발생하지만 작용하는 위치와 회로적 영향이 본질적으로 다릅니다. "
                "Cdep은 게이트 전압 인가 시 채널 표면 바로 아래 형성되는 공핍층 용량으로, 게이트 산화막 용량(Cox)과 직렬 연결되어 게이트 전압을 나누어 갖는 전압 분배기 역할을 합니다. "
                "따라서 Cdep가 커질수록 게이트 전압이 실리콘 표면 전위를 제어하는 효율이 떨어지며, 서브스레숄드 스윙(SS) 공식 '60mV 곱하기 (1 + Cdep/Cox)'에 의해 SS가 나빠집니다. "
                "온/오프 스위칭을 가파르게 만들어 누설을 줄이려면 Cdep/Cox 비율을 0에 가깝게 줄여야 합니다. "
                "반면 접합 커패시턴스(Cj)는 소스/드레인 확산 영역과 기판 사이의 pn 접합에서 생기는 용량으로, 트랜지스터의 정적 스위칭 기울기가 아닌 신호 전송 시 RC 딜레이와 동적 스위칭 전력 소모를 결정짓습니다. "
                "이 두 커패시턴스를 구분하여 채널 전계 효율과 AC 스위칭 속도를 동시에 극대화하겠습니다."
            ),
            "deep_lecture": {
                "background": "트랜지스터의 DC 스위칭 성능(SS)과 AC 동작 속도($f_{max}$)를 결정하는 두 가지 핵심 기생 용량의 물리적 차이를 명확히 이해하고 있는지 검증하는 소자 물리 핵심 질문입니다.",
                "action_principle": "1. 공핍 커패시턴스 $C_{dep}$: $C_{dep} = \\frac{\\epsilon_{Si}}{W_d}$, 채널 표면에 직렬 배치 ➔ 표면 전위 제어율 $m = 1 + \\frac{C_{dep}}{C_{ox}}$ 결정\n2. Subthreshold Swing(SS) 영향: $SS = \\ln(10) \\cdot \\frac{kT}{q} \\cdot \\left(1 + \\frac{C_{dep}}{C_{ox}}\\right)$. $C_{dep}$가 존재하면 상온 이론 한계($60\\text{ mV/dec}$)보다 커져 누설 전류 증가\n3. 완전 공핍(FD) 혁신: FD-SOI나 FinFET/GAA는 기판 두께가 극도로 얇아 공핍층이 더 이상 늘어나지 못함 ($W_d = t_{body}$, 완전 공핍화) ➔ $C_{dep} \\to 0$에 수렴하여 이상적인 $60\\text{ mV/dec}$에 근접\n4. 접합 커패시턴스 $C_j$: $C_j = \\frac{\\epsilon_{Si} A_{j}}{W_{pn}}$, 소스/드레인-웰 간의 병렬 커패시턴스로 동작 지연 시간 $\\tau = R_{total} C_j$ 및 동적 전력 $P = C_j V^2 f$에 영향",
                "core_points": [
                    "$C_{dep}$의 직렬 전압 분배 역할과 SS 수식($1 + C_{dep}/C_{ox}$) 연계",
                    "$C_j$의 병렬 RC 딜레이 및 동적 스위칭 속도 영향 구분",
                    "FinFET/GAA에서 완전 공핍화를 통해 SS가 60 mV/dec에 근접하는 원리 설명"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="40" y="45" width="220" height="150" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="150" y="80" fill="#38bdf8" font-size="15" font-weight="bold" text-anchor="middle">공핍 커패시턴스 Cdep</text>
  <text x="150" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">게이트 Cox와 직렬 연결</text>
  <text x="150" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">전압 분배기: SS 기울기 결정</text>
  <text x="150" y="165" fill="#38bdf8" font-size="12" text-anchor="middle">SS = 60(1 + Cdep/Cox)</text>

  <path d="M 275 120 L 315 120" stroke="#f59e0b" stroke-width="3"/>

  <rect x="330" y="45" width="230" height="150" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="445" y="80" fill="#f59e0b" font-size="15" font-weight="bold" text-anchor="middle">접합 커패시턴스 Cj</text>
  <text x="445" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">S/D - 기판 pn 접합 용량</text>
  <text x="445" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">배선 및 기생 로드 연결</text>
  <text x="445" y="165" fill="#f59e0b" font-size="12" text-anchor="middle">AC 딜레이(RC) &amp; 동적 전력</text>

  <path d="M 575 120 L 615 120" stroke="#10b981" stroke-width="3"/>

  <rect x="630" y="45" width="130" height="150" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="695" y="80" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">소자 최적화</text>
  <text x="695" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">완전공핍(FD)</text>
  <text x="695" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">SS ≈ 60mV</text>
  <text x="695" y="165" fill="#10b981" font-size="12" text-anchor="middle">초고속 스위칭</text>
</svg>"""
        },
        {
            "id": "t_14",
            "category": "tech",
            "category_label": "반도체 소자·공정 실전 핵심",
            "number": 14,
            "title": "HBM(High Bandwidth Memory)의 핵심 TSV 적층 기술과 MR-MUF의 방열/보이드 억제 메커니즘",
            "core_keyword": ["SK하이닉스 독보적 MR-MUF", "액상 에폭시 일괄 주입", "열 저항 40% 개선 & 무결점 보이드"],
            "speech_1m30s": (
                "SK하이닉스가 글로벌 AI 메모리 패권을 장악한 핵심 병기는 바로 TSV 초미세 수직 적층과 독보적인 'MR-MUF(Mass Reflow Molded Underfill)' 패키징 기술입니다. "
                "수천 개의 마이크로 범프로 구성된 TSV 적층에서 가장 큰 난제는 칩 간 수 마이크로미터의 미세 갭에 공기 방울인 '보이드(Void)'가 생기는 것과, 초고단 적층 시 발생하는 막대한 발열입니다. "
                "경쟁사가 사용하는 필름 부착 방식(TC-NCF)은 칩을 한 장 쌓을 때마다 열과 압력을 가해야 해 공정 시간이 길고 필름 간 보이드 위험과 웨이퍼 휨이 발생합니다. "
                "반면 SK하이닉스의 MR-MUF는 적층된 수천 개 범프를 한 번에 일괄 리플로우하여 접합한 후, 액체 상태의 보호재를 칩 사이에 고압 주입해 굳히는 일괄 공정입니다. "
                "액상이 미세 틈새를 완벽히 파고들어 보이드 발생을 원천 제어하며, 고밀도 열전도 필러가 첨가된 특수 소재를 통해 열 저항을 40% 이상 대폭 낮췄습니다. "
                "이 압도적인 수율과 방열 신뢰성이 HBM 16단 이상의 초고단 적층을 가능케 하는 핵심 원동력입니다."
            ),
            "deep_lecture": {
                "background": "HBM은 초고속 데이터 전송에 따른 발열 제어가 제품의 생사를 결정합니다. SK하이닉스는 3세대 HBM2E부터 MR-MUF를 도입하고 HBM3E에 '어드밴스드 MR-MUF'를 적용하여 시장 점유율 1위를 확고히 굳혔습니다.",
                "action_principle": "1. TSV 수직 연결: 실리콘 다이를 관통하는 초미세 구리 기둥(TSV)으로 1,024개 I/O 병렬 연결\n2. TC-NCF vs MR-MUF 비교:\n   - TC-NCF: 고체 필름 ➔ 칩 단위 열압착 ➔ 누적 열 스트레스, 보이드 트랩, 긴 텍트 타임\n   - MR-MUF: 일괄 리플로우(Mass Reflow) ➔ 액상 에폭시 몰딩 언더필(Molded Underfill) 주입 ➔ 공정 단순화, 기계적 응력 분산\n3. Advanced MR-MUF의 방열 메커니즘: 미세 실리카 필러 함량을 높여 열전도도(Thermal Conductivity) 2.5배 향상, 칩 두께를 얇게 하면서도 휨 현상(Warpage) 방지\n4. 효과: 방열 성능 40% 개선, 생산성 3배 향상",
                "core_points": [
                    "MR-MUF의 일괄 리플로우 및 액체 언더필 주입 프로세스 명쾌한 대비",
                    "TC-NCF 대비 보이드 제어 및 열저항 40% 개선의 물리적 이유 설명",
                    "SK하이닉스의 HBM 초격차 주도권과 패키징 기술의 직결"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="40" y="45" width="220" height="150" fill="#1e293b" stroke="#ef4444" stroke-width="2" rx="8"/>
  <text x="150" y="80" fill="#ef4444" font-size="15" font-weight="bold" text-anchor="middle">종래 방식 (TC-NCF)</text>
  <text x="150" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">고체 필름 매장마다 압착</text>
  <text x="150" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">미세 에어포켓(보이드) 리스크</text>
  <text x="150" y="165" fill="#f87171" font-size="12" text-anchor="middle">열전도도 한계 및 휨 발생</text>

  <path d="M 275 120 L 315 120" stroke="#38bdf8" stroke-width="3"/>

  <rect x="330" y="45" width="230" height="150" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="445" y="80" fill="#38bdf8" font-size="15" font-weight="bold" text-anchor="middle">SK하이닉스 MR-MUF</text>
  <text x="445" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">범프 일괄 리플로우(MR)</text>
  <text x="445" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">액상 에폭시 고압 주입(MUF)</text>
  <text x="445" y="165" fill="#38bdf8" font-size="12" text-anchor="middle">미세 갭 완벽 충진 (보이드 0%)</text>

  <path d="M 575 120 L 615 120" stroke="#10b981" stroke-width="3"/>

  <rect x="630" y="45" width="130" height="150" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="695" y="80" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">초격차 결과</text>
  <text x="695" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">열저항 40% 개선</text>
  <text x="695" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">생산성 3배 향상</text>
  <text x="695" y="165" fill="#10b981" font-size="12" text-anchor="middle">16단+ HBM 석권</text>
</svg>"""
        },
        {
            "id": "t_15",
            "category": "tech",
            "category_label": "반도체 소자·공정 실전 핵심",
            "number": 15,
            "title": "RIE(Reactive Ion Etching) 식각에서 화학적 라디칼과 물리적 이온 충돌의 시너지 메커니즘 (Coburn-Winters Model)",
            "core_keyword": ["Coburn-Winters 시너지 모델", "라디칼 흡착 + 이온 충돌 손상 활성화", "수직 이방성 및 고선택비"],
            "speech_1m30s": (
                "반도체 건식 식각의 근간인 RIE의 본질은 화학적 라디칼과 물리적 이온 충돌이 결합하여 단독 효과의 합보다 수십 배 높은 식각률을 내는 'Coburn-Winters 시너지 메커니즘'에 있습니다. "
                "중성 라디칼에 의한 순수 화학 식각은 선택비는 높지만 모든 방향으로 깎이는 등방성(Isotropic)을 띠어 언더컷이 발생합니다. "
                "반대로 아르곤 같은 이온의 물리적 스퍼터 식각은 수직성은 우수하지만 식각 속도가 느리고 하부막 손상과 낮은 선택비가 문제입니다. "
                "RIE는 이 둘을 동시에 챔버 내에서 일으킵니다. 수직으로 직진하는 고에너지 양이온이 실리콘 표면을 타격하여 표면 격자 결합을 끊고 화학적 활성화 상태(Damage Layer)를 생성하거나 측벽 보호막을 제거합니다. "
                "이 활성화된 부위에 화학 라디칼이 결합하여 상온에서도 기화하기 쉬운 SiF4와 같은 휘발성 가스를 폭발적으로 생성해 탈착시킵니다. "
                "이온이 도달하지 못하는 측벽은 식각되지 않고 오직 수직 방향으로만 고속 식각이 진행되어 완벽한 수직 이방성과 높은 선택비를 동시에 달성합니다."
            ),
            "deep_lecture": {
                "background": "1979년 Coburn과 Winters가 발표한 $XeF_2$ 가스와 $Ar^+$ 이온의 시너지 식각 실험은 현대 모든 플라즈마 건식 식각(RIE, ICP, CCP) 장비의 동작 이론적 토대입니다.",
                "action_principle": "1. 단독 효과의 한계:\n   - Radical-only ($XeF_2$): 실리콘 자발 식각 속도 약 $5\\text{ Å/min}$\n   - Ion-only ($Ar^+$): 순수 물리 스퍼터링 속도 약 $2\\text{ Å/min}$\n2. 동시 조사 시 시너지: 두 입자가 동시 조사될 때 식각 속도가 $50\\sim 100\\text{ Å/min}$로 10배 이상 비약적 증가\n3. 표면 반응 3단계:\n   - 1단계: 수직 충돌 이온이 실리콘 결합 절단 및 흡착 활성화 사이트 형성\n   - 2단계: 불소(F) 라디칼이 활성화된 Si 원자와 빠르게 반응하여 할로겐화물 계면층($SiF_x$) 형성\n   - 3단계: 이온의 추가 충돌 에너지로 $SiF_4$ 휘발 촉진 및 배기\n4. 측벽 보호막(Passivation): 플루오로카본($CF_x$) 폴리머가 측벽을 보호하여 완벽한 수직 프로파일 사수",
                "core_points": [
                    "Coburn-Winters 실험의 시너지 효과(1+1이 10 이상이 되는 메커니즘) 언급",
                    "이온의 수직 타격에 의한 결합 손상/활성화와 라디칼의 휘발성 부산물 탈착 연계",
                    "측벽 보호막(Passivation) 형성을 통한 완벽한 수직 이방성(Anisotropy) 달성"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="40" y="45" width="220" height="150" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="150" y="80" fill="#38bdf8" font-size="15" font-weight="bold" text-anchor="middle">화학적 라디칼 (F*)</text>
  <text x="150" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">높은 화학 선택비</text>
  <text x="150" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">단독 시 등방성 언더컷 발생</text>
  <text x="150" y="165" fill="#38bdf8" font-size="12" text-anchor="middle">낮은 자발 식각 속도</text>

  <path d="M 275 120 L 315 120" stroke="#f59e0b" stroke-width="3"/>

  <rect x="330" y="45" width="230" height="150" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="445" y="80" fill="#f59e0b" font-size="15" font-weight="bold" text-anchor="middle">물리적 이온 (Ar+)</text>
  <text x="445" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">수직 방향 직진 타격</text>
  <text x="445" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">표면 격자 결합 파괴·활성화</text>
  <text x="445" y="165" fill="#f59e0b" font-size="12" text-anchor="middle">측벽 폴리머 스퍼터링 제거</text>

  <path d="M 575 120 L 615 120" stroke="#10b981" stroke-width="3"/>

  <rect x="630" y="45" width="130" height="150" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="695" y="80" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">시너지 식각</text>
  <text x="695" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">식각 속도 10배↑</text>
  <text x="695" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">수직 프로파일</text>
  <text x="695" y="165" fill="#10b981" font-size="12" text-anchor="middle">Coburn-Winters</text>
</svg>"""
        }
    ]
    return topics
