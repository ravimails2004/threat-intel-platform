FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
