# Day 10

## What did I build?

I extended my chatbot to support multiple tools by adding a second function, `send_email()`, alongside `get_inventory()`. I also updated my tool execution logic to iterate through all requested tool calls using a `for` loop and dynamically execute functions with `**arguments`.

## What did I learn?

Today I learned that the `tool_calls` field is a list because an LLM may request multiple function calls for a single user request. I also learned how Python's `**` operator unpacks a dictionary into keyword arguments, allowing the same line of code to execute different functions with different parameter lists.

## Biggest challenge today

Understanding how multiple tool calls work in practice and realizing that different AI models may not support multiple tool calls in the same way.

## How did I solve it?

I replaced my single-tool logic with a loop over `tool_calls` and used dynamic argument unpacking with `**arguments`. While experimenting, I also discovered that my chosen model handles tool calling differently, which helped me understand that provider capabilities can affect application behavior.

## What surprised me?

I was surprised that my application architecture was correct even though the model did not always produce the expected multi-tool behavior. I learned that AI providers can implement function calling differently, and the same code may behave differently across models.

## One thing I still don't understand

I'm curious to learn how production AI agents repeatedly call the LLM until all required tools have been executed and a final natural language response is generated.