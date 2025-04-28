def build_prompt(query: str, documents) -> str:
    """builds the prompt for the llm"""
    context = "\n\n".join(doc.page_content for doc in documents)
    return f"""You are a helpful assistant.

Use the following context to answer the user's question.

Context:
{context}

Question:
{query}

Answer:"""