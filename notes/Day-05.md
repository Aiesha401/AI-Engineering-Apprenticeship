# Day 5

## What did I build?

Today I upgraded my chatbot by introducing a **system prompt**. Instead of behaving like a generic AI assistant, I made it act as a friendly Python mentor. I also experimented with different prompts to observe how changing instructions changes the AI's personality and responses.

Although I didn't build a completely new application today, I significantly improved how my chatbot behaves by learning prompt engineering techniques.


## What did I learn?

Today I learned several important concepts about LLM Engineering.

### System Prompts
- A system prompt defines the AI's personality and behavior.
- It is added once at the beginning of the conversation.
- It has a higher priority than user messages.
- The same LLM can become a Python mentor, chef, business consultant, or customer support assistant just by changing the system prompt.

### Prompt Engineering
I learned that prompt engineering is not about using "magic words."

It is about writing clear instructions by specifying:
- Identity
- Task
- Audience
- Context
- Output Style
- Structure
- Constraints
- Recovery instructions (what the AI should do if information is missing)

A good prompt reduces ambiguity and helps the model generate better responses.

### Zero-shot Prompting
The AI is given only the task without any examples.

### Few-shot Prompting
The AI is first shown examples and then asked to perform a similar task. Since LLMs are excellent pattern recognizers, providing examples usually produces more consistent outputs.

### Structured Outputs
I learned that AI applications should not always return paragraphs. Instead, they can return structured JSON objects that Python programs can easily process, store in databases, or use inside applications.


## Biggest challenge today

The biggest challenge was understanding how professional prompts are designed. Initially, I thought prompts were simply questions for the AI. Later I understood that prompts are actually specifications that clearly describe the task, audience, constraints, and expected output.


## How did I solve it?

By comparing simple prompts with well-designed prompts, I realized that the quality of the output depends heavily on how clearly I communicate my requirements.

I also practiced writing prompts myself and received feedback to improve them.


## What surprised me?

The biggest surprise was discovering that changing only a single system prompt can completely change the AI's behavior without changing the model itself.

I was also surprised that structured JSON responses are far more useful for software applications than plain text because Python can directly work with the returned data.

Another surprising realization was that prompt engineering is very similar to writing software requirements rather than trying to find "magic prompts."


## One thing I still don't understand

I want to learn how AI models actually call external tools or APIs when they don't know something themselves.

For example:
- How can an AI check today's weather?
- How can it access a database?
- How can it retrieve real-time sales data from CommerceOps-AI?

I'm excited to learn Tool Calling, RAG, LangChain, and LangGraph to understand how production AI systems work.