# Day 11: 🐦 AI Twitter Thread Generator

An AI-powered tool that takes any long-form topic or news snippet and transforms it into a viral-ready, 5-tweet Twitter thread.

## 🚀 Features
- **Local Execution:** Runs entirely on your machine using Ollama.
- **Tone Selection:** Choose from Professional, Hype, Educational, or Witty.
- **Smart Formatting:** Includes "hooks," numbered tweets, and emojis automatically.

## 🛠️ Tech Stack
- **Python** (Core Logic)
- **Streamlit** (UI Framework)
- **LangChain** (AI Orchestration)
- **Ollama** (Running Llama 3.2 locally)

## 📦 Setup & Run
1. Ensure Ollama is running and pull the model:
   `ollama pull llama3.2`
2. Install dependencies:
   `pip install langchain langchain-ollama streamlit`
3. Run the app:
   `streamlit run aitg.py`