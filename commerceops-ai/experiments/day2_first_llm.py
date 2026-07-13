from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("NVIDIA_API_KEY")

client = OpenAI(
    base_url = "https://integrate.api.nvidia.com/v1",
    api_key=api_key
)

try:
    response = client.chat.completions.create(
        model="meta/llama-3.3-70b-instruct",
        messages=[
            {
                "role": "user",
                "content": "Say hello in one sentence."
            }
        ],
        temperature=0.2,
        max_tokens=50
    )

    print(response.choices[0].message.content)

except Exception as e:
    print("❌ API Request Failed")
    print(e)
