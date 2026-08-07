# Day 26

## What did I build?

Today I improved my Retrieval-Augmented Generation (RAG) pipeline by implementing Top-k retrieval. Instead of retrieving only one or two documents, my application now retrieves the three most relevant chunks from ChromaDB, combines them into a single context, and uses that context to answer user questions. I also modified the application to process multiple questions in one execution.

## What did I learn?

I learned that Top-k retrieval means retrieving the k most relevant chunks from a vector database instead of only the single best match. This provides the LLM with richer context and allows it to answer questions that require information from multiple documents.

## Biggest challenge today

The biggest challenge was understanding why retrieving multiple chunks is important. Initially, I thought retrieving one relevant document would always be enough, but I realized that many user questions require information spread across different documents.

## How did I solve it?

I increased the retrieval size from two to three documents using `n_results=3`. I combined the retrieved chunks into a single context using `"\n".join()` and passed that context to the LLM. I also refactored the code to loop through multiple user questions instead of manually changing the query each time.

## What surprised me?

I was surprised that the LLM correctly refused to answer questions when the retrieved documents did not contain enough information. Instead of hallucinating, it responded with "I don't have enough information in the provided documents," showing how a good system prompt and retrieval pipeline can improve reliability.

## One thing I still don't understand

I want to learn how production RAG systems decide the best value of k and how they filter irrelevant retrieved chunks before sending them to the LLM.

## Summary

Today I enhanced my RAG pipeline with Top-k retrieval and multi-query support. My application now retrieves multiple relevant chunks, builds richer context for the LLM, and produces more grounded responses while avoiding fabricated answers. This brought my CommerceOps AI one step closer to a production-quality Retrieval-Augmented Generation system.