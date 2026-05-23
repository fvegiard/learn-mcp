FROM python:3.14-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    "mcp[cli]>=1.6.0" \
    qdrant-client \
    sentence-transformers

COPY server.py /app/server.py
COPY references.json /app/references.json

WORKDIR /app
EXPOSE 8001

HEALTHCHECK --interval=30s --timeout=10s --retries=3 --start-period=15s \
    CMD curl -sfI http://127.0.0.1:8001/sse || exit 1

CMD ["python", "server.py"]