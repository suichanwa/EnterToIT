import cv2
import numpy as np
import pyautogui
import pytesseract
import time
import win32api
import win32con
import re

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


def find_skill_nodes():
    """
    Find clickable skill nodes in the skill tree.
    Returns list of (x, y) coordinates of skill nodes.
    """
    # Capture full screen
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    
    # Convert to grayscale
    gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)
    
    # Apply threshold to find dark skill nodes (they appear darker than background)
    _, thresh = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY_INV)
    
    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    skill_nodes = []
    
    for contour in contours:
        area = cv2.contourArea(contour)
        
        # Skill nodes should be reasonably sized (adjust based on your screen resolution)
        if 800 < area < 3000:
            x, y, w, h = cv2.boundingRect(contour)
            
            # Check if it's roughly square (skill nodes appear square-ish)
            aspect_ratio = w / h if h > 0 else 0
            if 0.7 < aspect_ratio < 1.3:
                # Calculate center
                center_x = x + w // 2
                center_y = y + h // 2
                
                # Check if node has the characteristic appearance
                roi = gray[y:y+h, x:x+w]
                if roi.size > 0:
                    # Skill nodes have dark borders and specific interior pattern
                    mean_brightness = np.mean(roi)
                    
                    # Look for nodes that are darker than background
                    if mean_brightness < 120:
                        skill_nodes.append((center_x, center_y))
                        print(f"[SKILL] Found skill node at ({center_x}, {center_y})")
    
    # Save debug image
    debug_img = screenshot_np.copy()
    for x, y in skill_nodes:
        cv2.circle(debug_img, (x, y), 20, (0, 255, 0), 2)
    cv2.imwrite('skill_nodes_detected.png', cv2.cvtColor(debug_img, cv2.COLOR_RGB2BGR))
    print(f"[SKILL] Found {len(skill_nodes)} skill nodes. Debug image saved to skill_nodes_detected.png")
    
    return skill_nodes


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


def upgrade_available_skills():
    """
    Find and click all available skill upgrades.
    Returns number of skills upgraded.
    """
    print("[SKILL] Searching for upgradeable skills...")
    
    clickable_nodes = find_clickable_skill_nodes()
    
    if not clickable_nodes:
        print("[SKILL] No upgradeable skills found")
        return 0
    
    print(f"[SKILL] Found {len(clickable_nodes)} upgradeable skills")
    
    for i, (x, y) in enumerate(clickable_nodes, 1):
        print(f"[SKILL] Upgrading skill {i}/{len(clickable_nodes)}...")
        click_skill_node(x, y)
        time.sleep(0.5)
    
    return len(clickable_nodes)


def read_currency_amount():
    """
    Read the currency/money amount from the top-left corner of the screen.
    Returns the amount as an integer, or None if not found.
    """
    # Capture full screen
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    
    # Convert to grayscale
    gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)
    
    screen_w, screen_h = pyautogui.size()
    
    # Currency is typically in top-left corner (look for the dice icon)
    search_x = 0
    search_y = 0
    search_width = int(screen_w * 0.2)  # Left 20% of screen
    search_height = int(screen_h * 0.15)   # Top 15% of screen
    
    roi = gray[search_y:search_y+search_height, search_x:search_x+search_width]
    
    # Apply threshold to isolate white/light text
    _, thresh = cv2.threshold(roi, 180, 255, cv2.THRESH_BINARY)
    
    # Save debug image
    cv2.imwrite('currency_detection.png', thresh)
    print("[CURRENCY] Debug image saved to currency_detection.png")
    
    # Use tesseract to detect text
    text = pytesseract.image_to_string(thresh, config='--psm 6')
    
    print(f"[CURRENCY] Raw OCR text: '{text}'")
    
    # Extract all numbers from text
    numbers = re.findall(r'\d+', text.replace(',', '').replace(' ', ''))
    
    if numbers:
        # Take the largest number found (likely the currency amount)
        amounts = [int(n) for n in numbers]
        currency = max(amounts)
        print(f"[CURRENCY] Detected currency: {currency}")
        return currency
    
    print("[CURRENCY] Could not detect currency amount")
    return None


