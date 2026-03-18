import os
import io

from pypdf import PdfReader
from docx import Document

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from app.services.llm_service import generate_response


# project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VECTOR_DB_PATH = os.path.join(BASE_DIR, "vector_store")

# ensure directory exists
os.makedirs(VECTOR_DB_PATH, exist_ok=True)


# embeddings model
embeddings = HuggingFaceEmbeddings(
    model_name="embedding_model"
)


# load vector database once
vector_db = Chroma(
    persist_directory=VECTOR_DB_PATH,
    embedding_function=embeddings
)


def ingest_document(filename, content):

    # -------- Detect file type --------

    if filename.endswith(".pdf"):

        pdf = PdfReader(io.BytesIO(content))
        text = ""

        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text


    elif filename.endswith(".docx"):

        doc = Document(io.BytesIO(content))
        text = ""

        for para in doc.paragraphs:
            text += para.text + "\n"


    else:
        text = content.decode("utf-8")


    # -------- Split document --------
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = splitter.split_text(text)


    # -------- Store in vector DB --------
    vector_db.add_texts(chunks)

    vector_db.persist()

    return len(chunks)


def query_documents(question):

    docs = vector_db.similarity_search(question, k=6)

    if not docs:
        return {
            "context": "",
            "answer": "I couldn't find relevant information in the document."
        }

    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
You are an AI assistant answering questions using ONLY the provided document context.

Rules:
- Answer the question only using the information in the context.
- If the answer is not found in the context, say: "I don't know based on the provided document."
- Do NOT make up information.
- Keep the answer concise and clear.

Context:
{context}

Question:
{question}
"""

    answer = generate_response(prompt)

    return {
        "context": context,
        "answer": answer
    }