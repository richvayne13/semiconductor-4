# -*- coding: utf-8 -*-
"""
직무 질문 16~20문항 데이터 생성 스크립트 (t_part4.py)
"""

def get_tech_topics_part4():
    topics = [
        {
            "id": "t_16",
            "category": "tech",
            "category_label": "반도체 소자·공정 실전 핵심",
            "number": 16,
            "title": "3D NAND 고단화에 따른 HARC(High Aspect Ratio Contact) 식각에서의 보잉(Bowing) 및 틸트(Tilt) 불량 제어 기술",
            "core_keyword": ["HARC 종횡비 70:1+", "보잉(Bowing) & 틸트(Tilt)", "극저온 식각(Cryogenic) & 펄스 RF"],
            "speech_1m30s": (
                "300단 이상 초고단 3D NAND의 채널 홀 식각은 종횡비(A/R)가 70대 1을 초과하는 극한의 HARC 공정으로, '보잉(Bowing)'과 '틸트(Tilt)' 제어가 수율의 성패를 가릅니다. "
                "보잉은 홀 입구 마스크의 하전(Charging)이나 에지 산란으로 인해 굴절된 이온이 홀 중간부 측벽을 집중 타격하여 항아리처럼 배가 부르는 불량이며, 틸트는 플라즈마 쉬스 전계의 비대칭으로 인해 바닥으로 갈수록 홀 축이 휘어 인접 채널과 단락되는 결함입니다. "
                "이를 해결하기 위해 첫째, 영하 60도 이하의 '극저온 식각(Cryogenic Etching)' 기술을 도입합니다. 저온에서 측벽 화학 반응을 동결시키고 플루오로카본 보호막을 자발적으로 흡착시켜 보잉을 원천 차단합니다. "
                "둘째, 소스 파워와 바이어스 전압을 수십 kHz 주기로 온/오프하는 '펄스드 RF(Pulsed RF)'를 적용하여 마스크에 축적된 전하를 중화하고 이온의 직진성을 극대화합니다. "
                "하드웨어와 플라즈마 물성의 복합 제어로 초고단 수직 채널을 한 치의 흔들림 없이 수직으로 관통시키겠습니다."
            ),
            "deep_lecture": {
                "background": "3D NAND는 적층 수가 증가함에 따라 채널 홀의 깊이가 수 ㎛에 달합니다. 상단부터 하단까지 균일한 임계 선폭(CD)을 유지하지 못하면 셀 트랜지스터 특성 산포가 폭증하여 동작이 불가능해집니다.",
                "action_principle": "1. 불량 메커니즘:\n   - Bowing: 마스크 패싯(Faceting) 및 양전하 트랩 ➔ 이온 반사 각도 산란 ➔ 넥(Neck) 하부 측벽 측면 식각\n   - Tilt: 웨이퍼 에지 부근 플라즈마 쉬스(Sheath) 휨 현상 ➔ 이온 궤적 경사 입사 ➔ 바닥 패드 미스얼라인\n2. 극저온(Cryogenic) 혁신: $-60^\\circ\\text{C} \\sim -80^\\circ\\text{C}$ 냉각 ➔ 자발적 화학 식각률 억제, 폴리머 응축 증착 ➔ 이방성 비약적 향상\n3. 펄스드 RF 제어: RF-On 시 고에너지 이온 주입, RF-Off 시 전자 침투를 통한 양전하 중화(Discharging) ➔ 왜곡 없는 수직 가속 실현\n4. 멀티 티어(Multi-tier) 본딩: 단일 에칭 한계 극복을 위해 150단씩 나누어 뚫고 이어 붙이는 COP/하이브리드 공정 융합",
                "core_points": [
                    "HARC 식각의 두 대 불량인 보잉(항아리 변형)과 틸트(축 기울어짐) 원인 분해",
                    "극저온 식각(측벽 반응 동결)의 물리 화학적 메커니즘 설명",
                    "펄스드 RF(하전 중화 및 이온 직진성 확보)의 공정 솔루션 연계"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="40" y="45" width="220" height="150" fill="#1e293b" stroke="#ef4444" stroke-width="2" rx="8"/>
  <text x="150" y="80" fill="#ef4444" font-size="15" font-weight="bold" text-anchor="middle">보잉 (Bowing) 불량</text>
  <text x="150" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">마스크 하전 ➔ 이온 산란</text>
  <text x="150" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">홀 중간부 배부름 현상</text>
  <text x="150" y="165" fill="#f87171" font-size="12" text-anchor="middle">인접 홀 절연 파괴 위험</text>

  <path d="M 275 120 L 315 120" stroke="#f59e0b" stroke-width="3"/>

  <rect x="330" y="45" width="230" height="150" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="445" y="80" fill="#f59e0b" font-size="15" font-weight="bold" text-anchor="middle">틸트 (Tilt) 불량</text>
  <text x="445" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">쉬스 전계 비대칭 왜곡</text>
  <text x="445" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">바닥 관통축 경사 발생</text>
  <text x="445" y="165" fill="#f59e0b" font-size="12" text-anchor="middle">하부 패드 미스얼라인 단락</text>

  <path d="M 575 120 L 615 120" stroke="#10b981" stroke-width="3"/>

  <rect x="630" y="45" width="130" height="150" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="695" y="80" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">공정 대책</text>
  <text x="695" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">극저온(-60℃)</text>
  <text x="695" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">펄스드 RF</text>
  <text x="695" y="165" fill="#10b981" font-size="12" text-anchor="middle">수직 관통</text>
</svg>"""
        },
        {
            "id": "t_17",
            "category": "tech",
            "category_label": "반도체 소자·공정 실전 핵심",
            "number": 17,
            "title": "박막 증착 공정에서 CVD와 ALD의 표면 반응 율속 단계(Rate-Limiting Step) 차이와 Step Coverage 메커니즘",
            "core_keyword": ["CVD 물질전달/표면반응 율속", "ALD 자기제한적 반응(Self-Limiting)", "100% 단차 피복성(Step Coverage)"],
            "speech_1m30s": (
                "CVD와 ALD의 박막 품질 격차는 전구체 주입 방식과 '율속 단계(Rate-Limiting Step)'의 물리적 차이에서 비롯됩니다. "
                "CVD는 다중 반응 가스를 챔버에 동시에 지속 주입하므로 고온에서는 가스 공급 속도가 지배하는 물질전달 율속, 저온에서는 화학 결합 속도가 지배하는 표면반응 율속으로 동작합니다. "
                "깊은 트렌치 내부에서는 기체 확산 속도가 소모 속도를 따라가지 못해 입구만 두껍게 증착되고 내부는 얇아지는 오버행과 보이드가 발생하여 Step Coverage가 60~80%에 머뭅니다. "
                "반면 ALD는 전구체 주입, 퍼지, 반응 가스 주입, 퍼지의 4단계를 시간적으로 엄격히 격리합니다. "
                "단원자층 흡착이 끝나면 반응 사이트가 포화되어 더 이상 반응하지 않는 '자기제한적 표면 반응(Self-Limiting)'에 의해 100% 표면반응 율속으로만 진행됩니다. "
                "충분한 노출 시간만 주어지면 가스가 트렌치 바닥까지 균일하게 침투 흡착하므로, 종횡비 100대 1의 구조에서도 100%에 달하는 완벽한 Step Coverage를 구현합니다."
            ),
            "deep_lecture": {
                "background": "DRAM 커패시터, HKMG 게이트 절연막, 3D NAND 제어 게이트 등 초미세 3차원 패턴에서 균일한 두께 증착(Conformality)은 정전 용량과 항타 전압을 결정하는 핵심 공정 척도입니다.",
                "action_principle": "1. CVD 속도론: 아레니우스 곡선(Arrhenius Plot) 상에서 저온(표면 반응 율속, $E_a$ 큼) ➔ 고온(물질 전달 율속, 기체 경계층 확산 지배). 패턴 종횡비 증가 시 물질 공급 부족으로 입구 막힘(Clogging) 유발\n2. ALD 사이클 메커니즘:\n   - Pulse 1: 화학 흡착(Chemisorption) ➔ 표면 포화 시 반응 정지 (Self-Limiting)\n   - Purge 1: 물리 흡착된 과잉 전구체 배기\n   - Pulse 2: 반응물(산화제/환원제) 주입 ➔ 단원자층 박막 합성\n   - Purge 2: 부산물 배기\n3. Step Coverage 공식: $SC = \\frac{t_{bottom}}{t_{top}} \\times 100\\%$. ALD는 공급 제약이 없으므로 $SC \\approx 100\\%$\n4. 트레이드오프: ALD의 단점인 느린 증착 속도($\\sim 1\\text{ Å/cycle}$)는 공간 분할 ALD(Spatial ALD)로 극복",
                "core_points": [
                    "CVD의 연속 주입 및 물질전달/표면반응 율속 영역 구분",
                    "ALD의 4단계 시분할 주입 및 '자기제한적 반응(Self-Limiting)' 본질 설명",
                    "초고종횡비 구조에서 Step Coverage 100% 달성 메커니즘"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="40" y="45" width="220" height="150" fill="#1e293b" stroke="#ef4444" stroke-width="2" rx="8"/>
  <text x="150" y="80" fill="#ef4444" font-size="15" font-weight="bold" text-anchor="middle">CVD 연속 반응</text>
  <text x="150" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">가스 동시 지속 투입</text>
  <text x="150" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">트렌치 입구 확산 병목</text>
  <text x="150" y="165" fill="#f87171" font-size="12" text-anchor="middle">Step Coverage 60~80%</text>

  <path d="M 275 120 L 315 120" stroke="#38bdf8" stroke-width="3"/>

  <rect x="330" y="45" width="230" height="150" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="445" y="80" fill="#38bdf8" font-size="15" font-weight="bold" text-anchor="middle">ALD 자기제한 반응</text>
  <text x="445" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">4단계 시분할 펄스·퍼지</text>
  <text x="445" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">단원자층 포화 시 반응 정지</text>
  <text x="445" y="165" fill="#38bdf8" font-size="12" text-anchor="middle">Self-Limiting 메커니즘</text>

  <path d="M 575 120 L 615 120" stroke="#10b981" stroke-width="3"/>

  <rect x="630" y="45" width="130" height="150" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="695" y="80" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">완벽한 피복</text>
  <text x="695" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">SC ≈ 100%</text>
  <text x="695" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">보이드 제로</text>
  <text x="695" y="165" fill="#10b981" font-size="12" text-anchor="middle">초박막 균일성</text>
</svg>"""
        },
        {
            "id": "t_18",
            "category": "tech",
            "category_label": "반도체 소자·공정 실전 핵심",
            "number": 18,
            "title": "화학기계적 연마(CMP) 공정에서 디싱(Dishing)과 에로전(Erosion) 발생 원인 및 억제 슬러리 설계",
            "core_keyword": ["패드 벤딩에 의한 디싱(Dishing)", "패턴 밀도차에 의한 에로전(Erosion)", "고선택비 슬러리 & BTA 억제제"],
            "speech_1m30s": (
                "구리 배선 CMP 공정의 대표적 불량인 '디싱(Dishing)'과 '에로전(Erosion)'은 서로 다른 영역에서 발생하지만 모두 국소적 과연마로 인해 단차가 생기는 결함입니다. "
                "디싱은 폭이 넓은 구리 배선 트렌치 중앙부가 주변 절연막보다 오목하게 파이는 현상입니다. 구리의 경도가 절연막보다 낮고 탄성 연마 패드가 트렌치 내부로 휘어져 들어가(Pad Bending) 구리를 긁어내기 때문입니다. "
                "반면 에로전은 좁은 배선이 빽빽하게 밀집된 고밀도 어레이 영역에서 구리와 산화막 절연막이 함께 깎여나가 필드보다 낮아지는 현상입니다. 패턴 밀도 차이로 연마 압력이 국소 집중되어 발생합니다. "
                "이를 제어하기 위해 첫째, 경도가 높은 하드 패드를 사용하여 패드 휨을 억제합니다. 둘째, 정적 에칭을 막는 BTA 보호막 형성제와 구리 대비 배리어 메탈 연마 선택비가 제어된 '고선택비 슬러리'를 사용합니다. "
                "여기에 질화막 연마 정지층을 조합하여 수 나노미터 수준의 원자급 평탄도를 사수하겠습니다."
            ),
            "deep_lecture": {
                "background": "다층 금속 배선(BEOL)에서 CMP 후 국소 단차가 발생하면 금속 두께 감소로 인한 저항(RC) 산포 폭증과 후속 포토 공정의 초점 심도(DOF) 불량이 발생합니다.",
                "action_principle": "1. 불량 메커니즘 비교:\n   - Dishing: 광역 배선(Wide Line) 중앙부 오목 파임 ➔ 패드 탄성 침하(Pad Bending) 및 화학적 정적 용해 지배\n   - Erosion: 고밀도 어레이(Dense Pattern)의 절연막 손실 ➔ 유효 압력 집중($P_{eff} \\propto 1/\\text{Area}$)에 의한 과연마\n2. 프레스턴 방정식(Preston's Equation): $MRR = k_p \\cdot P \\cdot V$ (재료 제거율은 압력과 속도에 비례)\n3. 화학적 억제 슬러리 설계:\n   - BTA(Benzotriazole): 구리 표면에 불용성 $Cu(I)-BTA$ 보호 피막 형성 ➔ 오목한 부위의 정적 부식 방어\n   - 킬레이트제 및 pH 최적화: 돌출 부위의 패드 기계적 마찰 시에만 보호막을 벗겨내어 선택 연마\n4. 하드웨어 대책: 고경도 폴리우레탄 패드 및 $Si_3N_4$ 연마 정지층(Stop Layer)",
                "core_points": [
                    "디싱(단일 광폭 배선 파임)과 에로전(밀집 패턴 전체 침식) 명확한 구분",
                    "패드 탄성 변형(Pad Bending)과 국소 압력 집중 원리 설명",
                    "BTA 부식 억제제와 하드 패드를 활용한 정밀 슬러리/장비 솔루션 제시"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="40" y="45" width="220" height="150" fill="#1e293b" stroke="#ef4444" stroke-width="2" rx="8"/>
  <text x="150" y="80" fill="#ef4444" font-size="15" font-weight="bold" text-anchor="middle">디싱 (Dishing)</text>
  <text x="150" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">광폭 배선 중앙부 침하</text>
  <text x="150" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">패드 벤딩(탄성 휨) 원인</text>
  <text x="150" y="165" fill="#f87171" font-size="12" text-anchor="middle">배선 저항(R) 급증</text>

  <path d="M 275 120 L 315 120" stroke="#f59e0b" stroke-width="3"/>

  <rect x="330" y="45" width="230" height="150" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="445" y="80" fill="#f59e0b" font-size="15" font-weight="bold" text-anchor="middle">에로전 (Erosion)</text>
  <text x="445" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">밀집 패턴 국소 압력 집중</text>
  <text x="445" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">배선 + 절연막 동반 손실</text>
  <text x="445" y="165" fill="#f59e0b" font-size="12" text-anchor="middle">광역 평탄도 붕괴</text>

  <path d="M 575 120 L 615 120" stroke="#10b981" stroke-width="3"/>

  <rect x="630" y="45" width="130" height="150" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="695" y="80" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">슬러리 솔루션</text>
  <text x="695" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">BTA 억제막</text>
  <text x="695" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">고경도 패드</text>
  <text x="695" y="165" fill="#10b981" font-size="12" text-anchor="middle">원자급 평탄화</text>
</svg>"""
        },
        {
            "id": "t_19",
            "category": "tech",
            "category_label": "반도체 소자·공정 실전 핵심",
            "number": 19,
            "title": "금속 배선 신뢰성을 좌우하는 일렉트로마이그레이션(Electromigration, Black's Equation)과 보이드 형성 억제법",
            "core_keyword": ["전자풍(Electron Wind) 운동량 전달", "Black's Equation (MTTF)", "보이드/힐록 억제 & 코발트 캡핑"],
            "speech_1m30s": (
                "일렉트로마이그레이션(EM)은 고밀도 전류가 흐를 때 전도 전자의 흐름인 '전자풍(Electron Wind)'이 금속 원자와 운동량을 교환하여 원자를 물리적으로 밀어내는 신뢰성 파괴 현상입니다. "
                "원자가 빠져나간 음극(Cathode)에는 공공(Vacancy)이 뭉쳐 보이드(Void)가 생기며 단선 오픈 불량을 일으키고, 원자가 쌓인 양극(Anode)에는 힐록(Hillock) 돌기가 솟아올라 인접 배선과 쇼트를 냅니다. "
                "배선의 평균 수명은 블랙의 방정식(Black's Equation)에 따르며, 전류 밀도(J)의 제곱에 반비례하고 온도에 지수함수적으로 급감합니다. "
                "구리 배선에서 원자 이동의 가장 취약한 고속도로는 결정립 내부가 아니라 상부 절연막과의 계면(Interface)입니다. "
                "이를 방어하기 위해 구리 표면에 코발트(Co)나 루테늄(Ru) 같은 고융점 금속 캡핑층을 무전해도금하여 계면 결합력을 극대화합니다. "
                "또한 배선 결정립을 대나무 마디 형태의 뱀부 구조(Bamboo Structure)로 성장시켜 결정립계 확산 경로를 차단함으로써 10년 이상의 수명을 보증합니다."
            ),
            "deep_lecture": {
                "background": "선단 공정으로 갈수록 배선 단면적이 줄어들어 구리 배선 내부의 실효 전류 밀도가 $10^6\\text{ A/cm}^2$를 상회합니다. EM은 반도체 칩의 장기 수명(Long-term Reliability)을 결정짓는 핵심 물리 한계입니다.",
                "action_principle": "1. 물리 메커니즘: 원자에 작용하는 총 힘 $F_{total} = F_{direct} + F_{wind} = q(Z_{el} + Z_{wd})E$. 고밀도 전자의 산란 충돌력(Electron wind force)이 직접 정전인력을 압도하여 원자를 양극으로 이동시킴\n2. 블랙 방정식(Black's Equation): $MTTF = \\frac{A}{J^n} \\exp\\left(\\frac{E_a}{kT}\\right)$ ($n \\approx 2$, $E_a$: 확산 활성화 에너지)\n3. 확산 경로 취약 순위: 계면(Interface, $E_a \\approx 0.8\\sim 1.0\\text{ eV}$) ➔ 결정립계(Grain boundary, $\\sim 1.2\\text{ eV}$) ➔ 벌크 결정 격자(Bulk lattice, $\\sim 2.3\\text{ eV}$)\n4. 억제 솔루션: Cu 상단에 CoWP 또는 ALD Co/Ru 캡핑층 증착 ➔ 계면 확산 활성화 에너지 2배 상승, 배선 폭 스케일링을 통한 Bamboo 구조 유도",
                "core_points": [
                    "전자풍(Electron Wind)과 원자 운동량 전달 메커니즘 규명",
                    "블랙 방정식(Black's Eq)을 통한 전류 밀도($J^2$) 및 온도($T$) 의존성 제시",
                    "상부 Co/Ru 금속 캡핑과 뱀부 구조(Bamboo Structure)를 통한 수명 개선책"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="40" y="45" width="220" height="150" fill="#1e293b" stroke="#ef4444" stroke-width="2" rx="8"/>
  <text x="150" y="80" fill="#ef4444" font-size="15" font-weight="bold" text-anchor="middle">전자풍 (Electron Wind)</text>
  <text x="150" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">고전류 밀도 전자 충돌</text>
  <text x="150" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">금속 원자 양극 방향 이동</text>
  <text x="150" y="165" fill="#f87171" font-size="12" text-anchor="middle">음극 보이드 / 양극 힐록</text>

  <path d="M 275 120 L 315 120" stroke="#f59e0b" stroke-width="3"/>

  <rect x="330" y="45" width="230" height="150" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="445" y="80" fill="#f59e0b" font-size="15" font-weight="bold" text-anchor="middle">블랙 방정식 (Black Eq)</text>
  <text x="445" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">MTTF = (A / J^2) exp(Ea/kT)</text>
  <text x="445" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">온도·전류밀도 극도로 민감</text>
  <text x="445" y="165" fill="#f59e0b" font-size="12" text-anchor="middle">상부 계면이 주 확산 경로</text>

  <path d="M 575 120 L 615 120" stroke="#10b981" stroke-width="3"/>

  <rect x="630" y="45" width="130" height="150" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="695" y="80" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">신뢰성 확보</text>
  <text x="695" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">Co/Ru 캡핑층</text>
  <text x="695" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">뱀부(Bamboo) 격자</text>
  <text x="695" y="165" fill="#10b981" font-size="12" text-anchor="middle">10년 수명 사수</text>
</svg>"""
        },
        {
            "id": "t_20",
            "category": "tech",
            "category_label": "반도체 소자·공정 실전 핵심",
            "number": 17,
            "number": 20,
            "title": "차세대 패키징 하이브리드 본딩(Cu-Cu Direct Bonding)의 표면 활성화 및 CMP 화학기계 연마 메커니즘",
            "core_keyword": ["솔더리스 Cu-Cu 직접 접합", "나노미터 Cu 리세스 CMP", "열팽창 계수(CTE) 기반 입계 성장"],
            "speech_1m30s": (
                "차세대 초고밀도 3D 패키징의 정점인 하이브리드 본딩은 중간 솔더 범프를 완전히 없애고 'Cu 금속 패드'와 'SiO2 절연막'을 원자 스케일로 동시 접합하는 기술입니다. "
                "기존 마이크로 범프의 10㎛ 피치 한계를 단 1㎛ 이하로 극초미세화하여 I/O 밀도를 100배 이상 폭증시킵니다. "
                "이 공정의 성공을 좌우하는 열쇠는 '원자급 CMP 리세스 제어'와 '플라즈마 표면 활성화'입니다. "
                "먼저 CMP 공정을 통해 절연막 표면보다 Cu 패드가 단 수 나노미터(nm) 정도 미세하게 낮게 파이도록 리세스(Recess)를 정밀 제어합니다. "
                "이후 질소 플라즈마로 표면을 활성화하여 친수성 실라놀(-OH)기를 형성하고, 상온에서 두 웨이퍼를 맞닿게 하여 유전막 간의 수소 결합으로 1차 접합을 이룹니다. "
                "이어 350도 이하의 후속 열처리 시 구리의 열팽창계수가 산화막보다 훨씬 큰 점을 이용합니다. 리세스되었던 구리가 팽창하여 빈틈없이 맞물리며 계면에서 입계 확산(Grain Growth)을 일으켜 완전한 금속 결합을 이룹니다. "
                "HBM4와 차세대 3D 패키징의 물리적 한계를 돌파하는 핵심 솔루션입니다."
            ),
            "deep_lecture": {
                "background": "HBM4 16단/20단 고적층 및 3D 로직-메모리 이종 접합에서 칩 두께를 줄이고 범프 저항/인덕턴스를 제로화하기 위해 TSMC(SoIC), SK하이닉스, 삼성전자가 사활을 걸고 양산 라인에 도입 중인 핵심 기술입니다.",
                "action_principle": "1. 범프리스(Bumpless) 패러다임: 마이크로 범프 대비 피치($< 1\\mu\\text{m}$), 저항 90% 이상 절감, 기생 인덕턴스 제거\n2. CMP 정밀 제어 난제: Cu 패드가 절연막보다 튀어나오면(Protrusion) 유전체 접합이 실패하고, 너무 깊게 파이면 Cu 간 접촉이 불가능 ➔ $1\\sim 5\\text{ nm}$ Cu Dishing/Recess 창(Process Window) 유지\n3. 표면 화학 활성화: $N_2/Ar$ 플라즈마 처리 ➔ 결합 파괴 및 표면 친수화 ➔ 상온 접합 시 $\\text{Si-OH} + \\text{HO-Si} \\to \\text{Si-O-Si} + \\text{H}_2\\text{O}$ 탈수 축합 반응 완결\n4. Cu 상호 확산(Interdiffusion): CTE 차이($\\alpha_{Cu} \\approx 17\\text{ ppm/K}$ vs $\\alpha_{SiO_2} \\approx 0.5\\text{ ppm/K}$)에 의해 열팽창 압력이 발생하여 계면 보이드 소멸 및 결정립 성장(Grain Growth)",
                "core_points": [
                    "솔더 범프 없는 Cu-Cu 및 유전체 동시 접합의 원리 및 피치 1㎛ 이하 혁신",
                    "CMP 공정에서 수 nm 급 Cu 리세스(Recess) 제어의 절대적 중요성",
                    "열팽창계수(CTE) 차이를 이용한 후속 어닐링 금속 입계 확산 메커니즘"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="40" y="45" width="220" height="150" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="150" y="80" fill="#38bdf8" font-size="15" font-weight="bold" text-anchor="middle">초정밀 CMP 리세스</text>
  <text x="150" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">Cu 패드 1~5nm 미세 리세스</text>
  <text x="150" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">표면 거칠기(Rq) &lt; 0.5nm</text>
  <text x="150" y="165" fill="#38bdf8" font-size="12" text-anchor="middle">원자급 고평탄도 유지</text>

  <path d="M 275 120 L 315 120" stroke="#f59e0b" stroke-width="3"/>

  <rect x="330" y="45" width="230" height="150" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="445" y="80" fill="#f59e0b" font-size="15" font-weight="bold" text-anchor="middle">상온 유전막 가접합</text>
  <text x="445" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">플라즈마 친수성(-OH) 형성</text>
  <text x="445" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">SiO2 - SiO2 수소 결합</text>
  <text x="445" y="165" fill="#f59e0b" font-size="12" text-anchor="middle">탈수 축합 공유 결합</text>

  <path d="M 575 120 L 615 120" stroke="#10b981" stroke-width="3"/>

  <rect x="630" y="45" width="130" height="150" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="695" y="80" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">열팽창 결합</text>
  <text x="695" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">Cu 열팽창(CTE)</text>
  <text x="695" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">입계 확산 완성</text>
  <text x="695" y="165" fill="#10b981" font-size="12" text-anchor="middle">HBM4 16단+</text>
</svg>"""
        }
    ]
    return topics
