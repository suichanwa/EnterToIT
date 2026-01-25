import cv2
import numpy as np
import pyautogui


def find_skill_tree_button():
    """
    Find the 'skill tree' button on screen.
    Returns (x, y) coordinates if found, None otherwise.
    """
    # Capture full screen
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    
    # Convert to grayscale
    gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)
    
    # The "skill tree" button appears to be in top-right area with white text on dark background
    # Let's search for text-like patterns in the UI area
    screen_w, screen_h = pyautogui.size()
    
    # Search in top-right corner (where the button is in your screenshot)
    search_x = int(screen_w * 0.7)  # Right 30% of screen
    search_y = 0
    search_width = int(screen_w * 0.3)
    search_height = int(screen_h * 0.15)  # Top 15% of screen
    
    roi = gray[search_y:search_y+search_height, search_x:search_x+search_width]
    
    # Apply threshold to find white text on dark background
    _, thresh = cv2.threshold(roi, 200, 255, cv2.THRESH_BINARY)
    
    # Find contours (text areas)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Look for rectangular regions that could be buttons
    for contour in contours:
        area = cv2.contourArea(contour)
        
        # Button should be reasonably sized
        if 500 < area < 5000:
            x, y, w, h = cv2.boundingRect(contour)
            
            # Button should be roughly horizontal rectangle
            if 1.5 < (w / h) < 5:
                # Convert back to screen coordinates
                abs_x = search_x + x + w // 2
                abs_y = search_y + y + h // 2
                
                print(f"[UI] Found potential button at ({abs_x}, {abs_y})")
                return (abs_x, abs_y)
    
    print("[UI] Skill tree button not found")
    return None


def click_skill_tree():
    """
    Find and click the skill tree button.
    Returns True if successful, False otherwise.
    """
    pos = find_skill_tree_button()
    
    if pos:
        x, y = pos
        print(f"[UI] Clicking skill tree button at ({x}, {y})")
        pyautogui.click(x, y)
        return True
    
    return False