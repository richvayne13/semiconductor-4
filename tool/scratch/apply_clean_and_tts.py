# -*- coding: utf-8 -*-
import json
import re

html_path = r"C:\Work\반도체4_AISK대비\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# ==============================================================================
# 1. DEFAULT_TOPICS 텍스트 정제 (불필요한 영어 괄호 제거, 필수 약어는 보존)
# ==============================================================================
KEEP_EXACT_ACRONYMS = {
    'ICP', 'EUV', 'ALD', 'CVD', 'PVD', 'DRAM', 'NAND', 'HBM', 'TSV', 'CMP', 'PR',
    'BARC', 'CAR', 'MOR', 'CTF', 'BLSA', 'DOF', 'DoF', 'EL', 'GAA', 'MIM', 'ZAZ',
    'HARC', 'BSPDN', 'CXL', 'PIM', 'PNM', 'ISPP', 'LDPC', 'ECC', 'PUC', 'COP',
    'GIDL', 'TRR', 'BCAT', 'VCT', 'EM', 'RIE', 'ECD', 'PEB', 'PAG', 'LER', 'LWR',
    'NTD', 'OAI', 'PSM', 'RET', 'UHV', 'CNT', 'CTE', 'PECVD', 'HF', 'LF', 'RF',
    'SEG', 'SCE', 'SILC', 'TLC', 'QLC', 'MLC', 'SLC', 'MR-MUF', 'NCF', 'TCB', 'EMC',
    'SOH', 'ACL', 'STI', 'ILD', 'IMD', '1T-1C', '1T1C', 'MAC', 'TCO', 'EOT', 'CD',
    'NA', 'SOP', 'SPC', 'FMEA', 'OOC', 'OOS', 'IP', 'PIR', 'HDP', 'TEOS', 'BL', 'WL',
    'DIP', 'QFP', 'BGA', 'WLP', 'FOWLP', 'RDL', 'SiP', 'CoWoS', 'PLP', 'SADP', 'SAQP',
    'OPC', 'DSA', 'EBR', 'HMDS', 'TMAH', 'PFC', 'GWP', 'SWAP', 'LPP', 'AI', 'GPU',
    'CPU', 'NPU', 'LLM', 'PCIe', 'DMA', 'OS', 'ALU', 'DDR', 'GDDR', 'SONOS', 'ONO',
    'CMOS', 'NMOS', 'PMOS', 'FinFET', 'MBCFET', 'MOSFET', 'FET', 'SiGe', 'eSiGe'
}

REMOVE_ELEMENT_AFTER_KOR = {'Cu', 'Al', 'Si', 'Sn', 'Ru', 'Mo', 'Co', 'W', 'Ti', 'Ni', 'Au', 'B', 'P', 'As'}

def clean_script_text(text):
    if not text:
        return ""

    # Standalone unwanted phrases in parentheses
    unwanted = [
        r'\(\s*METAL\s+ION\s*\)',
        r'\(\s*IONIZED\s+PVD\s*\)',
        r'\(\s*OVERHANG\s*\)',
        r'\(\s*Overhang\s*\)',
        r'\(\s*Ionized\s+PVD\s*\)',
        r'\(\s*Metal\s+Ion\s*\)',
    ]
    for p in unwanted:
        text = re.sub(p, '', text, flags=re.IGNORECASE)

    def replacer(m):
        kor = m.group(1)
        content = m.group(2).strip()

        # Check if content has Acronyms, e.g. (CAR, Chemically Amplified Resist) -> (CAR)
        # or (Electromigration, EM) -> (EM)
        parts = [p.strip() for p in re.split(r'[,/]', content)]
        found_acronyms = [p for p in parts if p in KEEP_EXACT_ACRONYMS and p not in REMOVE_ELEMENT_AFTER_KOR]
        if found_acronyms:
            acr_str = ", ".join(found_acronyms)
            return f"{kor}({acr_str})"

        if content in KEEP_EXACT_ACRONYMS:
            if content in REMOVE_ELEMENT_AFTER_KOR:
                return kor
            return f"{kor}({content})"

        # Keep pure Korean parentheses, e.g. (옥사이드) or (1)
        if not re.search(r'[A-Za-z]', content):
            return f"{kor}({content})"

        # Otherwise remove English repetition!
        return kor

    # Replace Korean word immediately followed by parenthesis
    text = re.sub(r'([가-힣]+)\s*\(([^()]+)\)', replacer, text)
    text = re.sub(r'[ \t]{2,}', ' ', text)
    return text

