import cv2
import numpy as np
import pyautogui
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def read_currency_from_region(region_name, x, y, width, height):
    """
    Read currency amount from a specific screen region.
    
    Args:
        region_name: Name for debugging purposes
        x, y: Top-left corner of region
        width, height: Size of region
    
    Returns:
        Integer amount or None if not found
    """
    # Capture full screen
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    
    # Convert to grayscale
    gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)
    
    # Extract region
    roi = gray[y:y+height, x:x+width]
    
    # Try different thresholding methods
    # Method 1: High threshold for white text
    _, thresh1 = cv2.threshold(roi, 180, 255, cv2.THRESH_BINARY)
    
    # Method 2: Lower threshold
    _, thresh2 = cv2.threshold(roi, 150, 255, cv2.THRESH_BINARY)
    
    # Method 3: Adaptive threshold
    thresh3 = cv2.adaptiveThreshold(roi, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                    cv2.THRESH_BINARY, 11, 2)
    
    # Save debug images
    cv2.imwrite(f'{region_name}_detection_area.png', roi)
    cv2.imwrite(f'{region_name}_thresh1.png', thresh1)
    cv2.imwrite(f'{region_name}_thresh2.png', thresh2)
    cv2.imwrite(f'{region_name}_thresh3.png', thresh3)
    
    print(f"[{region_name.upper()}] Debug images saved")
    
    all_numbers = []
    
    # Try OCR on all threshold versions
    for thresh_method, thresh in [('high', thresh1), ('low', thresh2), ('adaptive', thresh3)]:
        text = pytesseract.image_to_string(thresh, config='--psm 6')
        
        # Extract numbers from text
        numbers = re.findall(r'\d+', text.replace(',', '').replace(' ', '').replace('.', ''))
        
        if numbers:
            for num_str in numbers:
                try:
                    num = int(num_str)
                    # Filter out unrealistic values (too small or too large)
                    if 1 < num < 1000000:
                        all_numbers.append(num)
                        print(f"[{region_name.upper()}] Found number {num} using {thresh_method} threshold")
                except ValueError:
                    continue
    
    if all_numbers:
        # Take the largest number found (likely the currency amount)
        currency = max(all_numbers)
        print(f"[{region_name.upper()}] Detected amount: {currency}")
        return currency
    
    print(f"[{region_name.upper()}] Could not detect amount")
    return None


def read_money():
    """
    Read the money/dice currency from the top-left corner.
    This is the main currency shown with a dice icon.
    Returns the amount as an integer, or None if not found.
    """
    screen_w, screen_h = pyautogui.size()
    
    # Money is in top-left corner, typically with a dice icon
    search_x = 0
    search_y = 0
    search_width = int(screen_w * 0.15)
    search_height = int(screen_h * 0.08)
    
    return read_currency_from_region('money', search_x, search_y, search_width, search_height)


def read_dark_matter():
    """
    Read the dark matter currency from the top-left corner.
    This is displayed below or near the money amount.
    Returns the amount as an integer, or None if not found.
    """
    screen_w, screen_h = pyautogui.size()
    
    # Dark matter is also in top-left, slightly below money
    # Adjust these values based on your screen layout
    search_x = 0
    search_y = int(screen_h * 0.06)  # Start slightly below money
    search_width = int(screen_w * 0.15)
    search_height = int(screen_h * 0.08)
    
    return read_currency_from_region('dark_matter', search_x, search_y, search_width, search_height)


def read_all_currencies():
    """
    Read all available currencies from the screen.
    Returns a dictionary with currency types and amounts.
    """
    currencies = {
        'money': read_money(),
        'dark_matter': read_dark_matter()
    }
    
    print(f"[CURRENCY] All currencies: {currencies}")
    return currencies


def read_currency_from_tooltip(tooltip_roi):
    """
    Extract currency amount from a tooltip image region.
    The tooltip shows "cost / current_amount" format in red text.
    
    Args:
        tooltip_roi: numpy array of the tooltip region (RGB)
    
    Returns:
        Tuple of (cost, current_amount) or (None, None)
    """
    # Convert to HSV for red color detection
    roi_hsv = cv2.cvtColor(tooltip_roi, cv2.COLOR_RGB2HSV)
    
    # Define red color range (for cost text)
    lower_red1 = np.array([0, 80, 80])
    upper_red1 = np.array([15, 255, 255])
    lower_red2 = np.array([165, 80, 80])
    upper_red2 = np.array([180, 255, 255])
    
    # Create masks for red color
    mask1 = cv2.inRange(roi_hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(roi_hsv, lower_red2, upper_red2)
    red_mask = cv2.bitwise_or(mask1, mask2)
    
    # Read red text (cost information)
    red_text = pytesseract.image_to_string(red_mask, config='--psm 6')
    print(f"[TOOLTIP] Red text: '{red_text}'")
    
    # Parse cost from red text - format is "cost / current_amount"
    # Example: "30 / 169"
    cost_match = re.search(r'(\d+)\s*/\s*(\d+)', red_text.replace(',', ''))
    
    if cost_match:
        cost = int(cost_match.group(1))
        current_amount = int(cost_match.group(2))
        print(f"[TOOLTIP] Detected cost: {cost}, current amount: {current_amount}")
        return cost, current_amount
    
    # Fallback: try to find any numbers in the text
    numbers = re.findall(r'\d+', red_text.replace(',', ''))
    if len(numbers) >= 2:
        cost = int(numbers[0])
        current_amount = int(numbers[1])
        print(f"[TOOLTIP] Detected (fallback) cost: {cost}, current amount: {current_amount}")
        return cost, current_amount
    elif len(numbers) == 1:
        cost = int(numbers[0])
        print(f"[TOOLTIP] Detected only cost (fallback): {cost}")
        return cost, None
    
    print("[TOOLTIP] Could not detect cost from tooltip")
    return None, None