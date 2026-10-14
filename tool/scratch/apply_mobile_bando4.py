# -*- coding: utf-8 -*-
"""
apply_mobile_bando4.py
반도체 4 (AISK 마스터 대시보드) 모바일 완벽 반응형 UI 구축:
1. 모바일 상단 고정 헤더 바 (☰ 목차, 타이틀, ⬆ 맨위로)
2. 슬라이드 인 목차 서랍 (Drawer) & 배경 블러 오버레이 (Backdrop)
3. 목차 링크 터치 시 서랍 자동 닫힘 & 스무스 스크롤
4. 하단 모바일 플로팅 액션 버튼 (📑 목차, ⬆ 맨위로)
5. 카드, 실전 호흡 텍스트, 타이머, 모달 창의 모바일 최적화
"""

import re

MOBILE_CSS_BANDO4 = """
    /* ====================================================
       📱 모바일 & 태블릿 완벽 반응형 UI (반도체 4 AISK)
       ==================================================== */
    .mobile-top-bar { display: none; }
    .mobile-fab-container { display: none; }
    .drawer-backdrop { display: none; }

    @media (max-width: 900px) {
      body {
        flex-direction: column !important;
        overflow-x: hidden !important;
        width: 100% !important;
      }

      /* 모바일 상단 바 */
      .mobile-top-bar {
        display: flex !important;
        position: sticky;
        top: 0;
        left: 0;
        right: 0;
        height: 52px;
        background: rgba(17, 24, 39, 0.95);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        border-bottom: 1px solid var(--border);
        padding: 0 14px;
        align-items: center;
        justify-content: space-between;
        z-index: 1000;
        box-shadow: 0 4px 16px rgba(0,0,0,0.5);
      }

      .mobile-menu-btn {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: var(--bg-elevated);
        color: var(--accent-blue);
        border: 1px solid var(--border);
        border-radius: 8px;
        padding: 6px 12px;
        font-size: 0.88rem;
        font-weight: 700;
        cursor: pointer;
      }

      .mobile-header-title {
        font-size: 0.95rem;
        font-weight: 800;
        color: var(--text-main);
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        max-width: 55vw;
      }

      .mobile-top-btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 34px;
        height: 34px;
        background: var(--bg-elevated);
        color: var(--text-sub);
        border: 1px solid var(--border);
        border-radius: 8px;
        font-size: 0.9rem;
        cursor: pointer;
      }

      /* 사이드바 서랍 (Off-canvas Drawer) */
      aside {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        bottom: 0 !important;
        width: 84vw !important;
        max-width: 320px !important;
        height: 100vh !important;
        z-index: 1200 !important;
        transform: translateX(-100%) !important;
        transition: transform 0.28s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 4px 0 24px rgba(0,0,0,0.7) !important;
        background: var(--bg-sidebar) !important;
        overflow-y: auto !important;
      }

      body.drawer-open aside {
        transform: translateX(0) !important;
      }

      /* 배경 블러 오버레이 */
      .drawer-backdrop {
        display: block !important;
        position: fixed;
        inset: 0;
        background: rgba(0, 0, 0, 0.7);
        backdrop-filter: blur(3px);
        -webkit-backdrop-filter: blur(3px);
        z-index: 1100;
        opacity: 0;
        pointer-events: none;
        transition: opacity 0.25s ease;
      }

      body.drawer-open .drawer-backdrop {
        opacity: 1 !important;
        pointer-events: auto !important;
      }

      /* 메인 영역 */
      main {
        margin-left: 0 !important;
        padding: 16px 12px 100px !important;
        width: 100% !important;
        max-width: 100vw !important;
        box-sizing: border-box !important;
        overflow-x: hidden !important;
      }

      .drawer-float-open-btn {
        display: none !important;
      }

      /* 모바일 전용 플로팅 버튼 */
      .mobile-fab-container {
        display: flex !important;
        position: fixed;
        bottom: 24px;
        right: 16px;
        gap: 8px;
        z-index: 950;
      }

      .mobile-fab-btn {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: var(--accent-blue);
        color: #090d16;
        border: none;
        border-radius: 30px;
        padding: 10px 16px;
        font-size: 0.88rem;
        font-weight: 800;
        box-shadow: 0 4px 16px rgba(56, 189, 248, 0.4);
        cursor: pointer;
      }

      .mobile-fab-btn.top-btn {
        background: var(--bg-elevated);
        color: var(--accent-blue);
        border: 1px solid var(--border);
        padding: 10px 12px;
        border-radius: 50%;
        width: 42px;
        height: 42px;
        justify-content: center;
      }

      /* 헤더 및 안내 배너 */
      .main-header {
        margin-bottom: 20px !important;
      }

      .main-title {
        font-size: 1.35rem !important;
        line-height: 1.3 !important;
      }

      .main-desc {
        font-size: 0.85rem !important;
      }

      .quick-edit-banner {
        font-size: 0.82rem !important;
        padding: 10px 12px !important;
      }

      /* 카드 내부 반응형 */
      .topic-section {
        padding: 18px 14px !important;
        margin-bottom: 20px !important;
        border-radius: 14px !important;
      }

      .topic-title {
        font-size: 1.15rem !important;
        line-height: 1.45 !important;
      }

      .speech-card {
        padding: 16px 14px !important;
        border-radius: 12px !important;
      }

      .speech-body {
        font-size: 0.94rem !important;
        line-height: 1.8 !important;
      }

      .card-actions {
        flex-wrap: wrap !important;
        gap: 6px !important;
      }

      /* 모달 창 */
      .modal-box {
        width: 92vw !important;
        max-width: 480px !important;
        padding: 20px 16px !important;
      }
    }
"""

