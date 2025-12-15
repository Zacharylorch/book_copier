#!/bin/bash
# Script to build Windows installer on Mac using Wine and Inno Setup

set -e

echo "Building Windows Installer on Mac..."
echo "===================================="
echo ""

# Check if Wine is installed
if ! command -v wine &> /dev/null; then
    echo "ERROR: Wine is not installed."
    echo ""
    echo "Install Wine using Homebrew:"
    echo "  brew install --cask wine-stable"
    echo ""
    echo "Or install Wine using:"
    echo "  brew install wine"
    echo ""
    exit 1
fi

# Check if Inno Setup is available
INNO_SETUP_PATH="$HOME/.wine/drive_c/Program Files (x86)/Inno Setup 6/ISCC.exe"

if [ ! -f "$INNO_SETUP_PATH" ]; then
    echo "ERROR: Inno Setup not found at: $INNO_SETUP_PATH"
    echo ""
    echo "Please install Inno Setup:"
    echo "1. Download Inno Setup from: https://jrsoftware.org/isinfo.php"
    echo "2. Install it using Wine:"
    echo "   wine innosetup-6.x.x.exe"
    echo ""
    echo "Or use the portable version and extract it to:"
    echo "  ~/.wine/drive_c/Program Files (x86)/Inno Setup 6/"
    echo ""
    exit 1
fi

# Create output directory
mkdir -p installer_output

# Build the installer using Wine
echo "Compiling installer with Inno Setup..."
echo ""

wine "$INNO_SETUP_PATH" installer.iss

if [ $? -eq 0 ]; then
    echo ""
    echo "SUCCESS: Installer created in installer_output folder"
    echo "File: installer_output/EbookScreenshotTool_Setup.exe"
else
    echo ""
    echo "ERROR: Installer build failed"
    exit 1
fi

