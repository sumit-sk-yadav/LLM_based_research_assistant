import os
import pickle
from pathlib import Path
from typing import List
from langchain_core.documents import Document
from langchain_chroma import Chroma
from chromadb.config import Settings
from scripts.embedding import Embedder, hash_documents
from . import logger

def embed_and_store(documents:List[Document], 
                    storage_dir:str = "embeddings", 
                    model_name:str = "thenlper/gte-small") -> Chroma:
    
    os.makedirs(storage_dir, exist_ok=True)
    hash_path = Path(storage_dir)/"hash.pkl"
    present_hash = hash_documents(documents)
    
    if hash_path.exists():
        with open(hash_path, 'rb') as f:
            saved_hash = pickle.load(f)
        
        if saved_hash == present_hash:
            print("Reusing the existing embeddings stored in Chroma")
            logger.info("Previously existing embeddings found")
            return Chroma(persist_directory=storage_dir,
                            embedding_function=Embedder(model_name),
                            client_settings=Settings(persist_directory = storage_dir,
                                anonymized_telemetry=False))
        
    
    print(f"Generating new embeddings using {model_name} and storing in {storage_dir}")
    logger.info("Generating new embeddings. No previously existing embeddings found")
    vectorstore = Chroma.from_documents(documents=documents,
                                        embedding=Embedder(model_name),
                                        persist_directory=storage_dir)
    
    with open(hash_path, 'wb') as f:
        pickle.dump(present_hash, f)
    
    return vectorstore