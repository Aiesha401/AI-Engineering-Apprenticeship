# Day 34

## What did I build?

I built a multi-step CommerceOps agent using LangGraph that can call tools, receive their results, and generate a final answer.

## What did I learn?

I learned how to use state to maintain the conversation between the user, LLM, and tools. I also learned how conditional edges create the agent loop between the model and tool nodes.

## Biggest challenge today

Understanding why the tool result needs to be added back into the message state before the LLM can generate the final answer.

## How did I solve it?

I used `ToolMessage` to store the tool result and `add_messages` to preserve the complete message history throughout the graph.

## What surprised me?

I was surprised that the `while True` agent loop from Day 31 can be represented as a LangGraph flow such as `model → tools → model` without manually writing the loop.

## One thing I still don't understand

I still want to understand how to structure a larger production agent with more tools, more complex state, and error handling.