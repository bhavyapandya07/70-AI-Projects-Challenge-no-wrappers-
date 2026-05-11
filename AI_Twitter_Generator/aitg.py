import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate # Fixed import

# Initialize the local model
llm = OllamaLLM(model="llama3.2")

st.set_page_config(page_title="AI Thread Generator", page_icon="🐦")
st.title("🐦 AI Twitter Thread Generator")

topic = st.text_area("What's the thread about?", placeholder="e.g. The future of AI Agents in 2026")
tone = st.selectbox("Tone", ["Professional", "Hype", "Educational", "Witty"])

if st.button("Generate Thread"):
    if topic:
        with st.spinner("Writing your thread..."):
            template = """
            You are an expert Twitter ghostwriter. Create a 5-tweet thread about: {topic}.
            The tone should be {tone}. 
            Each tweet must be numbered (1/5, 2/5, etc.) and include relevant emojis.
            Ensure the first tweet is a 'hook' to grab attention.
            """
            prompt = PromptTemplate.from_template(template)
            chain = prompt | llm
            
            response = chain.invoke({"topic": topic, "tone": tone})
            st.markdown(response)
    else:
        st.warning("Please enter a topic!")