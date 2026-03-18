from fastapi import FastAPI

from app.api import llm_routes
from app.api import ocr_routes
from app.api import ml_routes
from app.api import rag_routes
from app.api import summarize_routes


app = FastAPI(title="Offline AI API")


app.include_router(llm_routes.router)
app.include_router(ocr_routes.router)
app.include_router(ml_routes.router)
app.include_router(rag_routes.router)
app.include_router(summarize_routes.router)


@app.get("/", tags=["System"])
def root():
    return {"message": "Offline AI API running"}