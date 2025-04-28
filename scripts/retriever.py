class VectorstoreRetriever:
    def __init__(self, vectorstore, k: int = 5):
        self.vectorstore = vectorstore
        self.k = k

    def retrieve(self, query: str):# retrieves from the vector store
        return self.vectorstore.similarity_search(query, k=self.k)
