@echo off
REM Batch script to build standalone executable using PyInstaller
REM Make sure PyInstaller is installed: pip install pyinstaller

echo Building standalone executable...
echo.

REM Check if PyInstaller is installed
python -c "import PyInstaller" 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: PyInstaller not found
    echo Installing PyInstaller...
    pip install pyinstaller
)

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Build the executable
echo.
echo Building executable...
pyinstaller --name=EbookScreenshotTool --onefile --console ^
    --add-data="ebook_screenshot.py;." ^
    --add-data="get_coordinates.py;." ^
    --hidden-import=pyautogui ^
    --hidden-import=PIL ^
    --hidden-import=json ^
    --collect-all=pyautogui ^
    --collect-all=PIL ^
    launcher.py

if %ERRORLEVEL% EQU 0 (
    echo.
    echo SUCCESS: Executable created in dist folder
    echo Run: dist\EbookScreenshotTool.exe
) else (
    echo.
    echo ERROR: Build failed
)

pause

