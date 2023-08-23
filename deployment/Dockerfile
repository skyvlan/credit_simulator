FROM python:3.8-slim

RUN apt-get update
RUN pip install poetry

WORKDIR /app

COPY poetry.lock pyproject.toml main.py /app/
RUN poetry install --no-root --no-dev


COPY ./src /app/src/
COPY ./bin /app/bin/
COPY ./tests /app/tests/



CMD echo "test"

