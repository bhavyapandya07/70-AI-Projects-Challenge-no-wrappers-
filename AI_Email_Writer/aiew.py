import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate

st.set_page_config(page_title="AI Email Writer", page_icon="✉️", layout="centered")
st.title("✉️ AI Email Writer")
st.markdown("Transform a quick idea into a polished, ready-to-send email.")
st.sidebar.header("Model Settings")
model_name = "llama3.2:1b"
email_prompt = PromptTemplate.from_template(
    """You are an expert copywriter and executive assistant. Write a clear, well-structured email based on the following parameters:
    Recipient: {recipient}
    Tone: {tone}
    Core Idea/Message: {idea}
    Ensure the subject line is catchy and appropriate. Do not include any placeholder brackets (like [Your Name]) at the sign-off; just end the email naturally so the user can append their own signature later.
    Drafted Email:"""
)
col1, col2 = st.columns(2)
with col1:
    recipient_input = st.text_input("Who is this email for?", placeholder="e.g., The Marketing Team, John Doe, etc.")
with col2:
    tone_input = st.selectbox("Select the Tone", ["Professional", "Casual", "Persuasive", "Urgent", "Friendly"])
idea_input = st.text_area(
    "What is the main idea of the email?", 
    value="Write a follow-up email to the sponsors of the Star Promptathon at Ramnarain Ruia College, thanking them for their support and sharing the success metrics of the event.",
    height=150
)
if st.button("Draft Email", type="primary"):
    if idea_input.strip() and recipient_input.strip():
        with st.spinner(f"Drafting with {model_name}..."):
            try:
                llm = Ollama(model=model_name)
                formatted_prompt = email_prompt.format(
                    recipient=recipient_input,
                    tone=tone_input,
                    idea=idea_input
                )
                drafted_email = llm.invoke(formatted_prompt)
                st.success("Email Drafted Successfully!")
                st.markdown("### Your Output:")
                st.info(drafted_email)
            except Exception as e:
                st.error(f"Error connecting to Ollama. Ensure the Ollama app is running locally.\n\nDetails: {e}")
    else:
        st.warning("Please fill in both the Recipient and the Core Idea fields.")