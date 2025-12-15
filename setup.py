"""
PyInstaller setup script for creating a standalone Windows executable.
Alternative to Inno Setup installer.
"""

from setuptools import setup
import PyInstaller.__main__

# This script can be used with PyInstaller to create a standalone executable
# Run: pyinstaller setup.py

if __name__ == "__main__":
    PyInstaller.__main__.run([
        'launcher.py',
        '--name=EbookScreenshotTool',
        '--onefile',
        '--windowed',
        '--add-data=ebook_screenshot.py;.',
        '--add-data=get_coordinates.py;.',
        '--hidden-import=pyautogui',
        '--hidden-import=PIL',
        '--hidden-import=json',
        '--collect-all=pyautogui',
        '--collect-all=PIL',
    ])

