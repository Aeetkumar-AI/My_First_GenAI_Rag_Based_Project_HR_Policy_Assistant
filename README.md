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


## Git Command
```bash
git status
```

```bash
git add .
```

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