MOBILE_HTML_BANDO4 = """
  <!-- 📱 모바일 상단 헤더 바 -->
  <div class="mobile-top-bar">
    <button class="mobile-menu-btn" onclick="openDrawer()" aria-label="목차 열기">
      <span style="font-size:1.1rem; line-height:1;">☰</span> <span>목차 (23)</span>
    </button>
    <div class="mobile-header-title">AISK 면접 마스터</div>
    <button class="mobile-top-btn" onclick="scrollToTop()" aria-label="맨 위로">
      <span>⬆</span>
    </button>
  </div>

  <!-- 📱 모바일 서랍 배경 오버레이 -->
  <div id="drawerBackdrop" class="drawer-backdrop" onclick="closeDrawer()"></div>

  <!-- 📱 모바일 우측 하단 플로팅 액션 버튼 (FAB) -->
  <div class="mobile-fab-container">
    <button class="mobile-fab-btn" onclick="openDrawer()">
      <span>📑</span> <span>목차 열기</span>
    </button>
    <button class="mobile-fab-btn top-btn" onclick="scrollToTop()" title="맨 위로">
      <span>⬆</span>
    </button>
  </div>
"""

MOBILE_JS_BANDO4 = """
  // 📱 모바일 서랍(Drawer) 및 스크롤 제어 함수
  function openDrawer() {
    document.body.classList.add('drawer-open');
  }

  function closeDrawer() {
    document.body.classList.remove('drawer-open');
  }

  function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  // 모바일에서 목차 링크 클릭 시 자동으로 서랍 닫기
  document.addEventListener('DOMContentLoaded', function() {
    document.addEventListener('click', function(e) {
      const link = e.target.closest('#sidebarNav a, .nav-item a, .sidebar-nav a');
      if (link && window.innerWidth <= 900) {
        closeDrawer();
      }
    });

    const collapseBtn = document.getElementById('sidebarCollapseBtn');
    if (collapseBtn) {
      collapseBtn.addEventListener('click', function() {
        if (window.innerWidth <= 900) {
          closeDrawer();
        }
      });
    }

    const floatBtn = document.getElementById('sidebarFloatOpenBtn');
    if (floatBtn) {
      floatBtn.addEventListener('click', function() {
        openDrawer();
      });
    }
  });
"""

def update_bando4_html(file_path):
    print(f"Updating {file_path} for mobile UI...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Inject Mobile CSS before </style>
    if "/* ====================================================\n       📱 모바일 & 태블릿 완벽 반응형 UI (반도체 4 AISK)" not in html:
        style_end = html.find("</style>")
        if style_end != -1:
            html = html[:style_end] + MOBILE_CSS_BANDO4 + "\n" + html[style_end:]
            print("Injected MOBILE_CSS_BANDO4")

    # 2. Inject Mobile HTML Fragments after <body>
    if '<div class="mobile-top-bar">' not in html:
        body_start = html.find("<body>")
        if body_start != -1:
            insert_pos = body_start + len("<body>\n")
            html = html[:insert_pos] + MOBILE_HTML_BANDO4 + "\n" + html[insert_pos:]
            print("Injected MOBILE_HTML_BANDO4")

    # 3. Inject Mobile JS before </body>
    if "function openDrawer()" not in html:
        body_end = html.rfind("</body>")
        if body_end != -1:
            html = html[:body_end] + f"<script>\n{MOBILE_JS_BANDO4}\n</script>\n" + html[body_end:]
            print("Injected MOBILE_JS_BANDO4")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Completed {file_path} successfully!")

if __name__ == "__main__":
    update_bando4_html(r"C:\Work\반도체4_AISK대비\index.html")
    update_bando4_html(r"C:\Work\반도체4_AISK대비\result\261010_v1.0\index.html")
    print("Done applying mobile UI to 반도체 4!")
