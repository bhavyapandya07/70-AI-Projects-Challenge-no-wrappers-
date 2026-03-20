# Day 8: AI Resume Analyzer 📄

This project is part of the 70-AI-PROJECTS challenge. It is a local, privacy-first AI application that acts as an expert Tech Recruiter. Users can upload their resumes in PDF format, and the app will process the document to provide actionable, constructive feedback.

Built with a clean web interface, it processes documents and runs inference entirely on your local machine, ensuring sensitive personal data never leaves your computer.

## ✨ Features
* **PDF Text Extraction:** Seamlessly reads and extracts text from uploaded PDF resumes.
* **Local AI Inference:** Powered by Ollama running the highly efficient `llama3.2:1b` model.
* **Privacy First:** Zero API calls to external servers; your data remains 100% local.
* **Structured Feedback:** Automatically generates an Overall Impression, Key Strengths, Areas for Improvement, and ATS (Applicant Tracking System) Optimization Tips.
* **Interactive UI:** A simple, intuitive web interface built with Streamlit.

## 🛠️ Tech Stack
* **Frontend/UI:** Streamlit
* **PDF Processing:** PyPDF2
* **LLM Orchestration:** LangChain
* **Local LLM Runner:** Ollama
* **Model:** Llama 3.2 1B (`llama3.2:1b`)

## 📋 Prerequisites
1. **Python 3.8+**
2. **Ollama**: Download and install from [ollama.com](https://ollama.com/).

Once Ollama is installed, open your terminal and pull the specific lightweight model used in this project:
```bash
ollama run llama3.2:1b