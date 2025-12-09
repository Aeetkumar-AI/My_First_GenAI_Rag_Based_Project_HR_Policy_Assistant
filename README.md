# My_First_GenAI_Rag_Based_Project_HR_Policy_Assistant

# Project Structure
```bash
Clinical-ChatBot-App-MediBuddy/
│
├── src/
│   ├── __init__.py
│   ├── loaders.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vectorstore.py
│   ├── llm.py
│   └── rag_pipeline.py
│
├── config/
│   └── config.yaml
│
├── data/
│   └── sample_pdfs/
│
├── exploration/
│   └── notebook.ipynb
│
├── Project_Preparation/
│   └── README.md
│
├── .env
├── requirements.txt
├── setup.py
└── app.py

## Create Folder Structure using templates.py

```bash
list_of_files = [
    "src/__init__.py",
    "src/embeddings.py",
    "src/loaders.py",
     "src/chunking.py",
    "src/vectorstore.py",
    "src/rag_pipeline.py",
    "src/llm.py",
    "config/config.yaml",
    ".env",
    "setup.py",
    "requirements.txt",
    "app.py",
    "exploration/notebook.ipynb",
    "data/sample_pdfs/.gitkeep",
    "Project_Preparation/README.md",
    ".gitignore",
]
```
## Create virtual Env -- Isolated Env for Installing project dependency/packages

```bash
python -m venv venv
```
## Activate Environment
```bash
venv\Scripts\activate.bat
```

## Deactivate Virtual Enviroment
```bash
venv\Scripts\deactivate.bat
```
## Update requirements.txt file as per required packages
```bash
langchain
langchain-openai
openai
chromadb
python-dotenv
langchain-community
langchain-core
streamlit
langchain-groq
langchain-text-splitters
sentence-transformers
spacy
PyPDF2
pdfplumber
faiss-cpu
```
## Install the requirements.txt
```bash
pip install -r requirments.txt
```

## Start bulding exploration notebook -- 
    - give you clear about what are steps need to follow to build this project
    - Explor on diffrent Document loaders
    - Explore on different Chunking
    - explore on diffrent embedding models
    - explore on different vector data base 
    - explore on retrievals 
    - explore on llm models
    - explore on prompt engineering-prompt templates
    - rag pipeline
    - ask question

## Src Code Building
    - loaders.py
    - chunking.py
    - embddings.py
    - vectorstore.py
    - llm.py
    - rag_pipeline.py


## creat app.py
    - streamlit app.py


## To run streamlit application
```bash
streamlit run app.py
```

## Push code to Github


## Prerequisites

- Git and Git Bash installed
- A GitHub account with access to this repository

## 1) Create or locate your SSH key

If you don't have an SSH key, generate one (replace with your email):

```bash
ssh-keygen -t ed25519 -C "<emailid>@gmail.com"     ##ssh-keygen -t ed25519 -C "ajeetkumar.kumar0102@gmail.com"
# Accept defaults (press Enter) to store at ~/.ssh/id_ed25519
```

## 2) Start the ssh-agent and add your key (Git Bash)

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

If you see `Could not open a connection to your authentication agent`, re-run the `eval` line and then `ssh-add` again.

## 3) Copy the public key and add it to GitHub

```bash
cat ~/.ssh/id_ed25519.pub | clip.exe
```

- Open: https://github.com/settings/ssh/new
- Paste the key, give it a title (e.g., "Work laptop - Git Bash"), and save.

If `clip.exe` is not available, run `cat ~/.ssh/id_ed25519.pub` and copy the output manually.

## 4) Verify the SSH connection

```bash
ssh -T git@github.com
```

Expected response on success:

```
Hi <your-username>! You've successfully authenticated, but GitHub does not provide shell access.
```



## Git basics (common commands)

- Stage all changes:

## Git Command
```bash
git status
```

## Track the chages made local 
```bash
git add .
```

## Commit changes to git
```bash
git commit -m"folder tree/strcture created and updated requirements.txt file"
```

## git push local chanages to origin from local branch
```bash
git push origin main
```

# Azure Deployment
```bash
streamlit run app.py --server.port 8000 --server.address 0.0.0.0
```

