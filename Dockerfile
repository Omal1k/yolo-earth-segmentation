FROM python:3.13.5-alpine3.22

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install uv


COPY . .

RUN uv sync

EXPOSE 1234

CMD ["uv", "run","main.py"]