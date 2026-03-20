import streamlit as st
import PyPDF2
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate

llm = Ollama(model="llama3.2:1b")
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"
    return text
def analyze_resume(resume_text):
    template = """
    You are an expert Tech Recruiter and ATS (Applicant Tracking System) optimizer.
    Analyze the following resume text and provide constructive feedback.
    Format your response clearly with the following sections:
    1. Overall Impression
    2. Key Strengths
    3. Areas for Improvement
    4. ATS Optimization Tips
    Resume Text:
    {resume}
    """
    prompt = PromptTemplate.from_template(template)
    chain = prompt | llm
    return chain.invoke({"resume": resume_text})
st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="centered")
st.title("📄 AI Resume Analyzer")
st.markdown("Upload your resume (PDF) and get instant feedback from a local AI recruiter.")
uploaded_file = st.file_uploader("Upload your Resume (PDF format)", type=["pdf"])
if uploaded_file is not None:
    st.success("File uploaded successfully!")
    with st.spinner("Extracting text and analyzing... This might take a moment depending on your local machine."):
        resume_content = extract_text_from_pdf(uploaded_file)
        if not resume_content.strip():
            st.error("Could not extract text from this PDF. It might be an image-based PDF.")
        else:
            with st.expander("View Extracted Text"):
                st.text(resume_content[:1000] + "...\n[Text Truncated]")
            st.subheader("🤖 AI Feedback")
            feedback = analyze_resume(resume_content)
            st.markdown(feedback)