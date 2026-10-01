from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

from .agent import process_message


app = FastAPI(
    title="CommerceOps AI",
    description="AI assistant for CommerceOps employees",
    version="1.0.0"
)


class ChatRequest(BaseModel):
    message: str


STATIC_DIR = Path(__file__).parent / "static"


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "service": "CommerceOps AI"
    }


@app.get("/app")
def chat_interface():
    return FileResponse(
        STATIC_DIR / "index.html"
    )


@app.post("/chat")
def chat(request: ChatRequest):
    answer = process_message(request.message)

    return {
        "answer": answer
    }