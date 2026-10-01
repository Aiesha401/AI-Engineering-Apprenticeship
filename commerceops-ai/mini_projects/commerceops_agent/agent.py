import json
import logging
import time

from .config import MODEL, client
from .schemas import tools
from .tools import tool_functions


logger = logging.getLogger(__name__)


MAX_TOOL_CALL_ROUNDS = 5


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
    start_time = time.perf_counter()

    logger.info("Received user message")

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    for _ in range(MAX_TOOL_CALL_ROUNDS):

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.2,
            max_tokens=300,
            tools=tools
        )

        message = response.choices[0].message

        logger.info("Model response received")

        messages.append(message)

        if not message.tool_calls:
            elapsed_time = time.perf_counter() - start_time

            logger.info(
                "Request completed in %.2f seconds",
                elapsed_time
            )

            return message.content

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
                    tool_start_time = time.perf_counter()

                    tool_result = tool_functions[
                        tool_name
                    ](**arguments)

                    tool_elapsed_time = (
                        time.perf_counter()
                        - tool_start_time
                    )

                    logger.info(
                        "Tool completed: %s in %.4f seconds",
                        tool_name,
                        tool_elapsed_time
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

    logger.warning(
        "Maximum tool call rounds reached"
    )

    return "Unable to complete the request."