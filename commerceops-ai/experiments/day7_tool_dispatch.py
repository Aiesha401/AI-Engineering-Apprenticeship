from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url = "https://integrate.api.nvidia.com/v1",
    api_key = os.getenv("NVIDIA_API_KEY")
)
def get_today_orders():
    return 127

def get_total_revenue():
    return "$12,500"

def get_top_product():
    return "iPhone 16"

def greet():
    return "Hello!"

tools = {
    "get_today_orders": get_today_orders,
    "get_total_revenue": get_total_revenue,
    "get_top_product": get_top_product,
    "greet": greet
}

messages = [
    {
        "role" : "system",
        "content" : "You are an AI assistant.\
                    You have access to the following tools:\
                    1. get_today_orders\
                    - Returns today's order count.\
                    2. get_total_revenue\
                    - Returns today's total revenue.\
                    3. get_top_product\
                    - Returns today's top-selling product.\
                    4. greet\
                    - Greets the user.\
                    When a user's request requires one of these tools, respond ONLY in this format:\
                    Call: <tool_name>\
                    Examples:\
                    Call: get_today_orders\
                    Call: get_total_revenue\
                    Do not answer the question yourself if a tool is required.\
                    If no tool is needed, answer normally."
    }
]

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

    tool_name = ai_response.replace("Call:", "").strip()
    if tool_name in tools:
        tool_res = tools[tool_name]()
        messages.append(
            {
                "role": "user",
                "content": f"The tool returned {tool_res}. Answer the original question."
            }
        )
        res = client.chat.completions.create(
            model="meta/llama-3.1-8b-instruct",
            messages=messages,
            temperature=0.2,
            max_tokens=50
        )
        print(res.choices[0].message.content)