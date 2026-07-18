# Day 8

## What did I build?

I replaced my manual tool calling implementation with the official Function Calling API. Instead of parsing text like "Call: get_today_orders", my chatbot now receives structured tool calls, executes the requested Python function, and sends the result back to the LLM using the official `tool` role.

## What did I learn?

Today I learned how the official Function Calling API works. I understood the purpose of the `tools` parameter, how the LLM returns `tool_calls` instead of plain text, and why Python functions stay inside my application while only their descriptions are sent to the LLM.

## Biggest challenge today

Understanding why `message.content` was `None` and how the LLM could request a tool without returning any text.

## How did I solve it?

I inspected the complete API response instead of only looking at `message.content`. This helped me discover the `tool_calls` field, extract the function name, execute the corresponding Python function, and return the result using the official `tool` role.

## What surprised me?

I was surprised to learn that the LLM never executes Python code. It only decides which function should be called, while Python performs the actual execution and sends the result back to the LLM.

## One thing I still don't understand

I'm curious to learn how the LLM decides whether to generate a normal text response or request a tool call, and how function arguments are automatically generated for tools.