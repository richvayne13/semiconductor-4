@echo off
chcp 65001 > nul
echo ===================================================
echo [SK하이닉스 AISK 대비 대시보드 빌드 스크립트 v1.0]
echo ===================================================

cd /d "%~dp0"
python build_aisk_dashboard.py

if %ERRORLEVEL% EQU 0 (
    echo [성공] 대시보드 빌드 및 루트 동기화가 성공적으로 완료되었습니다.
) else (
    echo [오류] 빌드 중 에러가 발생했습니다. 코드와 데이터를 점검하십시오.
)

pause
