# Building Windows Installer on Mac

There are several ways to build a Windows installer on Mac. Here are the most practical options:

## Option 1: Using Wine (Recommended for Local Development)

Wine allows you to run Windows applications on Mac.

### Step 1: Install Wine

Using Homebrew:
```bash
brew install --cask wine-stable
```

Or install the development version:
```bash
brew install wine
```

### Step 2: Install Inno Setup

1. Download Inno Setup from: https://jrsoftware.org/isinfo.php
2. Install it using Wine:
```bash
wine innosetup-6.x.x.exe
```

Or download the portable version and extract it to:
```
~/.wine/drive_c/Program Files (x86)/Inno Setup 6/
```

### Step 3: Build the Installer

Run the provided script:
```bash
chmod +x build_installer_mac.sh
./build_installer_mac.sh
```

Or manually:
```bash
wine "$HOME/.wine/drive_c/Program Files (x86)/Inno Setup 6/ISCC.exe" installer.iss
```

The installer will be created in `installer_output/EbookScreenshotTool_Setup.exe`

## Option 2: Using GitHub Actions (Recommended for Releases)

This is the easiest way if you're using GitHub. The installer is built automatically on Windows runners.

### Setup

1. Push your code to GitHub
2. The workflow (`.github/workflows/build-installer.yml`) will automatically:
   - Build the installer on a Windows runner
   - Create an artifact you can download
   - If you create a release tag, it will attach the installer to the release

### Manual Trigger

1. Go to your GitHub repository
2. Click "Actions" tab
3. Select "Build Windows Installer" workflow
4. Click "Run workflow"

### Using Release Tags

Create a release tag to automatically build and attach the installer:
```bash
git tag v1.0.0
git push origin v1.0.0
```

## Option 3: Using Cross-Platform Tools

### NSIS (Nullsoft Scriptable Install System)

NSIS can be installed on Mac and can build Windows installers:

1. Install NSIS:
```bash
brew install nsis
```

2. Create an NSIS script (alternative to Inno Setup)

### Electron Builder

If you want to package as an Electron app, Electron Builder can create Windows installers on Mac.

## Option 4: Virtual Machine

Use a Windows VM (Parallels, VMware, VirtualBox) to run Inno Setup natively. This is the most reliable but requires a Windows license.

## Troubleshooting Wine

### Wine Configuration

If you encounter issues, you may need to configure Wine:
```bash
winecfg
```

### 64-bit vs 32-bit

Inno Setup is 32-bit. Make sure Wine is configured correctly:
```bash
WINEARCH=win32 winecfg
```

### Missing Dependencies

On some systems, you may need:
```bash
brew install winetricks
winetricks vcrun2015  # Visual C++ runtime
```

## Quick Start (Wine Method)

```bash
# 1. Install Wine
brew install --cask wine-stable

# 2. Download and install Inno Setup
# Download from: https://jrsoftware.org/isinfo.php
wine innosetup-6.x.x.exe

# 3. Build installer
chmod +x build_installer_mac.sh
./build_installer_mac.sh
```

## Recommended Approach

- **For development/testing**: Use Wine locally (Option 1)
- **For releases**: Use GitHub Actions (Option 2) - it's free, reliable, and doesn't require Wine setup

