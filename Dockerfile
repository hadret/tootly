# syntax=docker/dockerfile:1
FROM python:3.10-slim
LABEL org.opencontainers.image.source https://github.com/hadret/tweetly

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY ./tweetly /code/app

CMD ["python", "app/main.py"]
