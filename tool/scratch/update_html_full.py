import json
import re

# Load the updated topics
with open("context/data/aisk_curated_topics.json", "r", encoding="utf-8") as f:
    topics = json.load(f)

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Replace DEFAULT_TOPICS
m = re.search(r'const DEFAULT_TOPICS = (\[.*?\]);', content, re.DOTALL)
if not m:
    raise ValueError("DEFAULT_TOPICS not found")

topics_json = json.dumps(topics, ensure_ascii=False, indent=2)
content = content[:m.start(1)] + topics_json + content[m.end(1):]

# 2. Update STORAGE_KEY to v4
content = re.sub(
    r"const STORAGE_KEY = 'aisk_master_topics_custom_v\d+';",
    "const STORAGE_KEY = 'aisk_master_topics_custom_v4';",
    content
)

# 3. Update header description and quick edit banner
old_desc = """        <p class="main-desc">
          인성·협업 가치와 소자·공정 실전 핵심 문항을 마스터하는 인터랙티브 학습 시스템입니다.<br>
          각 카드의 제목이나 1분 30초 본문을 <strong>클릭하여 즉시 타이핑 수정</strong>할 수 있으며, <strong>[➕ 신규 항목 추가]</strong>로 나만의 문항을 무제한 등록하고 영구 보존할 수 있습니다.
        </p>
        <!-- 직접 클릭 수정 안내 배너 -->
        <div class="quick-edit-banner">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#38bdf8" stroke-width="2"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg>
          <span><strong>원클릭 직접 편집 지원:</strong> 별도의 수정 버튼 없이 제목이나 답변 상자를 <strong>한 번만 클릭</strong>하면 즉시 타이핑하여 수정할 수 있으며, <strong>입력 즉시 자동 저장</strong>됩니다.</span>
        </div>"""

new_desc = """        <p class="main-desc">
          인성 질문(<strong>1분 실전 호흡: 약 280자</strong>)과 직무 질문(<strong>3분 심층 마스터: 약 900자</strong>)으로 최적화된 마스터 시스템입니다.<br>
          각 카드의 제목이나 본문을 <strong>클릭하여 즉시 타이핑 수정</strong>할 수 있으며, <strong>[➕ 신규 항목 추가]</strong>로 나만의 문항을 무제한 등록하고 영구 보존할 수 있습니다.
        </p>
        <!-- 직접 클릭 수정 안내 배너 -->
        <div class="quick-edit-banner">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#38bdf8" stroke-width="2"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg>
          <span><strong>인성 1분 / 직무 3분 맞춤 분량 &amp; 원클릭 편집:</strong> 인성 문항은 1분(250~330자), 직무 문항은 3분(800~1300자)으로 설계되었으며, <strong>한 번만 클릭</strong>하면 바로 수정 및 실시간 자동 저장됩니다.</span>
        </div>"""

if old_desc in content:
    content = content.replace(old_desc, new_desc)
    print("Replaced main-desc and quick-edit-banner")
else:
    print("old_desc match failed, checking...")

# 4. Update Timer Widget HTML
old_timer_html = """      <!-- 1분 30초 실전 스톱워치 위젯 -->
      <div class="timer-widget">
        <div class="timer-header">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
          1분 30초 실전 타이머
        </div>
        <div class="timer-display" id="timerDisplay">01:30</div>
        <div class="timer-controls">
          <button class="timer-btn start" id="timerStartBtn">시작</button>
          <button class="timer-btn" id="timerPauseBtn">정지</button>
          <button class="timer-btn" id="timerResetBtn">초기화</button>
        </div>
        <div class="timer-progress-bar">
          <div class="timer-progress" id="timerProgress"></div>
        </div>
      </div>"""

