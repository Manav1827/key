import pyautogui
import time
from utils import get_timestamp
import os

def capture_screenshot_periodically(interval=5):
    os.makedirs("logs", exist_ok=True)
    while True:
        filename = f"logs/screenshot_{get_timestamp().replace(':', '-')}.png"
        screenshot = pyautogui.screenshot()
        screenshot.save(filename)
        time.sleep(interval)
