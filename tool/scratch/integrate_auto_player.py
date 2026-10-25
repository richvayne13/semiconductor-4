# -*- coding: utf-8 -*-
import re

html_path = r"C:\Work\반도체4_AISK대비\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# ==============================================================================
# 1. CSS: 연속 자동 플레이어 (Auto-Player Dock & Settings)
# ==============================================================================
css_to_add = """
    /* ==========================================================================
       🎧 모바일 연속 자동 듣기 플레이어 (Hands-Free Loop Player) 스타일
       ========================================================================== */
    .auto-player-dock {
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      z-index: 9999;
      background: rgba(15, 23, 42, 0.96);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-top: 1.5px solid rgba(56, 189, 248, 0.5);
      box-shadow: 0 -10px 40px rgba(0, 0, 0, 0.7);
      padding: 10px 16px 14px 16px;
      display: none;
      flex-direction: column;
      gap: 8px;
      font-family: inherit;
      color: #fff;
      animation: slideUpDock 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .auto-player-dock.active {
      display: flex !important;
    }
    @keyframes slideUpDock {
      from { transform: translateY(100%); }
      to { transform: translateY(0); }
    }

    .ap-dock-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
    }
    .ap-topic-info {
      display: flex;
      align-items: center;
      gap: 8px;
      flex: 1;
      min-width: 0;
    }
    .ap-badge {
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 800;
      white-space: nowrap;
      background: linear-gradient(135deg, #0284c7 0%, #38bdf8 100%);
      color: #0f172a;
    }
    .ap-title {
      font-size: 0.88rem;
      font-weight: 700;
      color: #f1f5f9;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .ap-status-banner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 6px 12px;
      border-radius: 8px;
      font-size: 0.8rem;
      font-weight: 700;
      background: rgba(30, 41, 59, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.08);
    }
    .ap-status-banner.speaking-q {
      background: rgba(56, 189, 248, 0.15);
      border-color: #38bdf8;
      color: #38bdf8;
    }
    .ap-status-banner.countdown {
      background: rgba(245, 158, 11, 0.15);
      border-color: #f59e0b;
      color: #fbbf24;
    }
    .ap-status-banner.speaking-ans {
      background: rgba(16, 185, 129, 0.15);
      border-color: #10b981;
      color: #34d399;
    }

    /* 카운트다운 프로그레스 바 */
    .ap-progress-bar-wrap {
      width: 100%;
      height: 4px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 2px;
      overflow: hidden;
    }
    .ap-progress-bar {
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, #f59e0b, #10b981);
      transition: width 0.1s linear;
    }

    /* 제어 버튼 그룹 */
    .ap-controls {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      flex-wrap: wrap;
    }
    .ap-btn-group-main {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .ap-btn {
      padding: 8px 14px;
      border-radius: 8px;
      font-size: 0.82rem;
      font-weight: 700;
      border: 1px solid rgba(255, 255, 255, 0.15);
      background: #1e293b;
      color: #f1f5f9;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.2s;
      font-family: inherit;
    }
    .ap-btn:hover {
      background: #334155;
    }
    .ap-btn-play {
      background: linear-gradient(135deg, #10b981 0%, #059669 100%);
      color: #fff;
      border: none;
      padding: 8px 18px;
      font-size: 0.88rem;
      box-shadow: 0 0 12px rgba(16, 185, 129, 0.4);
    }
    .ap-btn-play.playing {
      background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
      box-shadow: 0 0 12px rgba(239, 68, 68, 0.4);
      animation: recPulse 1.2s infinite;
    }
    .ap-btn-skip {
      background: rgba(245, 158, 11, 0.2);
      border-color: #f59e0b;
      color: #fbbf24;
    }
    .ap-btn-skip:hover {
      background: #f59e0b;
      color: #0f172a;
    }

    /* 설정 팝업 패널 */
    .ap-settings-panel {
      display: none;
      background: rgba(15, 23, 42, 0.98);
      border: 1px solid rgba(56, 189, 248, 0.35);
      border-radius: 12px;
      padding: 14px;
      margin-top: 6px;
      flex-direction: column;
      gap: 12px;
      font-size: 0.82rem;
    }
    .ap-settings-panel.open {
      display: flex !important;
    }
    .ap-setting-row {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .ap-setting-label {
      font-size: 0.78rem;
      font-weight: 800;
      color: #94a3b8;
    }
    .ap-chip-group {
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
    }
    .ap-chip {
      padding: 5px 11px;
      border-radius: 6px;
      border: 1px solid rgba(255, 255, 255, 0.12);
      background: #1e293b;
      color: #cbd5e1;
      cursor: pointer;
      font-size: 0.78rem;
      font-weight: 700;
      transition: all 0.15s;
    }
    .ap-chip.active {
      background: #0284c7;
      border-color: #38bdf8;
      color: #fff;
      box-shadow: 0 0 10px rgba(56, 189, 248, 0.4);
    }
"""

