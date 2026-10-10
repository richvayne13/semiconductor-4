# -*- coding: utf-8 -*-
"""
인성 질문 11~15문항 데이터 생성 스크립트 (p_part3.py)
"""

def get_personality_topics_part3():
    topics = [
        {
            "id": "p_11",
            "category": "personality",
            "category_label": "인성·협업·조직 가치",
            "number": 11,
            "title": "단순 반복 업무(모니터링, 일상 점검)에 대한 마인드셋과 이를 개선·자동화한 경험",
            "core_keyword": ["기초 루틴의 가치", "잠재 리스크 감지", "파이썬 자동화 스크립트"],
            "speech_1m30s": (
                "단순 반복 업무는 공정 안정성을 지키는 가장 견고한 방어선이자, 시스템의 미세 이상을 가장 먼저 감지할 수 있는 핵심 기회라고 생각합니다. "
                "학부 연구실에서 매일 아침 10개 장비의 진공도, 가스 유량, 온도 로그 50여 개를 수기로 기록하고 이상 여부를 체크하는 루틴이 있었습니다. "
                "반복적이고 지루한 작업일 수 있었지만, 저는 이 데이터가 장비 예방정비(PM) 시점을 예측하는 골든 타임 지표임을 인식하고 1년간 단 하루도 누락 없이 기록했습니다. "
                "나아가 매일 40분씩 소요되는 수기 취합의 비효율을 개선하기 위해, 장비 통신 로그를 자동으로 파싱하여 이상치가 발생하면 메신저로 즉시 알림을 주는 자동화 파이프라인을 구축했습니다. "
                "그 결과 점검 시간을 5분으로 단축하면서도 펌프 진공 누설 이상을 3주 앞당겨 사전 예방할 수 있었습니다. "
                "기본적인 일상 루틴을 충실히 수행하면서도 기술적 자동화로 업무 생산성을 높이는 엔지니어가 되겠습니다."
            ),
            "deep_lecture": {
                "background": "반도체 FAB 엔지니어는 24시간 라인 모니터링, FDC 센서 확인, 일상 SPC 차트 점검 등 단순 반복성 모니터링을 끊임없이 수행합니다. 반복 업무를 소홀히 하지 않는 성실성과 비효율을 자동화로 개선하는 혁신 의지를 동시에 평가합니다.",
                "action_principle": "1. 반복 업무의 가치 재정의 (단순 작업이 아닌 품질과 안전의 마지노선)\n2. 성실한 완수 태도 증명 (결측치 없는 철저한 이행)\n3. 주도적 자동화 솔루션 개발 (Python/스크립트 기반 파이프라인)\n4. 정량적 성과 (시간 단축 + 설비 사고 예방)",
                "core_points": [
                    "단순 업무를 경시하지 않고 '골든 타임 지표'로 해석하는 성숙한 마인드",
                    "수작업 낭비를 개선하는 자발적 엔지니어링 역량 강조",
                    "SK하이닉스 양산 현장의 FDC(Fault Detection and Classification) 및 이상 감지 마인드셋 연결"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="40" y="45" width="210" height="150" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="145" y="85" fill="#38bdf8" font-size="15" font-weight="bold" text-anchor="middle">1. 일상 루틴의 가치</text>
  <text x="145" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">50여 개 파라미터 점검</text>
  <text x="145" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">품질·안전 1차 방어선</text>

  <path d="M 265 120 L 305 120" stroke="#f59e0b" stroke-width="3"/>

  <rect x="320" y="45" width="210" height="150" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="425" y="85" fill="#f59e0b" font-size="15" font-weight="bold" text-anchor="middle">2. 자동화 파이프라인</text>
  <text x="425" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">로그 자동 파싱 알고리즘</text>
  <text x="425" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">실시간 임계치 알람 연동</text>

  <path d="M 545 120 L 585 120" stroke="#10b981" stroke-width="3"/>

  <rect x="600" y="45" width="160" height="150" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="680" y="85" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">3. 정량 성과</text>
  <text x="680" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">40분 ➔ 5분 단축</text>
  <text x="680" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">진공 누설 사전 차단</text>
</svg>"""
        },
        {
            "id": "p_12",
            "category": "personality",
            "category_label": "인성·협업·조직 가치",
            "number": 12,
            "title": "극심한 업무 압박과 스트레스 상황 속에서 멘탈과 건강을 관리하는 본인만의 루틴",
            "core_keyword": ["우선순위 매트릭스", "감정-문제 분리", "주기적 유산소 운동"],
            "speech_1m30s": (
                "극심한 압박 상황에서는 감정과 문제를 즉시 분리하고, 통제 가능한 일에 집중하는 '우선순위 구조화 루틴'과 '신체 리셋 루틴'으로 멘탈을 관리합니다. "
                "연구 마감과 학술대회 발표, 장비 트러블이 한 주에 동시 발생하여 극도의 스트레스를 겪은 적이 있습니다. "
                "그때 저는 패닉에 빠지는 대신 A4 용지에 통제할 수 있는 일과 통제할 수 없는 일을 분류하고, 중요도-시급성 매트릭스로 당일 해결할 3가지 핵심 과제에만 몰입했습니다. "
                "더불어 퇴근 후 30분간 야외 러닝을 통해 엔도르핀을 활성화하고 뇌의 과부하를 비워내는 신체적 리셋을 규칙화했습니다. "
                "이를 통해 3주간의 격무 속에서도 단 한 번의 번아웃이나 건강 문제 없이 모든 프로젝트를 최고 성적으로 완수할 수 있었습니다. "
                "SK하이닉스의 촌각을 다투는 양산 현장에서도 냉철한 문제 해결력과 건강한 체력으로 흔들림 없이 성과를 창출하겠습니다."
            ),
            "deep_lecture": {
                "background": "반도체 팹과 연구소는 24시간 가동되며 수율 변동, 라인 정지 위험 등 상시적인 스트레스와 데드라인 압박이 존재합니다. 지속 가능한 고성과를 창출할 수 있는 회복탄력성(Resilience)과 자기관리 능력이 필수적입니다.",
                "action_principle": "1. 감정적 대응 지양 및 통제 가능 영역으로의 프레임 전환\n2. 우선순위 매트릭스(Eisenhower Matrix) 기반 과업 구조화\n3. 지속 가능한 신체 리셋 루틴(러닝, 수면 리듬 등) 제시\n4. 장기적 성과 창출을 위한 체력 및 안정성 증명",
                "core_points": [
                    "‘스트레스를 안 받는다’는 비현실적 답변 대신 체계적인 해소 메커니즘 제시",
                    "문제 중심 대처(Problem-focused coping)와 정서 중심 대처의 조화",
                    "체력과 멘탈 관리가 업무 지속성에 미치는 영향 강조"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="40" y="45" width="210" height="150" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="145" y="85" fill="#38bdf8" font-size="15" font-weight="bold" text-anchor="middle">1. 인지적 분리</text>
  <text x="145" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">감정 vs 팩트 분리</text>
  <text x="145" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">통제 가능 변수 집중</text>

  <path d="M 265 120 L 305 120" stroke="#f59e0b" stroke-width="3"/>

  <rect x="320" y="45" width="210" height="150" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="425" y="85" fill="#f59e0b" font-size="15" font-weight="bold" text-anchor="middle">2. 우선순위 매트릭스</text>
  <text x="425" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">Eisenhower 4분면 분류</text>
  <text x="425" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">Top 3 과제 몰입 해결</text>

  <path d="M 545 120 L 585 120" stroke="#10b981" stroke-width="3"/>

  <rect x="600" y="45" width="160" height="150" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="680" y="85" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">3. 신체 리셋</text>
  <text x="680" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">30분 야외 러닝</text>
  <text x="680" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">번아웃 제로 지속성</text>
</svg>"""
        },
        {
            "id": "p_13",
            "category": "personality",
            "category_label": "인성·협업·조직 가치",
            "number": 13,
            "title": "낯선 기술 도메인이나 새로운 공정 장비를 단기간에 습득해야 할 때의 학습 전략",
            "core_keyword": ["Top-Down 구조화", "매뉴얼·논문 크로스체크", "전문가 인터뷰"],
            "speech_1m30s": (
                "새로운 도메인을 단기간에 습득할 때는 '전체 아키텍처 파악 ➔ 핵심 파라미터 매핑 ➔ 실무자 피드백'의 3단계 역공학 학습 전략을 사용합니다. "
                "기존에 다뤄보지 않았던 고진공 스퍼터링 공정과 플라즈마 진단 장비를 단 2주 만에 셋업하고 운용해야 했던 프로젝트가 있었습니다. "
                "저는 먼저 장비 전체 매뉴얼의 계통도(P&ID)를 분석하여 가스 공급계, 진공 배기계, RF 전원계의 상호작용 블록 다이어그램을 직접 그렸습니다. "
                "이후 관련 핵심 논문 10편을 크로스체크하여 증착률과 플라즈마 밀도에 직결되는 핵심 변수 4가지를 선별했습니다. "
                "의문이 남는 기구적 특성은 설비 엔지니어 선배를 찾아가 구체적인 데이터 로그를 보여주며 질문하여 노하우를 빠르게 흡수했습니다. "
                "결과적으로 2주 만에 단독 운용 승인을 받았고, 최적 공정 마진을 기존보다 15% 넓히는 레시피를 도출했습니다. "
                "빠른 학습 민첩성으로 차세대 선행 공정 도입 시 누구보다 빠르게 램프업을 완결하겠습니다."
            ),
            "deep_lecture": {
                "background": "반도체 기술은 HBM4, 1c/1d nm DRAM, 하이브리드 본딩 등 신공정과 신설비가 끊임없이 도입됩니다. 기존 지식에 안주하지 않고 빠른 학습 곡선(Learning Curve)을 그릴 수 있는 엔지니어가 핵심 경쟁력입니다.",
                "action_principle": "1. Top-Down 시스템 구조화 (블록 다이어그램 작성)\n2. 원리 기반 심층 분석 (논문 및 공식 매뉴얼 분석)\n3. 현장 실무 노하우 흡수 (선배/엔지니어 인터뷰)\n4. 단기간 성과 검증 및 레시피 최적화 달성",
                "core_points": [
                    "단순 주입식 암기가 아닌 '시스템 계통도(P&ID)' 기반 구조적 접근",
                    "선배 엔지니어에게 질문할 때 '본인의 가설과 데이터'를 준비하는 스마트한 자세",
                    "학습 민첩성(Learning Agility)을 통한 조기 라인 셋업 역량 입증"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="40" y="45" width="210" height="150" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="145" y="85" fill="#38bdf8" font-size="15" font-weight="bold" text-anchor="middle">1. 계통도 구조화</text>
  <text x="145" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">P&amp;ID 분석 및 블록화</text>
  <text x="145" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">가스·진공·RF 상호작용</text>

  <path d="M 265 120 L 305 120" stroke="#f59e0b" stroke-width="3"/>

  <rect x="320" y="45" width="210" height="150" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="425" y="85" fill="#f59e0b" font-size="15" font-weight="bold" text-anchor="middle">2. 핵심 변수 매핑</text>
  <text x="425" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">논문 10편 크로스체크</text>
  <text x="425" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">지배 파라미터 4종 압축</text>

  <path d="M 545 120 L 585 120" stroke="#10b981" stroke-width="3"/>

  <rect x="600" y="45" width="160" height="150" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="680" y="85" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">3. 실무자 검증</text>
  <text x="680" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">가설 기반 타겟 질문</text>
  <text x="680" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">2주 만에 단독 운용</text>
</svg>"""
        },
        {
            "id": "p_14",
            "category": "personality",
            "category_label": "인성·협업·조직 가치",
            "number": 14,
            "title": "라인 공정 중 돌발 사고나 파라미터 이탈 발생 시 초동 대처 및 보고 프로세스",
            "core_keyword": ["인터록 발동", "영향 로트 격리", "5W1H 팩트 기반 보고"],
            "speech_1m30s": (
                "돌발 사고나 공정 이상 발생 시 저의 행동 원칙은 '피해 확산 즉시 차단 ➔ 영향 로트 홀드 ➔ 팩트 중심 5W1H 신속 보고'입니다. "
                "진공 챔버 실험 중 순간적인 냉각수 순환 압력 강하로 챔버 내부 온도가 급상승하는 알람이 울린 적이 있습니다. "
                "저는 즉시 장비 인터록(Interlock)을 활성화하여 RF 전원을 차단하고 안전 밸브를 개방해 장비와 샘플 파손을 방지했습니다. "
                "이어 사고 직전 30분간의 로트와 동일 라인 인접 샘플을 즉시 격리(Hold) 조치하여 오염 확산을 차단했습니다. "
                "이후 추측성 원인은 일절 배제하고 '발생 시각, 이탈 파라미터 수치, 즉각 조치 사항, 현재 설비 상태'를 객관적 데이터 표로 정리하여 담당 교수님과 선배들에게 10분 내 1차 보고했습니다. "
                "그 결과 2차 장비 고장 없이 1시간 내에 냉각수 밸브 이물질을 제거하고 정상 복구할 수 있었습니다. "
                "SK하이닉스 양산 팹에서도 한 번의 실수가 수백억 원의 웨이퍼 스크랩으로 이어지지 않도록 철저한 초동 방어와 프로토콜을 사수하겠습니다."
            ),
            "deep_lecture": {
                "background": "반도체 FAB에서 돌발 설비 이상은 단 몇 분 만에 수십 매의 웨이퍼 폐기(Scrap)를 유발합니다. 패닉에 빠지거나 책임을 회피하지 않고, 안전 수칙에 따른 확산 차단과 신속·정확한 팩트 보고가 생명선입니다.",
                "action_principle": "1. 1단계: 피해 최소화 및 안전 인터록 가동\n2. 2단계: 잠재 영향 제품/로트 홀드(격리)\n3. 3단계: 팩트(데이터) 중심 5W1H 신속 보고 (추측 배제)\n4. 4단계: 근본 원인(RCA) 분석 및 재발 방지 대책 수립",
                "core_points": [
                    "이상 발생 시 '숨기거나 혼자 수습하려 하지 않고' 정형화된 프로토콜 준수",
                    "원인 분석보다 '피해 확산 차단(Interlock & Lot Hold)'이 우선이라는 엔지니어 상식",
                    "보고 시 '추측'이 아닌 '계측 수치와 시간대' 중심 보고"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="40" y="45" width="210" height="150" fill="#1e293b" stroke="#ef4444" stroke-width="2" rx="8"/>
  <text x="145" y="85" fill="#ef4444" font-size="15" font-weight="bold" text-anchor="middle">Step 1: 즉각 차단</text>
  <text x="145" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">인터록(Interlock) 가동</text>
  <text x="145" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">RF 전원 차단 / 안전 확보</text>

  <path d="M 265 120 L 305 120" stroke="#f59e0b" stroke-width="3"/>

  <rect x="320" y="45" width="210" height="150" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="425" y="85" fill="#f59e0b" font-size="15" font-weight="bold" text-anchor="middle">Step 2: 로트 홀드</text>
  <text x="425" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">영향 웨이퍼 즉시 격리</text>
  <text x="425" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">2차 오염·확산 원천 차단</text>

  <path d="M 545 120 L 585 120" stroke="#10b981" stroke-width="3"/>

  <rect x="600" y="45" width="160" height="150" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="680" y="85" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">Step 3: 팩트 보고</text>
  <text x="680" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">5W1H 데이터 정리</text>
  <text x="680" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">10분 내 신속 상황 공유</text>
</svg>"""
        },
        {
            "id": "p_15",
            "category": "personality",
            "category_label": "인성·협업·조직 가치",
            "number": 15,
            "title": "나와 업무 성향(직관파 vs 꼼꼼파 등)이 정반대인 동료와 협업하여 시너지를 낸 경험",
            "core_keyword": ["성향 상호보완", "역할 분담 인터페이스", "크로스 체크"],
            "speech_1m30s": (
                "서로 다른 업무 성향은 갈등의 요인이 아니라, 시스템의 결점을 없애는 최적의 상호보완적 자산입니다. "
                "반도체 회로 시뮬레이션 프로젝트 당시, 저는 모든 파라미터의 물리적 수식을 끝까지 검증해야 직성이 풀리는 꼼꼼한 분석형이었던 반면, 파트너는 빠른 프로토타입 실행과 직관적 가설 설정을 선호하는 스피드형이었습니다. "
                "초기에는 진행 속도 문제로 충돌이 있었으나, 저는 서로의 강점을 시스템화하자고 제안했습니다. "
                "동료가 과감한 가설로 신속하게 3~4가지 설계 후보군을 뽑아내면, 제가 노이즈 마진과 코너 시뮬레이션을 정밀하게 수행하여 결함을 검증하는 투트랙 인터페이스를 구축했습니다. "
                "이 협업 방식을 통해 설계 탐색 속도는 2배로 높이면서도 설계 오류는 0건을 기록하여 최우수 프로젝트로 선정되었습니다. "
                "SK하이닉스에서도 다양한 부서와 엔지니어의 상이한 강점을 조화롭게 엮어 집단지성 시너지를 극대화하겠습니다."
            ),
            "deep_lecture": {
                "background": "반도체 조직은 소자, 공정, 회로, 설비 등 다양한 백그라운드와 성향을 가진 엔지니어들이 유기적으로 연결되어 일합니다. 나와 다른 스타일을 배척하지 않고 생산적인 파트너십으로 전환하는 포용성과 협업 지능을 평가합니다.",
                "action_principle": "1. 상대방의 업무 스타일 존중 및 인정\n2. 갈등을 시스템적 역할 분담으로 전환\n3. 상호보완적 투트랙 프로세스 구축 (속도 + 정밀도)\n4. 시너지 창출 및 조직 성과 달성",
                "core_points": [
                    "성향 차이를 '틀림'이 아닌 '다름'과 '상호보완성'으로 규정",
                    "신속한 탐색(속도)과 정밀한 검증(완결성)의 환상적 조합 제시",
                    "상호 피드백을 통해 프로젝트 완성도를 끌어올린 실질적 사례"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="40" y="45" width="210" height="150" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="145" y="85" fill="#38bdf8" font-size="15" font-weight="bold" text-anchor="middle">동료: 스피드 &amp; 가설</text>
  <text x="145" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">신속한 프로토타이핑</text>
  <text x="145" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">후보군 신속 도출</text>

  <path d="M 265 120 L 305 120" stroke="#f59e0b" stroke-width="3"/>

  <rect x="320" y="45" width="210" height="150" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="425" y="85" fill="#f59e0b" font-size="15" font-weight="bold" text-anchor="middle">본인: 정밀 &amp; 무결점</text>
  <text x="425" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">코너 시뮬레이션 검증</text>
  <text x="425" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">노이즈 마진 수학적 확정</text>

  <path d="M 545 120 L 585 120" stroke="#10b981" stroke-width="3"/>

  <rect x="600" y="45" width="160" height="150" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="680" y="85" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">시너지 성과</text>
  <text x="680" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">개발 속도 2배 향상</text>
  <text x="680" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">설계 결함 0건 달성</text>
</svg>"""
        }
    ]
    return topics
