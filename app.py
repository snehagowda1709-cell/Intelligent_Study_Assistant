import streamlit as st
from agents import StudyAgent
import pdfplumber

st.set_page_config(page_title="Intelligent Study Assistant", layout="wide")
st.title("📚 Intelligent Study Assistant")

# Initialize Gemini Agent
agent = StudyAgent(api_key="AIzaSyDc6XUrniKtRH79PMGbDVebn6-il0SWMTc")

st.write("Upload your PDF notes below, then ask questions!")

# PDF upload
pdf_file = st.file_uploader("Upload your study PDF notes", type=["pdf"])

if pdf_file:
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"

    agent.load_notes(text)
    st.success("PDF loaded successfully!")

# Ask question
query = st.text_input("Ask any study question based on your PDF:")

if query:
    with st.spinner("Generating answer..."):
        response = agent.answer_question(query)

    st.subheader("📘 Answer:")
    st.write(response)
