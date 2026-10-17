# -*- coding: utf-8 -*-
import json
import re
import shutil

# 22개 전체 인성 문항 각각에 대한 [답변 1 (speech_1m30s)] 및 [답변 2 (speech_alt)] 정의
# 모든 답변은 1분 실전 호흡(220~320자) 및 2가지 핵심 근거/실행(첫째/둘째) 구조로 완비
dual_personality_data = {
    "p_01": {
        "speech_1m30s": "제가 양산기술 직무에 가장 적합한 이유는 '데이터 기반 원인 규명 역량'과 '설비 하드웨어 이해도'를 겸비했기 때문입니다. 첫째, 시계열 데이터 잔차 분석을 통해 공정 산포 속 1% 미만의 미세 이상 신호를 포착하고 핵심 불량 인자를 통계적으로 특정해 본 경험이 있습니다. 둘째, 이상 원인을 단순 레시피 수치가 아닌 챔버 내부의 물리·기구적 거동과 1:1로 매칭하여 근본적인 트러블슈팅을 완결할 수 있습니다. 데이터와 설비를 아우르는 시각으로 수율 안정화에 기여하겠습니다.",
        "speech_alt": "양산기술 엔지니어로서 저의 강점은 '현장 중심의 문제 해결력'과 '반복 불량을 막는 시스템화 역량'입니다. 첫째, 학부 연구 및 프로젝트에서 불량 발생 시 현장의 장비 로그와 작업 조건을 직접 대조하며 가설을 검증하는 실전 훈련을 거쳤습니다. 둘째, 문제를 일회성 조치로 끝내지 않고 공정 파라미터 간의 상관관계를 표준 매뉴얼과 자동 알림 파이프라인으로 구축해 재발률을 0%로 낮췄습니다. 집요한 현장 실행력으로 SK하이닉스의 무결점 양산을 뒷받침하겠습니다."
    },
    "p_02": {
        "speech_1m30s": "SK하이닉스에 지원한 이유는 세계 최고 수준의 기술 리더십과 한계를 돌파하는 도전 DNA에 깊이 공감했기 때문입니다. 첫째, 독보적인 MR-MUF 패키징과 초고속 TSV 적층 기술로 글로벌 HBM 시장을 제패하며 AI 메모리 패러다임을 주도하는 기술력에 매료되었습니다. 둘째, 실패를 두려워하지 않고 데이터와 집념으로 수율 한계를 넘어서는 조직 문화 속에서 엔지니어로서 가장 크게 성장할 수 있다고 확신했습니다. 1b/1c 나노 DRAM과 차세대 HBM 양산 최전선에서 원가와 수율 경쟁력을 높이는 주역이 되겠습니다.",
        "speech_alt": "급변하는 AI 반도체 시장에서 압도적인 양산 경쟁력으로 승부하는 SK하이닉스의 일원이 되고자 지원했습니다. 첫째, 아무리 뛰어난 소자 설계라도 수만 장의 웨이퍼에서 균일한 수율을 확보하는 양산 기술이 뒷받침되어야만 시장 1위를 지킬 수 있다고 믿습니다. 둘째, 부서 간 벽을 허물고 원팀(One-Team)으로 난제를 해결하는 SK하이닉스의 협업 문화는 제가 추구하는 엔지니어링 가치관과 정확히 일치합니다. 현장의 미세 산포를 빈틈없이 제어하여 글로벌 메모리 1위 위상을 굳건히 지키겠습니다."
    },
    "p_03": {
        "speech_1m30s": "원인 불명의 데이터 산포를 잡기 위해 3주간 50개 이상의 공정 변수를 전수 검증하여 수율을 15% 끌어올린 경험이 있습니다. 첫째, 초기 가설이 연이어 빗나갔을 때 좌절하지 않고 공정 단계별 데이터 로깅 주기를 세분화하여 시계열 잔차 분석을 처음부터 다시 수행했습니다. 둘째, 분석을 통해 특정 온도 구간에서 발생하는 비선형 센서 노이즈가 진짜 원인임을 밝혀내고 보정 알고리즘을 적용해 산포를 완벽히 잡았습니다. 끝까지 데이터로 답을 찾아내는 집요함이 저의 가장 큰 무기입니다.",
        "speech_alt": "장비 노후화로 인해 반복되던 박막 두께 불균일 문제를 해결하기 위해 한 달간 매일 장비 로그와 하드웨어 부품을 대조하며 매달린 경험이 있습니다. 첫째, 기존 관행대로 레시피 시간만 늘리는 임시방편을 거부하고 가스 샤워헤드의 미세 막힘과 배기 밸브 압력 편차를 전수 측정했습니다. 둘째, 확보한 정량 데이터를 바탕으로 예방정비(PM) 주기와 클리닝 프로토콜을 재설계하여 두께 균일도를 98% 이상으로 복원했습니다. 타협하지 않는 끈기로 양산 한계를 돌파하겠습니다."
    },
    "p_04": {
        "speech_1m30s": "프로젝트 중간 평가에서 기존 방식의 한계를 데이터로 직시하고, 과감한 방향 전환(Pivot)을 통해 납기와 성능을 동시에 사수한 경험이 있습니다. 첫째, 목표 성능 미달을 확인한 즉시 매몰 비용에 연연하지 않고 기존 설계 수정안과 신규 아키텍처 단순화 대안의 리스크·소요시간을 정량 비교했습니다. 둘째, 대체 모델이 수율 확보와 일정 단축 면에서 우월함을 실험 데이터로 입증해 팀원들을 설득하고 역할을 병렬로 재배치해 기한 내 목표를 100% 달성했습니다.",
        "speech_alt": "공정 최적화 과제 중 3주간 개발하던 A 코팅 방식에서 고온 미세 박리 현상을 발견했을 때, 마감 열흘을 앞두고 과감히 B 플라즈마 표면 처리로 전환한 경험이 있습니다. 첫째, 당장의 제출보다 양산 신뢰성 통과가 본질임을 DoE 불량 예측 데이터로 시각화하여 현상 유지를 원하던 팀원들을 설득했습니다. 둘째, 부족한 시간을 만회하기 위해 실험군을 2교대 병렬 검증 체계로 재편하여 단 5일 만에 박리율 0%를 달성했습니다. 데이터를 믿고 결단하는 실행력으로 기여하겠습니다."
    },
    "p_05": {
        "speech_1m30s": "동료가 피드백 후 대화를 피한다면 감정적 맞대응을 배제하고 '전달 태도 성찰'과 '1:1 신뢰 회복'으로 접근하겠습니다. 첫째, 반나절의 감정 쿨다운 시간을 존중한 뒤 편안한 1:1 자리에서 제 표현이 거칠어 마음을 상하게 해드린 점에 대해 먼저 진심으로 사과하겠습니다. 둘째, 만약 이후에도 관계가 회복되지 않는다면 감정이 섞인 사적 의견 대신 표준작업서(SOP)와 정량 데이터 지표를 매개로 소통하고, 필요시 선임자의 객관적 업무 조율을 요청해 팀 공정 리스크를 예방하겠습니다.",
        "speech_alt": "피드백으로 인해 동료와의 관계가 경색되었을 때는 '의도와 감정의 분리' 및 '공통 목표 환기'를 통해 해법을 찾겠습니다. 첫째, 비공개 자리에서 동료의 노력을 먼저 인정하고 제 피드백이 개인에 대한 지적이 아니라 팀 산출물의 완성도를 높이기 위한 것이었음을 차분히 설명하며 고충을 경청하겠습니다. 둘째, 그럼에도 진전이 없다면 업무 인터페이스를 체크리스트 기반으로 명확히 문서화하여 감정 소모 없이 상호 작업이 원활히 진행되도록 시스템적 소통 체계를 구축하겠습니다."
    },
    "p_06": {
        "speech_1m30s": "신규 입사 후 팀원들이 각자 따로 일하는 분위기라면, 성급한 지적 대신 '심리적 안전감 형성'과 '정보 투명화'로 협업의 물꼬를 트겠습니다. 첫째, 비공식 티타임과 현장 관찰을 통해 선배님들의 업무 특성과 파편화된 원인을 먼저 겸손히 경청하겠습니다. 둘째, 장비 예약 현황이나 트러블 이력을 한눈에 볼 수 있는 공유 시트를 자발적으로 정리해 배포하고 주간 15분 스탠드업 미팅을 제안하여, 협업할 때 내 업무가 편해진다는 작은 성공 경험(Small Win)을 퍼뜨리겠습니다.",
        "speech_alt": "팀 내 협업이 부족한 상황에서는 막내로서 '공통 병목 업무 솔선수범'과 '공정 간 가교(Bridge) 역할'을 통해 자연스러운 원팀 문화를 만들겠습니다. 첫째, 각 담당자가 바빠서 놓치기 쉬운 공통 계측 데이터 정리나 부품 재고 파악을 먼저 도맡아 선배님들의 신뢰를 얻겠습니다. 둘째, 선후 공정 인터페이스가 맞닿는 이슈에서 양측 데이터를 보기 쉽게 요약해 전달하는 윤활유 역할을 수행함으로써 팀원들이 자연스럽게 소통하고 시너지를 내도록 유도하겠습니다."
    },
    "p_07": {
        "speech_1m30s": "수율·납기와 품질이 충돌하는 위기 상황에서 저의 최우선 원칙은 '품질 무타협'과 '영향 범위 국소화'입니다. 첫째, 잠재 결함을 묵인한 출하는 고객사 리콜과 막대한 신뢰 손실로 이어지므로, 이상 징후가 포착된 영향 로트(Lot)와 의심 챔버를 즉시 보류(Hold)하여 불량 유출을 차단하겠습니다. 둘째, 전체 라인 셧다운으로 인한 캐파 손실을 막기 위해 정상 챔버로 백업 라우팅을 즉각 가동하고, 유관 부서에 팩트 데이터를 투명하게 공유하여 단계적 출하 대안을 실행하겠습니다.",
        "speech_alt": "납기 압박 속에서도 품질 마지노선을 지키면서 캐파 손실을 최소화하는 '데이터 기반 2단계 대응'을 실행하겠습니다. 첫째, 결함 로트의 계측 로그와 공정 파라미터를 즉시 추출해 불량 영향도를 정량 평가하고, 신뢰성 기준에 미달하는 제품은 단호히 격리하겠습니다. 둘째, 설비·품질 부서와 즉시 태스크포스를 꾸려 소규모 DoE로 근본 원인을 빠르게 교정하고 인터록을 재설정한 뒤 가동률을 끌어올림으로써, 고객 신뢰와 양산 캐파를 동시에 방어하겠습니다."
    },
    "p_08": {
        "speech_1m30s": "중간 점검에서 목표 미달 징후를 발견한다면 혼자 끌어안지 않고 '신속한 조기 공론화'와 '스코프 우선순위 재조정'을 실행하겠습니다. 첫째, 마감 임박 후의 실패 통보가 가장 위험하므로 지연의 핵심 병목을 기술 난제와 리소스 부족 등으로 정량화하여 팀장님과 팀원들에게 즉시 투명하게 공유하겠습니다. 둘째, 전체 납기를 지키기 위해 반드시 완수해야 할 필수(Must-have) 과제에 팀 가용 리소스를 집중 재배치하고 부가 과제는 후속 릴리즈로 분리하는 현실적 플랜 B로 목표를 완수하겠습니다.",
        "speech_alt": "팀 목표 달성에 적신호가 켜졌을 때는 '병목 구간의 공학적 분해'와 '협업 프로세스 단축'으로 골든 타임을 확보하겠습니다. 첫째, 현재까지 축적된 실험 데이터를 역추적하여 목표치와의 갭(Gap)을 유발하는 가장 큰 지배 인자 1~2개를 특정하고 불필요한 시행착오를 즉시 중단하겠습니다. 둘째, 선배 엔지니어 및 유관 부서에 조기 기술 자문을 요청해 검증된 레퍼런스 조건을 빠르게 도입하고, 일일 단위 마일스톤 점검으로 실행 속도를 높여 목표를 기한 내 달성하겠습니다."
    },
    "p_09": {
        "speech_1m30s": "상사로부터 품질 기준을 우회하라는 지시를 받는다면, 감정적 반발 대신 '객관적 리스크 데이터 건의'와 '컴플라이언스 준수'로 대처하겠습니다. 첫째, 지시의 배경 맥락을 먼저 확인하되 품질 우회 시 발생할 수 있는 수율 손실, 고객 클레임, 법적 리스크를 정량 데이터와 사내 규정에 근거해 1:1로 정중히 재확인하겠습니다. 둘째, 그럼에도 회사와 고객에 치명적 피해를 주는 부당 지시가 강행된다면 사내 공식 윤리·품질 보고 절차에 따라 차상위자에게 객관적 팩트를 보고해 품질 원칙을 사수하겠습니다.",
        "speech_alt": "비합리적이거나 규정에 어긋나는 지시에 직면했을 때는 '원칙 사수'와 '상사의 목표를 충족하는 합법적 대안(Plan B) 제시'로 풀어가겠습니다. 첫째, 품질 기준을 타협할 수 없는 공학적 이유를 명확히 말씀드려 조직 전체가 입을 수 있는 장기적 리스크를 방어하겠습니다. 둘째, 단순한 거절에 그치지 않고 상사분이 우려하시는 납기나 수율 목표를 정상적인 규정 테두리 안에서 달성할 수 있는 공정 조건 최적화 및 백업 설비 활용 대안을 함께 보고하여 문제를 해결하겠습니다."
    },
    "p_10": {
        "speech_1m30s": "오후 회의가 임박해 설득할 시간이 부족하다면, 상사분의 풍부한 실무 연륜이 담긴 'A안을 최우선으로 완벽히 준비'하되 'B안을 백업 카드로 병행 정리'하겠습니다. 첫째, 현장 경험이 많은 상사분의 판단이 거시적 맥락에서 옳을 가능성이 높으므로 당면한 회의의 성공을 위해 A안의 논리와 데이터를 빈틈없이 보강하겠습니다. 둘째, 제가 구상한 B안의 핵심 데이터와 잠재 리스크 보완 포인트는 1페이지 별첨 메모로 준비해 두었다가 회의 중 추가 대안이 필요할 때 유연하게 제시해 팀에 기여하겠습니다.",
        "speech_alt": "회의 직전 상사분의 A안과 제 B안이 충돌할 때는 '조직 의사결정 속도에 맞춘 선(先) 헌신'과 '데이터 기반의 사후 보완'으로 대응하겠습니다. 첫째, 촉박한 상황에서 논쟁으로 준비 시간을 허비하지 않고 상사분의 A안이 회의에서 설득력을 얻도록 관련 지표와 예상 질의응답을 철저히 준비하겠습니다. 둘째, 회의 종료 후 여유 있는 시점에 A안 실행 시 발생할 수 있는 세부 리스크를 완화할 보조 수단으로서 B안의 장점을 접목한 절충안을 정중히 건의하여 완성도를 높이겠습니다."
    },
    "p_11": {
        "speech_1m30s": "신제품 개발 초반에 일정이 정리되지 않아 혼란스럽다면, 'WBS 기반의 업무 분해'와 '크리티컬 패스 시각화'로 팀의 기준점을 세우겠습니다. 첫째, 개발 과제를 소자 설계, 단위 공정 평가, 신뢰성 검증 등 세부 단위로 쪼개고 작업 간 선후 의존성(Dependency)을 연결해 전체 납기를 좌우하는 핵심 병목 경로를 도출하겠습니다. 둘째, 이를 공유 칸반 보드와 간트 차트로 시각화하여 팀원 누구나 실시간 진척도와 자신의 우선순위를 명확히 인지하고 개발에 몰입할 수 있도록 지원하겠습니다.",
        "speech_alt": "초기 프로젝트의 일정 혼란을 조기에 잡기 위해 '인풋-아웃풋 마감 역산(Backward Scheduling)'과 '주간 마일스톤 동기화'를 추진하겠습니다. 첫째, 최종 양산 이관 목표일로부터 역산하여 각 공정 단계별로 반드시 산출되어야 할 데이터 규격과 마감 기한을 체크리스트로 명문화하겠습니다. 둘째, 제가 자발적으로 일정 관리 총무를 맡아 매주 짧은 싱크 미팅에서 지연 리스크를 조기 식별하고 선배님들의 의사결정을 지원함으로써 체계적인 프로젝트 운영에 기여하겠습니다."
    },
    "p_12": {
        "speech_1m30s": "팀 실수로 생산이 중단된 위기에서는 소모적인 책임 공방을 즉시 멈추고 '선(先) 라인 정상화'와 '후(後) 시스템적 재발 방지'에 집중하겠습니다. 첫째, 네 탓 공방은 골든 타임을 낭비할 뿐이므로 영향 로트를 즉시 격리하고 설비 인터록과 공정 조건을 점검해 라인을 안전하게 복구하는 데 전력을 다하겠습니다. 둘째, 복구 후에는 특정 개인을 질책하는 대신 5-Why 분석으로 표준작업서(SOP)의 모호함이나 더블 체킹 부재 등 시스템의 허점을 찾아 Fool-proof 인터록으로 자산화하겠습니다.",
        "speech_alt": "생산 중단 사고 시 가장 중요한 것은 '심리적 안전감 보호를 통한 정확한 원인 규명'과 '2차 피해 차단'입니다. 첫째, 현장에서 책임 추궁 분위기를 진정시키고 사실관계(장비 로그, 작업 시간, 변경점)만을 객관적으로 수집하여 후속 공정으로의 오염 확산을 즉각 차단하겠습니다. 둘째, 사고 원인을 개인의 부주의가 아닌 '누구나 실수할 수 있었던 환경적 결함'으로 정의하고, 교대 인수인계 프로토콜과 자동 검증 알람을 고도화하여 팀의 양산 신뢰성을 한 단계 끌어올리겠습니다."
    },
    "p_13": {
        "speech_1m30s": "타 부서와의 협업에서 소통 부재로 일정이 지연된다면, '상위 공통 KPI 정렬'과 '표준 업무 인터페이스 문서화'로 해결하겠습니다. 첫째, 각 부서의 입장이 다르더라도 '최종 양산 수율과 출하 납기 사수'라는 회사 전체의 상위 목표가 같음을 환기하여 이해관계를 한 방향으로 정렬하겠습니다. 둘째, 구두나 메신저 소통의 누락을 막기 위해 데이터 인수인계 양식과 마감 기한을 명시한 표준 인터페이스 시트를 구축하고 주간 15분 정례 싱크로 병목을 선제 해소하겠습니다.",
        "speech_alt": "부서 간 소통 병목은 서로 사용하는 기술 용어와 우선순위가 달라 발생하므로, '역지사지 현장 소통'과 '실시간 공유 대시보드'로 돌파하겠습니다. 첫째, 이메일로만 독촉하기보다 상대 부서 담당자를 직접 찾아가 그들이 겪는 설비 부하나 인력 제약을 먼저 경청하고 우리 부서가 도울 수 있는 데이터 전처리 지원을 선제안하겠습니다. 둘째, 양 부서가 공동으로 확인하는 진척도 현황판을 운영해 일정 지연 징후를 초기에 함께 발견하고 조율하는 원팀 협업 체계를 정착시키겠습니다."
    },
    "p_14": {
        "speech_1m30s": "신규 입사자로서 팀 내 업무 경계가 모호할 때는 관망하지 않고 '공통 기초 업무 솔선수범'과 '주도적 R&R 확립'으로 기여하겠습니다. 첫째, 회의록 액션 아이템 정리, 방대한 계측 데이터 전처리, 트러블 이력 아카이빙 등 바쁜 선배님들이 미처 손대지 못하는 사각지대 업무를 자발적으로 도맡겠습니다. 둘째, 이 과정에서 전체 공정 흐름과 프로젝트 맥락을 빠르게 파악한 뒤 선배님들께 제가 전담할 수 있는 세부 분석 파트를 구체적으로 제안하여 든든한 1인분의 엔지니어로 자리잡겠습니다.",
        "speech_alt": "개선 프로젝트에서 각자의 역할이 불분명할 때는 신입의 시각을 살려 '업무 현황 가시화'와 '빠른 실행 지원'으로 팀의 구심점을 돕겠습니다. 첫째, 현재 진행 중인 세부 과제들과 미할당된 이슈 목록을 한 장의 매트릭스 표로 일목요연하게 정리해 팀 미팅 자료로 공유하겠습니다. 둘째, 손이 많이 가는 샘플 계측이나 기초 시뮬레이션 검증을 제가 먼저 자원하여 빠르게 처리함으로써, 선배님들이 핵심 의사결정에 집중할 수 있도록 돕고 팀의 전체 속도를 높이겠습니다."
    },
    "p_15": {
        "speech_1m30s": "신규 팀원의 적응이 더디고 속도가 느리다면, 태만으로 단정하기보다 '심리적 안전감 부여'와 '업무 미세 분할(Micro-tasking)'로 온보딩을 돕겠습니다. 첫째, 1:1 티타임을 통해 저의 신입 시절 시행착오를 먼저 공유하며 모르는 것을 편안하게 질문할 수 있는 안전한 분위기를 만들겠습니다. 둘째, 방대한 업무를 통째로 맡기지 않고 반나절 단위로 완결 가능한 작은 과제로 쪼개어 페어 워크(Pair-work)로 함께 시연함으로써, 작은 성공 경험을 통해 자신감과 속도를 동시에 끌어올리겠습니다.",
        "speech_alt": "적응에 어려움을 겪는 동료에게는 '체계적인 실무 치트시트(가이드) 제공'과 '강점 기반의 역할 매칭'으로 실질적인 성장을 지원하겠습니다. 첫째, 현장에서 자주 쓰이는 설비 약어, 데이터 추출 경로, 보고서 양식을 한눈에 볼 수 있는 1페이지 실무 가이드를 만들어 전달해 시행착오 시간을 줄여주겠습니다. 둘째, 동료가 어느 단계에서 병목을 겪는지 세심히 관찰하여 강점이 있는 파트부터 성취감을 느끼게 돕고, 점진적으로 업무 범위를 넓혀 원팀의 주력으로 함께 성장하겠습니다."
    },
    "p_16": {
        "speech_1m30s": "프로젝트 중 동료와 업무 방식이 충돌한다면, 감정을 배제하고 '프로젝트 목표 기준의 정량 비교'와 '소규모 파일럿 검증'으로 해결하겠습니다. 첫째, 내 방식을 고집하기 전에 동료가 해당 방식을 제안한 공학적 의도와 기대 효과를 끝까지 경청하며 존중하겠습니다. 둘째, 개인의 선호가 아닌 정확도, 리드타임, 공정 리스크 3가지 지표로 양측 안을 객관적으로 비교하고, 우열을 가리기 어렵다면 작은 샘플로 A/B 파일럿 테스트를 수행해 실제 데이터로 최선의 결론을 도출하겠습니다.",
        "speech_alt": "동료와의 의견 대립은 산출물의 완성도를 높일 수 있는 건강한 과정이므로, '장점 융합(Hybrid) 대안 도출'로 시너지를 내겠습니다. 첫째, 양측 의견이 충돌하는 핵심 원인이 '속도 우선'인지 '안정성 우선'인지 기준점의 차이를 먼저 명확히 정의하겠습니다. 둘째, 동료 방식의 빠른 처리 속도와 제 방식의 에러 검증 로직을 결합한 제3의 하이브리드 절충안을 설계하여, 감정적 앙금 없이 두 마리 토끼를 모두 잡는 원팀 의사결정을 이끌어내겠습니다."
    },
    "p_17": {
        "speech_1m30s": "낯선 설비와 빠른 현장 호흡에 적응이 어렵다면, 조급함을 버리고 '표준(SOP)·경청 기반의 현장 언어 습득'과 '일일 오답노트 루틴'으로 돌파하겠습니다. 첫째, 표준작업지도서(SOP)와 안전 수칙, 과거 설비 트러블 이력을 철저히 숙지하고 베테랑 작업자 및 선배님들의 점검 동선을 겸손히 경청해 이론과 현장의 간극을 줄이겠습니다. 둘째, 매일 퇴근 전 그날 배운 설비 특성과 실수를 오답노트로 자산화하고 기초 데이터 정리부터 완벽히 수행해 조기에 신뢰받는 현장형 엔지니어가 되겠습니다.",
        "speech_alt": "생산 현장 초기 적응의 어려움은 '현장 밀착형 행동 루틴'과 '작은 기여(Small Win) 실천'으로 빠르게 극복하겠습니다. 첫째, 책상 앞 모니터에만 머물지 않고 하루 두 번 이상 직접 팹 라인과 설비 현장을 발로 뛰며 장비의 정상 가동음과 센서 수치 범위를 몸으로 체화하겠습니다. 둘째, 교대 인수인계 자료 시각화나 일일 모니터링 시트 정리처럼 신입으로서 즉시 도움을 줄 수 있는 일부터 빈틈없이 완수하여 선배님들과 자연스럽게 융화되고 현장 적응력을 높이겠습니다."
    },
    "p_18": {
        "speech_1m30s": "부서 간 갈등은 각자 맡은 KPI를 책임감 있게 수행하는 과정에서 발생하는 자연스러운 현상이므로, '상대 부서 제약 경청'과 '상위 공동 목표 기반 데이터 조율'로 해결하겠습니다. 첫째, 우리 입장만 강요하기 전에 설비 부하나 일정 압박 등 상대 부서의 현실적 고충을 먼저 경청하고 공감하겠습니다. 둘째, 판단 기준을 개별 부서의 유불리가 아닌 '라인 전체의 최종 수율과 납기'라는 상위 KPI로 정렬하고 조건별 손익을 정량 데이터로 시뮬레이션해 윈윈(Win-Win) 절충안을 도출하겠습니다.",
        "speech_alt": "타 부서와의 갈등 상황에서는 감정적 대립을 철저히 배제하고 '선제적 지원 제안'과 '인터페이스 시스템화'로 협력 관계를 구축하겠습니다. 첫째, 갈등의 원인이 되는 병목 지점을 분석하여 상대 부서의 실무 부담을 덜어줄 수 있는 데이터 전처리나 인력 백업 방안을 먼저 제안하며 협상 테이블을 열겠습니다. 둘째, 합의된 조건과 책임 범위를 명확한 표준 프로토콜로 문서화하여 향후 동일한 이슈로 부서 간 마찰이 재발하지 않도록 지속 가능한 협업 구조를 만들겠습니다."
    },
    "p_19": {
        "speech_1m30s": "생산 일정이 촉박할수록 조급함에 흔들리지 않고 '품질·안전 무타협 원칙' 아래 '병목 공정 집중 돌파와 투명한 공유'로 냉정히 대응하겠습니다. 첫째, 납기에 쫓겨 표준 공정(SOP)이나 안전 수칙을 생략하면 대량 불량과 라인 셧다운이라는 더 큰 손실을 부르므로 기본 원칙은 철저히 사수하겠습니다. 둘째, 전체 흐름에서 지연을 유발하는 핵심 병목(Bottleneck) 구간을 데이터로 식별해 가용 설비 백업 라우팅과 리소스 집중 투입으로 리드타임을 단축하고, 유관 부서에 실시간 공유해 납기를 지키겠습니다.",
        "speech_alt": "극심한 일정 압박 상황에서는 '업무 트리아지(우선순위 분류)'와 '선제적 리스크 소통'으로 일정과 품질을 모두 방어하겠습니다. 첫째, 당장 출하 품질과 직결되는 핵심 공정 작업(Must-have)과 후속으로 미룰 수 있는 부가 업무를 즉시 분리하여 골든 타임 내 코어 작업에 에너지를 100% 집중하겠습니다. 둘째, 혼자 문제를 껴안지 않고 생산관리 및 설비 부서에 시간대별 진척도를 투명하게 공유하여 교차 지원과 설비 할당 최적화를 이끌어냄으로써 압박을 원팀의 실행력으로 돌파하겠습니다."
    },
    "p_20": {
        "speech_1m30s": "동일한 문제가 반복되는 이유는 현상만 덮는 임시방편에 그쳐 근본 원인을 제거하지 못했기 때문이므로, '5-Why 근본 원인 규명'과 'Fool-proof 시스템화'로 뿌리 뽑겠습니다. 첫째, 과거 발생 이력과 설비 센서 데이터를 전수 분석해 작업자 실수가 아닌 부품 마모나 공정 마진 부족 등 물리적 근본 원인을 끝까지 추적하고 DoE로 검증하겠습니다. 둘째, 검증된 대책을 개인의 주의에만 맡기지 않고 설비 인터록(Interlock), 알람 자동화, SOP 개정으로 시스템화하여 재발률을 0%로 만들겠습니다.",
        "speech_alt": "만성적인 반복 트러블을 개선하기 위해 '데이터 패턴 모니터링 자동화'와 '유관 부서 합동 표준 개정'을 실행하겠습니다. 첫째, 문제가 터진 후 사후 대응하는 방식에서 벗어나, 불량 발생 직전의 미세한 센서 신호 변화(Weak Signal)를 파이썬 스크립트와 FDC 알람으로 모델링해 사전 예지보전 체계를 구축하겠습니다. 둘째, 도출된 개선안을 공정·설비·품질 부서와 투명하게 공유하여 수평 전개(Yokoten)함으로써 유사 라인 전체의 잠재 불량까지 선제적으로 차단하겠습니다."
    },
    "p_21": {
        "speech_1m30s": "제가 제조·공정 조직에서 가장 중요하게 생각하는 가치관은 '기본과 원칙(SOP) 준수'와 '데이터 앞에서의 투명한 정직성'입니다. 첫째, 24시간 가동되는 생산 현장에서 단 한 번의 절차 생략이나 타협은 대형 품질 불량과 안전사고로 직결되므로 사소한 일상 점검도 정석대로 수행하는 기본기가 모든 생산성의 토대입니다. 둘째, 엔지니어는 감이 아닌 객관적 데이터로 소통하며 미세한 이상 징후나 실수가 발견되었을 때 즉시 투명하게 공유하여 초기 골든 타임 내에 문제를 해결해야 합니다.",
        "speech_alt": "제조 및 공정 엔지니어로서 최우선으로 삼는 가치관은 '유기적인 원팀(One-Team) 책임감'과 '현장 중심의 지속적 혁신'입니다. 첫째, 반도체 라인은 수백 개의 선후 공정과 설비·생산·품질 부서가 맞물려 돌아가므로 내 담당 공정만 끝내면 된다는 시야를 넘어 후공정 수율과 동료의 안전까지 배려해야 합니다. 둘째, 기존 관행에 안주하지 않고 현장의 작은 산포와 비효율을 끊임없이 파고들어 개선하는 주인 의식(VWBE)으로 세계 최고 수준의 양산 경쟁력을 완성하겠습니다."
    },
    "p_22": {
        "speech_1m30s": "안전과 생산성이 충돌하는 어떠한 순간에도 제 판단 기준은 '안전이 모든 생산 목표보다 절대 우선한다'는 무타협 원칙입니다. 첫째, 단기 생산량을 위해 위험을 방치하면 동료의 생명을 위협할 뿐 아니라 중대 재해로 인한 라인 전면 셧다운이라는 돌이킬 수 없는 손실을 초래하므로, 위험 감지 즉시 작업을 중단하고 작업자를 보호하겠습니다. 둘째, 안전·설비 부서와 협력해 위험 요인을 물리적(LOTO 등)으로 완전 제거한 뒤 재가동하며, 불가피한 지연은 투명하게 보고하고 백업 라우팅으로 만회하겠습니다.",
        "speech_alt": "안전과 생산성의 딜레마에서는 '선(先) 안전 확보 후(後) 공학적 대안 도출'이라는 명확한 프로토콜로 행동하겠습니다. 첫째, 안전 인터록 해제나 보호구 미착용 같은 타협은 어떤 긴급 납기 상황에서도 단호히 거부하고 현장 안전 수칙을 100% 준수하겠습니다. 둘째, 안전 조치로 인해 발생하는 가동 시간 손실은 무리한 작업 강행이 아니라 유휴 설비 전환 배치와 공정 대기 시간 단축 등 엔지니어링 최적화로 만회함으로써, 안전이 곧 지속 가능한 최고의 생산성임을 증명하겠습니다."
    }
}

