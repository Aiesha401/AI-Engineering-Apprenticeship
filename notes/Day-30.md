# Day 30

## What did I build?

Today I learned how LangChain handles tools and conversation memory.I converted normal Python functions into LangChain tools using the `@tool` decorator and inspected their names, descriptions, and argument schemas.I also connected tools to the Nemotron model using `bind_tools()` and observed the model generating structured tool calls.
For memory, I used LangChain's `HumanMessage` and `AIMessage` objects to represent conversation history and passed previous messages into a prompt before invoking the model.

## What did I learn?

I learned that the `@tool` decorator turns a Python function into a structured LangChain tool.
A LangChain tool contains information such as:
- name
- description
- argument schema
- underlying function
I learned that tools can be executed directly with:

`tool.invoke({...})`

I also learned that `model.bind_tools(tools)` makes tools available to the model so that the model can decide when a tool should be called.The model produces a structured `tool_call` containing the tool name and arguments. The tool still needs to be executed and its result returned to the model.

## Memory

I learned how LangChain represents conversation history using message objects such as:
- HumanMessage
- AIMessage
Conversation history can be passed back into the model along with the current question so that the model has access to previous conversation turns.I learned that this is not permanent model memory. The previous conversation must be supplied to the model as context.

## Biggest takeaway

The most important connection today was seeing how LangChain maps onto the tool-calling and memory systems I previously built manually.
Previously, I manually handled tool names, arguments, function execution, and conversation messages.
LangChain provides structured abstractions for these same concepts.

## Summary

Day 30 introduced LangChain tools, tool binding, tool calls, and conversation memory.
I successfully created CommerceOps-style tools, connected them to the Nemotron model, observed structured tool calls, executed a tool with arguments, and created a conversation history using LangChain message objects.

Tomorrow I will combine these concepts to start rebuilding CommerceOps AI using LangChain.