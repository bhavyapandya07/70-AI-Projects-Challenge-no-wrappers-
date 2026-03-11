## Project 3: AI Code Explainer 🤖

This project is part of my 70-Day AI Challenge. It is a Python-based tool that takes a code snippet as input and provides a clear, concise explanation of what the code does. 

It leverages **Hugging Face's Serverless Inference API** to run the `Qwen2.5-Coder-32B-Instruct` model completely free of charge in the cloud.

## Tech Stack

❏ **Language:** Python

❏ **API:** Hugging Face Inference API (Free Tier)

❏ **Model:** `Qwen/Qwen2.5-Coder-32B-Instruct`

❏ **Libraries:** `huggingface_hub`

## Setup & Execution

❏ **Get an API Key:** Create a free account on [Hugging Face](https://huggingface.co/) and generate an Access Token (Read).

❏ **Add Key to Code:** Open `explainer.py` and replace `"YOUR_HUGGINGFACE_TOKEN"` with your actual token.

❏ **Activate Environment:** Ensure your virtual environment is active.
   ```cmd
   .\venv\Scripts\activate