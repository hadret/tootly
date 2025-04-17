# syntax=docker/dockerfile:1
FROM ghcr.io/astral-sh/uv:0.6.14-python3.12-bookworm-slim
LABEL org.opencontainers.image.source=https://github.com/hadret/tootly

ENV UV_PYTHON_DOWNLOADS=never \
    UV_PYTHON=python3.12

WORKDIR /code

COPY pyproject.toml uv.lock /code/
RUN uv sync --frozen
COPY ./tootly /code/app

CMD ["uv", "run", "app/main.py"]
