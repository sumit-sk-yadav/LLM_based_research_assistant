from scripts.retriever import VectorstoreRetriever
from scripts.utils import build_prompt
import ollama

class RAGChain:
    """Rag chain"""
    def __init__(self, vectorstore, model_name:str="llama3.2", k=5):
        self.retriever = VectorstoreRetriever(vectorstore, k) # retrieves the vector store 
        self.model_name = model_name

    def run(self, query: str) -> str:
        documents = self.retriever.retrieve(query) # retrieves relevant info from vector store
        prompt = build_prompt(query, documents) # creates the prompt based on the template
        response = ollama.chat(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}] # passes the prompt to the llm and gets the response
        )
        return response["message"]["content"] # returns the response of the LLM