# -*- coding: utf-8 -*-
"""
인성 질문 16~20문항 데이터 생성 스크립트 (p_part4.py)
"""

def get_personality_topics_part4():
    topics = [
        {
            "id": "p_16",
            "category": "personality",
            "category_label": "인성·협업·조직 가치",
            "number": 16,
            "title": "많은 노력을 쏟았으나 결과가 기대에 미치지 못했을 때의 회복탄력성과 피드백 수용",
            "core_keyword": ["원인 분해", "객관적 피드백 수용", "재도전 로드맵"],
            "speech_1m30s": (
                "노력 대비 결과가 부진할 때 저는 실망에 매몰되지 않고, 실패를 '성공을 위한 데이터 포인트'로 전환하는 회복탄력성을 발휘합니다. "
                "박막 증착 균일도 개선을 위해 3개월간 100회 이상의 실험을 수행했으나, 최종 평가에서 목표 편차 3%를 달성하지 못하고 5.2%에 머물렀던 적이 있습니다. "
                "결과를 받아들인 직후, 감정적 좌절 대신 실험 전 과정을 5개 단계로 분해하여 데이터 로그를 전수 조사했습니다. "
                "그리고 연구원 선배들에게 제 실패 데이터를 가감 없이 공개하며 피드백을 요청했습니다. "
                "그 과정에서 제가 챔버 내부 가스 유량비에만 집중하느라 샤워헤드와 서셉터 간의 미세한 간격(Gap) 열팽창 효과를 간과했음을 발견했습니다. "
                "피드백을 즉시 반영하여 Gap 보정 설계를 추가했고, 재실험 3주 만에 편차 2.1%를 달성하며 목표를 초과 달성했습니다. "
                "실패를 두려워하지 않고 피드백을 발판 삼아 한계를 돌파하는 집요한 엔지니어가 되겠습니다."
            ),
            "deep_lecture": {
                "background": "반도체 수율 향상 및 소자 개발은 99번의 실패 끝에 1번의 성공을 거두는 고난도 연구 개발의 연속입니다. 실패에 좌절하지 않고 실패 원인을 데이터로 규명하며, 타인의 조언을 적극 흡수하는 회복탄력성(Resilience)을 평가합니다.",
                "action_principle": "1. 결과에 대한 담담한 인정 및 감정 통제\n2. 실패 요인의 체계적 분해 및 데이터 기반 분석\n3. 선배/동료의 객관적 비판 및 피드백 적극 수용\n4. 솔루션 수정 후 재도전을 통한 목표 초과 달성",
                "core_points": [
                    "노력의 양(100회 실험)을 앞세우지 않고 '실패 원인의 구조적 규명' 강조",
                    "자신의 부족함을 인정하고 피드백을 구하는 개방적(Open-minded) 태도",
                    "실패가 다음 성공의 핵심 자산이 되었음을 입증"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="40" y="45" width="210" height="150" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="145" y="85" fill="#38bdf8" font-size="15" font-weight="bold" text-anchor="middle">1. 실패 원인 분해</text>
  <text x="145" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">편차 5.2% 결과 직시</text>
  <text x="145" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">5단계 전수 데이터 감사</text>

  <path d="M 265 120 L 305 120" stroke="#f59e0b" stroke-width="3"/>

  <rect x="320" y="45" width="210" height="150" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="425" y="85" fill="#f59e0b" font-size="15" font-weight="bold" text-anchor="middle">2. 개방적 피드백</text>
  <text x="425" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">선배진 데이터 공개 리뷰</text>
  <text x="425" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">Gap 열팽창 병목 규명</text>

  <path d="M 545 120 L 585 120" stroke="#10b981" stroke-width="3"/>

  <rect x="600" y="45" width="160" height="150" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="680" y="85" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">3. 재도전 완결</text>
  <text x="680" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">Gap 보정 파라미터 적용</text>
  <text x="680" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">편차 2.1% 초과 달성</text>
</svg>"""
        },
        {
            "id": "p_17",
            "category": "personality",
            "category_label": "인성·협업·조직 가치",
            "number": 17,
            "title": "규정 준수(Safety/Protocol)와 생산성/납기 단축 간의 윤리적 딜레마 직면 시 선택 기준",
            "core_keyword": ["안전·품질 타협 불가", "원칙 속 프로세스 최적화", "롱텀 리스크 방지"],
            "speech_1m30s": (
                "안전 규정과 품질 프로토콜은 어떤 상황에서도 타협할 수 없는 절대적 가치이며, 진정한 생산성 혁신은 규정을 우회하는 것이 아니라 규정을 지키면서 프로세스를 효율화하는 데서 나옵니다. "
                "학부 공동 장비 셋업 중, 납기 일정이 촉박하다는 이유로 독성 가스 퍼지(Purge) 검증 단계를 축소하고 곧바로 시운전에 들어가자는 팀 내 의견이 있었습니다. "
                "저는 '10분의 단축이 라인 전체의 대형 사고와 수개월의 셧다운으로 이어질 수 있다'는 점을 명확히 짚으며 원칙 준수를 설득했습니다. "
                "대신 납기를 맞추기 위해, 안전 규정을 준수하면서도 병렬로 진행할 수 있는 배선 작업과 소프트웨어 캘리브레이션을 동시 진행하는 '병렬 공정 최적화'를 실행했습니다. "
                "결과적으로 단 한 건의 안전사고 없이 목표 일정 내에 셋업을 완벽히 마쳤습니다. "
                "SK하이닉스 양산 현장에서도 안전과 신뢰성 프로토콜을 철저히 사수하면서도 스마트한 공정 재배치로 생산성을 견인하겠습니다."
            ),
            "deep_lecture": {
                "background": "반도체 클린룸은 유독 가스(SiH4, NF3, Cl2 등)와 고전압, 초정밀 화학물질을 다룹니다. 납기나 수율 압박 때문에 안전·품질 규정을 무시하는 행동은 회사 전체를 위협하는 치명적 참사를 낳을 수 있습니다.",
                "action_principle": "1. 절대 원칙 천명: 안전 및 품질 프로토콜은 타협 불가(Non-negotiable)\n2. 리스크 예측 환기: 지름길 선택 시 발생할 괴멸적 비용 공유\n3. 합리적 대안 제시: 규정 내에서 병렬화(Parallelization)를 통한 시간 단축\n4. 무사고 완결 및 생산성 목표 동시 달성",
                "core_points": [
                    "단순히 ‘안 됩니다’라고 거절하는 데 그치지 않고 ‘병렬 작업’ 대안 제시",
                    "‘단기적 편의’보다 ‘장기적 신뢰성과 안정성’을 우선하는 엔지니어 윤리관",
                    "SK하이닉스의 EHS(환경·보건·안전) 경영 철학과 완벽히 부합"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="40" y="45" width="210" height="150" fill="#1e293b" stroke="#ef4444" stroke-width="2" rx="8"/>
  <text x="145" y="85" fill="#ef4444" font-size="15" font-weight="bold" text-anchor="middle">원칙 사수 (Safety First)</text>
  <text x="145" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">독성 가스 퍼지 검증</text>
  <text x="145" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">규정 축소·우회 절대 거부</text>

  <path d="M 265 120 L 305 120" stroke="#f59e0b" stroke-width="3"/>

  <rect x="320" y="45" width="210" height="150" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="425" y="85" fill="#f59e0b" font-size="15" font-weight="bold" text-anchor="middle">스마트 대안 (병렬화)</text>
  <text x="425" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">배선 &amp; SW 보정 병행</text>
  <text x="425" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">공정 순서 재배치 최적화</text>

  <path d="M 545 120 L 585 120" stroke="#10b981" stroke-width="3"/>

  <rect x="600" y="45" width="160" height="150" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="680" y="85" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">동시 달성</text>
  <text x="680" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">무사고 100% 안전</text>
  <text x="680" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">목표 납기 내 완결</text>
</svg>"""
        },
        {
            "id": "p_18",
            "category": "personality",
            "category_label": "인성·협업·조직 가치",
            "number": 18,
            "title": "주변 동료나 선후배들이 평가하는 '엔지니어로서의 본인'의 핵심 평판과 캐릭터",
            "core_keyword": ["집요한 원인 해결사", "끝까지 책임지는 오너십", "정리 공유 요정"],
            "speech_1m30s": (
                "동료들은 저를 '원인을 끝까지 추적해 매듭짓는 집요한 해결사'이자 '지식을 투명하게 나누는 공유형 엔지니어'로 평가합니다. "
                "캡스톤 디자인 프로젝트 당시, 회로 보드에서 간헐적으로 전원 드롭이 발생하여 팀원들이 원인을 찾지 못하고 부품을 통째로 교체하려 했을 때였습니다. "
                "저는 일시적 해결에 안주하지 않고, 오실로스코프로 48시간 동안 파워서플라이의 과도응답 리플 전압을 전수 로깅했습니다. "
                "그 결과 특정 부하 조건에서 접지 임피던스가 치솟는 현상을 밝혀내 바이패스 커패시터를 적재적소에 배치해 근본 해결했습니다. "
                "이후 동일 문제가 재발하지 않도록 '트러블슈팅 가이드 및 노이즈 디버깅 위키'를 만들어 팀과 후배들에게 공유했습니다. "
                "팀원들은 '너에게 문제를 맡기면 임시변통이 아니라 뿌리까지 뽑아내고, 팀 전체의 지산으로 만들어준다'며 깊은 신뢰를 보냈습니다. "
                "SK하이닉스에서도 수율 저하의 근본 원인을 뿌리 뽑고 팀의 지적 자산을 살찌우는 든든한 동료가 되겠습니다."
            ),
            "deep_lecture": {
                "background": "타인의 평가는 지원자의 메타인지와 실제 협업 레퍼런스를 보여줍니다. 자기 자랑에 그치지 않고, 동료들이 실제로 의지하고 도움을 받았던 구체적인 행동 양식과 별명/평판을 제시해야 합니다.",
                "action_principle": "1. 주변의 객관적 키워드 제시 (집요한 문제 해결사 + 지식 공유자)\n2. 일시적 땜질이 아닌 근본 원인(Root Cause) 해결 에피소드\n3. 개인의 해결을 조직의 자산(가이드/위키)으로 승화시킨 행동\n4. 팀 내 신뢰도 및 기여도 증명",
                "core_points": [
                    "동료들의 실제 평가 표현을 인용하여 진정성 확보",
                    "‘근본 원인 해결’이라는 엔지니어의 핵심 덕목과 ‘공유’라는 조직 친화적 태도 융합",
                    "SK하이닉스의 지식 공유 및 집단지성 문화에 직결"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="40" y="45" width="210" height="150" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="145" y="85" fill="#38bdf8" font-size="15" font-weight="bold" text-anchor="middle">평판 1: 집요한 해결사</text>
  <text x="145" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">땜질 처방 거부</text>
  <text x="145" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">48시간 연속 파형 분석</text>

  <path d="M 265 120 L 305 120" stroke="#f59e0b" stroke-width="3"/>

  <rect x="320" y="45" width="210" height="150" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="425" y="85" fill="#f59e0b" font-size="15" font-weight="bold" text-anchor="middle">평판 2: 지식 공유자</text>
  <text x="425" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">트러블슈팅 위키 문서화</text>
  <text x="425" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">동료·후배 노하우 전파</text>

  <path d="M 545 120 L 585 120" stroke="#10b981" stroke-width="3"/>

  <rect x="600" y="45" width="160" height="150" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="680" y="85" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">조직적 가치</text>
  <text x="680" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">팀원들의 전폭적 신뢰</text>
  <text x="680" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">재발 방지 시스템화</text>
</svg>"""
        },
        {
            "id": "p_19",
            "category": "personality",
            "category_label": "인성·협업·조직 가치",
            "number": 19,
            "title": "SK하이닉스의 경영철학인 VWBE를 실제 프로젝트에서 발휘하여 동료의 동기부여를 이끈 경험",
            "core_keyword": ["솔선수범", "VWBE 전파", "심리적 안전감 조성"],
            "speech_1m30s": (
                "VWBE의 진정한 힘은 개인의 몰입을 넘어, 동료들의 자발적 동기부여까지 점화하는 '선한 영향력'에 있다고 믿습니다. "
                "산학 과제에서 촉박한 일정과 복잡한 파라미터 조합으로 인해 팀원들의 사기가 저하되고 수동적으로 변했던 적이 있습니다. "
                "저는 팀원들에게 업무를 강요하는 대신, 먼저 자발적으로 주말 동안 1,000건의 실험 데이터를 정리하고 통계 분석 대시보드 프로토타입을 만들어 월요일 아침 팀원들에게 공유했습니다. "
                "제가 열정을 쏟아 기초 토대를 마련한 것을 본 동료들은 큰 자극을 받았고, '나도 데이터 시각화 모듈을 붙여보겠다', '내가 통계 검증을 교차 검토하겠다'며 자발적으로 두뇌 활용(Brain Engagement)을 시작했습니다. "
                "결국 팀 전체가 SUPEX 수준의 몰입 상태에 도달하여 당초 일정보다 2주 앞당겨 최종 결과물을 제출했습니다. "
                "SK하이닉스에서도 먼저 행동하고 헌신하는 VWBE의 기폭제가 되어 조직 전체의 시너지를 이끌겠습니다."
            ),
            "deep_lecture": {
                "background": "SK의 핵심 문화인 VWBE는 한 사람의 자발적 열정이 팀 전체로 번져나갈 때 SUPEX(Super Excellent) 컴퍼니를 달성할 수 있습니다. 리더십이나 강압이 아닌 '솔선수범과 헌신'으로 팀원들의 내재적 동기를 자극한 경험을 요구합니다.",
                "action_principle": "1. 팀 내 침체 상황 인식 (강요형 리더십 지양)\n2. 솔선수범 기반 행동: 스스로 먼저 높은 수준의 결과물 선제 구축\n3. 동료들의 자발적 동기(Willingly) 점화 및 심리적 안전감 부여\n4. 팀 전체의 SUPEX 몰입 상태 유도 및 조기 달성",
                "core_points": [
                    "말이 아닌 행동(선제적 프로토타입 제작)으로 팀원들을 감동시킨 과정",
                    "개인의 열정이 팀 전체의 VWBE로 확산되는 메커니즘 묘사",
                    "SK하이닉스가 지향하는 행복하고 자발적인 조직 문화 기여"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="40" y="45" width="210" height="150" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="145" y="85" fill="#f59e0b" font-size="15" font-weight="bold" text-anchor="middle">1. 선제적 솔선수범</text>
  <text x="145" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">주말 자발적 데이터 분석</text>
  <text x="145" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">분석 대시보드 선제 공유</text>

  <path d="M 265 120 L 305 120" stroke="#38bdf8" stroke-width="3"/>

  <rect x="320" y="45" width="210" height="150" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="425" y="85" fill="#38bdf8" font-size="15" font-weight="bold" text-anchor="middle">2. 동료 VWBE 촉발</text>
  <text x="425" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">내재적 동기부여 전파</text>
  <text x="425" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">자발적 모듈 개발 참여</text>

  <path d="M 545 120 L 585 120" stroke="#10b981" stroke-width="3"/>

  <rect x="600" y="45" width="160" height="150" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="680" y="85" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">3. SUPEX 완결</text>
  <text x="680" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">2주 조기 목표 달성</text>
  <text x="680" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">집단지성 시너지 창출</text>
</svg>"""
        },
        {
            "id": "p_20",
            "category": "personality",
            "category_label": "인성·협업·조직 가치",
            "number": 20,
            "title": "입사 후 3년 차, 5년 차에 SK하이닉스에서 이루고자 하는 구체적인 엔지니어링 마일스톤과 비전",
            "core_keyword": ["1b/1c nm 산포 안정화", "HBM 고단화 핵심 수율 견인", "글로벌 팹 마스터 엔지니어"],
            "speech_1m30s": (
                "입사 3년 차에는 담당 단위 공정의 산포를 통계적으로 완벽히 장악하는 '공정 스페셜리스트'가 되고, 5년 차에는 HBM과 차세대 초고단 3D NAND의 수율을 견인하는 '수율 아키텍트'로 성장하겠습니다. "
                "3년 차에는 FAB 현장의 설비 센서 데이터와 계측 프로파일을 결합하여 공정 Cpk(공정능력지수)를 1.67 이상으로 끌어올리는 이상 탐지 자동화 알고리즘을 현업에 안착시키겠습니다. "
                "이를 통해 비계획 장비 셧다운과 웨이퍼 결함을 선제적으로 방어하는 핵심 기여를 하겠습니다. "
                "5년 차에는 16단 이상 HBM 적층 공정의 TSV 및 MR-MUF 공정 마진 최적화나 1c nm 이하 DRAM의 BCAT 미세 결함 제어 프로젝트의 테스크포스 리더를 맡겠습니다. "
                "단위 공정의 경계를 넘어 인접 공정과의 복합 결함을 통합 해결함으로써, SK하이닉스가 AI 메모리 시장에서 압도적 1위를 영속할 수 있도록 핵심 기술 주권을 지키는 엔지니어로 도약하겠습니다."
            ),
            "deep_lecture": {
                "background": "포부 질문은 막연한 '열심히 배우겠다'가 아니라, 회사의 핵심 로드맵(1b/1c nm DRAM, HBM4 16단 적층, 300단 이상 3D NAND)과 연계된 구체적이고 정량적인 성장 마일스톤을 보여주어야 합니다.",
                "action_principle": "1. 3년 차 단기 목표: 단위 공정 완전 장악 및 Cpk 1.67 달성 (실무적 스페셜리스트)\n2. 5년 차 중장기 목표: HBM 적층 / 선단 D램 수율 통합 아키텍트 (TF 리더십)\n3. SK하이닉스의 미래 경쟁력(AI 메모리 초격차)과의 긴밀한 정렬\n4. 책임감 있는 기술 주권 사수 의지 표명",
                "core_points": [
                    "구체적인 수치(Cpk 1.67, 16단 HBM, 1c nm DRAM) 제시로 전문성 신뢰도 확보",
                    "‘배우는 사람(Junior)’에서 ‘성과를 주도하는 핵심 인력(Senior Lead)’으로의 명확한 로드맵",
                    "SK하이닉스의 비전과 지원자의 목표 일치"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="40" y="45" width="210" height="150" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="145" y="85" fill="#38bdf8" font-size="15" font-weight="bold" text-anchor="middle">3년 차: 공정 스페셜리스트</text>
  <text x="145" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">공정 Cpk &gt; 1.67 달성</text>
  <text x="145" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">센서 기반 이상 사전 감지</text>

  <path d="M 265 120 L 305 120" stroke="#f59e0b" stroke-width="3"/>

  <rect x="320" y="45" width="210" height="150" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="425" y="85" fill="#f59e0b" font-size="15" font-weight="bold" text-anchor="middle">5년 차: 수율 아키텍트</text>
  <text x="425" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">16단 HBM MR-MUF 최적화</text>
  <text x="425" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">1c nm BCAT 복합 결함 해결</text>

  <path d="M 545 120 L 585 120" stroke="#10b981" stroke-width="3"/>

  <rect x="600" y="45" width="160" height="150" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="680" y="85" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">궁극적 비전</text>
  <text x="680" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">글로벌 팹 마스터 엔지니어</text>
  <text x="680" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">AI 메모리 초격차 수호</text>
</svg>"""
        }
    ]
    return topics
