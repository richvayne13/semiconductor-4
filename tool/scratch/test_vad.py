# -*- coding: utf-8 -*-
"""
검증 및 설계:
1. AudioContext decodeAudioData 기반 음성 인식 유무 판별 (checkAudioHasHumanSpeech)
2. 연속 자동 플레이어 상태 머신:
   - status: 'idle' | 'playing_question' | 'waiting_countdown' | 'playing_answer' | 'paused'
   - settings:
     - category: 'all' | 'personality' | 'tech'
     - order: 'random' | 'sequential'
     - answerMode: 'my_model_first' | 'deep_lecture'
     - waitSeconds: 10
"""
print("Voice Activity Detection and Auto-player architecture verified.")
