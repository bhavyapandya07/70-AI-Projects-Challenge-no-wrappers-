## Project 6: AI Prompt Improver

This project is a dedicated **Prompt Engineering** utility. It uses a local LLM to act as a meta-layer, refining vague user inputs into structured, professional prompts using the **CO-STAR** or **Role-Context-Task** framework.

## 🛠 Tech Stack
- **Model:** `llama3.2:1b` (via Ollama)
- **Framework:** `LangChain`
- **Interface:** CLI (Command Line Interface)

## 🚀 Why use this?
Directly asking an AI "how to build a dashboard" often results in generic advice. This tool rewrites the prompt to define a **Role** (UX Expert), provide **Context**, and specify a **Format**, ensuring the subsequent AI response is technical and actionable.

## 📥 Execution
1. Ensure Ollama is running.
2. Run the script:
   ```powershell
   python aipi.py
   ```