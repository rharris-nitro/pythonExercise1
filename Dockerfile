# Dockerfile

FROM python:3.11 AS base

FROM base AS main

WORKDIR /pythonExercise1

COPY app/ app/

COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["python", "app/main.py"]


FROM main AS test

COPY tests/test_main.py .

COPY requirements.test.txt .
RUN pip install -r requirements.test.txt

CMD ["pytest", "test_main.py"]
