from app.services.llm_service import generate_response

def summarize_text(text: str):

    prompt = f"""
    Summarize the following text in a concise paragraph:

    {text}
    """

    return generate_response(prompt)