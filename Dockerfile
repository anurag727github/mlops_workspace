FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY hello.py .
COPY test_hello.py .
COPY monitor_data.py .

CMD ["python", "hello.py"]