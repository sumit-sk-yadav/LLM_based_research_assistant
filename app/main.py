import asyncio
from scripts.loader import load_all_pdf_files
from scripts.splitter import text_splitter
from scripts.vector_store import embed_and_store

async def main():
    data_folder = 'data'
    pages = await load_all_pdf_files(data_folder)
    print(f"Total pages loaded {len(pages)}")

    chunks = text_splitter(pages = pages)
    print(f"Total number of chunks: {len(chunks)}")
    
    vector_db = embed_and_store(chunks)
    print("Document Embeddings generated")


if __name__ == "__main__":
    asyncio.run(main())