new_timer_html = """      <!-- 실전 스톱워치 위젯 (1분 인성 / 3분 직무 모드 전환) -->
      <div class="timer-widget">
        <div class="timer-header">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
          <span id="timerTitleText">1분 실전 타이머 (인성)</span>
        </div>
        <div class="timer-mode-group">
          <button class="timer-mode-btn active" id="mode1mBtn" onclick="switchTimerMode(60)">1분 (인성)</button>
          <button class="timer-mode-btn" id="mode3mBtn" onclick="switchTimerMode(180)">3분 (직무)</button>
        </div>
        <div class="timer-display" id="timerDisplay">01:00</div>
        <div class="timer-controls">
          <button class="timer-btn start" id="timerStartBtn">시작</button>
          <button class="timer-btn" id="timerPauseBtn">정지</button>
          <button class="timer-btn" id="timerResetBtn">초기화</button>
        </div>
        <div class="timer-progress-bar">
          <div class="timer-progress" id="timerProgress"></div>
        </div>
      </div>"""

if old_timer_html in content:
    content = content.replace(old_timer_html, new_timer_html)
    print("Replaced timer widget HTML")
else:
    print("old_timer_html match failed, checking...")

# 5. Add Timer Mode Group CSS if not present
if ".timer-mode-group" not in content:
    mode_css = """    .timer-mode-group {
      display: flex;
      gap: 6px;
      margin-bottom: 10px;
    }
    .timer-mode-btn {
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 0.76rem;
      font-weight: 700;
      cursor: pointer;
      border: 1px solid var(--border);
      background: #1e293b;
      color: var(--text-sub);
      transition: all 0.15s;
    }
    .timer-mode-btn:hover {
      color: #ffffff;
      border-color: #38bdf8;
    }
    .timer-mode-btn.active {
      background: rgba(56, 189, 248, 0.2);
      border-color: #38bdf8;
      color: #38bdf8;
    }
    .len-guide-sub {
      font-size: 0.72rem;
      color: #94a3b8;
      margin-left: 4px;
      font-weight: normal;
    }
"""
    content = content.replace(".timer-controls {", mode_css + "\n    .timer-controls {")
    print("Added timer-mode-group CSS")

# 6. Update renderCards and lenTag logic
# Find renderCards
old_render_part = """        const kwPills = keywords.map(kw => `<span class="kw-pill">#${escapeHtml(kw)}</span>`).join('');
        const corePtsHtml = (lecture.core_points || []).map(pt => `<li>${escapeHtml(pt)}</li>`).join('');
        const actionPrincipleHtml = (lecture.action_principle || '').replace(/\\n/g, '<br>');

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
                  <div class="speech-len-tag">실전 호흡: <strong id="len-tag-${t.id}">${speechCharCount}자</strong></div>
                  <span class="save-status-badge" id="save-status-${t.id}">클릭하여 바로 수정</span>
                  <button class="btn-card-action delete-btn" onclick="deleteTopic('${t.id}')" title="이 문항 삭제">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>
                    삭제
                  </button>
                </div>
              </div>

              <!-- 제목 (클릭 시 즉시 수정) -->
              <h2 class="topic-title editable-field" contenteditable="true" data-field="title" data-id="${t.id}" title="클릭하여 제목 바로 수정">${title}</h2>

              <!-- 1분 30초 실전 핵심 전달 카드 (본문 클릭 시 즉시 작성/수정) -->
              <div class="speech-card">
                <div class="speech-card-header">
                  <div class="speech-card-title">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="22"></line></svg>
                    <span>1분 30초 실전 핵심 전달 (구어체 최적화 호흡)</span>
                  </div>
                  <span class="speech-click-hint">✏️ 클릭하여 바로 작성·수정 (자동 저장)</span>
                  <button class="btn-card-action" onclick="copySpeech('${t.id}')" title="답변 복사">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                    복사
                  </button>
                </div>
                <div class="speech-body editable-field" contenteditable="true" data-field="speech_1m30s" data-id="${t.id}" id="speech-text-${t.id}" title="클릭하여 바로 수정 (자동 저장)">${escapeHtml(speech)}</div>
                <div class="speech-guide-footer">
                  <span class="guide-tip">💡 팁: 첫 10초에 두괄식 핵심 메시지를 각인시키고, 60초간 구체적 데이터·원리를 전개한 후, 마지막 20초에 양산 수율 기여로 완결합니다.</span>
                </div>
              </div>"""

