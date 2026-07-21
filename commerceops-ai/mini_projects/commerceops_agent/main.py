from config import client
from tools import *
from schemas import tools
import json

MODEL = "nvidia/nemotron-3-ultra-550b-a55b"

messages = [
    {
        "role": "system",
        "content": (
                "You are CommerceOps AI."
                "You help employees answer inventory,sales and revenue questions."
                "Always use tools whenever they can answer the user's request."
                "Never fabricate business data."
        )
    }
]
def main():
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
                model=MODEL,
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

if __name__ == "__main__":
    main()