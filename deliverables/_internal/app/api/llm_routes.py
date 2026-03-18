from fastapi import APIRouter, HTTPException

from app.schemas.llm_schema import PromptRequest
from app.services.llm_service import generate_response


router = APIRouter(tags=["LLM"])


@router.post(
    "/chat",
    summary="Chat with local LLM",
    description="Send a prompt to the local LLM (Ollama) and receive a generated response."
)
def chat(request: PromptRequest):

    if not request.prompt.strip():
        raise HTTPException(
            status_code=400,
            detail="Prompt cannot be empty"
        )

    try:
        response = generate_response(request.prompt)

        return {
            "prompt": request.prompt,
            "response": response
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"LLM generation failed: {str(e)}"
        )