new_render_part = """        const kwPills = keywords.map(kw => `<span class="kw-pill">#${escapeHtml(kw)}</span>`).join('');
        const isPersonality = (cat === 'personality');
        const cardHeaderTitle = isPersonality 
          ? '1분 실전 핵심 전달 (구어체 호흡 · 약 250~330자)' 
          : '3분 심층 기술 마스터 전달 (원리·수식·양산 심화 · 약 800~1300자)';
        const cardLenGuide = isPersonality ? '1분 권장: 250~330자' : '3분 권장: 800~1300자';
        const guideTip = isPersonality
          ? '💡 팁: 첫 10초에 두괄식 핵심 메시지를 각인시키고, 40초간 구체적 행동/근거를 전개한 후, 마지막 10초에 조직 가치 기여로 완결합니다.'
          : '💡 팁: 첫 30초에 물리적 정의 및 아키텍처를 제시하고, 2분간 공학적 메커니즘·수식·트레이드오프를 심층 전개한 후, 마지막 30초에 SK하이닉스 양산 수율/품질 개선 기여로 완결합니다.';

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
                <div class="speech-guide-footer">
                  <span class="guide-tip">${guideTip}</span>
                </div>
              </div>"""

if old_render_part in content:
    content = content.replace(old_render_part, new_render_part)
    print("Replaced renderCards speech card template")
else:
    print("old_render_part match failed, checking...")

# 7. Add getLenColor helper function and update input event
old_input_logic = """      // 1) 1분 30초 발화 글자수 실시간 업데이트
      if (field === 'speech_1m30s') {
        const lenTag = document.getElementById(`len-tag-${id}`);
        if (lenTag) {
          lenTag.textContent = `${text.length}자`;
          if (text.length >= 380 && text.length <= 450) {
            lenTag.style.color = 'var(--accent-emerald)';
          } else {
            lenTag.style.color = 'var(--accent-amber)';
          }
        }
      }"""

new_input_logic = """      // 1) 발화 글자수 실시간 업데이트 (인성 1분 / 직무 3분 맞춤 판정)
      if (field === 'speech_1m30s') {
        const lenTag = document.getElementById(`len-tag-${id}`);
        const topic = currentTopics.find(t => t.id === id);
        const cat = topic ? topic.category : 'personality';
        if (lenTag) {
          lenTag.textContent = `${text.length}자`;
          lenTag.style.color = getLenColor(text.length, cat);
        }
      }"""

if old_input_logic in content:
    content = content.replace(old_input_logic, new_input_logic)
    print("Replaced speech length real-time counting logic")
else:
    print("old_input_logic match failed, checking...")

# Add getLenColor helper
helper_fn = """    function getLenColor(textLen, category) {
      if (category === 'personality') {
        return (textLen >= 250 && textLen <= 330) ? 'var(--accent-emerald)' : 'var(--accent-amber)';
      } else {
        return (textLen >= 800 && textLen <= 1300) ? 'var(--accent-emerald)' : 'var(--accent-amber)';
      }
    }
"""

if "function getLenColor" not in content:
    content = content.replace("function renderDashboard()", helper_fn + "\n    function renderDashboard()")
    print("Added getLenColor helper function")

# 8. Update Timer JS logic to support dual 1-minute / 3-minute modes
old_timer_js = """    // ========================================================
    // 9. 1분 30초 실전 타이머
    // ========================================================
    const TOTAL_SECONDS = 90;
    let remainingSeconds = TOTAL_SECONDS;
    let timerInterval = null;
    const timerDisplay = document.getElementById('timerDisplay');
    const timerProgress = document.getElementById('timerProgress');
    const timerStartBtn = document.getElementById('timerStartBtn');
    const timerPauseBtn = document.getElementById('timerPauseBtn');
    const timerResetBtn = document.getElementById('timerResetBtn');

    function updateTimerUI() {
      const mins = Math.floor(remainingSeconds / 60);
      const secs = remainingSeconds % 60;
      timerDisplay.textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;

      const pct = (remainingSeconds / TOTAL_SECONDS) * 100;
      timerProgress.style.width = pct + '%';

      if (remainingSeconds <= 15 && remainingSeconds > 0) {
        timerDisplay.classList.add('warning');
        timerProgress.classList.add('warning');
      } else {
        timerDisplay.classList.remove('warning');
        timerProgress.classList.remove('warning');
      }
    }

    timerStartBtn.addEventListener('click', () => {
      if (timerInterval) return;
      timerInterval = setInterval(() => {
        if (remainingSeconds > 0) {
          remainingSeconds--;
          updateTimerUI();
        } else {
          clearInterval(timerInterval);
          timerInterval = null;
          showToast('⏰ 1분 30초 실전 발화 시간이 완료되었습니다!');
        }
      }, 1000);
    });

    timerPauseBtn.addEventListener('click', () => {
      if (timerInterval) {
        clearInterval(timerInterval);
        timerInterval = null;
      }
    });

    timerResetBtn.addEventListener('click', () => {
      if (timerInterval) {
        clearInterval(timerInterval);
        timerInterval = null;
      }
      remainingSeconds = TOTAL_SECONDS;
      updateTimerUI();
    });"""

