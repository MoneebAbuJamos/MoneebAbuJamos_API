from fastapi import APIRouter, UploadFile, File, HTTPException

from app.schemas.llm_schema import RAGQueryRequest
from app.services.rag_service import ingest_document, query_documents


router = APIRouter(tags=["RAG"])


@router.post(
    "/rag/upload",
    summary="Upload document for RAG",
    description="Upload a TXT, PDF, or DOCX document to be indexed into the vector database."
)
async def upload_document(file: UploadFile = File(...)):

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="File must have a name"
        )

    if not file.filename.endswith((".txt", ".pdf", ".docx")):
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type"
        )

    try:
        content = await file.read()

        if not content:
            raise HTTPException(
                status_code=400,
                detail="Uploaded file is empty"
            )

        result = ingest_document(file.filename, content)

        return {
            "message": "Document processed",
            "filename": file.filename,
            "chunks": result
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Document ingestion failed: {str(e)}"
        )


@router.post(
    "/rag/query",
    summary="Ask question about documents",
    description="Query the vector database and generate an answer using the local LLM."
)
def query(request: RAGQueryRequest):

    if not request.question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty"
        )

    try:
        answer = query_documents(request.question)

        return answer

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"RAG query failed: {str(e)}"
        )