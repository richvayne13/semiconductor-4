# -*- coding: utf-8 -*-
import re

html_path = r"C:\Work\반도체4_AISK대비\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# ==============================================================================
# 1. CSS: 취소선 (Alt+S) 스타일 추가
# ==============================================================================
css_strikethrough = """
    /* ✂️ 취소선 (Alt+S) 세련된 스타일 */
    s, del, strike,
    .speech-body s, .speech-body del, .speech-body strike,
    .editable-field s, .editable-field del, .editable-field strike {
      text-decoration: line-through 2px rgba(239, 68, 68, 0.8) !important;
      color: var(--text-muted) !important;
      opacity: 0.7;
    }
"""

if "text-decoration: line-through" not in content:
    content = content.replace("</style>", css_strikethrough + "\n  </style>", 1)
    print("Added strikethrough CSS.")

# ==============================================================================
# 2. formatSpeechHtml & getCleanSpeechHtml 업데이트 (s, del, strike 태그 보존)
# ==============================================================================
old_format = """function formatSpeechHtml(text) {
      if (!text) return '';
      let safe = escapeHtml(text);
      safe = safe.replace(/&lt;b&gt;/gi, '<b>')
                 .replace(/&lt;\/b&gt;/gi, '</b>')
                 .replace(/&lt;strong&gt;/gi, '<strong>')
                 .replace(/&lt;\/strong&gt;/gi, '</strong>');
      return safe;
    }"""

new_format = """function formatSpeechHtml(text) {
      if (!text) return '';
      let safe = escapeHtml(text);
      safe = safe.replace(/&lt;b&gt;/gi, '<b>')
                 .replace(/&lt;\/b&gt;/gi, '</b>')
                 .replace(/&lt;strong&gt;/gi, '<strong>')
                 .replace(/&lt;\/strong&gt;/gi, '</strong>')
                 .replace(/&lt;s&gt;/gi, '<s>')
                 .replace(/&lt;\/s&gt;/gi, '</s>')
                 .replace(/&lt;del&gt;/gi, '<del>')
                 .replace(/&lt;\/del&gt;/gi, '</del>')
                 .replace(/&lt;strike&gt;/gi, '<strike>')
                 .replace(/&lt;\/strike&gt;/gi, '</strike>');
      return safe;
    }"""

old_clean = """      // <b>, </b>, <strong>, </strong>만 보존하고 기타 불필요한 태그 제거
      content = content.replace(/<(?!b|\/b|strong|\/strong)[^>]+>/gi, '');"""

new_clean = """      // <b>, <strong>, <s>, <del>, <strike> 보존하고 기타 불필요한 태그 제거
      content = content.replace(/<(?!b|\/b|strong|\/strong|s|\/s|del|\/del|strike|\/strike)[^>]+>/gi, '');"""

if old_format in content:
    content = content.replace(old_format, new_format, 1)
    print("Updated formatSpeechHtml for strikethrough.")

if old_clean in content:
    content = content.replace(old_clean, new_clean, 1)
    print("Updated getCleanSpeechHtml for strikethrough.")

# ==============================================================================
# 3. keydown 이벤트 리스너: Alt+S (및 Ctrl+Shift+S) 취소선 토글 단축키 구현
# ==============================================================================
old_keydown = """    // 🌟 Ctrl+B 단축키 누르면 선택 텍스트 볼드(노란색 음영) 처리 & 실시간 자동 저장
    document.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && (e.key === 'b' || e.key === 'B')) {
        const target = e.target.closest('.editable-field');
        if (target) {
          e.preventDefault();
          document.execCommand('bold', false, null);
          target.dispatchEvent(new Event('input', { bubbles: true }));
        }
      }
    });"""

new_keydown = """    // 🌟 Ctrl+B (노란색 형광펜 볼드) 및 Alt+S (취소선) 단축키
    document.addEventListener('keydown', (e) => {
      const target = e.target.closest('.editable-field');
      if (!target) return;

      // 1. Ctrl+B: 볼드 강조 (노란색 형광펜)
      if ((e.ctrlKey || e.metaKey) && (e.key === 'b' || e.key === 'B')) {
        e.preventDefault();
        document.execCommand('bold', false, null);
        target.dispatchEvent(new Event('input', { bubbles: true }));
      }

      // 2. Alt+S (또는 Ctrl+Shift+S): 취소선 (Strike-through) 처리
      if ((e.altKey && (e.key === 's' || e.key === 'S' || e.code === 'KeyS')) ||
          ((e.ctrlKey || e.metaKey) && e.shiftKey && (e.key === 's' || e.key === 'S' || e.code === 'KeyS'))) {
        e.preventDefault();
        document.execCommand('strikeThrough', false, null);
        target.dispatchEvent(new Event('input', { bubbles: true }));
        if (typeof showToast === 'function') {
          showToast('✂️ 취소선이 적용되었습니다 (Alt+S)');
        }
      }
    });"""

if old_keydown in content:
    content = content.replace(old_keydown, new_keydown, 1)
    print("Updated keydown listener for Alt+S strikethrough.")

# ==============================================================================
# 4. 카드 힌트 텍스트에 Alt+S 안내 추가
# ==============================================================================
content = content.replace(
    "<strong>Ctrl+B</strong>: 노란색 음영 볼드 강조",
    "<strong>Ctrl+B</strong>: 형광펜 볼드, <strong>Alt+S</strong>: 취소선"
)
content = content.replace(
    "<strong>Ctrl+B</strong>: 노란 형광펜",
    "<strong>Ctrl+B</strong>: 형광펜, <strong>Alt+S</strong>: 취소선"
)

# ==============================================================================
# 5. build-time 및 STORAGE_KEY 갱신
# ==============================================================================
new_storage_key = "aisk_master_topics_custom_v24_strikethrough_alts"
content = content.replace("aisk_master_topics_custom_v23_pc_auto_player", new_storage_key)

content = re.sub(
    r'<meta name="build-time" content="[^"]+">',
    '<meta name="build-time" content="2026-10-25T11:20:00+09:00">',
    content
)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Successfully integrated Alt+S strikethrough into {html_path}! Total size: {len(content)} bytes.")