for pid, d in dual_personality_data.items():
    l1 = len(d["speech_1m30s"])
    l2 = len(d["speech_alt"])
    assert 220 <= l1 <= 320, f"{pid} speech_1m30s len {l1} out of 220~320"
    assert 220 <= l2 <= 320, f"{pid} speech_alt len {l2} out of 220~320"
    print(f"{pid}: 답변1={l1}자, 답변2={l2}자")

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

m = re.search(r'const DEFAULT_TOPICS = (\[.*?\]);', content, re.DOTALL)
if not m:
    raise ValueError("DEFAULT_TOPICS not found")

topics = json.loads(m.group(1))
for t in topics:
    if t["category"] == "personality" and t["id"] in dual_personality_data:
        t["speech_1m30s"] = dual_personality_data[t["id"]]["speech_1m30s"]
        t["speech_alt"] = dual_personality_data[t["id"]]["speech_alt"]

new_json_str = json.dumps(topics, ensure_ascii=False, indent=2)
content = content[:m.start(1)] + new_json_str + content[m.end(1):]

# Bump STORAGE_KEY to v12
content = re.sub(r"const STORAGE_KEY = 'aisk_master_topics_custom_v\d+';", "const STORAGE_KEY = 'aisk_master_topics_custom_v12';", content)
content = re.sub(r"localStorage\.getItem\('aisk_master_topics_custom_v\d+'\)", "localStorage.getItem('aisk_master_topics_custom_v11')", content)

