import cv2
import numpy as np
import pyautogui
import pytesseract
import time
import win32api
import win32con

# Configure tesseract path (Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def find_skill_tree_button():
    """
    Find the 'skill tree' button on screen using OCR.
    Returns (x, y) coordinates if found, None otherwise.
    """
    # Capture full screen
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    
    # Convert to grayscale
    gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)
    
    screen_w, screen_h = pyautogui.size()
    
    # Search in right side of screen (where UI buttons are)
    search_x = int(screen_w * 0.7)  # Right 30% of screen
    search_y = 0
    search_width = int(screen_w * 0.3)
    search_height = int(screen_h * 0.15)  # Top 15% of screen
    
    roi = gray[search_y:search_y+search_height, search_x:search_x+search_width]
    roi_color = screenshot_np[search_y:search_y+search_height, search_x:search_x+search_width]
    
    # Apply threshold to isolate white text on dark background
    _, thresh = cv2.threshold(roi, 180, 255, cv2.THRESH_BINARY)
    
    # Save debug images
    cv2.imwrite('skill_tree_search.png', thresh)
    cv2.imwrite('skill_tree_color.png', cv2.cvtColor(roi_color, cv2.COLOR_RGB2BGR))
    print("[UI] Debug images saved to skill_tree_search.png and skill_tree_color.png")
    
    # Use tesseract to detect text and get bounding boxes
    data = pytesseract.image_to_data(thresh, output_type=pytesseract.Output.DICT)
    
    # Look for "skill" and "tree" text - they should be close to each other
    skill_pos = None
    tree_pos = None
    
    for i in range(len(data['text'])):
        text = data['text'][i].lower().strip()
        conf = int(data['conf'][i]) if data['conf'][i] != '-1' else 0
        
        if conf > 20:  # Lowered confidence threshold
            x = data['left'][i]
            y = data['top'][i]
            w = data['width'][i]
            h = data['height'][i]
            
            if 'skill' in text:
                skill_pos = (x, y, w, h)
                print(f"[UI] Found 'skill' at x={x}, y={y}, w={w}, h={h}, conf={conf}")
            elif 'tree' in text:
                tree_pos = (x, y, w, h)
                print(f"[UI] Found 'tree' at x={x}, y={y}, w={w}, h={h}, conf={conf}")
    
    # If we found both words, calculate center of the button area
    if skill_pos and tree_pos:
        # Get bounding box that encompasses both words
        min_x = min(skill_pos[0], tree_pos[0])
        min_y = min(skill_pos[1], tree_pos[1])
        max_x = max(skill_pos[0] + skill_pos[2], tree_pos[0] + tree_pos[2])
        max_y = max(skill_pos[1] + skill_pos[3], tree_pos[1] + tree_pos[3])
        
        # Calculate center of the button (add padding to account for button border)
        center_x = (min_x + max_x) // 2
        center_y = (min_y + max_y) // 2 + 15  # Offset down to click button center
        
        # Convert back to screen coordinates
        abs_x = search_x + center_x
        abs_y = search_y + center_y
        
        print(f"[UI] Calculated button center at ({abs_x}, {abs_y})")
        return (abs_x, abs_y)
    
    # If only "skill" found, assume button is centered around the text
    elif skill_pos:
        # Click at the horizontal center of "skill" text, but lower vertically
        center_x = skill_pos[0] + skill_pos[2] // 2
        center_y = skill_pos[1] + skill_pos[3] // 2 + 20  # 20px below text center
        
        abs_x = search_x + center_x
        abs_y = search_y + center_y
        
        print(f"[UI] Using 'skill' position, adjusted to ({abs_x}, {abs_y})")
        return (abs_x, abs_y)
    
    print("[UI] 'skill tree' button not found")
    print("[UI] Detected text in search area:")
    for i in range(len(data['text'])):
        text = data['text'][i].strip()
        conf = int(data['conf'][i]) if data['conf'][i] != '-1' else 0
        if text and conf > 20:
            print(f"  - '{text}' (confidence: {conf}%)")
    
    return None


def win32_click(x, y):
    """
    Perform a mouse click using Windows API (more reliable than pyautogui for some games)
    """
    # Move cursor
    win32api.SetCursorPos((x, y))
    time.sleep(0.1)
    
    # Mouse down
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(0.05)
    
    # Mouse up
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(0.1)


def click_skill_tree():
    """
    Find and click the skill tree button.
    Returns True if successful, False otherwise.
    """
    
    pos = find_skill_tree_button()
    
    if pos:
        x, y = pos
        print(f"[UI] Moving mouse to ({x}, {y})...")
        
        # Move mouse to position
        pyautogui.moveTo(x, y, duration=0.5)
        
        # Verify we reached the position
        current_x, current_y = pyautogui.position()
        print(f"[UI] Mouse now at ({current_x}, {current_y})")
        
        time.sleep(0.3)
        
        print(f"[UI] Performing Windows API click...")
        # Use Windows API click instead of pyautogui
        win32_click(x, y)
        
        time.sleep(0.5)
        
        print(f"[UI] Click completed")
        return True
    
    return False