# -*- coding: utf-8 -*-
import json
import re

# 1. topics_dump.json 읽기
with open(r'C:\Work\반도체4_AISK대비\tool\topics_dump.json', 'r', encoding='utf-8') as f:
    topics_list = json.load(f)

print(f"Loaded {len(topics_list)} topics from dump.")

# 2. index.html 읽기
with open(r'C:\Work\반도체4_AISK대비\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 3. CSS 추가: 직무·소자 서브필터 박스 스타일
subfilter_css = """
    /* 🛠 직무·소자 공정 서브필터 컴팩트 박스 */
    .proc-subfilter-box {
      padding: 10px 14px;
      background: rgba(15, 23, 42, 0.65);
      border-bottom: 1px solid var(--border);
      backdrop-filter: blur(8px);
    }
    .proc-subfilter-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6px;
    }
    .proc-subfilter-title {
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--text-muted);
      letter-spacing: 0.5px;
      text-transform: uppercase;
      display: flex;
      align-items: center;
      gap: 4px;
    }
    .proc-subfilter-reset {
      font-size: 0.7rem;
      color: var(--primary-light);
      cursor: pointer;
      padding: 2px 6px;
      border-radius: 4px;
      background: rgba(56, 189, 248, 0.1);
      transition: all 0.2s;
    }
    .proc-subfilter-reset:hover {
      background: rgba(56, 189, 248, 0.25);
      color: #fff;
    }
    .proc-subfilter-chips {
      display: flex;
      flex-wrap: wrap;
      gap: 4px;
    }
    .proc-chip {
      padding: 4px 7px;
      font-size: 0.76rem;
      font-weight: 800;
      font-family: inherit;
      border-radius: 5px;
      border: 1px solid rgba(255, 255, 255, 0.08);
      background: #1e293b;
      color: var(--text-sub);
      cursor: pointer;
      transition: all 0.18s ease;
      min-width: 26px;
      text-align: center;
      line-height: 1.2;
    }
    .proc-chip:hover {
      background: #334155;
      color: var(--text-main);
      border-color: rgba(56, 189, 248, 0.4);
      transform: translateY(-1px);
    }
    .proc-chip.active {
      background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
      color: #ffffff;
      border-color: #38bdf8;
      box-shadow: 0 0 10px rgba(56, 189, 248, 0.35);
    }
    .proc-chip.chip-dev {
      min-width: 36px;
    }
    .proc-chip.chip-dev.active {
      background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%);
      border-color: #a78bfa;
      box-shadow: 0 0 10px rgba(167, 139, 250, 0.35);
    }

    /* 메인 본문 상단 숏컷 바 */
    .main-proc-bar {
      margin-bottom: 20px;
      padding: 12px 18px;
      background: linear-gradient(135deg, rgba(30, 41, 59, 0.7) 0%, rgba(15, 23, 42, 0.8) 100%);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }
    .main-proc-label {
      font-size: 0.82rem;
      color: var(--text-sub);
      display: flex;
      align-items: center;
      gap: 6px;
      white-space: nowrap;
    }
    .main-proc-label strong {
      color: var(--text-main);
    }
    .main-proc-chips {
      display: flex;
      flex-wrap: wrap;
      gap: 5px;
      align-items: center;
    }
"""

if '.proc-subfilter-box' not in html:
    html = html.replace('</style>', subfilter_css + '\n  </style>')

# 4. 사이드바 서브필터 박스 HTML 삽입
subfilter_html = """
    <!-- 직무·소자 공정 서브필터 컴팩트 박스 -->
    <div class="proc-subfilter-box" id="procSubfilterBox">
      <div class="proc-subfilter-header">
        <span class="proc-subfilter-title">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18"/><path d="M9 21V9"/></svg>
          공정·소자 숏컷
        </span>
        <span class="proc-subfilter-reset" onclick="selectProcessFilter('ALL')">전체보기</span>
      </div>
      <div class="proc-subfilter-chips">
        <button class="proc-chip active" data-proc="ALL" title="직무·소자 전체 (45문항)" onclick="selectProcessFilter('ALL')">ALL</button>
        <button class="proc-chip" data-proc="W" title="W: 웨이퍼 제조공정 (5문항)" onclick="selectProcessFilter('W')">W</button>
        <button class="proc-chip" data-proc="O" title="O: 산화공정 (5문항)" onclick="selectProcessFilter('O')">O</button>
        <button class="proc-chip" data-proc="P" title="P: 포토공정 (5문항)" onclick="selectProcessFilter('P')">P</button>
        <button class="proc-chip" data-proc="E" title="E: 식각공정 (5문항)" onclick="selectProcessFilter('E')">E</button>
        <button class="proc-chip" data-proc="D" title="D: 박막(데포)공정 (5문항)" onclick="selectProcessFilter('D')">D</button>
        <button class="proc-chip" data-proc="I" title="I: 이온주입공정 (5문항)" onclick="selectProcessFilter('I')">I</button>
        <button class="proc-chip" data-proc="M" title="M: 금속배선공정 (5문항)" onclick="selectProcessFilter('M')">M</button>
        <button class="proc-chip" data-proc="PKG" title="P: 패키징공정 (5문항)" onclick="selectProcessFilter('PKG')">P</button>
        <button class="proc-chip chip-dev" data-proc="DEV" title="반도체 소자 (5문항)" onclick="selectProcessFilter('DEV')">소자</button>
      </div>
    </div>
"""

pattern_tabs = r'(<div class="filter-tabs">.*?</div>)'
m_tabs = re.search(pattern_tabs, html, re.DOTALL)
if m_tabs and 'procSubfilterBox' not in html:
    html = html.replace(m_tabs.group(1), m_tabs.group(1) + '\n' + subfilter_html)

# 5. 메인 본문 상단 숏컷 바 삽입
main_shortcut_html = """
      <!-- 🚀 메인 본문 공정·소자 빠른 점프 바 -->
      <div class="main-proc-bar">
        <div class="main-proc-label">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
          <strong>직무·소자 WOPEDIMP 숏컷:</strong>
        </div>
        <div class="main-proc-chips">
          <button class="proc-chip active" data-proc="ALL" title="직무·소자 전체 (45문항)" onclick="selectProcessFilter('ALL')">ALL (45)</button>
          <button class="proc-chip" data-proc="W" title="W: 웨이퍼 제조공정 (5문항)" onclick="selectProcessFilter('W')">W 웨이퍼</button>
          <button class="proc-chip" data-proc="O" title="O: 산화공정 (5문항)" onclick="selectProcessFilter('O')">O 산화</button>
          <button class="proc-chip" data-proc="P" title="P: 포토공정 (5문항)" onclick="selectProcessFilter('P')">P 포토</button>
          <button class="proc-chip" data-proc="E" title="E: 식각공정 (5문항)" onclick="selectProcessFilter('E')">E 에칭</button>
          <button class="proc-chip" data-proc="D" title="D: 박막(데포)공정 (5문항)" onclick="selectProcessFilter('D')">D 데포</button>
          <button class="proc-chip" data-proc="I" title="I: 이온주입공정 (5문항)" onclick="selectProcessFilter('I')">I 이온</button>
          <button class="proc-chip" data-proc="M" title="M: 금속배선공정 (5문항)" onclick="selectProcessFilter('M')">M 메탈</button>
          <button class="proc-chip" data-proc="PKG" title="P: 패키징공정 (5문항)" onclick="selectProcessFilter('PKG')">P 패키징</button>
          <button class="proc-chip chip-dev" data-proc="DEV" title="반도체 소자 (5문항)" onclick="selectProcessFilter('DEV')">소자 DEV</button>
        </div>
      </div>
"""

if 'main-proc-bar' not in html:
    html = html.replace('<div id="topicContainer">', main_shortcut_html + '\n      <div id="topicContainer">')

# 6. DEFAULT_TOPICS 데이터 안전 교체 (정확한 인덱스 슬라이싱)
json_formatted = json.dumps(topics_list, ensure_ascii=False, indent=2)
prefix = 'const DEFAULT_TOPICS = '
start_idx = html.find(prefix)
if start_idx == -1:
    raise ValueError("const DEFAULT_TOPICS not found")

# find closing semicolon of DEFAULT_TOPICS
semi_idx = html.find(';\n\n    //', start_idx)
if semi_idx == -1:
    semi_idx = html.find(';\n\n    const STORAGE_KEY', start_idx)
if semi_idx == -1:
    semi_idx = html.find(';', start_idx + len(prefix))

html = html[:start_idx + len(prefix)] + json_formatted + html[semi_idx:]
print("Safely replaced DEFAULT_TOPICS.")

# 7. JS 로직 고도화:
# - STORAGE_KEY 버전 업데이트 (v15_wopedimp)
html = re.sub(r"const STORAGE_KEY = 'aisk_master_topics_custom_v\d+';", "const STORAGE_KEY = 'aisk_master_topics_custom_v15_wopedimp';", html)

# - updateCounters() 함수 개선
old_counters = """    function updateCounters() {
      const totalCount = currentTopics.length;
      const pCount = currentTopics.filter(t => t.category === 'personality').length;
      const tCount = currentTopics.filter(t => t.category === 'tech').length;

      document.getElementById('tabAll').textContent = `전체 (${totalCount})`;
      document.getElementById('tabPersonality').textContent = `인성·협업 (${pCount})`;
      document.getElementById('tabTech').textContent = `직무·소자 (${tCount})`;
    }"""

new_counters = """    function updateCounters() {
      const totalCount = currentTopics.length;
      const pCount = currentTopics.filter(t => t.category === 'personality').length;
      const tCount = currentTopics.filter(t => t.category === 'tech').length;

      const tabAll = document.getElementById('tabAll');
      const tabPersonality = document.getElementById('tabPersonality');
      const tabTech = document.getElementById('tabTech');

      if (tabAll) tabAll.textContent = `전체 (${totalCount})`;
      if (tabPersonality) tabPersonality.textContent = `인성·협업 (${pCount})`;
      if (tabTech) tabTech.textContent = `직무·소자 (${tCount})`;
    }"""

if old_counters in html:
    html = html.replace(old_counters, new_counters)

# - renderSidebar() 함수 개선
old_sidebar_loop = """      currentTopics.forEach((t, index) => {
        const cat = t.category;
        const num = t.number || (index + 1);
        const title = escapeHtml(t.title);
        const keywordsStr = (t.core_keyword || []).join(' ');
        
        let numStr = '';
        let badgeClass = '';
        if (cat === 'personality') {
          numStr = `인성-${String(num).padStart(2, '0')}`;
          badgeClass = 'cat-badge-p';
        } else {
          numStr = `직무-${String(num).padStart(2, '0')}`;
          badgeClass = 'cat-badge-t';
        }

        html += `
          <li class="nav-item" data-category="${cat}" data-search="${title} ${escapeHtml(keywordsStr)} ${numStr}">
            <a href="#${t.id}" class="nav-link" id="link-${t.id}">
              <span class="nav-num ${badgeClass}">${numStr}</span>
              <span class="nav-text">${title}</span>
            </a>
          </li>
        `;
      });"""

new_sidebar_loop = """      currentTopics.forEach((t, index) => {
        const cat = t.category;
        const proc = t.process || '';
        const num = t.number || (index + 1);
        const title = escapeHtml(t.title);
        const keywordsStr = (t.core_keyword || []).join(' ');
        
        let numStr = '';
        let badgeClass = '';
        if (cat === 'personality') {
          numStr = `인성-${String(num).padStart(2, '0')}`;
          badgeClass = 'cat-badge-p';
        } else {
          if (proc === 'DEV') {
            numStr = `소자-${String(num).padStart(2, '0')}`;
          } else if (proc) {
            numStr = `${proc}-${String(num).padStart(2, '0')}`;
          } else {
            numStr = `직무-${String(num).padStart(2, '0')}`;
          }
          badgeClass = 'cat-badge-t';
        }

        html += `
          <li class="nav-item" data-category="${cat}" data-process="${proc}" data-search="${title} ${escapeHtml(keywordsStr)} ${numStr} ${proc}">
            <a href="#${t.id}" class="nav-link" id="link-${t.id}">
              <span class="nav-num ${badgeClass}">${numStr}</span>
              <span class="nav-text">${title}</span>
            </a>
          </li>
        `;
      });"""

if old_sidebar_loop in html:
    html = html.replace(old_sidebar_loop, new_sidebar_loop)

# - renderCards() 함수 개선
old_card_num = """        let numStr = '';
        let badgeClass = '';
        if (cat === 'personality') {
          numStr = `인성-${String(num).padStart(2, '0')}`;
          badgeClass = 'cat-badge-p';
        } else {
          numStr = `직무-${String(num).padStart(2, '0')}`;
          badgeClass = 'cat-badge-t';
        }"""

new_card_num = """        const proc = t.process || '';
        let numStr = '';
        let badgeClass = '';
        if (cat === 'personality') {
          numStr = `인성-${String(num).padStart(2, '0')}`;
          badgeClass = 'cat-badge-p';
        } else {
          if (proc === 'DEV') {
            numStr = `소자-${String(num).padStart(2, '0')}`;
          } else if (proc) {
            numStr = `${proc}-${String(num).padStart(2, '0')}`;
          } else {
            numStr = `직무-${String(num).padStart(2, '0')}`;
          }
          badgeClass = 'cat-badge-t';
        }"""

if old_card_num in html:
    html = html.replace(old_card_num, new_card_num)

html = html.replace(
    '<section class="topic-section" id="${t.id}" data-category="${cat}">',
    '<section class="topic-section" id="${t.id}" data-category="${cat}" data-process="${proc}">'
)

# - 필터 및 검색 로직 개선
old_filter_logic = """    function applyFilterAndSearch() {
      const activeFilterChip = document.querySelector('.filter-chip.active');
      const filter = activeFilterChip ? activeFilterChip.getAttribute('data-filter') : 'all';
      const query = searchInput.value.toLowerCase().trim();

      const navItems = document.querySelectorAll('.nav-item');
      const topicSections = document.querySelectorAll('.topic-section');

      navItems.forEach(item => {
        const itemCat = item.getAttribute('data-category');
        const searchData = item.getAttribute('data-search').toLowerCase();

        const catMatch = (filter === 'all' || itemCat === filter);
        const searchMatch = (query === '' || searchData.includes(query));

        item.style.display = (catMatch && searchMatch) ? 'block' : 'none';
      });

      topicSections.forEach(section => {
        const secCat = section.getAttribute('data-category');
        const secText = section.innerText.toLowerCase();

        const catMatch = (filter === 'all' || secCat === filter);
        const searchMatch = (query === '' || secText.includes(query));

        section.style.display = (catMatch && searchMatch) ? 'block' : 'none';
      });
    }"""

new_filter_logic = """    let currentProcessFilter = 'ALL';

    function selectProcessFilter(proc) {
      currentProcessFilter = proc;

      // 직무·소자 칩 활성화 상태 동기화 (사이드바 및 메인 상단 모두)
      document.querySelectorAll('.proc-chip').forEach(btn => {
        if (btn.getAttribute('data-proc') === proc) {
          btn.classList.add('active');
        } else {
          btn.classList.remove('active');
        }
      });

      // 만약 인성 탭이 켜져 있는 상태에서 특정 공정을 누르면 직무·소자 탭으로 자동 전환
      const activeFilterChip = document.querySelector('.filter-chip.active');
      if (activeFilterChip && activeFilterChip.getAttribute('data-filter') === 'personality' && proc !== 'ALL') {
        document.querySelectorAll('.filter-chip').forEach(c => c.classList.remove('active'));
        const tabTech = document.getElementById('tabTech');
        if (tabTech) tabTech.classList.add('active');
      }

      applyFilterAndSearch();
    }

    function applyFilterAndSearch() {
      const activeFilterChip = document.querySelector('.filter-chip.active');
      const filter = activeFilterChip ? activeFilterChip.getAttribute('data-filter') : 'all';
      const query = searchInput.value.toLowerCase().trim();

      const navItems = document.querySelectorAll('.nav-item');
      const topicSections = document.querySelectorAll('.topic-section');

      navItems.forEach(item => {
        const itemCat = item.getAttribute('data-category');
        const itemProc = item.getAttribute('data-process') || '';
        const searchData = item.getAttribute('data-search').toLowerCase();

        // 1. 카테고리 매칭
        let catMatch = (filter === 'all' || itemCat === filter);

        // 2. 공정 서브필터 매칭 (currentProcessFilter가 ALL이 아니면 해당 공정만)
        let procMatch = true;
        if (currentProcessFilter !== 'ALL') {
          if (itemCat === 'tech') {
            procMatch = (itemProc === currentProcessFilter);
          } else {
            procMatch = false;
          }
        }

        // 3. 검색어 매칭
        const searchMatch = (query === '' || searchData.includes(query));

        item.style.display = (catMatch && procMatch && searchMatch) ? 'block' : 'none';
      });

      topicSections.forEach(section => {
        const secCat = section.getAttribute('data-category');
        const secProc = section.getAttribute('data-process') || '';
        const secText = section.innerText.toLowerCase();

        let catMatch = (filter === 'all' || secCat === filter);

        let procMatch = true;
        if (currentProcessFilter !== 'ALL') {
          if (secCat === 'tech') {
            procMatch = (secProc === currentProcessFilter);
          } else {
            procMatch = false;
          }
        }

        const searchMatch = (query === '' || secText.includes(query));

        section.style.display = (catMatch && procMatch && searchMatch) ? 'block' : 'none';
      });
    }"""

if old_filter_logic in html:
    html = html.replace(old_filter_logic, new_filter_logic)

# 저장
with open(r'C:\Work\반도체4_AISK대비\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html successfully! Size:", len(html))
