## 📝 AI Meeting Notes Generator

Welcome to **Day 9** of the 70 AI Projects series! 

The **AI Meeting Notes Generator** is a powerful, locally-hosted tool designed to turn messy, raw meeting transcripts into clean, structured notes. It automatically extracts an Executive Summary, Key Decisions, and Action Items using a local Large Language Model, ensuring your internal meeting data stays entirely private.

## 🛠️ Tech Stack
* **Python**
* **Streamlit** (for the frontend GUI)
* **LangChain** (for prompt structuring)
* **Ollama** (running `llama3.2:1b` locally)

## 📋 Prerequisites
1. **Python 3.8+** installed.
2. **Ollama** installed and running on your Windows machine.
3. The `llama3.2:1b` model pulled via Ollama. If not, open your terminal and run:
   ```bash
   ollama pull llama3.2:1b

streamlit run aimng.py