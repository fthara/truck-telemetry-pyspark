FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /workspace

COPY pyproject.toml uv.lock ./
COPY apps/spark ./apps/spark
COPY packages/shared ./packages/shared

RUN uv sync --frozen --package truck-spark

ENV PATH="/workspace/.venv/bin:$PATH"

WORKDIR /workspace/apps/spark

CMD ["python", "jobs/consume_trucks.py"]