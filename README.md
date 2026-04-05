# AI Chatbot with Multi-Layer Intent Routing

## Overview
This project is an AI-powered chatbot designed to handle user interactions using a multi-layer intent detection and routing system.

The goal of the system is to combine deterministic logic with AI-based understanding to build a scalable and efficient conversational backend.

---

## Architecture

The system follows a layered approach:

1. **FSM (Deterministic Layer)**
   - Handles high-confidence scenarios (e.g. structured flows like lead collection)
   - Fast and predictable

2. **Semantic Matching (Embeddings)**
   - Matches user queries to known intents using similarity
   - Provides flexibility beyond hardcoded rules

3. **LLM Fallback**
   - Handles complex or unknown queries
   - Ensures robustness of the system

**Pipeline:**
User Input → Intent Detection → Routing → FSM / RAG / LLM → Response

---

## Features

- Multi-layer intent detection system
- FSM-based conversation handling
- LLM integration for fallback responses
- Modular backend structure
- Telegram interface (can be extended to other channels)

---

## Tech Stack

- Python
- FastAPI / Flask (if applicable)
- OpenAI API / LLM provider
- Embeddings-based similarity
- Telegram Bot API

---

## Current Limitations

This project is a prototype and still under development. Current limitations include:

- FSM logic needs refinement
- No persistent storage (state resets after restart)
- Intent detection is partially rule-based
- Retrieval (RAG) can be improved
- Logging and monitoring are minimal

---

## Roadmap

Planned improvements:

- Add dedicated intent classification layer
- Introduce persistent storage (database)
- Improve FSM as part of a unified pipeline
- Enhance RAG with re-ranking and better context selection
- Add logging and analytics
- Decouple core logic from Telegram (multi-channel support)
- Improve error handling and fallback strategies

---

## Key Learning

This project helped me understand:

- How to design layered AI systems
- Trade-offs between deterministic logic and LLMs
- Building scalable backend architectures for AI applications
- Handling real-world uncertainty in user input

---

## How to Run

```bash
git clone ...
pip install -r requirements.txt
python main.py
```
---
## Environment settings
Create a file with the .env extension in the root of the project
```
BOT_TOKEN=your_telegram_bot_token
AI_API_KEY=your_api_key
BASE_URL=your_api_url