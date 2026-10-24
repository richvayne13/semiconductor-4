# -*- coding: utf-8 -*-
import re

html_path = r"C:\Work\반도체4_AISK대비\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. CSS 스타일 추가 (.btn-voice-toggle, .interview-speak-btn, .speaking 애니메이션)
css_to_add = """
    /* 질문 음성(TTS) & 자동 녹음 제어 스타일 */
    .btn-voice-toggle {
      padding: 7px 14px;
      font-size: 0.82rem;
      font-weight: 700;
      border-radius: 8px;
      border: 1px solid rgba(56, 189, 248, 0.35);
      background: rgba(15, 23, 42, 0.85);
      color: var(--text-sub);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
      font-family: inherit;
    }
    .btn-voice-toggle:hover {
      background: #1e293b;
      color: #fff;
    }
    .btn-voice-toggle.active {
      background: linear-gradient(135deg, rgba(6, 182, 212, 0.25) 0%, rgba(16, 185, 129, 0.25) 100%);
      border-color: #10b981;
      color: #34d399;
      box-shadow: 0 0 12px rgba(16, 185, 129, 0.3);
    }
    .interview-speak-btn {
      padding: 5px 12px;
      font-size: 0.78rem;
      font-weight: 700;
      border-radius: 6px;
      border: 1px solid rgba(56, 189, 248, 0.35);
      background: rgba(56, 189, 248, 0.12);
      color: #38bdf8;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.2s;
      font-family: inherit;
    }
    .interview-speak-btn:hover {
      background: #38bdf8;
      color: #0f172a;
    }
    .interview-speak-btn.speaking {
      background: #38bdf8;
      color: #0f172a;
      box-shadow: 0 0 14px rgba(56, 189, 248, 0.6);
      animation: recPulse 1.2s infinite;
    }
    .interview-q-title.speaking {
      color: #38bdf8;
      text-shadow: 0 0 14px rgba(56, 189, 248, 0.45);
      transition: all 0.3s;
    }
    .btn-record-toggle.waiting-voice {
      background: #0284c7;
      border-color: #38bdf8;
      animation: recPulse 1.5s infinite;
    }
"""

if ".btn-voice-toggle" not in content:
    content = content.replace("</style>", css_to_add + "\n  </style>")

# 2. HTML 컨트롤 바에 [🔊 자동 질문&녹음: ON] 버튼 추가
# <div class="interview-action-group"> 내부에 추가
old_action_group = """          <div class="interview-action-group">
            <button class="btn-random-interview" onclick="pickRandomInterviewTopic()" title="현재 카테고리에서 무작위 질문 추첨">
              <span>🎲 랜덤 문항 출제</span>
            </button>
            <button class="btn-step-interview" onclick="navigateInterviewTopic(-1)" title="이전 질문">◀ 이전</button>
            <span class="interview-progress-text" id="interviewProgressText">1 / 71</span>
            <button class="btn-step-interview" onclick="navigateInterviewTopic(1)" title="다음 질문">다음 ▶</button>
          </div>"""

new_action_group = """          <div class="interview-action-group">
            <button class="btn-voice-toggle active" id="btnAutoVoiceToggle" onclick="toggleAutoVoiceAndRecord()" title="문항 전환 시 질문 음성 자동 재생 후 녹음 자동 시작">
              <span id="btnAutoVoiceText">🔊 자동 질문&녹음: ON</span>
            </button>
            <button class="btn-random-interview" onclick="pickRandomInterviewTopic()" title="현재 카테고리에서 무작위 질문 추첨 (질문 음성 후 녹음 자동 시작)">
              <span>🎲 랜덤 문항 출제</span>
            </button>
            <button class="btn-step-interview" onclick="navigateInterviewTopic(-1)" title="이전 질문">◀ 이전</button>
            <span class="interview-progress-text" id="interviewProgressText">1 / 71</span>
            <button class="btn-step-interview" onclick="navigateInterviewTopic(1)" title="다음 질문 (질문 음성 후 녹음 자동 시작)">다음 ▶</button>
          </div>"""

if 'id="btnAutoVoiceToggle"' not in content and old_action_group in content:
    content = content.replace(old_action_group, new_action_group, 1)

# 3. 질문 카드 상단 헤더에 [🔊 질문 다시 듣기] 버튼 추가
old_hint_btn = """          <button class="interview-hint-toggle-btn" onclick="toggleInterviewHint()">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
            <span>핵심 키워드 힌트</span>
          </button>"""

