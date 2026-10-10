# -*- coding: utf-8 -*-
"""
SK하이닉스 AISK 심층 대비 인터랙티브 대시보드 빌더 스크립트
build_aisk_dashboard.py
"""

import os
import json
import shutil
import html

def escape(text):
    return html.escape(text)

def generate_dashboard():
    data_path = r"C:\Work\반도체4_AISK대비\context\data\aisk_topics.json"
    result_dir = r"C:\Work\반도체4_AISK대비\result\261010_v1.0"
    result_html_path = os.path.join(result_dir, "index.html")
    root_html_path = r"C:\Work\반도체4_AISK대비\index.html"

    os.makedirs(result_dir, exist_ok=True)

    with open(data_path, "r", encoding="utf-8") as f:
        topics = json.load(f)

    # 사이드바 아이템 생성
    nav_items_html = []
    cards_html = []

    for t in topics:
        t_id = t["id"]
        cat = t["category"]
        cat_label = t["category_label"]
        num = t["number"]
        title = t["title"]
        keywords = t.get("core_keyword", [])
        speech = t["speech_1m30s"]
        lecture = t["deep_lecture"]
        svg = t["svg_diagram"]

        speech_char_count = len(speech)
        num_str = f"인성-{num:02d}" if cat == "personality" else f"직무-{num:02d}"
        badge_class = "cat-badge-p" if cat == "personality" else "cat-badge-t"

        # Sidebar nav item
        keywords_str = " ".join(keywords)
        nav_items_html.append(f"""
        <li class="nav-item" data-category="{cat}" data-search="{escape(title)} {escape(keywords_str)} {num_str}">
          <a href="#{t_id}" class="nav-link" id="link-{t_id}">
            <span class="nav-num {badge_class}">{num_str}</span>
            <span class="nav-text">{escape(title)}</span>
          </a>
        </li>
        """)

        # Core keywords pills
        kw_pills = "".join([f'<span class="kw-pill">#{escape(kw)}</span>' for kw in keywords])

        # Core points in lecture
        core_pts_html = "".join([f'<li>{escape(pt)}</li>' for pt in lecture.get("core_points", [])])

        # Action principle formatting (개행 처리)
        action_principle_text = lecture.get("action_principle", "").replace("\n", "<br>")

        # Card HTML
        cards_html.append(f"""
        <section class="topic-section" id="{t_id}" data-category="{cat}">
          <div class="topic-header">
            <div class="topic-title-wrap">
              <span class="topic-badge {badge_class}">{num_str}</span>
              <span class="category-chip">{escape(cat_label)}</span>
              <div class="kw-container">{kw_pills}</div>
            </div>
            <div class="speech-len-tag">실전 호흡: <strong>{speech_char_count}자</strong> (약 1분 30초)</div>
          </div>

          <h2 class="topic-title">{escape(title)}</h2>

          <!-- 1분 30초 실전 핵심 전달 카드 -->
          <div class="speech-card">
            <div class="speech-card-header">
              <div class="speech-card-title">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="22"></line></svg>
                <span>1분 30초 실전 핵심 전달 (구어체 최적화 호흡)</span>
              </div>
              <button class="btn-copy" onclick="copySpeech('{t_id}')" title="답변 복사">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                복사
              </button>
            </div>
            <div class="speech-body" id="speech-text-{t_id}">
              {escape(speech)}
            </div>
            <div class="speech-guide-footer">
              <span class="guide-tip">💡 팁: 첫 10초에 두괄식 핵심 메시지를 각인시키고, 60초간 구체적 데이터·원리를 전개한 후, 마지막 20초에 양산 수율 기여로 완결합니다.</span>
            </div>
          </div>

          <!-- 아키텍처 다이어그램 -->
          <div class="diagram-section">
            <div class="diagram-title">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="9" y1="21" x2="9" y2="9"></line></svg>
              구조화 아키텍처 다이어그램 (Architectural Schematic)
            </div>
            <div class="svg-container">
              {svg}
            </div>
          </div>

          <!-- 세부 마스터 강의 노트 -->
          <div class="lecture-box">
            <div class="lecture-header">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
              세부 마스터 강의 노트 (Technical & Behavioral Deep-Dive)
            </div>

            <div class="lecture-content">
              <div class="lecture-item">
                <h4 class="lecture-sub-title">1. 배경 및 출제 의도 (Background & Core Context)</h4>
                <p class="lecture-desc">{escape(lecture.get("background", ""))}</p>
              </div>

              <div class="lecture-item">
                <h4 class="lecture-sub-title">2. 핵심 행동·물리 원리 (Action & Physical Principles)</h4>
                <div class="principle-box">
                  {action_principle_text}
                </div>
              </div>

              <div class="lecture-item">
                <h4 class="lecture-sub-title">3. 마스터 공략 핵심 포인트 (Key Takeaways)</h4>
                <ul class="core-pts-list">
                  {core_pts_html}
                </ul>
              </div>
            </div>
          </div>
        </section>
        """)

    full_html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="0">
  <title>SK하이닉스 AISK 심층 대비 마스터 백과사전 (인성 20 + 직무 20)</title>
  
  <!-- Pretendard & JetBrains Mono Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
  
  <!-- KaTeX for Semiconductor Physics Formulas -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
          onload="renderMathInElement(document.body, {{delimiters: [{{left: '$$', right: '$$', display: true}}, {{left: '$', right: '$', display: false}}]}});"></script>

  <style>
    :root {{
      --bg-body: #090d16;
      --bg-card: #111827;
      --bg-sidebar: #0f172a;
      --bg-elevated: #1e293b;
      --border: #1e293b;
      --border-focus: #38bdf8;
      
      --text-main: #f8fafc;
      --text-sub: #cbd5e1;
      --text-muted: #64748b;
      
      --accent-blue: #38bdf8;
      --accent-indigo: #6366f1;
      --accent-amber: #f59e0b;
      --accent-emerald: #10b981;
      --accent-rose: #f43f5e;
      
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
      
      --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.3);
      --shadow-md: 0 8px 24px rgba(0, 0, 0, 0.45);
      --shadow-lg: 0 16px 36px rgba(0, 0, 0, 0.6);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif;
      -webkit-font-smoothing: antialiased;
    }}

    body {{
      background-color: var(--bg-body);
      color: var(--text-main);
      display: flex;
      min-height: 100vh;
      overflow-x: hidden;
    }}

    /* 사이드바 접힘 제어 */
    body.sidebar-collapsed aside {{
      transform: translateX(-100%);
    }}
    body.sidebar-collapsed main {{
      margin-left: 0;
      max-width: 100%;
      padding: 40px 80px 120px;
    }}
    body.sidebar-collapsed .drawer-float-open-btn {{
      display: inline-flex;
    }}

    .drawer-float-open-btn {{
      position: fixed;
      top: 20px;
      left: 20px;
      z-index: 99;
      background: #0f172a;
      border: 1.5px solid var(--accent-blue);
      color: var(--accent-blue);
      border-radius: 10px;
      padding: 8px 16px;
      font-size: 0.88rem;
      font-weight: 700;
      cursor: pointer;
      display: none;
      align-items: center;
      gap: 8px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.7);
      transition: all 0.2s ease;
    }}
    .drawer-float-open-btn:hover {{
      background: var(--accent-blue);
      color: #0f172a;
      transform: translateY(-2px);
    }}

    /* 좌측 사이드바 */
    aside {{
      width: 380px;
      background-color: var(--bg-sidebar);
      border-right: 1px solid var(--border);
      position: fixed;
      top: 0;
      bottom: 0;
      left: 0;
      display: flex;
      flex-direction: column;
      z-index: 50;
      box-shadow: var(--shadow-lg);
      transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    .sidebar-header {{
      padding: 22px 20px 16px;
      border-bottom: 1px solid var(--border);
      background: linear-gradient(180deg, rgba(30, 41, 59, 0.6) 0%, rgba(15, 23, 42, 0) 100%);
    }}

    .sidebar-header-top {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 8px;
    }}

    .sidebar-title {{
      font-size: 1.15rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      background: linear-gradient(90deg, #38bdf8, #818cf8);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .btn-collapse {{
      background: rgba(30, 41, 59, 0.85);
      border: 1px solid rgba(56, 189, 248, 0.4);
      color: var(--accent-blue);
      border-radius: 6px;
      padding: 4px 10px;
      font-size: 0.75rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      transition: all 0.2s;
    }}
    .btn-collapse:hover {{
      background: var(--accent-blue);
      color: #0f172a;
    }}

    .sidebar-desc {{
      font-size: 0.78rem;
      color: var(--text-muted);
      line-height: 1.4;
    }}

    /* 카테고리 필터 칩 */
    .filter-tabs {{
      display: flex;
      gap: 6px;
      padding: 12px 18px;
      border-bottom: 1px solid var(--border);
      background: rgba(15, 23, 42, 0.4);
    }}

    .filter-chip {{
      flex: 1;
      padding: 6px 4px;
      font-size: 0.78rem;
      font-weight: 700;
      border-radius: 6px;
      border: 1px solid var(--border);
      background: #1e293b;
      color: var(--text-sub);
      cursor: pointer;
      text-align: center;
      transition: all 0.2s;
    }}
    .filter-chip:hover {{
      border-color: var(--accent-blue);
      color: var(--text-main);
    }}
    .filter-chip.active {{
      background: linear-gradient(135deg, #0284c7, #4f46e5);
      border-color: #38bdf8;
      color: #ffffff;
      box-shadow: 0 2px 10px rgba(56, 189, 248, 0.3);
    }}

    .search-box {{
      padding: 12px 18px;
      border-bottom: 1px solid var(--border);
    }}

    .search-input {{
      width: 100%;
      padding: 9px 13px;
      background-color: rgba(15, 23, 42, 0.8);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      color: var(--text-main);
      font-size: 0.84rem;
      outline: none;
      transition: all 0.2s;
    }}
    .search-input:focus {{
      border-color: var(--accent-blue);
      box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.2);
    }}

    .nav-list {{
      flex: 1;
      overflow-y: auto;
      padding: 10px 8px;
      list-style: none;
    }}
    .nav-list::-webkit-scrollbar {{
      width: 5px;
    }}
    .nav-list::-webkit-scrollbar-thumb {{
      background: var(--border);
      border-radius: 4px;
    }}

    .nav-item {{
      margin-bottom: 4px;
    }}

    .nav-link {{
      display: flex;
      align-items: flex-start;
      gap: 10px;
      padding: 9px 12px;
      color: var(--text-sub);
      text-decoration: none;
      font-size: 0.84rem;
      line-height: 1.4;
      font-weight: 500;
      border-radius: var(--radius-sm);
      transition: all 0.15s ease;
    }}
    .nav-link:hover {{
      background-color: rgba(255, 255, 255, 0.05);
      color: var(--accent-blue);
      transform: translateX(3px);
    }}
    .nav-link.active {{
      background: linear-gradient(90deg, rgba(56, 189, 248, 0.18), rgba(99, 102, 241, 0.08));
      color: var(--accent-blue);
      font-weight: 700;
      border-left: 3px solid var(--accent-blue);
    }}

    .nav-num {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.7rem;
      font-weight: 700;
      padding: 2px 6px;
      border-radius: 4px;
      white-space: nowrap;
      margin-top: 1px;
    }}
    .cat-badge-p {{
      color: #f59e0b;
      background: rgba(245, 158, 11, 0.12);
      border: 1px solid rgba(245, 158, 11, 0.3);
    }}
    .cat-badge-t {{
      color: #38bdf8;
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.3);
    }}

    .nav-text {{
      flex: 1;
      word-break: keep-all;
    }}

    /* 메인 컨텐츠 영역 */
    main {{
      margin-left: 380px;
      flex: 1;
      padding: 40px 60px 120px;
      max-width: 1300px;
      transition: margin-left 0.3s cubic-bezier(0.4, 0, 0.2, 1), padding 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    /* 헤더 및 스톱워치 위젯 */
    .main-header {{
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 30px;
      margin-bottom: 40px;
      padding-bottom: 24px;
      border-bottom: 1px solid var(--border);
      flex-wrap: wrap;
    }}

    .header-left {{
      flex: 1;
      min-width: 320px;
    }}

    .badge-top {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 12px;
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.35);
      border-radius: 20px;
      color: var(--accent-blue);
      font-size: 0.8rem;
      font-weight: 700;
      margin-bottom: 12px;
    }}

    .main-title {{
      font-size: 2.2rem;
      font-weight: 800;
      letter-spacing: -0.03em;
      line-height: 1.25;
      margin-bottom: 10px;
      background: linear-gradient(135deg, #ffffff 40%, #94a3b8 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .main-desc {{
      font-size: 0.98rem;
      color: var(--text-sub);
      line-height: 1.6;
    }}

    /* 1분 30초 실전 스톱워치 위젯 */
    .timer-widget {{
      background: linear-gradient(145deg, #1e293b, #0f172a);
      border: 1.5px solid rgba(56, 189, 248, 0.4);
      border-radius: var(--radius-md);
      padding: 16px 22px;
      display: flex;
      flex-direction: column;
      align-items: center;
      min-width: 260px;
      box-shadow: 0 8px 25px rgba(0, 0, 0, 0.5);
    }}

    .timer-header {{
      display: flex;
      align-items: center;
      gap: 7px;
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--accent-blue);
      margin-bottom: 8px;
    }}

    .timer-display {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 2.4rem;
      font-weight: 800;
      letter-spacing: 2px;
      color: #ffffff;
      margin-bottom: 10px;
    }}
    .timer-display.warning {{
      color: #ef4444;
      animation: pulse 1s infinite;
    }}

    @keyframes pulse {{
      0%, 100% {{ opacity: 1; transform: scale(1); }}
      50% {{ opacity: 0.6; transform: scale(1.05); }}
    }}

    .timer-controls {{
      display: flex;
      gap: 8px;
      margin-bottom: 10px;
    }}

    .timer-btn {{
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 0.8rem;
      font-weight: 700;
      cursor: pointer;
      border: 1px solid var(--border);
      background: #334155;
      color: #ffffff;
      transition: all 0.15s;
    }}
    .timer-btn:hover {{
      background: #475569;
    }}
    .timer-btn.start {{
      background: #0284c7;
      border-color: #38bdf8;
    }}
    .timer-btn.start:hover {{
      background: #0369a1;
    }}

    .timer-progress-bar {{
      width: 100%;
      height: 6px;
      background: #334155;
      border-radius: 3px;
      overflow: hidden;
    }}
    .timer-progress {{
      height: 100%;
      width: 100%;
      background: linear-gradient(90deg, #10b981, #38bdf8);
      transition: width 1s linear;
    }}
    .timer-progress.warning {{
      background: #ef4444;
    }}

    /* 질문 카드 스타일 */
    .topic-section {{
      background-color: var(--bg-card);
      border: 2px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 34px 38px;
      margin-bottom: 50px;
      box-shadow: var(--shadow-md);
      scroll-margin-top: 30px;
      transition: all 0.25s ease;
    }}
    .topic-section:hover {{
      border-color: rgba(56, 189, 248, 0.6);
      box-shadow: var(--shadow-lg);
    }}

    .topic-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 18px;
      padding-bottom: 14px;
      border-bottom: 1px solid var(--border);
      flex-wrap: wrap;
      gap: 12px;
    }}

    .topic-title-wrap {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }}

    .topic-badge {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.85rem;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 6px;
    }}

    .category-chip {{
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--text-sub);
      background: rgba(255, 255, 255, 0.06);
      padding: 3px 9px;
      border-radius: 6px;
    }}

    .kw-container {{
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
    }}
    .kw-pill {{
      font-size: 0.75rem;
      color: #94a3b8;
      background: rgba(148, 163, 184, 0.1);
      padding: 2px 7px;
      border-radius: 4px;
    }}

    .speech-len-tag {{
      font-size: 0.82rem;
      color: var(--text-muted);
    }}
    .speech-len-tag strong {{
      color: var(--accent-emerald);
    }}

    .topic-title {{
      font-size: 1.55rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      line-height: 1.4;
      margin-bottom: 24px;
      color: #f8fafc;
    }}

    /* 1분 30초 실전 핵심 전달 상자 */
    .speech-card {{
      background: linear-gradient(135deg, rgba(14, 165, 233, 0.12) 0%, rgba(99, 102, 241, 0.12) 100%);
      border: 1.5px solid #0284c7;
      border-radius: var(--radius-md);
      padding: 22px 26px;
      margin-bottom: 28px;
      box-shadow: 0 4px 20px rgba(2, 132, 199, 0.15);
    }}

    .speech-card-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 14px;
    }}

    .speech-card-title {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background-color: #0284c7;
      color: #ffffff;
      font-size: 0.82rem;
      font-weight: 700;
      padding: 5px 12px;
      border-radius: 6px;
      letter-spacing: 0.02em;
    }}

    .btn-copy {{
      background: rgba(15, 23, 42, 0.6);
      border: 1px solid rgba(56, 189, 248, 0.4);
      color: var(--accent-blue);
      border-radius: 6px;
      padding: 4px 10px;
      font-size: 0.75rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.2s;
    }}
    .btn-copy:hover {{
      background: var(--accent-blue);
      color: #0f172a;
    }}

    .speech-body {{
      font-size: 1.05rem;
      line-height: 1.85;
      color: #f1f5f9;
      word-break: keep-all;
      letter-spacing: -0.01em;
      font-weight: 500;
    }}

    .speech-guide-footer {{
      margin-top: 14px;
      padding-top: 12px;
      border-top: 1px dashed rgba(56, 189, 248, 0.3);
    }}
    .guide-tip {{
      font-size: 0.8rem;
      color: #94a3b8;
    }}

    /* 아키텍처 다이어그램 영역 */
    .diagram-section {{
      background: #090d16;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 20px;
      margin-bottom: 28px;
    }}

    .diagram-title {{
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--accent-blue);
      display: flex;
      align-items: center;
      gap: 7px;
      margin-bottom: 14px;
    }}

    .svg-container svg {{
      width: 100%;
      height: auto;
      display: block;
      border-radius: 8px;
    }}

    /* 세부 마스터 강의 노트 */
    .lecture-box {{
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 24px 28px;
    }}

    .lecture-header {{
      font-size: 0.95rem;
      font-weight: 800;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 20px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--border);
    }}

    .lecture-item {{
      margin-bottom: 22px;
    }}
    .lecture-item:last-child {{
      margin-bottom: 0;
    }}

    .lecture-sub-title {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--accent-blue);
      margin-bottom: 8px;
    }}

    .lecture-desc {{
      font-size: 0.92rem;
      color: var(--text-sub);
      line-height: 1.65;
    }}

    .principle-box {{
      background: rgba(30, 41, 59, 0.5);
      border-left: 3px solid var(--accent-indigo);
      border-radius: 0 6px 6px 0;
      padding: 12px 16px;
      font-size: 0.9rem;
      line-height: 1.7;
      color: #e2e8f0;
    }}

    .core-pts-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 8px;
      margin-top: 6px;
    }}
    .core-pts-list li {{
      position: relative;
      padding-left: 20px;
      font-size: 0.9rem;
      color: var(--text-sub);
      line-height: 1.6;
    }}
    .core-pts-list li::before {{
      content: "✔";
      position: absolute;
      left: 0;
      top: 0;
      color: var(--accent-emerald);
      font-weight: 800;
    }}

    /* 복사 토스트 */
    .toast {{
      position: fixed;
      bottom: 30px;
      right: 30px;
      background: #10b981;
      color: #ffffff;
      padding: 12px 20px;
      border-radius: 8px;
      font-size: 0.9rem;
      font-weight: 700;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
      transform: translateY(100px);
      opacity: 0;
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      z-index: 1000;
    }}
    .toast.show {{
      transform: translateY(0);
      opacity: 1;
    }}

    @media (max-width: 900px) {{
      aside {{
        transform: translateX(-100%);
      }}
      body.sidebar-open aside {{
        transform: translateX(0);
      }}
      main {{
        margin-left: 0;
        padding: 30px 20px 80px;
      }}
      .drawer-float-open-btn {{
        display: inline-flex;
      }}
      .main-header {{
        flex-direction: column;
      }}
      .timer-widget {{
        width: 100%;
      }}
    }}
  </style>
