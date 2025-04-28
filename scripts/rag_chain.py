from scripts.retriever import VectorstoreRetriever
from scripts.utils import build_prompt
import ollama

class RAGChain:
    def __init__(self, vectorstore, model_name="llama3:latest", k=5):
        self.retriever = VectorstoreRetriever(vectorstore, k)
        self.model_name = model_name

    def run(self, query: str) -> str:
        documents = self.retriever.retrieve(query)
        prompt = build_prompt(query, documents)
        response = ollama.chat(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}]
        )
        return response["message"]["content"]