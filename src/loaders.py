# loaders.py
import pdfplumber

def load_document(file_path: str) -> str:
    """Load a PDF file and return extracted text."""
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"
    return text.strip()
