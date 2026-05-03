FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install kafka-python opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp
CMD ["python", "app.py"]
