import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma

DATA_PATH = "data/interview_docs.txt"
DB_PATH = "database/chroma_db"


def load_documents():
    loader = TextLoader(DATA_PATH)
    documents = loader.load()
    return documents


def split_documents(documents):
    text_splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = text_splitter.split_documents(documents)
    return chunks


def create_embeddings():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return embeddings


def create_vector_db(chunks, embeddings):
    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_PATH
    )

    print("Vector database created successfully!")


def main():
    print("Loading documents...")
    documents = load_documents()

    print("Splitting documents...")
    chunks = split_documents(documents)

    print("Creating embeddings...")
    embeddings = create_embeddings()

    print("Creating vector database...")
    create_vector_db(chunks, embeddings)


if __name__ == "__main__":
    main()