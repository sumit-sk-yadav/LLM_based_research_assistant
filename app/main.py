import asyncio
from scripts.loader import load_all_pdf_files

async def main():
    data_folder = 'data'
    pages = await load_all_pdf_files(data_folder)
    print(f"Total pages loaded {len(pages)}")



if __name__ == "__main__":
    asyncio.run(main())