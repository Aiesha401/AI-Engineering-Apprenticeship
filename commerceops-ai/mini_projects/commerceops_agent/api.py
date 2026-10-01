from fastapi import FastAPI
from pydantic import BaseModel

from .agent import process_message


app = FastAPI(
    title="CommerceOps AI",
    description="AI assistant for CommerceOps employees",
    version="1.0.0"
)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "service": "CommerceOps AI"
    }


@app.post("/chat")
def chat(request: ChatRequest):
    answer = process_message(request.message)

    return {
        "answer": answer
    }