# Ebook PDF Screenshot Tool

A Python script that automates taking screenshots of ebook pages and combines them into a single PDF file.

## Features

- Automatically captures screenshots of each page in an ebook reader
- Configurable screenshot region (top-left and bottom-right coordinates)
- Supports any keyboard key for page navigation
- Combines all screenshots into a single PDF file
- User-friendly command-line interface
- Windows installer available

## Requirements

- Windows OS
- Python 3.8 or higher
- An ebook reader application (Adobe Digital Editions, Calibre, etc.)

## Installation Options

### Option 1: Windows Installer (Recommended)

1. **Build the installer:**
   - Install [Inno Setup](https://jrsoftware.org/isinfo.php)
   - Run `build_installer.bat` to create the installer
   - The installer will be created in the `installer_output` folder

2. **Install:**
   - Run `EbookScreenshotTool_Setup.exe`
   - Follow the installation wizard
   - The installer will automatically install Python dependencies

3. **Run:**
   - Launch "Ebook Screenshot Tool" from the Start Menu or desktop shortcut
   - The launcher will first run the coordinate setup, then the screenshot tool

### Option 2: Standalone Executable

1. **Build the executable:**
   ```bash
   build_exe.bat
   ```
   - This creates a standalone `.exe` file in the `dist` folder
   - No Python installation required for end users

2. **Run:**
   - Double-click `dist\EbookScreenshotTool.exe`

### Option 3: Python Script (Development)

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the launcher:
```bash
python launcher.py
```

## Usage Workflow

The tool uses a two-step process:

### Step 1: Coordinate Setup
1. Run the launcher (or `get_coordinates.py` directly)
2. Move your mouse to the **top-left corner** of the ebook page area
3. Press Enter to capture the coordinate
4. Move your mouse to the **bottom-right corner** of the ebook page area
5. Press Enter to capture the coordinate
6. Coordinates are saved automatically

### Step 2: Screenshot Capture
1. Open your ebook reader application and navigate to page 1
2. The tool will prompt you for:
   - **Number of pages**: Enter how many pages you want to capture
   - **Navigation key**: The key to press to move to the next page (e.g., 'right', 'space', 'pagedown')
3. A **5-second countdown** will start
4. The script will:
   - Capture each page as a screenshot
   - Automatically navigate to the next page
   - Combine all screenshots into a PDF file

## Finding Screenshot Coordinates

The coordinate helper tool (`get_coordinates.py`) makes it easy to find coordinates:
- Simply move your mouse to the corners and press Enter
- Coordinates are automatically saved for use by the screenshot tool

Alternatively, you can:
1. Use Windows Snipping Tool or any screenshot tool to identify the region
2. Use Python to get mouse coordinates:
   ```python
   import pyautogui
   print(pyautogui.position())  # Move mouse and run this to get coordinates
   ```
3. Or use a tool like [Mouse Position](https://www.microsoft.com/en-us/p/mouse-position/9nblggh4z3sp) from Microsoft Store

## Common Navigation Keys

- `right` - Right arrow key
- `left` - Left arrow key  
- `space` - Spacebar
- `pagedown` - Page Down key
- `pageup` - Page Up key
- `down` - Down arrow key
- `n` - N key (for "next")
- `enter` - Enter key

## Output

The script creates a PDF file named `ebook_screenshots_YYYYMMDD_HHMMSS.pdf` in the same directory as the script.

## Notes

- Make sure your ebook reader window is visible and not minimized
- The script disables PyAutoGUI's failsafe feature for automation
- You can interrupt the process with Ctrl+C
- Ensure sufficient disk space for screenshots
- The delay between page turns (default 1.0 seconds) helps ensure pages load properly
- Coordinates are saved in `screenshot_coordinates.json` and can be reused
- You can run `get_coordinates.py` again anytime to update the coordinates

## Troubleshooting

- **Screenshots are blank**: Check that your coordinates are correct and the ebook reader window is visible. Re-run the coordinate setup.
- **Wrong pages captured**: The delay is fixed at 1.0 seconds. If pages aren't loading fast enough, you may need to modify the script.
- **Key not working**: Try different key names (check PyAutoGUI documentation for supported keys)
- **PDF creation fails**: Ensure Pillow is properly installed and you have write permissions
- **Coordinates not found**: Make sure you run `get_coordinates.py` first, or run the launcher which handles this automatically
- **Python not found (installer)**: The installer checks for Python 3.8+. Install Python from [python.org](https://www.python.org/downloads/) if needed

## Building the Installer

### On Windows

#### Using Inno Setup (Recommended)
1. Download and install [Inno Setup](https://jrsoftware.org/isinfo.php)
2. Run `build_installer.bat`
3. The installer will be in `installer_output\EbookScreenshotTool_Setup.exe`

#### Using PyInstaller (Standalone EXE)
1. Run `build_exe.bat`
2. The executable will be in `dist\EbookScreenshotTool.exe`
3. This creates a single file that includes Python and all dependencies

### On Mac

#### Option 1: Using Wine (Local Development)
1. Install Wine: `brew install --cask wine-stable`
2. Download and install Inno Setup using Wine
3. Run `./build_installer_mac.sh`
4. See `INSTALLER_BUILD.md` for detailed instructions

#### Option 2: Using GitHub Actions (Recommended)
1. Push your code to GitHub
2. The workflow will automatically build the installer on Windows
3. Download the installer from the Actions artifacts
4. See `.github/workflows/build-installer.yml` for the workflow

For more details, see `INSTALLER_BUILD.md`

