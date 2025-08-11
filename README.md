Echo - Your AI-Powered Virtual Assistant
========================================

[](https://github.com/gyanprakash03/Echo-virtual-assistant/new/main?filename=README.md#echo---your-ai-powered-virtual-assistant)

Echo is a voice-controlled Python virtual assistant that can:

-   Open websites on your command

-   Play songs on YouTube

-   Reply to WhatsApp messages on your behalf

-   Answer any question using Google's Gemini API

Features
--------

[](https://github.com/gyanprakash03/Echo-virtual-assistant/new/main?filename=README.md#features)

-   Voice Activation: Just say "Echo" to wake the assistant.

-   Open Websites: Example -- "open google" → opens Google in your browser.

-   Play Music: Example -- "play despacito" → plays the song on YouTube.

-   WhatsApp Auto-Reply: Automatically reads the visible chat from WhatsApp Web and replies in your style using AI.

-   Ask Anything: Uses Google's Gemini API for general questions and answers.

Installation
------------

[](https://github.com/gyanprakash03/Echo-virtual-assistant/new/main?filename=README.md#installation)

### Clone the Repository
```bash
   git clone https://github.com/your-username/echo-assistant.git
   cd echo-assistant
```

### Set Up a Virtual Environment
```bash
   python -m venv .venvsource
   .venv/bin/activate # macOS/Linux
   .venv\Scripts\activate # Windows
```

### Install Dependencies
```bash 
   pip install -r requirements.txt
```
###  Set Up Environment Variables

```env
   GEMINI_API_KEY=your_google_gemini_api_key
```

  -   You can get a Gemini API key from Google AI Studio.

Usage
-----

[](https://github.com/gyanprakash03/Echo-virtual-assistant/new/main?filename=README.md#usage)

### Run the assistant:

```bash
   python main.py
```

### Example Commands

[](https://github.com/gyanprakash03/Echo-virtual-assistant/new/main?filename=README.md#example-commands)

-   "Echo" → Activates Echo

-   "open wikipedia" → Opens Wikipedia.

-   "play shape of you" → Plays the song on YouTube.

-   "reply" → Reads your current WhatsApp Web chat, generates a response, and sends it.

-   "who is Albert Einstein" → Gets an AI-generated answer.

-   "sleep" → Puts Echo to sleep until reactivated.

-   "exit" → Exits the program.

Requirements
------------

[](https://github.com/gyanprakash03/Echo-virtual-assistant/new/main?filename=README.md#requirements)

-   Python 3.8+

-   A working microphone

-   Google Gemini API key

-   WhatsApp Web open in Google Chrome for the reply feature

-   pyautogui requires screen access permissions (macOS users may need to enable in System Preferences)

Disclaimer
----------

[](https://github.com/gyanprakash03/Echo-virtual-assistant/new/main?filename=README.md#disclaimer)

-   WhatsApp automation is done via WhatsApp Web using simulated mouse and keyboard actions.

-   Coordinates for selecting chats may need to be adjusted for your screen resolution.
