# Gemini AI Assistant with Memory and Real-Time Search

## Overview

Gemini AI Assistant is a Python-based conversational chatbot powered by Google's Gemini 2.5 Flash model. The assistant supports persistent conversation memory, allowing it to remember previous interactions, and uses Google Search grounding to retrieve real-time information such as weather updates, cryptocurrency prices, news, and current events.

The project demonstrates practical implementation of Generative AI, API integration, conversation management, and persistent data storage using Python.

---

## Features

* AI-powered conversations using Gemini 2.5 Flash
* Persistent chat memory stored locally in JSON format
* Real-time information retrieval using Google Search grounding
* Multi-turn conversations with contextual understanding
* Environment variable-based API key security
* Memory clearing functionality
* Lightweight and beginner-friendly architecture

---

## Technologies Used

* Python
* Google Gemini API
* Google GenAI SDK
* Python Dotenv
* JSON Storage

---

## Project Structure

```text
Gemini_Chatbot/
│
├── app.py
├── memory.py
├── history.json
├── .env
├── requirements.txt
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/gemini-ai-assistant.git
cd gemini-ai-assistant
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install google-genai python-dotenv
```

---

## Configure API Key

Create a `.env` file in the project root directory:

```env
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

Get your API key from Google AI Studio.

---

## Running the Application

Start the chatbot using:

```bash
python app.py
```

Example:

```text
Gemini AI Assistant
Type 'exit' to quit
Type 'clear' to clear memory

You: My name is Gomit

Bot: Nice to meet you, Gomit!

You: What is my name?

Bot: Your name is Gomit.

You: Current Bitcoin price

Bot: [Real-time response retrieved using Google Search grounding]
```

---

## Memory System

The chatbot stores conversation history in a local JSON file (`history.json`).

Features:

* Remembers previous messages
* Loads history automatically on startup
* Saves new conversations automatically
* Supports memory reset using the `clear` command

---

## Real-Time Search

The assistant uses Gemini's Google Search grounding capability to answer questions about:

* Weather
* Cryptocurrency prices
* News
* Current events
* Sports
* Stock prices
* General web information

Example:

```text
You: Weather in Mumbai

Bot: Provides the latest weather information retrieved in real time.
```

---

## Future Improvements

* Flask Web Interface
* Voice Input and Output
* SQLite Database Integration
* Multiple Chat Sessions
* Streaming Responses
* User Authentication
* Chat Export Functionality

---

## Learning Outcomes

This project helped demonstrate:

* Generative AI integration
* API usage and authentication
* Persistent memory implementation
* Context management
* Environment variable handling
* Python project structuring

---

## Author

Gomit Ghosh

Aspiring AI Engineer | Python Developer | Machine Learning Enthusiast

---

## License

This project is open-source and available under the MIT License.