# Update loadTopics to also sync speech_alt if missing
old_load_sync = """          DEFAULT_TOPICS.forEach(dt => {
            if (!currentTopics.some(ct => ct.id === dt.id)) {
              currentTopics.push(JSON.parse(JSON.stringify(dt)));
              updated = true;
            }
          });"""

new_load_sync = """          DEFAULT_TOPICS.forEach(dt => {
            const existing = currentTopics.find(ct => ct.id === dt.id);
            if (!existing) {
              currentTopics.push(JSON.parse(JSON.stringify(dt)));
              updated = true;
            } else if (dt.speech_alt && !existing.speech_alt) {
              existing.speech_alt = dt.speech_alt;
              updated = true;
            }
          });"""

if old_load_sync in content:
    content = content.replace(old_load_sync, new_load_sync)

# Add CSS for .speech-card.alt-card if not present
alt_card_css = """
    .speech-card.alt-card {
      background: linear-gradient(135deg, rgba(16, 185, 129, 0.10) 0%, rgba(56, 189, 248, 0.10) 100%);
      border: 1.5px solid #10b981;
      box-shadow: 0 4px 20px rgba(16, 185, 129, 0.12);
      margin-top: -10px;
    }
    .speech-card.alt-card .speech-card-title {
      background-color: #059669;
    }
"""
if ".speech-card.alt-card" not in content:
    content = content.replace("    .speech-card-header {", alt_card_css + "\n    .speech-card-header {")

