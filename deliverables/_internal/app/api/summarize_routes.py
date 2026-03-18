from fastapi import APIRouter, HTTPException

from app.schemas.llm_schema import SummarizeRequest
from app.services.summarize_service import summarize_text


router = APIRouter(tags=["LLM"])


@router.post(
    "/llm/summarize",
    summary="Summarize text",
    description="Generate a concise summary for the provided text using the local LLM."
)
def summarize(request: SummarizeRequest):

    if not request.text.strip():
        raise HTTPException(
            status_code=400,
            detail="Text cannot be empty"
        )

    try:
        summary = summarize_text(request.text)

        return {
            "summary": summary
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Summarization failed: {str(e)}"
        )