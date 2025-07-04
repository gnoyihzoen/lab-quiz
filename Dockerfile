FROM python:3.12-slim

WORKDIR /app

COPY web/requirements.txt .
RUN apt-get update && apt-get install -y git && pip install --no-cache-dir -r requirements.txt && rm -rf /var/lib/apt/lists/*

COPY web /app
