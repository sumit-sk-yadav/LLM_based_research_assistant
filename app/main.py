import asyncio
from scripts.loader import load_all_pdf_files
from scripts.splitter import text_splitter
from scripts.vector_store import embed_and_store
from scripts.vector_store import load_vectorstore
from scripts.rag_chain import RAGChain

async def prepare_data():
    data_folder = 'data'
    pages = await load_all_pdf_files(data_folder)
    print(f"Total pages loaded: {len(pages)}")

    chunks = text_splitter(pages=pages)
    print(f"Total number of chunks: {len(chunks)}")
    
    vector_db = embed_and_store(chunks)
    print("Document Embeddings generated and stored.")

def start_rag_app():
    
    vectorstore = load_vectorstore(persist_dir="embeddings")
    rag_chain = RAGChain(vectorstore, model_name="llama3.2")

    print("\n>>>>>>>>>>>> Study Assistant Ready. Ask your questions!<<<<<<<<<<<\n")

    while True:
        query = input("Enter your question (or 'exit()' to quit): ")
        if query.lower() == 'exit()':
            break
        answer = rag_chain.run(query)
        print(f"\nAnswer: {answer}\n")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Study Assistant")
    parser.add_argument("--prepare", action="store_true", help="Prepare data (load PDFs and embed)")
    args = parser.parse_args()

    if args.prepare:
        asyncio.run(prepare_data())
    else:
        start_rag_app()