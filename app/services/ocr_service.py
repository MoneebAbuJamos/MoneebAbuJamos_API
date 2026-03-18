import pytesseract
from PIL import Image
import io


async def extract_text(file, language):

    contents = await file.read()

    image = Image.open(io.BytesIO(contents))

    text = pytesseract.image_to_string(
        image,
        lang=language
    )

    return text