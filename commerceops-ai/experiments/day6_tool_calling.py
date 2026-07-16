from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

def get_today_orders():
    return 127

messages = [
    {
        "role" : "system",
        "content" : "You are an AI assistant.\
                    You have access to one tool: get_today_orders()\
                    if the user asks about today's orders, respond with \
                    Call: get_today_orders()\
                    Do not answer the question yourself.\
                    For any other question respond normally."
    }
]
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    messages.append({
        "role": "user",
        "content": user_input
    })
    response = client.chat.completions.create(
        model="meta/llama-3.1-8b-instruct",
        messages=messages,
        temperature=0.2,
        max_tokens=50
    )
    ai_response = response.choices[0].message.content
    print("AI:", ai_response)
    if "get_today_orders()" in ai_response:
        print("python executing tool...")
        tool_result = get_today_orders()
        print(f"Tool returned: {tool_result}")
        messages.append(
            {
                "role": "assistant",
                "content": "CALL: get_today_orders"
            }
        )
    
        messages.append(
            {
                "role": "user",
                "content": f"The tool returned {tool_result}. Answer the original question."
            }
        )
    
        res = client.chat.completions.create(
            model="meta/llama-3.1-8b-instruct",
            messages=messages,
            temperature=0.2,
            max_tokens=50
        )
        print(res.choices[0].message.content)
    