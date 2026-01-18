# Dictation Station 🎙️

A local dictation app that transcribes speech and cleans it up using a local LLM.

## Requirements
* Docker Desktop
* [LM Studio](https://lmstudio.ai/) running the Local Server on port 1234.

## How to Run
1. Start LM Studio server.
2. Run:
   ```bash
   docker compose up --build
   ```
3. Open `http://localhost:8501`.
