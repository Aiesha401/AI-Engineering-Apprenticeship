# Day 29

## What did I build?

Today I started the LangChain module and rebuilt a simple LLM workflow using LangChain. I created reusable prompt templates, connected them to my NVIDIA Nemotron model, and built my first LangChain chain.

I also created a CommerceOps AI prompt using system and human message roles and used variables inside the prompt template.

## What did I learn?

I learned that LangChain provides abstractions for composing LLM application components.

I learned how to use `ChatPromptTemplate.from_template()` to create a reusable prompt containing variables such as `{topic}`.

I also learned how `ChatPromptTemplate.from_messages()` can define structured messages with roles such as `system` and `human`.

I learned that the system message can define how CommerceOps AI should behave, while the human message contains the actual task or question.

## Biggest challenge today

The biggest challenge was understanding what LangChain is actually doing compared with the OpenAI-compatible API calls I had already written manually.

Initially, it looked like LangChain was doing something completely different, but I realized that my NVIDIA model is still responsible for generating the response. LangChain provides abstractions around prompts, messages, and chains.

## How did I solve it?

I compared my previous manual LLM calls with the LangChain implementation.

Previously I manually created messages and called:

`client.chat.completions.create()`

With LangChain, I created a prompt template, connected it to the model using:

`chain = prompt | model`

and executed the workflow using:

`chain.invoke()`

This helped me understand that a chain is essentially a sequence of connected components.

## What surprised me?

I was surprised by how simple the chain composition syntax is.

Instead of manually passing the formatted prompt into the model, I can write:

`chain = prompt | model`

and then provide the required variables when calling:

`chain.invoke({...})`

I also learned that LangChain represents messages as objects such as `HumanMessage` and `AIMessage`.

## One thing I still don't understand

I want to understand how LangChain chains become more useful when multiple components are connected together, especially when tools, memory, and retrieval are involved.

## Summary

Today I began learning LangChain by working with prompt templates and chains. I learned how to create reusable prompts with variables, structure conversations using system and human messages, connect prompts to my NVIDIA Nemotron model, and execute the resulting chain with `invoke()`.

The biggest takeaway was that LangChain is not the LLM itself. It provides abstractions that make it easier to compose and manage LLM application workflows.