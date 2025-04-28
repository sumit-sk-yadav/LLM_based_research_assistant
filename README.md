📚 Study Assistant

An intelligent Retrieval-Augmented Generation (RAG) application designed to assist with studying documents.
It loads PDFs, splits and embeds the content, stores embeddings using ChromaDB, and answers user queries using an LLM (Llama 3) enhanced with retrieval capabilities.


LLM_BASED_RESEARCH_ASSISTANT/
├── data/                   # Raw PDF files
├── embeddings/             # Stored vector database (ChromaDB)
├── scripts/
│   ├── loader.py           # Logic to load PDFs into memory
│   ├── splitter.py         # Chunking long text into manageable pieces
│   ├── embedding.py         # Embedding generation using Sentence Transformers
│   ├── vector_store.py     # Embedding storage and retrieval (Chroma)
│   ├── retriever.py        # Retrieving relevant documents
│   ├── rag_chain.py        # RAG pipeline combining retriever + LLM
│   └── utils.py            # Helper functions and configurations
├── app/
│   └── main.py             # CLI Application Entry Point
├── .gitignore
├── requirements.txt
└── README.md

⚙️ How It Works

run ''' python -m app.main '''

What it will do:

1. Prepare Data

Load the PDF files, split them into smaller chunks, and generate embeddings.

Steps:

    Load all PDFs from the data/ folder.

    Split the content into manageable text chunks.

    Compute embeddings using a SentenceTransformer (thenlper/gte-small).

    Store the embeddings into a persistent ChromaDB database in embeddings/.

2. Start Querying

Once embeddings are ready, the querying can be started.

This will:

    Load the persisted vectorstore from disk.

    Initialize the RAG pipeline.

    Allow you to enter natural language questions.

    Retrieve relevant document chunks and generate answers using an LLM (Llama 3 via Ollama).


🛠️ Technologies Used

    Python 3.12.10

    Ollama (llama3.2 model via local inference)

    SentenceTransformers for embedding generation

    ChromaDB for vector database management

    LangChain (core abstractions for documents, embeddings, retrieval)

    AsyncIO for efficient PDF loading

🔮 Planned Extensions

    Tool-Enhanced RAG: Integrate external tools (e.g., calculators, search APIs).

    Streaming Outputs: Display LLM answers as they are generated.

    Web UI: Interactive front-end with Streamlit or FastAPI.

    Multi-Model Support: Switch between different LLMs easily (Mistral, GPT-NeoX, etc.).