new_timer_js = """    // ========================================================
    // 9. 실전 맞춤 타이머 (1분 인성 / 3분 직무 모드)
    // ========================================================
    let currentTimerDuration = 60; // 기본 1분 (인성)
    let remainingSeconds = currentTimerDuration;
    let timerInterval = null;
    const timerDisplay = document.getElementById('timerDisplay');
    const timerProgress = document.getElementById('timerProgress');
    const timerStartBtn = document.getElementById('timerStartBtn');
    const timerPauseBtn = document.getElementById('timerPauseBtn');
    const timerResetBtn = document.getElementById('timerResetBtn');

    function switchTimerMode(seconds) {
      if (timerInterval) {
        clearInterval(timerInterval);
        timerInterval = null;
      }
      currentTimerDuration = seconds;
      remainingSeconds = seconds;

      const mode1mBtn = document.getElementById('mode1mBtn');
      const mode3mBtn = document.getElementById('mode3mBtn');
      const titleText = document.getElementById('timerTitleText');

      if (seconds === 60) {
        if (mode1mBtn) mode1mBtn.classList.add('active');
        if (mode3mBtn) mode3mBtn.classList.remove('active');
        if (titleText) titleText.textContent = '1분 실전 타이머 (인성)';
      } else {
        if (mode1mBtn) mode1mBtn.classList.remove('active');
        if (mode3mBtn) mode3mBtn.classList.add('active');
        if (titleText) titleText.textContent = '3분 심층 타이머 (직무)';
      }
      updateTimerUI();
    }

    function updateTimerUI() {
      const mins = Math.floor(remainingSeconds / 60);
      const secs = remainingSeconds % 60;
      timerDisplay.textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;

      const pct = (remainingSeconds / currentTimerDuration) * 100;
      timerProgress.style.width = pct + '%';

      const warningThreshold = (currentTimerDuration === 60 ? 10 : 30);
      if (remainingSeconds <= warningThreshold && remainingSeconds > 0) {
        timerDisplay.classList.add('warning');
        timerProgress.classList.add('warning');
      } else {
        timerDisplay.classList.remove('warning');
        timerProgress.classList.remove('warning');
      }
    }

    timerStartBtn.addEventListener('click', () => {
      if (timerInterval) return;
      timerInterval = setInterval(() => {
        if (remainingSeconds > 0) {
          remainingSeconds--;
          updateTimerUI();
        } else {
          clearInterval(timerInterval);
          timerInterval = null;
          showToast(`⏰ ${currentTimerDuration === 60 ? '1분 인성' : '3분 직무'} 실전 발화 시간이 완료되었습니다!`);
        }
      }, 1000);
    });

    timerPauseBtn.addEventListener('click', () => {
      if (timerInterval) {
        clearInterval(timerInterval);
        timerInterval = null;
      }
    });

    timerResetBtn.addEventListener('click', () => {
      if (timerInterval) {
        clearInterval(timerInterval);
        timerInterval = null;
      }
      remainingSeconds = currentTimerDuration;
      updateTimerUI();
    });"""

if old_timer_js in content:
    content = content.replace(old_timer_js, new_timer_js)
    print("Replaced Timer JS logic")
else:
    print("old_timer_js match failed, checking...")

# Save updated files
with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

with open("result/261010_v1.0/index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Saved index.html and result/261010_v1.0/index.html successfully.")