# Update renderCards() to render both 답변 1 and 답변 2 for personality topics
old_card_render = """        const isPersonality = (cat === 'personality');
        const cardHeaderTitle = isPersonality 
          ? '1분 실전 핵심 전달 (구어체 호흡 · 약 220~320자)' 
          : '3분 심층 기술 마스터 전달 (원리·수식·양산 심화 · 약 800~1500자)';
        const cardLenGuide = isPersonality ? '1분 권장: 220~320자' : '3분 권장: 800~1500자';

        const lenColor = getLenColor(speechCharCount, cat);

        html += `
          <section class="topic-section" id="${t.id}" data-category="${cat}">
            <div id="view-${t.id}">
              <div class="topic-header">
                <div class="topic-title-wrap">
                  <span class="topic-badge ${badgeClass}">${numStr}</span>
                  <span class="category-chip">${escapeHtml(catLabel)}</span>
                  <div class="kw-container editable-field" contenteditable="true" data-field="keywords" data-id="${t.id}" title="클릭하여 키워드 바로 수정">${kwPills}</div>
                </div>

                <div class="card-actions">
                  <div class="speech-len-tag">실전 호흡: <strong id="len-tag-${t.id}" style="color: ${lenColor};">${speechCharCount}자</strong> <span class="len-guide-sub">(${cardLenGuide})</span></div>
                  <span class="save-status-badge" id="save-status-${t.id}">클릭하여 바로 수정</span>
                  <button class="btn-card-action delete-btn" onclick="deleteTopic('${t.id}')" title="이 문항 삭제">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>
                    삭제
                  </button>
                </div>
              </div>

              <!-- 제목 (클릭 시 즉시 수정) -->
              <h2 class="topic-title editable-field" contenteditable="true" data-field="title" data-id="${t.id}" title="클릭하여 제목 바로 수정">${title}</h2>

              <!-- 실전 핵심 전달 카드 (본문 클릭 시 즉시 작성/수정) -->
              <div class="speech-card">
                <div class="speech-card-header">
                  <div class="speech-card-title">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="22"></line></svg>
                    <span>${cardHeaderTitle}</span>
                  </div>
                  <span class="speech-click-hint">✏️ 클릭하여 바로 작성·수정 (자동 저장)</span>
                  <button class="btn-card-action" onclick="copySpeech('${t.id}')" title="답변 복사">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                    복사
                  </button>
                </div>
                <div class="speech-body editable-field" contenteditable="true" data-field="speech_1m30s" data-id="${t.id}" id="speech-text-${t.id}" title="클릭하여 바로 수정 (자동 저장)">${escapeHtml(speech)}</div>
              </div>"""