if ".auto-player-dock" not in content:
    content = content.replace("</style>", css_to_add + "\n  </style>", 1)
    print("Added auto-player CSS styles.")

# ==============================================================================
# 2. HTML: 모바일 탑바 버튼 및 플레이어 도크 마크업
# ==============================================================================
# 2-1. 모바일 탑바에 [🎧 연속듣기] 버튼 추가
old_mob_btn = '<button class="mobile-top-btn" id="mobModeBtn"'
new_mob_btn = '<button class="mobile-top-btn" id="mobAutoPlayBtn" onclick="toggleAutoPlayerDock()" style="font-size:0.78rem; font-weight:800; min-width:82px; margin-right:6px; background:linear-gradient(135deg, #f59e0b 0%, #ef4444 100%); color:#fff; border:none; box-shadow:0 0 10px rgba(245,158,11,0.4);" title="모바일 핸즈프리 연속 자동 듣기">🎧 연속듣기</button><button class="mobile-top-btn" id="mobModeBtn"'

if 'id="mobAutoPlayBtn"' not in content and old_mob_btn in content:
    content = content.replace(old_mob_btn, new_mob_btn, 1)
    print("Added mobAutoPlayBtn to mobile-top-bar.")

# 2-2. 메인 헤더 및 사이드바에도 [🎧 연속 자동 듣기] 추가
old_main_mode_wrap = '<div class="mode-toggle-wrap" style="margin-left: 4px;">'
new_main_mode_wrap = """<button class="btn-voice-toggle" onclick="toggleAutoPlayerDock()" style="background:linear-gradient(135deg, #f59e0b 0%, #ef4444 100%); color:#fff; border:none; box-shadow:0 0 12px rgba(245,158,11,0.35); padding:6px 14px; font-size:0.82rem; font-weight:800;" title="질문 읽고 10초 후 답변 읽기를 무한 자동 반복하는 핸즈프리 모드">
              <span>🎧 연속 자동 듣기</span>
            </button>
            <div class="mode-toggle-wrap" style="margin-left: 4px;">"""

if 'onclick="toggleAutoPlayerDock()"' not in content and old_main_mode_wrap in content:
    content = content.replace(old_main_mode_wrap, new_main_mode_wrap, 1)
    print("Added Auto-Play button to main header.")

