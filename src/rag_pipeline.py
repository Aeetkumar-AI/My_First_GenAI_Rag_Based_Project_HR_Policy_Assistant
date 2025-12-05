import os
import hashlib
from src.loaders import load_document
from src.chunking import split_into_chunks
from src.embeddings import get_embeddings
from src.vectorstore import get_vectorstore, load_vectorstore, get_retriever
from src.llm import get_llm
from langchain_core.output_parsers import StrOutputParser

def hash_file(file_path):
    with open(file_path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def build_rag_pipeline(pdf_path):

    embeddings = get_embeddings()
    
    file_hash = hash_file(pdf_path)
    db_dir = f"db/{file_hash}"

    # Load cached FAISS if exists ⏩
    if os.path.exists(db_dir):
        vector_db = load_vectorstore(embeddings, db_dir)
    else:
        text = load_document(pdf_path)
        docs = split_into_chunks(text)
        vector_db = get_vectorstore(docs, embeddings, db_dir)

    retriever = get_retriever(vector_db)
    llm = get_llm()

    return retriever, llm

def ask_question(retriever, llm, query):
    RAG_CHAIN = (
        retriever
        | (lambda docs: "\n\n".join([d.page_content for d in docs]))
        | llm
        | StrOutputParser()
    )
    return RAG_CHAIN.invoke(query)
