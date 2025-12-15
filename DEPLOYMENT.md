# Deployment Guide: GitHub to Windows

This guide will walk you through pushing to GitHub and installing on Windows.

## Step 1: Push to GitHub

### On Mac (where you are now):

```bash
# Check what files will be committed
git status

# Add all files
git add -A

# Commit the changes
git commit -m "Add ebook screenshot tool with Windows installer support"

# Push to GitHub
git push origin master
```

If your default branch is `main` instead of `master`:
```bash
git push origin main
```

## Step 2: Build Installer on GitHub

After pushing, the GitHub Actions workflow will automatically run. To manually trigger it:

1. Go to your GitHub repository
2. Click on the **Actions** tab
3. Select **Build Windows Installer** workflow
4. Click **Run workflow** button
5. Wait for the build to complete (usually 2-3 minutes)

## Step 3: Download the Installer

Once the workflow completes:

1. In the **Actions** tab, click on the completed workflow run
2. Scroll down to **Artifacts**
3. Click on **EbookScreenshotTool_Setup** to download the installer
4. Save the `.exe` file to your Windows computer

## Step 4: Install on Windows

1. **Transfer the installer** to your Windows device (via USB, email, cloud storage, etc.)

2. **Run the installer:**
   - Double-click `EbookScreenshotTool_Setup.exe`
   - If Windows shows a security warning, click "More info" → "Run anyway"
   - Follow the installation wizard

3. **The installer will:**
   - Install the application files
   - Automatically install Python dependencies (if Python is installed)
   - Create Start Menu shortcuts
   - Optionally create desktop shortcuts

4. **First time setup:**
   - The installer checks for Python 3.8+
   - If Python is not found, you'll need to install it from [python.org](https://www.python.org/downloads/)
   - After Python installation, re-run the installer or install dependencies manually:
     ```cmd
     pip install -r requirements.txt
     ```

## Step 5: Run the Application

1. **Launch the tool:**
   - From Start Menu: Search for "Ebook Screenshot Tool"
   - Or double-click the desktop shortcut (if created)
   - Or run `run.bat` from the installation directory

2. **First run workflow:**
   - The coordinate helper will run first
   - Move your mouse to the top-left corner of the ebook page area, press Enter
   - Move your mouse to the bottom-right corner, press Enter
   - Coordinates are saved automatically

3. **Screenshot process:**
   - Enter the number of pages to capture
   - Enter the navigation key (e.g., 'right', 'space', 'pagedown')
   - A 5-second countdown will start
   - The tool will automatically capture all pages and create a PDF

## Troubleshooting

### Installer won't run on Windows
- Right-click → Properties → Check "Unblock" if present
- Temporarily disable antivirus if it blocks the download

### Python not found during installation
- Install Python 3.8+ from [python.org](https://www.python.org/downloads/)
- Make sure to check "Add Python to PATH" during installation
- Re-run the installer after Python installation

### Dependencies not installed
If the installer doesn't install dependencies automatically:
```cmd
cd "C:\Program Files\EbookScreenshotTool"
pip install -r requirements.txt
```

### Application won't start
- Check if Python is installed: `python --version`
- Check if dependencies are installed: `pip list`
- Run from command prompt to see error messages:
  ```cmd
  python launcher.py
  ```

## Quick Reference Commands

### On Mac (before pushing):
```bash
git add -A
git commit -m "Your commit message"
git push origin master  # or 'main'
```

### On Windows (after downloading installer):
1. Run `EbookScreenshotTool_Setup.exe`
2. Install Python if needed
3. Launch from Start Menu

### Manual installation on Windows (if installer doesn't work):
```cmd
# Clone the repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO

# Install dependencies
pip install -r requirements.txt

# Run the tool
python launcher.py
```

