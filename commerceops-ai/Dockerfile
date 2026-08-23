FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY mini_projects/commerceops_agent ./mini_projects/commerceops_agent

CMD ["sh", "-c", "uvicorn mini_projects.commerceops_agent.api:app --host 0.0.0.0 --port ${PORT:-8000}"]