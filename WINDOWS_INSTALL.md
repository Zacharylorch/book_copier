# Installing and Running on Windows

This guide will help you install and run the Ebook Screenshot Tool on a Windows device.

## Method 1: Using the Pre-built Installer (Recommended)

### Step 1: Download the Installer

1. Go to your GitHub repository
2. Click on the **Actions** tab
3. Find the latest "Build Windows Installer" workflow run (should have a green checkmark)
4. Click on the workflow run
5. Scroll down to **Artifacts** section
6. Click **EbookScreenshotTool_Setup** to download the installer

Alternatively, if you created a Release:
1. Go to the **Releases** section of your GitHub repository
2. Download `EbookScreenshotTool_Setup.exe` from the latest release

### Step 2: Install

1. Run the downloaded `EbookScreenshotTool_Setup.exe`
2. Follow the installation wizard
3. The installer will:
   - Install the application files
   - Check for Python (must be installed separately if not found)
   - Install Python dependencies automatically
   - Create Start Menu and desktop shortcuts

### Step 3: Run

1. **Option A**: Double-click the desktop shortcut "Ebook Screenshot Tool"
2. **Option B**: Open Start Menu → Search "Ebook Screenshot Tool" → Click it
3. **Option C**: Navigate to installation folder and run `launcher.py` or `run.bat`

The tool will:
1. First run the coordinate setup
2. Then run the screenshot capture tool

## Method 2: From Source Code

### Prerequisites

1. **Install Python 3.8 or higher**
   - Download from: https://www.python.org/downloads/
   - During installation, check "Add Python to PATH"

2. **Verify Python installation**
   ```cmd
   python --version
   ```

### Step 1: Clone the Repository

```cmd
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

Or download as ZIP from GitHub and extract it.

### Step 2: Install Dependencies

```cmd
pip install -r requirements.txt
```

### Step 3: Run

**Option A: Use the launcher (recommended)**
```cmd
python launcher.py
```

**Option B: Run directly**
```cmd
python get_coordinates.py
python ebook_screenshot.py
```

**Option C: Use the batch file**
```cmd
run.bat
```

## First Time Setup

### 1. Set Screenshot Coordinates

When you first run the tool, it will ask you to:
1. Move your mouse to the **top-left corner** of the ebook page area
2. Press Enter
3. Move your mouse to the **bottom-right corner** of the ebook page area
4. Press Enter
5. Coordinates are saved automatically

### 2. Capture Screenshots

1. Open your ebook reader application
2. Navigate to page 1
3. Run the tool
4. Enter:
   - Number of pages to capture
   - Key to press for next page (e.g., 'right', 'space', 'pagedown')
5. Wait for the 5-second countdown
6. The tool will automatically capture all pages

## Troubleshooting

### Python Not Found

If you get "Python not found" error:
1. Install Python from https://www.python.org/downloads/
2. Make sure to check "Add Python to PATH" during installation
3. Restart your command prompt/terminal

### Dependencies Not Installing

Try:
```cmd
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Screenshots Are Blank

1. Make sure your ebook reader window is visible (not minimized)
2. Re-run the coordinate setup to ensure correct coordinates
3. Check that the coordinates are within your screen bounds

### Key Not Working

Try different key names:
- `right` - Right arrow
- `left` - Left arrow
- `space` - Spacebar
- `pagedown` - Page Down
- `down` - Down arrow
- `n` - N key

### Permission Errors

Run Command Prompt or PowerShell as Administrator if you encounter permission errors.

## Uninstalling

### If Installed via Installer

1. Go to Settings → Apps → Apps & features
2. Search for "Ebook Screenshot Tool"
3. Click Uninstall

### If Installed from Source

Simply delete the folder where you cloned/extracted the code.

## Output

The PDF file will be created in the same directory as the script:
- Filename format: `ebook_screenshots_YYYYMMDD_HHMMSS.pdf`
- Example: `ebook_screenshots_20240115_143022.pdf`