# Extract DEFAULT_TOPICS
start_marker = "const DEFAULT_TOPICS = ["
idx_start = html.find(start_marker)
if idx_start == -1:
    raise ValueError("start_marker not found")

end_marker = "    const STORAGE_KEY = 'aisk_master_topics_custom_v20_wopedimp_real_exam';"
idx_end = html.find(end_marker, idx_start)
if idx_end == -1:
    raise ValueError("end_marker not found")

existing_json_str = html[idx_start + len("const DEFAULT_TOPICS = "):idx_end].strip()
if existing_json_str.endswith(";"):
    existing_json_str = existing_json_str[:-1].strip()

topics = json.loads(existing_json_str)
print(f"Loaded {len(topics)} topics for cleaning.")

mod_count = 0
for t in topics:
    orig_s = t.get('speech_1m30s', '')
    orig_a = t.get('speech_alt', '')
    orig_t = t.get('title', '')

    new_s = clean_script_text(orig_s)
    new_a = clean_script_text(orig_a)
    new_t = clean_script_text(orig_t)

    if new_s != orig_s or new_a != orig_a or new_t != orig_t:
        mod_count += 1
        t['speech_1m30s'] = new_s
        t['speech_alt'] = new_a
        t['title'] = new_t

print(f"Cleaned {mod_count} topics out of {len(topics)}.")

new_storage_key = "aisk_master_topics_custom_v21_cleaned_tts"
formatted_json = json.dumps(topics, ensure_ascii=False, indent=2)
replacement = f"const DEFAULT_TOPICS = {formatted_json};\n\n    const STORAGE_KEY = '{new_storage_key}';"

html = html[:idx_start] + replacement + html[idx_end + len(end_marker):]
html = html.replace("aisk_master_topics_custom_v20_wopedimp_real_exam", new_storage_key)

# ==============================================================================
# 2. CSS 스타일 추가: .btn-play-lecture
# ==============================================================================
lecture_btn_css = """
    /* 🔊 심화해설 아나운서 TTS 재생 버튼 */
    .btn-play-lecture {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      padding: 4px 10px;
      font-size: 0.76rem;
      font-weight: 700;
      border-radius: 6px;
      border: 1px solid rgba(56, 189, 248, 0.45);
      background: rgba(56, 189, 248, 0.12);
      color: #38bdf8;
      cursor: pointer;
      transition: all 0.2s;
      font-family: inherit;
    }
    .btn-play-lecture:hover {
      background: #0284c7;
      color: #fff;
      border-color: #38bdf8;
      box-shadow: 0 0 10px rgba(56, 189, 248, 0.35);
    }
    .btn-play-lecture.playing {
      background: #0284c7;
      color: #fff;
      border-color: #38bdf8;
      box-shadow: 0 0 14px rgba(56, 189, 248, 0.65);
      animation: recPulse 1.2s infinite;
    }
"""

if ".btn-play-lecture" not in html:
    html = html.replace("</style>", lecture_btn_css + "\n  </style>", 1)
    print("Added .btn-play-lecture CSS.")

# ==============================================================================
# 3. HTML 렌더링에 재생 버튼 삽입
# ==============================================================================
# 3-1. 학습 모드 심화해설 헤더 버튼
# Find:
old_learn_header = """                  <button class="btn-card-action" onclick="copySpeech('${t.id}', 1)" title="답변 복사">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                    ${isPersonality ? '답변 1 복사' : '심화해설 복사'}
                  </button>"""

