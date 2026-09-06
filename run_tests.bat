@echo off
setlocal
cd /d "%~dp0"
echo ===================================================
echo   Running AvitoParser Test Suite (PRs #327, #328, #329)
echo ===================================================
call .venv\Scripts\activate.bat
pytest -v
echo.
pause
endlocal
