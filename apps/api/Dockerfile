FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /workspace

ENV UV_PROJECT_ENVIRONMENT=/opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY pyproject.toml uv.lock ./

COPY apps/api/pyproject.toml ./apps/api/pyproject.toml
COPY packages/shared/pyproject.toml ./packages/shared/pyproject.toml

RUN uv sync --frozen --package truck-api --no-install-workspace

COPY apps/api ./apps/api
COPY packages/shared ./packages/shared

RUN uv sync --frozen --package truck-api

CMD ["uvicorn", "apps.api.app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--reload-dir", "/workspace/apps"]