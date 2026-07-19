from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(
    base_url = "https://integrate.api.nvidia.com/v1",
    api_key = os.getenv("NVIDIA_API_KEY")
)
def get_inventory(product):
    inventory = {
        "iphone 16": 42,
        "samsung s24": 18,
        "macbook air": 9
    }

    return inventory.get(product.lower(), "Product not found")

def get_total_revenue():
    return "$12,500"

def get_top_product():
    return "iPhone 16"

def greet():
    return "Hello!"

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_inventory",
            "description": "Returns inventory for a product.",
            "parameters": {
                "type": "object",
                "properties": {
                    "product": {
                        "type": "string",
                        "description": "The name of the product."
                    }
                },
                "required": ["product"]
            }
        }
    }
]

tool_functions = {
    "get_inventory": get_inventory,
    "get_total_revenue": get_total_revenue,
    "get_top_product": get_top_product,
    "greet": greet
}
messages = [
    {
        "role" : "system",
        "content" : "You are a helpful AI assistant."
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
        max_tokens=50,
        tools=tools
    )
    message = response.choices[0].message
    messages.append(message)
    tool_calls = message.tool_calls
    if message.tool_calls:
        tool_name = tool_calls[0].function.name
        arguments = json.loads(tool_calls[0].function.arguments)
        tool_result = tool_functions[tool_name](arguments["product"])
    
        messages.append(
            {
                "role": "tool",
                "tool_call_id" : tool_calls[0].id,
                "content": str(tool_result)
            }
        )
        res = client.chat.completions.create(
            model="meta/llama-3.1-8b-instruct",
            messages=messages,
            temperature=0.2,
            max_tokens=50,
            tools=tools
        )
        print(res.choices[0].message.content)