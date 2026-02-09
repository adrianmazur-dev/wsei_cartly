FROM python:3.12-slim AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml ./
COPY pyproject.toml pyproject.toml
COPY libs/ libs/

RUN uv sync --no-dev --no-install-project

COPY src/ src/

RUN uv sync --no-dev


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

ENV PYTHONPATH=/app/src
CMD ["/app/.venv/bin/uvicorn", "cartly.main:app", "--host", "0.0.0.0", "--port", "8000"]
