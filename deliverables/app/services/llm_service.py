import os
from llama_cpp import Llama

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MODEL_PATH = os.path.join(BASE_DIR, "models", "qwen.gguf")

llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=4096,
    n_threads=os.cpu_count()
)

def generate_response(prompt: str):

    response = llm.create_chat_completion(
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=200
    )

    return response["choices"][0]["message"]["content"]