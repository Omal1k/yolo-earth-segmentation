FROM python:3.13-slim

WORKDIR /app

RUN apt update && apt install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install uv


COPY . .

RUN uv sync

EXPOSE 1234

CMD ["uv", "run","main.py"]