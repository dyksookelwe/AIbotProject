Personal Conversational AI (Telegram Bot)

Overview

This project is a Telegram bot that generates responses in a personalized communication style based on past message history.

The system is built using a combination of:
 • retrieval (vector search over message history)
 • prompt-based style control
 • local LLM inference (LLaMA 3 via Ollama)

The goal of this project is not to train a new model, but to control and shape the behavior of an existing model using context and examples.

⸻

Architecture
User message → similarity search (RAG) → context injection → LLM → response
Components:
 • Telegram Bot (aiogram)
Handles incoming messages and sends responses
 • Data Processor
Extracts and filters personal messages from Telegram export
 • Vector Database (NumPy + SentenceTransformers)
Encodes messages into embeddings for similarity search
 • AI Logic
 • retrieves relevant past messages
 • builds prompt with contextual examples
 • sends request to LLM
 • LLM (LLaMA 3 via Ollama)
Generates final response

⸻

How it works
 1. Message history is parsed from exported Telegram data
 2. Messages are converted into embeddings and stored locally
 3. When user sends a message:
 • it is encoded into a vector
 • similar past messages are retrieved
 • these messages are injected into the prompt
 4. LLM generates a response using:
 • retrieved context
 • predefined style instructions

⸻

Key Idea

This project does not train a model.

Instead, it relies on:
 • prompt engineering → to control style and tone
 • retrieval (RAG) → to provide relevant context

The model is used as a text generator, not as a learned representation of the user.

⸻

Current Limitations (Old Version)
 • Uses raw messages as context → leads to:
 • repetition
 • incoherent responses
 • copying fragments instead of generating naturally
 • No dialogue structure (no Q/A pairs)
 • Style is mixed with data → model confuses:
 • what to copy
 • how to behave

⸻

Planned Improvements

Next version will include:
 • filtering message history into structured dialogue pairs
 • separating:
 • style (prompt)
 • context (RAG)
 • reducing noise in retrieved messages
 • improving response consistency
 • better control over generation (temperature, penalties)

⸻

Tech Stack
 • Python
 • aiogram
 • SentenceTransformers
 • Ollama
 • NumPy
 • scikit-learn

⸻

Running the Project
 1. Export Telegram data
 2. Configure .env:
 • BOT_TOKEN
 • TELEGRAM_NICK
 • TARGET_CHATS
 3. Run:
    python bot.py

⸻
Purpose

This project is a learning exercise focused on:
 • building AI-powered systems
 • working with LLMs in real applications
 • understanding RAG pipelines
 • controlling model behavior through prompts

⸻

Notes

This is an experimental project and not intended for production use.
The focus is on system design and understanding AI integration rather than model training.
