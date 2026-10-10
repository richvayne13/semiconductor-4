@echo off
chcp 65001 > nul
echo ========================================================
echo [SK하이닉스 AISK 대비 대시보드 빌드 및 GitHub 원클릭 배포]
echo ========================================================

cd /d "%~dp0"
python build_aisk_dashboard.py
if %ERRORLEVEL% NEQ 0 (
    echo [오류] 빌드 실패!
    pause
    exit /b %ERRORLEVEL%
)

cd /d "%~dp0..\.."
git add .
git commit -m "update: AISK 마스터 대시보드 갱신 및 온라인 배포"
git push origin main

echo.
echo [배포 완료] 온라인 라이브 URL: https://richvayne13.github.io/semiconductor-4/
echo.
pause
