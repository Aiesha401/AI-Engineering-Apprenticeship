# Day 36

## What did I build?

I added structured logging and improved environment-based configuration to CommerceOps AI.

## What did I learn?

I learned how logging helps track what the application is doing, while environment variables keep configuration such as API keys outside the source code.

## Biggest challenge today

The main challenge was understanding what information should be logged during the agent and tool execution process.

## How did I solve it?

I added logs for user messages, model responses, tool requests, tool arguments, tool completion, and tool failures.

## What surprised me?

I noticed that the HTTP client also produces its own request logs, separate from the logs I created for the CommerceOps agent.

## One thing I still don't understand

I want to learn how production applications configure logging levels, log files, and structured logs for debugging deployed systems.