import os
from langchain_ollama import OllamaLLM 
from langchain_core.prompts import PromptTemplate

def generate_blog(topic):
    llm = OllamaLLM(model="llama3.2:1b") 
    template = """
    You are an expert design blogger and Framer Partner. 
    Write a high-energy, professional blog post about: {topic}.
    
    Format in Markdown with:
    - Catchy H1 Title
    - Intro, Body (H2), and Conclusion
    - 3 Key Takeaways
    """
    prompt = PromptTemplate.from_template(template)
    chain = prompt | llm
    print(f"🚀 Generating blog for: {topic}...")
    try:
        response = chain.invoke({"topic": topic})
        os.makedirs("output", exist_ok=True)
        filename = f"output/framer_update_blog.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(response)
        print(f"✅ Success! Blog saved to {filename}")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("👉 Remember to start the Ollama Desktop App first!")
if __name__ == "__main__":
    user_topic = input("Enter blog topic: ")
    generate_blog(user_topic)