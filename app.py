import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

from memory import (
    add_message,
    get_history,
    load_history,
    clear_history
)

# ==========================
# LOAD ENV VARIABLES
# ==========================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found in .env file"
    )

# ==========================
# GEMINI CLIENT
# ==========================

client = genai.Client(
    api_key=API_KEY
)

MODEL = "gemini-2.5-flash"

# ==========================
# LOAD OLD CHAT HISTORY
# ==========================

load_history()


# ==========================
# BUILD CONTEXT
# ==========================

def build_context():

    history = get_history()

    # Use only last 10 messages
    history = history[-10:]

    context = ""

    for msg in history:
        context += (
            f"{msg['role']}: "
            f"{msg['text']}\n"
        )

    return context


# ==========================
# ASK GEMINI
# ==========================

def ask_gemini(user_input):

    context = build_context()

    prompt = f"""
You are a helpful AI assistant.

Conversation History:
{context}

Current User Message:
{user_input}

Respond naturally and remember previous messages.
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            tools=[
                types.Tool(
                    google_search=types.GoogleSearch()
                )
            ]
        )
    )

    return response.text


# ==========================
# CHAT LOOP
# ==========================

print("=" * 50)
print("Gemini AI Assistant")
print("Type 'exit' to quit")
print("Type 'clear' to clear memory")
print("=" * 50)

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    if user_input.lower() == "clear":
        clear_history()
        print("Memory cleared.")
        continue

    try:

        add_message(
            "user",
            user_input
        )

        reply = ask_gemini(
            user_input
        )

        add_message(
            "assistant",
            reply
        )

        print("\nBot:", reply)

    except Exception as e:

        print(
            "\nError:",
            str(e)
        )
