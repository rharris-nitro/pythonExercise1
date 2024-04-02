# Dockerfile

FROM python:3.11 AS base

FROM base AS main

WORKDIR /app

COPY app/ .

ENTRYPOINT ["python"]
CMD ["main.py"]


FROM main AS main-dev
RUN pip3 install debugpy==1.8.0 -t /tmp


FROM main-dev AS test

COPY tests/test_main.py .

COPY requirements.test.txt .
RUN pip install -r requirements.test.txt

ENTRYPOINT ["pytest"]
