# Day 17

## What did I build?

Today I built my first FastAPI application and exposed several HTTP endpoints. I created routes that returned JSON responses, accepted path parameters and query parameters, and explored the automatically generated API documentation using Swagger UI.

## What did I learn?

I learned what an API is and how FastAPI makes it easy to build web services. I learned how to define routes using decorators, work with path and query parameters, run a FastAPI application using Uvicorn, and test endpoints through both a web browser and the interactive Swagger documentation.

## Biggest challenge today

The biggest challenge was understanding the difference between path parameters and query parameters, and how URLs are mapped to Python functions.

## How did I solve it?

I built multiple endpoints that each demonstrated a different routing style. By testing them directly in the browser and through Swagger UI, I was able to see how FastAPI passed URL values into my Python functions and automatically converted parameter types.

## What surprised me?

I was surprised by how much functionality FastAPI provides with very little code. Automatic JSON serialization, type conversion, and interactive API documentation all worked without requiring additional configuration.

## One thing I still don't understand

I'd like to learn how to connect FastAPI endpoints to my CommerceOps AI and SQLite database so that API requests can trigger real AI tool calls and database queries instead of returning hardcoded responses.