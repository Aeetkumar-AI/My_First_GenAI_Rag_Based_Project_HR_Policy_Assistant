# llm.py
from langchain_openai import ChatOpenAI

def get_llm():
    """Return OpenAI LLM."""
    return ChatOpenAI(
        model="gpt-4o",  # or gpt-5
        temperature=0.2
    )
