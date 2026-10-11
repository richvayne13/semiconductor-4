# -*- coding: utf-8 -*-
"""
단일 클릭 직접 인라인 수정(Direct Click-to-Edit) 적용 스크립트
apply_click_to_edit.py
"""

import os
import re

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. CSS 추가 및 수정 버튼 스타일 대체
    css_to_add = """
    /* ========================================================
       핵심: 한 번만 클릭해도 바로 수정되는 .editable-field 스타일
       ======================================================== */
    .editable-field {
      cursor: text !important;
      position: relative;
      border-radius: 6px;
      transition: background-color 0.15s, outline 0.15s, box-shadow 0.15s;
      outline: 1.5px solid transparent;
    }

    .editable-field:hover {
      outline: 1.5px dashed rgba(56, 189, 248, 0.5) !important;
      background-color: rgba(56, 189, 248, 0.04) !important;
    }

    .editable-field:focus {
      outline: 2px solid var(--accent-blue) !important;
      background-color: rgba(15, 23, 42, 0.95) !important;
      box-shadow: 0 0 0 4px rgba(56, 189, 248, 0.25) !important;
      color: #ffffff !important;
    }

    /* 제목 수정 */
    .topic-title.editable-field {
      font-size: 1.55rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      line-height: 1.4;
      margin-bottom: 24px;
      color: #f8fafc;
      padding: 4px 8px;
      margin-left: -8px;
    }

    /* 키워드 수정 박스 */
    .kw-wrap.editable-field {
      display: inline-block;
      font-size: 0.78rem;
      color: #94a3b8;
      background: rgba(148, 163, 184, 0.08);
      border-radius: 6px;
      padding: 3px 8px;
    }

    /* 1분 30초 실전 핵심 전달 상자 */
    .speech-body.editable-field {
      font-size: 1.05rem;
      line-height: 1.85;
      color: #f1f5f9;
      word-break: keep-all;
      letter-spacing: -0.01em;
      font-weight: 500;
      padding: 8px 12px;
      margin-left: -12px;
      white-space: pre-wrap;
      min-height: 80px;
    }

    .speech-click-hint {
      font-size: 0.78rem;
      color: var(--accent-blue);
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }

    .save-status-badge {
      font-size: 0.76rem;
      color: #64748b;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      font-weight: 600;
      padding: 3px 8px;
      border-radius: 4px;
      background: rgba(30, 41, 59, 0.5);
      transition: all 0.2s;
    }

    /* 직접 클릭 수정 안내 배너 */
    .quick-edit-banner {
      background: linear-gradient(135deg, rgba(56, 189, 248, 0.1) 0%, rgba(99, 102, 241, 0.08) 100%);
      border: 1px solid rgba(56, 189, 248, 0.35);
      border-radius: var(--radius-sm);
      padding: 10px 14px;
      font-size: 0.86rem;
      color: #e2e8f0;
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 16px;
    }
    .quick-edit-banner strong {
      color: var(--accent-blue);
    }
"""

    # .btn-card-action.edit-btn:hover 앞부분에 스타일 삽입
    content = content.replace(".btn-card-action.edit-btn:hover {", css_to_add + "\n    .btn-card-action.edit-btn:hover {")

    # 2. main-header에 quick-edit-banner 삽입
    banner_html = """
        <!-- 직접 클릭 수정 안내 배너 -->
        <div class="quick-edit-banner">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#38bdf8" stroke-width="2"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg>
          <span><strong>원클릭 직접 편집 지원:</strong> 별도의 수정 버튼 없이 제목이나 답변 상자를 <strong>한 번만 클릭</strong>하면 즉시 타이핑하여 수정할 수 있으며, <strong>입력 즉시 자동 저장</strong>됩니다.</span>
        </div>
"""
    # main-desc 뒤에 삽입
    content = re.sub(
        r'(<p class="main-desc">.*?</p>)',
        r'\1' + banner_html,
        content,
        flags=re.DOTALL
    )

    # 3. renderCards 템플릿 수정
    # 수정 버튼 제거, save-status-badge 추가
    old_card_actions = """                <div class="card-actions">
                  <div class="speech-len-tag">실전 호흡: <strong>${speechCharCount}자</strong></div>
                  <button class="btn-card-action edit-btn" onclick="startEdit('${t.id}')" title="제목 및 본문 수정">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg>
                    수정
                  </button>
                  <button class="btn-card-action delete-btn" onclick="deleteTopic('${t.id}')" title="이 문항 삭제">"""

    new_card_actions = """                <div class="card-actions">
                  <div class="speech-len-tag">실전 호흡: <strong id="len-tag-${t.id}">${speechCharCount}자</strong></div>
                  <span class="save-status-badge" id="save-status-${t.id}">클릭하여 바로 수정</span>
                  <button class="btn-card-action delete-btn" onclick="deleteTopic('${t.id}')" title="이 문항 삭제">"""

    content = content.replace(old_card_actions, new_card_actions)

    # 제목 및 키워드 및 본문 editable-field로 교체
    old_title_and_speech = """              <h2 class="topic-title">${title}</h2>

              <!-- 1분 30초 실전 핵심 전달 카드 -->
              <div class="speech-card">
                <div class="speech-card-header">
                  <div class="speech-card-title">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="22"></line></svg>
                    <span>1분 30초 실전 핵심 전달 (구어체 최적화 호흡)</span>
                  </div>
                  <button class="btn-card-action" onclick="copySpeech('${t.id}')" title="답변 복사">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                    복사
                  </button>
                </div>
                <div class="speech-body" id="speech-text-${t.id}">
                  ${escapeHtml(speech)}
                </div>"""

    new_title_and_speech = """              <!-- 제목 (클릭 시 즉시 수정) -->
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
                <div class="speech-body editable-field" contenteditable="true" data-field="speech_1m30s" data-id="${t.id}" id="speech-text-${t.id}" title="클릭하여 바로 수정 (자동 저장)">${escapeHtml(speech)}</div>"""

    content = content.replace(old_title_and_speech, new_title_and_speech)

    # kw-container 부분 수정: editable-field 추가
    content = content.replace(
        '<div class="kw-container">${kwPills}</div>',
        '<div class="kw-container editable-field" contenteditable="true" data-field="keywords" data-id="${t.id}" title="클릭하여 키워드 바로 수정">${kwPills}</div>'
    )

    # 4. JS 이벤트 핸들러 교체: startEdit / cancelEdit / saveEdit 제거 및 direct click-to-edit 이벤트 리스너 탑재
    old_edit_js = """    // ========================================================
    // 3. 인라인 편집 기능 (In-place Edit)
    // ========================================================
    function startEdit(id) {
      const topic = currentTopics.find(t => t.id === id);
      if (!topic) return;

      const viewEl = document.getElementById(`view-${id}`);
      const editWrap = document.getElementById(`edit-form-wrap-${id}`);

      viewEl.style.display = 'none';
      editWrap.style.display = 'block';

      const keywordsStr = (topic.core_keyword || []).join(', ');
      const pointsStr = ((topic.deep_lecture || {}).core_points || []).join('\\n');

      editWrap.innerHTML = `
        <div class="edit-form-wrap">
          <div class="edit-form-header">
            <div class="edit-form-title">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg>
              문항 편집 모드
            </div>
            <span style="font-size: 0.8rem; color: #94a3b8;">수정 후 저장 시 로컬에 즉시 영구 저장됩니다.</span>
          </div>

          <div class="form-group">
            <label class="form-label">분류 카테고리</label>
            <select class="form-select" id="edit-cat-${id}">
              <option value="personality" ${topic.category === 'personality' ? 'selected' : ''}>인성·협업·조직 가치</option>
              <option value="tech" ${topic.category === 'tech' ? 'selected' : ''}>반도체 소자·공정 실전 핵심</option>
            </select>
          </div>

          <div class="form-group">
            <label class="form-label">문항 제목</label>
            <input type="text" class="form-input" id="edit-title-${id}" value="${escapeHtml(topic.title)}" required>
          </div>

          <div class="form-group">
            <label class="form-label">핵심 키워드 (쉼표 구분)</label>
            <input type="text" class="form-input" id="edit-kw-${id}" value="${escapeHtml(keywordsStr)}">
          </div>

          <div class="form-group">
            <label class="form-label">
              1분 30초 실전 핵심 전달 (구어체)
              <span class="char-counter" id="edit-counter-${id}">${topic.speech_1m30s.length}자 (권장 380~450자)</span>
            </label>
            <textarea class="form-textarea" id="edit-speech-${id}" style="min-height: 140px;" oninput="updateSpeechCounter('edit-speech-${id}', 'edit-counter-${id}')">${escapeHtml(topic.speech_1m30s)}</textarea>
          </div>



          <div class="form-actions">
            <button class="btn-cancel" onclick="cancelEdit('${id}')">취소</button>
            <button class="btn-submit" onclick="saveEdit('${id}')">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
              저장 완료
            </button>
          </div>
        </div>
      `;
    }

    function cancelEdit(id) {
      const viewEl = document.getElementById(`view-${id}`);
      const editWrap = document.getElementById(`edit-form-wrap-${id}`);
      if (viewEl && editWrap) {
        editWrap.style.display = 'none';
        editWrap.innerHTML = '';
        viewEl.style.display = 'block';
      }
    }

    function saveEdit(id) {
      const topic = currentTopics.find(t => t.id === id);
      if (!topic) return;

      const newCat = document.getElementById(`edit-cat-${id}`).value;
      const newTitle = document.getElementById(`edit-title-${id}`).value.trim();
      const newKw = document.getElementById(`edit-kw-${id}`).value.split(',').map(s => s.trim()).filter(Boolean);
      const newSpeech = document.getElementById(`edit-speech-${id}`).value.trim();
      const bgEl = document.getElementById(`edit-bg-${id}`);
      const newBg = bgEl ? bgEl.value.trim() : (topic.deep_lecture?.background || '');
      const principleEl = document.getElementById(`edit-principle-${id}`);
      const newPrinciple = principleEl ? principleEl.value.trim() : (topic.deep_lecture?.action_principle || '');
      const pointsEl = document.getElementById(`edit-points-${id}`);
      const newPoints = pointsEl ? pointsEl.value.split('\\n').map(s => s.trim()).filter(Boolean) : (topic.deep_lecture?.core_points || []);

      if (!newTitle || !newSpeech) {
        alert('제목과 1분 30초 실전 답변은 필수입니다.');
        return;
      }

      topic.category = newCat;
      topic.category_label = (newCat === 'personality' ? '인성·협업·조직 가치' : '반도체 소자·공정 실전 핵심');
      topic.title = newTitle;
      topic.core_keyword = newKw;
      topic.speech_1m30s = newSpeech;
      topic.deep_lecture = topic.deep_lecture || {};
      topic.deep_lecture.background = newBg;
      topic.deep_lecture.action_principle = newPrinciple;
      topic.deep_lecture.core_points = newPoints;

      saveTopicsToStorage();
      renderDashboard();
      showToast('💾 문항 수정 내용이 성공적으로 저장되었습니다!');

      // 해당 카드로 부드럽게 스크롤
      const targetCard = document.getElementById(id);
      if (targetCard) {
        targetCard.scrollIntoView({ behavior: 'smooth' });
      }
    }"""

    new_edit_js = """    // ========================================================
    // 3. 인라인 직접 클릭 편집(Direct Click-to-Edit) 이벤트 핸들러
    // ========================================================
    let autoSaveTimer = null;
    const topicContainer = document.getElementById('topicContainer');

    // 입력 중 실시간 처리 (글자수 계산 & 디바운스 자동 저장)
    topicContainer.addEventListener('input', (e) => {
      const target = e.target.closest('.editable-field');
      if (!target) return;

      const id = target.getAttribute('data-id');
      const field = target.getAttribute('data-field');
      const text = target.innerText;

      // 1) 1분 30초 발화 글자수 실시간 업데이트
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
      }

      // 2) 제목 실시간 사이드바 반영
      if (field === 'title') {
        const navLink = document.querySelector(`#link-${id} .nav-text`);
        if (navLink) {
          navLink.textContent = text.trim() || '(제목 없음)';
        }
      }

      // 3) 상태 배지 업데이트
      const statusEl = document.getElementById(`save-status-${id}`);
      if (statusEl) {
        statusEl.innerHTML = '<span style="color: #38bdf8;">수정 중...</span>';
      }

      // 4) 400ms 디바운스 자동 저장
      clearTimeout(autoSaveTimer);
      autoSaveTimer = setTimeout(() => {
        saveFieldDirect(id, field, target);
      }, 400);
    });

    // 포커스를 벗어날 때 즉시 저장
    topicContainer.addEventListener('focusout', (e) => {
      const target = e.target.closest('.editable-field');
      if (!target) return;

      const id = target.getAttribute('data-id');
      const field = target.getAttribute('data-field');
      saveFieldDirect(id, field, target);
    });

    // 필드 데이터 실제 저장 로직
    function saveFieldDirect(id, field, element) {
      const topic = currentTopics.find(t => t.id === id);
      if (!topic) return;

      const rawText = element.innerText;

      if (field === 'title') {
        topic.title = rawText.trim();
      } else if (field === 'speech_1m30s') {
        topic.speech_1m30s = rawText;
      } else if (field === 'keywords') {
        topic.core_keyword = rawText.split(',').map(s => s.replace(/#/g, '').trim()).filter(Boolean);
      }

      saveTopicsToStorage();

      const statusEl = document.getElementById(`save-status-${id}`);
      if (statusEl) {
        statusEl.innerHTML = '<span style="color: #10b981;">✓ 자동 저장됨</span>';
        setTimeout(() => {
          if (statusEl) {
            statusEl.textContent = '클릭하여 바로 수정';
          }
        }, 1800);
      }
    }"""

    content = content.replace(old_edit_js, new_edit_js)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'[성공] 업데이트 완료: {filepath}')

if __name__ == '__main__':
    update_file(r'C:\Work\반도체4_AISK대비\index.html')
    update_file(r'C:\Work\반도체4_AISK대비\result\261010_v1.0\index.html')
