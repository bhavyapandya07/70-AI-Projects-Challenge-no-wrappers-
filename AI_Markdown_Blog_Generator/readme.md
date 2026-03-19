## Project 5: AI Markdown Blog Generator

This project is part of my **70-Day AI Challenge**. It is a locally-hosted content creation tool that transforms a simple topic into a fully formatted, SEO-friendly Markdown blog post. 

Unlike traditional tools that use expensive APIs, this script leverages **Ollama** to run Large Language Models (LLMs) like `Llama 3` or `Mistral` directly on my Windows machine, ensuring 100% privacy and zero cost.


## 🛠 Tech Stack

* **Language:** Python
* **Orchestration:** `LangChain` / `langchain-ollama`
* **Inference Engine:** `Ollama` (Local LLM runner)
* **Model:** `Llama 3` (8B Parameters)
* **Environment:** Windows + VS Code

## 🚀 Features

* **Local Inference:** No OpenAI/Anthropic API keys required.
* **Markdown Auto-Formatting:** Generates H1, H2, H3 tags, bullet points, and code blocks.
* **Partner-Ready:** Optimized for high-energy design and tech blogging (perfect for Framer/UI-UX topics).
* **Automated Export:** Automatically saves results as `.md` files in a dedicated `/output` folder.

## 📥 Setup & Execution

1.  **Start Ollama:**
    Ensure the Ollama desktop app is running in your Windows System Tray.
    ```powershell
    ollama run llama3
    ```

2.  **Activate Environment:**
    ```powershell
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```powershell
    pip install langchain-ollama langchain-core
    ```

4.  **Run the Script:**
    ```powershell
    python aimbg.py
    ```

## 📂 Project Structure

```text
AI_Markdown_Blog_Generator/
├── aimbg.py          # Main application logic
├── output/           # Generated .md files (git ignored)
└── readme.md         # This documentation
```