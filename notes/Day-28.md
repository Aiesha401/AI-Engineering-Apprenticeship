# Day 28

## What did I build?

Today I built the final CommerceOps AI RAG knowledge system using company-style documents covering employee policies, refunds, shipping, inventory, customer communication, invoices, management approval, and customer support.

The system generates embeddings for the documents, stores them in ChromaDB, retrieves the top-k results for a user question, filters results using a distance threshold, builds the retrieved context, and sends that context to the LLM to generate a grounded answer.

## What did I learn?

I learned how the different components of a RAG pipeline work together:

Documents → Embeddings → ChromaDB → Query Embedding → Top-k Retrieval → Distance Filtering → Context → LLM → Answer.

I also learned that a RAG system can only answer reliably when the correct information is successfully retrieved and included in the context.

## Biggest challenge today

The biggest challenge was testing a question that required information from different areas of the company knowledge base.

For example, when I asked:

"How quickly should customer support respond to a customer asking about a refund?"

the retrieval system returned refund, email, and shipping documents instead of the customer support document.

## How did I solve it?

I investigated the retrieved documents and their distance values instead of assuming that the LLM was the problem. The LLM correctly refused to invent an answer because the customer-support response-time information was not present in the retrieved context.

This showed me that retrieval quality is an important part of RAG and that a good LLM cannot compensate for incorrect or incomplete retrieval.

## What surprised me?

I was surprised that the RAG pipeline could correctly answer questions across several different areas of CommerceOps knowledge while also refusing to answer questions when the required information was not available.

I also learned that retrieval failures are useful for understanding where a RAG system needs improvement.

## One thing I still don't understand

I want to learn how production RAG systems improve retrieval when semantic search retrieves related but incorrect documents, and how techniques such as reranking, better chunking, metadata filtering, or query transformation can improve retrieval quality.

## Summary

Today I completed the first full CommerceOps AI knowledge retrieval system. I combined embeddings, ChromaDB, Top-k retrieval, distance filtering, context injection, and an LLM into a complete RAG pipeline.

The RAG module is now complete, but I also identified a real retrieval-quality problem that can be addressed later during the project's production and performance-improvement phase.

This completes the RAG module from Days 20–28.