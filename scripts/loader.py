from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from . import logger


async def load_all_pdf_files(folder_path: str) -> list:
    """Fuction to get all PDF Files in a folder and load them using the PyPDFLoader.
    The function creates a list of all the pages across all PDF documents found in the mentioned folder
    Args:
        folder_path (str): the path to the folder where the necessary PDF files are stored

    Returns:
        list: list of all pages from all the PDF documents in the specified folder
    """
    pages = []
    all_pdf_files = list(Path(folder_path).rglob("*.pdf"))# search all pdf files in folder
    if not all_pdf_files:
        logger.warning(f" No PDF file/'s found in {folder_path}")
    
    logger.info(f"Found {len(all_pdf_files)} PDF file/'s in {folder_path}")
    
    for pdf_file in all_pdf_files:
        try:
            loader = PyPDFLoader(pdf_file)
            async for page in loader.alazy_load():
                pages.append(page)
        except Exception as e:
            logger.error(e)
    
    logger.info(f'Finished loading PDF files from {folder_path}. Total pages loaded: {len(pages)}')
    return pages
