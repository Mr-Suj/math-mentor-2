import chromadb
from app.rag.embedder import embed_text

# client = chromadb.Client()
# collection = client.get_or_create_collection(name="math_knowledge")

client = chromadb.PersistentClient(path="data/chroma_db")

collection = client.get_or_create_collection(
    name="math_knowledge"
)

def add_document(doc_id, text):

    embedding = embed_text(text)

    collection.add(
        ids=[doc_id],
        documents=[text],
        embeddings=[embedding]
    )