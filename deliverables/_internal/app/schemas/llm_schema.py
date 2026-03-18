from pydantic import BaseModel, Field


# ---------- LLM Chat ----------
class PromptRequest(BaseModel):
    prompt: str = Field(
        ...,
        min_length=1,
        description="User prompt sent to the local LLM"
    )


# ---------- Summarization ----------
class SummarizeRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        description="Text to summarize using the LLM"
    )


# ---------- RAG Query ----------
class RAGQueryRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=3,
        description="Question used to retrieve information from uploaded documents"
    )


# ---------- ML Sentiment ----------
class SentimentRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        description="Text input for sentiment prediction"
    )