new_learn_header = """                  <div style="display:flex; align-items:center; gap:6px;">
                    <button class="btn-card-action btn-play-lecture" id="btn-play-lecture-${t.id}" onclick="toggleLectureVoice('${t.id}')" title="아나운서 음성(TTS)으로 심화해설을 들으며 학습합니다">
                      <span id="txt-play-lecture-${t.id}">🔊 심화해설 듣기</span>
                    </button>
                    <button class="btn-card-action" onclick="copySpeech('${t.id}', 1)" title="답변 복사">
                      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                      ${isPersonality ? '답변 1 복사' : '심화해설 복사'}
                    </button>
                  </div>"""

if old_learn_header in html:
    html = html.replace(old_learn_header, new_learn_header, 1)
    print("Injected TTS play button into Learn View card header.")
else:
    print("Notice: old_learn_header not directly matched, checking alternatives.")

# 3-2. 면접 모드 모범답안 헤더 버튼
old_int_header = """              <div style="display:flex; align-items:center; gap:10px;">
                <span style="font-size:0.8rem; color:var(--text-muted);">해설 분량: <strong id="int-len-tag-${topic.id}" style="color:${color1};">${cleanLen1}자</strong></span>
                <button class="btn-card-action" onclick="copySpeech('${topic.id}', 1)" title="심화해설 복사" style="padding:3px 8px; font-size:0.74rem;">📋 심화해설 복사</button>
              </div>"""

new_int_header = """              <div style="display:flex; align-items:center; gap:8px;">
                <span style="font-size:0.8rem; color:var(--text-muted);">해설 분량: <strong id="int-len-tag-${topic.id}" style="color:${color1};">${cleanLen1}자</strong></span>
                <button class="btn-card-action btn-play-lecture" id="btn-int-play-lecture-${topic.id}" onclick="toggleLectureVoice('${topic.id}', 'int')" title="아나운서 음성(TTS)으로 심화해설을 들으며 연습합니다" style="padding:3px 8px; font-size:0.74rem;">
                  <span id="txt-int-play-lecture-${topic.id}">🔊 심화해설 듣기</span>
                </button>
                <button class="btn-card-action" onclick="copySpeech('${topic.id}', 1)" title="심화해설 복사" style="padding:3px 8px; font-size:0.74rem;">📋 심화해설 복사</button>
              </div>"""

if old_int_header in html:
    html = html.replace(old_int_header, new_int_header, 1)
    print("Injected TTS play button into Interview Mode model answer header.")
else:
    print("Notice: old_int_header not directly matched.")

