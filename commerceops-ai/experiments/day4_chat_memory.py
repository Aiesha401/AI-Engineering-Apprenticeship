from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

messages = []

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )
    response = client.chat.completions.create(
        model="meta/llama-3.1-8b-instruct",
        messages=messages,
        temperature=0.2,
        max_tokens=50
    )
    ai_response = response.choices[0].message.content
    print("AI:", ai_response)
    messages.append(
        {
            "role": "assistant",
            "content": ai_response
        }
    )