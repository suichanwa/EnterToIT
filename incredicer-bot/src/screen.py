import pyautogui
import numpy as np

def grab_center_region(width: int, height: int) -> np.ndarray:
    screen_w, screen_h = pyautogui.size()

    left = screen_w // 2 - width // 2
    top = screen_h // 2 - height // 2

    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    return np.array(screenshot), left, top
