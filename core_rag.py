import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda

# Load environment variables 
load_dotenv()

# Global configuration variables
DATA_DIR = "/backend/data"
PERSIST_DIR = "/backend/chroma_db"
COLLECTION_NAME = "sample"


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CHROMA_PATH = os.path.abspath(os.path.join(CURRENT_DIR, "..", "chroma_db"))


# Define the Prompt Framework globally
prompt = PromptTemplate(
    template="""
    You are a helpful assistant.
    Answer ONLY from the provided document context.
    If the context is insufficient, just say you don't know.

    Context:{context}
    Question: {question}
    """,
    input_variables=['context', 'question']
)


def ingest_documents():
    """
    Step 1, 2 & 3: Document Indigestion and splitting data into chunks then storing in vector store i.e. ChromaDB.
    """
    if not os.path.exists(DATA_DIR):
        print(f"Error: The directory '{DATA_DIR}' does not exist.")
        return

    print("Loading documents from directory...")
    loader = PyPDFDirectoryLoader(DATA_DIR)
    chunks = loader.load()

    # Split the documents into smaller chunks to fit into the embedding model's context window
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    split_chunks = text_splitter.split_documents(chunks)

    print(f"Generated {len(split_chunks)} chunks. Generating embeddings...")
    embedding_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2")

    # Store the chunks and their embeddings in ChromaDB
    vector_store = Chroma.from_documents(
        documents=split_chunks,
        embedding=embedding_model,
        persist_directory=PERSIST_DIR,
        collection_name=COLLECTION_NAME
    )
    print("Success: ChromaDB has been built and saved locally!")


def _format_docs(retrieved_docs):
    """Helper function to combine the pieces of text together"""
    return "\n\n".join(doc.page_content for doc in retrieved_docs)


def query_documents(user_question: str) -> str:
    """
    Step 5 & 6: Run this every time a user asks a question.
    It reads from the already-saved database without reloading PDFs.
    """
    # 1. Re-connect to the existing database on your hard drive
    embedding_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2")
    vector_store = Chroma(
        persist_directory=PERSIST_DIR,
        embedding_function=embedding_model,
        collection_name=COLLECTION_NAME
    )
    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

    # 2. Set up the LLM
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)

    # 3. Build your LCEL chain (exactly how you wrote it)
    parallel_chain = RunnableParallel({
        'context': retriever | RunnableLambda(_format_docs),
        'question': RunnablePassthrough()
    })
    parser = StrOutputParser()
    main_chain = parallel_chain | prompt | llm | parser

    # 4. Fire the query and return the answer string
    return main_chain.invoke(user_question)


# --- Local Testing Block ---
if __name__ == "__main__":
    # If it's your first time running it, uncomment the line below to build your DB:
    # ingest_documents()
    
    # Test your query function
    output = query_documents("What is generative ai?")
    print("\n--- Answer ---")
    print(output)

