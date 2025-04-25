import asyncio
from scripts.loader import load_all_pdf_files
from scripts.splitter import text_splitter

async def main():
    data_folder = 'data'
    pages = await load_all_pdf_files(data_folder)
    print(f"Total pages loaded {len(pages)}")

    chunks = text_splitter(pages = pages)
    print(f"Total number of chunks: {len(chunks)}")


if __name__ == "__main__":
    asyncio.run(main())