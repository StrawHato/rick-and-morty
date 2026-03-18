FROM python:3.12-alpine3.17
LABEL maineiner="strawhato"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install requirements.txt
COPY . .