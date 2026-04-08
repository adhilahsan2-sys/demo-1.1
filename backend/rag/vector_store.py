from langchain_chroma import Chroma
from rag.embeddings import get_embedding_model

DB_PATH = "database/chroma_db"


def store_resume_chunks(chunks):

    embeddings = get_embedding_model()

    db = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        persist_directory=DB_PATH
    )

    print("Resume embeddings stored successfully!")

    return db