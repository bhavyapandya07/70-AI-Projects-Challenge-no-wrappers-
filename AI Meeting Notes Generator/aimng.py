import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate

st.set_page_config(page_title="AI Meeting Notes", page_icon="📝", layout="centered")
st.title("📝 AI Meeting Notes Generator")
st.write("Turn raw meeting transcripts into structured notes, action items, and decisions.")
st.sidebar.markdown("### Settings")
model_name = "llama3.2:1b"
prompt_template = PromptTemplate.from_template(
    """You are a highly efficient executive assistant. Read the following meeting transcript and extract the key information into structured notes.
    Please format the output exactly as follows:
    ## 📌 Executive Summary
    (Provide a brief 1-2 paragraph summary of the meeting)
    ## 🎯 Key Decisions
    (List the major decisions made as bullet points)
    ## ✅ Action Items
    (List specific tasks, who is responsible for them, and deadlines if mentioned)
    Transcript: 
    {transcript}
    Meeting Notes:"""
)
transcript_input = st.text_area("Paste the meeting transcript here:", height=250)
if st.button("Generate Notes"):
    if transcript_input.strip():
        with st.spinner(f"Analyzing transcript with {model_name}..."):
            try:
                llm = Ollama(model=model_name)
                formatted_prompt = prompt_template.format(transcript=transcript_input)
                response = llm.invoke(formatted_prompt)
                st.success("Notes Generated Successfully!")
                st.markdown(response)
            except Exception as e:
                st.error(f"Error connecting to Ollama. Ensure Ollama is running in the background.\n\nDetails: {e}")
    else:
        st.warning("Please paste a transcript to generate notes.")