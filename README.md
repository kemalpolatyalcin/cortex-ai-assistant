# Cortex AI Assistant

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)
![Gemini AI](https://img.shields.io/badge/AI-Google_Gemini-FF6F00.svg)

Cortex is a context-aware, voice-controlled, and multimodal AI assistant built for seamless desktop interaction. It can see your screen, listen to your voice commands, maintain conversational memory, and perform deep web searches to provide real-time, accurate solutions.

## Key Features

* Multimodal Vision: Captures and analyzes your current screen state instantly.
* Voice Interaction: English-first speech recognition and text-to-speech feedback for hands-free operation.
* Contextual Memory: Remembers the flow of the conversation during the active session.
* Deep Web Research: Integrates Google Search Grounding to fetch the most up-to-date information when required.
* FastAPI Backend: High-performance, Dockerized backend architecture.

## Tech Stack

* Backend: Python, FastAPI, Uvicorn, Docker
* AI Engine: Google Generative AI (Gemini Flash)
* Audio & Vision: `SpeechRecognition`, `pyttsx3`, `Pillow` (ImageGrab)

## Getting Started

### 1. Prerequisites
* Python 3.8+
* Docker & Docker Compose
* A valid Google Gemini API Key

### 2. Installation
Clone the repository:
```bash
git clone [https://github.com/YOUR_USERNAME/cortex-ai-assistant.git](https://github.com/YOUR_USERNAME/cortex-ai-assistant.git)
cd cortex-ai-assistant