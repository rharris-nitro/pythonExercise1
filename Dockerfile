# Dockerfile

FROM python:3.11 AS base

FROM base AS main

WORKDIR /app

COPY app/ .

ENTRYPOINT ["python"]
CMD ["app/main.py"]


FROM main AS main-dev
RUN pip3 install --no-cache-dir debugpy==1.8.0 -t /tmp


FROM main AS test

COPY tests/test_main.py .

COPY requirements.test.txt .
RUN pip install -r requirements.test.txt

ENTRYPOINT ["pytest"]
CMD ["test_main.py"]
