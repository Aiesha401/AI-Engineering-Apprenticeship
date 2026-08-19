import logging
import json

from config import client, MODEL
from tools import tool_functions
from schemas import tools

logger = logging.getLogger(__name__)

messages = [
    {
        "role": "system",
        "content": (
            "You are CommerceOps AI. "
            "You help employees answer inventory, sales and revenue questions. "
            "Always use tools whenever they can answer the user's request. "
            "Never fabricate business data."
        )
    }
]


def process_message(user_input):

    logger.info(
        "Received user message"
    )

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

        logger.info(
            "Model response received"
        )


        messages.append(message)

        if message.tool_calls:

            for tool_call in message.tool_calls:

                tool_name = tool_call.function.name

                logger.info(
                    "Tool requested: %s",
                    tool_name
                )

                arguments = json.loads(
                    tool_call.function.arguments
                )

                logger.info(
                    "Tool arguments: %s",
                    arguments
                )

                if tool_name not in tool_functions:

                    tool_result = (
                        f"Tool '{tool_name}' not found."
                    )

                else:

                    try:
                        tool_result = tool_functions[
                            tool_name
                        ](**arguments)

                        logger.info(
                            "Tool completed: %s",
                            tool_name
                        )

                    except Exception as e:

                        logger.exception(
                            "Tool execution failed: %s",
                            tool_name
                        )

                        tool_result = (
                            f"Tool execution failed: {e}"
                        )

                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": str(tool_result)
                    }
                )

            continue

        return message.content