new_card_render = """        const isPersonality = (cat === 'personality');
        const speechAlt = t.speech_alt || '';
        const speechAltCharCount = speechAlt.length;
        const cardHeaderTitle = isPersonality 
          ? '답변 1 · 1분 실전 핵심 전달 (구어체 호흡 · 약 220~320자)' 
          : '3분 심층 기술 마스터 전달 (원리·수식·양산 심화 · 약 800~1500자)';
        const cardLenGuide = isPersonality ? '1분 권장: 220~320자' : '3분 권장: 800~1500자';

        const lenColor = getLenColor(speechCharCount, cat);
        const lenAltColor = getLenColor(speechAltCharCount, cat);
        const lenSummaryHtml = isPersonality
          ? `답변1: <strong id="len-tag-${t.id}" style="color: ${lenColor};">${speechCharCount}자</strong> / 답변2: <strong id="len-alt-tag-${t.id}" style="color: ${lenAltColor};">${speechAltCharCount}자</strong> <span class="len-guide-sub">(${cardLenGuide})</span>`
          : `실전 호흡: <strong id="len-tag-${t.id}" style="color: ${lenColor};">${speechCharCount}자</strong> <span class="len-guide-sub">(${cardLenGuide})</span>`;

        const altCardHtml = isPersonality ? `
              <!-- 답변 2: 1분 실전 대안 전달 카드 (인성 전용 2번째 답변) -->
              <div class="speech-card alt-card">
                <div class="speech-card-header">
                  <div class="speech-card-title">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="22"></line></svg>
                    <span>답변 2 · 1분 실전 대안 전달 (다른 관점·어프로치 · 약 220~320자)</span>
                  </div>
                  <span class="speech-click-hint">✏️ 클릭하여 바로 작성·수정 (자동 저장)</span>
                  <button class="btn-card-action" onclick="copySpeech('${t.id}', 2)" title="답변 2 복사">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                    답변 2 복사
                  </button>
                </div>
                <div class="speech-body editable-field" contenteditable="true" data-field="speech_alt" data-id="${t.id}" id="speech-alt-text-${t.id}" title="클릭하여 답변 2 바로 수정 (자동 저장)">${escapeHtml(speechAlt)}</div>
              </div>` : '';

        html += `
          <section class="topic-section" id="${t.id}" data-category="${cat}">
            <div id="view-${t.id}">
              <div class="topic-header">
                <div class="topic-title-wrap">
                  <span class="topic-badge ${badgeClass}">${numStr}</span>
                  <span class="category-chip">${escapeHtml(catLabel)}</span>
                  <div class="kw-container editable-field" contenteditable="true" data-field="keywords" data-id="${t.id}" title="클릭하여 키워드 바로 수정">${kwPills}</div>
                </div>

                <div class="card-actions">
                  <div class="speech-len-tag">${lenSummaryHtml}</div>
                  <span class="save-status-badge" id="save-status-${t.id}">클릭하여 바로 수정</span>
                  <button class="btn-card-action delete-btn" onclick="deleteTopic('${t.id}')" title="이 문항 삭제">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>
                    삭제
                  </button>
                </div>
              </div>

              <!-- 제목 (클릭 시 즉시 수정) -->
              <h2 class="topic-title editable-field" contenteditable="true" data-field="title" data-id="${t.id}" title="클릭하여 제목 바로 수정">${title}</h2>

              <!-- 실전 핵심 전달 카드 (본문 클릭 시 즉시 작성/수정) -->
              <div class="speech-card">
                <div class="speech-card-header">
                  <div class="speech-card-title">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="22"></line></svg>
                    <span>${cardHeaderTitle}</span>
                  </div>
                  <span class="speech-click-hint">✏️ 클릭하여 바로 작성·수정 (자동 저장)</span>
                  <button class="btn-card-action" onclick="copySpeech('${t.id}', 1)" title="답변 복사">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                    ${isPersonality ? '답변 1 복사' : '복사'}
                  </button>
                </div>
                <div class="speech-body editable-field" contenteditable="true" data-field="speech_1m30s" data-id="${t.id}" id="speech-text-${t.id}" title="클릭하여 바로 수정 (자동 저장)">${escapeHtml(speech)}</div>
              </div>
              ${altCardHtml}"""

