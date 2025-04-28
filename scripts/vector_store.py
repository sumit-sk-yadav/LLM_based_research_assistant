import os
import pickle
from pathlib import Path
from typing import List
from langchain_core.documents import Document
from langchain_chroma import Chroma
from chromadb.config import Settings
from scripts.embedding import Embedder, hash_documents

def embed_and_store(documents:List[Document], 
                    storage_dir:str = "embeddings", 
                    model_name:str = "thenlper/gte-small") -> Chroma:
    """embeds the given information and stores it as a chroma database. creates a hash map to check for changes in the embeddings so as to not redundantly keep recreeating them.

    Args:
        documents (List[Document]): list of documents to be embedded
        storage_dir (str, optional): directory for storing the generated embeddings. Defaults to "embeddings".
        model_name (str, optional): name of the model to be used to createe the embeddings. Defaults to "thenlper/gte-small".

    Returns:
        Chroma: Chroma vector database
    """
    
    os.makedirs(storage_dir, exist_ok=True)
    hash_path = Path(storage_dir)/"hash.pkl"
    present_hash = hash_documents(documents)
    
    if hash_path.exists():
        with open(hash_path, 'rb') as f:
            saved_hash = pickle.load(f)
        
        if saved_hash == present_hash:
            print("Reusing the existing embeddings stored in Chroma")
            return Chroma(persist_directory=storage_dir,
                            embedding_function=Embedder(model_name),
                            client_settings=Settings(persist_directory = storage_dir,
                                anonymized_telemetry=False))
        
    
    print(f"Generating new embeddings using {model_name} and storing in {storage_dir}")
    vectorstore = Chroma.from_documents(documents=documents,
                                        embedding=Embedder(model_name),
                                        persist_directory=storage_dir)
    
    with open(hash_path, 'wb') as f:
        pickle.dump(present_hash, f)
    
    return vectorstore

def load_vectorstore(
    persist_dir: str = "embeddings",
    model_name: str = "thenlper/gte-small"
) -> Chroma:
    """loads a previously stored vector store

    Args:
        persist_dir (str, optional): directory whre the vector store is stored. Defaults to "embeddings".
        model_name (str, optional): namee of the embedding model. Defaults to "thenlper/gte-small".

    Returns:
        Chroma: Chroma database
    """
    return Chroma(
        persist_directory=persist_dir,
        embedding_function=Embedder(model_name),
        client_settings=Settings(persist_directory=persist_dir, anonymized_telemetry=False)
    )