# Day 18

## What did I build?

Today I connected my FastAPI application to the backend logic I had already built for CommerceOps AI. Instead of returning hardcoded responses, my API endpoints now call reusable Python functions to retrieve inventory and revenue data, and I implemented proper HTTP error handling for missing products.

## What did I learn?

I learned how to keep FastAPI routes focused on handling HTTP requests while delegating business logic to separate Python functions. I also learned how FastAPI automatically converts Python objects into JSON responses and how to use HTTPException to return appropriate error codes when resources are not found.

## Biggest challenge today

The biggest challenge was encountering SQLite's thread safety error when using my existing database connection inside FastAPI. It was my first experience with how web servers execute requests differently from standalone Python scripts.

## How did I solve it?

I learned that FastAPI handles requests using worker threads, while my SQLite connection had been created in a different thread. For this project, I resolved the issue by allowing the SQLite connection to be shared across threads with check_same_thread=False. More importantly, I now understand why the error occurred and why larger applications usually create separate database connections for each request.

## What surprised me?

I was surprised by how little code was required to expose my backend through HTTP. The helper functions I built during the SQL module could be reused almost unchanged, with FastAPI acting as a thin layer between HTTP requests and my application logic.

## One thing I still don't understand

I'd like to learn how production applications manage database connections safely across many concurrent users, and how frameworks like FastAPI typically organize routes, services, and database access in larger projects.