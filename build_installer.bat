@echo off
REM Batch script to build the Windows installer using Inno Setup
REM Make sure Inno Setup is installed and in your PATH

echo Building Windows Installer...
echo.

REM Check if Inno Setup compiler is available
where iscc >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Inno Setup Compiler (iscc.exe) not found in PATH
    echo Please install Inno Setup and add it to your PATH, or run:
    echo "C:\Program Files (x86)\Inno Setup 6\ISCC.exe installer.iss"
    pause
    exit /b 1
)

REM Create output directory
if not exist installer_output mkdir installer_output

REM Compile the installer
iscc installer.iss

if %ERRORLEVEL% EQU 0 (
    echo.
    echo SUCCESS: Installer created in installer_output folder
) else (
    echo.
    echo ERROR: Installer build failed
)

pause

