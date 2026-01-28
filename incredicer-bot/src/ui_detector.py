import cv2
import numpy as np
import pyautogui
import pytesseract
import time
import win32api
import win32con
from utils.currency import read_dark_matter, read_currency_from_tooltip

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
        win32_click(x, y)
        
        time.sleep(0.5)
        
        print(f"[UI] Click completed")
        return True
    
    return False


def find_clickable_skill_nodes():
    """
    Find skill nodes that have yellow indicators (indicating they can be upgraded).
    Returns list of (x, y) coordinates.
    """
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    
    # Convert to HSV for better color detection
    hsv = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2HSV)
    
    # Define yellow color range (for the indicators on nodes)
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    
    # Create mask for yellow indicators
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    
    # Find contours of yellow indicators
    contours, _ = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    clickable_nodes = []
    
    for contour in contours:
        area = cv2.contourArea(contour)
        
        # Yellow indicators are small
        if 50 < area < 500:
            x, y, w, h = cv2.boundingRect(contour)
            
            # The skill node center is near the yellow indicator
            # Offset to find the actual node center (indicator is usually on bottom-right)
            node_x = x - 15
            node_y = y - 15
            
            clickable_nodes.append((node_x, node_y))
            print(f"[SKILL] Found clickable node at ({node_x}, {node_y})")
    
    # Save debug image
    debug_img = screenshot_np.copy()
    for x, y in clickable_nodes:
        cv2.circle(debug_img, (x, y), 25, (0, 255, 0), 3)
    cv2.imwrite('clickable_skill_nodes.png', cv2.cvtColor(debug_img, cv2.COLOR_RGB2BGR))
    print(f"[SKILL] Found {len(clickable_nodes)} clickable nodes. Debug image saved.")
    
    return clickable_nodes


def click_skill_node(x, y):
    """
    Click on a skill node at the given coordinates.
    """
    print(f"[SKILL] Clicking skill node at ({x}, {y})")
    
    # Move to position
    pyautogui.moveTo(x, y, duration=0.3)
    time.sleep(0.2)
    
    # Click using Windows API
    win32_click(x, y)
    time.sleep(0.5)
    
    print(f"[SKILL] Skill node clicked")


