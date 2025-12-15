"""
Helper script to get mouse coordinates for screenshot region setup.
Move your mouse to the corners of the region you want to capture.
"""

import pyautogui
import time
import json
import os

COORDINATES_FILE = "screenshot_coordinates.json"

def save_coordinates(x1, y1, x2, y2):
    """Save coordinates to a JSON file."""
    coords = {
        "x1": x1,
        "y1": y1,
        "x2": x2,
        "y2": y2
    }
    with open(COORDINATES_FILE, 'w') as f:
        json.dump(coords, f)
    print(f"\n✓ Coordinates saved to {COORDINATES_FILE}")

def load_coordinates():
    """Load coordinates from JSON file if it exists."""
    if os.path.exists(COORDINATES_FILE):
        try:
            with open(COORDINATES_FILE, 'r') as f:
                coords = json.load(f)
                return coords.get("x1"), coords.get("y1"), coords.get("x2"), coords.get("y2")
        except:
            return None
    return None

print("=" * 60)
print("Mouse Coordinate Helper")
print("=" * 60)
print("\nThis script will help you find coordinates for screenshot regions.")
print("Move your mouse to the desired positions and press Enter.")
print("Press Ctrl+C to exit.\n")

try:
    # Check if coordinates already exist
    existing = load_coordinates()
    if existing:
        x1, y1, x2, y2 = existing
        print(f"Found existing coordinates: ({x1}, {y1}, {x2}, {y2})")
        use_existing = input("Use existing coordinates? (y/n): ").strip().lower()
        if use_existing == 'y':
            save_coordinates(x1, y1, x2, y2)
            print("\nCoordinates ready for screenshot tool!")
            exit(0)
    
    while True:
        input("Move mouse to TOP-LEFT corner of screenshot region, then press Enter...")
        x1, y1 = pyautogui.position()
        print(f"Top-left coordinates: ({x1}, {y1})")
        
        input("\nMove mouse to BOTTOM-RIGHT corner of screenshot region, then press Enter...")
        x2, y2 = pyautogui.position()
        print(f"Bottom-right coordinates: ({x2}, {y2})")
        
        print(f"\nRegion: ({x1}, {y1}, {x2}, {y2})")
        print(f"Width: {x2 - x1}, Height: {y2 - y1}")
        
        # Validate coordinates
        if x2 > x1 and y2 > y1:
            save_coordinates(x1, y1, x2, y2)
            print("\n✓ Coordinates saved and ready for screenshot tool!")
            break
        else:
            print("\n✗ Invalid coordinates. Bottom-right must be below and to the right of top-left.")
            again = input("Try again? (y/n): ").strip().lower()
            if again != 'y':
                break
        print()
            
except KeyboardInterrupt:
    print("\n\nExiting...")
except Exception as e:
    print(f"\n\nError: {str(e)}")

