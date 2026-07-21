# Day 11
## What did I build?

I built my first autonomous AI agent by implementing an agent loop that repeatedly executes tool calls until the model produces a final response. I also created a small CommerceOps AI assistant capable of checking inventory, generating inventory reports, retrieving revenue and top-selling products, and sending emails. Finally, I refactored the project into separate modules (config.py, tools.py, schemas.py, and main.py) to make it cleaner and easier to maintain.

## What did I learn?

Today I learned that an AI agent is essentially a loop that alternates between the LLM and external tools until a task is complete. I learned how to implement a nested conversation loop and agent loop, how to execute multiple tool calls dynamically, and how tool results are fed back into the model so it can continue reasoning before generating a final answer.

## Biggest challenge today

The biggest challenge was understanding the agent loop architecture and debugging why the model sometimes returned normal text instead of tool calls. I also had to learn how to properly handle unknown tools, tool execution errors, and multiple rounds of tool execution.

## How did I solve it?

I added debugging statements to inspect the model's responses and verified whether tool_calls were being returned. I improved my error handling so that tool failures were sent back to the model instead of crashing the application. Once the agent loop was working correctly, I refactored the code into separate files to make the project more modular and maintainable.

## What surprised me?

I was surprised by how powerful the agent loop became once it was implemented. The model was able to plan multiple steps on its own—for example, generating an inventory report, using that report to compose an email, and then sending the email without me hardcoding that workflow. It also surprised me that adding new capabilities mostly involved creating new tools rather than changing the agent logic.

## One thing I still don't understand

I'm curious to learn how production AI agents manage much larger collections of tools, decide which tools to use efficiently, and prevent unnecessary or repetitive tool calls during complex tasks.