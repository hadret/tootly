# syntax=docker/dockerfile:1
FROM ghcr.io/astral-sh/uv:0.11.3-python3.13-trixie-slim
LABEL org.opencontainers.image.source=https://github.com/hadret/tootly

ENV UV_PYTHON_DOWNLOADS=never \
    UV_PYTHON=python3.13

WORKDIR /code

COPY pyproject.toml uv.lock /code/
RUN uv sync --frozen
COPY ./tootly /code/app

CMD ["uv", "run", "app/main.py"]
