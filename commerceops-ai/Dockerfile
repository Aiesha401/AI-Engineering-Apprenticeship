FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY mini_projects/commerceops_agent ./mini_projects/commerceops_agent

CMD ["python", "mini_projects/commerceops_agent/main.py"]