# Day 33

## What did I build?

I built a LangGraph workflow with typed state and conditional routing for inventory, revenue, and general questions.

## What did I learn?

I learned how nodes update state and how conditional edges use the state to decide which node should run next.

## Biggest challenge today

Understanding why the router was sending the revenue request to the general node even though the intent was correctly identified.

## How did I solve it?

I updated the routing function to handle the `revenue` intent separately and tested inventory, revenue, and general questions.

## What surprised me?

I was surprised that the graph can dynamically choose different paths instead of always following the same sequence of nodes.

## One thing I still don't understand

I still want to understand how LangGraph will use LLM responses and tool calls to make these routing decisions in the actual CommerceOps agent.