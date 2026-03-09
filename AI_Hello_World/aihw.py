import ollama
import sys

def chat_with_ai():
    print("🤖 AI Hello World Initialized!")
    print("--------------------------------")
    
    model_name = "llama3.2:1b"
    user_prompt = "Explain what an LLM is to a 10-year-old in exactly two sentences."
    
    print(f"👱🏻 You: {user_prompt}\n")
    print(f"🤖 {model_name} is thinking...\n")
    
    try:
        response = ollama.chat(model=model_name, messages=[
            {
                'role': 'user',
                'content': user_prompt,
            },
        ])
        ai_response = response['message']['content']
        print(f"🤖 AI: {ai_response}")
        
    except Exception as e:
        print(f"\n❌ Error: Could not connect to Ollama. ")
        print(f"Make sure you have downloaded Ollama and ran 'ollama run {model_name}' in your command prompt first!")
        print(f"Detailed error: {e}")

if __name__ == "__main__":
    chat_with_ai()