def get_skill_cost(x, y):
    """
    Hover over a skill node and read its cost from the tooltip.
    The tooltip shows cost in format: "cost / current_money" in red at the bottom.
    Returns (cost, description) tuple, or (None, None) if not readable.
    """
    print(f"[COST] Hovering over skill at ({x}, {y}) to read cost...")
    
    # Move to skill node
    pyautogui.moveTo(x, y, duration=0.3)
    time.sleep(0.8)  # Wait for tooltip to appear
    
    # Capture screen
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    screen_h, screen_w, _ = screenshot_np.shape
    
    # Tooltip appears centered on screen, search in the center area
    # Based on the image, tooltip is roughly 800x400 pixels
    tooltip_width = 900
    tooltip_height = 450
    tooltip_x = max(0, (screen_w // 2) - (tooltip_width // 2))
    tooltip_y = max(0, (screen_h // 2) - (tooltip_height // 2))
    
    # Extract tooltip region
    roi = screenshot_np[tooltip_y:tooltip_y+tooltip_height, tooltip_x:tooltip_x+tooltip_width]
    
    # Convert to grayscale
    gray = cv2.cvtColor(roi, cv2.COLOR_RGB2GRAY)
    
    # Save color version for debugging
    cv2.imwrite(f'tooltip_color_{x}_{y}.png', cv2.cvtColor(roi, cv2.COLOR_RGB2BGR))
    
    # The cost is in RED color at the bottom. Let's extract red text specifically
    roi_hsv = cv2.cvtColor(roi, cv2.COLOR_RGB2HSV)
    
    # Define red color range
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([180, 255, 255])
    
    # Create masks for red color
    mask1 = cv2.inRange(roi_hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(roi_hsv, lower_red2, upper_red2)
    red_mask = cv2.bitwise_or(mask1, mask2)
    
    # Also try with white text (for the description)
    _, white_thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)
    
    # Save debug images
    cv2.imwrite(f'tooltip_red_{x}_{y}.png', red_mask)
    cv2.imwrite(f'tooltip_white_{x}_{y}.png', white_thresh)
    
    # Read red text (cost information)
    red_text = pytesseract.image_to_string(red_mask, config='--psm 6')
    print(f"[COST] Red text (cost): '{red_text}'")
    
    # Read white text (skill description)
    white_text = pytesseract.image_to_string(white_thresh, config='--psm 6')
    print(f"[COST] White text (description): '{white_text}'")
    
    # Parse cost from red text - format is "cost / current_money"
    # Example: "30 / 169"
    cost_match = re.search(r'(\d+)\s*/\s*(\d+)', red_text.replace(',', ''))
    
    if cost_match:
        cost = int(cost_match.group(1))
        current_money_in_tooltip = int(cost_match.group(2))
        print(f"[COST] Detected cost: {cost} (tooltip shows current money: {current_money_in_tooltip})")
        
        # Extract skill description from white text
        description = white_text.strip()
        
        return cost, description
    
    # Fallback: try to find any numbers in the text
    numbers = re.findall(r'\d+', red_text.replace(',', ''))
    if len(numbers) >= 1:
        cost = int(numbers[0])
        print(f"[COST] Detected cost (fallback): {cost}")
        return cost, white_text.strip()
    
    print("[COST] Could not detect cost from tooltip")
    return None, None


def find_affordable_skill_nodes(current_money):
    """
    Find skill nodes that can be afforded with current money.
    Returns list of (x, y, cost, description) tuples sorted by cost (cheapest first).
    """
    print(f"[AFFORD] Finding skills affordable with {current_money} currency...")
    
    # Get all clickable nodes (with yellow indicators)
    clickable_nodes = find_clickable_skill_nodes()
    
    if not clickable_nodes:
        print("[AFFORD] No clickable nodes found")
        return []
    
    affordable_skills = []
    
    for x, y in clickable_nodes:
        cost, description = get_skill_cost(x, y)
        
        if cost is not None:
            if cost <= current_money:
                affordable_skills.append((x, y, cost, description))
                print(f"[AFFORD] ✓ Skill at ({x}, {y}) costs {cost} - AFFORDABLE")
                if description:
                    print(f"         Description: {description[:50]}...")
            else:
                print(f"[AFFORD] ✗ Skill at ({x}, {y}) costs {cost} - TOO EXPENSIVE")
        else:
            print(f"[AFFORD] ? Skill at ({x}, {y}) - cost unknown, skipping")
    
    # Sort by cost (cheapest first)
    affordable_skills.sort(key=lambda s: s[2])
    
    print(f"[AFFORD] Found {len(affordable_skills)} affordable skills")
    return affordable_skills


def upgrade_affordable_skills():
    """
    Read current money, find affordable skills, and upgrade them.
    Stops when no more affordable skills are available.
    Returns number of skills upgraded.
    """
    print("[UPGRADE] Starting smart upgrade process...")
    
    # Step 1: Read current currency
    current_money = read_currency_amount()
    
    if current_money is None:
        print("[UPGRADE] ERROR: Could not read currency amount")
        return 0
    
    print(f"[UPGRADE] Current money: {current_money}")
    
    upgraded_count = 0
    remaining_money = current_money
    consecutive_failures = 0
    max_failures = 2  # Stop after 2 consecutive rounds with no purchases
    
    # Keep trying to upgrade until we can't afford anything
    while consecutive_failures < max_failures:
        print(f"\n[UPGRADE] === Upgrade Round {upgraded_count + 1} ===")
        print(f"[UPGRADE] Money available: {remaining_money}")
        
        # Step 2: Find affordable skills
        affordable_skills = find_affordable_skill_nodes(remaining_money)
        
        if not affordable_skills:
            print("[UPGRADE] No affordable skills found in this round")
            consecutive_failures += 1
            continue
        
        # Step 3: Purchase affordable skills (cheapest first)
        purchased_this_round = 0
        
        for x, y, cost, description in affordable_skills:
            if cost > remaining_money:
                print(f"[UPGRADE] Stopping - not enough money for skill costing {cost}")
                break
            
            print(f"[UPGRADE] Purchasing skill at ({x}, {y}) for {cost}...")
            if description:
                print(f"[UPGRADE] Effect: {description[:80]}")
            
            click_skill_node(x, y)
            
            remaining_money -= cost
            upgraded_count += 1
            purchased_this_round += 1
            print(f"[UPGRADE] Money remaining: {remaining_money}")
            
            time.sleep(0.8)  # Wait for purchase animation
        
        if purchased_this_round == 0:
            consecutive_failures += 1
        else:
            consecutive_failures = 0  # Reset counter on successful purchase
        
        # Brief pause before next round
        time.sleep(1)
    
    print(f"\n[UPGRADE] === Upgrade Complete ===")
    print(f"[UPGRADE] Total skills upgraded: {upgraded_count}")
    print(f"[UPGRADE] Money spent: {current_money - remaining_money}")
    print(f"[UPGRADE] Money remaining: {remaining_money}")
    
    return upgraded_count