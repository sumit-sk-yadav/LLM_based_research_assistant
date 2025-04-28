import hashlib
from typing import List
from langchain_core.documents import Document
from sentence_transformers import SentenceTransformer
from langchain.embeddings.base import Embeddings

#create an embedding class
class Embedder(Embeddings):
    """ class for creation of the embeddings"""
    def __init__(self, model_name:str = "thenlper/gte-small"):
        self.model = SentenceTransformer(model_name)
    
    def embed_documents(self, texts):
        """ encodes the given text based on the given model"""
        return self.model.encode(texts, show_progress_bar=True, convert_to_numpy=True).tolist()
    
    def embed_query(self, text):
        return self.model.encode(text, convert_to_numpy=True).tolist()


#function to hash the documents
def hash_documents(documents: List[Document]) -> str:
    """hash the document given as input

    Args:
        documents (List[Document]): list containing document type objects

    Returns:
        str: hashed string for the list
    """
    hasher = hashlib.sha256()
    for doc in documents:
        hasher.update(doc.page_content.encode("utf-8"))
    return hasher.hexdigest()