# 2-3. 하단 고정 플레이어 도크 마크업 주입 (body 닫기 전)
auto_player_dock_html = """
  <!-- ==========================================================================
       🎧 모바일 연속 자동 듣기 플레이어 (Hands-Free Loop Dock)
       ========================================================================== -->
  <div class="auto-player-dock" id="autoPlayerDock">
    <!-- 상단: 문항 정보 & 닫기/설정 토글 -->
    <div class="ap-dock-top">
      <div class="ap-topic-info">
        <span class="ap-badge" id="apBadge">인성-01</span>
        <span class="ap-title" id="apTitle">지원동기 및 직무 포부</span>
      </div>
      <div style="display: flex; align-items: center; gap: 6px;">
        <button class="ap-btn" onclick="toggleApSettingsPanel()" style="padding: 4px 8px; font-size: 0.74rem;" title="플레이어 설정">
          ⚙️ 설정
        </button>
        <button class="ap-btn" onclick="toggleAutoPlayerDock()" style="padding: 4px 8px; font-size: 0.74rem; color: #ef4444;" title="플레이어 닫기">
          ✕
        </button>
      </div>
    </div>

    <!-- 진행 상태 알림 배너 -->
    <div class="ap-status-banner" id="apStatusBanner">
      <span id="apStatusText">🎧 연속 자동 재생 대기 중 (재생 버튼을 누르면 시작됩니다)</span>
      <span id="apTimerNotice" style="font-family: var(--font-mono); font-weight: 800;">10s</span>
    </div>

    <!-- 카운트다운 게이지 바 -->
    <div class="ap-progress-bar-wrap">
      <div class="ap-progress-bar" id="apProgressBar"></div>
    </div>

    <!-- 하단 제어 버튼군 -->
    <div class="ap-controls">
      <div class="ap-btn-group-main">
        <button class="ap-btn" onclick="stepAutoPlayer(-1)" title="이전 질문">◀ 이전</button>
        <button class="ap-btn ap-btn-play" id="btnApPlayToggle" onclick="toggleAutoPlayerPlay()" title="연속 자동 재생 시작/일시정지">
          <span id="txtApPlayToggle">▶️ 연속 재생 시작</span>
        </button>
        <button class="ap-btn" onclick="stepAutoPlayer(1)" title="다음 질문">다음 ▶</button>
      </div>
      <button class="ap-btn ap-btn-skip" id="btnApSkipWait" onclick="skipAutoPlayerCountdown()" title="10초 대기를 건너뛰고 바로 답변을 듣습니다" style="display:none;">
        ⏩ 바로 답변 듣기
      </button>
    </div>

    <!-- 확장 설정 패널 -->
    <div class="ap-settings-panel" id="apSettingsPanel">
      <div class="ap-setting-row">
        <span class="ap-setting-label">1. 출제 범위 (카테고리)</span>
        <div class="ap-chip-group">
          <button class="ap-chip active" id="apChipCatAll" onclick="setApCategory('all')">전체 (106)</button>
          <button class="ap-chip" id="apChipCatP" onclick="setApCategory('personality')">인성 (22)</button>
          <button class="ap-chip" id="apChipCatT" onclick="setApCategory('tech')">직무·소자 (84)</button>
        </div>
      </div>

      <div class="ap-setting-row">
        <span class="ap-setting-label">2. 출제 순서</span>
        <div class="ap-chip-group">
          <button class="ap-chip active" id="apChipOrderRandom" onclick="setApOrder('random')">🎲 랜덤 출제</button>
          <button class="ap-chip" id="apChipOrderSeq" onclick="setApOrder('sequential')">📋 순서대로 출제</button>
        </div>
      </div>

      <div class="ap-setting-row">
        <span class="ap-setting-label">3. 답변 음성 재생 소스</span>
        <div class="ap-chip-group">
          <button class="ap-chip active" id="apChipAnsMyModel" onclick="setApAnswerMode('my_model_first')" title="내가 녹음한 모범답안이 있으면 내 음성으로, 없거나 무음이면 아나운서가 자동 재생">
            🎙️ 내 모범답안 우선 (미녹음·무음 시 아나운서)
          </button>
          <button class="ap-chip" id="apChipAnsLecture" onclick="setApAnswerMode('lecture_tts')" title="전문 아나운서의 심화해설 음성으로 낭독">
            📘 심화해설 아나운서 전용
          </button>
        </div>
      </div>

      <div class="ap-setting-row">
        <span class="ap-setting-label">4. 질문 후 생각/답변 대기 시간</span>
        <div class="ap-chip-group">
          <button class="ap-chip" id="apChipWait5" onclick="setApWaitSeconds(5)">5초</button>
          <button class="ap-chip active" id="apChipWait10" onclick="setApWaitSeconds(10)">10초 (기본)</button>
          <button class="ap-chip" id="apChipWait15" onclick="setApWaitSeconds(15)">15초</button>
          <button class="ap-chip" id="apChipWait20" onclick="setApWaitSeconds(20)">20초</button>
        </div>
      </div>
    </div>
  </div>
"""

if 'id="autoPlayerDock"' not in content:
    content = content.replace("</body>", auto_player_dock_html + "\n</body>", 1)
    print("Added autoPlayerDock HTML markup.")

