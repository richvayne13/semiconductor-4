# -*- coding: utf-8 -*-
"""
직무 질문 6~10문항 데이터 생성 스크립트 (t_part2.py)
"""

def get_tech_topics_part2():
    topics = [
        {
            "id": "t_06",
            "category": "tech",
            "category_label": "반도체 소자·공정 실전 핵심",
            "number": 6,
            "title": "이온 주입 시 채널링(Channeling)과 게이트 산화막의 터널링(Tunneling)의 물리적 차이 및 억제 대책",
            "core_keyword": ["고전적 결정 격자 통과 vs 양자역학적 장벽 투과", "7도 틸트 & PAI", "High-k EOT 디커플링"],
            "speech_1m30s": (
                "채널링과 터널링은 이름은 유사하지만 발생 영역과 물리적 메커니즘이 완전히 다른 별개의 현상입니다. "
                "채널링은 이온 주입 시 발생하는 '고전역학적 격자 경로 현상'입니다. 단결정 실리콘의 특정 결정축 방향으로 입사된 이온이 원자핵과 큰 산란 충돌을 겪지 않고, 격자 사이의 빈 공간을 터널처럼 깊숙이 파고들어 접합 깊이 꼬리(Tail)를 형성하는 불량입니다. "
                "이를 억제하기 위해 웨이퍼를 7도 기울이는 틸트(Tilt) 주입이나, Ge/Si 이온으로 표면을 미리 비정질화하는 PAI 공정을 적용합니다. "
                "반면 터널링은 게이트 유전막에서 일어나는 '양자역학적 파동 투과 현상'입니다. 산화막 두께가 1.5nm 이하로 얇아질 때, 전자가 자신의 에너지보다 높은 절연막 전위 장벽을 파동함수 상태로 직접 뚫고 지나가 누설 전류를 유발합니다. "
                "이를 막기 위해 물리적 두께를 두껍게 유지하면서도 정전 용량을 확보하는 High-k 유전체를 도입합니다. "
                "이처럼 두 현상의 물리적 차이를 명확히 구분하여 공정 결함과 소자 누설을 정확히 타겟팅하겠습니다."
            ),
            "deep_lecture": {
                "background": "공정 현장에서 자주 혼동되는 두 용어의 물리적 본질(Classical vs Quantum)을 구분하고, 각각의 현상이 소자 신뢰성에 미치는 영향과 양산 대응책을 설명하는 고난도 질문입니다.",
                "action_principle": "1. 채널링의 본질: 고전적 핵 저지능(Nuclear Stopping Power) 결여 ➔ 결정 격자 간극 통과 ➔ 도펀트 프로파일 왜곡 ➔ 틸트(7° Tilt) 및 사전 비정질화(PAI)로 방어\n2. 터널링의 본질: 양자역학적 슈뢰딩거 파동 투과 ➔ 터널링 확률 $T \\propto \\exp(-2\\kappa d)$ ➔ 게이트 누설 급증 ➔ High-k($HfO_2$) 도입으로 물리적 두께 $d$ 확보\n3. 완벽한 대조 요약: 채널링은 기판 내부 '이온의 기하학적 깊이 이탈', 터널링은 절연막을 가로지르는 '전자의 파동적 절연 파괴'",
                "core_points": [
                    "고전역학적 공간 통과(Channeling)와 양자역학적 전위 장벽 투과(Tunneling) 명쾌한 대조",
                    "채널링 대책: 7° 틸트, 트위스트, PAI(Pre-Amorphization Implantation)",
                    "터널링 대책: High-k 메탈 게이트(HKMG)를 통한 물리적 두께 확보"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="40" y="45" width="220" height="150" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="150" y="80" fill="#38bdf8" font-size="15" font-weight="bold" text-anchor="middle">채널링 (Channeling)</text>
  <text x="150" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">이온 주입 시 결정축 침투</text>
  <text x="150" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">고전적 기하 경로 통과</text>
  <text x="150" y="165" fill="#38bdf8" font-size="12" text-anchor="middle">대책: 7° 틸트 &amp; PAI 공정</text>

  <path d="M 275 120 L 315 120" stroke="#f59e0b" stroke-width="3"/>

  <rect x="330" y="45" width="230" height="150" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="445" y="80" fill="#f59e0b" font-size="15" font-weight="bold" text-anchor="middle">터널링 (Tunneling)</text>
  <text x="445" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">게이트 절연막 전위 장벽</text>
  <text x="445" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">양자역학적 파동함수 투과</text>
  <text x="445" y="165" fill="#f59e0b" font-size="12" text-anchor="middle">대책: High-k 박막 도입</text>

  <path d="M 575 120 L 615 120" stroke="#10b981" stroke-width="3"/>

  <rect x="630" y="45" width="130" height="150" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="695" y="80" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">핵심 요약</text>
  <text x="695" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">이온 vs 전자</text>
  <text x="695" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">고전 vs 양자</text>
  <text x="695" y="165" fill="#10b981" font-size="12" text-anchor="middle">기하 vs 장벽</text>
</svg>"""
        },
        {
            "id": "t_07",
            "category": "tech",
            "category_label": "반도체 소자·공정 실전 핵심",
            "number": 7,
            "title": "HKMG 공정에서 TiN과 TaN의 일함수 조절(WFM) 및 금속 게이트 확산 배리어로서의 역할",
            "core_keyword": ["티아이엔(TiN) & 티에이엔(TaN)", "일함수 금속(WFM)", "확산 배리어(Barrier Metal)"],
            "speech_1m30s": (
                "HKMG 구조에서 '티아이엔(TiN)'과 '티에이엔(TaN)'은 소자의 문턱전압을 결정하는 '일함수 조절 금속(WFM)'이자 상하부 층간 오염을 막는 '확산 배리어'라는 핵심 이중 역할을 수행합니다. "
                "과거 폴리실리콘 게이트의 공핍화(Poly Depletion)와 페르미 레벨 피닝을 해결하기 위해 금속 게이트가 도입되었습니다. "
                "이때 TiN과 TaN은 질소 비율과 박막 두께 제어를 통해 약 4.6~4.9 eV 수준의 일함수를 형성하여 PMOS의 목표 문턱전압을 정확히 맞추는 p-WFM 핵심 소재로 활용됩니다. "
                "동시에 상부의 저저항 메인 게이트인 텅스텐(W)이나 알루미늄 원자가 하부의 초박형 High-k 유전체(HfO2)로 침투하여 특성을 파괴하는 것을 차단하는 견고한 확산 방지막 역할을 합니다. "
                "결정립계가 조밀한 비정질 또는 나노결정질 구조를 형성하여 산소 공공 확산까지 억제함으로써 소자의 수명과 동작 신뢰성을 보장합니다. "
                "TiN/TaN 박막의 ALD 증착 정밀 제어로 선단 메모리의 문턱전압 산포를 완벽히 통제하겠습니다."
            ),
            "deep_lecture": {
                "background": "HKMG는 32nm 로직 및 1z/1a nm DRAM 이후 필수 공정입니다. 폴리실리콘의 공핍층(약 0.4nm EOT 손실)을 제거하고, HfO2와의 계면 반응을 제어하기 위해 전이금속 질화물인 TiN, TaN이 표준으로 사용됩니다.",
                "action_principle": "1. 명칭 및 호칭: 학술/현업에서 TiN은 '티아이엔' 또는 질화티타늄, TaN은 '티에이엔' 또는 질화탄탈럼으로 호칭\n2. 일함수 엔지니어링: $V_{th} = \\Phi_{ms} - \\frac{Q_{ox}}{C_{ox}} + 2\\phi_F + \\frac{Q_d}{C_{ox}}$에서 금속 일함수($\\Phi_m$)를 실리콘 밴드에 매칭. TiN은 두께 튜닝을 통해 PMOS 또는 Mid-gap 전극으로 작동\n3. 확산 배리어 기능: 금속 게이트 필링재(W, Al)의 스파이킹 방지 및 산소 유입 차단으로 EOT 증가(Oxidation) 방어\n4. ALD 증착 기법: 수 나노미터 급 단차 피복성(Conformality) 확보를 위해 PEALD로 원자층 제어",
                "core_points": [
                    "TiN/TaN의 정확한 호칭 및 이중 역할(WFM + 배리어) 명확 제시",
                    "폴리실리콘 공핍 효과(Poly Depletion) 극복 배경 설명",
                    "질소 농도 및 두께 조절을 통한 일함수($\\Phi_m$) 엔지니어링 원리"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="40" y="45" width="220" height="150" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="150" y="80" fill="#38bdf8" font-size="15" font-weight="bold" text-anchor="middle">역할 1: WFM 일함수</text>
  <text x="150" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">TiN / TaN (티아이엔/티에이엔)</text>
  <text x="150" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">일함수 4.6 ~ 4.9 eV 튜닝</text>
  <text x="150" y="165" fill="#38bdf8" font-size="12" text-anchor="middle">목표 문턱전압(Vth) 정밀 셋업</text>

  <path d="M 275 120 L 315 120" stroke="#f59e0b" stroke-width="3"/>

  <rect x="330" y="45" width="230" height="150" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="445" y="80" fill="#f59e0b" font-size="15" font-weight="bold" text-anchor="middle">역할 2: 확산 배리어</text>
  <text x="445" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">상부 메탈(W, Al) 상호 침투 차단</text>
  <text x="445" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">산소 결함(Oxygen Vacancy) 방어</text>
  <text x="445" y="165" fill="#f59e0b" font-size="12" text-anchor="middle">조밀한 결정립 나노박막</text>

  <path d="M 575 120 L 615 120" stroke="#10b981" stroke-width="3"/>

  <rect x="630" y="45" width="130" height="150" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="695" y="80" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">HKMG 완성</text>
  <text x="695" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">Poly 공핍 제거</text>
  <text x="695" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">HfO2 계면 보호</text>
  <text x="695" y="165" fill="#10b981" font-size="12" text-anchor="middle">신뢰성 확보</text>
</svg>"""
        },
        {
            "id": "t_08",
            "category": "tech",
            "category_label": "반도체 소자·공정 실전 핵심",
            "number": 8,
            "title": "접합 및 실리사이드 공정에서 Pt(백금)의 역할 (NiPt 살리사이드 열안정성 및 초고일함수 전극)",
            "core_keyword": ["피티(Pt) / 백금", "NiPt 실리사이드 열안정화", "NiSi2 상전이 억제"],
            "speech_1m30s": (
                "반도체 공정에서 '피티(Pt)' 즉 백금은 극소량의 첨가만으로 니켈 실리사이드(NiSi)의 치명적 약점인 '열적 불안정성'을 완벽히 해결하는 핵심 구원투수입니다. "
                "선단 미세 공정에서는 실리콘 소모량이 적고 저온 형성이 가능한 NiSi가 필수적이지만, 600도 이상의 후속 열공정을 거치면 고저항상인 NiSi2로 상전이되거나 박막이 뭉치는 응집(Agglomeration) 현상으로 콘택 저항이 폭증합니다. "
                "이때 니켈에 약 5~10%의 Pt를 합금 형태로 도핑하면, Pt가 결정립계(Grain Boundary)에 편석되어 실리콘과의 계면 에너지를 낮추고 NiSi2 형성의 핵생성 장벽을 대폭 높입니다. "
                "그 결과 실리사이드의 열적 분해 온도를 750도 이상으로 150도 가량 끌어올려 고저항 상전이를 원천 차단합니다. "
                "또한 Pt 자체의 5.6eV에 달하는 매우 높은 일함수를 활용해 PMOS 쇼트키 접합이나 차세대 커패시터 전극에서 누설 전류를 억제합니다. "
                "희유금속 Pt의 고유 물성을 극대화하여 초미세 접합의 전기적 신뢰성을 확보하겠습니다."
            ),
            "deep_lecture": {
                "background": "과거 CoSi2에서 NiSi로 전환된 이유는 실리콘 소모량 감소와 세장화 효과(Narrow linewidth effect) 극복 때문이었습니다. 그러나 NiSi의 낮은 열적 내구성(Thermal Budget 취약)을 해결한 것이 바로 Pt 첨가 기술입니다.",
                "action_principle": "1. 호칭 정의: 현업에서는 '피티' 또는 '백금(Platinum)'으로 통칭\n2. NiSi의 열적 한계: 약 600℃에서 고저항 면심입방(FCC) 구조의 $NiSi_2$로 상전이 발생 및 결정립 응집에 의한 단선/저항 급증\n3. Pt의 열안정화 메커니즘: Pt는 NiSi 격자 내에 치환 고용되어 계면 에너지를 안정화하고, $NiSi_2$ 상전이 엔탈피 장벽을 증가시킴 (열안정성 약 150℃ 향상)\n4. 고일함수 응용: Pt는 금속 중 최고 수준의 일함수($\\sim 5.65\\text{ eV}$)를 가져 PMOS 쇼트키 배리어 높이(SBH)를 낮추고 전도성 극대화",
                "core_points": [
                    "Pt의 정확한 발음(피티/백금)과 NiPt 살리사이드(Salicide) 적용 배경",
                    "NiSi에서 $NiSi_2$로의 고저항 상전이 억제 메커니즘 설명",
                    "초고일함수(5.6 eV) 특성과 접합 저항 개선의 연계"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="40" y="45" width="220" height="150" fill="#1e293b" stroke="#ef4444" stroke-width="2" rx="8"/>
  <text x="150" y="80" fill="#ef4444" font-size="15" font-weight="bold" text-anchor="middle">순수 NiSi의 취약점</text>
  <text x="150" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">600℃ 이상 후속 열공정</text>
  <text x="150" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">고저항 NiSi2 상전이</text>
  <text x="150" y="165" fill="#f87171" font-size="12" text-anchor="middle">결정립 응집 ➔ 저항 폭증</text>

  <path d="M 275 120 L 315 120" stroke="#38bdf8" stroke-width="3"/>

  <rect x="330" y="45" width="230" height="150" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="445" y="80" fill="#38bdf8" font-size="15" font-weight="bold" text-anchor="middle">Pt 첨가 혁신 (NiPt)</text>
  <text x="445" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">5~10% Pt 고용 합금</text>
  <text x="445" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">NiSi2 핵생성 장벽 대폭 상승</text>
  <text x="445" y="165" fill="#38bdf8" font-size="12" text-anchor="middle">열분해 온도 750℃+ 보장</text>

  <path d="M 575 120 L 615 120" stroke="#10b981" stroke-width="3"/>

  <rect x="630" y="45" width="130" height="150" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="695" y="80" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">초고일함수</text>
  <text x="695" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">Pt 일함수 5.6eV</text>
  <text x="695" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">PMOS SBH 강하</text>
  <text x="695" y="165" fill="#10b981" font-size="12" text-anchor="middle">접합 저항 극소화</text>
</svg>"""
        },
        {
            "id": "t_09",
            "category": "tech",
            "category_label": "반도체 소자·공정 실전 핵심",
            "number": 9,
            "title": "DRAM 셀에서 BCAT(Buried Channel Array Transistor) 도입 배경 및 GIDL(Gate-Induced Drain Leakage) 억제 메커니즘",
            "core_keyword": ["매립형 게이트 BCAT", "유효 채널 길이(Leff) 3차원 확보", "GIDL 억제 및 Retention 개선"],
            "speech_1m30s": (
                "DRAM 미세화에서 BCAT(매립형 트랜지스터)이 필수 도입된 이유는 '평면 트랜지스터의 채널 길이 한계 극복'과 'GIDL 누설 전류 억제를 통한 리프레시 시간 사수' 때문입니다. "
                "DRAM 셀 피치가 40nm 이하로 줄어들며 종래 평면 트랜지스터는 단채널 효과로 인해 전하를 유지하지 못하고 문턱전압이 무너졌습니다. "
                "BCAT은 실리콘 기판 내부를 트렌치 형태로 깊게 파고 그 내부에 워드라인 게이트를 매립함으로써, 한정된 셀 면적 안에서도 유효 채널 길이(Leff)를 3차원 곡면을 따라 2배 이상 길게 확보했습니다. "
                "특히 DRAM 커패시터에 저장된 전하 손실의 주원인인 GIDL은 게이트와 드레인 겹침 영역의 강한 수직 전계로 인해 발생하는 밴드 간 터널링(BTBT) 현상입니다. "
                "BCAT 구조는 게이트 상부를 두꺼운 절연 질화막 캡핑층으로 매립 격리하여 게이트와 저장 노드 접합 간의 최대 전계를 완화시켰습니다. "
                "이를 통해 오프 상태 누설 전류를 획기적으로 낮추어 DRAM의 핵심 척도인 데이터 보존 시간(tRET)을 비약적으로 개선했습니다."
            ),
            "deep_lecture": {
                "background": "DRAM 셀은 1T-1C 구조로 커패시터의 전하 누설을 막아 리프레시(Refresh) 주기를 길게 가져가는 것이 상용화의 핵심입니다. BCAT은 20nm 이하 DRAM 양산의 최대 분수령이 된 3차원 트랜지스터 구조입니다.",
                "action_principle": "1. 구조적 혁신: 평면(Planar) 게이트 ➔ 기판 음각 식각 후 게이트 매립(Buried Wordline) ➔ 유효 채널 길이($L_{eff}$) 극대화로 SCE 차단\n2. GIDL 물리 메커니즘: 게이트가 오프($V_G < 0$)이고 저장 노드가 충전($V_D = V_{DD}$)일 때, 강한 계면 전계에 의해 실리콘 원자가 전자대에서 전도대로 전자가 직접 터널링(Band-to-Band Tunneling, BTBT)\n3. BCAT의 GIDL 차단책: 게이트 전극을 기판 표면 아래로 깊게 낮추고 상부에 Nitride Capping 증착 ➔ Gate-to-Drain Overlap 영역의 국소 전계 집중 완화\n4. 효과: 리텐션 타임(Retention time) 수 배 연장 및 센싱 마진 확보",
                "core_points": [
                    "3차원 기판 매립을 통한 유효 채널 길이($L_{eff}$) 확보 원리",
                    "GIDL의 물리적 실체인 밴드 간 터널링(BTBT)과 리프레시(tRET) 연결",
                    "절연 캡핑층을 통한 게이트-드레인 전계 완화 메커니즘 설명"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="40" y="45" width="220" height="150" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="150" y="80" fill="#38bdf8" font-size="15" font-weight="bold" text-anchor="middle">3차원 매립 구조</text>
  <text x="150" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">실리콘 음각 트렌치 식각</text>
  <text x="150" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">게이트 전극 내부 매립</text>
  <text x="150" y="165" fill="#38bdf8" font-size="12" text-anchor="middle">유효 채널(Leff) 2배 확보</text>

  <path d="M 275 120 L 315 120" stroke="#f59e0b" stroke-width="3"/>

  <rect x="330" y="45" width="230" height="150" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="445" y="80" fill="#f59e0b" font-size="15" font-weight="bold" text-anchor="middle">GIDL 누설 억제</text>
  <text x="445" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">상부 Nitride 캡핑 절연</text>
  <text x="445" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">Gate-Drain 전계 집중 차단</text>
  <text x="445" y="165" fill="#f59e0b" font-size="12" text-anchor="middle">밴드 간 터널링(BTBT) 원천 봉쇄</text>

  <path d="M 575 120 L 615 120" stroke="#10b981" stroke-width="3"/>

  <rect x="630" y="45" width="130" height="150" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="695" y="80" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">리프레시 사수</text>
  <text x="695" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">Off-누설 극소화</text>
  <text x="695" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">데이터 보존(tRET)</text>
  <text x="695" y="165" fill="#10b981" font-size="12" text-anchor="middle">초격차 DRAM 양산</text>
</svg>"""
        },
        {
            "id": "t_10",
            "category": "tech",
            "category_label": "반도체 소자·공정 실전 핵심",
            "number": 10,
            "title": "High-k 유전체 도입 시 물리적 두께(t_phys)와 등가산화막두께(EOT) 디커플링 메커니즘",
            "core_keyword": ["EOT 수식 유도", "물리적 두께 vs 정전 용량", "직접 터널링 누설 10,000배 억제"],
            "speech_1m30s": (
                "High-k 유전체 도입의 본질은 '터널링을 막는 물리적 두께(t_phys)'와 '게이트 정전 제어력을 결정하는 전기적 두께(EOT)'를 분리하여 독립 제어하는 디커플링에 있습니다. "
                "종래 SiO2 유전체는 유전율이 3.9에 불과하여, 정전 용량을 늘리려면 물리적 두께를 1nm 이하로 깎아야 했고, 이는 원자 4~5개 층에 불과해 직접 터널링 누설 전류가 폭발하는 한계에 봉착했습니다. "
                "반면 유전율이 20 이상인 HfO2와 같은 High-k 물질을 적용하면, EOT 공식 't_phys 곱하기 (k_SiO2 / k_high-k)'에 의해 물리적 두께를 5nm 이상으로 두껍게 유지할 수 있습니다. "
                "물리적 두께가 두꺼우므로 양자역학적 파동 투과 확률이 지수함수적으로 감소하여 터널링 누설 전류를 1만 배 이상 차단할 수 있습니다. "
                "동시에 전기적으로는 1nm 미만의 얇은 SiO2를 쓴 것과 동일한 높은 커패시턴스를 확보하여 온전류 구동력을 완벽히 살려냅니다. "
                "이 디커플링 메커니즘을 토대로 초미세 선단 노드의 저전력 고성능 소자를 설계하겠습니다."
            ),
            "deep_lecture": {
                "background": "트랜지스터의 구동 전류($I_{on} \\propto C_{ox}$)를 높이려면 산화막 용량($C_{ox} = \\frac{\\kappa \\epsilon_0}{t_{phys}}$)을 키워야 합니다. High-k는 두께($t$)와 유전율($\\kappa$)의 관계를 혁신한 소자 물리의 정점입니다.",
                "action_principle": "1. EOT의 정의: $EOT = t_{phys} \\times \\left(\\frac{\\kappa_{SiO_2}}{\\kappa_{high-k}}\\right) = t_{phys} \\times \\left(\\frac{3.9}{\\kappa_{high-k}}\\right)$\n2. 디커플링 메커니즘: $\\kappa_{high-k} \\approx 20\\sim 25$ 적용 시, $EOT = 0.8\\text{ nm}$를 달성하면서도 실제 물리적 두께는 $t_{phys} = 4\\sim 5\\text{ nm}$ 확보\n3. 터널링 차단 효과: 직류 터널링 전류 밀도 $J_{tunnel} \\propto \\exp(-2 \\sqrt{2m^* \\Phi_B} \\cdot t_{phys} / \\hbar)$에 의해 물리적 두께가 지수함수($\\exp$) 인자로 작용하여 누설 전류 수만 배 감소\n4. 계면 IL(Interfacial Layer): Si와의 열역학적 안정성 및 이동도 저하 방지를 위해 $0.5\\text{ nm}$ 수준의 초박형 $SiO_x$ IL 필수",
                "core_points": [
                    "EOT와 $t_{phys}$의 수학적 상관관계 및 유전율($\\kappa$) 비례식 명시",
                    "터널링 전류의 물리적 두께 지수 의존성($\\exp(-t_{phys})$) 설명",
                    "구동 전류(Capacitance)와 누설 전류(Leakage)의 트레이드오프 극복 원리"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="40" y="45" width="220" height="150" fill="#1e293b" stroke="#ef4444" stroke-width="2" rx="8"/>
  <text x="150" y="80" fill="#ef4444" font-size="15" font-weight="bold" text-anchor="middle">SiO2의 물리 한계</text>
  <text x="150" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">k = 3.9 저유전율</text>
  <text x="150" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">두께 &lt; 1.2nm 극한 박막화</text>
  <text x="150" y="165" fill="#f87171" font-size="12" text-anchor="middle">직접 터널링 누설 폭발</text>

  <path d="M 275 120 L 315 120" stroke="#38bdf8" stroke-width="3"/>

  <rect x="330" y="45" width="230" height="150" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="445" y="80" fill="#38bdf8" font-size="15" font-weight="bold" text-anchor="middle">High-k (HfO2) 도입</text>
  <text x="445" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">k = 20 ~ 25 고유전율</text>
  <text x="445" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">물리 두께 t_phys = 5nm 확보</text>
  <text x="445" y="165" fill="#38bdf8" font-size="12" text-anchor="middle">EOT = 0.8nm 초고정전용량</text>

  <path d="M 575 120 L 615 120" stroke="#10b981" stroke-width="3"/>

  <rect x="630" y="45" width="130" height="150" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="695" y="80" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">디커플링 성과</text>
  <text x="695" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">누설 10,000배 ↓</text>
  <text x="695" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">Ion 구동력 유지</text>
  <text x="695" y="165" fill="#10b981" font-size="12" text-anchor="middle">저전력 고성능</text>
</svg>"""
        }
    ]
    return topics
