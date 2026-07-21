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
def get_inventory_report():
    return{
        "iphone 16": 42,
        "samsung s24": 18,
        "macbook air": 9
    }
def get_total_revenue():
    return "$12,500"

def get_top_product():
    return "iPhone 16"


def send_email(recipient, message):
    return f"Email sent to {recipient} with message: {message}"

inventory_tool =     {
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

inventory_report_tool =     {
    "type": "function",
    "function": {
        "name": "get_inventory_report",
        "description": "Returns a report of the current inventory.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
}

revenue_tool = {
    "type": "function",
    "function" : {
        "name": "get_total_revenue",
        "description": "Returns the total revenue.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
}

top_product_tool = {
        "type": "function",
    "function" : {
        "name": "get_top_product",
        "description": "Returns the top-selling product.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
}

email_tool = {
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

tools = [
    inventory_tool,
    inventory_report_tool,
    revenue_tool,
    top_product_tool,
    email_tool
]

tool_functions = {
    "get_inventory": get_inventory,
    "get_total_revenue": get_total_revenue,
    "get_top_product": get_top_product,
    "get_inventory_report": get_inventory_report,
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
    while True:
        response = client.chat.completions.create(
            model="nvidia/nemotron-3-ultra-550b-a55b",
            messages=messages,
            temperature=0.2,
            max_tokens=300,
            tools=tools
        )
        message = response.choices[0].message
        messages.append(message)
        print("Content:", message.content)
        print("Tool calls:", message.tool_calls)
        if message.tool_calls:
            for tool_call in message.tool_calls:
                tool_name = tool_call.function.name
                arguments = json.loads(tool_call.function.arguments)
                if tool_name not in tool_functions:
                    tool_result = f"Tool '{tool_name}' not found."
                else:
                    try:
                        tool_result = tool_functions[tool_name](**arguments)
                    except Exception as e:
                        tool_result = f"Tool execution failed: {e}"
                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id" : tool_call.id,
                        "content": str(tool_result)
                    }
                )
            continue
        print(message.content)
        break