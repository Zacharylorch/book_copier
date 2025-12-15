"""
Ebook PDF Screenshot Tool for Windows
Takes screenshots of ebook pages and combines them into a PDF.
"""

import pyautogui
import time
from PIL import Image
import sys
from datetime import datetime
import json
import os

# Disable pyautogui failsafe for automation
pyautogui.FAILSAFE = False

COORDINATES_FILE = "screenshot_coordinates.json"

def load_coordinates():
    """Load coordinates from JSON file."""
    if not os.path.exists(COORDINATES_FILE):
        print(f"\n✗ Error: {COORDINATES_FILE} not found!")
        print("Please run get_coordinates.py first to set up screenshot coordinates.")
        return None
    
    try:
        with open(COORDINATES_FILE, 'r') as f:
            coords = json.load(f)
            x1 = coords.get("x1")
            y1 = coords.get("y1")
            x2 = coords.get("x2")
            y2 = coords.get("y2")
            
            if x1 is None or y1 is None or x2 is None or y2 is None:
                print(f"\n✗ Error: Invalid coordinates in {COORDINATES_FILE}")
                return None
            
            return (x1, y1, x2, y2)
    except Exception as e:
        print(f"\n✗ Error reading coordinates: {str(e)}")
        return None

def get_user_input():
    """Get user input for configuration."""
    print("=" * 60)
    print("Ebook PDF Screenshot Tool")
    print("=" * 60)
    
    # Load coordinates from file
    region = load_coordinates()
    if region is None:
        return None, None, None, None
    
    x1, y1, x2, y2 = region
    print(f"\n✓ Loaded screenshot region: ({x1}, {y1}, {x2}, {y2})")
    print(f"  Width: {x2 - x1}, Height: {y2 - y1}")
    
    print("\nPlease prepare your ebook reader application.")
    print("Make sure it's open and ready to start from page 1.")
    
    # Get number of pages
    while True:
        try:
            num_pages = int(input("\nEnter the number of pages to capture: "))
            if num_pages > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Get key to press for next page
    print("\n" + "=" * 60)
    print("Navigation Key Configuration")
    print("=" * 60)
    print("Common keys: 'right', 'space', 'down', 'pagedown', 'n'")
    print("For arrow keys, use: 'right', 'left', 'up', 'down'")
    print("For special keys, use: 'space', 'enter', 'pagedown', 'pageup'")
    next_key = input("Enter the key to press to move to next page: ").strip().lower()
    
    # Delay between actions (default 1.0)
    delay = 1.0
    
    return num_pages, region, next_key, delay

def take_screenshot(region):
    """Take a screenshot of the specified region."""
    x1, y1, x2, y2 = region
    width = x2 - x1
    height = y2 - y1
    
    screenshot = pyautogui.screenshot(region=(x1, y1, width, height))
    return screenshot

def press_key(key):
    """Press the specified key."""
    pyautogui.press(key)

def create_pdf_from_images(images, output_filename):
    """Create a PDF from a list of PIL Images."""
    if not images:
        print("No images to create PDF from!")
        return False
    
    # Convert all images to RGB if needed (PDF requires RGB)
    rgb_images = []
    for img in images:
        if img.mode != 'RGB':
            img = img.convert('RGB')
        rgb_images.append(img)
    
    # Save first image and append others
    if len(rgb_images) == 1:
        rgb_images[0].save(output_filename, 'PDF', resolution=100.0)
    else:
        rgb_images[0].save(
            output_filename,
            'PDF',
            resolution=100.0,
            save_all=True,
            append_images=rgb_images[1:]
        )
    
    return True

def main():
    """Main function to orchestrate the screenshot process."""
    try:
        # Get user configuration
        num_pages, region, next_key, delay = get_user_input()
        
        if num_pages is None or region is None or next_key is None:
            print("\n✗ Configuration incomplete. Exiting.")
            return 1
        
        print("\n" + "=" * 60)
        print("Starting Screenshot Capture")
        print("=" * 60)
        print(f"Pages to capture: {num_pages}")
        print(f"Region: {region}")
        print(f"Next page key: {next_key}")
        print(f"Delay: {delay} seconds")
        print("\n" + "=" * 60)
        print("Starting in 5 seconds...")
        print("Make sure your ebook reader is ready and positioned correctly!")
        print("=" * 60)
        for i in range(5, 0, -1):
            print(f"Starting in {i}...")
            time.sleep(1)
        
        screenshots = []
        
        # Capture screenshots
        for page_num in range(1, num_pages + 1):
            print(f"Capturing page {page_num}/{num_pages}...")
            
            # Take screenshot
            screenshot = take_screenshot(region)
            screenshots.append(screenshot)
            
            # If not the last page, press key to move to next page
            if page_num < num_pages:
                press_key(next_key)
                time.sleep(delay)
        
        print(f"\nCaptured {len(screenshots)} screenshots!")
        
        # Create PDF
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"ebook_screenshots_{timestamp}.pdf"
        
        print(f"\nCreating PDF: {output_filename}")
        if create_pdf_from_images(screenshots, output_filename):
            print(f"✓ Successfully created PDF: {output_filename}")
        else:
            print("✗ Failed to create PDF")
            return 1
        
        return 0
        
    except KeyboardInterrupt:
        print("\n\nProcess interrupted by user.")
        return 1
    except Exception as e:
        print(f"\n\nError occurred: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())

