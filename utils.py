from datetime import datetime
import os
from logger_config import LOG_FILE

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def save_log(data):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(data)
