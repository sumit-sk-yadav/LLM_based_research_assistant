from langchain_chroma import Chroma
from scripts.embedding import Embedder
from langchain_ollama import OllamaLLM
from langchain.chains.qa_with_sources.retrieval import RetrievalQAWithSourcesChain

def load_vectorstore(persist_dir: str = "embeddings", model_name:str = "thenlper/gte-small"):
    embedding_fn = Embedder(model_name=model_name)
    
    vector_store = Chroma(persist_directory=persist_dir, embedding_function=embedding_fn)
    
    return vector_store


def retrieve_relevant_documents(query:str, vector_store:Chroma, top_k:int = 5):
    retriever = vector_store.as_retriever(search_kwargs = {"k": top_k})
    
    return retriever.get_relevant_documents(query=query)


def setup_llm_model(llm_model:str = "gemma3"):
    llm = OllamaLLM(model=llm_model, model_kwargs={"temperature": 0.2, "max_length": 512})

    return llm


def retriever_chain_setup(llm, retriever):
    
    return RetrievalQAWithSourcesChain(llm = llm, retriever=retriever, return_source_documents=True)


def retrieve_and_answer(query: str):
    
    vector_store = load_vectorstore()
    
    relevant_docs = retrieve_relevant_documents(query=query, vector_store=vector_store)
    
    llm = setup_llm_model()
    
    qa_chain = retriever_chain_setup(llm, vector_store.as_retriever())
    
    result = qa_chain(query)
    
    answer = result['result']
    sources = result['source_documents']
    
    return answer, sources

