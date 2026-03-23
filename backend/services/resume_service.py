from backend.utils.file_loader import extract_text_from_pdf
from backend.utils.text_chunker import chunk_text
from backend.rag.vector_store import store_resume_chunks
from backend.llm.groq_client import ask_groq


def summarize_resume(text):

    prompt = f"""
You are an AI career assistant.

Summarize the following resume into 4–5 bullet points highlighting:

- Skills
- Experience
- Education
- Key strengths

Resume:
{text}
"""

    return ask_groq(prompt)


def process_resume(file_path):

    print("Processing resume...")

    # Step 1: Extract text
    text = extract_text_from_pdf(file_path)

    # Step 2: Chunk text
    chunks = chunk_text(text)

    # Step 3: Store embeddings
    store_resume_chunks(chunks)

    # Step 4: Generate AI summary
    summary = summarize_resume(text)

    print("Resume processed successfully!")

    return {
        "chunks": chunks,
        "summary": summary
    }