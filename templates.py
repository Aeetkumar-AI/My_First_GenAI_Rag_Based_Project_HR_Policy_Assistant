import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


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

for file_path in list_of_files:
   filepath = Path(file_path)
   filedir, filename = os.path.split(filepath)

   if filedir != "":
         os.makedirs(filedir, exist_ok=True)
         logging.info(f"Created directory: {filedir}")

   if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Created emptyfile: {filepath}")

   else:
        logging.info(f"File already exists and is not empty: {filepath}")

