# -*- coding: utf-8 -*-
"""
인성 질문 6~10문항 데이터 생성 스크립트 (p_part2.py)
"""

def get_personality_topics_part2():
    topics = [
        {
            "id": "p_06",
            "category": "personality",
            "category_label": "인성·협업·조직 가치",
            "number": 6,
            "title": "SK의 핵심 가치인 'VWBE(자발적·의욕적 두뇌활용)'를 바탕으로 한계를 돌파한 경험",
            "core_keyword": ["SUPEX 추구", "자발적 몰입", "자동화 툴 개발"],
            "speech_1m30s": (
                "주어진 업무 범위에 만족하지 않고, 프로세스 병목을 해소하기 위해 스스로 야간까지 파고들어 자동화 분석 도구를 구축했던 경험이 있습니다. "
                "반복되는 데이터 수작업 검증으로 팀 전체가 일주일에 10시간 이상을 낭비하고 있었으나, 기존 관행이라는 이유로 방치되어 있었습니다. "
                "저는 시키지 않았지만 자발적으로 퇴근 후 파이썬 기반 데이터 파싱 및 이상치 자동 알림 스크립트를 개발하기 시작했습니다. "
                "사내 보안 가이드라인을 준수하며 일주일간 코드를 테스트했고, 결국 2시간 걸리던 데이터 검증을 단 3초 만에 끝내는 파이프라인을 완성했습니다. "
                "이를 팀에 배포하여 주당 10시간의 공수를 절감하고 오류율을 0%로 만들었습니다. "
                "자발적 의욕(VWBE)으로 기존 한계를 뛰어넘어 팀의 생산성을 극대화하는 것이 진정한 엔지니어의 자세임을 체감했습니다."
            ),
            "deep_lecture": {
                "background": "SK의 고유 경영철학인 SKMS(SK Management System)에서 VWBE(Voluntarily, Willingly, Brain Engagement)는 단순한 지시 수행자가 아닌 '자기 주도적 최고 목표(SUPEX) 도전자'를 의미합니다.",
                "action_principle": "1. 문제 인식: 관행적 낭비 요소의 능동적 포착\n2. 자발적 몰입: 지시받지 않은 영역까지 스스로 두뇌 활용\n3. 가치 창출: 팀 전체의 생산성 및 품질 혁신\n4. SUPEX(Super Excellent Level) 도달 증명",
                "core_points": [
                    "‘누가 시켜서 한 일’이 아닌 ‘순수 자발적 동기’ 강조",
                    "정량적 성과 (주당 10시간 절감, 오류율 0%) 제시",
                    "개인적 만족에 그치지 않고 ‘조직 자산화(배포)’로 연결"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="50" y="45" width="200" height="150" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="150" y="85" fill="#f59e0b" font-size="15" font-weight="bold" text-anchor="middle">Voluntarily (자발적)</text>
  <text x="150" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">관행적 낭비 포착</text>
  <text x="150" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">지시 없는 주도적 착수</text>

  <path d="M 270 120 L 305 120" stroke="#38bdf8" stroke-width="3"/>

  <rect x="315" y="45" width="200" height="150" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="415" y="85" fill="#38bdf8" font-size="15" font-weight="bold" text-anchor="middle">Brain Engagement</text>
  <text x="415" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">스크립트 파이프라인</text>
  <text x="415" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">검증 자동화 알고리즘</text>

  <path d="M 535 120 L 570 120" stroke="#10b981" stroke-width="3"/>

  <rect x="580" y="45" width="180" height="150" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="670" y="85" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">SUPEX 달성</text>
  <text x="670" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">2시간 ➔ 3초 단축</text>
  <text x="670" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">오류율 0% 팀 자산화</text>
</svg>"""
        },
        {
            "id": "p_07",
            "category": "personality",
            "category_label": "인성·협업·조직 가치",
            "number": 7,
            "title": "상사나 선배의 업무 지시가 공학적으로 비합리적이라고 판단될 때의 대처법",
            "core_keyword": ["의도 파악", "데이터 기반 대안", "리스크-기대효과 비교"],
            "speech_1m30s": (
                "상사의 지시를 현장에서 즉각 반박하지 않고, 먼저 '지시의 근본적인 경영상 의도'를 파악한 뒤 공학적 데이터와 대안을 갖추어 1:1로 건의하겠습니다. "
                "선배 엔지니어의 판단에는 현장 상황이나 일정 등 제가 미처 보지 못한 전체적인 맥락이 담겨 있을 수 있습니다. 따라서 '왜 이런 지시를 내리셨을까'를 먼저 경청하고 고민하겠습니다. "
                "그럼에도 공학적 리스크(수율 저하, 설비 부하)가 명확하다면, 감정적 반발이 아닌 정량 데이터로 보고서를 준비하겠습니다. "
                "'기존 지시 방식대로 진행 시 예상되는 수율 리스크 A%'와 이를 방어하면서 상사의 목적을 달성할 수 있는 '대안 B'를 수치화하여 조용히 건의드리겠습니다. "
                "비판을 위한 비판이 아니라, 조직의 손실을 막고 상사의 성공을 돕는 엔지니어로 행동하겠습니다."
            ),
            "deep_lecture": {
                "background": "반도체 팹은 엄격한 규율과 팀워크가 요구되지만, 맹목적인 복종은 자칫 대량 불량(웨이퍼 폐기)으로 이어질 수 있습니다. '예의를 갖추되 데이터 기반으로 리스크를 선제 보고하는 프로페셔널리즘'을 평가합니다.",
                "action_principle": "1. 선 경청: 상사의 거시적 의도 파악\n2. 객관적 검증: 비합리성의 원인을 데이터로 규명\n3. 대안(Solution) 제시: 반론만 제기하지 않고 대안 2안을 함께 보고\n4. 조직 보호: 비공개 1:1 건의로 상사의 체면과 조직 안정 도모",
                "core_points": [
                    "감정적 반항 vs 무조건적 굴복의 양극단 극복",
                    "엔지니어의 무기는 '데이터와 대안(Alternative)'임을 강조",
                    "조직의 수율과 품질을 사수하려는 주인 의식"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <circle cx="140" cy="120" r="50" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="140" y="115" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">1단계</text>
  <text x="140" y="135" fill="#cbd5e1" font-size="12" text-anchor="middle">상사 의도 경청</text>

  <line x1="200" y1="120" x2="280" y2="120" stroke="#64748b" stroke-width="2"/>

  <circle cx="340" cy="120" r="50" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
  <text x="340" y="115" fill="#f59e0b" font-size="14" font-weight="bold" text-anchor="middle">2단계</text>
  <text x="340" y="135" fill="#cbd5e1" font-size="12" text-anchor="middle">데이터 리스크 분석</text>

  <line x1="400" y1="120" x2="480" y2="120" stroke="#64748b" stroke-width="2"/>

  <circle cx="540" cy="120" r="50" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
  <text x="540" y="115" fill="#a855f7" font-size="14" font-weight="bold" text-anchor="middle">3단계</text>
  <text x="540" y="135" fill="#cbd5e1" font-size="12" text-anchor="middle">대안 A/B 수립</text>

  <line x1="600" y1="120" x2="680" y2="120" stroke="#64748b" stroke-width="2"/>

  <circle cx="710" cy="120" r="45" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
  <text x="710" y="115" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">4단계</text>
  <text x="710" y="135" fill="#cbd5e1" font-size="11" text-anchor="middle">1:1 건의</text>
</svg>"""
        },
        {
            "id": "p_08",
            "category": "personality",
            "category_label": "인성·협업·조직 가치",
            "number": 8,
            "title": "촉박한 마감 일정과 품질(완성도) 사이에서 트레이드오프 발생 시 우선순위 기준",
            "core_keyword": ["치명 결함 무관용", "핵심 스펙 사수", "단계적 릴리즈 전략"],
            "speech_1m30s": (
                "양산 엔지니어에게 마감과 품질은 양자택일의 문제가 아니라, '치명적 결함 무관용'의 대원칙 아래 '우선순위 기반의 단계적 달성'으로 풀어야 할 과제입니다. "
                "반도체에서 일정에 쫓겨 품질을 타협하면 고객사 클레임과 막대한 웨이퍼 폐기로 이어집니다. 따라서 안전 및 소자의 핵심 스펙(Baseline Yield)에 영향을 주는 항목은 타협 없이 100% 품질을 고수하겠습니다. "
                "대신 전체 항목을 '필수 불가결(Must-have)'과 '부가적 개선(Nice-to-have)'으로 분리하겠습니다. 1차 마감일까지 핵심 신뢰성과 수율에 직결되는 코어 스펙을 무결점으로 완성하여 납기를 준수하겠습니다. "
                "이어 부가적인 최적화 작업은 상사 및 유관 부서와 사전 조율을 거쳐 2단계 업데이트 일정으로 분리해 완결하겠습니다. "
                "품질의 마지노선을 지키며 납기 신뢰성을 확보하는 현실적이고 전략적인 실행력을 발휘하겠습니다."
            ),
            "deep_lecture": {
                "background": "실제 양산 현장은 매일 납기와 수율의 줄다리기입니다. '무조건 품질 최고'라는 비현실적 이상론이나, '일정 맞추려 불량 묵인'이라는 위험한 태도 모두 탈락 대상입니다. '핵심 스펙 분리 및 단계적 접근'이 정답입니다.",
                "action_principle": "1. 품질의 절대 기준 정의 (안전, 핵심 신뢰성 = 타협 불가)\n2. 기능 및 항목의 모듈화 (Core vs Nice-to-have)\n3. 1차 컷오프 납기 준수 + 2차 패치 일정 투명한 소통",
                "core_points": [
                    "품질 타협으로 인한 잠재적 천문학적 손실 인지",
                    "모듈형 우선순위화(Triage) 역량",
                    "상사 및 고객사와의 일정 투명성 확보"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="50" y="45" width="320" height="150" fill="#1e293b" stroke="#ef4444" stroke-width="2" rx="8"/>
  <text x="210" y="80" fill="#ef4444" font-size="16" font-weight="bold" text-anchor="middle">[ Core Quality ] 타협 불가</text>
  <text x="210" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">소자 핵심 신뢰성 &amp; 안전 스펙</text>
  <text x="210" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">수율 마지노선 100% 사수</text>
  <text x="210" y="165" fill="#f59e0b" font-size="12" text-anchor="middle">➔ 1차 마감 기한 내 무결점 납기</text>

  <rect x="430" y="45" width="320" height="150" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="590" y="80" fill="#38bdf8" font-size="16" font-weight="bold" text-anchor="middle">[ Sub-Optimization ] 단계적 진행</text>
  <text x="590" y="115" fill="#cbd5e1" font-size="13" text-anchor="middle">부가적 편의 &amp; 마이너 최적화</text>
  <text x="590" y="140" fill="#cbd5e1" font-size="13" text-anchor="middle">일정 투명 소통 및 합의</text>
  <text x="590" y="165" fill="#10b981" font-size="12" text-anchor="middle">➔ 2단계 후속 일정 완결</text>
</svg>"""
        },
        {
            "id": "p_09",
            "category": "personality",
            "category_label": "인성·협업·조직 가치",
            "number": 9,
            "title": "타 부서와의 이해관계 대립으로 일정 지연이 예상될 때의 조율 노하우",
            "core_keyword": ["상위 공동 KPI", "상대 부서 제약 경청", "절충 데이터 시뮬레이션"],
            "speech_1m30s": (
                "부서 간 갈등은 각자의 직무 KPI에 충실하기 때문에 발생하는 자연스러운 현상입니다. 따라서 우리 부서의 입장만 강요하기보다 '조직 전체의 상위 목표(수율과 출하 일정)'를 공통분모로 삼아 해법을 찾겠습니다. "
                "실제 공정팀과 설비팀 간의 메인터넌스 일정 충돌 상황을 가정한다면, 상대 부서가 일정 조정을 꺼리는 근본 이유(부품 수급, 예방보전 주기 등)를 먼저 경청하겠습니다. "
                "이후 각자의 일정 고집 시 발생하는 손실과, 3일씩 일정을 교차 배분했을 때의 시뮬레이션 데이터를 테이블 위에 올리겠습니다. "
                "상대 부서의 실무적 부담을 덜어줄 수 있는 지원책(데이터 전처리 지원, 인력 백업)을 먼저 제안하며 윈윈(Win-Win)의 절충점을 도출하겠습니다. "
                "사일로(Silo)를 넘어 전체 최적화의 관점으로 소통하는 엔지니어가 되겠습니다."
            ),
            "deep_lecture": {
                "background": "반도체 회사는 공정(수율), 설비(가동률), 품질(불량률), 생산관리(납기) 부서 간의 이해관계가 첨예하게 대립합니다. 자기 부서 이기주의(Silo Effect)를 넘어 '회사 전체 KPI'로 협상하는 능력을 봅니다.",
                "action_principle": "1. 상대 부서의 KPI와 현실적 페인포인트(Pain-point) 파악\n2. 상위 공동 목표(Overall Goal) 상기\n3. 상호 양보와 시뮬레이션 기반 절충안 제시\n4. 우리 부서의 지원책 선제적 제공",
                "core_points": [
                    "부서 간 대립을 감정 싸움이 아닌 '제도/KPI의 문제'로 보는 성숙한 시각",
                    "데이터 기반의 객관적 중재안",
                    "전체 최적화(Global Optimum) 지향 마인드"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="50" y="50" width="200" height="140" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="150" y="90" fill="#38bdf8" font-size="15" font-weight="bold" text-anchor="middle">공정 부서</text>
  <text x="150" y="125" fill="#cbd5e1" font-size="13" text-anchor="middle">수율 &amp; 품질 최우선</text>
  <text x="150" y="150" fill="#94a3b8" font-size="12" text-anchor="middle">파라미터 변경 요구</text>

  <rect x="550" y="50" width="200" height="140" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="650" y="90" fill="#f59e0b" font-size="15" font-weight="bold" text-anchor="middle">설비 부서</text>
  <text x="650" y="125" fill="#cbd5e1" font-size="13" text-anchor="middle">가동률 &amp; 부품 주기</text>
  <text x="650" y="150" fill="#94a3b8" font-size="12" text-anchor="middle">다운타임 최소화</text>

  <rect x="280" y="30" width="240" height="180" fill="#0f172a" stroke="#10b981" stroke-width="2" rx="10"/>
  <text x="400" y="70" fill="#10b981" font-size="16" font-weight="bold" text-anchor="middle">전체 상위 KPI로 정렬</text>
  <text x="400" y="105" fill="#f1f5f9" font-size="13" text-anchor="middle">SK하이닉스 종합 원가 &amp; 출하</text>
  <text x="400" y="135" fill="#cbd5e1" font-size="12" text-anchor="middle">데이터 시뮬레이션 절충</text>
  <text x="400" y="165" fill="#38bdf8" font-size="12" text-anchor="middle">교차 지원 체계 합의</text>
</svg>"""
        },
        {
            "id": "p_10",
            "category": "personality",
            "category_label": "인성·협업·조직 가치",
            "number": 10,
            "title": "본인이 가진 가장 치명적인 단점과 이를 극복하기 위해 실천 중인 루틴",
            "core_keyword": ["과도한 완벽주의", "타임박싱(Time-boxing)", "중간 공유 문화"],
            "speech_1m30s": (
                "저의 단점은 모든 세부 사항을 완벽하게 검증하려다 초기 의사결정이 다소 지연될 수 있다는 점입니다. "
                "데이터를 꼼꼼히 살피는 것은 엔지니어의 장점이지만, 양산 라인의 긴박한 셋업 상황에서는 80%의 신속한 판단과 단계적 개선이 더 중요할 때가 많습니다. "
                "이를 보완하기 위해 두 가지 구체적 루틴을 정착시켰습니다. "
                "첫째, 과제를 시작할 때 분석 시간의 상한선을 미리 정해두는 '타임박싱(Time-boxing)' 기법을 실천합니다. 정해진 시간 내에 나온 데이터로 1차 가설을 세우고 실행합니다. "
                "둘째, 혼자서 100% 완성할 때까지 쥐고 있지 않고, 50% 진행 시점에 동료 및 선배에게 '중간 공유'를 요청해 방향성을 피드백받습니다. "
                "신중함이라는 강점은 살리되, 현장이 요구하는 신속한 실행력(Speed)을 겸비한 엔지니어로 진화하고 있습니다."
            ),
            "deep_lecture": {
                "background": "단점 질문의 치명적 실수는 치명적인 인격 결함(거짓말, 분노 조절 실패)을 말하거나, 반대로 뻔한 장점 자랑을 늘어놓는 것입니다. '실제 일어날 법한 공학적 단점'과 '이를 통제하는 체계적인 행동 루틴'이 핵심입니다.",
                "action_principle": "1. 장점의 이면에서 비롯된 현실적 단점 솔직 인정\n2. 단점이 조직에 미칠 수 있는 리스크 명확히 인식\n3. 습관/루틴 기반의 구체적 보완 행동 2가지 제시\n4. 속도와 신중함의 균형으로 결론",
                "core_points": [
                    "‘완벽주의’라는 흔한 단점도 ‘타임박싱과 50% 룰’이라는 실전 루틴으로 차별화",
                    "자기 객관화(Self-awareness) 역량",
                    "양산 현장에 필요한 스피드(Speed) 마인드셋 탑재"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="50" y="50" width="220" height="140" fill="#1e293b" stroke="#ef4444" stroke-width="2" rx="8"/>
  <text x="160" y="90" fill="#ef4444" font-size="15" font-weight="bold" text-anchor="middle">단점: 과도한 완벽주의</text>
  <text x="160" y="125" fill="#cbd5e1" font-size="13" text-anchor="middle">데이터 과몰입으로</text>
  <text x="160" y="150" fill="#cbd5e1" font-size="13" text-anchor="middle">초기 실행 지연 리스크</text>

  <path d="M 290 120 L 330 120" stroke="#38bdf8" stroke-width="3"/>

  <rect x="350" y="50" width="390" height="140" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="545" y="80" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">극복을 위한 2대 실천 루틴</text>
  
  <rect x="370" y="100" width="165" height="70" fill="#0f172a" stroke="#64748b" rx="4"/>
  <text x="452" y="125" fill="#38bdf8" font-size="12" text-anchor="middle">1. 타임박싱</text>
  <text x="452" y="150" fill="#94a3b8" font-size="11" text-anchor="middle">분석 시간 상한선 설정</text>

  <rect x="555" y="100" width="165" height="70" fill="#0f172a" stroke="#64748b" rx="4"/>
  <text x="637" y="125" fill="#f59e0b" font-size="12" text-anchor="middle">2. 50% 중간 공유</text>
  <text x="637" y="150" fill="#94a3b8" font-size="11" text-anchor="middle">조기 피드백 ➔ 신속 교정</text>
</svg>"""
        }
    ]
    return topics
