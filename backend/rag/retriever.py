from langchain_chroma import Chroma
from backend.rag.embeddings import get_embedding_model

DB_PATH = "database/chroma_db"


def get_retriever():

    embeddings = get_embedding_model()

    db = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embeddings
    )

    retriever = db.as_retriever()

    return retriever