assert old_card_render in content, "old_card_render not found"
content = content.replace(old_card_render, new_card_render)

# Update input listener and saveFieldDirect for speech_alt
old_input_len = """      // 1) 발화 글자수 실시간 업데이트 (인성 1분 / 직무 3분 맞춤 판정)
      if (field === 'speech_1m30s') {
        const lenTag = document.getElementById(`len-tag-${id}`);
        const topic = currentTopics.find(t => t.id === id);
        const cat = topic ? topic.category : 'personality';
        if (lenTag) {
          lenTag.textContent = `${text.length}자`;
          lenTag.style.color = getLenColor(text.length, cat);
        }
      }"""

new_input_len = """      // 1) 발화 글자수 실시간 업데이트 (인성 1분 / 직무 3분 맞춤 판정)
      if (field === 'speech_1m30s' || field === 'speech_alt') {
        const tagId = (field === 'speech_alt') ? `len-alt-tag-${id}` : `len-tag-${id}`;
        const lenTag = document.getElementById(tagId);
        const topic = currentTopics.find(t => t.id === id);
        const cat = topic ? topic.category : 'personality';
        if (lenTag) {
          lenTag.textContent = `${text.length}자`;
          lenTag.style.color = getLenColor(text.length, cat);
        }
      }"""

assert old_input_len in content, "old_input_len not found"
content = content.replace(old_input_len, new_input_len)

