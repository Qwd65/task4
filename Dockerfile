FROM python:3.9-slim

WORKDIR /app

COPY data.csv .
COPY app.py .

RUN pip install pandas

CMD ["python", "app.py"]
