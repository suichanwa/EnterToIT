# src/hotkeys.py

import keyboard

def init_hotkeys(toggle_callback):
    keyboard.add_hotkey("F8", toggle_callback)
