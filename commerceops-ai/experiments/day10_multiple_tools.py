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

def send_email(recipient, message):
    return f"Email sent to {recipient} with message: {message}"

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
    },
    {
        "type" : "function",
        "function" : {
            "name": "send_email",
            "description": "send email to a recipient with a message",
            "parameters" : {
                "type" : "object",
                "properties" : {
                    "recipient":{
                        "type" : "string",
                        "description" : "The email address of the recipient."
                    },
                    "message" : {
                        "type" : "string",
                        "description" : "The message to be sent in the email."
                    }
                },
                "required" : ["recipient", "message"]
            }
        }
    }
]

tool_functions = {
    "get_inventory": get_inventory,
    "get_total_revenue": get_total_revenue,
    "get_top_product": get_top_product,
    "greet": greet,
    "send_email": send_email
}
messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful AI assistant. "
            "When a suitable tool is available, use it instead of describing what you would do. "
            "Do not explain that you need to call a function. Actually call the function."
        )
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
        model="nvidia/nemotron-3-ultra-550b-a55b",
        messages=messages,
        temperature=0.2,
        max_tokens=800,
        tools=tools
    )
    message = response.choices[0].message
    messages.append(message)
    tool_calls = message.tool_calls
    if tool_calls:
        for tool_call in tool_calls:
            tool_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)
            tool_result = tool_functions[tool_name](**arguments)
        
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id" : tool_call.id,
                    "content": str(tool_result)
                }
            )
    res = client.chat.completions.create(
        model="nvidia/nemotron-3-ultra-550b-a55b",
        messages=messages,
        temperature=0.2,
        max_tokens=50,
        tools=tools
    )
    print(res.choices[0].message.content)