FROM python:3.13-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY server.py /app/server.py
COPY merge_refs.py /app/merge_refs.py
COPY data/ /app/data/
COPY references.json /app/references.json

VOLUME /root/.cache/huggingface

EXPOSE 8001

HEALTHCHECK --interval=30s --timeout=10s --retries=3 --start-period=15s \
    CMD curl -sf --max-time 5 http://127.0.0.1:8001/sse > /dev/null 2>&1 || exit 1

CMD ["python", "server.py"]