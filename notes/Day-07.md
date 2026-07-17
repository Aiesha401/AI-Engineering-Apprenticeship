# Day 7

## What did I build?

I improved my chatbot by replacing multiple `if-elif` statements with dynamic tool dispatch using a Python dictionary. Now the LLM returns the tool name, and Python executes the corresponding function dynamically.

## What did I learn?

Today I learned that Python functions are first-class objects, which means they can be stored inside dictionaries and executed dynamically. This allowed me to replace long conditional statements with a much cleaner approach using `tools[tool_name]()`.

## Biggest challenge today

Understanding how functions could be stored inside a dictionary without being executed immediately.

## How did I solve it?

I experimented with a small example using `say_hello()` and realized that `tools["hello"]` returns the function object, while `tools["hello"]()` actually executes it.

## What surprised me?

I was surprised that a single line of code could replace multiple `if-elif` statements and make the code much cleaner.

## One thing I still don't understand

I'm curious to learn how production AI systems expose available tools to an LLM without relying on manually written system prompts.