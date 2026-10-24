# -*- coding: utf-8 -*-
with open(r'C:\Work\반도체4_AISK대비\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. HTML 마크업: learnViewContainer 및 interviewViewContainer 구조 삽입
# topicContainer를 learnViewContainer로 감싸기
target_tc = """    <!-- 문항 카드 컨테이너 -->
    <div id="topicContainer">
      <!-- JavaScript로 동적 렌더링 -->
    </div>"""

interview_containers_html = """    <!-- 문항 카드 컨테이너 (학습 백과사전 모드) -->
    <div id="learnViewContainer">
      <div id="topicContainer">
        <!-- JavaScript로 동적 렌더링 -->
      </div>
    </div>

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
          <div style="display: flex; align-items: center; gap: 12px; flex-wrap: wrap;">
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
            <span id="intLenGuideNotice" style="font-size:0.75rem; color:var(--text-muted); margin-left:6px;">(권장 분량)</span>
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

    </div> <!-- /interviewViewContainer -->"""

if target_tc in html:
    html = html.replace(target_tc, interview_containers_html)
    print("Replaced topicContainer with learnViewContainer and interviewViewContainer successfully!")
else:
    print("Warning: target_tc not found!")

# 2. 자바스크립트 로직 추가: 면접 모드 제어, STT 음성인식, 랜덤 출제, 히스토리 저장
interview_js = """
    // ========================================================
    // 🎙️ 실전 면접 모드 (Interview Mode) 핵심 엔진
    // ========================================================
    let currentViewMode = 'learn'; // 'learn' | 'interview'
    let interviewCurrentTopicId = null;
    let interviewCategory = 'all'; // 'all' | 'personality' | 'tech'
    let interviewProcess = 'ALL'; // 'ALL', 'COM', 'W', 'O', 'P', 'E', 'D', 'I', 'M', 'PKG', 'DEV'
    
    // 녹음 / STT 관련 상태
    let isRecording = false;
    let recognition = null;
    let recTimerInterval = null;
    let recSeconds = 0;
    const INTERVIEW_RECORDS_KEY_PREFIX = 'aisk_interview_history_';

    // 1. 모드 전환 함수
    function toggleViewMode(mode) {
      currentViewMode = mode;
      const body = document.body;
      const btnLearnMain = document.getElementById('btnModeLearnMain');
      const btnIntMain = document.getElementById('btnModeInterviewMain');
      const btnLearnSide = document.getElementById('btnModeLearnSide');
      const btnIntSide = document.getElementById('btnModeInterviewSide');
      const mobBtn = document.getElementById('mobModeBtn');

      if (mode === 'interview') {
        body.classList.add('interview-mode');
        if (btnLearnMain) btnLearnMain.classList.remove('active');
        if (btnIntMain) btnIntMain.classList.add('active');
        if (btnLearnSide) btnLearnSide.classList.remove('active');
        if (btnIntSide) btnIntSide.classList.add('active');
        if (mobBtn) mobBtn.textContent = '📖 학습';

        // 현재 문항이 없으면 랜덤 또는 첫 번째 문항 로드
        if (!interviewCurrentTopicId) {
          pickRandomInterviewTopic();
        } else {
          loadInterviewTopic(interviewCurrentTopicId);
        }
        showToast('🎙️ 실전 면접 모드로 전환되었습니다. 랜덤 출제나 녹음으로 연습해보세요!');
      } else {
        body.classList.remove('interview-mode');
        if (btnLearnMain) btnLearnMain.classList.add('active');
        if (btnIntMain) btnIntMain.classList.remove('active');
        if (btnLearnSide) btnLearnSide.classList.add('active');
        if (btnIntSide) btnIntSide.classList.remove('active');
        if (mobBtn) mobBtn.textContent = '🎙️ 면접';
        showToast('📖 학습 백과사전 모드로 전환되었습니다.');
      }
    }

    // 2. 면접 카테고리 선택 (전체 / 인성 / 직무)
    function selectInterviewCategory(cat) {
      interviewCategory = cat;
      document.querySelectorAll('.interview-cat-btn').forEach(btn => btn.classList.remove('active'));

      if (cat === 'all') {
        const el = document.getElementById('intCatAll');
        if (el) el.classList.add('active');
        const procChips = document.getElementById('interviewProcChips');
        if (procChips) procChips.style.display = 'flex';
      } else if (cat === 'personality') {
        const el = document.getElementById('intCatPersonality');
        if (el) el.classList.add('active');
        const procChips = document.getElementById('interviewProcChips');
        if (procChips) procChips.style.display = 'none';
      } else if (cat === 'tech') {
        const el = document.getElementById('intCatTech');
        if (el) el.classList.add('active');
        const procChips = document.getElementById('interviewProcChips');
        if (procChips) procChips.style.display = 'flex';
      }

      pickRandomInterviewTopic();
    }

    // 3. 직무 내 공정 서브필터 선택 (WOPEDIMP + 공통 + 소자)
    function selectInterviewProcess(proc) {
      interviewProcess = proc;
      document.querySelectorAll('#interviewProcChips .proc-chip').forEach(btn => {
        if (btn.getAttribute('data-intproc') === proc) {
          btn.classList.add('active');
        } else {
          btn.classList.remove('active');
        }
      });
      pickRandomInterviewTopic();
    }

    // 4. 현재 조건에 맞는 문항 풀(Pool) 추출
    function getFilteredInterviewPool() {
      return currentTopics.filter(t => {
        if (interviewCategory === 'personality') {
          return t.category === 'personality';
        } else if (interviewCategory === 'tech') {
          if (t.category !== 'tech') return false;
          if (interviewProcess !== 'ALL') {
            return (t.process || '') === interviewProcess;
          }
          return true;
        } else {
          // all
          if (interviewProcess !== 'ALL') {
            return t.category === 'tech' && (t.process || '') === interviewProcess;
          }
          return true;
        }
      });
    }

    // 5. 랜덤 문항 출제
    function pickRandomInterviewTopic() {
      const pool = getFilteredInterviewPool();
      if (pool.length === 0) {
        showToast('해당 조건의 문항이 없습니다.');
        return;
      }

      // 현재 문항을 제외한 후보에서 선택
      let candidates = pool.filter(t => t.id !== interviewCurrentTopicId);
      if (candidates.length === 0) candidates = pool;

      const randomIndex = Math.floor(Math.random() * candidates.length);
      const chosen = candidates[randomIndex];
      loadInterviewTopic(chosen.id);
      showToast(`🎲 랜덤 출제: [${chosen.title.slice(0, 24)}...]`);
    }

    // 6. 이전/다음 문항 이동
    function navigateInterviewTopic(direction) {
      const pool = getFilteredInterviewPool();
      if (pool.length === 0) return;

      let currentIndex = pool.findIndex(t => t.id === interviewCurrentTopicId);
      if (currentIndex === -1) currentIndex = 0;

      let nextIndex = currentIndex + direction;
      if (nextIndex < 0) nextIndex = pool.length - 1;
      if (nextIndex >= pool.length) nextIndex = 0;

      loadInterviewTopic(pool[nextIndex].id);
    }

    // 7. 면접 문항 상세 로드 & UI 바인딩
    function loadInterviewTopic(id) {
      const topic = currentTopics.find(t => t.id === id);
      if (!topic) return;

      interviewCurrentTopicId = id;

      // 녹음 중이었다면 정지
      if (isRecording) {
        stopRecording();
      }

      // 텍스트창 및 타이머 초기화
      const transcriptArea = document.getElementById('intTranscriptArea');
      if (transcriptArea) transcriptArea.value = '';
      updateInterviewCharCount();
      resetRecordingTimer();

      // 배지 및 카테고리
      const badgeEl = document.getElementById('intQBadge');
      const catEl = document.getElementById('intQCategory');
      const titleEl = document.getElementById('intQTitle');
      const progressEl = document.getElementById('interviewProgressText');

      const isPersonality = (topic.category === 'personality');
      const proc = topic.process || '';
      let numStr = '';
      if (isPersonality) {
        numStr = `인성-${String(topic.number || 1).padStart(2, '0')}`;
        if (badgeEl) {
          badgeEl.className = 'interview-q-badge cat-badge-p';
          badgeEl.textContent = numStr;
        }
      } else {
        if (proc === 'DEV') numStr = `소자-${String(topic.number || 1).padStart(2, '0')}`;
        else if (proc === 'COM') numStr = `공통-${String(topic.number || 1).padStart(2, '0')}`;
        else if (proc) numStr = `${proc}-${String(topic.number || 1).padStart(2, '0')}`;
        else numStr = `직무-${String(topic.number || 1).padStart(2, '0')}`;

        if (badgeEl) {
          badgeEl.className = 'interview-q-badge cat-badge-t';
          badgeEl.textContent = numStr;
        }
      }

      if (catEl) catEl.textContent = topic.category_label || (isPersonality ? '인성·협업 가치' : '반도체 직무·공정·소자');
      if (titleEl) titleEl.textContent = topic.title;

      // 진행률 번호 표시 (현재 풀 내 위치)
      const pool = getFilteredInterviewPool();
      const currIdx = pool.findIndex(t => t.id === id);
      if (progressEl) {
        progressEl.textContent = `${currIdx >= 0 ? currIdx + 1 : 1} / ${pool.length}`;
      }

      // 키워드 힌트 목록
      const kwListEl = document.getElementById('intKeywordsList');
      if (kwListEl) {
        const kws = topic.core_keyword || [];
        kwListEl.innerHTML = kws.map(k => `<span class="kw-pill">#${escapeHtml(k)}</span>`).join('');
      }
      // 힌트 박스는 기본 접힘
      const hintBox = document.getElementById('intHintBox');
      if (hintBox) hintBox.classList.remove('show');

      // 글자 수 권장 분량 안내
      const lenNotice = document.getElementById('intLenGuideNotice');
      if (lenNotice) {
        lenNotice.textContent = isPersonality ? '(인성 1분 권장: 250~330자)' : '(직무 3분 권장: 800~1300자)';
      }

      // 나의 이전 답변 히스토리 렌더링
      renderInterviewHistory(id);

      // 모범답안 렌더링 (하단)
      renderInterviewModelAnswer(topic);

      // 사이드바 active 링크 동기화
      document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
      const activeLink = document.getElementById(`link-${id}`);
      if (activeLink) {
        activeLink.classList.add('active');
        activeLink.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    }

    // 키워드 힌트 토글
    function toggleInterviewHint() {
      const hintBox = document.getElementById('intHintBox');
      if (hintBox) {
        hintBox.classList.toggle('show');
      }
    }

    // 8. 녹음 및 Web Speech API (STT 실시간 음성인식)
    function toggleRecording() {
      if (isRecording) {
        stopRecording();
      } else {
        startRecording();
      }
    }

    function startRecording() {
      const btn = document.getElementById('btnRecordToggle');
      const btnText = document.getElementById('btnRecordText');
      const statusNotice = document.getElementById('recStatusNotice');
      const recDot = document.getElementById('recDot');

      // 브라우저 SpeechRecognition 확인
      const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

      if (SpeechRecognition) {
        try {
          recognition = new SpeechRecognition();
          recognition.lang = 'ko-KR';
          recognition.continuous = true;
          recognition.interimResults = true;

          const transcriptArea = document.getElementById('intTranscriptArea');
          let finalTranscript = transcriptArea.value ? (transcriptArea.value + ' ') : '';

          recognition.onresult = (event) => {
            let interim = '';
            for (let i = event.resultIndex; i < event.results.length; ++i) {
              if (event.results[i].isFinal) {
                finalTranscript += event.results[i][0].transcript + ' ';
              } else {
                interim += event.results[i][0].transcript;
              }
            }
            transcriptArea.value = (finalTranscript + interim).trim();
            updateInterviewCharCount();
          };

          recognition.onerror = (event) => {
            console.warn('SpeechRecognition error:', event.error);
            if (event.error === 'not-allowed') {
              showToast('⚠️ 마이크 사용 권한을 허용해주세요.');
              stopRecording();
            }
          };

          recognition.onend = () => {
            // 녹음 중 상태인데 브라우저가 자동 중단했을 경우 재시작
            if (isRecording) {
              try { recognition.start(); } catch (e) {}
            }
          };

          recognition.start();
        } catch (e) {
          console.warn('Recognition start failed:', e);
        }
      } else {
        showToast('ℹ️ 현재 브라우저는 실시간 STT 음성인식을 지원하지 않아 타이머만 동작합니다. (Chrome 권장)');
      }

      isRecording = true;
      if (btn) btn.classList.add('recording');
      if (btnText) btnText.textContent = '⏹️ 답변 완료 (녹음 종료)';
      if (statusNotice) statusNotice.textContent = '🎙️ 녹음 및 자동 대사 인식 중입니다. 편안하게 답변을 말해보세요...';
      if (recDot) recDot.style.background = '#ef4444';

      // 타이머 시작
      recSeconds = 0;
      updateTimerDisplay(recSeconds);
      clearInterval(recTimerInterval);
      recTimerInterval = setInterval(() => {
        recSeconds++;
        updateTimerDisplay(recSeconds);
      }, 1000);
    }

    function stopRecording() {
      isRecording = false;
      const btn = document.getElementById('btnRecordToggle');
      const btnText = document.getElementById('btnRecordText');
      const statusNotice = document.getElementById('recStatusNotice');
      const recDot = document.getElementById('recDot');

      if (btn) btn.classList.remove('recording');
      if (btnText) btnText.textContent = '답변 녹음 시작 (STT)';
      if (statusNotice) statusNotice.textContent = '답변 녹음이 종료되었습니다. 아래에서 수정하거나 [이번 답변 기록 저장]을 누르세요.';
      if (recDot) recDot.style.background = '#64748b';

      clearInterval(recTimerInterval);
      recTimerInterval = null;

      if (recognition) {
        try { recognition.stop(); } catch (e) {}
        recognition = null;
      }
    }

    function resetRecordingTimer() {
      clearInterval(recTimerInterval);
      recTimerInterval = null;
      recSeconds = 0;
      updateTimerDisplay(0);
      const recDot = document.getElementById('recDot');
      if (recDot) recDot.style.background = '#64748b';
    }

    function updateTimerDisplay(sec) {
      const display = document.getElementById('recTimerDisplay');
      if (!display) return;
      const m = String(Math.floor(sec / 60)).padStart(2, '0');
      const s = String(sec % 60).padStart(2, '0');
      display.textContent = `${m}:${s}`;
    }

    // 텍스트 글자 수 갱신
    function updateInterviewCharCount() {
      const area = document.getElementById('intTranscriptArea');
      const countEl = document.getElementById('intTranscriptLen');
      if (area && countEl) {
        countEl.textContent = `${area.value.length}자`;
      }
    }

    // 실시간 글자수 input 리스너
    document.addEventListener('input', (e) => {
      if (e.target && e.target.id === 'intTranscriptArea') {
        updateInterviewCharCount();
      }
    });

    function clearCurrentTranscript() {
      const area = document.getElementById('intTranscriptArea');
      if (area) {
        area.value = '';
        updateInterviewCharCount();
      }
      resetRecordingTimer();
      if (isRecording) stopRecording();
      showToast('대사창이 비워졌습니다.');
    }

    // 9. 답변 기록 저장 (문항별 다회차 누적)
    function saveCurrentInterviewRecord() {
      const area = document.getElementById('intTranscriptArea');
      if (!area || !area.value.trim()) {
        showToast('⚠️ 저장할 답변 내용이 없습니다. 먼저 말하거나 작성해주세요.');
        return;
      }

      if (!interviewCurrentTopicId) return;

      if (isRecording) {
        stopRecording();
      }

      const text = area.value.trim();
      const storageKey = INTERVIEW_RECORDS_KEY_PREFIX + interviewCurrentTopicId;
      let history = [];
      try {
        const saved = localStorage.getItem(storageKey);
        if (saved) history = JSON.parse(saved);
      } catch (e) {}

      const durationStr = (recSeconds > 0) ? `${Math.floor(recSeconds / 60)}분 ${recSeconds % 60}초` : '시간 미측정';

      const newRecord = {
        id: 'rec_' + Date.now(),
        tryNumber: history.length + 1,
        date: new Date().toLocaleString('ko-KR', { month:'numeric', day:'numeric', hour:'2-digit', minute:'2-digit' }),
        durationSeconds: recSeconds,
        durationFormatted: durationStr,
        text: text,
        charCount: text.length
      };

      history.unshift(newRecord); // 최신 기록을 맨 위에 배치
      localStorage.setItem(storageKey, JSON.stringify(history));

      showToast(`🎉 [제 ${newRecord.tryNumber}회차] 답변 기록이 성공적으로 저장되었습니다!`);
      renderInterviewHistory(interviewCurrentTopicId);

      // 대사창 비우기 및 타이머 리셋
      area.value = '';
      updateInterviewCharCount();
      resetRecordingTimer();
    }

    // 10. 답변 히스토리 렌더링
    function renderInterviewHistory(topicId) {
      const listEl = document.getElementById('intHistoryList');
      const badgeEl = document.getElementById('historyCountBadge');
      if (!listEl) return;

      const storageKey = INTERVIEW_RECORDS_KEY_PREFIX + topicId;
      let history = [];
      try {
        const saved = localStorage.getItem(storageKey);
        if (saved) history = JSON.parse(saved);
      } catch (e) {}

      if (badgeEl) {
        badgeEl.textContent = `${history.length}회 연습함`;
      }

      if (history.length === 0) {
        listEl.innerHTML = `
          <div style="text-align:center; padding: 24px 16px; color: var(--text-muted); font-size: 0.88rem; border: 1px dashed var(--border); border-radius: 8px;">
            아직 이 문항에 대한 연습 기록이 없습니다.<br>
            위에서 [답변 녹음 시작]을 눌러 첫 번째 답변을 기록해보세요!
          </div>
        `;
        return;
      }

      let html = '';
      history.forEach(rec => {
        html += `
          <div class="history-card-item" id="${rec.id}">
            <div class="history-card-meta">
              <div style="display:flex; align-items:center; gap:8px;">
                <span class="history-try-badge">제 ${rec.tryNumber}회차</span>
                <span>⏱️ ${rec.durationFormatted}</span>
                <span>📝 ${rec.charCount}자</span>
                <span style="opacity:0.6;">· ${rec.date}</span>
              </div>
              <div style="display:flex; gap:6px;">
                <button class="btn-card-action" onclick="copyRecordText('${rec.id}')" title="이 기록 복사">
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                  복사
                </button>
                <button class="btn-card-action" onclick="deleteInterviewRecord('${topicId}', '${rec.id}')" title="이 기록 삭제" style="color:#ef4444;">
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>
                  삭제
                </button>
              </div>
            </div>
            <div class="history-card-text" id="text-${rec.id}">${escapeHtml(rec.text)}</div>
          </div>
        `;
      });

      listEl.innerHTML = html;
    }

    function copyRecordText(recId) {
      const el = document.getElementById(`text-${recId}`);
      if (!el) return;
      navigator.clipboard.writeText(el.innerText).then(() => {
        showToast('📋 답변 기록이 클립보드에 복사되었습니다.');
      });
    }

    function deleteInterviewRecord(topicId, recId) {
      if (!confirm('이 답변 기록을 삭제하시겠습니까?')) return;

      const storageKey = INTERVIEW_RECORDS_KEY_PREFIX + topicId;
      let history = [];
      try {
        const saved = localStorage.getItem(storageKey);
        if (saved) history = JSON.parse(saved);
      } catch (e) {}

      history = history.filter(r => r.id !== recId);
      localStorage.setItem(storageKey, JSON.stringify(history));
      renderInterviewHistory(topicId);
      showToast('기록이 삭제되었습니다.');
    }

    // 11. 하단 모범답안 렌더링 & 토글
    function renderInterviewModelAnswer(topic) {
      const container = document.getElementById('modelAnswerText');
      if (!container) return;

      const isPersonality = (topic.category === 'personality');
      let html = '';

      if (isPersonality) {
        html += `
          <div style="margin-bottom: 16px;">
            <div style="font-size:0.88rem; font-weight:800; color:var(--accent-blue); margin-bottom:8px;">[답변 1] 1분 30초~2분 실전 핵심 모범답안</div>
            <div class="speech-body" style="background:#1e293b; padding:12px 14px; border-radius:8px; border:1px solid var(--border); font-size:0.98rem; line-height:1.8;">${formatSpeechHtml(topic.speech_1m30s)}</div>
          </div>
        `;
        if (topic.speech_alt) {
          html += `
            <div>
              <div style="font-size:0.88rem; font-weight:800; color:var(--accent-emerald); margin-bottom:8px;">[답변 2] 1분 30초~2분 실전 대안 관점 모범답안</div>
              <div class="speech-body" style="background:#1e293b; padding:12px 14px; border-radius:8px; border:1px solid var(--border); font-size:0.98rem; line-height:1.8;">${formatSpeechHtml(topic.speech_alt)}</div>
            </div>
          `;
        }
      } else {
        html += `
          <div>
            <div style="font-size:0.88rem; font-weight:800; color:var(--primary-light); margin-bottom:8px;">[3분 심층 마스터 모범답안] 원리·수식·양산 심화 해설</div>
            <div class="speech-body" style="background:#1e293b; padding:12px 14px; border-radius:8px; border:1px solid var(--border); font-size:0.98rem; line-height:1.8;">${formatSpeechHtml(topic.speech_1m30s)}</div>
          </div>
        `;
      }

      container.innerHTML = html;
    }

    function toggleModelAnswer() {
      const content = document.getElementById('modelBodyContent');
      const icon = document.getElementById('modelToggleIcon');
      if (!content) return;

      content.classList.toggle('open');
      if (icon) {
        icon.style.transform = content.classList.contains('open') ? 'rotate(180deg)' : 'rotate(0deg)';
      }
    }

    function copyModelAnswer() {
      const topic = currentTopics.find(t => t.id === interviewCurrentTopicId);
      if (!topic) return;
      const text = topic.speech_1m30s ? topic.speech_1m30s.replace(/<[^>]+>/g, '') : '';
      navigator.clipboard.writeText(text).then(() => {
        showToast('📋 모범답안 텍스트가 클립보드에 복사되었습니다.');
      });
    }

    // 12. 사이드바 클릭 인터셉트 (면접 모드일 때 면접 뷰 질문 로드)
    document.addEventListener('click', (e) => {
      const navLink = e.target.closest('.nav-link');
      if (!navLink) return;

      const href = navLink.getAttribute('href');
      if (href && href.startsWith('#')) {
        const targetId = href.substring(1);
        if (currentViewMode === 'interview') {
          e.preventDefault();
          loadInterviewTopic(targetId);
          if (window.innerWidth <= 1024) {
            closeDrawer();
          }
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }
      }
    });
"""

# 스크립트 파일 끝 부분에 추가
pos_script_end = html.rfind('</script>')
if pos_script_end != -1 and 'toggleViewMode' not in html[pos_script_end-2000:pos_script_end]:
    html = html[:pos_script_end] + interview_js + '\n  ' + html[pos_script_end:]
    print("Added interview mode JS engine successfully.")

# 파일 저장
with open(r'C:\Work\반도체4_AISK대비\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html size:", len(html))
