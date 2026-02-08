FROM python:3.12-slim AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./
COPY backend/pyproject.toml backend/pyproject.toml
COPY backend/libs/ backend/libs/

RUN uv sync --project backend --no-dev --no-install-project

COPY backend/src/ backend/src/

RUN uv sync --project backend --no-dev


FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

COPY --from=builder /app /app

RUN adduser --disabled-password --no-create-home appuser \
    && mkdir -p /app/data \
    && chown -R appuser:appuser /app/data

USER appuser

EXPOSE 8000

CMD ["/app/.venv/bin/fastapi", "run", "backend/src/cartly/main.py", "--host", "0.0.0.0", "--port", "8000"]