# ==============================================================================
# 3. JavaScript: 연속 자동 플레이어 엔진 및 음성 검출 (VAD)
# ==============================================================================
js_engine_to_add = """
    // ==============================================================================
    // 🎧 모바일 연속 자동 듣기 플레이어 엔진 (Hands-Free Loop Engine)
    // ==============================================================================
    let apIsActive = false;             // 플레이어 도크 활성 여부
    let apIsPlaying = false;            // 자동 재생 루프 가동 여부
    let apCurrentStep = 'idle';         // 'idle' | 'question' | 'countdown' | 'answer'
    let apCurrentTopicId = null;

    // 플레이어 설정
    let apCategory = 'all';             // 'all' | 'personality' | 'tech'
    let apOrder = 'random';             // 'random' | 'sequential'
    let apAnswerMode = 'my_model_first';// 'my_model_first' | 'lecture_tts'
    let apWaitSeconds = 10;             // 기본 10초 대기

    // 타이머 및 오디오 객체
    let apCountdownInterval = null;
    let apCountdownRemain = 10;
    let apCurrentAudioEl = null;
    let apCurrentUtterance = null;
    let apLoopTimeout = null;

    // 플레이어 도크 열기/닫기
    function toggleAutoPlayerDock() {
      const dock = document.getElementById('autoPlayerDock');
      if (!dock) return;
      apIsActive = !apIsActive;
      if (apIsActive) {
        dock.classList.add('active');
        if (!apCurrentTopicId) {
          const pool = getApFilteredPool();
          if (pool.length > 0) {
            apCurrentTopicId = pool[0].id;
            updateApTopicHeader(pool[0]);
          }
        }
        showToast('🎧 연속 자동 플레이어가 열렸습니다. [▶️ 연속 재생 시작]을 누르세요.');
      } else {
        dock.classList.remove('active');
        stopAutoPlayerLoop();
        showToast('🎧 연속 자동 플레이어가 종료되었습니다.');
      }
    }

    function toggleApSettingsPanel() {
      const panel = document.getElementById('apSettingsPanel');
      if (panel) panel.classList.toggle('open');
    }

    // 설정 변경 함수들
    function setApCategory(cat) {
      apCategory = cat;
      ['All', 'P', 'T'].forEach(k => {
        const chip = document.getElementById(`apChipCat${k}`);
        if (chip) chip.classList.remove('active');
      });
      if (cat === 'all') document.getElementById('apChipCatAll')?.classList.add('active');
      else if (cat === 'personality') document.getElementById('apChipCatP')?.classList.add('active');
      else if (cat === 'tech') document.getElementById('apChipCatT')?.classList.add('active');

      showToast(`출제 범위가 [${cat === 'all' ? '전체' : cat === 'personality' ? '인성' : '직무·소자'}]로 변경되었습니다.`);
      if (!apIsPlaying) {
        const pool = getApFilteredPool();
        if (pool.length > 0) {
          apCurrentTopicId = pool[0].id;
          updateApTopicHeader(pool[0]);
        }
      }
    }

    function setApOrder(order) {
      apOrder = order;
      document.getElementById('apChipOrderRandom')?.classList.toggle('active', order === 'random');
      document.getElementById('apChipOrderSeq')?.classList.toggle('active', order === 'sequential');
      showToast(`출제 순서가 [${order === 'random' ? '랜덤' : '순서대로'}]로 변경되었습니다.`);
    }

    function setApAnswerMode(mode) {
      apAnswerMode = mode;
      document.getElementById('apChipAnsMyModel')?.classList.toggle('active', mode === 'my_model_first');
      document.getElementById('apChipAnsLecture')?.classList.toggle('active', mode === 'lecture_tts');
      showToast(mode === 'my_model_first' ? '답변 소스: [내 모범답안 우선]' : '답변 소스: [심화해설 아나운서]');
    }

    function setApWaitSeconds(sec) {
      apWaitSeconds = sec;
      [5, 10, 15, 20].forEach(s => {
        document.getElementById(`apChipWait${s}`)?.classList.toggle('active', s === sec);
      });
      showToast(`답변 구상 대기 시간이 [${sec}초]로 설정되었습니다.`);
    }

    // 대상 문항 풀 추출
    function getApFilteredPool() {
      if (apCategory === 'personality') {
        return currentTopics.filter(t => t.category === 'personality');
      } else if (apCategory === 'tech') {
        return currentTopics.filter(t => t.category !== 'personality');
      }
      return currentTopics;
    }

    function updateApTopicHeader(topic) {
      if (!topic) return;
      const badgeEl = document.getElementById('apBadge');
      const titleEl = document.getElementById('apTitle');
      if (badgeEl) {
        const isP = (topic.category === 'personality');
        const num = topic.number || 1;
        const numStr = isP ? `인성-${String(num).padStart(2, '0')}` : `${topic.process || '직무'}-${String(num).padStart(2, '0')}`;
        badgeEl.textContent = numStr;
        badgeEl.style.background = isP ? 'linear-gradient(135deg, #ec4899 0%, #f43f5e 100%)' : 'linear-gradient(135deg, #0284c7 0%, #38bdf8 100%)';
      }
      if (titleEl) {
        titleEl.textContent = topic.title;
      }
    }

    // 재생/일시정지 토글
    function toggleAutoPlayerPlay() {
      if (apIsPlaying) {
        pauseAutoPlayer();
      } else {
        startAutoPlayer();
      }
    }

    function startAutoPlayer() {
      apIsPlaying = true;
      const btn = document.getElementById('btnApPlayToggle');
      const txt = document.getElementById('txtApPlayToggle');
      if (btn) btn.classList.add('playing');
      if (txt) txt.textContent = '⏸️ 일시정지';

      // 다른 음성 중지
      if (typeof stopSpeakingQuestion === 'function') stopSpeakingQuestion();
      if (typeof stopLectureVoice === 'function') stopLectureVoice();

      const pool = getApFilteredPool();
      if (pool.length === 0) {
        showToast('출제 대상 문항이 없습니다.');
        pauseAutoPlayer();
        return;
      }

      if (!apCurrentTopicId || !pool.some(t => t.id === apCurrentTopicId)) {
        apCurrentTopicId = pool[0].id;
      }

      runAutoPlayerLoop();
    }

    function pauseAutoPlayer() {
      apIsPlaying = false;
      const btn = document.getElementById('btnApPlayToggle');
      const txt = document.getElementById('txtApPlayToggle');
      if (btn) btn.classList.remove('playing');
      if (txt) txt.textContent = '▶️ 연속 재생 시작';

      stopAllCurrentApAudio();
      clearInterval(apCountdownInterval);
      clearTimeout(apLoopTimeout);

      updateApBanner('paused', '⏸️ 연속 자동 재생이 일시정지되었습니다.');
      document.getElementById('btnApSkipWait').style.display = 'none';
      document.getElementById('apProgressBar').style.width = '0%';
    }

    function stopAutoPlayerLoop() {
      pauseAutoPlayer();
      apCurrentStep = 'idle';
    }

    function stepAutoPlayer(direction) {
      stopAllCurrentApAudio();
      clearInterval(apCountdownInterval);
      clearTimeout(apLoopTimeout);

      const pool = getApFilteredPool();
      if (pool.length === 0) return;

      if (apOrder === 'random') {
        let candidates = pool.filter(t => t.id !== apCurrentTopicId);
        if (candidates.length === 0) candidates = pool;
        const nextTopic = candidates[Math.floor(Math.random() * candidates.length)];
        apCurrentTopicId = nextTopic.id;
      } else {
        let idx = pool.findIndex(t => t.id === apCurrentTopicId);
        if (idx === -1) idx = 0;
        let nextIdx = idx + direction;
        if (nextIdx < 0) nextIdx = pool.length - 1;
        if (nextIdx >= pool.length) nextIdx = 0;
        apCurrentTopicId = pool[nextIdx].id;
      }

      const topic = currentTopics.find(t => t.id === apCurrentTopicId);
      updateApTopicHeader(topic);

      if (apIsPlaying) {
        runAutoPlayerLoop();
      }
    }

    function stopAllCurrentApAudio() {
      if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
      }
      if (apCurrentAudioEl) {
        apCurrentAudioEl.pause();
        apCurrentAudioEl = null;
      }
    }

    function updateApBanner(stepClass, text, timerNotice = '') {
      const banner = document.getElementById('apStatusBanner');
      const statusText = document.getElementById('apStatusText');
      const timerNoticeEl = document.getElementById('apTimerNotice');
      if (banner) {
        banner.className = 'ap-status-banner ' + stepClass;
      }
      if (statusText) statusText.textContent = text;
      if (timerNoticeEl) timerNoticeEl.textContent = timerNotice;
    }

    // ==============================================================================
    // 🎧 연속 자동 루프 핵심 실행 머신
    // ==============================================================================
    async function runAutoPlayerLoop() {
      if (!apIsPlaying) return;

      const topic = currentTopics.find(t => t.id === apCurrentTopicId);
      if (!topic) {
        stepAutoPlayer(1);
        return;
      }
      updateApTopicHeader(topic);

      // STEP 1: 질문 읽기 (Question TTS)
      apCurrentStep = 'question';
      updateApBanner('speaking-q', '🔊 질문을 읽고 있습니다...', '질문 낭독');
      document.getElementById('btnApSkipWait').style.display = 'none';
      document.getElementById('apProgressBar').style.width = '0%';

      await playQuestionTTSAsync(topic.title);
      if (!apIsPlaying) return;

      // STEP 2: 대기 카운트다운 (10초 생각/답변 시간)
      apCurrentStep = 'countdown';
      document.getElementById('btnApSkipWait').style.display = 'inline-flex';
      updateApBanner('countdown', `⏳ 답변을 생각해보세요 (${apWaitSeconds}초 후 답변이 재생됩니다)`, `${apWaitSeconds}s`);

      const waitPassed = await runCountdownWaitAsync(apWaitSeconds);
      if (!apIsPlaying) return;

      // STEP 3: 답변 읽기 (Answer Playback)
      apCurrentStep = 'answer';
      document.getElementById('btnApSkipWait').style.display = 'none';
      document.getElementById('apProgressBar').style.width = '100%';

      await playAnswerAudioAsync(topic);
      if (!apIsPlaying) return;

      // STEP 4: 다음 문항으로 자동 전환 (1.5초 휴식 후 다음 루프)
      updateApBanner('', '✅ 답변 완료! 다음 문항으로 이동합니다...', '1.5s');
      apLoopTimeout = setTimeout(() => {
        if (!apIsPlaying) return;
        stepAutoPlayer(1);
      }, 1500);
    }

    // 1) 질문 TTS Promise
    function playQuestionTTSAsync(title) {
      return new Promise((resolve) => {
        if (!('speechSynthesis' in window)) {
          setTimeout(resolve, 2000);
          return;
        }
        window.speechSynthesis.cancel();

        const cleanQ = cleanTextForAnnouncerTTS(title);
        const utterance = new SpeechSynthesisUtterance(cleanQ);
        utterance.lang = 'ko-KR';
        utterance.rate = 1.0;
        utterance.pitch = 1.0;

        const voices = window.speechSynthesis.getVoices();
        const koVoice = voices.find(v => v.lang === 'ko-KR' || v.lang === 'ko_KR' || (v.lang && v.lang.startsWith('ko')));
        if (koVoice) utterance.voice = koVoice;

        utterance.onend = () => resolve();
        utterance.onerror = () => resolve();

        apCurrentUtterance = utterance;
        try {
          window.speechSynthesis.speak(utterance);
        } catch (e) {
          resolve();
        }
      });
    }

    // 2) 카운트다운 대기 Promise
    let countdownResolver = null;
    function runCountdownWaitAsync(seconds) {
      return new Promise((resolve) => {
        countdownResolver = resolve;
        apCountdownRemain = seconds;
        const total = seconds;

        const pBar = document.getElementById('apProgressBar');
        clearInterval(apCountdownInterval);

        apCountdownInterval = setInterval(() => {
          apCountdownRemain -= 0.1;
          const pct = Math.max(0, Math.min(100, ((total - apCountdownRemain) / total) * 100));
          if (pBar) pBar.style.width = `${pct}%`;

          const dispSec = Math.ceil(Math.max(0, apCountdownRemain));
          updateApBanner('countdown', `⏳ 답변을 생각해보세요 (${dispSec}초 후 답변이 재생됩니다)`, `${dispSec}s`);

          if (apCountdownRemain <= 0) {
            clearInterval(apCountdownInterval);
            countdownResolver = null;
            resolve(true);
          }
        }, 100);
      });
    }

    function skipAutoPlayerCountdown() {
      if (apCurrentStep === 'countdown' && countdownResolver) {
        clearInterval(apCountdownInterval);
        const res = countdownResolver;
        countdownResolver = null;
        res(true);
      }
    }

    // ==============================================================================
    // 3) 답변 재생 및 사람 음성 인식 검출 (VAD Silence Detection)
    // ==============================================================================
    async function playAnswerAudioAsync(topic) {
      const isPersonality = (topic.category === 'personality');

      // 모드가 'my_model_first'인 경우: 내 모범답안 녹음 우선 검사
      if (apAnswerMode === 'my_model_first') {
        const recId = getModelAudioRecordId(topic.id);
        const entry = await getAudioEntryForRecord(recId);

        let hasValidSpeech = false;
        if (entry && (entry.blob || entry.dataUrl)) {
          updateApBanner('speaking-ans', '🔍 녹음된 음성의 발화 유효성을 분석하고 있습니다...');
          hasValidSpeech = await checkAudioHasHumanSpeech(entry.blob);
        }

        if (hasValidSpeech && entry) {
          // 실제 사람 목소리가 감지된 내 녹음 파일 재생!
          updateApBanner('speaking-ans', '🎙️ 내가 녹음한 모범답안 음성을 재생합니다...', '내 음성');
          await playUserAudioElementAsync(entry.objectUrl || entry.dataUrl);
          return;
        } else {
          // 녹음이 없거나, 녹음은 되었으나 사람이 말하지 않은 무음/타이핑 전용인 경우
          const fallbackScript = (topic.speech_alt && topic.speech_alt.trim()) 
            ? topic.speech_alt 
            : (topic.speech_1m30s || '');

          const reasonMsg = (entry && (entry.blob || entry.dataUrl)) 
            ? 'ℹ️ 녹음에서 실제 발화가 감지되지 않아 작성된 모범답안을 아나운서가 읽습니다.' 
            : 'ℹ️ 녹음된 음성이 없어 모범답안을 아나운서 음성으로 읽습니다.';

          updateApBanner('speaking-ans', `🔊 ${reasonMsg}`, '아나운서');
          showToast(reasonMsg);
          await playAnnouncerSpeechTTSAsync(fallbackScript);
          return;
        }
      }

      // 모드가 'lecture_tts'인 경우: 심화해설 아나운서 낭독
      updateApBanner('speaking-ans', '📘 전문 아나운서 심화해설을 재생합니다...', '심화해설');
      const lectureScript = topic.speech_1m30s || topic.speech_alt || '';
      await playAnnouncerSpeechTTSAsync(lectureScript);
    }

    // 오디오 파일 내 실제 사람 음성 검출 (Web Audio API RMS & Peak 진폭 분석)
    async function checkAudioHasHumanSpeech(audioBlob) {
      if (!audioBlob || audioBlob.size < 6000) {
        console.log('Audio blob too small or missing:', audioBlob ? audioBlob.size : 0);
        return false;
      }

      try {
        const arrayBuffer = await audioBlob.arrayBuffer();
        const AudioContextClass = window.AudioContext || window.webkitAudioContext;
        if (!AudioContextClass) return true; // AudioContext 미지원 브라우저는 녹음 재생 시도

        const audioCtx = new AudioContextClass();
        const audioBuffer = await audioCtx.decodeAudioData(arrayBuffer);
        audioCtx.close();

        // 1초 미만이면 사람의 완전한 문장 발화로 보기 어려움
        if (audioBuffer.duration < 1.0) {
          console.log(`Audio duration too short: ${audioBuffer.duration.toFixed(2)}s`);
          return false;
        }

        const channelData = audioBuffer.getChannelData(0);
        let maxPeak = 0;
        let sumSquares = 0;
        let activeSamples = 0;

        // 연산 속도를 위해 20개 간격으로 서브샘플링
        const step = Math.max(1, Math.floor(channelData.length / 8000));
        let count = 0;
        for (let i = 0; i < channelData.length; i += step) {
          const amp = Math.abs(channelData[i]);
          if (amp > maxPeak) maxPeak = amp;
          sumSquares += amp * amp;
          if (amp >= 0.03) activeSamples++;
          count++;
        }

        const rms = Math.sqrt(sumSquares / count);
        const activeRatio = activeSamples / count;

        console.log(`[VAD Analysis] Peak: ${maxPeak.toFixed(4)}, RMS: ${rms.toFixed(4)}, ActiveRatio: ${(activeRatio*100).toFixed(1)}%, Duration: ${audioBuffer.duration.toFixed(1)}s`);

        // 유효 음성 기준:
        // 사람 발화 시 Peak >= 0.035, RMS >= 0.005, 유효 음성 샘플 비율 >= 3%
        const isHumanVoice = (maxPeak >= 0.035 && rms >= 0.004 && activeRatio >= 0.02);
        return isHumanVoice;
      } catch (err) {
        console.warn('Audio decoding for VAD failed, assume valid:', err);
        return true;
      }
    }

    // HTML5 Audio 엘리먼트 비동기 재생 Promise
    function playUserAudioElementAsync(src) {
      return new Promise((resolve) => {
        const audio = new Audio();
        audio.src = src;
        audio.preload = 'auto';
        apCurrentAudioEl = audio;

        audio.onended = () => {
          apCurrentAudioEl = null;
          resolve();
        };
        audio.onerror = () => {
          console.warn('User audio playback failed');
          apCurrentAudioEl = null;
          resolve();
        };

        audio.play().catch(err => {
          console.warn('Audio play interrupted:', err);
          apCurrentAudioEl = null;
          resolve();
        });
      });
    }

    // 아나운서 심화해설/대본 TTS Promise
    function playAnnouncerSpeechTTSAsync(rawText) {
      return new Promise((resolve) => {
        if (!('speechSynthesis' in window)) {
          setTimeout(resolve, 3000);
          return;
        }
        window.speechSynthesis.cancel();

        const cleanText = cleanTextForAnnouncerTTS(rawText);
        if (!cleanText) {
          resolve();
          return;
        }

        const utterance = new SpeechSynthesisUtterance(cleanText);
        utterance.lang = 'ko-KR';
        utterance.rate = 1.05;
        utterance.pitch = 1.0;

        const voices = window.speechSynthesis.getVoices();
        const koVoice = voices.find(v => v.lang === 'ko-KR' || v.lang === 'ko_KR' || (v.lang && v.lang.startsWith('ko')));
        if (koVoice) utterance.voice = koVoice;

        utterance.onend = () => {
          apCurrentUtterance = null;
          resolve();
        };
        utterance.onerror = () => {
          apCurrentUtterance = null;
          resolve();
        };

        apCurrentUtterance = utterance;
        try {
          window.speechSynthesis.speak(utterance);
        } catch (e) {
          resolve();
        }
      });
    }
"""

if "function toggleAutoPlayerDock" not in content:
    idx_last_script = content.rfind("</script>")
    if idx_last_script != -1:
        content = content[:idx_last_script] + "\n" + js_engine_to_add + "\n" + content[idx_last_script:]
        print("Injected auto-player JavaScript engine.")

# ==============================================================================
# 4. build-time 및 STORAGE_KEY 갱신
# ==============================================================================
new_storage_key = "aisk_master_topics_custom_v22_auto_player"
content = content.replace("aisk_master_topics_custom_v21_cleaned_tts", new_storage_key)

content = re.sub(
    r'<meta name="build-time" content="[^"]+">',
    '<meta name="build-time" content="2026-10-25T11:10:00+09:00">',
    content
)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Successfully integrated Auto-Player into {html_path}! Total size: {len(content)} bytes.")
