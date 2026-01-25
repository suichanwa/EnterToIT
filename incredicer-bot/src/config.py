DEBUG = True

# Scan entire screen - will be adjusted based on actual screen size
SCAN_WIDTH = 2880  # Full width for 2880x1800 display
SCAN_HEIGHT = 1800  # Full height

SCAN_DELAY = 0.15  # Even faster scanning

MOVE_DURATION = 0.12

# More lenient color range for dice detection
DICE_COLOR_LOWER = (150, 150, 150)
DICE_COLOR_UPPER = (255, 255, 255)

# Add these validation parameters if not present
MIN_DICE_AREA = 2000
MAX_DICE_AREA = 10000
MIN_ASPECT_RATIO = 0.7
MAX_ASPECT_RATIO = 1.3