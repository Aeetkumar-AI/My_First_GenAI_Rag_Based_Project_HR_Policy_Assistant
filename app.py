import streamlit as st
from src.rag_pipeline import build_rag_pipeline, ask_question

st.set_page_config(page_title="Enterprise HR Assistant (RAG-powered) for IIM Ahmedabad", page_icon="📘", layout="wide")
st.title("Enterprise HR Assistant (RAG-powered)")

# 🔹 Cache the pipeline so embeddings are not recomputed
@st.cache_resource
def cached_rag_pipeline(path):
    return build_rag_pipeline(path)

uploaded_file = st.file_uploader("Upload HR PDF", type=["pdf"])

if uploaded_file:
    # Save uploaded PDF
    with open("uploaded.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("PDF uploaded!")

    # 🔥 Cached pipeline load
    retriever, llm = cached_rag_pipeline("uploaded.pdf")
    st.success("RAG Pipeline Ready!")

    question = st.text_input("Ask any HR policy question")

    if st.button("Ask") and question:
        answer = ask_question(retriever, llm, question)
        st.write("### Answer:")
        st.write(answer)
