# vectorstore.py
import os
from langchain_community.vectorstores import FAISS

def get_vectorstore(docs, embeddings, db_dir):
    os.makedirs(db_dir, exist_ok=True)
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local(db_dir)
    return vectorstore

def load_vectorstore(embeddings, db_dir):
    if not os.path.exists(db_dir):
        raise FileNotFoundError("Vectorstore not found.")
    return FAISS.load_local(db_dir, embeddings, allow_dangerous_deserialization=True)

def get_retriever(vectorstore):
    return vectorstore.as_retriever(search_kwargs={"k": 5})
