# embeddings.py
from langchain_openai import OpenAIEmbeddings

def get_embeddings():
    """Return OpenAI embeddings."""
    return OpenAIEmbeddings(model="text-embedding-3-large")
