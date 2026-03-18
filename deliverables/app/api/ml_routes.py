from fastapi import APIRouter, HTTPException

from app.schemas.llm_schema import SentimentRequest
from app.services.ml_service import predict_sentiment, get_model_info


router = APIRouter(tags=["ML"])


@router.post(
    "/ml/sentiment",
    summary="Predict sentiment",
    description="Predict sentiment (positive or negative) for the given text using the trained ML model."
)
def sentiment_analysis(request: SentimentRequest):

    if not request.text.strip():
        raise HTTPException(
            status_code=400,
            detail="Text cannot be empty"
        )

    try:
        result = predict_sentiment(request.text)

        return {
            "text": request.text,
            "sentiment": result
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Sentiment prediction failed: {str(e)}"
        )


@router.get(
    "/ml/model-info",
    summary="Get ML model information",
    description="Return basic information about the trained ML model used for sentiment prediction."
)
def model_info():

    try:
        return get_model_info()

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to retrieve model info: {str(e)}"
        )