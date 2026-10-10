@echo off
setlocal
cd /d "%~dp0"

echo ===== Step 1 of 3: find Python =====
set PYCMD=
py --version >nul 2>&1 && set PYCMD=py
if "%PYCMD%"=="" python --version >nul 2>&1 && set PYCMD=python
if "%PYCMD%"=="" goto nopython

echo ===== Step 2 of 3: build DetoxLock.exe with the icon =====
%PYCMD% -m pip install pyinstaller
if errorlevel 1 goto fail
%PYCMD% -m PyInstaller --onefile --noconsole --icon icon.ico --name DetoxLock detox_lock.py
if errorlevel 1 goto fail

echo ===== Step 3 of 3: build the installer =====
set "ISCC="
if exist "%ProgramFiles(x86)%\Inno Setup 6\ISCC.exe" set "ISCC=%ProgramFiles(x86)%\Inno Setup 6\ISCC.exe"
if exist "%ProgramFiles%\Inno Setup 6\ISCC.exe" set "ISCC=%ProgramFiles%\Inno Setup 6\ISCC.exe"
if exist "%LOCALAPPDATA%\Programs\Inno Setup 6\ISCC.exe" set "ISCC=%LOCALAPPDATA%\Programs\Inno Setup 6\ISCC.exe"
if not defined ISCC goto noinno

"%ISCC%" installer.iss
if errorlevel 1 goto fail

echo.
echo SUCCESS! Your installer is here: installer_output\DetoxLock_Setup.exe
echo Give people only that one file.
goto end

:nopython
echo.
echo ERROR: Python is not installed or not in PATH.
echo Install it from https://www.python.org/downloads/ (tick "Add python.exe to PATH"),
echo restart your PC, then run this file again.
goto end

:noinno
echo.
echo DetoxLock.exe was built (dist\DetoxLock.exe), but Inno Setup is missing.
echo 1. Install the free Inno Setup from https://jrsoftware.org/isdl.php
echo 2. Run this file again.
goto end

:fail
echo.
echo Something went wrong. Take a screenshot of this window and send it to me.

:end
echo.
pause
