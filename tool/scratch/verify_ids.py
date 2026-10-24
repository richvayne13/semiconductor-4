import re

with open(r'C:\Work\반도체4_AISK대비\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

ids = [
    'intHistoryList', 'modelAnswerText', 'modelBodyContent', 'modelToggleIcon',
    'intHintBox', 'btnModeLearnMain', 'btnModeInterviewMain',
    'intTranscriptLen', 'btnRecordText', 'interviewProcChips', 'mobModeBtn',
    'recStatusNotice', 'intLenGuideNotice', 'btnModeInterviewSide',
    'btnModeLearnSide', 'intCatTech', 'intCatPersonality', 'intCatAll',
    'interviewProgressText', 'intQBadge', 'intKeywordsList', 'btnRecordToggle',
    'intTranscriptArea', 'recTimerDisplay', 'intQTitle', 'historyCountBadge',
    'recDot', 'intQCategory'
]

missing = []
for i in ids:
    if f'id="{i}"' not in html and f"id='{i}'" not in html:
        missing.append(i)

if missing:
    print("MISSING:", missing)
else:
    print("All IDs verified successfully!")