old_save_field = """      } else if (field === 'speech_1m30s') {
        topic.speech_1m30s = rawText;
      }"""

new_save_field = """      } else if (field === 'speech_1m30s') {
        topic.speech_1m30s = rawText;
      } else if (field === 'speech_alt') {
        topic.speech_alt = rawText;
      }"""

assert old_save_field in content, "old_save_field not found"
content = content.replace(old_save_field, new_save_field)

old_copy_speech = """    function copySpeech(id) {
      const el = document.getElementById(`speech-text-${id}`);
      if (!el) return;
      const text = el.innerText.trim();
      navigator.clipboard.writeText(text).then(() => {
        showToast('📋 1분 30초 실전 답변이 클립보드에 복사되었습니다!');
      }).catch(err => {
        console.error('복사 실패:', err);
      });
    }"""

new_copy_speech = """    function copySpeech(id, variant = 1) {
      const targetId = (variant === 2) ? `speech-alt-text-${id}` : `speech-text-${id}`;
      const el = document.getElementById(targetId);
      if (!el) return;
      const text = el.innerText.trim();
      navigator.clipboard.writeText(text).then(() => {
        showToast(`📋 ${variant === 2 ? '답변 2' : '실전 답변'} 내용이 클립보드에 복사되었습니다!`);
      }).catch(err => {
        console.error('복사 실패:', err);
      });
    }"""

assert old_copy_speech in content, "old_copy_speech not found"
content = content.replace(old_copy_speech, new_copy_speech)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

with open("result/261010_v1.0/index.html", "w", encoding="utf-8") as f:
    f.write(content)

with open("context/data/aisk_curated_topics.json", "w", encoding="utf-8") as f:
    json.dump(topics, f, ensure_ascii=False, indent=2)

shutil.copyfile("index.html", "../index.html")
print("Successfully applied dual answers (답변 1 & 답변 2) to all 22 personality questions!")
