import os
from app.rag.vector_store import add_document

KB_PATH = "data/knowledge_base"


def load_knowledge():

    for file in os.listdir(KB_PATH):

        with open(os.path.join(KB_PATH, file), "r") as f:
            text = f.read()
        print(f"loaded {file}")
        
        add_document(file, text)


if __name__ == "__main__":
    load_knowledge()