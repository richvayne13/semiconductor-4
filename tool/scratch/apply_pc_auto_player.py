# -*- coding: utf-8 -*-
import re

html_path = r"C:\Work\반도체4_AISK대비\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# ==============================================================================
# 1. CSS 개선: PC 화면에서 중앙 하단 플로팅 독으로 아름답게 자리잡도록 스타일 보강
# ==============================================================================
pc_dock_css = """
    /* PC 대화면 전용 플로팅 도크 스타일 */
    @media (min-width: 901px) {
      .auto-player-dock {
        left: 50% !important;
        right: auto !important;
        transform: translateX(-50%) !important;
        width: 880px !important;
        max-width: 92vw !important;
        border-radius: 16px 16px 0 0 !important;
        border-left: 1.5px solid rgba(56, 189, 248, 0.5) !important;
        border-right: 1.5px solid rgba(56, 189, 248, 0.5) !important;
        box-shadow: 0 -12px 48px rgba(0, 0, 0, 0.85) !important;
      }
    }
"""

if "/* PC 대화면 전용 플로팅 도크 스타일 */" not in content:
    content = content.replace("</style>", pc_dock_css + "\n  </style>", 1)
    print("Added PC dock CSS.")

# ==============================================================================
# 2. PC 좌측 사이드바 상단에 [🎧 연속 자동 듣기 모드] 버튼 추가
# ==============================================================================
target_side = """        <button class="mode-toggle-btn" id="btnModeInterviewSide" onclick="toggleViewMode('interview')" style="flex: 1; justify-content: center;">
          <span>🎙️ 실전 면접</span>
        </button>
      </div>
    </div>"""

replacement_side = """        <button class="mode-toggle-btn" id="btnModeInterviewSide" onclick="toggleViewMode('interview')" style="flex: 1; justify-content: center;">
          <span>🎙️ 실전 면접</span>
        </button>
      </div>
    </div>

    <!-- 🎧 PC 사이드바: 연속 자동 듣기 모드 버튼 -->
    <div style="padding: 0 16px 12px 16px;">
      <button class="btn-voice-toggle" onclick="toggleAutoPlayerDock()" style="width: 100%; justify-content: center; background: linear-gradient(135deg, #f59e0b 0%, #ef4444 100%); color: #fff; border: none; padding: 9px 14px; font-size: 0.84rem; font-weight: 800; border-radius: 8px; box-shadow: 0 4px 14px rgba(245, 158, 11, 0.35); cursor: pointer;" title="질문 읽고 10초 후 답변 읽기를 무한 자동 반복하는 핸즈프리 모드">
        <span>🎧 연속 자동 듣기 모드</span>
      </button>
    </div>"""

if "<!-- 🎧 PC 사이드바: 연속 자동 듣기 모드 버튼 -->" not in content and target_side in content:
    content = content.replace(target_side, replacement_side, 1)
    print("Added Auto Player button to PC sidebar.")
else:
    print("Notice: target_side not found or already added.")

# ==============================================================================
# 3. PC 메인 상단 헤더에 [🎧 연속 자동 듣기] 버튼 추가
# ==============================================================================
target_main = """            <button class="mode-toggle-btn" id="btnModeInterviewMain" onclick="toggleViewMode('interview')">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="22"></line></svg>
              <span>🎙️ 실전 면접 연습 모드</span>
            </button>
          </div>"""

replacement_main = """            <button class="mode-toggle-btn" id="btnModeInterviewMain" onclick="toggleViewMode('interview')">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="22"></line></svg>
              <span>🎙️ 실전 면접 연습 모드</span>
            </button>
          </div>
          <!-- 🎧 PC 메인 헤더: 연속 자동 듣기 버튼 -->
          <button class="btn-voice-toggle" onclick="toggleAutoPlayerDock()" style="margin-left: 8px; background: linear-gradient(135deg, #f59e0b 0%, #ef4444 100%); color: #fff; border: none; padding: 7px 15px; font-size: 0.84rem; font-weight: 800; border-radius: 8px; box-shadow: 0 4px 14px rgba(245, 158, 11, 0.35); cursor: pointer; display: inline-flex; align-items: center; gap: 6px;" title="질문 읽고 10초 후 답변 읽기를 무한 자동 반복하는 핸즈프리 모드">
            <span>🎧 연속 자동 듣기</span>
          </button>"""

if "<!-- 🎧 PC 메인 헤더: 연속 자동 듣기 버튼 -->" not in content and target_main in content:
    content = content.replace(target_main, replacement_main, 1)
    print("Added Auto Player button to PC main header.")
else:
    print("Notice: target_main not found or already added.")

# ==============================================================================
# 4. 실전 면접 모드 (Interview Mode) 상단 바에도 버튼 추가
# ==============================================================================
target_int_bar = """          <div class="interview-action-group">
            <button class="btn-voice-toggle active" id="btnAutoVoiceToggle" onclick="toggleAutoVoiceAndRecord()" title="문항 전환 시 질문 음성 자동 재생 후 녹음 자동 시작">
              <span id="btnAutoVoiceText">🔊 자동 질문&녹음: ON</span>
            </button>"""

replacement_int_bar = """          <div class="interview-action-group">
            <button class="btn-voice-toggle" onclick="toggleAutoPlayerDock()" style="background: linear-gradient(135deg, #f59e0b 0%, #ef4444 100%); color: #fff; border: none; box-shadow: 0 0 12px rgba(245, 158, 11, 0.4); padding: 7px 14px; font-weight: 800;" title="질문 읽고 10초 후 답변 읽기를 무한 자동 반복하는 핸즈프리 모드">
              <span>🎧 연속 자동 듣기</span>
            </button>
            <button class="btn-voice-toggle active" id="btnAutoVoiceToggle" onclick="toggleAutoVoiceAndRecord()" title="문항 전환 시 질문 음성 자동 재생 후 녹음 자동 시작">
              <span id="btnAutoVoiceText">🔊 자동 질문&녹음: ON</span>
            </button>"""

if 'title="질문 읽고 10초 후 답변 읽기를 무한 자동 반복하는 핸즈프리 모드"' not in content and target_int_bar in content:
    content = content.replace(target_int_bar, replacement_int_bar, 1)
    print("Added Auto Player button to Interview Mode action group.")

# ==============================================================================
# 5. build-time 및 STORAGE_KEY 갱신
# ==============================================================================
new_storage_key = "aisk_master_topics_custom_v23_pc_auto_player"
content = content.replace("aisk_master_topics_custom_v22_auto_player", new_storage_key)

content = re.sub(
    r'<meta name="build-time" content="[^"]+">',
    '<meta name="build-time" content="2026-10-25T11:15:00+09:00">',
    content
)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Successfully updated PC Auto-Player UI into {html_path}! Total size: {len(content)} bytes.")
