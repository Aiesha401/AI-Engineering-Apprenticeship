from fastapi import FastAPI
from pydantic import BaseModel
from mini_projects.commerceops_agent.config import client

MODEL = "nvidia/nemotron-3-ultra-550b-a55b"

class ChatRequest(BaseModel):
    message: str

app = FastAPI()

# @app.post("/chat")
# def chat():

#     return {
#         "response": "Hello!"
#     }

@app.post("/chat")
def chat(request: ChatRequest):
    completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": request.message
            }
        ]
    )

    response = completion.choices[0].message.content

    return {
        "response": response
    }
