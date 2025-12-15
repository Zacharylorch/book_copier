"""
Launcher script that runs get_coordinates.py first, then ebook_screenshot.py
"""

import subprocess
import sys
import os

def main():
    """Run coordinate setup, then screenshot tool."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("=" * 60)
    print("Ebook Screenshot Tool Launcher")
    print("=" * 60)
    print("\nThis will run the coordinate setup first, then the screenshot tool.")
    print()
    
    # Step 1: Run get_coordinates.py
    print("Step 1: Setting up screenshot coordinates...")
    print("-" * 60)
    try:
        coord_script = os.path.join(script_dir, "get_coordinates.py")
        result = subprocess.run([sys.executable, coord_script], check=False)
        
        if result.returncode != 0:
            print("\n✗ Coordinate setup failed or was cancelled.")
            input("Press Enter to exit...")
            return 1
            
    except Exception as e:
        print(f"\n✗ Error running coordinate setup: {str(e)}")
        input("Press Enter to exit...")
        return 1
    
    # Step 2: Run ebook_screenshot.py
    print("\n" + "=" * 60)
    print("Step 2: Running screenshot tool...")
    print("-" * 60)
    try:
        screenshot_script = os.path.join(script_dir, "ebook_screenshot.py")
        result = subprocess.run([sys.executable, screenshot_script], check=False)
        
        if result.returncode != 0:
            print("\n✗ Screenshot process failed or was cancelled.")
            input("Press Enter to exit...")
            return 1
            
    except Exception as e:
        print(f"\n✗ Error running screenshot tool: {str(e)}")
        input("Press Enter to exit...")
        return 1
    
    print("\n" + "=" * 60)
    print("Process completed!")
    print("=" * 60)
    input("\nPress Enter to exit...")
    return 0

if __name__ == "__main__":
    sys.exit(main())

