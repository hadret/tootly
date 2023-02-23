# syntax=docker/dockerfile:1
FROM python:3.11-slim
LABEL org.opencontainers.image.source https://github.com/hadret/tootly

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY ./tootly /code/app

CMD ["python", "app/main.py"]