# ==============================================================================
# 4. 자바스크립트 엔진: cleanTextForTTS & toggleLectureVoice
# ==============================================================================
lecture_js = """
    // ==============================================================================
    // 🔊 심화해설 전문 아나운서 음성(TTS) 재생 및 텍스트 정제 엔진
    // ==============================================================================
    let currentLectureUtterance = null;
    let playingLectureTopicId = null;
    let playingLectureMode = null; // 'learn' | 'int'

    // 아나운서 TTS 발음 최적화 및 괄호 영문 완전 정제 함수
    function cleanTextForAnnouncerTTS(rawText) {
      if (!rawText) return '';
      let text = rawText;

      // 1. HTML 태그 제거
      text = text.replace(/<[^>]+>/g, ' ');

      // 2. 괄호 처리:
      // (1) 약어 목록에 있는 괄호: 괄호만 벗겨서 자연스럽게 발음되도록 치환
      // (2) 그 외 모든 영문 포함 괄호: 괄호 및 내부 텍스트 완전 제거
      const keepAcronymsSet = new Set([
        'ICP', 'EUV', 'ALD', 'CVD', 'PVD', 'DRAM', 'NAND', 'HBM', 'TSV', 'CMP', 'PR',
        'BARC', 'CAR', 'MOR', 'CTF', 'BLSA', 'DOF', 'DoF', 'EL', 'GAA', 'MIM', 'ZAZ',
        'HARC', 'BSPDN', 'CXL', 'PIM', 'PNM', 'ISPP', 'LDPC', 'ECC', 'PUC', 'COP',
        'GIDL', 'TRR', 'BCAT', 'VCT', 'EM', 'RIE', 'ECD', 'PEB', 'PAG', 'LER', 'LWR',
        'NTD', 'OAI', 'PSM', 'RET', 'UHV', 'CNT', 'CTE', 'PECVD', 'HF', 'LF', 'RF',
        'SEG', 'SCE', 'SILC', 'TLC', 'QLC', 'MLC', 'SLC', 'MR-MUF', 'NCF', 'TCB', 'EMC',
        'SOH', 'ACL', 'STI', 'ILD', 'IMD', '1T-1C', '1T1C', 'MAC', 'TCO', 'EOT', 'CD',
        'NA', 'SOP', 'SPC', 'FMEA', 'OOC', 'OOS', 'IP', 'PIR', 'HDP', 'TEOS', 'BL', 'WL'
      ]);

      text = text.replace(/\\(([^()]+)\\)/g, (match, inner) => {
        const trimmed = inner.trim();
        // 만약 보존할 약어에 속하면 괄호를 벗겨서 단어만 남김
        if (keepAcronymsSet.has(trimmed)) {
          return ' ' + trimmed + ' ';
        }
        // 순수 한글이나 숫자 괄호(예: (1), (첫째))는 보존
        if (!/[A-Za-z]/.test(trimmed)) {
          return match;
        }
        // 그 외 모든 영어 나열/병기 괄호는 완전 제거
        return ' ';
      });

      // 3. 발음 및 수식·단위 친화적 한글 치환 사전
      const phonetics = [
        [/1T-1C|1T1C/gi, '원티 원씨'],
        [/SiO2/g, '에스아이오투'],
        [/Si3N4/g, '에스아이쓰리엔포'],
        [/Al2O3/g, '알루미나'],
        [/ZrO2/g, '지르코니아'],
        [/TiN/g, '질화티타늄'],
        [/TaN/g, '질화탄탈륨'],
        [/Ta/g, '탄탈륨'],
        [/Ti/g, '티타늄'],
        [/Ru/g, '루테늄'],
        [/Mo/g, '몰리브덴'],
        [/Sn/g, '주석'],
        [/SiGe/g, '실리콘 게르마늄'],
        [/eSiGe/g, '임베디드 실리콘 게르마늄'],
        [/HfO2/g, '하프니아'],
        [/SnH4/g, '스타난'],
        [/CuClx|CuCl/g, '염화구리'],
        [/AlCl3/g, '염화알루미늄'],
        [/NF3/g, '삼불화질소'],
        [/CF4/g, '사불화탄소'],
        [/C4F8/g, '옥타플루오로사이클로부탄'],
        [/SF6/g, '육불화황'],
        [/WF6/g, '육불화텅스텐'],
        [/SiH4/g, '실란'],
        [/NH3/g, '암모니아'],
        [/H2O2/g, '과산화수소'],
        [/H2SO4/g, '황산'],
        [/HCl/g, '염산'],
        [/HF/g, '불산'],
        [/IPA/g, '아이피에이'],
        [/MR-MUF/g, '엠알 엠유에프'],
        [/NCF/g, '엔씨에프'],
        [/TCB/g, '티씨비'],
        [/EMC/g, '이엠씨'],
        [/BSPDN/g, '비에스피디엔'],
        [/HARC/g, '하크'],
        [/BARC/g, '바크'],
        [/GAA/g, '지에이에이'],
        [/MIM/g, '엠아이엠'],
        [/ZAZ/g, '지에이지'],
        [/TSV/g, '티에스브이'],
        [/HBM/g, '에이치비엠'],
        [/CTF/g, '씨티에프'],
        [/BLSA/g, '비엘에스에이'],
        [/PUC/g, '피유씨'],
        [/COP/g, '씨오피'],
        [/CXL/g, '씨엑스엘'],
        [/PIM/g, '피아이엠'],
        [/PNM/g, '피엔엠'],
        [/ISPP/g, '아이에스피피'],
        [/LDPC/g, '엘디피씨'],
        [/ECC/g, '이씨씨'],
        [/GIDL/g, '지아이디엘'],
        [/TRR/g, '티알알'],
        [/BCAT/g, '비캣'],
        [/VCT/g, '브이씨티'],
        [/EM/g, '이엠'],
        [/RIE/g, '알아이이'],
        [/ECD/g, '이씨디'],
        [/CMP/g, '씨엠피'],
        [/PEB/g, '피이비'],
        [/PAG/g, '피에이지'],
        [/CAR/g, '씨에이알'],
        [/MOR/g, '엠오알'],
        [/LER/g, '엘이알'],
        [/LWR/g, '엘더블유알'],
        [/NTD/g, '엔티디'],
        [/OAI/g, '오에이아이'],
        [/PSM/g, '피에스엠'],
        [/RET/g, '알이티'],
        [/UHV/g, '초고진공'],
        [/CNT/g, '탄소나노튜브'],
        [/CTE/g, '열팽창계수'],
        [/PECVD/g, '피이씨브이디'],
        [/LPP/g, '엘피피'],
        [/DoF|DOF/g, '초점심도'],
        [/EL/g, '노광 관용도'],
        [/NA/g, '엔에이'],
        [/CD/g, '씨디'],
        [/EOT/g, '이오티'],
        [/tRET/g, '티알이티'],
        [/SRH/g, '에스알에이치'],
        [/MAC/g, '맥'],
        [/ALU/g, '에이엘유'],
        [/TCO/g, '티씨오'],
        [/PCIe/g, '피씨아이이'],
        [/LLM/g, '엘엘엠'],
        [/NPU/g, '엔피유'],
        [/GPU/g, '지피유'],
        [/CPU/g, '씨피유'],
        [/DRAM/g, '디램'],
        [/NAND/g, '낸드'],
        [/ALD/g, '에이엘디'],
        [/CVD/g, '씨브이디'],
        [/PVD/g, '피브이디'],
        [/EUV/g, '이유브이'],
        [/ICP/g, '아이씨피'],
        [/PR/g, '피알'],
        [/RF/g, '알에프'],
        [/HF/g, '고주파'],
        [/LF/g, '저주파'],
        [/TLC/g, '티엘씨'],
        [/QLC/g, '큐엘씨'],
        [/MLC/g, '엠엘씨'],
        [/SLC/g, '에스엘씨'],
        [/SOH/g, '에스오에이치'],
        [/ACL/g, '에이씨엘'],
        [/STI/g, '에스티아이'],
        [/ILD/g, '아이엘디'],
        [/IMD/g, '아이엠디'],
        [/SOP/g, '에스오피'],
        [/fF/g, '펨토패럿'],
        [/nm/g, '나노미터'],
        [/µm|μm/g, '마이크로미터'],
        [/MV\\/cm/g, '메가볼트 퍼 센티미터'],
        [/eV/g, '일렉트론볼트'],
        [/℃/g, '도'],
        [/≈/g, '약 '],
        [/~/g, '에서 '],
        [/%/g, '퍼센트']
      ];

      for (const [reg, rep] of phonetics) {
        text = text.replace(reg, rep);
      }

      // 4. 불필요한 기호 정리
      text = text.replace(/[*#_\\$`]/g, ' ');
      text = text.replace(/\\s+/g, ' ').trim();
      return text;
    }

    // 심화해설 음성(TTS) 토글 재생
    function toggleLectureVoice(topicId, mode = 'learn') {
      // 1. 이미 재생 중인 경우
      if (currentLectureUtterance && playingLectureTopicId === topicId) {
        stopLectureVoice();
        showToast('⏹️ 심화해설 음성 재생을 중단했습니다.');
        return;
      }

      // 다른 음성(질문 음성 등)이 돌고 있으면 모두 중지
      if (typeof stopSpeakingQuestion === 'function') {
        stopSpeakingQuestion();
      }
      stopLectureVoice();

      const topic = currentTopics.find(t => t.id === topicId);
      if (!topic) return;

      const rawScript = topic.speech_1m30s || topic.speech_alt || '';
      if (!rawScript) {
        showToast('해당 문항의 심화해설 내용이 없습니다.');
        return;
      }

      const cleanText = cleanTextForAnnouncerTTS(rawScript);
      if (!cleanText) return;

      if (!('speechSynthesis' in window)) {
        showToast('현재 브라우저는 음성 합성(TTS) 기능을 지원하지 않습니다.');
        return;
      }

      const utterance = new SpeechSynthesisUtterance(cleanText);
      utterance.lang = 'ko-KR';
      utterance.rate = 1.05; // 전문 아나운서 호흡 속도
      utterance.pitch = 1.0;

      // 한국어 음성 탐색
      const voices = window.speechSynthesis.getVoices();
      const koVoice = voices.find(v => v.lang === 'ko-KR' || v.lang === 'ko_KR' || (v.lang && v.lang.startsWith('ko')));
      if (koVoice) {
        utterance.voice = koVoice;
      }

      currentLectureUtterance = utterance;
      playingLectureTopicId = topicId;
      playingLectureMode = mode;

      // UI 상태 반영 (재생 중 버튼 전환)
      updateLectureVoiceButtonUi(topicId, mode, true);
      showToast('🔊 아나운서 심화해설 음성을 재생합니다.');

      utterance.onend = () => {
        stopLectureVoice();
      };
      utterance.onerror = (e) => {
        console.warn('SpeechSynthesis lecture error:', e);
        stopLectureVoice();
      };

      try {
        window.speechSynthesis.speak(utterance);
      } catch (err) {
        console.warn('SpeechSynthesis speak failed:', err);
        stopLectureVoice();
      }
    }

    function stopLectureVoice() {
      if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
      }
      if (playingLectureTopicId) {
        updateLectureVoiceButtonUi(playingLectureTopicId, playingLectureMode, false);
      }
      currentLectureUtterance = null;
      playingLectureTopicId = null;
      playingLectureMode = null;
    }

    function updateLectureVoiceButtonUi(topicId, mode, isPlaying) {
      const btnLearn = document.getElementById(`btn-play-lecture-${topicId}`);
      const txtLearn = document.getElementById(`txt-play-lecture-${topicId}`);
      const btnInt = document.getElementById(`btn-int-play-lecture-${topicId}`);
      const txtInt = document.getElementById(`txt-int-play-lecture-${topicId}`);

      if (btnLearn && txtLearn) {
        if (isPlaying) {
          btnLearn.classList.add('playing');
          txtLearn.textContent = '⏹️ 해설 중지';
        } else {
          btnLearn.classList.remove('playing');
          txtLearn.textContent = '🔊 심화해설 듣기';
        }
      }

      if (btnInt && txtInt) {
        if (isPlaying) {
          btnInt.classList.add('playing');
          txtInt.textContent = '⏹️ 해설 중지';
        } else {
          btnInt.classList.remove('playing');
          txtInt.textContent = '🔊 심화해설 듣기';
        }
      }
    }
"""

if "function toggleLectureVoice" not in html:
    # Append before the last </script>
    idx_last_script = html.rfind("</script>")
    if idx_last_script != -1:
        html = html[:idx_last_script] + "\n" + lecture_js + "\n" + html[idx_last_script:]
        print("Injected lecture TTS JavaScript engine.")

# ==============================================================================
# 5. build-time 메타태그 갱신
# ==============================================================================
html = re.sub(
    r'<meta name="build-time" content="[^"]+">',
    '<meta name="build-time" content="2026-10-25T11:00:00+09:00">',
    html
)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Successfully updated {html_path}! Total length: {len(html)} bytes.")
