# CommerceOps AI

CommerceOps AI is an AI-powered business operations assistant that allows users to ask questions about inventory, revenue, and product performance using natural language.

The application uses an LLM with tool calling to interact with business data stored in SQLite. It provides a FastAPI interface and can be run locally or inside a Docker container.

## Live Demo

**Web App:** https://commerceops-ai.onrender.com/app

**API Documentation:** https://commerceops-ai.onrender.com/docs

## Features

- Natural-language business queries
- Inventory lookup
- Inventory reporting
- Total revenue reporting
- Top-performing product identification
- LLM-based tool calling
- Multi-tool execution
- SQLite-backed business data
- FastAPI REST API
- Structured application logging
- Dockerized deployment
- Browser-based chat interface for interacting with the AI assistant
- FastAPI REST API for programmatic access
- SQLite-backed business data
- LLM tool calling for business operations
- Multi-step agent workflow
- Structured logging and performance monitoring
- Automated tests with pytest
- Docker containerization
- Cloud deployment with Render

## Tech Stack

- Python
- FastAPI
- LangChain
- LangGraph
- SQLite
- Docker
- NVIDIA API
- pytest

## Architecture

CommerceOps AI follows a modular agent-based architecture:
```text
     User
      │
      ▼
     Web Chat Interface
      │
      ▼
     FastAPI /chat
      │
      ▼
     CommerceOps Agent
      │
      ▼
     LLM Tool Calling
      │
      ▼ 
     Business Tools
      │
      ▼
     SQLite Database
```
The application also exposes Swagger/OpenAPI documentation through /docs.

## Request Flow
1. The user sends a natural-language request.
2. FastAPI receives the request through the /chat endpoint.
3. The agent sends the user's message to the LLM.
4. The LLM determines whether a tool is required.
5. The requested CommerceOps tool is executed.
6. The tool retrieves or processes data from SQLite.
7. The tool result is returned to the LLM.
8. The LLM generates the final response.
9. FastAPI returns the response to the user.

## Project Structure

```text
    commerceops-ai/
    ├── experiments/
    ├── mini_projects/
    │   └── commerceops_agent/
    │       ├── agent.py
    │       ├── api.py
    │       ├── commerceops.db
    │       ├── config.py
    │       ├── logging_config.py
    │       ├── main.py
    │       ├── schemas.py
    │       └── tools.py
    ├── tests/
    │   └── test_tools.py
    ├── Dockerfile
    ├── .dockerignore
    ├── .gitignore
    ├── requirements.txt
    └── README.md
```

## Core Modules
- agent.py — handles LLM interaction and the agent workflow.
- tools.py — contains business tools that interact with the SQLite database.
- schemas.py — defines structured tool schemas.
- config.py — manages application configuration.
- logging_config.py — configures application logging.
- api.py — exposes the FastAPI endpoints.
- main.py — provides the terminal interface.
- commerceops.db — SQLite database containing business data.
- tests/ — contains automated tests for the business tools.

## How It Works
CommerceOps AI uses an LLM-driven tool-calling workflow to answer business questions.

```text
     User Request
          │
          ▼
     LLM
          │
          ▼
     Tool Selection
          │
          ▼
     Tool Execution
          │
          ▼
     SQLite Database
          │
          ▼
     Tool Result
          │
          ▼
     LLM
          │
          ▼
     Final Answer
```

The agent can execute multiple tools when a request requires information from multiple operations.
The application also logs important steps such as incoming requests, model responses, requested tools, tool arguments, and tool completion.

## Available Tools

The CommerceOps agent currently provides tools for:
- Checking inventory for a product
- Generating an inventory report
- Calculating total revenue
- Identifying the top-performing product
- Sending email notifications

## API

### Web Interface

`GET /app`

Provides the browser-based CommerceOps AI chat interface.

### Health Check

`GET /`

Returns the service health status.

### Chat

`POST /chat`

Accepts a user message and returns the AI-generated response.

Example request:

```json
{
  "message": "How many iPhones are in stock?"
}
```

### API Documentation

`/docs`

Provides interactive Swagger/OpenAPI documentation.

## Web Interface

CommerceOps AI includes a lightweight browser-based chat interface.

The interface is available at:

`/app`

Users can ask questions about inventory, revenue, and products. The frontend communicates with the FastAPI `/chat` endpoint and displays the assistant's responses in a scrollable chat interface.

### Health Check

GET /

Example response:
{
  "status": "ok",
  "service": "CommerceOps AI"
}

### Chat

POST /chat

Request:
{
  "message": "What is our total revenue?"
}

The API sends the request to the CommerceOps agent and returns the generated response.
Interactive API documentation is available through:
/docs

## Example Queries

The agent can answer questions such as:

How many iPhones are in stock?

Give me the inventory report.

What is our total revenue?

Which product is performing the best?

What is the inventory of iPhone 16 and Samsung S24?

## Testing

Automated tests are written using pytest.
Run the tests from the project root:
python -m pytest

The current test suite covers the core business tools.

## Local Setup

1. Clone the repository
git clone https://github.com/Aiesha401/AI-Engineering-Apprenticeship.git
cd commerceops-ai

2. Create a virtual environment
Windows PowerShell:
python -m venv venv

Activate it:
.\venv\Scripts\Activate.ps1

3. Install dependencies
python -m pip install -r requirements.txt

4. Configure environment variables
Create a .env file containing the required API configuration.
Do not commit your .env file or API keys to GitHub.
5. Run the terminal application
python -m mini_projects.commerceops_agent.main

## Running the API
Start the FastAPI application with:
uvicorn mini_projects.commerceops_agent.api:app --reload

The API will be available at:
http://localhost:8000

Swagger documentation:
http://localhost:8000/docs

## Docker

Build the Docker image:
docker build -t commerceops-ai .

Run the container:
docker run --env-file .env -p 8001:8000 commerceops-ai

The API can then be accessed at:
http://localhost:8001

Swagger documentation:
http://localhost:8001/docs

## Deployment

CommerceOps AI is containerized using Docker and deployed on Render.

**Live Application:** https://commerceops-ai.onrender.com/app

**API Documentation:** https://commerceops-ai.onrender.com/docs

## Future Improvements

- Add product-level revenue analytics
- Expand business data and operations
- Add more comprehensive automated tests
- Improve LLM latency and reduce unnecessary model calls
- Add authentication and user-level access control
- Improve frontend experience and responsiveness