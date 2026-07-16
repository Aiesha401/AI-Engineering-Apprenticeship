# Day 6

## What did I build?

Today I built my first AI application capable of performing a simple tool call.

Instead of letting the LLM answer every question directly, I created a Python function called `get_today_orders()` and designed a workflow where the LLM decides when that function should be used.

The overall flow was:

User → LLM → Python Function → Tool Result → LLM → Final Answer

Although the tool was simulated with a simple Python function, I understood the complete architecture behind modern AI agents and tool calling.


## What did I learn?

Today was one of the biggest learning days of my AI Engineering journey.

### Tool Calling

I learned that LLMs cannot execute Python functions themselves.

Instead, they decide **which tool should be used**, while Python is responsible for executing that tool and returning the result.

### The Role of Python

Python acts as the orchestrator of the entire workflow.

It:
- Sends the user's message to the LLM.
- Reads the LLM's decision.
- Executes the required Python function.
- Sends the tool's output back to the LLM.
- Displays the final response to the user.

### Multiple LLM Calls

I learned that answering a tool-related question usually requires multiple LLM calls.

The first call decides which tool is needed.

The second call receives the tool's output and generates a natural language response for the user.

### Communication Protocol

I also learned that the LLM and Python communicate through an agreed protocol.

In today's implementation, the protocol was:

`Call: get_today_orders()`

Python looked for this response and executed the corresponding function.

### Architecture over Syntax

The most important lesson today was understanding the architecture behind tool calling rather than simply learning a framework or API.


## Biggest challenge today

The biggest challenge was understanding how the LLM could "call" a Python function.

Initially, it felt impossible because the LLM cannot execute Python code directly.


## How did I solve it?

By breaking the workflow into individual steps, I understood that the LLM never executes the function.

Instead, it requests the tool, Python executes it, and then Python sends the result back to the LLM.

Building a manual version of this architecture made the concept much easier to understand.


## What surprised me?

I was amazed to see that my Python program and the LLM could work together as a team.

The LLM decided which tool it needed, Python executed the tool, and then the LLM used the returned result to generate a final response.

It no longer felt like I was building a chatbot—I felt like I was building an actual AI application.


## One thing I still don't understand

I want to understand how production AI systems manage hundreds or even thousands of available tools without writing hundreds of `if` statements.

I'm also curious about how real tool calling APIs automatically identify the correct function and pass arguments to it.