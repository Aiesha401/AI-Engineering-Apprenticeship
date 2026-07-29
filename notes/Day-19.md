# Day 19

## What did I build?

Today I built a FastAPI endpoint that exposes my LLM through an HTTP API using POST requests and Pydantic request models. I also refactored my CommerceOps AI by extracting the agent logic into a reusable process_message() function, separating the terminal interface from the AI's core processing logic.

## What did I learn?

I learned how to create POST endpoints in FastAPI, accept JSON request bodies with Pydantic models, and return AI-generated responses through an API. I also learned an important software engineering principle: separating the interface from the business logic so that the same AI processing function can be reused by different clients such as the terminal, FastAPI, or future web applications.

## Biggest challenge today

The biggest challenge was understanding how to adapt my terminal-based chatbot into an API. At first, I thought I needed to import my entire main() function, but I realized that the terminal loop and the AI processing logic are separate responsibilities.

## How did I solve it?

I created a reusable process_message() function that encapsulates the complete LLM interaction and tool-calling workflow. The terminal application now simply reads user input and calls this function, making the agent logic reusable for other interfaces like FastAPI.

## What surprised me?

I was surprised by how little code was needed to expose an LLM as a web service. Once the chatbot logic was separated from the terminal loop, FastAPI became a thin wrapper that simply accepted HTTP requests, called the processing function, and returned JSON responses.

## One thing I still don't understand

I'd like to learn how production AI applications manage conversation state across multiple users, since my current implementation stores conversation history in a single global messages list and isn't designed for many simultaneous conversations.