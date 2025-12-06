# llm.py
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()


# llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)  # gpt-5-pro-2025-10-06,gpt-4.1-2025-04-14, gpt-3.5-turbo-0125
# llm = ChatOpenAI(model="gpt-5.1-2025-11-13", temperature=0)

def get_llm():
    """Return OpenAI LLM."""
    return ChatOpenAI(
        model="gpt-4o-mini",  # or gpt-5
        temperature=0.2
    )
