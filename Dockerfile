# Dockerfile

FROM python:3.11 AS base

FROM base AS main

    WORKDIR /pythonExercise1

    COPY ./app /pythonExercise1/app

    ENTRYPOINT ["python"]
    CMD ["-m", "app.main"]


FROM main AS dev

    COPY ./tests /pythonExercise1/tests
    COPY requirements.test.txt .

    RUN pip install -r requirements.test.txt && \
        pip install debugpy==1.8.0 -t /tmp
