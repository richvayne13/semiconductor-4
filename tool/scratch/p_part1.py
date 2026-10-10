# -*- coding: utf-8 -*-
"""
인성 질문 20문항 데이터 생성 스크립트 (personality_data.py)
"""

def get_personality_topics():
    topics = [
        {
            "id": "p_01",
            "category": "personality",
            "category_label": "인성·협업·조직 가치",
            "number": 1,
            "title": "SK하이닉스 양산기술/소자 직무에 본인이 가장 적합한 이유",
            "core_keyword": ["데이터 기반 원인 규명", "설비 메커니즘 연계", "수율 개선 오너십"],
            "speech_1m30s": (
                "제가 해당 직무에 가장 적합한 이유는 '데이터 기반의 원인 규명 역량'과 '현장 설비 메커니즘에 대한 구조적 이해'를 함께 갖추고 있기 때문입니다. "
                "공정 미세화가 심화될수록 수율을 결정짓는 것은 막연한 가설이 아니라, 계측 데이터와 센서 신호 속에서 1% 미만의 미세한 이상 징후(Weak Signal)를 포착해 내는 정밀한 분석력입니다. "
                "저는 시계열 데이터 필터링과 잔차 분석을 통해 산포의 원인을 추적하고, 이를 설비의 기구적 거동 및 공정 챔버 조건과 1:1로 매칭하여 트러블슈팅을 완결해 본 경험이 있습니다. "
                "단순히 주어진 레시피를 운영하는 데 그치지 않고, 공정 산포와 설비 파라미터 간의 상관관계를 통계적으로 모델링하여 잠재 불량을 선제 차단하겠습니다. "
                "수율 한계 돌파를 최우선으로 삼아 현장 엔지니어링의 생산성을 극대화하는 실전형 인재로 기여하겠습니다."
            ),
            "deep_lecture": {
                "background": "SK하이닉스는 1b/1c nm DRAM 및 300단 이상 3D NAND 양산에서 극심한 공정 산포와 설비 다운타임 제어에 직면해 있습니다. 단순 이론가가 아닌 '데이터 분석력과 설비 하드웨어 이해를 융합한 엔지니어'를 최우선으로 선호합니다.",
                "action_principle": "1. 두괄식 핵심 역량 제시 (데이터 + 설비)\n2. 공정 미세화에 따른 양산기술의 본질(Weak Signal 포착) 연결\n3. 실무적 트러블슈팅 경험의 신뢰성 확보\n4. 수율 안정화 기여 포부로 완결",
                "core_points": [
                    "막연한 열정이 아닌 '정량적 분석 도구(잔차 분석, 시계열 필터링)' 언급",
                    "소프트웨어(데이터)와 하드웨어(챔버 기구 메커니즘)의 연결 강조",
                    "SK하이닉스의 핵심 KPI인 '수율(Yield)'과 '셋업 로스 최소화'에 직결"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="30" y="30" width="220" height="180" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="140" y="65" fill="#38bdf8" font-size="16" font-weight="bold" text-anchor="middle">1. 데이터 분석력</text>
  <text x="140" y="105" fill="#cbd5e1" font-size="13" text-anchor="middle">시계열 센서 신호 처리</text>
  <text x="140" y="130" fill="#cbd5e1" font-size="13" text-anchor="middle">1% 미만 약신호(Dip) 포착</text>
  <text x="140" y="155" fill="#cbd5e1" font-size="13" text-anchor="middle">동적 임계치 &amp; 잔차 분석</text>

  <path d="M 260 120 L 290 120" stroke="#f59e0b" stroke-width="3" marker-end="url(#arrow)"/>

  <rect x="300" y="30" width="220" height="180" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="410" y="65" fill="#f59e0b" font-size="16" font-weight="bold" text-anchor="middle">2. 설비 메커니즘 이해</text>
  <text x="410" y="105" fill="#cbd5e1" font-size="13" text-anchor="middle">챔버 기구부 구동 특성</text>
  <text x="410" y="130" fill="#cbd5e1" font-size="13" text-anchor="middle">RF 파워 / 가스 유량 산포</text>
  <text x="410" y="155" fill="#cbd5e1" font-size="13" text-anchor="middle">공정 파라미터 1:1 매칭</text>

  <path d="M 530 120 L 560 120" stroke="#10b981" stroke-width="3"/>

  <rect x="570" y="30" width="200" height="180" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="670" y="65" fill="#10b981" font-size="16" font-weight="bold" text-anchor="middle">3. 실전 양산 성과</text>
  <text x="670" y="105" fill="#cbd5e1" font-size="13" text-anchor="middle">수율(Yield) 골든 타임 사수</text>
  <text x="670" y="130" fill="#cbd5e1" font-size="13" text-anchor="middle">비계획 다운타임 제로화</text>
  <text x="670" y="155" fill="#cbd5e1" font-size="13" text-anchor="middle">SK하이닉스 양산 경쟁력</text>
</svg>"""
        },
        {
            "id": "p_02",
            "category": "personality",
            "category_label": "인성·협업·조직 가치",
            "number": 2,
            "title": "업무 피드백 후 상대방이 기분 상해 대화를 피할 때의 대처 방안",
            "core_keyword": ["감정 쿨다운 존중", "전달 태도 성찰", "목표 중심 1:1 대화"],
            "speech_1m30s": (
                "상대방의 침묵은 피드백 내용 자체보다 '전달 방식과 상황에서 느낀 감정적 불편함'에서 기인했을 가능성이 높습니다. 따라서 감정을 식히는 시간을 존중한 뒤, '전달 방식에 대한 자기 성찰'을 바탕으로 1:1 대화를 통해 신뢰를 회복하겠습니다. "
                "먼저 현장에서 즉각 따지거나 방치하지 않고 반나절 정도 생각할 여유를 주겠습니다. 그사이 제가 공개된 자리에서 말했거나, 상대의 노력에 대한 인정 없이 단점만 부각하지 않았는지 전달 태도를 점검하겠습니다. "
                "이후 단둘이 차 한잔을 나누는 편안한 자리에서 '지난번 말씀드릴 때 제 배려가 부족해 마음을 상하게 해드려 죄송하다'고 전달 방식에 대해 먼저 진심으로 사과하겠습니다. "
                "그리고 제 의도는 동료의 성과를 깎아내리려는 것이 아니라 팀의 완성도를 함께 높이고자 했던 것임을 설명하고, 상대방의 관점과 고충을 경청하여 공동의 목표로 다시 정렬하겠습니다."
            ),
            "deep_lecture": {
                "background": "협업이 절대적인 반도체 팹 라인에서는 동료 간 감정적 단절이 공정 인수인계 누락이나 대형 사고로 이어질 수 있습니다. 정답을 맞히는 것보다 '상대의 자존감을 지켜주며 협력 관계를 복원하는 기술'이 필수적입니다.",
                "action_principle": "1. 즉각 반응 금지 (Cool-down 타임 확보)\n2. 내용이 아닌 '태도/전달법'에 대한 우선 사과\n3. 비공개 1:1 안전한 대화 환경 구축\n4. 팀 목표(공동의 승리)로 재정렬",
                "core_points": [
                    "내 피드백이 무조건 옳다는 아집을 버리고 '태도의 오류'를 인정하는 성숙함",
                    "대화 단절을 방치하지 않고 주도적으로 복원하려는 적극성",
                    "협업의 본질인 '팀 성과 극대화'로 결론 유도"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <circle cx="120" cy="120" r="50" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
  <text x="120" y="115" fill="#f59e0b" font-size="14" font-weight="bold" text-anchor="middle">Step 1</text>
  <text x="120" y="135" fill="#cbd5e1" font-size="12" text-anchor="middle">감정 쿨다운</text>

  <line x1="180" y1="120" x2="260" y2="120" stroke="#64748b" stroke-width="2" stroke-dasharray="4"/>

  <circle cx="320" cy="120" r="50" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="320" y="115" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Step 2</text>
  <text x="320" y="135" fill="#cbd5e1" font-size="12" text-anchor="middle">전달 태도 성찰</text>

  <line x1="380" y1="120" x2="460" y2="120" stroke="#64748b" stroke-width="2" stroke-dasharray="4"/>

  <circle cx="520" cy="120" r="50" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
  <text x="520" y="115" fill="#a855f7" font-size="14" font-weight="bold" text-anchor="middle">Step 3</text>
  <text x="520" y="135" fill="#cbd5e1" font-size="12" text-anchor="middle">1:1 사과 &amp; 경청</text>

  <line x1="580" y1="120" x2="660" y2="120" stroke="#64748b" stroke-width="2" stroke-dasharray="4"/>

  <circle cx="700" cy="120" r="50" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
  <text x="700" y="115" fill="#10b981" font-size="14" font-weight="bold" text-anchor="middle">Step 4</text>
  <text x="700" y="135" fill="#cbd5e1" font-size="12" text-anchor="middle">팀 목표 정렬</text>
</svg>"""
        },
        {
            "id": "p_03",
            "category": "personality",
            "category_label": "인성·협업·조직 가치",
            "number": 3,
            "title": "팀 프로젝트 중 무임승차자(Free-rider)가 발생했을 때의 해결 경험 및 대처법",
            "core_keyword": ["원인 분석 경청", "역할 세분화 R&R", "성취 경험 유도"],
            "speech_1m30s": (
                "무임승차를 단순히 태만으로 규정하고 배제하기보다, '업무 난이도에 대한 두려움이나 역할 불명확성'에서 기인하지 않았는지 원인을 먼저 파악하겠습니다. "
                "실제 팀 프로젝트 당시 한 팀원이 과제를 전혀 진행하지 못해 전체 일정이 지연된 적이 있었습니다. 저는 공개적으로 비난하지 않고 1:1로 대화를 나누며, 해당 팀원이 분석 도구 사용에 미숙해 어디서부터 시작할지 몰라 위축되어 있음을 확인했습니다. "
                "이에 전체 모듈을 통째로 맡기는 대신, 데이터 전처리 및 레퍼런스 정리 등 상대의 강점에 맞는 세부 단위로 R&R(역할과 책임)을 재조정했습니다. "
                "또한 초기 단계에 협업 툴 사용법을 함께 실습하며 작은 성취를 맛보게 돕자, 이후에는 주도적으로 데이터를 정리해 팀에 기여했습니다. "
                "팀원의 숨은 병목을 찾아 시스템적으로 해소해 줄 때 진정한 원팀(One-team)의 시너지가 발휘된다고 믿습니다."
            ),
            "deep_lecture": {
                "background": "팀 단위 성과 평가가 중요한 조직에서는 무임승차자를 배제(Exclude)하거나 대신 떠안는(Carry) 양극단 모두 조직에 해롭습니다. '역할을 재설계하여 끝까지 끌고 가는 인클루시브 리더십'을 평가합니다.",
                "action_principle": "1. 인격적 비난 대신 역량적 병목 확인\n2. 1:1 소통을 통한 심리적 안전감 부여\n3. R&R 미세 분할(Micro-tasking)로 진입 장벽 완화\n4. 작은 성공 경험을 통한 내적 동기 부여",
                "core_points": [
                    "감정적 배척이 아닌 문제 해결적 접근법",
                    "R&R(Role & Responsibility) 재설계 역량",
                    "조직 내 이탈자를 시스템 안으로 복귀시키는 포용력"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="50" y="40" width="200" height="160" fill="#1e293b" stroke="#ef4444" stroke-width="2" rx="8"/>
  <text x="150" y="80" fill="#ef4444" font-size="15" font-weight="bold" text-anchor="middle">기존 문제 상황</text>
  <text x="150" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">거대 업무 통배정</text>
  <text x="150" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">도구 미숙 ➔ 위축</text>
  <text x="150" y="170" fill="#cbd5e1" font-size="13" text-anchor="middle">무임승차 오인 발생</text>

  <path d="M 270 120 L 320 120" stroke="#38bdf8" stroke-width="3"/>

  <rect x="340" y="40" width="410" height="160" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="545" y="75" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">해결 솔루션: Micro-R&amp;R 재배치</text>
  <rect x="360" y="100" width="115" height="75" fill="#0f172a" stroke="#64748b" rx="4"/>
  <text x="417" y="130" fill="#38bdf8" font-size="12" text-anchor="middle">1. 원인 경청</text>
  <text x="417" y="155" fill="#94a3b8" font-size="11" text-anchor="middle">병목 확인</text>

  <rect x="490" y="100" width="115" height="75" fill="#0f172a" stroke="#64748b" rx="4"/>
  <text x="547" y="130" fill="#f59e0b" font-size="12" text-anchor="middle">2. 작업 분할</text>
  <text x="547" y="155" fill="#94a3b8" font-size="11" text-anchor="middle">강점 매칭</text>

  <rect x="620" y="100" width="115" height="75" fill="#0f172a" stroke="#64748b" rx="4"/>
  <text x="677" y="130" fill="#10b981" font-size="12" text-anchor="middle">3. 성공 경험</text>
  <text x="677" y="155" fill="#94a3b8" font-size="11" text-anchor="middle">자발적 몰입</text>
</svg>"""
        },
        {
            "id": "p_04",
            "category": "personality",
            "category_label": "인성·협업·조직 가치",
            "number": 4,
            "title": "본인의 원칙이나 소신과 팀의 결정/방향성이 충돌했을 때의 조율 방식",
            "core_keyword": ["공학적 데이터 근거", "충분한 의견 개진", "결정 후 100% 헌신"],
            "speech_1m30s": (
                "의사결정 전에는 '데이터에 기반하여 소신껏 치열하게 토론'하되, 팀의 최종 합의가 이루어진 후에는 '개인 의견을 내려놓고 결정된 방향에 100% 헌신(Commit)'하는 것이 저의 원칙입니다. "
                "엔지니어로서 자신의 관점을 갖는 것은 중요하지만, 그것은 직관이 아닌 객관적 검증 데이터로 입증되어야 합니다. "
                "따라서 팀의 결정과 제 생각이 다를 때는 감정적으로 고집부리지 않고, 제 제안의 리스크와 기대효과를 정량 수치로 시뮬레이션하여 팀 회의에서 객관적으로 공유하겠습니다. "
                "그럼에도 불구하고 전체 프로젝트 일정이나 조직의 전략적 우선순위에 의해 다른 대안이 최종 채택된다면, 제 주장을 뒤로하고 팀이 선택한 방안이 반드시 성공할 수 있도록 제 위치에서 빈틈없이 실행을 지원하겠습니다. "
                "원팀의 성공이 곧 개인의 성공보다 항상 우선하기 때문입니다."
            ),
            "deep_lecture": {
                "background": "인텔의 'Disagree and Commit(치열하게 반론하되, 결정되면 전적으로 헌신하라)' 원칙과 SK의 SUPEX 추구 철학이 맞닿아 있습니다. 우유부단한 무조건적 복종도 안 되지만, 결정 후 뒤에서 불평하는 태도는 치명적입니다.",
                "action_principle": "1. 결정 전: 객관적 데이터 기반의 건전한 대안 제시\n2. 조율 중: 전체 최적화(조직 KPI) 관점에서의 시야 확대\n3. 결정 후: 깔끔한 승복과 전력투구 실행",
                "core_points": [
                    "데이터 중심의 논리적 소신 피력",
                    "팀의 상위 목표(Overall Optimization) 이해력",
                    "결정된 사항에 대한 강력한 실행력과 충성도"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="60" y="50" width="300" height="140" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="8"/>
  <text x="210" y="90" fill="#38bdf8" font-size="16" font-weight="bold" text-anchor="middle">[ 결정 전 ] 치열한 논쟁</text>
  <text x="210" y="125" fill="#cbd5e1" font-size="13" text-anchor="middle">객관적 데이터 기반 반론</text>
  <text x="210" y="150" fill="#cbd5e1" font-size="13" text-anchor="middle">리스크 &amp; 기대효과 정량 비교</text>

  <path d="M 380 120 L 420 120" stroke="#f59e0b" stroke-width="4"/>

  <rect x="440" y="50" width="300" height="140" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="590" y="90" fill="#10b981" font-size="16" font-weight="bold" text-anchor="middle">[ 결정 후 ] 100% 헌신</text>
  <text x="590" y="125" fill="#cbd5e1" font-size="13" text-anchor="middle">사적 고집 배제 &amp; 완전 승복</text>
  <text x="590" y="150" fill="#cbd5e1" font-size="13" text-anchor="middle">채택된 방안의 성공에 집중</text>
</svg>"""
        },
        {
            "id": "p_05",
            "category": "personality",
            "category_label": "인성·협업·조직 가치",
            "number": 5,
            "title": "가장 크게 실패했던 경험과 그 실패를 통해 배운 교훈",
            "core_keyword": ["가설 검증 미흡", "근본 원인 5-Why", "재발 방지 시스템화"],
            "speech_1m30s": (
                "과거 프로젝트에서 충분한 예비 검증 없이 가설에만 의존해 공정 파라미터를 변경했다가, 샘플 전체에 불량이 발생해 일정이 2주 지연된 실패 경험이 있습니다. "
                "당시 수치를 개선하겠다는 조급한 마음에 파라미터 간의 상호 간섭 효과를 면밀히 시뮬레이션하지 않았던 것이 패인이었습니다. "
                "저는 실패를 숨기지 않고 팀원들에게 솔직히 공유한 뒤, 왜 실패했는지 5-Why 기법으로 근본 원인을 파고들었습니다. 그 결과 레시피 변경 전 반드시 거쳐야 할 '사전 체크리스트'와 '소규모 시범 테스트(DoE)' 프로세스가 부재했음을 발견했습니다. "
                "이에 재발 방지를 위한 단계별 검증 프로토콜을 직접 수립하여 문서화했고, 이후 동일한 오류 없이 프로젝트를 최종 완수했습니다. "
                "이 경험을 통해 엔지니어의 확신은 감이 아니라 철저한 데이터와 시스템적 검증으로 증명되어야 함을 뼈저리게 배웠습니다."
            ),
            "deep_lecture": {
                "background": "실패 경험 질문의 핵심은 '실패 자체'가 아니라 '실패를 마주하는 정직성'과 '원인을 분석하여 시스템적 재발 방지책을 세우는 역량'입니다.",
                "action_principle": "1. 명확한 실패 상황과 본인의 실수 솔직 인정\n2. 감정적 자책이 아닌 냉정한 원인 분석(5-Why)\n3. 개인의 조심에 그치지 않고 '시스템/프로토콜 개선'으로 승화\n4. 엔지니어링 마인드셋의 성숙함 입증",
                "core_points": [
                    "치명적 도덕적 결함이 아닌 '공학적 판단 착오와 조급함'을 소재로 선정",
                    "동료 탓을 하지 않고 주도적으로 복구한 책임감",
                    "재발 방지 프로세스(Checklist, DoE) 구축 성과"
                ]
            },
            "svg_diagram": """<svg viewBox="0 0 800 240" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="240" fill="#0f172a" rx="12"/>
  <rect x="40" y="45" width="210" height="150" fill="#1e293b" stroke="#ef4444" stroke-width="2" rx="8"/>
  <text x="145" y="85" fill="#ef4444" font-size="15" font-weight="bold" text-anchor="middle">1. 실패 발생</text>
  <text x="145" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">조급한 가설 변경</text>
  <text x="145" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">샘플 불량 &amp; 지연</text>

  <path d="M 260 120 L 295 120" stroke="#64748b" stroke-width="2"/>

  <rect x="305" y="45" width="210" height="150" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="8"/>
  <text x="410" y="85" fill="#f59e0b" font-size="15" font-weight="bold" text-anchor="middle">2. 원인 심층 분석</text>
  <text x="410" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">5-Why 기법 적용</text>
  <text x="410" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">사전 검증 부재 식별</text>

  <path d="M 525 120 L 560 120" stroke="#64748b" stroke-width="2"/>

  <rect x="570" y="45" width="200" height="150" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="8"/>
  <text x="670" y="85" fill="#10b981" font-size="15" font-weight="bold" text-anchor="middle">3. 재발 방지 자산화</text>
  <text x="670" y="120" fill="#cbd5e1" font-size="13" text-anchor="middle">체크리스트 수립</text>
  <text x="670" y="145" fill="#cbd5e1" font-size="13" text-anchor="middle">DoE 프로토콜 표준화</text>
</svg>"""
        }
    ]
    return topics
