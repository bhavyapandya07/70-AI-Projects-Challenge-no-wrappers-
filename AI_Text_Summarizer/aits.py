from transformers import pipeline

def summarize_text(text):
    print("⏳ Loading local LLM from cache...")
    generator = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")
    print("\n📝 Summarizing text...")
    prompt = f"<|system|>\nYou are a highly accurate AI assistant. Summarize the following text concisely in ENGLISH.</s>\n<|user|>\nSummarize this text: {text}</s>\n<|assistant|>\n"
    result = generator(prompt, max_new_tokens=150, do_sample=True, temperature=0.3)
    generated_text = result[0]['generated_text']
    summary = generated_text.split("<|assistant|>\n")[-1].strip()
    return summary

if __name__ == "__main__":
    article = """
    I'm Bhavya Pandya 👋🏻
    A Designer & AI First Developer
    Also with the magic of no-code & AI, I craft digital melodies that users not only love but also waltz with joy!
    Helping Organizations Create MVPs in 30days with ENFIQ.
    """
    print("Original Text:\n", article.strip())
    print("-" * 50)
    try:
        result = summarize_text(article)
        print("\nSummary:\n", result)
    except Exception as e:
        print(f"An error occurred: {e}")