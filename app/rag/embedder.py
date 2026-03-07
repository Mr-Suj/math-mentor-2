from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-small-en")

def embed_text(text: str):
    return model.encode(text).tolist()