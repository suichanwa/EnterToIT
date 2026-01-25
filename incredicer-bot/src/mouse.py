# src/mouse.py

import pyautogui
from config import MOVE_DURATION

pyautogui.FAILSAFE = True

def hover(x: int, y: int):
    pyautogui.moveTo(x, y, duration=MOVE_DURATION)
