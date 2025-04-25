from . import logger
from langchain.text_splitter import RecursiveCharacterTextSplitter

def text_splitter(pages:list[str], c_size: int = 1000, c_overlap: int = 50) -> list:
    """split a given document into chunks and return the chunks as a list

    Args:
        pages (list[str]): list of document objects to be split
        c_size (int): Maximum number of characters in a chunk
        c_overlap (int): Number of overlapping characters between chunks

    Raises:
        e: any error encountered while splitting

    Returns:
        list: list of chunked document objects
    """
    chunks = []
    if pages:
        try:
            splitter = RecursiveCharacterTextSplitter(chunk_size = c_size,chunk_overlap=c_overlap,
                                                    strip_whitespace = True)
            
            chunks = splitter.split_documents(pages)
            
            logger.info(f'Split {len(pages)} pages into chunks of size {c_size}')
        
        except Exception as e:
            logger.error(e)
            
            raise e
    logger.info(f'Finished splitting of {len(pages)} pages Successfully')
    return chunks