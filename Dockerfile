# Dockerfile

FROM python:3.11 AS base

FROM base AS main

    WORKDIR /pythonExercise1

    COPY ./app/main.py .

    CMD ["python", "main.py"]

FROM base AS test

    COPY app/ app/
    COPY tests/test_main.py .

    COPY requirements-test.txt .
    RUN pip install -r requirements-test.txt

    CMD ["pytest", "test_main.py"]
