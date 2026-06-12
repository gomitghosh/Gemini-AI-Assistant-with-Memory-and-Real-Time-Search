import json
import os

HISTORY_FILE = "history.json"

conversation_history = []


def load_history():
    global conversation_history

    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                conversation_history = json.load(f)
        except:
            conversation_history = []
    else:
        conversation_history = []


def save_history():
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(
            conversation_history,
            f,
            indent=4,
            ensure_ascii=False
        )


def add_message(role, text):
    conversation_history.append(
        {
            "role": role,
            "text": text
        }
    )

    save_history()


def get_history():
    return conversation_history


def clear_history():
    global conversation_history

    conversation_history = []
    save_history()
