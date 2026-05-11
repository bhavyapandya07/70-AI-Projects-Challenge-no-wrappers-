import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# 1. Training Data (Small dataset for the vibe)
# We train the model to distinguish between "Technical" and "Gaming" talk
X = [
    "How to fix a python bug", "git push origin main", "VS Code is my favorite IDE",
    "Genshin Impact new update", "Counter-Strike 2 competitive play", "Xbox Game Pass is worth it"
]
y = ["Technical", "Technical", "Technical", "Gaming", "Gaming", "Gaming"]

# 2. Build the Machine Learning Pipeline
# Tfidf turns words into numbers; LogisticRegression classifies them.
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression())
])

model.fit(X, y)

# 3. Streamlit UI
st.title("⚖️ Day 12: AI Text Classifier")
st.write("I'll guess if your text is **Technical** or **Gaming** related.")

user_text = st.text_input("Enter a sentence:")

if user_text:
    prediction = model.predict([user_text])[0]
    st.subheader(f"Prediction: {prediction}")