FROM python:3.13.5-alpine3.22

WORKDIR /app

RUN pip install uv


COPY . .

RUN uv sync

EXPOSE 1234

CMD ["uv", "run","main.py"]