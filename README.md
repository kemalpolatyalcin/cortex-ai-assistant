# Cortex AI Assistant

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)
![Gemini AI](https://img.shields.io/badge/AI-Google_Gemini-FF6F00.svg)

Cortex is a context-aware, voice-controlled, and multimodal AI assistant built for seamless desktop interaction. It analyzes the screen state, processes voice commands, maintains session memory, and executes deep web research to provide accurate, real-time solutions.

## Key Features

- **Multimodal Vision:** Captures and analyzes your current screen state instantly.
- **Voice Interaction:** English-first speech recognition and text-to-speech feedback for hands-free operation.
- **Contextual Memory:** Remembers the flow of the conversation during the active session.
- **Deep Web Research:** Integrates Google Search Grounding to fetch the most up-to-date information when required.
- **FastAPI Backend:** High-performance, Dockerized backend architecture.

## Tech Stack

- **Backend:** Python, FastAPI, Uvicorn, Docker
- **AI Engine:** Google Generative AI (Gemini Flash)
- **Audio & Vision:** `SpeechRecognition`, `pyttsx3`, `Pillow` (`ImageGrab`)

## Getting Started

### 1. Prerequisites

- Python 3.8+
- Docker and Docker Compose
- A valid Google Gemini API Key

### 2. Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/kemalpolatyalcin/cortex-ai-assistant.git
cd cortex-ai-assistant
```

### Running the Assistant

Create a `.env` file and add your API key:

```env
GOOGLE_API_KEY=your_api_key_here
```

Start the backend:

```bash
docker compose up --build
```

In another terminal, install the dependencies and launch the assistant:

```bash
pip install -r requirements.txt
python cortex_vision.py
```

Press the global hotkey:

```
CTRL + ALT + S
```

Speak your command clearly in English.

## Security Note

> Never commit your `.env` file or expose your API keys to the public. This repository utilizes a `.gitignore` configuration to prevent credentials from being uploaded. Always verify that your sensitive data remains strictly local.