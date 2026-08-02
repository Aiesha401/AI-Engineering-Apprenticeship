# Day 22

## What did I build?

Today I built my first semantic search system using ChromaDB. I created a collection, added multiple CommerceOps policy documents, and queried them using natural language questions. Instead of searching for exact keywords, ChromaDB retrieved documents based on their semantic meaning.

## What did I learn?

I learned that a vector database stores embeddings alongside their associated documents and uses similarity search to retrieve the most relevant information. I also learned that a ChromaDB collection is similar to a table in SQLite, but instead of storing rows for SQL queries, it stores documents and their vector representations for semantic search.

## Biggest challenge today

The biggest challenge was getting ChromaDB running because I initially encountered an import error related to `grpc`. After troubleshooting the environment and correcting a few coding mistakes, I was able to successfully create a collection and perform semantic searches.

## How did I solve it?

I verified my Python environment, corrected the issues in my code, and reran the application. ChromaDB automatically downloaded its default embedding model, allowing me to add documents and retrieve semantically similar results without generating embeddings manually.

## What surprised me?

I was amazed by how accurately ChromaDB retrieved relevant documents even when my queries used completely different wording. For example, it matched "free delivery" with "free shipping" and "buying" with "purchase", showing how semantic search understands meaning instead of exact keywords.

## One thing I still don't understand

I want to learn how production applications use custom embedding models instead of ChromaDB's default embedding model, and how external embeddings are stored and searched inside a vector database.

## Summary

Today I built my first semantic search engine. Instead of manually comparing embedding vectors, I learned how a vector database automatically stores embeddings and retrieves documents based on semantic similarity. This completed my understanding of the retrieval side of Retrieval-Augmented Generation (RAG) and prepared me for integrating my own embedding model into the retrieval pipeline.