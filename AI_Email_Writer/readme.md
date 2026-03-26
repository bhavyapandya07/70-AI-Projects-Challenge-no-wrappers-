## ✉️ AI Email Writer

Welcome to **Day 10** of the 70 AI Projects series! 

The **AI Email Writer** is a locally hosted web application that transforms a quick idea into a polished, ready-to-send email. By providing the recipient's name, selecting a desired tone, and inputting your core message, this tool leverages a local Large Language Model to draft the perfect email for you—all without sending your data to the cloud.

## 🛠️ Tech Stack
* **Python**
* **Streamlit** (for the web interface)
* **LangChain** (for prompt orchestration)
* **Ollama** (running `llama3.2:1b` locally)

## 📋 Prerequisites
1. **Python 3.8+** installed on your Windows machine.
2. **Ollama** installed and running locally. 
3. The `llama3.2:1b` model pulled via Ollama. If you don't have it, run this in your terminal:
   ```bash
   ollama pull llama3.2:1b

streamlit run aiew.py