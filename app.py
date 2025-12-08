# Importing necessary libraries
# Import Streamlit for web app interface
import streamlit as st
from src.rag_pipeline import build_rag_pipeline, ask_question

from dotenv import load_dotenv
load_dotenv()
import os

st.set_page_config(page_title="Enterprise HR Assistant (RAG-powered)", page_icon="📘", layout="wide")
st.title("Enterprise HR Assistant (RAG-powered)")

# # 🔹 Cache the pipeline so embeddings are not recomputed
@st.cache_resource
def cached_rag_pipeline(path):
    return build_rag_pipeline(path)

# Provide file uploader for PDF documents
uploaded_file = st.file_uploader("Upload HR PDF", type=["pdf"])

if uploaded_file:
    # Save uploaded PDF
    base_dir = os.path.dirname(os.path.abspath(__file__))
    upload_folder= os.path.join(base_dir, "uploaded_docs")
    os.makedirs(upload_folder, exist_ok=True)
    save_path = os.path.join(upload_folder, uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

#     # with open("uploaded.pdf", "wb") as f:
#     #     f.write(uploaded_file.getbuffer())

    st.success("PDF uploaded!")

    # 🔥 Cached pipeline load
    # retriever, llm = cached_rag_pipeline("uploaded.pdf")
    retriever, llm = cached_rag_pipeline(save_path) 
    st.success("RAG Pipeline Ready!")

    question = st.text_input("Ask any HR policy question")

    if st.button("Ask") and question:
        answer = ask_question(retriever, llm, question)
        st.write("### Answer:")
        st.write(answer)
