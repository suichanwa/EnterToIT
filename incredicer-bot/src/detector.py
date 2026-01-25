import cv2
import numpy as np
import pyautogui
from config import DEBUG

MIN_AREA = 4000
MAX_AREA = 12000
MIN_CONTRAST = 5  # Lowered from 20 to detect dice with 1-2 dots 
MIN_ASPECT_RATIO = 0.85
MAX_ASPECT_RATIO = 1.15
MIN_INTERIOR_BRIGHTNESS = 130  # Lowered from 140 to 130
MAX_BORDER_BRIGHTNESS = 135


def detect_dice(image: np.ndarray):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Adaptive threshold works MUCH better on textured backgrounds
    thresh = cv2.adaptiveThreshold(
        blur,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        11,
        2
    )

    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    dice_centers = []

    for c in contours:
        area = cv2.contourArea(c)
        if not (MIN_AREA < area < MAX_AREA):
            continue

        x, y, w, h = cv2.boundingRect(c)

        ratio = w / h
        if not (MIN_ASPECT_RATIO < ratio < MAX_ASPECT_RATIO):
            continue

        # Extract regions
        roi = gray[y:y+h, x:x+w]

        if roi.size == 0:
            continue

        b = int(min(w, h) * 0.2)
        if b < 2:
            continue
            
        border = np.concatenate([
            roi[:b, :].flatten(),
            roi[-b:, :].flatten(),
            roi[:, :b].flatten(),
            roi[:, -b:].flatten()
        ])

        interior = roi[b:-b, b:-b]

        if interior.size == 0:
            continue

        border_mean = np.mean(border)
        interior_mean = np.mean(interior)
        contrast = interior_mean - border_mean

        if DEBUG:
            print(
                f"[DEBUG] area={int(area)} "
                f"border={int(border_mean)} "
                f"interior={int(interior_mean)} "
                f"contrast={int(contrast)} "
                f"ratio={ratio:.2f}"
            )

        if contrast < MIN_CONTRAST:
            if DEBUG:
                print(f"[DEBUG] ✗ Rejected: low contrast ({int(contrast)} < {MIN_CONTRAST})")
            continue

        if interior_mean < MIN_INTERIOR_BRIGHTNESS:
            if DEBUG:
                print(f"[DEBUG] ✗ Rejected: interior too dark ({int(interior_mean)} < {MIN_INTERIOR_BRIGHTNESS})")
            continue

        if border_mean > MAX_BORDER_BRIGHTNESS:
            if DEBUG:
                print(f"[DEBUG] ✗ Rejected: border too bright ({int(border_mean)} > {MAX_BORDER_BRIGHTNESS})")
            continue

        cx = x + w // 2
        cy = y + h // 2
        dice_centers.append((cx, cy))

        if DEBUG:
            print(f"[DEBUG] ✓ DICE ACCEPTED at ({cx}, {cy})")

    if DEBUG and len(dice_centers) > 0:
        cv2.imshow("dice_view", image)
        cv2.imshow("threshold", thresh)
        cv2.waitKey(1)

    return dice_centers[0] if dice_centers else None


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
