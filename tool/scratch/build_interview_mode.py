# -*- coding: utf-8 -*-
import json
import re

with open(r'C:\Work\반도체4_AISK대비\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. CSS 추가: 면접 모드 전용 스타일
interview_css = """
    /* ========================================================
       🎙️ 실전 면접 모드 (Interview Mode) 핵심 스타일
       ======================================================== */
    .mode-toggle-wrap {
      display: inline-flex;
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid var(--border);
      padding: 3px;
      border-radius: 9999px;
      gap: 3px;
      backdrop-filter: blur(8px);
    }
    .mode-toggle-btn {
      padding: 6px 14px;
      font-size: 0.82rem;
      font-weight: 700;
      border-radius: 9999px;
      border: none;
      background: transparent;
      color: var(--text-sub);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
      font-family: inherit;
    }
    .mode-toggle-btn:hover {
      color: #fff;
      background: rgba(255, 255, 255, 0.08);
    }
    .mode-toggle-btn.active {
      background: linear-gradient(135deg, #0284c7 0%, #2563eb 100%);
      color: #ffffff;
      box-shadow: 0 2px 10px rgba(37, 99, 235, 0.4);
    }

    /* 뷰 모드 제어: body에 interview-mode 클래스 추가 시 */
    body.interview-mode #learnViewContainer {
      display: none !important;
    }
    body.interview-mode #interviewViewContainer {
      display: block !important;
    }

    #interviewViewContainer {
      display: none;
      animation: fadeInView 0.25s ease-out;
    }
    @keyframes fadeInView {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* 면접 상단 네비게이션 제어 바 */
    .interview-control-bar {
      background: linear-gradient(135deg, rgba(30, 41, 59, 0.85) 0%, rgba(15, 23, 42, 0.95) 100%);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 16px 20px;
      margin-bottom: 20px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .interview-control-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }
    .interview-cat-group {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }
    .interview-cat-btn {
      padding: 7px 16px;
      font-size: 0.88rem;
      font-weight: 700;
      border-radius: 8px;
      border: 1px solid var(--border);
      background: #1e293b;
      color: var(--text-sub);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
      font-family: inherit;
    }
    .interview-cat-btn:hover {
      background: #334155;
      color: #fff;
    }
    .interview-cat-btn.active {
      background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
      color: #fff;
      border-color: #38bdf8;
      box-shadow: 0 0 12px rgba(56, 189, 248, 0.3);
    }
    .interview-action-group {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }
    .btn-random-interview {
      background: linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%);
      color: #fff;
      font-weight: 800;
      font-size: 0.88rem;
      padding: 8px 16px;
      border-radius: 8px;
      border: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      box-shadow: 0 4px 14px rgba(236, 72, 153, 0.35);
      transition: all 0.2s;
      font-family: inherit;
    }
    .btn-random-interview:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 18px rgba(236, 72, 153, 0.5);
    }
    .btn-step-interview {
      background: #1e293b;
      border: 1px solid var(--border);
      color: var(--text-main);
      padding: 7px 12px;
      border-radius: 6px;
      font-size: 0.82rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s;
    }
    .btn-step-interview:hover {
      background: #334155;
      color: #fff;
    }
    .interview-progress-text {
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--text-muted);
      padding: 0 4px;
    }

    /* 면접 질문 카드 */
    .interview-question-box {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 24px 24px 20px 24px;
      margin-bottom: 20px;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
      position: relative;
    }
    .interview-q-meta {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      flex-wrap: wrap;
      gap: 8px;
    }
    .interview-q-badge-wrap {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .interview-q-badge {
      font-size: 0.78rem;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: 5px;
    }
    .interview-q-title {
      font-size: 1.35rem;
      font-weight: 800;
      line-height: 1.5;
      color: #ffffff;
      margin-bottom: 14px;
      letter-spacing: -0.02em;
    }
    .interview-hint-btn {
      background: rgba(56, 189, 248, 0.1);
      border: 1px solid rgba(56, 189, 248, 0.25);
      color: var(--primary-light);
      padding: 5px 12px;
      border-radius: 6px;
      font-size: 0.78rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.2s;
    }
    .interview-hint-btn:hover {
      background: rgba(56, 189, 248, 0.2);
      color: #fff;
    }
    .interview-hint-box {
      margin-top: 12px;
      padding: 10px 14px;
      background: rgba(15, 23, 42, 0.6);
      border-radius: 6px;
      border-left: 3px solid var(--accent-blue);
      display: none;
      animation: fadeInView 0.2s ease;
    }
    .interview-hint-box.show {
      display: block;
    }

    /* 녹음 & STT 콘솔 */
    .interview-recorder-box {
      background: #0f172a;
      border: 1px solid rgba(56, 189, 248, 0.3);
      border-radius: var(--radius-lg);
      padding: 20px;
      margin-bottom: 22px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    }
    .recorder-header-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
      flex-wrap: wrap;
      gap: 10px;
    }
    .btn-record-toggle {
      background: #ef4444;
      color: #ffffff;
      border: none;
      padding: 9px 20px;
      border-radius: 9999px;
      font-weight: 800;
      font-size: 0.92rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
      box-shadow: 0 4px 14px rgba(239, 68, 68, 0.35);
      font-family: inherit;
    }
    .btn-record-toggle:hover {
      background: #dc2626;
      transform: translateY(-1px);
    }
    .btn-record-toggle.recording {
      background: #dc2626;
      animation: recPulse 1.4s infinite;
    }
    @keyframes recPulse {
      0% { box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.7); }
      70% { box-shadow: 0 0 0 12px rgba(239, 68, 68, 0); }
      100% { box-shadow: 0 0 0 0 rgba(239, 68, 68, 0); }
    }
    .record-timer-badge {
      font-family: 'JetBrains Mono', monospace;
      font-size: 1.1rem;
      font-weight: 800;
      color: #f8fafc;
      background: #1e293b;
      padding: 5px 12px;
      border-radius: 6px;
      border: 1px solid var(--border);
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .speech-transcript-area {
      width: 100%;
      min-height: 120px;
      background: #1e293b;
      border: 1px solid var(--border);
      border-radius: 8px;
      color: #f8fafc;
      font-size: 1rem;
      line-height: 1.75;
      padding: 12px 14px;
      font-family: inherit;
      resize: vertical;
      margin-bottom: 12px;
      transition: border 0.2s;
    }
    .speech-transcript-area:focus {
      outline: none;
      border-color: #38bdf8;
      box-shadow: 0 0 10px rgba(56, 189, 248, 0.25);
    }
    .recorder-action-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
    }
    .btn-save-record {
      background: linear-gradient(135deg, #059669 0%, #10b981 100%);
      color: #fff;
      border: none;
      padding: 8px 18px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.86rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      box-shadow: 0 3px 10px rgba(16, 185, 129, 0.3);
      transition: all 0.2s;
    }
    .btn-save-record:hover {
      background: #059669;
    }
    .btn-clear-record {
      background: transparent;
      border: 1px solid var(--border);
      color: var(--text-muted);
      padding: 7px 12px;
      border-radius: 6px;
      font-size: 0.8rem;
      cursor: pointer;
      transition: all 0.2s;
    }
    .btn-clear-record:hover {
      color: #ef4444;
      border-color: #ef4444;
    }

    /* 나의 답변 기록 히스토리 목록 */
    .interview-history-box {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 20px 22px;
      margin-bottom: 22px;
    }
    .history-box-title {
      font-size: 0.95rem;
      font-weight: 800;
      color: #f1f5f9;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
    }
    .history-card-item {
      background: #1e293b;
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 8px;
      padding: 14px 16px;
      margin-bottom: 10px;
      transition: all 0.2s;
    }
    .history-card-item:hover {
      border-color: rgba(56, 189, 248, 0.35);
    }
    .history-card-meta {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
      font-size: 0.78rem;
      color: var(--text-muted);
    }
    .history-try-badge {
      background: rgba(56, 189, 248, 0.15);
      color: #38bdf8;
      font-weight: 800;
      padding: 2px 7px;
      border-radius: 4px;
      font-size: 0.74rem;
    }
    .history-card-text {
      font-size: 0.94rem;
      line-height: 1.7;
      color: #e2e8f0;
      white-space: pre-wrap;
      word-break: keep-all;
    }

    /* 하단 모범답안 확인 카드 */
    .interview-model-box {
      background: rgba(30, 41, 59, 0.7);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 20px 22px;
      margin-bottom: 30px;
    }
    .model-header-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
      user-select: none;
    }
    .model-title-text {
      font-size: 1rem;
      font-weight: 800;
      color: var(--primary-light);
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .model-body-content {
      margin-top: 14px;
      padding-top: 14px;
      border-top: 1px solid var(--border);
      font-size: 1.02rem;
      line-height: 1.85;
      color: #f1f5f9;
      white-space: pre-wrap;
      word-break: keep-all;
      display: none;
    }
    .model-body-content.open {
      display: block;
      animation: fadeInView 0.2s ease;
    }
"""

# CSS 추가
if '/* ========================================================\n       🎙️ 실전 면접 모드' not in html:
    html = html.replace('</style>', interview_css + '\n  </style>')
    print("Added interview mode CSS successfully.")

# 2. 사이드바 상단 액션 바와 메인 헤더에 모드 전환 토글 스위치 추가
mode_toggle_html = """
    <!-- 🎛️ 모드 전환 토글 (학습 백과사전 vs 실전 면접) -->
    <div style="padding: 10px 16px; border-bottom: 1px solid var(--border); background: rgba(15, 23, 42, 0.5);">
      <div class="mode-toggle-wrap" style="width: 100%;">
        <button class="mode-toggle-btn active" id="btnModeLearnSide" onclick="toggleViewMode('learn')" style="flex: 1; justify-content: center;">
          <span>📖 학습 모드</span>
        </button>
        <button class="mode-toggle-btn" id="btnModeInterviewSide" onclick="toggleViewMode('interview')" style="flex: 1; justify-content: center;">
          <span>🎙️ 실전 면접</span>
        </button>
      </div>
    </div>
"""

# 사이드바 상단 액션 바 뒤에 삽입
pos_act_end = html.find('</div>\n\n    <!-- 카테고리 필터 탭 -->')
if pos_act_end != -1 and 'btnModeInterviewSide' not in html:
    html = html[:pos_act_end+6] + mode_toggle_html + html[pos_act_end+6:]
    print("Added mode toggle to sidebar successfully.")

# 메인 헤더의 header-btn-group 앞에도 큼직한 모드 전환 토글 삽입
main_mode_toggle = """
        <!-- 모드 전환 헤더 스위처 -->
        <div style="margin-bottom: 14px;">
          <div class="mode-toggle-wrap">
            <button class="mode-toggle-btn active" id="btnModeLearnMain" onclick="toggleViewMode('learn')">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
              <span>📖 학습 백과사전 모드</span>
            </button>
            <button class="mode-toggle-btn" id="btnModeInterviewMain" onclick="toggleViewMode('interview')">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="22"></line></svg>
              <span>🎙️ 실전 면접 연습 모드</span>
            </button>
          </div>
        </div>
"""

pos_header_btns = html.find('<div class="header-btn-group">')
if pos_header_btns != -1 and 'btnModeInterviewMain' not in html:
    html = html[:pos_header_btns] + main_mode_toggle + html[pos_header_btns:]
    print("Added mode toggle to main header successfully.")

# 모바일 상단 바에도 면접 모드 전환 버튼 추가
pos_mob_title = html.find('<div class="mobile-header-title">AISK 면접 마스터</div>')
if pos_mob_title != -1 and 'toggleViewMode' not in html[pos_mob_title-100:pos_mob_title+300]:
    mob_toggle_btn = """<button class="mobile-top-btn" id="mobModeBtn" onclick="toggleViewMode(currentViewMode === 'learn' ? 'interview' : 'learn')" style="font-size:0.8rem; font-weight:800; min-width:64px; margin-right:6px;" title="면접 모드 토글">🎙️ 면접</button>"""
    html = html.replace('<div class="mobile-header-title">AISK 면접 마스터</div>', '<div class="mobile-header-title">AISK 마스터</div>' + mob_toggle_btn)
    print("Added mode toggle button to mobile top bar.")

# 3. HTML 메인 컨텐츠 영역 래핑:
# 기존 <div id="topicContainer"> 및 상단 바들을 <div id="learnViewContainer">로 감싸고,
# 바로 아래에 <div id="interviewViewContainer"> 추가!
pos_main_proc_bar = html.find('<!-- 🚀 메인 본문 공정·소자 빠른 점프 바 -->')
if pos_main_proc_bar != -1 and '<div id="learnViewContainer">' not in html:
    html = html[:pos_main_proc_bar] + '<div id="learnViewContainer">\n      ' + html[pos_main_proc_bar:]
    
    # 닫는 태그 찾기: </main> 바로 앞
    pos_main_close = html.find('</main>')
    
    # 면접 모드 컨테이너 HTML
    interview_view_html = """
    </div> <!-- /learnViewContainer -->

    <!-- ========================================================
         🎙️ 실전 면접 모드 전용 집중 뷰 (Interview View Container)
         ======================================================== -->
    <div id="interviewViewContainer">
      
      <!-- 상단 컨트롤 바 (카테고리 선택 / 랜덤 출제 / 이전-다음) -->
      <div class="interview-control-bar">
        <div class="interview-control-row">
          <div class="interview-cat-group">
            <button class="interview-cat-btn active" id="intCatAll" onclick="selectInterviewCategory('all')">전체 질문 (71)</button>
            <button class="interview-cat-btn" id="intCatPersonality" onclick="selectInterviewCategory('personality')">🤝 인성·협업 (22)</button>
            <button class="interview-cat-btn" id="intCatTech" onclick="selectInterviewCategory('tech')">⚙️ 직무·공정·소자 (49)</button>
          </div>

          <div class="interview-action-group">
            <button class="btn-random-interview" onclick="pickRandomInterviewTopic()" title="현재 카테고리에서 무작위 질문 추첨">
              <span>🎲 랜덤 문항 출제</span>
            </button>
            <button class="btn-step-interview" onclick="navigateInterviewTopic(-1)" title="이전 질문">◀ 이전</button>
            <span class="interview-progress-text" id="interviewProgressText">1 / 71</span>
            <button class="btn-step-interview" onclick="navigateInterviewTopic(1)" title="다음 질문">다음 ▶</button>
          </div>
        </div>

        <!-- 직무 선택 시 노출되는 WOPEDIMP 컴팩트 필터 칩 바 -->
        <div class="main-proc-chips" id="interviewProcChips" style="display: flex; gap: 5px; flex-wrap: wrap; padding-top: 4px; border-top: 1px solid rgba(255,255,255,0.06);">
          <span style="font-size: 0.74rem; font-weight: 700; color: var(--text-muted); align-self: center; margin-right: 4px;">공정 선택:</span>
          <button class="proc-chip active" data-intproc="ALL" onclick="selectInterviewProcess('ALL')">ALL (49)</button>
          <button class="proc-chip chip-com" data-intproc="COM" onclick="selectInterviewProcess('COM')">공통</button>
          <button class="proc-chip" data-intproc="W" onclick="selectInterviewProcess('W')">W</button>
          <button class="proc-chip" data-intproc="O" onclick="selectInterviewProcess('O')">O</button>
          <button class="proc-chip" data-intproc="P" onclick="selectInterviewProcess('P')">P</button>
          <button class="proc-chip" data-intproc="E" onclick="selectInterviewProcess('E')">E</button>
          <button class="proc-chip" data-intproc="D" onclick="selectInterviewProcess('D')">D</button>
          <button class="proc-chip" data-intproc="I" onclick="selectInterviewProcess('I')">I</button>
          <button class="proc-chip" data-intproc="M" onclick="selectInterviewProcess('M')">M</button>
          <button class="proc-chip" data-intproc="PKG" onclick="selectInterviewProcess('PKG')">P</button>
          <button class="proc-chip chip-dev" data-intproc="DEV" onclick="selectInterviewProcess('DEV')">소자</button>
        </div>
      </div>

      <!-- 📋 면접 질문 카드 -->
      <div class="interview-question-box">
        <div class="interview-q-meta">
          <div class="interview-q-badge-wrap">
            <span class="interview-q-badge cat-badge-t" id="intQBadge">직무-01</span>
            <span class="category-chip" id="intQCategory">반도체 직무 · 기술</span>
          </div>
          <button class="interview-hint-btn" onclick="toggleInterviewHint()">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
            <span>핵심 키워드 힌트</span>
          </button>
        </div>

        <h2 class="interview-q-title" id="intQTitle">질문을 불러오는 중입니다...</h2>

        <!-- 키워드 힌트 박스 (토글) -->
        <div class="interview-hint-box" id="intHintBox">
          <div style="font-size:0.75rem; font-weight:700; color:var(--text-muted); margin-bottom:4px;">💡 권장 핵심 키워드</div>
          <div id="intKeywordsList" style="display:flex; flex-wrap:wrap; gap:6px;"></div>
        </div>
      </div>

      <!-- 🎙️ 실시간 녹음 & STT 자동 대사 기록 콘솔 -->
      <div class="interview-recorder-box">
        <div class="recorder-header-row">
          <div style="display: flex; align-items: center; gap: 12px;">
            <button class="btn-record-toggle" id="btnRecordToggle" onclick="toggleRecording()">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="22"></line></svg>
              <span id="btnRecordText">답변 녹음 시작 (STT)</span>
            </button>
            <span style="font-size: 0.8rem; color: var(--text-muted);" id="recStatusNotice">버튼을 누르고 말하면 실시간으로 자동 텍스트 기록됩니다.</span>
          </div>

          <div class="record-timer-badge" id="intRecTimer">
            <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#ef4444;" id="recDot"></span>
            <span id="recTimerDisplay">00:00</span>
          </div>
        </div>

        <!-- 실시간 자동 대사 기록 창 (수정 가능) -->
        <textarea class="speech-transcript-area" id="intTranscriptArea" placeholder="[답변 녹음 시작] 버튼을 누르고 음성으로 답변하시거나, 키보드로 직접 나의 답변을 작성하세요..."></textarea>

        <div class="recorder-action-row">
          <div style="font-size: 0.82rem; color: var(--text-sub);">
            현재 글자수: <strong id="intTranscriptLen" style="color:#38bdf8;">0자</strong>
            <span id="intLenGuideNotice" style="font-size:0.75rem; color:var(--text-muted); margin-left:6px;">(권장 분량 안내)</span>
          </div>
          <div style="display: flex; gap: 8px;">
            <button class="btn-clear-record" onclick="clearCurrentTranscript()">지우기</button>
            <button class="btn-save-record" onclick="saveCurrentInterviewRecord()">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"></path><polyline points="17 21 17 13 7 13 7 21"></polyline><polyline points="7 3 7 8 15 8"></polyline></svg>
              <span>이번 답변 기록 저장</span>
            </button>
          </div>
        </div>
      </div>

      <!-- 📝 나의 답변 기록 히스토리 (문항별 다회차 누적 보관) -->
      <div class="interview-history-box">
        <div class="history-box-title">
          <span style="display:flex; align-items:center; gap:6px;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
            이 문항의 나의 답변 기록
          </span>
          <span id="historyCountBadge" style="font-size:0.76rem; font-weight:700; color:var(--primary-light);">0회 연습함</span>
        </div>

        <div id="intHistoryList">
          <!-- JS로 동적 렌더링 -->
        </div>
      </div>

      <!-- 📖 모범답안 (맨 아래 배치) -->
      <div class="interview-model-box">
        <div class="model-header-row" onclick="toggleModelAnswer()">
          <div class="model-title-text">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
            <span>📖 모범답안 확인하기 (노란색 볼드 음영 반영)</span>
          </div>
          <span id="modelToggleIcon" style="font-size: 1.1rem; color: var(--text-muted); transition: transform 0.2s;">▼</span>
        </div>

        <div class="model-body-content" id="modelBodyContent">
          <!-- 모범답안 텍스트 및 서식 렌더링 -->
          <div id="modelAnswerText"></div>
          
          <div style="margin-top: 14px; display: flex; justify-content: flex-end;">
            <button class="btn-card-action" onclick="copyModelAnswer()" title="모범답안 복사">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
              <span>모범답안 복사</span>
            </button>
          </div>
        </div>
      </div>

    </div> <!-- /interviewViewContainer -->
"""
    html = html[:pos_main_close] + interview_view_html + '\n  ' + html[pos_main_close:]
    print("Wrapped learn view and added interview view container successfully.")

# 파일 저장
with open(r'C:\Work\반도체4_AISK대비\index.html', 'w', encoding='utf-8') as f:
    f.write(html)
