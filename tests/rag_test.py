from app.rag.retriever import retrieve_context

# query = "Find Probability: P(A ∪ B)"
query = "Find derivative of x^2"
docs = retrieve_context(query)

print(docs)