</head>
<body>

  <!-- 모바일 및 사이드바 닫힘 시 플로팅 버튼 -->
  <button class="drawer-float-open-btn" id="sidebarFloatOpenBtn">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
    목차 열기
  </button>

  <!-- 좌측 사이드바 -->
  <aside id="sidebar">
    <div class="sidebar-header">
      <div class="sidebar-header-top">
        <h1 class="sidebar-title">AISK MASTER</h1>
        <button class="btn-collapse" id="sidebarCollapseBtn">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="11 17 6 12 11 7"></polyline><polyline points="18 17 13 12 18 7"></polyline></svg>
          접기
        </button>
      </div>
      <p class="sidebar-desc">SK하이닉스 심층 대비 마스터 40문항</p>
    </div>

    <!-- 카테고리 필터 탭 -->
    <div class="filter-tabs">
      <button class="filter-chip active" data-filter="all">전체 (40)</button>
      <button class="filter-chip" data-filter="personality">인성·협업 (20)</button>
      <button class="filter-chip" data-filter="tech">직무·소자 (20)</button>
    </div>

    <!-- 실시간 검색창 -->
    <div class="search-box">
      <input type="text" id="searchInput" class="search-input" placeholder="키워드, 문항 번호, 제목 검색..." autocomplete="off">
    </div>

    <!-- 목차 리스트 -->
    <ul class="nav-list" id="navList">
      {"".join(nav_items_html)}
    </ul>
  </aside>

  <!-- 메인 본문 -->
  <main>
    <header class="main-header">
      <div class="header-left">
        <div class="badge-top">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
          SK hynix AISK 실전 대비 백과사전
        </div>
        <h1 class="main-title">SK하이닉스 AISK 심층 대비 마스터</h1>
        <p class="main-desc">
          인성·협업·조직 가치 20문항과 소자·공정 실전 핵심 20문항으로 구성된 총 40개 마스터 강의 컬렉션입니다.<br>
          각 문항마다 <strong>1분 30초 실전 핵심 전달</strong>(380~450자), <strong>구조화 아키텍처 다이어그램</strong>, <strong>세부 마스터 강의 노트</strong>를 탑재하여 완벽한 실전 전달력을 구현합니다.
        </p>
      </div>

      <!-- 1분 30초 실전 스톱워치 위젯 -->
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
      </div>
    </header>

    <!-- 문항 카드 컨테이너 -->
    <div id="topicContainer">
      {"".join(cards_html)}
    </div>
  </main>

  <div class="toast" id="toast">1분 30초 실전 답변이 클립보드에 복사되었습니다!</div>

  <script>
    // 1. 사이드바 접기 / 펼치기
    const sidebarCollapseBtn = document.getElementById('sidebarCollapseBtn');
    const sidebarFloatOpenBtn = document.getElementById('sidebarFloatOpenBtn');

    if (sidebarCollapseBtn) {{
      sidebarCollapseBtn.addEventListener('click', () => {{
        document.body.classList.add('sidebar-collapsed');
        localStorage.setItem('aisk_sidebar_collapsed', 'true');
      }});
    }}

    if (sidebarFloatOpenBtn) {{
      sidebarFloatOpenBtn.addEventListener('click', () => {{
        document.body.classList.remove('sidebar-collapsed');
        localStorage.setItem('aisk_sidebar_collapsed', 'false');
      }});
    }}

    if (localStorage.getItem('aisk_sidebar_collapsed') === 'true') {{
      document.body.classList.add('sidebar-collapsed');
    }}

    // 2. 카테고리 필터링
    const filterChips = document.querySelectorAll('.filter-chip');
    const navItems = document.querySelectorAll('.nav-item');
    const topicSections = document.querySelectorAll('.topic-section');

    filterChips.forEach(chip => {{
      chip.addEventListener('click', () => {{
        filterChips.forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        const filter = chip.getAttribute('data-filter');
        applyFilterAndSearch();
      }});
    }});

    // 3. 실시간 검색 필터링
    const searchInput = document.getElementById('searchInput');
    searchInput.addEventListener('input', () => {{
      applyFilterAndSearch();
    }});

    function applyFilterAndSearch() {{
      const activeFilterChip = document.querySelector('.filter-chip.active');
      const filter = activeFilterChip ? activeFilterChip.getAttribute('data-filter') : 'all';
      const query = searchInput.value.toLowerCase().trim();

      navItems.forEach(item => {{
        const itemCat = item.getAttribute('data-category');
        const searchData = item.getAttribute('data-search').toLowerCase();
        
        const catMatch = (filter === 'all' || itemCat === filter);
        const searchMatch = (query === '' || searchData.includes(query));

        if (catMatch && searchMatch) {{
          item.style.display = 'block';
        }} else {{
          item.style.display = 'none';
        }}
      }});

      topicSections.forEach(section => {{
        const secCat = section.getAttribute('data-category');
        const secText = section.innerText.toLowerCase();

        const catMatch = (filter === 'all' || secCat === filter);
        const searchMatch = (query === '' || secText.includes(query));

        if (catMatch && searchMatch) {{
          section.style.display = 'block';
        }} else {{
          section.style.display = 'none';
        }}
      }});
    }}

    // 4. 1분 30초 실전 타이머
    const TOTAL_SECONDS = 90;
    let remainingSeconds = TOTAL_SECONDS;
    let timerInterval = null;
    const timerDisplay = document.getElementById('timerDisplay');
    const timerProgress = document.getElementById('timerProgress');
    const timerStartBtn = document.getElementById('timerStartBtn');
    const timerPauseBtn = document.getElementById('timerPauseBtn');
    const timerResetBtn = document.getElementById('timerResetBtn');

    function updateTimerUI() {{
      const mins = Math.floor(remainingSeconds / 60);
      const secs = remainingSeconds % 60;
      timerDisplay.textContent = `${{String(mins).padStart(2, '0')}}:${{String(secs).padStart(2, '0')}}`;

      const pct = (remainingSeconds / TOTAL_SECONDS) * 100;
      timerProgress.style.width = pct + '%';

      if (remainingSeconds <= 15 && remainingSeconds > 0) {{
        timerDisplay.classList.add('warning');
        timerProgress.classList.add('warning');
      }} else {{
        timerDisplay.classList.remove('warning');
        timerProgress.classList.remove('warning');
      }}
    }}

    timerStartBtn.addEventListener('click', () => {{
      if (timerInterval) return;
      timerInterval = setInterval(() => {{
        if (remainingSeconds > 0) {{
          remainingSeconds--;
          updateTimerUI();
        }} else {{
          clearInterval(timerInterval);
          timerInterval = null;
          showToast('⏰ 1분 30초 실전 발화 시간이 완료되었습니다!');
        }}
      }}, 1000);
    }});

    timerPauseBtn.addEventListener('click', () => {{
      if (timerInterval) {{
        clearInterval(timerInterval);
        timerInterval = null;
      }}
    }});

    timerResetBtn.addEventListener('click', () => {{
      if (timerInterval) {{
        clearInterval(timerInterval);
        timerInterval = null;
      }}
      remainingSeconds = TOTAL_SECONDS;
      updateTimerUI();
    }});

    // 5. 복사 기능 및 토스트 알림
    function copySpeech(id) {{
      const el = document.getElementById(`speech-text-${{id}}`);
      if (!el) return;
      const text = el.innerText.trim();
      navigator.clipboard.writeText(text).then(() => {{
        showToast('📋 1분 30초 실전 답변이 클립보드에 복사되었습니다!');
      }}).catch(err => {{
        console.error('복사 실패:', err);
      }});
    }}

    function showToast(msg) {{
      const toast = document.getElementById('toast');
      toast.textContent = msg;
      toast.classList.add('show');
      setTimeout(() => {{
        toast.classList.remove('show');
      }}, 2600);
    }}

    // 6. 스크롤 활성 링크 감지 (IntersectionObserver)
    const observer = new IntersectionObserver((entries) => {{
      entries.forEach(entry => {{
        if (entry.isIntersecting) {{
          const id = entry.target.id;
          document.querySelectorAll('.nav-link').forEach(link => {{
            link.classList.remove('active');
          }});
          const activeLink = document.getElementById(`link-${{id}}`);
          if (activeLink) {{
            activeLink.classList.add('active');
          }}
        }}
      }});
    }}, {{
      rootMargin: '-20% 0px -70% 0px'
    }});

    topicSections.forEach(sec => {{
      observer.observe(sec);
    }});
  </script>
</body>
</html>
"""

    with open(result_html_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"[성공] 대시보드 생성 완료: {result_html_path}")

    shutil.copyfile(result_html_path, root_html_path)
    print(f"[성공] 루트 배포 완료: {root_html_path}")

if __name__ == "__main__":
    generate_dashboard()
