# syntax=docker/dockerfile:1
FROM python:3.10-slim
LABEL org.opencontainers.image.source https://github.com/hadret/tweetly

WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
