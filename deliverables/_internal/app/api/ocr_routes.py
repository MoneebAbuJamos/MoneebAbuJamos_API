from fastapi import APIRouter, UploadFile, File, Form
from enum import Enum

from app.services.ocr_service import extract_text


router = APIRouter(tags=["OCR"])


class OCRLanguage(str, Enum):
    arabic = "ara"
    english = "eng"
    mixed = "ara+eng"


@router.post("/extract")
async def ocr_extract(
    file: UploadFile = File(...),
    language: OCRLanguage = Form(OCRLanguage.mixed)
):

    text = await extract_text(file, language.value)

    return {"text": text}