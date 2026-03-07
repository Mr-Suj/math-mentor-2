from app.rag.vector_store import collection
from app.rag.embedder import embed_text


def retrieve_context(query):

    embedding = embed_text(query)

    results = collection.query(
        query_embeddings=[embedding],
        n_results=2
    )

    return results["documents"]