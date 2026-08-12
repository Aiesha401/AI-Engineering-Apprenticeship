# Day 31

## What did I build?

Today I rebuilt the core CommerceOps AI agent using LangChain.I created CommerceOps tools using LangChain's `@tool` decorator and connected them to the NVIDIA Nemotron model using `bind_tools()`.
I then implemented the complete tool-calling workflow where the model can request a tool, the application executes the tool, sends the result back through a `ToolMessage`, and allows the model to generate the final response.I also added an outer conversation loop so the application can continuously accept user questions.

## What did I learn?

I learned that LangChain Tool objects contain information such as the tool name, description, argument schema, and underlying function.
I learned that `model.bind_tools(tools)` makes these tools available to the model, but does not execute them automatically.
The model produces structured `tool_calls` containing the requested tool name, arguments, and tool-call ID.
I then execute the requested tool and create a `ToolMessage` containing the result. This result is sent back to the model so it can generate the final answer.

## Dynamic tool dispatch

I learned how to create a dictionary mapping tool names to their actual LangChain Tool objects:
`tool_map = {tool.name: tool for tool in tools}`
This allows the application to dynamically select and execute a tool without writing a separate `if/elif` condition for every tool.

## Agent loop

Today I finally connected the complete agent loop:
User question → Model → Tool call → Tool execution → ToolMessage → Model → Final answer.
I also learned the difference between the inner agent loop and the outer conversation loop.
The inner loop handles repeated model/tool interactions, while the outer loop allows the user to continue asking questions.

## Multiple tools

I tested questions requiring multiple tools, such as asking for both inventory and total revenue.
The model was able to request multiple tools, the application executed them, and the results were provided back to the model so it could produce one combined response.

## Biggest takeaway

The biggest takeaway was understanding that LangChain does not magically execute tools for the model.
The model decides which tool it wants to call, but the application is responsible for executing the tool and returning the result to the model.
LangChain provides structured abstractions such as Tool objects, `tool_calls`, and `ToolMessage` that make this workflow easier to implement.

## Connection to previous work

This connected directly to my earlier manual tool-calling implementation.
Previously I manually handled tool names, arguments, dynamic dispatch, tool results, and the agent loop.
Today I implemented the same underlying architecture using LangChain abstractions.
This helped me understand what LangChain is actually doing instead of treating it as a black box.

## Summary

Day 31 was the first day where CommerceOps AI was actually rebuilt using LangChain.
I implemented tools, dynamic tool dispatch, tool execution, ToolMessages, the model/tool interaction loop, multiple tool calls, and the continuous user conversation loop.
CommerceOps AI can now answer inventory and revenue questions using LangChain tools and return the results naturally to the user.