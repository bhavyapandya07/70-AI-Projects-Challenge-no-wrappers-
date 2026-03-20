import os
import json
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate

load_dotenv()
llm = Ollama(model="llama3.2:1b")
def generate_structured_json(user_description: str) -> str:
    """
    Takes a plain text description and returns a structured JSON object.
    """
    template = """
    You are a strict data extraction AI. 
    Convert the following user description into a well-structured JSON object.
    Extract key entities like names, ages, locations, skills, or items.
    CRITICAL: Output ONLY valid JSON. Do not include markdown formatting, backticks, or conversational text.
    User Description: {description}
    """
    prompt = PromptTemplate.from_template(template)
    chain = prompt | llm
    response = chain.invoke({"description": user_description})
    return response.strip()
if __name__ == "__main__":
    print("🤖 AI JSON Generator (Local via Ollama)")
    print("-" * 40)
    sample_text = "My name is Bhavya, I'm a 22-year-old Design Engineer living in Mumbai. I know Python, Figma, and Framer."
    print(f"Input Text: \n{sample_text}\n")
    print("Processing...\n")
    json_output = generate_structured_json(sample_text)
    print("Generated JSON:")
    print(json_output)