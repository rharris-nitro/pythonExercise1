FROM python:3.11

WORKDIR /pythonExercise1

COPY requirements.txt .

RUN pip install -r /pythonExercise1/requirements.txt

COPY . .

CMD ["python", "main.py"]
