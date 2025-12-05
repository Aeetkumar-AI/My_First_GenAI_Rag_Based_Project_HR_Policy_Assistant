# chunking.py
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def split_into_chunks(text: str):
    """Split text into meaningfully sized chunks."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_text(text)
    return [Document(page_content=chunk) for chunk in chunks]
