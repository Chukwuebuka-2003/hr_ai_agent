import streamlit as st
import requests
from PyPDF2 import PdfReader
import io

# Set Streamlit Page Config with Icon
st.set_page_config(
    page_title="AI-Powered HR Tools",
    page_icon="🧑‍💼",
    layout="wide"
)

# Backend API URL
BACKEND_URL = "https://ebuka-hrai.onrender.com"
MODEL_NAME = "groq/llama-3.3-70b-versatile"  # Default model name

# Streamlit App with Tabs
st.title("AI Agent Powered HR Tools")
tab1, tab2 = st.tabs(["Resume Reviewer", "HR Question Assistant"])

# Sidebar with Example HR Questions
st.sidebar.title("Example HR Questions")
example_questions = [
    "What are the best practices for conducting a job interview?",
    "How should I negotiate my salary?",
    "What is the proper format for a resignation letter?",
    "How do I handle workplace conflicts professionally?",
    "What are the top skills employers look for in 2024?"
]
selected_question = st.sidebar.radio("Choose an example question:", options=example_questions)

# Tab 1: Resume Reviewer
with tab1:
    st.header("Resume Reviewer")
    st.write("Upload your resume to receive detailed feedback.")

    uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])

    if uploaded_file:
        st.subheader("AI Feedback")
        with st.spinner("Sending resume to backend for analysis..."):
            try:
                files = {'file': (uploaded_file.name, uploaded_file, uploaded_file.type)}
                data = {'model_name': MODEL_NAME}

                response = requests.post(
                    f"{BACKEND_URL}/resume",
                    files=files,
                    data=data
                )

                if response.status_code == 200:
                    result = response.json().get("result", "No feedback received")
                    st.write(result)
                else:
                    st.error(f"Error from backend: {response.status_code}, {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Request failed: {e}")

# Tab 2: HR Question Assistant
with tab2:
    st.header("HR Question Assistant")
    st.write("Ask any HR-related questions, and the AI will provide professional advice.")

    question = st.text_input("Enter your HR-related question:", value=selected_question)

    if question.strip():
        st.subheader("AI Response")
        with st.spinner("Sending your question to backend..."):
            try:
                response = requests.post(
                    f"{BACKEND_URL}/hr",
                    json={
                        "question": question,
                        "model_name": MODEL_NAME
                    }
                )

                if response.status_code == 200:
                    result = response.json().get("result", "No answer received")
                    st.write(result)
                else:
                    st.error(f"Error from backend: {response.status_code}, {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Request failed: {e}")
