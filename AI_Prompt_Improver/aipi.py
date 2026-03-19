from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

def improve_prompt(vague_prompt):
    llm = OllamaLLM(model="llama3.2:1b")
    template = """
    You are an expert Prompt Engineer. Your task is to take a simple or vague user prompt and rewrite it to be highly effective for an AI.
    Original Prompt: {vague_prompt}
    Provide the improved version using the structure:
    1. Role: (Who should the AI be?)
    2. Context: (Background info)
    3. Task: (Specific instructions)
    4. Format: (Desired output style)
    Improved Prompt:
    """
    prompt_template = PromptTemplate.from_template(template)
    chain = prompt_template | llm
    print("\n✨ Refining your prompt...")
    result = chain.invoke({"vague_prompt": vague_prompt})
    print("\n--- IMPROVED PROMPT ---")
    print(result)
if __name__ == "__main__":
    raw_input = input("Enter a basic prompt: ")
    improve_prompt(raw_input)