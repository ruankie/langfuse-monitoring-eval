import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents.base import Document
from langchain_core.vectorstores import VectorStoreRetriever


PWD = os.path.dirname(os.path.abspath(__file__))
HF_EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
LOCAL_VECTORSTORE_PATH = os.path.join(PWD, "vectorstore/.chroma_db")
LOCAL_EMBEDDING_MODEL_SAVE_PATH = os.path.join(PWD, f"./embedding_model/{HF_EMBEDDING_MODEL_NAME}")
URLS = [
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
    "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
]


def _get_web_page_as_chunks(url: str) -> list[Document]:
    """
    Given a web page URL, load its contents and return
    a list of chunks of its contents.
    """
    docs = [WebBaseLoader(url).load() for url in URLS]
    docs_list = [item for sublist in docs for item in sublist]

    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=250, chunk_overlap=0
    )
    doc_splits = text_splitter.split_documents(docs_list)
    return doc_splits


def _add_docs_to_vectorstore(documents: list[Document]) -> Chroma:
    """
    Use the embedding model to embed the input documents and
    populate the vectorstore. Save populated vectorstore to disk
    and return populated vectorstore.
    """
    # Load embedding model
    print(f"Loading embedding model {HF_EMBEDDING_MODEL_NAME}")
    embedding_function = HuggingFaceEmbeddings(
        cache_folder=LOCAL_EMBEDDING_MODEL_SAVE_PATH, model_name=HF_EMBEDDING_MODEL_NAME
    )

    # Populate vectorstore with embeddings
    print("Populating vectorstore")
    vectorstore = Chroma.from_documents(
        documents=documents,
        collection_name="rag-chroma",
        embedding=embedding_function,
        persist_directory=LOCAL_VECTORSTORE_PATH,
    )

    return vectorstore


# TODO: separate ingest from load existing vectorstore
def get_populated_blog_vectorstore() -> VectorStoreRetriever:
    """
    Ingest the content of a list of blog URLs and return a usable vectorstore.

    Returns:
        VectorStoreRetriever: A populated vectorstore that can be used to
            retrieve relevant docs.

    Example:
        ```py
        retriever = get_populated_blog_vectorstore()
        documents = retriever.get_relevant_documents(question)
        ```
    """
    # Get website content as text chunks
    docs = []
    for url in URLS:
        docs += _get_web_page_as_chunks(url)

    # Add docs to vectorstore
    vectorstore = _add_docs_to_vectorstore(documents=docs)
    return vectorstore.as_retriever()