def get_skill_cost(x, y):
    """
    Hover over a skill node and read its cost from the tooltip.
    The tooltip shows cost in format: "cost / current_dark_matter" in red at the bottom.
    Returns (cost, current_dark_matter) tuple, or (None, None) if not readable.
    """
    print(f"[COST] Hovering over skill at ({x}, {y}) to read cost...")
    
    # Move to skill node
    pyautogui.moveTo(x, y, duration=0.3)
    time.sleep(1.0)  # Wait for tooltip to appear
    
    # Capture screen
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    screen_h, screen_w, _ = screenshot_np.shape
    
    # Tooltip appears centered on screen
    tooltip_width = 900
    tooltip_height = 500
    tooltip_x = max(0, (screen_w // 2) - (tooltip_width // 2))
    tooltip_y = max(0, (screen_h // 2) - (tooltip_height // 2))
    
    # Extract tooltip region
    roi = screenshot_np[tooltip_y:tooltip_y+tooltip_height, tooltip_x:tooltip_x+tooltip_width]
    
    # Save color version for debugging
    cv2.imwrite(f'tooltip_color_{x}_{y}.png', cv2.cvtColor(roi, cv2.COLOR_RGB2BGR))
    
    # Use currency module to extract cost and current amount
    cost, current_dark_matter = read_currency_from_tooltip(roi)
    
    # Save debug images
    gray = cv2.cvtColor(roi, cv2.COLOR_RGB2GRAY)
    _, white_thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)
    cv2.imwrite(f'tooltip_white_{x}_{y}.png', white_thresh)
    
    return cost, current_dark_matter


def find_affordable_skill_nodes():
    """
    Find skill nodes that can be afforded with current dark matter.
    Reads dark matter from UI and tooltip.
    Returns tuple of (affordable_skills list, current_dark_matter).
    """
    print(f"[AFFORD] Finding affordable skills...")
    
    # First, try to read dark matter from UI
    current_dark_matter = read_dark_matter()
    
    if current_dark_matter is not None:
        print(f"[AFFORD] Current dark matter from UI: {current_dark_matter}")
    
    # Get all clickable nodes (with yellow indicators)
    clickable_nodes = find_clickable_skill_nodes()
    
    if not clickable_nodes:
        print("[AFFORD] No clickable nodes found")
        return [], current_dark_matter
    
    affordable_skills = []
    
    for x, y in clickable_nodes:
        cost, dark_matter_from_tooltip = get_skill_cost(x, y)
        
        # Update current_dark_matter from tooltip if we got it
        if dark_matter_from_tooltip is not None:
            current_dark_matter = dark_matter_from_tooltip
            print(f"[AFFORD] Current dark matter from tooltip: {current_dark_matter}")
        
        if cost is not None:
            if current_dark_matter is not None:
                if cost <= current_dark_matter:
                    affordable_skills.append((x, y, cost))
                    print(f"[AFFORD] ✓ Skill at ({x}, {y}) costs {cost} dark matter - AFFORDABLE")
                else:
                    print(f"[AFFORD] ✗ Skill at ({x}, {y}) costs {cost} dark matter - TOO EXPENSIVE (have {current_dark_matter})")
            else:
                # If we don't know current dark matter yet, add it anyway
                affordable_skills.append((x, y, cost))
                print(f"[AFFORD] ? Skill at ({x}, {y}) costs {cost} dark matter - amount unknown, will attempt")
        else:
            print(f"[AFFORD] ? Skill at ({x}, {y}) - cost unknown, skipping")
    
    # Sort by cost (cheapest first)
    affordable_skills.sort(key=lambda s: s[2])
    
    print(f"[AFFORD] Found {len(affordable_skills)} affordable skills")
    return affordable_skills, current_dark_matter


def upgrade_affordable_skills():
    """
    Read current dark matter, find affordable skills, and upgrade them.
    Stops when no more affordable skills are available.
    Returns number of skills upgraded.
    """
    print("[UPGRADE] Starting smart upgrade process...")
    print("[UPGRADE] Note: Skills are purchased with DARK MATTER, not money")
    
    upgraded_count = 0
    consecutive_failures = 0
    max_failures = 2  # Stop after 2 consecutive rounds with no purchases
    
    # Keep trying to upgrade until we can't afford anything
    while consecutive_failures < max_failures:
        print(f"\n[UPGRADE] === Upgrade Round {upgraded_count + 1} ===")
        
        # Find affordable skills (this will read dark matter from UI and tooltips)
        affordable_skills, current_dark_matter = find_affordable_skill_nodes()
        
        if current_dark_matter is not None:
            print(f"[UPGRADE] Current dark matter: {current_dark_matter}")
        
        if not affordable_skills:
            print("[UPGRADE] No affordable skills found in this round")
            consecutive_failures += 1
            continue
        
        # Purchase affordable skills (cheapest first)
        purchased_this_round = 0
        
        for x, y, cost in affordable_skills:
            print(f"[UPGRADE] Purchasing skill at ({x}, {y}) for {cost} dark matter...")
            
            click_skill_node(x, y)
            
            if current_dark_matter is not None:
                current_dark_matter -= cost
                print(f"[UPGRADE] Dark matter remaining: ~{current_dark_matter}")
            
            upgraded_count += 1
            purchased_this_round += 1
            
            time.sleep(1.0)  # Wait for purchase animation
        
        if purchased_this_round == 0:
            consecutive_failures += 1
        else:
            consecutive_failures = 0  # Reset counter on successful purchase
        
        # Brief pause before next round
        time.sleep(1)
    
    print(f"\n[UPGRADE] === Upgrade Complete ===")
    print(f"[UPGRADE] Total skills upgraded: {upgraded_count}")
    
    return upgraded_count