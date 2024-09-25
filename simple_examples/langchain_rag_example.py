# For importing custom code
import sys

sys.path.append("../")

# Imports
from knowledge_base.utils import load_blog_vectorstore
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOllama

LOCAL_LLM_NAME = "llama3.1"


def get_rag_chain() -> callable:
    """
    Creates and returns a callable RAG chain.

    The RAG chain will use the provided language model (LLM) and retriever to answer questions
    based on retrieved context.

    Args:
        llm (BaseLLM): A language model instance that will generate answers.
        retriever (BaseRetriever): A retriever instance that will retrieve relevant documents.

    Returns:
        callable: A callable RAG chain function that takes a string input and returns the generated answer.

    Example:
        rag_chain = get_rag_chain(llm, retriever)
        response = rag_chain("What is LangChain?")
    """
    # LLM config
    llm = ChatOllama(model=LOCAL_LLM_NAME, temperature=0)

    # Vectorstore config
    retriever = load_blog_vectorstore()

    # Create a RetrievalQA chain using the provided retriever and LLM
    rag_chain = RetrievalQA.from_llm(
        llm=llm, retriever=retriever
    )

    # Return the callable chain
    return rag_chain
