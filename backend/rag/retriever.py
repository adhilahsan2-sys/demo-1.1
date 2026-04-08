from langchain_chroma import Chroma
from rag.embeddings import get_embedding_model
from utils.logger import log_event   # ✅ IMPORT LOGGER

DB_PATH = "database/chroma_db"


# ✅ STEP 1: Create retriever (NO CHANGE)
def get_retriever():

    embeddings = get_embedding_model()

    db = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embeddings
    )

    retriever = db.as_retriever()

    return retriever


# ✅ STEP 2: Retrieval WITH logging (NEW FUNCTION)
def retrieve_with_logging(query, session_id="default"):

    # Get retriever
    retriever = get_retriever()

    # Retrieve documents
    docs = retriever.get_relevant_documents(query)

    # Extract content
    context = [doc.page_content for doc in docs]

    # 🔥 LOG USER QUERY
    log_event("USER_QUERY", query, session_id)

    # 🔥 LOG RETRIEVED DOCUMENTS
    log_event("RETRIEVED_CONTEXT", context, session_id)

    return context