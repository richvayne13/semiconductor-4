@echo off
cd /d "%~dp0"

echo =====================================================
echo  SK hynix AISK Encyclopedia GitHub Push Start
echo =====================================================

git config http.schannelCheckRevoke false
git config http.sslVerify false

git add index.html
git commit -m "Auto update via git_push.bat"
git push origin main

if errorlevel 1 goto FAILED
goto SUCCESS

:SUCCESS
echo.
echo =====================================================
echo  Push Success!
echo  Site URL: https://richvayne13.github.io/semiconductor-4/#t_02
echo =====================================================
goto END

:FAILED
echo.
echo =====================================================
echo  Push Failed! Check the error message above.
echo =====================================================
goto END

:END
pause
