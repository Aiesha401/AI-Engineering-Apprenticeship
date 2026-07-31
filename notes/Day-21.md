# Day 21

## What did I build?

Today I generated my first real text embeddings using NVIDIA's `nemotron-3-embed-1b` model. I also implemented cosine similarity with NumPy to compare the semantic similarity between different pieces of text. To make my code cleaner, I created a reusable `get_embedding()` helper function.

## What did I learn?

I learned that embeddings are high-dimensional vectors representing the semantic meaning of text. I also learned how cosine similarity measures the angle between two embedding vectors to determine how similar their meanings are. Similar sentences produce higher similarity scores than unrelated ones.

## Biggest challenge today

The biggest challenge was getting NVIDIA's embedding API to work. I initially used the `nv-embedqa-e5-v5` model but encountered API errors related to `input_type` and model compatibility.

## How did I solve it?

After investigating the available models in NVIDIA Build, I switched to the `nvidia/nemotron-3-embed-1b` model, which worked correctly with the OpenAI-compatible SDK. I then successfully generated embeddings and compared them using cosine similarity.

## What surprised me?

I was surprised that a single sentence is represented by a vector with 2048 dimensions. It was fascinating to see that the embedding is simply a list of floating-point numbers, and yet those numbers capture the semantic meaning of the sentence.

## One thing I still don't understand

I understand how to compute cosine similarity, but I want to learn more about how embedding models are actually trained to place semantically similar sentences close together in high-dimensional space.

## Summary

Today I took my first step into semantic AI. Instead of comparing text using exact keywords, I learned how embedding models convert text into vectors and how cosine similarity allows computers to compare the meanings of sentences mathematically. This forms the foundation for semantic search, vector databases, and Retrieval-Augmented Generation (RAG).