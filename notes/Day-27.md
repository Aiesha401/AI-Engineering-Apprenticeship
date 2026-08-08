# Day 27

## What did I build?

Today I improved my RAG pipeline by adding retrieval-quality filtering. After retrieving the top 3 chunks from ChromaDB, I inspected their distance values and filtered out documents whose distance was above a chosen threshold before sending the remaining context to the LLM.

## What did I learn?

I learned that Top-k retrieval does not guarantee that every retrieved chunk is useful. ChromaDB provides distance values that indicate how close the retrieved embeddings are to the query embedding. For the distance values I observed, a smaller distance meant greater similarity.

I also learned that retrieving more context is not always better. Irrelevant documents can add unnecessary information to the LLM's context and potentially affect the quality of the answer.

## Biggest challenge today

The biggest challenge was understanding how to choose a distance threshold. Initially, I used a threshold of 1.5, but every retrieved document was below that value, so nothing was filtered.

## How did I solve it?

I experimented with a stricter threshold of 0.8. This caused weaker results to be removed from the retrieved context. I then passed only the filtered documents to the LLM.

## What surprised me?

I was surprised that simply retrieving the top 3 documents does not mean all three are equally relevant. Looking at their distance values made it possible to see which results were closer to the query and which were weaker matches.

## One thing I still don't understand

I want to learn how production RAG systems determine the best distance threshold and evaluate retrieval quality instead of choosing a threshold manually.

## Summary

Today I improved my RAG pipeline by inspecting ChromaDB distance values and filtering weaker retrieved chunks before sending context to the LLM. I learned that Top-k retrieval and relevance filtering work together: Top-k provides candidate documents, while filtering can remove results that are not relevant enough. This makes the retrieval stage more controlled and prepares my system for the final RAG module day.