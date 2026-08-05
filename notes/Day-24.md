# Day 24

## What did I build?

Today I built my first complete Retrieval-Augmented Generation (RAG) pipeline. I combined NVIDIA embeddings, ChromaDB, and an LLM into a single workflow where retrieved documents are injected into the prompt before generating an answer.

## What did I learn?

I learned how a production RAG pipeline works end-to-end. Instead of letting the LLM answer from its own knowledge, I first retrieved relevant documents from a vector database and supplied them as context. This grounds the model's responses in retrieved information.

## Biggest challenge today

The biggest challenge was understanding how retrieval and the LLM work together. I realized that ChromaDB only retrieves relevant documents—it does not generate the final answer. The retrieved context must be included in the prompt for the LLM to use it.

## How did I solve it?

I generated an embedding for the user's question, searched ChromaDB for the most relevant documents, combined those documents into a context string, and passed that context to the LLM with a system prompt instructing it to answer only from the provided information.

## What surprised me?

I was surprised that the LLM has no direct connection to ChromaDB. The vector database only returns documents, and the LLM only sees the text that I explicitly include in the prompt. This made the overall RAG architecture much clearer.

## One thing I still don't understand

I want to learn how larger documents are split into chunks and how chunk size affects retrieval quality in real-world RAG systems.

## Summary

Today I completed my first end-to-end RAG application. A user question is converted into an embedding, ChromaDB retrieves the most relevant documents, those documents are injected into the prompt, and the LLM generates a grounded answer based on the retrieved context. This is the foundation of modern AI knowledge assistants.