new_hint_and_speak = """          <div style="display: flex; gap: 8px; align-items: center;">
            <button class="interview-speak-btn" id="btnSpeakQuestion" onclick="replayQuestionVoice()" title="질문 음성 재생 (음성이 끝나면 답변 녹음이 자동 시작됩니다)">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path></svg>
              <span id="btnSpeakText">🔊 질문 다시 듣기</span>
            </button>
            <button class="interview-hint-toggle-btn" onclick="toggleInterviewHint()">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
              <span>핵심 키워드 힌트</span>
            </button>
          </div>"""

if 'id="btnSpeakQuestion"' not in content and old_hint_btn in content:
    content = content.replace(old_hint_btn, new_hint_and_speak, 1)

# 4. 자바스크립트 로직 교체
# 기존 5. 랜덤 문항 출제 ~ 8. 녹음 및 Web Speech API 영역 교체
old_script_start = "    // 5. 랜덤 문항 출제"
old_script_end = "    // 9. 답변 기록 저장 (문항별 다회차 누적)"

idx_s = content.find(old_script_start)
idx_e = content.find(old_script_end)

if idx_s != -1 and idx_e != -1:
    new_script_block = """    // TTS(질문 음성) 및 자동 녹음 상태 관리
    let isSpeakingQuestion = false;
    let autoVoiceAndRecordEnabled = true; // 기본 ON: 랜덤/다음 이동 시 질문 음성 후 녹음 자동 시작
    let questionUtterance = null;

    // 질문 음성 및 자동 녹음 토글
    function toggleAutoVoiceAndRecord() {
      autoVoiceAndRecordEnabled = !autoVoiceAndRecordEnabled;
      const btn = document.getElementById('btnAutoVoiceToggle');
      const text = document.getElementById('btnAutoVoiceText');
      if (btn && text) {
        if (autoVoiceAndRecordEnabled) {
          btn.classList.add('active');
          text.innerHTML = '🔊 자동 질문&녹음: <strong>ON</strong>';
          showToast('🔊 문항 이동 시 질문 음성 재생 후 자동 녹음이 켜졌습니다.');
        } else {
          btn.classList.remove('active');
          text.innerHTML = '🔈 자동 질문&녹음: <strong>OFF</strong>';
          stopSpeakingQuestion();
          showToast('🔈 질문 음성 및 자동 녹음이 꺼졌습니다.');
        }
      }
    }

    // 질문 음성 중지
    function stopSpeakingQuestion() {
      if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
      }
      isSpeakingQuestion = false;
      questionUtterance = null;

      const qTitle = document.getElementById('intQTitle');
      if (qTitle) qTitle.classList.remove('speaking');

      const speakBtn = document.getElementById('btnSpeakQuestion');
      const speakText = document.getElementById('btnSpeakText');
      if (speakBtn) speakBtn.classList.remove('speaking');
      if (speakText) speakText.textContent = '🔊 질문 다시 듣기';

      const btnRecord = document.getElementById('btnRecordToggle');
      if (btnRecord && !isRecording) {
        btnRecord.classList.remove('waiting-voice');
        const btnText = document.getElementById('btnRecordText');
        if (btnText) btnText.textContent = '답변 녹음 시작 (STT)';
      }
    }

    // 질문 음성(TTS) 재생 후 콜백(자동 녹음) 실행
    function speakInterviewQuestion(topic, onEndCallback) {
      stopSpeakingQuestion();
      if (isRecording) {
        stopRecording();
      }

      if (!('speechSynthesis' in window)) {
        console.warn('SpeechSynthesis API not supported');
        if (onEndCallback) onEndCallback();
        return;
      }

      const text = (topic && topic.title) ? topic.title.trim() : '';
      if (!text) {
        if (onEndCallback) onEndCallback();
        return;
      }

      const utterance = new SpeechSynthesisUtterance(text);
      utterance.lang = 'ko-KR';
      utterance.rate = 1.0;
      utterance.pitch = 1.0;

      // 한국어 음성 탐색
      const voices = window.speechSynthesis.getVoices();
      const koVoice = voices.find(v => v.lang === 'ko-KR' || v.lang === 'ko_KR' || (v.lang && v.lang.startsWith('ko')));
      if (koVoice) {
        utterance.voice = koVoice;
      }

      isSpeakingQuestion = true;
      questionUtterance = utterance;

      // UI 상태 반영 (질문 읽는 중)
      const qTitle = document.getElementById('intQTitle');
      if (qTitle) qTitle.classList.add('speaking');

      const speakBtn = document.getElementById('btnSpeakQuestion');
      const speakText = document.getElementById('btnSpeakText');
      if (speakBtn) speakBtn.classList.add('speaking');
      if (speakText) speakText.textContent = '⏹️ 질문 중단';

      const btnRecord = document.getElementById('btnRecordToggle');
      const btnRecordText = document.getElementById('btnRecordText');
      const statusNotice = document.getElementById('recStatusNotice');
      const recDot = document.getElementById('recDot');

      if (btnRecord) btnRecord.classList.add('waiting-voice');
      if (btnRecordText) btnRecordText.textContent = '⏳ 질문 음성 재생 중...';
      if (statusNotice) statusNotice.textContent = '🔊 면접관 질문 음성 재생 중입니다... (음성이 끝나면 답변 녹음이 자동 시작됩니다)';
      if (recDot) recDot.style.background = '#38bdf8';

      let finished = false;
      const handleFinish = () => {
        if (finished) return;
        finished = true;
        isSpeakingQuestion = false;
        questionUtterance = null;

        if (qTitle) qTitle.classList.remove('speaking');
        if (speakBtn) speakBtn.classList.remove('speaking');
        if (speakText) speakText.textContent = '🔊 질문 다시 듣기';
        if (btnRecord) btnRecord.classList.remove('waiting-voice');

        if (onEndCallback) {
          onEndCallback();
        }
      };

      utterance.onend = handleFinish;
      utterance.onerror = (e) => {
        console.warn('SpeechSynthesis error:', e);
        handleFinish();
      };

      try {
        window.speechSynthesis.speak(utterance);
      } catch (err) {
        console.warn('SpeechSynthesis speak failed:', err);
        handleFinish();
      }
    }

    // 질문 다시 듣기 (수동 버튼)
    function replayQuestionVoice() {
      if (isSpeakingQuestion) {
        stopSpeakingQuestion();
        showToast('질문 음성을 중단했습니다.');
        return;
      }
      const topic = currentTopics.find(t => t.id === interviewCurrentTopicId);
      if (!topic) return;

      showToast('🔊 질문 음성을 재생합니다. 끝나면 녹음이 자동 시작됩니다.');
      speakInterviewQuestion(topic, () => {
        startRecording();
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
      
      // 자동 질문 음성 및 후속 녹음 트리거 (autoVoice = true)
      loadInterviewTopic(chosen.id, true);
      showToast(`🎲 랜덤 출제: [${chosen.title.slice(0, 22)}...]`);
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

      // 자동 질문 음성 및 후속 녹음 트리거 (autoVoice = true)
      loadInterviewTopic(pool[nextIndex].id, true);
    }

    // 7. 면접 문항 상세 로드 & UI 바인딩
    function loadInterviewTopic(id, autoVoice = false) {
      const topic = currentTopics.find(t => t.id === id);
      if (!topic) return;

      interviewCurrentTopicId = id;

      // 기존 음성 및 녹음 즉시 중지
      stopSpeakingQuestion();
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

      // 자동 질문 음성 및 후속 녹음 시작
      if (autoVoice && autoVoiceAndRecordEnabled) {
        speakInterviewQuestion(topic, () => {
          startRecording();
        });
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
      // 만약 질문 음성을 재생 중인 상태에서 버튼을 누르면, 질문을 멈추고 바로 녹음 시작
      if (isSpeakingQuestion) {
        stopSpeakingQuestion();
        startRecording();
        return;
      }

      if (isRecording) {
        stopRecording();
      } else {
        startRecording();
      }
    }

    function startRecording() {
      stopSpeakingQuestion();

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
      if (btn) {
        btn.classList.remove('waiting-voice');
        btn.classList.add('recording');
      }
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

      if (btn) {
        btn.classList.remove('recording');
        btn.classList.remove('waiting-voice');
      }
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
      stopSpeakingQuestion();
      const area = document.getElementById('intTranscriptArea');
      if (area) {
        area.value = '';
        updateInterviewCharCount();
      }
      resetRecordingTimer();
      if (isRecording) stopRecording();
      showToast('대사창이 비워졌습니다.');
    }

"""
    content = content[:idx_s] + new_script_block + content[idx_e:]

# 5. build-time 및 STORAGE_KEY 갱신
content = re.sub(
    r'<meta name="build-time" content="[^"]+">',
    '<meta name="build-time" content="2026-10-24T13:00:00+09:00">',
    content
)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully injected auto voice & recording features into index.html!")
