# Day 25

## What did I build?

Today I explored document chunking techniques used in Retrieval-Augmented Generation (RAG). I implemented sentence-based chunking, fixed-size chunking, and fixed-size chunking with overlap to understand how documents are prepared before being stored in a vector database.

## What did I learn?

I learned that storing an entire document as one embedding reduces retrieval quality because a single vector has to represent many different topics. By splitting documents into smaller chunks, each chunk gets its own embedding, allowing the vector database to retrieve more relevant information.

## Biggest challenge today

The biggest challenge was understanding why overlap is important even though it creates duplicate content between chunks.

## How did I solve it?

By comparing chunked outputs with and without overlap, I realized that overlap preserves context when sentences or ideas span across chunk boundaries. Although overlapping chunks contain repeated text, they improve semantic retrieval by keeping related information together.

## What surprised me?

I was surprised that good RAG performance depends not only on embedding models but also on how documents are prepared before embedding. The chunking strategy itself has a significant impact on retrieval quality.

## One thing I still don't understand

I want to learn how production RAG systems decide the optimal chunk size and overlap for different types of documents.

## Summary

Today I learned why chunking is a fundamental step in RAG pipelines. I experimented with sentence-based and fixed-size chunking, added overlap between chunks, and understood how preserving context improves retrieval accuracy. This prepares me for retrieving the most relevant chunks instead of entire documents.