import ollama
import sys

def main():
    print("========================================")
    print("🤖 Welcome to your CLI AI Chatbot!")
    print("Type 'exit' or 'quit' to end the chat.")
    print("========================================\n")

    model_name = "llama3.2:1b"
    messages = []

    while True:
        try:
            user_input = input("👤 You: ")
            if user_input.lower() in ['exit', 'quit']:
                print("🤖 AI: Goodbye! Have a great day.")
                break
            if not user_input.strip():
                continue
            messages.append({'role': 'user', 'content': user_input})
            print("🤖 AI is thinking...", end="\r")
            response = ollama.chat(model=model_name, messages=messages)
            ai_response = response['message']['content']
            messages.append({'role': 'assistant', 'content': ai_response})
            sys.stdout.write("\033[K")
            print(f"🤖 AI: {ai_response}\n")
        except KeyboardInterrupt:
            print("\n🤖 AI: Conversation interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            break

if __name__ == "__main__":
    main()