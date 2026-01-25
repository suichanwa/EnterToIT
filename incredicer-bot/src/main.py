import time
from screen import grab_center_region
from detector import detect_dice
from mouse import hover
from hotkeys import init_hotkeys
from config import SCAN_WIDTH, SCAN_HEIGHT, SCAN_DELAY
from ui_detector import click_skill_tree

enabled = False 
last_dice_pos = None  # Track last dice position
MIN_DISTANCE = 50  # Reduced from 80 - allow clicking closer dice

# Mode selection
MODE = None


def toggle():
    global enabled
    enabled = not enabled
    print(f"[STATE] {'ENABLED' if enabled else 'PAUSED'}")


def distance(p1, p2):
    """Calculate Euclidean distance between two points"""
    if p1 is None or p2 is None:
        return float('inf')
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5


def run_dice_mode():
    """Mode 0: Click on dice"""
    global last_dice_pos
    loop_count = 0
    
    print("[MODE 0] Starting dice clicking mode...")
    
    while True:
        if not enabled:
            time.sleep(0.1)
            continue

        loop_count += 1
        print(f"[LOOP {loop_count}] Scanning screen...")

        image, offset_x, offset_y = grab_center_region(
            SCAN_WIDTH, SCAN_HEIGHT
        )

        if image is None:
            print("[WARN] Failed to capture screen")
            time.sleep(SCAN_DELAY)
            continue

        pos = detect_dice(image)

        if pos:
            x, y = pos
            abs_x = offset_x + x
            abs_y = offset_y + y

            # Check if this is the same dice we just rolled
            if last_dice_pos and distance((abs_x, abs_y), last_dice_pos) < MIN_DISTANCE:
                print(f"[SKIP] Same dice position, waiting...")
                time.sleep(SCAN_DELAY)
                continue

            print(f"[DETECT] Dice found at ({abs_x}, {abs_y}) → hovering")
            hover(abs_x, abs_y)
            last_dice_pos = (abs_x, abs_y)

            print("[ACTION] Waiting for roll cooldown...")
            time.sleep(1.0)
        else:
            print("[DETECT] Dice NOT found")
            last_dice_pos = None
            time.sleep(SCAN_DELAY)


def run_skill_tree_mode():
    """Mode 1: Find and click skill tree button"""
    print("[MODE 1] Starting skill tree test mode...")
    print("[MODE 1] Waiting 3 seconds before searching...")
    time.sleep(3)
    
    print("[MODE 1] Searching for skill tree button...")
    success = click_skill_tree()
    
    if success:
        print("[MODE 1] Successfully clicked skill tree button!")
    else:
        print("[MODE 1] Failed to find skill tree button")
    
    print("[MODE 1] Test complete. Exiting...")


# Main entry point
print("[INIT] Starting Incredicer bot...")
print("[INIT] F8 → Toggle ON / OFF")
print("[INIT] Move mouse to top-left corner to STOP")
print()
print("=" * 50)
print("SELECT MODE:")
print("  0 - Dice clicking mode (default)")
print("  1 - Skill tree test mode")
print("=" * 50)

while MODE is None:
    try:
        mode_input = input("Enter mode (0 or 1): ").strip()
        if mode_input in ['0', '1']:
            MODE = int(mode_input)
        else:
            print("Invalid input. Please enter 0 or 1.")
    except (ValueError, KeyboardInterrupt):
        print("\nDefaulting to mode 0")
        MODE = 0

print(f"\n[INIT] Selected mode: {MODE}")

init_hotkeys(toggle)

print("[INIT] Waiting 3 seconds before start...")
time.sleep(3)

# Run selected mode
if MODE == 0:
    run_dice_mode()
elif MODE == 1:
    run_skill_tree_mode()
