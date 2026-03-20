# Day 7: AI JSON Generator 🤖

This project is part of the 70-AI-PROJECTS challenge. It is a local, free-to-run AI tool that takes unstructured plain text descriptions and converts them into strictly formatted, structured JSON objects. 

It leverages **LangChain** for prompt orchestration and **Ollama** to run a lightweight LLM (`llama3.2:1b`) entirely locally, ensuring zero API costs and complete data privacy.

## 🛠️ Tech Stack
* **Language:** Python
* **LLM Orchestration:** LangChain
* **Local LLM Runner:** Ollamac
* **Model:** (`llama3.2:1b`)

## 📋 Prerequisites
Before running this project, ensure you have the following installed:
1. **Python 3.8+**
2. **Ollama**: Download and install from [ollama.com](https://ollama.com/).

Once Ollama is installed, open your terminal and pull the `phi3` model:
```bash
ollama run llama3.2:1b