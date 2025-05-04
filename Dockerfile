FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["uvicorn", "studentSurvey:app", "--host", "0.0.0.0", "--port", "8080"]