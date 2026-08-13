# Day 32

## What did I build?

I built simple LangGraph workflows using nodes, edges, START, END, and state. I also built a small CommerceOps inventory graph that checks inventory and formats the result.

## What did I learn?

I learned that nodes perform work, edges control the flow, and state carries information between nodes.

## Biggest challenge today

Understanding what state is and why it is passed to every node.

## How did I solve it?

I built progressively larger examples and saw how each node could read and update the state.

## What surprised me?

I was surprised that the agent loop I built with LangChain can be represented as a graph instead of only using a `while True` loop.

## One thing I still don't understand

I still want to understand how LangGraph will represent the full agent state, including LLM responses, tool calls, and tool results.