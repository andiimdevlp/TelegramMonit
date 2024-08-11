import json
import os
from datetime import datetime

from .config import log_file

def initialize_log():
    if not os.path.exists(log_file):
        with open(log_file, 'w') as f:
            json.dump([], f)

def log_message(log_entry):
    with open(log_file, 'r+') as f:
        logs = json.load(f)
        logs.append(log_entry)
        f.seek(0)
        json.dump(logs, f, indent=4)

def create_log_entry(event, status, media_info=None):
    return {
        "id": event.message.id,
        "status": status,
        "legenda": event.message.message if event.message.message else "",
        "data": event.message.date.isoformat(),
        "remetente": event.chat_id,
        "tipo": "media" if event.message.media else "texto",
        "media": media_info
    }
