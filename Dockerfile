# Dockerfile

FROM python:3.11

WORKDIR /pythonExercise1

COPY app/main.py .

CMD ["python", "main.py"]
