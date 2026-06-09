from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
# from core_rag import query_documents
from app.core_rag import query_documents  

app = FastAPI(
    title="GenAI Document Intelligence API",
    description="Asynchronous backend engine for document semantic analysis"
)

@app.get("/")
def read_root():
    """
    Triggers automatically when visiting http://127.0.0.1:8000 
    to confirm the API layer is active.
    """
    return {
        "status": "Success",
        "message": "API engine is working actively!",
        "version": "1.0.0"
    }


class ChatPayload(BaseModel):
    message: str


@app.post("/chat")
def chat_with_ai(payload: ChatPayload):
    """
    Receives the text from Streamlit, fires the RAG loop, 
    and returns the verified context answer.
    """
    try:
        # Pass the extracted payload string into your engine function
        answer = query_documents(payload.message)
        return {"response": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




@app.post("/ingest")
def ingest_data():
    """
    Yeh endpoint frontend se call hoga aur data/ folder ki 
    saari PDFs ko read karke ChromaDB banayega.
    """
    try:
        from app.core_rag import ingest_documents
        ingest_documents()  
        return {"status": "Success", "message": "Database built successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))