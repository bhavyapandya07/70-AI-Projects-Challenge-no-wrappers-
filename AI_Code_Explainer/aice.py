from huggingface_hub import InferenceClient

hf_token = "token" 
client = InferenceClient(api_key=hf_token)

def explain_code(code_snippet):
    print("\n🤖 Analyzing your code...")
    prompt = f"You are a helpful programming tutor. Explain the following code simply and concisely:\n\n{code_snippet}"
    try:
        response = client.chat.completions.create(
            model="Qwen/Qwen2.5-Coder-32B-Instruct", 
            messages=[{"role": "user", "content": prompt}],
            max_tokens=400
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    sample_code = """
    your test code here
    """
    print("Code to explain:")
    print(sample_code.strip())
    print("-" * 40)
    explanation = explain_code(sample_code)
    print("\nExplanation:\n", explanation)